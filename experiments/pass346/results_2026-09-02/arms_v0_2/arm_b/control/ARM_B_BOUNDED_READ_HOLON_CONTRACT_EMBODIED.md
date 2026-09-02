# Arm B — Bounded Project-File Read Holon Contract — Embodied State

Status: **EMBODIED + VISIBLE-QUALIFIED; NOT HIDDEN-TESTED; NOT PROMOTED**
Parent contract: `ARM_B_BOUNDED_READ_HOLON_CONTRACT_PRE_IMPLEMENTATION.md`
Parent SHA-256: `0ae30bdb4695f6514ad1590715d23f60eb12aa56f5ac042d5b03e13803ad4501`
Initial seal SHA-256: `4b59e5a846c5866d7b3153e683b5e0801cdc3726b1d84c109fea446282211e41`

## Embodiment correspondence
- exact project-root authority -> `_path_is_within` + `resolve_user_path` confines a candidate to supplied `base_root` when present;
- line-window semantics -> `read_file` uses 1-based inclusive slicing over `splitlines()` and preserves incumbent full-read behavior;
- UTF-8 byte ceiling -> `_bounded_utf8_text` clips encoded bytes and decodes only a valid prefix;
- parent single-read binding -> explicit `FileReadRequest` import/use in `lab_tools_project`;
- parent child-failure preservation -> `_project_read_one_many` catches `ContextPlaneError` and records error entry;
- parent success evidence -> `ReadManyFileEntry.from_read_result` derives returned UTF-8 byte count and truncation from actual returned content/source metadata.

## Closure after visible qualification
- C1 path resolution: **ESTABLISHED in arm-local + visible tests**;
- C2 line selection: **ESTABLISHED in arm-local + visible tests**;
- C3 UTF-8 byte bound: **ESTABLISHED in arm-local + visible tests**;
- C4 core response: **ESTABLISHED for tested scope**;
- C5 parent single read: **ESTABLISHED for tested scope**;
- C6 parent multi-read: **ESTABLISHED for tested mixed-success scope**;
- C7 error projection: **ESTABLISHED for tested context-plane missing-child failure**.

Whole closure: **VISIBLE-QUALIFIED, not hidden-qualified**.

## Evidence delta
- Arm-local contract tests: **9/9 PASS**.
- Common visible evaluator: **6/6 PASS**.
- Compile check: **PASS**.
- Hidden evaluator: **UNKNOWN / UNREAD at seal time**.
- Cross-arm implementation evidence used before seal: **NO**.
- Live receiver mutation: **NO**.

## Outcome stages for the tested visible scope
- attempted: **VERIFIED**;
- established: **VERIFIED for visible/arm-local cases**;
- observed: **VERIFIED via returned test results**;
- acknowledged: **VERIFIED at tested parent function seams, not at live deployment**.

## Assurance ceiling / nonclaims
The arm is an isolated implementation candidate that survived its declared visible qualification. It is not hidden-tested yet, not CSC-reviewed, not a production patch, not evidence of atomic snapshot behavior, and not general evidence that HSP is superior.
