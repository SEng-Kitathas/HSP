# HSP Bounded-Read Metadata Convergence v0.1 — Qualification Report

Status: **QUALIFIED ISOLATED CONVERGENCE CANDIDATE; NOT PROMOTED**
Process authority: Rahl Engineering Canonical SOP R4.2

## Baseline
- Exact final-B compatibility tree (legacy evaluator ordering): `2fa75e3f085f415e32ad131ae606d302192436d5ee4fd47896acfd060071a830`.
- Baseline portable manifest identity: `a33b74f0a6ce892adb010003e7ecb7e2ddbf087c2f1761e0a8422de6af2ca223`.
- 61 payload files.

## Referent closure
The candidate makes the previously ambiguous evidence explicit at the core measurement point:
- `file.size_bytes` = raw filesystem source bytes;
- `slice.selected_bytes` = UTF-8 bytes of decoded/logically selected text before byte clipping;
- `slice.returned_bytes` = UTF-8 bytes actually returned;
- `slice.truncated` = byte-budget clipping of selected decoded text only;
- both active read-many parents project returned bytes and truncation directly from validated core evidence.

Missing, malformed, or internally inconsistent child slice evidence raises `ValueError`; aggregation paths convert that to a failed child rather than inventing metadata.

## Active parent requalification
Initial scope covered the lab-native `project.files.read_many` parent. Pre-seal inspection found active `power_routes._read_many_file()` carrying the same default-zero/default-false defect. `SCOPE_AMENDMENT_01.md` authorized that seventh path before mutation. Both parents now consume one shared `validated_read_result_evidence()` implementation.

## Discriminators
Added CRLF and malformed-UTF-8/replacement fixtures. Verified that raw source bytes may differ from decoded selected/returned bytes without becoming truncation. Bounded cases prove truncation only at the core byte ceiling.

## Verification
- convergence tests: **19/19 PASS**;
- Pass 346 visible evaluator: **6/6 PASS**;
- M3 `tail_lines` regression: **9/9 PASS**;
- prior hidden hostile regression: **5/5 PASS**;
- compileall: **PASS**.

## R4.2 mutation-scope readback
Exactly seven authorized payload paths changed; zero payload files were added or removed. Runtime `__pycache__`, `.pyc`, and `.pcmmad_sync_runs` byproducts were removed before seal. Both imported schemas preserve their original BOM/newline style and their parsed semantic differences are limited to the three new FileReadResponse slice evidence fields, the slice required list, and the two ReadMany metadata descriptions.

## Aggregate identity referent scar
A reporting pass produced two aggregate tree digests over the same per-file byte map. Root cause: the legacy Pass 346 evaluator sorts Windows `Path` objects, while the portable helper sorted POSIX relative-path strings. Zero files differed from the stored stability manifest. R4.2 therefore requires the algorithm to be named with the digest.

Candidate identities:
- legacy Pass-346/evaluator tree: `5d2cef89b32c4f76ca139e779cbb12829620939f36c24625028cc1aecc2e6196`;
- portable POSIX-relative-path tree: `7855cb50a9c540a4d203b69a7e42acec3472684aa0336755ca691780d217e442`;
- canonical compact manifest JSON identity: `4d0bd3c25a3bd823aaf840c06fc58ea1c2f0027b30089751ff82bec830ed6f83`.

The portable file manifest itself is `CANDIDATE_FILE_MANIFEST.json`.

## Promotion ceiling
This is an isolated qualified convergence candidate. The live receiver remains outside this mutation. Promotion requires a separate currentness/rebase/rollback/live-smoke decision.
