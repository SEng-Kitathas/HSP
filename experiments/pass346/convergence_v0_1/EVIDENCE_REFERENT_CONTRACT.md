# HSP Post-Pass-346 Convergence — Evidence Referent Contract

Status: **PRE-IMPLEMENTATION / LOAD-BEARING FOR CONVERGENCE ONLY**
Process authority: Rahl Engineering Canonical SOP R4.2 (2026-09-03)
Scope: isolated `convergence_v0_1/target`; live receiver promotion is explicitly out of scope.

## Purpose
Close the exact metadata/evidence seam that prevented either Pass 346 arm from earning clean promotion.

## Authoritative referents
1. `file.size_bytes` = raw on-disk source byte count from filesystem stat for the exact file at the observation boundary.
2. `slice.selected_bytes` = UTF-8 byte length of the decoded/logically selected text **before** the `max_bytes` ceiling is applied.
3. `slice.returned_bytes` = UTF-8 byte length of the actual returned `content` after byte clipping.
4. `slice.truncated` = whether the byte ceiling clipped selected decoded text. Canonical condition for this implementation: `returned_bytes < selected_bytes`.
5. `read_many.size_bytes` = direct projection of child core `slice.returned_bytes`.
6. `read_many.truncated` = direct projection of child core `slice.truncated`.

## Forbidden substitutions
- raw filesystem `file.size_bytes` SHALL NOT be used as a proxy for selected/returned decoded UTF-8 bytes;
- decoded returned byte length SHALL NOT be compared to raw file size to infer truncation;
- newline normalization, replacement decoding, or other decode transformations SHALL NOT be misclassified as byte-budget truncation;
- missing or inconsistent child slice evidence SHALL NOT be laundered into parent success metadata.

## Core evidence consistency rules
For a successful read:
- `selected_bytes >= returned_bytes >= 0`;
- `returned_bytes == len(content.encode("utf-8"))`;
- `truncated == (returned_bytes < selected_bytes)`;
- `file.size_bytes` remains independently meaningful raw-source evidence and may differ from both selected and returned decoded-byte counts.

## Parent projection rule
`read_many` is a reuse/aggregation seam. It SHALL project the established child evidence directly. If `slice.selected_bytes`, `slice.returned_bytes`, or `slice.truncated` is missing, malformed, or inconsistent with returned content, that child SHALL be represented as a failed child entry rather than guessing/defaulting metadata.

## Required discriminators
- CRLF raw source versus normalized decoded content;
- malformed UTF-8 replacement decoding;
- bounded/unbounded full reads;
- ranged reads;
- tail reads;
- parent single read;
- `read_many` bounded success + child failure;
- missing/inconsistent slice evidence fail-closed behavior;
- imported OpenAPI schema exact field/description exposure.

## Mutation-scope contract
Authorized changed paths only:
- `api_wire_context.py`
- `context_engine.py`
- `lab_tools_project.py`
- `pcmmad_lab_action_schema_v10_3_pcmmad_native_protocol_compact_30_router.json`
- `pcmmad_lab_action_schema_ACTIVE.json`
- `tests/test_hsp_bounded_read_contract.py`

No other source/config path may change. Runtime byproducts (`__pycache__`, `.pyc`, `.pcmmad_sync_runs`) are not candidate payload and must be removed before seal.

For the BOM/CRLF ACTIVE schema, edits must preserve all bytes outside the intended semantic property/description changes. Whole-file newline normalization is forbidden.

## Promotion ceiling
A green convergence candidate is still only an isolated qualified candidate. Live receiver mutation requires a separate PROMOTION decision/currentness check/readback cycle.
