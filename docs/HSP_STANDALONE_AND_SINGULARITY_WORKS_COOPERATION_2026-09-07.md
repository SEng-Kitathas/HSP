# HSP Standalone and Singularity Works Cooperation — 2026-09-07

Status: **ACTIVE HSP-LOCAL ARCHITECTURE / INTERPRETATION DOCTRINE**

## HSP standalone rule

HSP SHALL remain independently runnable, testable, and research-active even while Singularity Works / Forge is incomplete, unavailable, changing, or being developed concurrently.

For HSP-SC, **STANDALONE** is the default required mode:

`HSP holon contract + typed semantic module -> HSP validation -> HSP semantic IR -> qualified HSP lowering -> host artifact -> HSP-local runtime/shadow verification`

Forge/Singularity Works is optional downstream observation/integration infrastructure. Its absence SHALL NOT block standalone HSP compilation or bounded qualification.

A future **FORGE_ASSISTED** mode may compare HSP-prescribed semantics with Forge-observed semantics, reuse Forge evidence/materialization machinery, and expose correspondence seams. Such integration requires its own explicit contract and qualification. It SHALL NOT silently become a prerequisite for HSP or rewrite normative HSP semantics by observation alone.

`HSP_STANDALONE != FORGE_DEPENDENT`

`OPTIONAL_INTEGRATION != RUNTIME_PREREQUISITE`

`HSP_PRESCRIBED != FORGE_OBSERVED`

## Composition-before-invention boundary

Standalone HSP does not imply reimplementing everything Forge already does. HSP SHOULD remain independent at its semantic/compiler core while reusing qualified Forge machinery in optional integration modes where doing so avoids duplicate generic evidence, source-observation, snapshot/delta, genome/pattern, or reversible-materialization infrastructure.

The intended ownership split is:
- HSP: normative holon semantics, referent meaning, composition closure, authority/effect obligations, semantic admissibility, lowering obligations, expected embodiment contracts.
- Forge: observational semantic facts, exact source/evidence identity, snapshots/deltas, source-analysis IR, pattern/genome providers, reversible materialization, and post-lowering observation when separately integrated.

## Singularity Works cooperative dual-thread authority

Operator-confirmed topology:
- Forge-app / front-end development is an active authoritative workstream over its owned front-end/product-shell surfaces.
- main-dev / back-end development is an active authoritative workstream over its owned main-development/back-end surfaces.
- Both workstreams can hold legitimate intermediate state concurrently.
- Different branch/worktree/local states are therefore not automatically evidence of stale authority, corruption, competition, or unauthorized drift.
- **main-dev directs cross-thread integration/convergence unless the operator explicitly states otherwise.**

This is cooperative concurrency, not competitive authority.

Before reporting a Singularity Works / Forge discrepancy as an authority conflict, determine whether it is explained by:
1. front-end versus back-end surface ownership;
2. unpublished local commits;
3. branch/worktree separation;
4. staged integration;
5. main-dev direction not yet propagated into the other workstream.

Only unexplained consequence-bearing contradictions should be escalated as authority conflict.

`FRONTEND_STATE != BACKEND_STATE` does not imply `AUTHORITY_CONFLICT`.

`COAUTHORITY != UNORDERED_PRECEDENCE`.

`COOPERATION != IDENTITY_COLLAPSE`.

## Project boundary

HSP and Singularity Works remain separate projects and authority domains even when collaborating. Neither silently inherits project/product authority from the other. HSP may continue standalone indefinitely; Forge-assisted correspondence is optional and separately qualified.

This doctrine does not mutate Singularity Works / Forge state and does not attempt to reconcile its concurrent workstreams from the HSP side.
