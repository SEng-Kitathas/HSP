# Continuity Donor Synthesis — 2026-09-02

Status: **controlled donor extraction; mechanism promoted, causal claims provisional**

## Donor material
The donor proposed three related continuity mechanisms:
1. carry compact execution/session state in structured tool return data;
2. move active project/session context into a local external state structure rather than relying on multi-turn transcript memory;
3. optionally expose external context through MCP.

It also asserted a specific causal model for OpenAI front-end safety behavior and message-context stripping. Those product-internal claims are **not established by the donor material or this project** and are intentionally excluded from load-bearing doctrine.

## What survives pressure
The mechanism survives even if the donor's causal story is completely wrong:
- locally persisted state outlives presentation-layer failure;
- the next authenticated project tool response can carry a compact recovery anchor;
- the recovery anchor can point to Current State, Live Shadow, Next Steps, Design Thread Stream, protocol state, result handles, and project rehydration;
- a state fingerprint makes stale recovery detectable;
- a bounded summary avoids re-materializing the whole transcript and protects thread life.

## Translation into existing PCMMAD architecture

### Existing surfaces already available
- Live Shadow = compact active state.
- Design Thread Stream = chronological recovery spine.
- Current State / Next Steps / Doctrine / Revisit / Trace = structured local state.
- `project.context.rehydrate` / compact `rehydrateProjectContext` = bounded recovery path.
- result handles = large-output indirection.
- lab session records = optional session lineage.
- append-only runtime protocol = typed state/continuity/ledger surface when initialized.

The missing mechanism was not another memory database. It was the **bridge from ordinary project-scoped tool responses back to those existing local anchors**.

## Derived continuity-envelope contract

A compact continuity envelope SHOULD provide:
- schema/version;
- project ID and optional session ID;
- state fingerprint;
- protocol initialization/ledger head when authoritative;
- separately labeled persisted mode hint when the protocol is uninitialized;
- bounded resume summary;
- bounded open loops;
- anchor paths/hashes for Live Shadow, Current State, and Next Steps;
- Design Thread pointer/size without retransmitting the stream;
- exact compact/native rehydration instructions;
- a plane note limiting claims to locally observable state.

## Security and truth boundary
- Attach continuity only after ordinary authentication succeeds.
- Do not expose project state on unauthenticated error paths.
- Do not use fake system-role text or prompt-injection framing.
- Do not describe the mechanism as bypassing safety policy.
- Do not claim tool returns are immune to filtering or presentation loss.
- Do not claim server-side evidence proves assistant readback or UI rendering.
- Do not mutate state merely to produce a continuity read.

## Failure-path requirement
A structured error should carry the same recovery envelope as success when authentication/project identity are known. If an internal exception escapes as an HTML/non-JSON 500, the API boundary should normalize it into a generic JSON error plus continuity while preserving detailed traceback server-side.

This rule directly addresses the observed cross-plane scar: the primary operation may fail or its assistant-facing readback may degrade, but the failure response itself should not destroy the deterministic route back to local state.

## Isolated embodiment
Project: `pcmmad-receiver-continuity-envelope-v0-1`

Qualification summary:
- live receiver source frozen at 60 files / tree `36b57da825f993b33ccf5fd1ebe755bb65d66a9a6f854ec43f4eb1f652e2b8f7`;
- candidate-specific tests: 11/11 PASS;
- full compile: PASS;
- known unhandled ranged-read 500 now returns generic JSON + continuity;
- unauthenticated project response does not receive continuity;
- 100 continuity reads produced no state/protocol file mutation;
- 256 concurrent reads produced one deterministic fingerprint;
- warmed mean build cost about 3.8 ms/call;
- representative serialized envelope about 2.3k characters;
- live receiver remains untouched.

The candidate is promotion-ready for review, not promoted by this document.
