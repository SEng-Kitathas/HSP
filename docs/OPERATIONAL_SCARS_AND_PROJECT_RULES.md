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
