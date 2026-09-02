from __future__ import annotations

import hashlib
import importlib
import json
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace


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
        if name in {'context_engine', 'lab_tools_project'} or name.startswith('api_wire_'):
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
    workspace = target_root.parent / 'hidden_eval_workspace'
    if workspace.exists():
        shutil.rmtree(workspace)
    project = workspace / 'project'
    project.mkdir(parents=True)
    (project / 'alias.txt').write_text('Ωß中', encoding='utf-8')
    (project / 'range.txt').write_text('one\ntwo\nthree\nfour\nfive\nsix\n', encoding='utf-8')
    (project / 'ok.txt').write_text('abcdefghij', encoding='utf-8')

    sys.path.insert(0, str(target_root))
    try:
        reset_modules()
        ce = importlib.import_module('context_engine')
        ltp = importlib.import_module('lab_tools_project')
        results: list[dict[str, object]] = []

        def stale_authority() -> None:
            assert actual_hash == expected_tree_hash, f'unacknowledged target bytes: expected {expected_tree_hash}, got {actual_hash}'

        def alias_byte() -> None:
            r = ce.read_file(ce.FileReadRequest(path='alias.txt', base_root=str(project), max_bytes=9))
            assert len(r.content.encode('utf-8')) <= 9, r.content
            assert r.content == 'Ωß中', r.content

        def range_case() -> None:
            r = ce.read_file(ce.FileReadRequest(path='range.txt', base_root=str(project), start_line=3, end_line=5, max_bytes=100))
            assert r.content == 'three\nfour\nfive', repr(r.content)
            assert (r.slice.start_line, r.slice.end_line) == (3, 5), r.slice

        def fallback_case() -> None:
            dep = SimpleNamespace(error_cls=RuntimeError, get_project_root=lambda project_id: project, read_file=ce.read_file)
            r = ltp._project_read_many_payload({'project_id':'HIDDEN','paths':['ok.txt','missing.txt'],'max_bytes_each':4}, dep)
            assert (r['read_count'], r['error_count']) == (1, 1), r
            assert 'error' not in r['files']['ok.txt'], r
            assert 'error' in r['files']['missing.txt'], r
            assert len(r['files']['ok.txt']['content'].encode('utf-8')) <= 4, r

        def evidence_parent() -> None:
            dep = SimpleNamespace(
                normalize_project_path=lambda payload: str(payload.get('path','')),
                project_root_path=lambda project_id: str(project),
                context_wrap=lambda thunk: thunk(),
                read_file=ce.read_file,
            )
            r = ltp._project_files_read_payload({'project_id':'HIDDEN','path':'range.txt','start_line':3,'end_line':5,'max_bytes':100}, dep)
            data = r.to_dict() if hasattr(r, 'to_dict') else r
            assert data['ok'] is True
            assert data['content'] == 'three\nfour\nfive', data
            assert data['slice']['start_line'] == 3 and data['slice']['end_line'] == 5, data

        for name, fn in [
            ('H-STALE-AUTH', stale_authority),
            ('H-ALIAS-BYTE', alias_byte),
            ('H-RANGE', range_case),
            ('H-FALLBACK', fallback_case),
            ('H-EVIDENCE', evidence_parent),
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
        raise SystemExit('usage: HIDDEN_EVALUATOR_RUNNER_V0_1.py TARGET_ROOT EXPECTED_TREE_HASH')
    report = evaluate(Path(sys.argv[1]), sys.argv[2])
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(0 if report['failed'] == 0 else 1)
