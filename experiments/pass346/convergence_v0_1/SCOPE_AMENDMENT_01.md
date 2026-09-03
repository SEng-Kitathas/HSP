# Convergence Scope Amendment 01 — Active Power Read-Many Parent

Status: **AUTHORIZED BEFORE NEW-PATH MUTATION**
Process authority: Rahl Engineering Canonical SOP R4.2 C24/C25/E13.

## Discovery
After the first six-path embodiment passed semantic regressions and mutation-scope review, parent-requalification inspection found another active parent reuse seam in `power_routes.py`:

`_read_many_file()` calls the same core `context_engine.read_file()` and currently tries to read top-level `size_bytes` / `truncated` fields that the core response does not define. It therefore returns default `size_bytes=0` / `truncated=False` on successful children.

This is the same evidence-referent class of defect and cannot be knowingly excluded from a convergence claim covering active bounded read-many surfaces.

## Amended authorized mutation scope
Original six authorized paths remain authorized. Add:
- `power_routes.py`

No other path is authorized by this amendment.

## Design correction
Centralize validation/projection of successful core read evidence in one public core helper in `context_engine.py`. Both:
- `lab_tools_project.ReadManyFileEntry.from_read_result`, and
- `power_routes._read_many_file`
shall consume the same validated child evidence.

The helper shall fail closed on absent/malformed/inconsistent slice evidence and shall return only established parent projection values: content, returned bytes, and byte-budget truncation.

## Verification delta
Add regression coverage for the power read-many parent on an unbounded CRLF source and for fail-closed handling of malformed child evidence where practical. Re-run the complete convergence/regression stack and mutation-scope review after the amendment.
