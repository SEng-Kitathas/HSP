# Additive Doctrine Addendum — Linear Human Read / Semantic Gate — 2026-09-03

Status: **ACTIVE ADDITIVE DOCTRINE OVER R4.2**

This addendum does not rewrite or replace the sealed Rahl Engineering Canonical SOP R4.2 package. It is an additive governing rule for this HSP workstream and any artifact admission/promotion decision made under it.

## Binding text

> **LINEAR HUMAN READ / SEMANTIC GATE**
> If an artifact can be meaningfully read, it SHALL receive a complete linear semantic read before it is promoted, sealed, published, admitted, or treated as load-bearing. Automated checks may precede and support the gate; they SHALL NOT substitute for it.

## Interpretation

1. “Can be meaningfully read” includes human-readable source, specifications, SOPs, reports, manifests with semantic fields, structured text, prompts, configuration, schemas, patches/diffs, test plans, verification reports, and other artifacts whose meaning cannot be reduced to byte/integrity checks alone.
2. “Complete linear semantic read” means traversing the readable artifact from beginning to end in its governing order, preserving its terminology, authority boundaries, caveats, contradictions, and internal dependencies rather than sampling only likely-relevant fragments.
3. Automated verification, hashes, parsers, schema checks, hostile tests, static analysis, search, summaries, and targeted reads may precede the gate and may guide attention, but none of them independently satisfy the semantic-read obligation.
4. The gate is required **before** an artifact is promoted, sealed, published, admitted, or treated as load-bearing. A structurally valid or hash-verified artifact may remain provisional until the semantic read completes.
5. Binary/non-semantic payloads are not forced through artificial textual inspection. Their admission remains governed by integrity, structure, provenance, execution, and domain-specific verification appropriate to the artifact.
6. Nested readable artifacts remain subject to the same rule when they themselves are being admitted as load-bearing. Archive/container inspection does not semantically admit readable members by proxy.
7. If a complete linear semantic read is infeasible because the artifact is too large, inaccessible, encrypted, malformed, or otherwise unreadable, that limitation SHALL be stated explicitly and the artifact SHALL NOT be promoted as semantically admitted merely because automation passed.

## Non-equivalences

`AUTOMATED_CHECK_PASS != SEMANTIC_ADMISSION`

`SEARCH_COVERAGE != LINEAR_READ`

`STRUCTURAL_VALIDITY != LOAD_BEARING_MEANING`

`CONTAINER_VERIFIED != READABLE_MEMBER_SEMANTICALLY_ADMITTED`

`SUMMARY_AVAILABLE != SOURCE_READ_COMPLETE`

## Process consequence

The promotion/sealing checklist now has an explicit semantic gate:

`INTEGRITY / STRUCTURE CHECKS -> COMPLETE LINEAR HUMAN READ WHEN MEANINGFULLY READABLE -> SEMANTIC ADMISSION -> PROMOTION / SEAL / PUBLICATION / LOAD-BEARING USE`

Automation may occur before, during, or after the linear read, but cannot replace it.
