# HSP Pass 346 — Frozen Preregistration v0.2

Status: FROZEN PREREGISTRATION; NO IMPLEMENTATION ARM HAS STARTED
Frozen target: PCMMAD Receiver V29 Native Protocol Release Candidate — bounded project-file read consequence

## 1. Authority lane and experiment boundary

This experiment is a mainline HSP / Practical Coding dogfood candidate. HSP means Holonic Software Paradigm. Practical Coding means constrained semantic composition plus faithful host lowering. CSC means Code Slop Cleanup and is downstream hostile QA only. HSP-DF is not used as selector authority.

The experiment compares exactly two implementation arms from identical frozen target bytes:

- ARM A — STRONG CONVENTIONAL IDIOMATIC BASELINE
- ARM B — PRACTICAL CODING / HSP v0

This preregistration does not authorize mutation of the live receiver. Both arms must work on isolated copies of the frozen snapshot. Pass 346 implementation/execution begins only after this preregistration gate is accepted; no arm code has been changed at freeze time.

## 2. Frozen target identity and currentness

Live source root:
`C:\Users\ancal\Desktop\PCMMAD_RECEIVER_V29_NATIVE_PROTOCOL_RC1\PCMMAD_receiver\baseline\pcmmad_receiver`

Package label from `README_CURRENT.txt`:
`PCMMAD Receiver V29 Native Protocol Release Candidate`

The deployment has no Git metadata at or above the live source root. Therefore exact revision identity is byte-addressed rather than invented as a commit.

Frozen snapshot path:
`target_snapshot_v0_2/`

Frozen source tree SHA-256:
`b27fd1a4e42bce1ad08af933026845083b0c577ca7e73b95301b76e9ae1b20af`

Snapshot manifest:
`TARGET_SNAPSHOT_MANIFEST_V0_2.json`

Snapshot manifest SHA-256 at creation:
`bc4d5da356d93921d6a96ec608544d85934c9af89f5d4862c91792822bf831fe`

Relevant live file:
`context_engine.py`

Relevant live file SHA-256:
`84685074d5a53c591a5be8b559e41882a3d4858d6303f20352203d1552009ba0`

Currentness evidence at freeze:
- server health returned `status=online` at `2026-09-02T01:43:21.217346+00:00`;
- running Python process command lines explicitly execute the `server.py` under the live source root above;
- the imported GPT action `readProjectFile` reproduced the byte-boundary defect against a fixture in this prereg project;
- the ranged-read failure reproduced both through the imported tool surface and by direct invocation of `context_engine.read_file` loaded from the live source root.

If the live source tree changes before either arm is instantiated, the currentness gate must be rerun and this preregistration must be superseded rather than silently reused.

### 2A. Supersession and currentness requalification

This v0.2 preregistration supersedes v0.1 **for arm admission only**. v0.1 is retained unchanged as historical/scar evidence. Its frozen tree `fccf30f5d26c691da6f6bda931de8fff21219e34295a7c391d1b2065bddb0a95` failed the mandatory currentness gate before any arm started.

Observed drift from v0.1 at recheck: active `browser_bridge_service.py`, `lab_tools_browser.py`, and `server.py` changed; three matching `.bak` files were added. The bounded-read mechanism file `context_engine.py` remained byte-identical at `84685074d5a53c591a5be8b559e41882a3d4858d6303f20352203d1552009ba0`. Diff inspection showed the active changes add browser upload support and HUD autostart behavior; they do not themselves repair the bounded-read path. This relevance judgment does not waive exact-target currentness, hence the new whole-tree freeze.

Live requalification immediately before this freeze:
- server health reported online at `2026-09-02T03:42:25.854488+00:00`;
- imported ranged `readProjectFile` on the prereg fixture still returned an HTTP 500;
- imported `readProjectFile(..., max_bytes=3)` still returned `ééé`, i.e. 6 UTF-8 bytes under a declared 3-byte ceiling;
- no implementation arm had started.

## 3. Real user and desired consequence

Real user: the operator of the live PCMMAD Lab control surface.

Desired consequence:
A caller can read a project text file, optionally restricted to a 1-based inclusive line window and a byte budget, and receive a bounded, truthful success/failure result through the receiver's exposed parent surfaces without an internal 5xx, path-authority escape, silent byte-ceiling violation, or false success.

This is not a request to redesign the context subsystem generally. The target is the bounded project-file read consequence and the integration seams that are required for that consequence to remain true when reused by parent surfaces.

## 4. Existing interfaces and downstream consumers

Load-bearing current interfaces:
- `context_engine.FileReadRequest`
- `context_engine.read_file`
- `api_wire_context.FileSlice`
- `api_wire_context.FileReadResponse`
- `api_wire_models.ProjectFilesReadRequest`
- `context_routes.project_files_read` (`/project/files/read`)
- `lab_tools_project.ProjectFilesReadRequest`
- `lab_tools_project._project_files_read_payload`
- lab-native tool name `project.files.read`
- imported GPT action surface `readProjectFile`
- `project.files.read_many`, which reuses `read_file` for full-file bounded reads and projects per-file failures separately

Current deployment contains 49 Python source files and no discovered `test*.py`, `pytest.ini`, `pyproject.toml`, or `tox.ini` test surface inside the deployed source root. Therefore arm-local regression tests must be added in the isolated experiment copies; a green existing suite cannot be assumed.

## 5. Verified current failure witnesses

W1 — ranged read failure:
A valid ranged read with `start_line` and `end_line` raises `NameError: name 's' is not defined` in the current `context_engine.read_file` ranged branch. Through the imported action this manifests as a server 500 rather than a bounded read result.

W2 — byte-budget failure:
Fixture `fixtures/utf8_multibyte.txt` has SHA-256 `f87cea9ac336de53cc19b3f952851055d7c94aee5b1c42b5e8f1278867fb3364`.
On the frozen live implementation:
- `max_bytes=3` returns three `é` characters = 6 UTF-8 bytes;
- `max_bytes=4` returns `ééé\n` = 7 UTF-8 bytes.
The imported `readProjectFile` surface reproduced the `max_bytes=3` case.

W3 — full-read control:
The same core function succeeds when no line range is supplied, establishing that W1 is not a general inability to read the file.

These witnesses are failures of different obligations and must not be collapsed into one bug label.

## 6. Common semantic referents and authority

The following referents are frozen for both arms:

- `project_id`: authority-bearing selector for the project root, not a display label.
- `path`: project-relative text-file referent resolved under the authorized project root.
- `logical line`: one element of Python `str.splitlines()` under the incumbent implementation; requested line indices are treated as 1-based and inclusive for this experiment.
- `max_bytes`: hard upper bound on the UTF-8 encoded byte length of returned `content`; it does not mean Python character count.
- `content`: the text actually returned to the caller, not the whole source file by implication.
- `success`: the requested read consequence was established and a parent surface returned a truthful success result; merely entering the function or reading some characters is not success.
- `failure`: a failed precondition, path check, decode/read operation, range operation, or parent-boundary operation that prevents the declared consequence. Failure must not be reported as a successful read.

Authority sources, strongest first for this experiment:
1. the current exposed action/wire contract and the operator's observed consequence;
2. frozen live source bytes and their explicit `FileSlice.max_bytes` / `MAX_READ_BYTES` semantics;
3. existing path-authority and error-mapping behavior that is not under change;
4. experiment-specific clarifications above where the incumbent implementation is ambiguous.

No external production-readiness authority is granted.

## 7. State, timing, effects, failure, and currentness

State ownership:
- file content is external mutable filesystem state owned outside the read operation;
- request parameters and response objects are operation-local;
- there is no declared transaction or file lock around the read.

Persistence:
- the consequence is read-only; it must not persist or mutate target file bytes.

Concurrency/currentness:
- the current implementation does not claim an atomic snapshot if another process changes the file during the read;
- no stronger concurrency/currentness guarantee may be invented by either arm without evidence;
- file metadata/content coherence under concurrent mutation remains a nonclaim unless explicitly qualified.

Timing:
- synchronous request/response path.

Retry/fallback:
- the single-file read has no authorized retry/fallback route in the incumbent design;
- `read_many` has a distinct per-file failure projection. It may preserve a failed child read as an error entry, but it may not convert that failure into a stronger successful-read claim.

Irreversible effects:
- none are required. Any write to the live receiver source or the source file being read is out of scope and grounds for stopping the arm.

Four-stage outcome interpretation for the HSP arm:
- attempted: read operation invoked;
- established: authorized file content was read and requested range/byte constraints were actually satisfied;
- observed: a coherent `FileReadResponse`-equivalent result exists at the core boundary;
- acknowledged: the relevant parent surface returns that result to the caller as success.

These states are not interchangeable.

## 8. Composition obligations common to both arms

The desired whole requires at least these capabilities:
- exact project-root-bound path resolution;
- text-file eligibility and decode behavior;
- logical line-window selection;
- UTF-8 byte-budget enforcement without producing invalid returned text;
- coherent slice/evidence reporting;
- parent-surface error mapping;
- reuse by the lab tool / HTTP route without strengthening the core claim;
- per-file failure preservation in `read_many`.

Whole-level invariants:
1. An individually valid path resolution plus an individually valid text slice does not count as a valid whole unless the byte budget and parent response are also valid.
2. If `max_bytes` is bounded, `len(content.encode("utf-8")) <= max_bytes`.
3. A requested line-window must not cause an internal exception for an otherwise valid text file.
4. A successful parent response must correspond to an established bounded read, not merely an attempted core call.
5. Path authority must remain project-root-bound.
6. The operation must remain read-only.
7. A parent reuse surface must be requalified at its seam; core success alone is insufficient evidence for parent success.

Forbidden strengthened claims:
- atomic snapshot under concurrent file mutation;
- binary-file support;
- arbitrary encoding preservation beyond the incumbent UTF-8-with-replacement default unless a later requirement explicitly changes it;
- production readiness;
- general proof of HSP efficacy.

## 9. Arm A — strong conventional idiomatic baseline

Arm A receives:
- the frozen target snapshot;
- this visible preregistration except the HSP-arm procedure section may be omitted from its working prompt;
- verified failure witnesses W1–W3;
- the common behavioral obligations and stop gates.

Arm A instruction:
Use the strongest conventional idiomatic Python engineering approach appropriate to the existing receiver architecture. Inspect actual call paths, implement the smallest coherent repair, and add appropriate regression/integration tests. Do not use HSP terminology, the v0 holon contract, the other arm's artifacts, or the hidden evaluator.

Arm A must not be intentionally weakened into a straw baseline.

## 10. Arm B — Practical Coding / HSP v0

Arm B receives the same frozen target bytes, failure witnesses, behavioral obligations, and stop gates as Arm A, plus the current HSP v0 holon contract and referent errata registry.

Before changing code, Arm B must embody a bounded-read holon contract that records at minimum:
- stable identity/referent/purpose/status/risk/lineage;
- provided/required capabilities and forbidden claims;
- project/path authority and consequence-side checks;
- file/request/response state ownership and currentness limits;
- read effect, preconditions, target, executor, failures, and four-stage outcome;
- local, seam, and whole invariants;
- child bindings / exported requirements / closure status;
- evidence witnesses, currentness, counterevidence, and assurance ceiling;
- explicit no-inherited-fallback-authority rule;
- reuse assumptions/guarantees and mandatory parent requalification;
- host-language correspondence, residual gaps, and tests;
- nonclaims.

Then Arm B lowers those obligations into the strongest practical existing Python mechanisms. It must not introduce formality or abstractions that do not buy demonstrated clarity, protection, or maintenance quality.

## 11. Evaluator separation and contamination control

Common snapshot:
`target_snapshot_v0_2/` tree SHA-256 `b27fd1a4e42bce1ad08af933026845083b0c577ca7e73b95301b76e9ae1b20af`.

Hidden evaluator commitment:
`evaluator/HIDDEN_PERTURBATIONS.json`
SHA-256 `afa6c7c06c66bf79127d0098b44ca49ffa1715e77b91107279e9f3d9e262b9cf`

The selected maintenance task and concrete hidden hostile values are withheld from implementation arms. The file must not be read into either arm's context until both initial implementations are sealed. Separate arm directories/branches and execution logs are mandatory. Neither arm may inspect the other's diff, tests, notes, or results until both are sealed.

Residual evaluator-separation limitation:
The orchestration thread created the hidden commitment and therefore cannot claim cryptographic ignorance of the candidate pool. The selected task/value payload is withheld from the implementation-arm contexts; this is process isolation, not a claim of perfect double blindness.

## 12. Required hostile perturbation classes

The evaluator must exercise all of the following after initial arm seals:
- changed requirement: one frozen hidden maintenance task not visible during implementation;
- alias/referent drift: byte count versus character count and exact line-window referents;
- stale authority: results produced from bytes that do not match the frozen tree hash are excluded unless explicitly requalified;
- retry/fallback pressure: mixed-success `read_many` behavior must preserve failed child status rather than manufacture success;
- partial outcomes: satisfying range while violating byte budget, or vice versa, is a failure of the whole;
- evidence loss: core-only green evidence is insufficient for an integration claim; at least one parent surface must exercise the consequence;
- maintenance task: hidden until initial implementations are sealed, then applied to both arms under the same evaluator rules.

Additional adversarial cases SHOULD cover empty files, EOF boundaries, start/end edge conditions, multibyte UTF-8 near the byte ceiling, unsupported/non-text paths, and project-root escape attempts without changing the incumbent authority model.

## 13. Cost and complexity metrics

Record separately for each arm:
- implementation wall-clock interval from first code mutation to initial seal;
- maintenance-perturbation wall-clock interval;
- source LOC added/deleted;
- test LOC added/deleted;
- files touched;
- new permanent abstractions/classes/types/helpers;
- commands executed and nonzero exits;
- initial failing tests and repair iterations;
- regression/integration test runtime;
- hidden hostile cases passed/failed by obligation class;
- CSC findings after domain verification;
- HSP-only contract/document mass and number of explicit obligations;
- maintenance perturbation diff size and whether previously established invariants were broken;
- residual gaps/nonclaims after the arm is complete.

Do not convert these into a single synthetic score unless a later preregistration supersession explicitly defines and justifies one.

## 14. Stop, rejection, and exclusion gates

Stop/reject the experiment before arm comparison if:
- the live target changes before arm instantiation and currentness is not requalified;
- either arm mutates the live deployment instead of an isolated copy;
- the hidden evaluator leaks into an implementation-arm context before initial seal;
- an arm reads the other arm's implementation before both are sealed;
- the target cannot be executed or tested in isolation enough to distinguish harness failure from mechanism failure;
- evaluator requirements are changed after seeing one arm's result without a visible preregistration supersession.

Exclude, do not overwrite, invalid runs.

A foreground timeout is not scientific failure. Harness failure is not automatically mechanism failure. Tool smoke is not execution qualification. Green tests are not external truth.

## 15. Adjudication and promotion ceiling

Primary question:
Does HSP v0 / Practical Coding produce a more consequence-preserving and maintainable implementation on this bounded live integration task than a strong conventional idiomatic baseline, after hostile perturbation, without unjustified complexity?

Interpretation rules:
- If only Arm A survives the frozen evaluator, that is a local conventional-baseline win and pressure against the HSP obligations that added cost or missed the defect.
- If only Arm B survives, that is a local HSP-arm win and evidence to inspect which explicit semantic obligation mattered.
- If both survive, correctness alone does not prove HSP value. Maintenance/change quality and permanent complexity must be examined; extra HSP ceremony without a demonstrated benefit is negative evidence about minimality.
- If both fail, no winner is manufactured. Identify the missing or harmful obligation and preserve the failure.

Maximum promotion ceiling:
A result may support or weaken claims about HSP v0 on this bounded receiver read-composition dogfood. It cannot establish HSP generally, production readiness, compiler authority, HSP-DF selector authority, or CSC semantic authority.

## 16. Freeze condition

This preregistration is frozen when:
1. this file exists with a reported SHA-256;
2. `TARGET_SNAPSHOT_MANIFEST_V0_2.json` and `target_snapshot_v0_2/` read back to the frozen tree hash;
3. the hidden evaluator file read back to its committed SHA-256;
4. continuity state records that no implementation arm has started.

No target implementation code is changed by the freeze itself.
