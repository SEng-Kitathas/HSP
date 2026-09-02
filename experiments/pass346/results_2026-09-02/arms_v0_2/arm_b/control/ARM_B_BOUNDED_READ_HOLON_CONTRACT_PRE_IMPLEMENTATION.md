# Arm B — Bounded Project-File Read Holon Contract

Status: **QUALIFIED (pre-embodiment); NOT EMBODIED; NOT OBSERVED**
Version: `pass346-arm-b-v0.2-preimpl-1`
Risk tier: B (multi-file integration seam; read-only consequence)
Exact referent: `arms_v0_2/arm_b/target` instantiated from frozen Pass 346 v0.2 bytes
Lineage: HSP v0 holon contract + Pass 346 frozen preregistration v0.2 + common visible baseline evidence only

## 1. Identity / purpose
`holon_id`: `hsp.pass346.arm_b.bounded_project_file_read`

Purpose: establish a truthful, project-root-authorized, optionally line-windowed and UTF-8-byte-bounded text read through the core `context_engine.read_file` boundary and its admitted parent reuse surfaces, without mutating the source file or live receiver.

Promotion ceiling: this contract can support only the bounded Pass 346 dogfood result. It grants no production readiness, no general HSP proof, no CSC semantic authority, and no stronger concurrency guarantee.

## 2. Boundary
### Provided capabilities
- resolve a requested text-file path under the exact supplied project root;
- read text with incumbent UTF-8 / replacement decode behavior;
- select a 1-based inclusive logical line window;
- bound returned `content` by UTF-8 encoded byte length;
- return coherent core `FileReadResponse` evidence;
- support `project.files.read` reuse without strengthening the core claim;
- support `project.files.read_many` while preserving each failed child as a failure entry.

### Required capabilities
- current allowed-root discovery;
- exact supplied project-root referent;
- filesystem text read/stat;
- existing wire dataclasses and parent context/error wrapper.

### Inputs
`project_id` at parent seam; `path`; optional `start_line`; optional `end_line`; optional `max_bytes`.

### Outputs
Core `FileReadResponse`; parent tool result derived from that response; `read_many` per-file entries with truthful success/failure projection.

### Forbidden claims
- no atomic filesystem snapshot;
- no binary-file support;
- no arbitrary encoding preservation beyond incumbent UTF-8-with-replacement behavior;
- no successful-read claim when path/range/byte/parent obligations are not established;
- no authority outside the exact supplied `base_root` merely because another broader allowed root contains the path;
- no fallback authority inherited from a failed primary read.

## 3. Authority
Owner/grant source: the parent project selector resolves an exact project root; `base_root` is consequence-bearing authority, not a display hint.

Required checks:
1. `base_root` itself must lie within configured allowed roots.
2. When `base_root` is supplied, the resolved candidate must remain within **that exact root**, for both relative and absolute user paths.
3. Without `base_root`, candidate confinement remains against configured allowed roots.
4. `emergent_authority: false`.

Currentness rule: frozen Arm B bytes remain the implementation referent until intentional Arm B mutation; any live receiver drift does not silently rewrite this arm.

## 4. State
External mutable state: target file bytes/metadata, owned by filesystem outside the operation.
Operation-local state: request, decoded text, logical line list, bounded content, response object.
Persistence: none required; operation is read-only.
Concurrency: no file lock / transaction / atomic-snapshot claim.
Currentness limit: metadata/content coherence under concurrent mutation remains a nonclaim.

## 5. Effect
Target: exact authorized text file.
Executor: synchronous receiver read path.
Preconditions: authorized path, existing regular file, admitted text extension, readable/decodeable under incumbent policy, valid bounded-read request semantics.
Required authority: exact supplied project root when parent provides one.

Failure modes include:
- base root outside allowed roots;
- candidate escaping the supplied base root;
- missing/non-file target;
- unsupported extension;
- read/decode/filesystem error;
- range implementation error;
- byte ceiling violation;
- missing parent binding/import;
- child failure in `read_many`.

Fallback: none for single-file read. `read_many` is not fallback; it is a parent aggregation effect that must preserve failed child status.

Four-stage outcome, pre-implementation:
- attempted: **OBSERVED** for current baseline witnesses;
- established: **FALSE/COUNTEREVIDENCED** for failing witnesses;
- observed: **OBSERVED FAILURE** on the common visible baseline (1/6 passes);
- acknowledged success: **NOT EARNED** for the failing parent paths.

## 6. Invariants
### Local
L1. If bounded, `len(content.encode("utf-8")) <= max_bytes`.
L2. Returned content is valid Python text and byte clipping never exposes a partial UTF-8 code unit.
L3. A valid requested line window must not trigger an internal exception.
L4. The read operation does not write target bytes.

### Seam
S1. With supplied `base_root`, no relative or absolute `path` may resolve outside that root.
S2. `project.files.read` must bind the core request type explicitly and preserve the core bounded result.
S3. `read_many` must convert a failed child into an error entry and increment `error_count`; it must not manufacture child success.
S4. `read_many` success metadata must describe the returned content rather than defaulting to unrelated zero/false placeholders when evidence is available.

### Whole
W1. Range success without byte-budget success is whole failure.
W2. Core success without parent-seam success is insufficient evidence for the exposed consequence.
W3. Path containment under a broad allowed root is insufficient when the parent supplied a narrower project root.
W4. A parent success claim requires an established bounded core read plus a successful parent projection.

## 7. Composition / closure
Children and planned bindings:
- C1 path resolution -> `resolve_user_path`: **OPEN until embodied/tested**;
- C2 line selection -> `read_file`: **OPEN**;
- C3 UTF-8 byte bound -> native `str.encode` / byte-prefix / valid decode helper: **OPEN**;
- C4 core response -> existing `FileReadResponse` / `FileSlice`: **BOUND, implementation currently defective**;
- C5 parent single read -> `_project_files_read_payload` + explicit `FileReadRequest` binding: **OPEN**;
- C6 parent multi-read -> `_project_read_one_many` / `_project_read_many_payload`: **OPEN**;
- C7 error projection -> existing context error classes + per-child entry: **OPEN**.

Exported requirements: none intentionally added.
Authority conflicts: none accepted; broader allowed-root membership must not override exact parent project-root authority.
Closure status: **OPEN** before embodiment and tests.

## 8. Evidence
E1. W1 ranged read `NameError: s`: status **OBSERVED**, witness = common frozen visible baseline; current for frozen pre-impl bytes; independence = common baseline, not arm-specific proof.
E2. W2 UTF-8 byte ceiling violation: **OBSERVED**, same currentness/independence ceiling.
E3. full-read control: **OBSERVED PASS**, establishes only that generic file reading works.
E4. project-root escape through supplied `base_root`: **OBSERVED FAILURE** on common baseline.
E5. parent `project.files.read` missing `FileReadRequest`: **OBSERVED FAILURE** on common baseline.
E6. `read_many` parent qualification blocked by missing request binding: **OBSERVED FAILURE** on common baseline.
E7. hidden evaluator: **UNKNOWN / UNREAD / NOT AVAILABLE TO IMPLEMENTATION ARM**.
E8. production behavior after mutation: **UNKNOWN** until arm-local tests execute.

Counterevidence: current baseline passes only 1/6 visible checks; therefore no pre-implementation success claim is admissible.
Assurance ceiling now: **QUALIFIED design contract only**.

## 9. Failure / recovery
A failed child read remains a failed child read. No retry/fallback route gains authority because the primary failed. `read_many` may continue to other children but cannot rewrite the failed child's epistemic or outcome state.

If implementation or qualification fails, preserve the failed diff/tests as evidence and repair within Arm B only. Do not inspect Arm A implementation before both initial seals.

## 10. Reuse
Assumptions exported to a parent: exact project root, admitted text extension, incumbent decode policy, synchronous non-atomic read semantics.
Guarantees after successful qualification only: bounded valid text from an authorized file plus truthful failure projection.
Every new parent must requalify authority, request binding, error mapping, and result projection. Core green evidence alone is insufficient.

## 11. Planned host lowering
- Project-root authority -> `pathlib.Path.resolve` plus explicit containment against the supplied `base_root` when present.
- UTF-8 hard ceiling -> encode once, byte-prefix, decode prefix with incomplete trailing code unit ignored.
- Range semantics -> native `splitlines`, 1-based inclusive index calculation, native slicing/join.
- Parent request binding -> explicit import/use of `FileReadRequest`.
- Child failure preservation -> catch the receiver's context-plane error type at the aggregation seam and project a per-file error entry.
- Success evidence in `read_many` -> derive returned byte count and truncation evidence from actual returned content/source metadata where available.
- Verification -> arm-local `unittest`, common visible evaluator, compile check; hidden evaluator remains unavailable until both seals.

Residual semantic gaps planned to remain explicit: no atomic snapshot; replacement decode can make returned-byte count differ from source-file byte count for malformed UTF-8; no production claim.

## 12. Nonclaims
This contract does not claim that the implementation exists yet, that any invariant is established post-mutation, that the hidden evaluator will pass, that HSP is superior, or that the live receiver has been repaired.
