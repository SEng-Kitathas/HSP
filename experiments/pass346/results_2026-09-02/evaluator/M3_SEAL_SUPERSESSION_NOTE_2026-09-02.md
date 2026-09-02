# Pass 346 M3 Maintenance Seal Supersession Note

Status: **INVALIDATE PRIOR M3 SEALS FOR BYTE-CLEAN ADJUDICATION; PRESERVE AS EVIDENCE**

The first M3 maintenance seals were semantically green but failed byte-clean artifact review.

Affected prior seals:
- Arm A: `ARM_A_MAINTENANCE_M3_SEAL.json` — SHA-256 `37ffe17cefd1f089e335b08d454ea6ba5f3a0375d1591e5967e287534361e92c`
- Arm B: `ARM_B_MAINTENANCE_M3_SEAL.json` — SHA-256 `08e2fe31b2f456688d273ee1bd8376eb3e624e9f2460754be6b8efab85a32b6d`

Failure mechanism:
- `pcmmad_lab_action_schema_ACTIVE.json` began with UTF-8 BOM and 4,568 CRLF line endings.
- The text-edit path decoded in universal-newline mode and wrote LF, normalizing the entire file while inserting the intended five-line `tail_lines` property block.
- Frozen/initial bytes: 483,448 bytes; CRLF count 4,568; SHA-256 `f8bc648f3c1188a5e052d33a0ecad204d809f14cfbfa6dfb889f89bcb32a3434`.
- Invalid M3 bytes: 479,521 bytes; CRLF count 0; SHA-256 `9f762864101e6b1a91c35fb42374165118a802b686ad5f5d683455ea0d6fc04a`.

Why this matters:
The experiment is byte-addressed. Passing semantic tests does not authorize unrelated byte churn. The prior M3 seals therefore remain evidence of a successful semantic implementation plus a failed artifact-preservation pass, but they are not the final maintenance seals.

Repair rule:
Restore the exact initial schema bytes independently in each arm, insert only the required `tail_lines` property while preserving BOM/newline style, verify that removing the inserted byte span reconstructs the initial bytes exactly, rerun all arm/visible/M3/hostile checks, and issue replacement seals.
