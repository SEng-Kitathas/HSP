# Operational Scars and Project Rules

Status: active working doctrine

This ledger records continuity-relevant operational failures whose lessons are strong enough to constrain future HSP/PCMMAD work. Preserve the failure and the rule it earned; do not rewrite history to make the path look cleaner.

## 2026-09-02 — Cross-plane asymmetric success/readback scar

### Observed scar
Local execution and persistence on the operator's dev machine can succeed while the assistant-facing readback or chat-rendering surface fails, returns an error, cannot dereference the path, or suppresses the response. A cybersecurity/content gate can also fire after local work has already executed. The chat runtime mount (for example `/mnt/data`) and the dev-machine Windows workspace are separate planes and may have asymmetric visibility.

### Lesson
**Local execution success != local artifact persistence != assistant readback success != artifact registration != chat rendering success != remote synchronization success.**

None of those states may be inferred from another merely because they normally occur together.

### Project rules earned by the scar
1. Track execution as an explicit state vector when it matters: **submitted -> started -> local execution completed -> local artifact persisted -> assistant readback confirmed -> artifact registered (if required) -> chat rendering confirmed -> remote synchronization confirmed (if required)**.
2. A failed or blocked assistant readback is **not evidence that local execution failed or that the local artifact is absent**.
3. Never rerun destructive, expensive, stateful, or contamination-sensitive work solely because chat/readback failed. Inspect local job status, project state, filesystem evidence, hashes, manifests, and alternate local read surfaces first.
4. If one assistant-facing read path fails, use other local surfaces where available: job status, execution journals, project search/listing, direct bounded file reads, manifests, hashes, Git state, or registered result handles.
5. State the failed plane explicitly. Do not collapse a local execution result, action-bridge result, assistant readback result, policy/render result, and remote-sync result into one generic "tool succeeded/failed" claim.
6. A cybersecurity/content block and a transport/filesystem/readback failure are orthogonal until evidence connects them. Do not diagnose one from the other.
7. When a response is blocked after an action may have run, inspect side effects before retrying. The safe default is **read before rerun**.
8. Local persisted state is the custody surface. Assistant claims about it remain provisional until a local status/readback path confirms the relevant fact.
9. When crossing from chat runtime to dev-machine workspace or back, name the bridge and preserve exact paths/IDs/hashes so asymmetric visibility is recoverable rather than mysterious.

## Prior carried scars
The experiment lineage also preserves earlier scars including stale-currentness supersession, foreground timeout != scientific failure, tool smoke != execution qualification, harness failure != mechanism failure, mirror != canonical bytes until exact comparison, green test != external truth, same identity != independent evidence, representation convenience != ontology, and invalid experiments are retained/excluded rather than overwritten.


## 2026-09-02 — Transcript-independent continuity hardening

### Donor signal admitted
Donor material proposed external/local session state plus continuity reinjection through structured tool returns when conversational context becomes unreliable. That mechanism is useful independently of the donor's explanation for *why* context may disappear.

Claims about the exact implementation of OpenAI front-end safety filtering, whether specific blocked text is removed from active model context, or whether tool/system payloads receive categorically different filtering are **not verified by this project and SHALL NOT be promoted into doctrine without evidence**.

### Lesson
**Project continuity SHALL NOT depend on the chat transcript remaining complete, readable, or authoritative.** The operator-owned dev-machine project state is the recovery anchor; chat is one control/presentation surface over that state.

### Project rules earned by the donor + scar synthesis
10. Project-scoped tool responses SHOULD carry a compact structured continuity envelope derived from local persisted state when the response surface can support it.
11. The envelope SHOULD include project/session identity when available, a state fingerprint, bounded resume summary/open loops, exact anchor paths/hashes, and an explicit rehydration route. It SHALL NOT dump the full transcript on every call.
12. Continuity metadata SHALL be added only after the normal authentication boundary. Error handling SHALL NOT turn a failed route into an accidental project-state disclosure.
13. Continuity reinjection SHALL be ordinary structured metadata, not fake `[SYSTEM]` text, role impersonation, stealth prompt injection, or a claimed safety-filter bypass.
14. A read-side continuity envelope SHALL be derived without mutating project/protocol state. Reads must not create synthetic history merely because continuity was requested.
15. Unstructured authenticated project/tool failures SHOULD still preserve a deterministic recovery pointer; a 500 must not erase the route back to Current State / Live Shadow merely because the primary operation failed.
16. If the runtime protocol is uninitialized, its default mode SHALL NOT silently outrank stronger persisted state. Default/uninitialized protocol values and file-derived mode hints must be labeled separately.
17. The server may prove local state, hashes, job status, and emitted response data. It SHALL NOT claim assistant readback success or chat-render success because those planes are not observable from the local server.
18. Session IDs, when present, SHOULD be carried as recovery/disambiguation metadata, but continuity correctness SHALL NOT depend on a session identifier always being supplied.
19. MCP MAY be an additional context transport, but the continuity architecture SHALL NOT require MCP when the receiver already exposes local project rehydration/state surfaces.

### Current embodiment candidate
An isolated candidate exists under project `pcmmad-receiver-continuity-envelope-v0-1`. It qualifies a shared `pcmmad.continuity-envelope.v1` for both compact authenticated Flask project routes and the larger native lab router. The live receiver has **not** been mutated by that candidate.
