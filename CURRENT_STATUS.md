# Current Status

- Mode: BUILD-COMMIT.
- Active role: R1 Conservative Auditor during recovery; R5 Reality Pressure resumes after an admissible arm-local implementation exists.
- Mainline: Pass 345 remains the last clean mainline checkpoint. HSP v0 remains research-only.
- Pass 346 v0.1 remains a retained stale-currentness scar; v0.2 is the active frozen experiment boundary.
- Live receiver disk was rechecked against all 60 v0.2 manifest-listed files on 2026-09-02: 60 same, 0 changed, 0 missing.
- Both isolated arm targets still match `target_snapshot_v0_2`: 60 source files each, 0 changed/missing/extra excluding runtime pycache.
- Hidden evaluator SHA-256 `afa6c7c06c66bf79127d0098b44ca49ffa1715e77b91107279e9f3d9e262b9cf`; no same-hash copy exists inside either arm.
- Initial independent-lane inference `job-59c99e6569a7` completed rc=0. Additional locally persisted cycles recovered after assistant readback loss: repair-01 `job-62f3c03ea7b3`, distilled repair-02 `job-ca3475050e5a`, Arm A 14B rescue `job-e6828252570f`, Arm B 14B rescue `job-34b2825c9bd1`; all completed rc=0.
- All recovered proposal/repair/rescue outputs are retained as failed evidence. None is admissible as written and no proposal patch has been applied to either arm.
- Fresh visible evaluator replay on each unchanged arm: **1 passed / 5 failed**. Only full-read control passes. Current failures: ranged-read `NameError: s`, UTF-8 byte ceiling, project base-root escape, missing `FileReadRequest` in parent project-file read, and the same missing import blocking `read_many` qualification.
- Accepted Arm A implementation: none. Accepted Arm B implementation: none. Arm seals: none. Hidden evaluation: not run. CSC: not run. Pass 346 winner/adjudication: none.
- Operational scar is now explicit: local execution completion, local artifact persistence, assistant readback, artifact registration, chat rendering, and remote synchronization are separate states. Readback/render failure does not prove local failure and does not authorize blind rerun.
- Detailed recovery record: `experiments/pass346/WORKSPACE_RECOVERY_AUDIT_2026-09-02.md`.
- Next step: generate genuinely admissible repairs independently in each arm, apply only to their own targets, run visible/domain qualification, seal both, then reveal the hidden evaluator.
