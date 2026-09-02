from __future__ import annotations

import hashlib
import importlib
import json
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace

from flask import Flask


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relevant_files(root: Path):
    for path in sorted(root.rglob('*')):
        if not path.is_file():
            continue
        if '__pycache__' in path.parts or '.pcmmad_sync_runs' in path.parts or path.suffix == '.pyc':
            continue
        yield path


def tree_hash(root: Path) -> str:
    h = hashlib.sha256()
    for path in relevant_files(root):
        rel = path.relative_to(root).as_posix()
        h.update(rel.encode('utf-8') + b'\0' + sha256_file(path).encode('ascii') + b'\n')
    return h.hexdigest()


def reset_modules() -> None:
    for name in list(sys.modules):
        if name in {'context_engine', 'lab_tools_project', 'context_routes', 'api_wire_context'} or name.startswith('api_wire_'):
            sys.modules.pop(name, None)


def check(name, fn, results):
    try:
        fn()
        results.append({'name': name, 'ok': True})
    except Exception as exc:
        results.append({'name': name, 'ok': False, 'error': f'{type(exc).__name__}: {exc}'})


def evaluate(target_root: Path, expected_tree_hash: str) -> dict[str, object]:
    target_root = target_root.resolve()
    actual_hash = tree_hash(target_root)
    workspace = target_root.parent / 'maintenance_m3_eval_workspace'
    shutil.rmtree(workspace, ignore_errors=True)
    project = workspace / 'project'
    project.mkdir(parents=True)
    (project / 'tail.txt').write_text('one\nΩmega\nthree\nfour\nfive\n', encoding='utf-8')
    (workspace / 'outside.txt').write_text('outside', encoding='utf-8')

    sys.path.insert(0, str(target_root))
    try:
        reset_modules()
        ce = importlib.import_module('context_engine')
        awc = importlib.import_module('api_wire_context')
        ltp = importlib.import_module('lab_tools_project')
        cr = importlib.import_module('context_routes')
        results: list[dict[str, object]] = []

        def seal_identity() -> None:
            assert actual_hash == expected_tree_hash, f'unacknowledged maintenance bytes: expected {expected_tree_hash}, got {actual_hash}'

        def core_tail() -> None:
            r = ce.read_file(ce.FileReadRequest(path='tail.txt', base_root=str(project), tail_lines=2, max_bytes=100))
            assert r.content == 'four\nfive', repr(r.content)
            assert (r.slice.start_line, r.slice.end_line) == (4, 5), r.slice

        def byte_ceiling_after_tail() -> None:
            r = ce.read_file(ce.FileReadRequest(path='tail.txt', base_root=str(project), tail_lines=4, max_bytes=8))
            assert len(r.content.encode('utf-8')) <= 8, repr(r.content)
            r.content.encode('utf-8').decode('utf-8')

        def tail_overflow_all_lines() -> None:
            r = ce.read_file(ce.FileReadRequest(path='tail.txt', base_root=str(project), tail_lines=99, max_bytes=1000))
            assert r.content == 'one\nΩmega\nthree\nfour\nfive', repr(r.content)
            assert (r.slice.start_line, r.slice.end_line) == (1, 5), r.slice

        def ambiguous_mode_rejected() -> None:
            try:
                ce.read_file(ce.FileReadRequest(path='tail.txt', base_root=str(project), start_line=2, tail_lines=2, max_bytes=100))
            except ValueError:
                return
            raise AssertionError('tail_lines + start_line was silently accepted')

        def lab_parent() -> None:
            dep = SimpleNamespace(
                normalize_project_path=lambda payload: str(payload.get('path', '')),
                project_root_path=lambda project_id: str(project),
                context_wrap=lambda thunk: thunk(),
                read_file=ce.read_file,
            )
            r = ltp._project_files_read_payload({'project_id':'M3','path':'tail.txt','tail_lines':2,'max_bytes':100}, dep)
            data = r.to_dict() if hasattr(r, 'to_dict') else r
            assert data['content'] == 'four\nfive', data
            assert data['slice']['start_line'] == 4 and data['slice']['end_line'] == 5, data

        def wire_and_http_parent() -> None:
            req = awc.ProjectFilesReadRequest.from_json({'project_id':'M3','path':'tail.txt','tail_lines':2,'max_bytes':100})
            assert req.tail_lines == 2
            cr._auth = lambda: None
            cr.project_root_path = lambda project_id: str(project)
            app = Flask('m3-eval')
            app.register_blueprint(cr.context_bp)
            client = app.test_client()
            response = client.post('/project/files/read', json={'project_id':'M3','path':'tail.txt','tail_lines':2,'max_bytes':100})
            assert response.status_code == 200, (response.status_code, response.get_data(as_text=True))
            data = response.get_json()
            assert data['content'] == 'four\nfive', data
            assert data['slice']['start_line'] == 4 and data['slice']['end_line'] == 5, data

        def imported_schema_exposure() -> None:
            for name in ('pcmmad_lab_action_schema_v10_3_pcmmad_native_protocol_compact_30_router.json','pcmmad_lab_action_schema_ACTIVE.json'):
                schema = json.loads((target_root / name).read_text(encoding='utf-8-sig'))
                request_schema = schema['components']['schemas']['ProjectFilesReadRequest']
                prop = request_schema['properties']['tail_lines']
                assert prop['type'] == 'integer' and prop['minimum'] == 1, prop
                assert request_schema['additionalProperties'] is False

        def authority_still_confined() -> None:
            try:
                ce.read_file(ce.FileReadRequest(path='../outside.txt', base_root=str(project), tail_lines=1, max_bytes=100))
            except Exception:
                return
            raise AssertionError('tail_lines path escaped exact project root')

        for name, fn in [
            ('M3-SEAL-IDENTITY', seal_identity),
            ('M3-CORE-TAIL', core_tail),
            ('M3-BYTE-CEILING', byte_ceiling_after_tail),
            ('M3-TAIL-OVERFLOW', tail_overflow_all_lines),
            ('M3-AMBIGUITY', ambiguous_mode_rejected),
            ('M3-LAB-PARENT', lab_parent),
            ('M3-WIRE-HTTP', wire_and_http_parent),
            ('M3-IMPORTED-SCHEMA', imported_schema_exposure),
            ('M3-PATH-AUTHORITY', authority_still_confined),
        ]:
            check(name, fn, results)
        passed = sum(1 for item in results if item['ok'])
        return {'target': str(target_root), 'expected_tree_hash': expected_tree_hash, 'actual_tree_hash': actual_hash, 'passed': passed, 'failed': len(results)-passed, 'tests': results}
    finally:
        if str(target_root) in sys.path:
            sys.path.remove(str(target_root))
        reset_modules()
        shutil.rmtree(workspace, ignore_errors=True)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: MAINTENANCE_M3_EVALUATOR_V0_1.py TARGET_ROOT EXPECTED_TREE_HASH')
    report = evaluate(Path(sys.argv[1]), sys.argv[2])
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(0 if report['failed'] == 0 else 1)
