# Pass 346 Workspace Recovery Audit — 2026-09-02

Status: VERIFIED LOCAL FORENSIC RECOVERY; NO ARM IMPLEMENTATION ACCEPTED; HIDDEN EVALUATOR UNOPENED

## Why this audit exists

Assistant-facing readback became unreliable while server-side work continued on the operator's dev machine. This audit reconstructs what actually persisted locally before any retry or promotion decision.

## Recovered topology

- HSP control/repository project: `E:\new pc\AI_Pushes_Sandbox\projects\HSP`
- Pass 346 isolated workspace: `E:\new pc\AI_Pushes_Sandbox\projects\hsp-pass346-prereg-pcmmad-bounded-read`
- Arm A target: `arms_v0_2/arm_a/target`
- Arm B target: `arms_v0_2/arm_b/target`
- Hidden evaluator remains at `evaluator/HIDDEN_PERTURBATIONS.json` in the sibling Pass 346 workspace.

## Source-state verification

A fresh local hash audit compared both isolated arm targets against `target_snapshot_v0_2` while excluding only runtime `__pycache__`/`.pyc` byproducts.

- Frozen source files: 60
- Arm A: 60 files; **0 changed, 0 missing, 0 extra**
- Arm B: 60 files; **0 changed, 0 missing, 0 extra**
- Hidden evaluator SHA-256: `afa6c7c06c66bf79127d0098b44ca49ffa1715e77b91107279e9f3d9e262b9cf`
- Hidden evaluator copies inside Arm A: none
- Hidden evaluator copies inside Arm B: none

The live receiver disk tree was also rechecked against all 60 v0.2 manifest entries and matched **60/60** with no missing or changed manifest-listed file.

## Recovered execution sequence

### Initial isolated inference
- Job: `job-59c99e6569a7`
- Status: completed, rc=0, stderr empty
- Arm A raw response SHA-256: `9d7f95dd68067bbec5b55d9af971c5d438a55dbb246ffc92789c7ac9a73a67dc`
- Arm B raw response SHA-256: `e67987b6ffe483fe5e8623a87e6103bd401d0338bb48cd882ee5b2ed6252095b`
- No patch applied.

### Arm-local repair cycle 01
- Job: `job-62f3c03ea7b3`
- Status: completed, rc=0
- Runner: `tools/pass346_run_arm_repair01.py`
- Arm A repair text SHA-256: `dbe5a7dd42e790c80342c31afe4a9a13a508abbcc9c52b467257bbff7c6540fc`
- Arm B repair text SHA-256: `cfc8c9f107786ac35b55b36afc96c442d2aa75198ef242af776909b4debd96ce`
- These normalized text hashes match the original in-memory proposal texts recorded by the first run: the repair cycle effectively repeated the rejected proposals.
- No patch applied.

### Distilled repair cycle 02
- Job: `job-ca3475050e5a`
- Status: completed, rc=0
- Runner: `tools/pass346_run_arm_repair02_distilled.py`
- Arm A raw SHA-256: `51cbcb1768e3fe181dc054abac6d36e229bf172db504ce96262c28c9fdf886a7`
- Arm B raw SHA-256: `0ee70b031e7305baf5604d8af04408e2e3cba169a21495a3009d0ac9ac030e32`
- No patch applied.

### 14B rescue cycle
- Arm A job: `job-e6828252570f`, rc=0, model alias `hsp-pass346-arm-a-14b`, local model ID `qwen2.5-coder-14b-q4kl`
- Arm B job: `job-34b2825c9bd1`, rc=0, model alias `hsp-pass346-arm-b-14b`, local model ID `qwen2.5-coder-14b-q4kl`
- Arm A raw SHA-256: `d88d387c4d9dbdcd8461cffb8cc25eafa2f4a60047b44fb112020c182958885b`
- Arm B raw SHA-256: `c3614008f1ded4ee2dd4e61ae463bbece57881621be18d670e56127e90090844`
- No patch applied.

All recovered job records show `artifact_registration_status: not_attempted`; the outputs persisted locally in arm control directories and execution logs but were not registered as result artifacts.

## Proposal adjudication

None of the recovered proposals is admissible for application as written.

### Arm A
- Initial and repair-01 proposals leave the undefined range variable `s` and UTF-8 byte-ceiling defect intact.
- Distilled repair-02 still uses undefined `s`, character slicing, and adds tests that are not grounded in the real call surface.
- 14B rescue is effectively a no-op against the defective mechanism.

### Arm B
- Initial and repair-01 proposals add `global s` without defining it and overclaim contract evidence/closure before execution.
- Distilled repair-02 references range variables/`max_bytes` before they are established and still does not implement a valid UTF-8 byte ceiling.
- 14B rescue proposes `target.is_text_file()` (not an existing `pathlib.Path` method), retains character slicing, and does not repair the undefined range variables.

Therefore all proposal artifacts are **retained as failed evidence**, not applied, not erased, and not promoted.

## Fresh visible-evaluator replay

The unchanged Arm A and Arm B targets were each replayed against `VISIBLE_EVALUATOR_V0_1.py`.

Both produced the same result: **1 passed / 5 failed**.

Passed:
- `W3_full_read_control`

Failed:
- `W1_range_core`: `NameError: name 's' is not defined`
- `W2_utf8_byte_ceiling`: 6 UTF-8 bytes returned under `max_bytes=3`
- `project_root_escape_rejected`: project-relative `../outside.txt` can escape the supplied `base_root` while remaining inside a broader allowed root
- `parent_project_files_read_surface`: `NameError: name 'FileReadRequest' is not defined`
- `read_many_child_failure_preserved`: same missing `FileReadRequest` prevents truthful parent-path qualification

This expands the current visible defect surface beyond the two originally emphasized witnesses; it does not retroactively rewrite the preregistration.

## Readback scar independently reproduced during recovery

Two current examples demonstrate asymmetric success/readback:

1. `getProjectExecutionOutput` returned HTTP 500 for completed job `job-ca3475050e5a`, while direct bounded reading of its persisted `system/logs/execution/.../stdout.log` succeeded and matched the recorded job output.
2. assistant-facing ranged `readProjectFile` against the frozen `context_engine.py` returned HTTP 500, while project search and direct server-side Python read the exact bytes successfully.

These observations justify the project rule that local execution/persistence, assistant readback, chat rendering, registration, and remote sync are separate states.

## Current experiment boundary

- Independent inference/repair attempts: completed and preserved.
- Accepted Arm A implementation: **NO**.
- Accepted Arm B implementation: **NO**.
- Source mutation in either arm: **NO**.
- Arm seals: **NO**.
- Hidden evaluator reveal: **NO**.
- CSC: **NO**.
- Pass 346 winner/adjudication: **NO**.

Pass 346 remains at the arm-local implementation gate. The correct next move is not to rerun because readback failed; it is to produce an admissible repair independently in each arm, apply it only to its own isolated target, run visible/domain qualification, and seal both before hidden-evaluator reveal.
