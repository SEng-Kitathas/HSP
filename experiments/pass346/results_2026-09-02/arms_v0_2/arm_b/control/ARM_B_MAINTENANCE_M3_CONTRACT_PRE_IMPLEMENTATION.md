# Arm B — Maintenance M3 Holon Delta Contract

Status: **QUALIFIED MAINTENANCE DELTA; NOT YET EMBODIED**
Task: add optional `tail_lines=N` request mode that returns the final N logical lines while preserving the existing byte ceiling and exact project-root authority.
Parent implementation seal: `4b59e5a846c5866d7b3153e683b5e0801cdc3726b1d84c109fea446282211e41`
Parent embodied contract: `ARM_B_BOUNDED_READ_HOLON_CONTRACT_EMBODIED.md`

## Referent / scope
Exact referent remains Arm B’s sealed isolated target. This maintenance delta does not authorize mutation of the live receiver or Arm A.

## New capability
`tail_lines` is an alternative logical-line selection mode. If supplied, it selects the final N elements of the incumbent `str.splitlines()` logical-line referent before the existing UTF-8 byte ceiling is applied.

## New preconditions / forbidden ambiguity
- `tail_lines` must be a positive integer when supplied.
- `tail_lines` MUST NOT be combined with `start_line` or `end_line`; ambiguous precedence is rejected rather than silently invented.
- `tail_lines > total logical lines` returns all available logical lines.
- empty file remains a successful empty read under valid authority.

## Authority/state/effect preservation
- Path authority is unchanged: the exact supplied `base_root` remains the confinement boundary.
- Read-only effect and no-atomic-snapshot nonclaim are unchanged.
- UTF-8 `max_bytes` remains a hard ceiling on returned content after line selection.
- No retry/fallback authority is added.

## Required seam propagation
The new mode must be represented and requalified across:
1. core `context_engine.FileReadRequest` / `read_file`;
2. HTTP wire `api_wire_context.ProjectFilesReadRequest`;
3. HTTP `/project/files/read` route lowering;
4. lab-native `lab_tools_project.ProjectFilesReadRequest` and `_project_files_read_payload`;
5. imported Custom GPT `ProjectFilesReadRequest` schema surfaces.

Core-only support is whole-level failure because the real user consequence is exposed through parent request surfaces.

## Invariants
M3-L1: selected logical lines are the final N lines under `splitlines()` semantics.
M3-L2: `len(content.encode("utf-8")) <= max_bytes` after tail selection.
M3-L3: exact project-root confinement remains unchanged.
M3-S1: HTTP and lab-native parent requests transport the same `tail_lines` referent to core.
M3-S2: imported action schema exposes `tail_lines` as optional integer `minimum: 1` without relaxing `additionalProperties: false`.
M3-W1: `tail_lines` + explicit start/end is rejected, not precedence-guessed.
M3-W2: prior range/full-read/read-many behavior must remain regression-green.

## Evidence state before mutation
- Parent B initial implementation: **VISIBLE-QUALIFIED + initial hidden hostile 5/5**.
- Maintenance task behavior: **UNKNOWN / NOT YET EMBODIED**.
- Cross-arm maintenance evidence: **NOT USED**.
- Hidden hostile concrete values are evaluator-side and are not required for this implementation delta.

## Planned lowering
Use the existing request dataclasses and explicit branch structure; add no new persistent abstraction unless the mode interaction becomes clearer because of it. Tail selection uses native list slicing, then the already-qualified UTF-8 byte-bound helper. Propagate one optional field through each admitted parent seam and both imported schema copies.

## Verification plan
- extend Arm B contract tests for tail selection, byte bound, ambiguity rejection, parent lab surface, wire parsing, and schema exposure;
- rerun all prior B tests;
- rerun visible evaluator;
- compile all target Python;
- seal maintenance bytes;
- only then run common maintenance evaluator and unchanged hidden hostile suite against the maintenance seal.

## Nonclaims
No claim yet that M3 works, that the live imported action has been updated, that maintenance proves HSP superiority, or that production promotion is warranted.
