from __future__ import annotations

import importlib
import json
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace


def _reset_modules() -> None:
    for name in list(sys.modules):
        if name in {"context_engine", "lab_tools_project"} or name.startswith("api_wire_"):
            sys.modules.pop(name, None)


def _check(name: str, fn, results: list[dict[str, object]]) -> None:
    try:
        fn()
        results.append({"name": name, "ok": True})
    except Exception as exc:
        results.append({"name": name, "ok": False, "error": f"{type(exc).__name__}: {exc}"})


def evaluate(target_root: Path) -> dict[str, object]:
    target_root = target_root.resolve()
    workspace = target_root.parent / "visible_eval_workspace"
    if workspace.exists():
        shutil.rmtree(workspace)
    root = workspace / "project"
    root.mkdir(parents=True)
    (root / "sample.txt").write_text("alpha\nbéta\ngamma\n", encoding="utf-8")
    (root / "utf8.txt").write_text("ééé", encoding="utf-8")
    (workspace / "outside.txt").write_text("outside", encoding="utf-8")

    sys.path.insert(0, str(target_root))
    try:
        _reset_modules()
        ce = importlib.import_module("context_engine")
        ltp = importlib.import_module("lab_tools_project")
        results: list[dict[str, object]] = []

        def range_core() -> None:
            r = ce.read_file(ce.FileReadRequest(path="sample.txt", base_root=str(root), start_line=2, end_line=2, max_bytes=100))
            assert r.ok is True
            assert r.content == "béta", repr(r.content)
            assert r.slice.start_line == 2 and r.slice.end_line == 2

        def byte_ceiling() -> None:
            r = ce.read_file(ce.FileReadRequest(path="utf8.txt", base_root=str(root), max_bytes=3))
            actual = len(r.content.encode("utf-8"))
            assert actual <= 3, f"returned {actual} UTF-8 bytes under max_bytes=3: {r.content!r}"

        def full_read_control() -> None:
            r = ce.read_file(ce.FileReadRequest(path="sample.txt", base_root=str(root), max_bytes=1000))
            assert r.content == "alpha\nbéta\ngamma\n"

        def project_root_escape_rejected() -> None:
            try:
                ce.read_file(ce.FileReadRequest(path="../outside.txt", base_root=str(root), max_bytes=100))
            except Exception:
                return
            raise AssertionError("project-relative read escaped base_root without rejection")

        def parent_tool_surface() -> None:
            dep = SimpleNamespace(
                normalize_project_path=lambda payload: str(payload.get("path", "")),
                project_root_path=lambda project_id: str(root),
                context_wrap=lambda thunk: thunk(),
                read_file=ce.read_file,
            )
            r = ltp._project_files_read_payload(
                {"project_id": "VISIBLE-EVAL", "path": "sample.txt", "start_line": 2, "end_line": 2, "max_bytes": 100},
                dep,
            )
            data = r.to_dict() if hasattr(r, "to_dict") else r
            assert data["ok"] is True
            assert data["content"] == "béta", data
            assert data["slice"]["start_line"] == 2 and data["slice"]["end_line"] == 2

        def read_many_preserves_child_failure() -> None:
            dep = SimpleNamespace(
                error_cls=RuntimeError,
                get_project_root=lambda project_id: root,
                read_file=ce.read_file,
            )
            r = ltp._project_read_many_payload(
                {"project_id": "VISIBLE-EVAL", "paths": ["sample.txt", "missing.txt"], "max_bytes_each": 5}, dep
            )
            assert r["read_count"] == 1 and r["error_count"] == 1, r
            assert "error" not in r["files"]["sample.txt"], r
            assert "error" in r["files"]["missing.txt"], r

        for name, fn in [
            ("W1_range_core", range_core),
            ("W2_utf8_byte_ceiling", byte_ceiling),
            ("W3_full_read_control", full_read_control),
            ("project_root_escape_rejected", project_root_escape_rejected),
            ("parent_project_files_read_surface", parent_tool_surface),
            ("read_many_child_failure_preserved", read_many_preserves_child_failure),
        ]:
            _check(name, fn, results)

        passed = sum(1 for r in results if r["ok"])
        return {"target": str(target_root), "passed": passed, "failed": len(results) - passed, "tests": results}
    finally:
        if str(target_root) in sys.path:
            sys.path.remove(str(target_root))
        _reset_modules()
        if workspace.exists():
            shutil.rmtree(workspace)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: VISIBLE_EVALUATOR_V0_1.py TARGET_ROOT")
    report = evaluate(Path(sys.argv[1]))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(0 if report["failed"] == 0 else 1)
