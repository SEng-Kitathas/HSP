# HSP Pass 346 — Final Adjudication — 2026-09-02

Status: **EXPERIMENT COMPLETE; NO WINNER; NO LIVE PROMOTION**

## Frozen question

Does HSP v0 / Practical Coding produce a more consequence-preserving and maintainable implementation on this bounded live integration task than a strong conventional idiomatic baseline, after hostile perturbation, without unjustified complexity?

## Result in one sentence

**No local winner is earned.** Both arms repaired the frozen bounded-read consequence, passed the visible evaluator, initial hidden hostile suite, withheld `tail_lines` maintenance task, and hostile replay; final CSC pressure then found an unresolved parent `read_many` evidence contract in both arms. Arm B found and partially repaired that seam, but its repair inferred semantics that were not fully established and fails a CRLF counterexample.

## Frozen source and contamination controls

- Frozen v0.2 target tree: `b27fd1a4e42bce1ad08af933026845083b0c577ca7e73b95301b76e9ae1b20af`.
- Hidden evaluator commitment/payload SHA-256: `afa6c7c06c66bf79127d0098b44ca49ffa1715e77b91107279e9f3d9e262b9cf`.
- Hidden evaluator was not read until both initial arm seals existed.
- Neither arm read the other arm's implementation before its initial seal.
- Live receiver source was not mutated.
- Recovered pre-implementation proposal/repair/rescue cycles were preserved as failed evidence and were not applied.

## Initial implementation results

| Metric | Arm A — conventional | Arm B — HSP v0 / Practical Coding |
|---|---:|---:|
| Initial implementation wall interval | 67.431 s | 76.752 s |
| Source LOC + / - | +20 / -9 | +40 / -16 |
| Test LOC added | 68 | 90 |
| New permanent helpers | 1 | 2 |
| Arm-local tests | 5/5 PASS | 9/9 PASS |
| Visible evaluator | 6/6 PASS | 6/6 PASS |
| Compile | PASS | PASS |
| Initial hidden hostile suite | 5/5 PASS | 5/5 PASS |
| Initial seal tree | `1f43febf...b285` | `89a5b76a...e60c` |

Initial seal artifacts:
- A seal SHA-256: `4f1a77b669fe47b836a20cf164f6a907cce8456ad1088e87b7327ed43fea9afb`.
- B seal SHA-256: `4b59e5a846c5866d7b3153e683b5e0801cdc3726b1d84c109fea446282211e41`.
- B pre-implementation holon contract SHA-256: `0ae30bdb4695f6514ad1590715d23f60eb12aa56f5ac042d5b03e13803ad4501`.

## Withheld maintenance task M3

Hidden task: add optional `tail_lines=N` while retaining byte ceiling and path authority.

Both arms independently implemented the same external semantics:
- `tail_lines` is an alternative logical-line selection mode;
- it cannot be combined with `start_line` / `end_line`;
- final N logical lines are selected before the UTF-8 byte ceiling is applied;
- exact project-root authority remains unchanged;
- the mode is propagated across core request, HTTP wire model, HTTP route, lab-native `project.files.read`, and both imported action schema copies.

Primary first-green maintenance intervals:
- A: 95.019 s.
- B: 57.215 s.

Before final adjudication, CSC byte review invalidated both first M3 seals because the shared editing path normalized all 4,568 CRLFs in the BOM-bearing ACTIVE action schema. The semantic implementations were green, but the byte-addressed artifacts had unrelated churn. Both invalid seals were retained, the exact initial schema bytes were restored, only the new property bytes were inserted, and exact insertion-only reconstruction was verified.

Replacement final M3 seals:
- A final tree: `b702382494803c2157dd87a4dacf45926099cf58bd5e2ca6031bb868d8fad4da`.
- A replacement seal SHA-256: `015c2340ddc2948edaa1cbd5b4f21018a248e8a654d2cb979dccb3d0c5a5c4ad`.
- B final tree: `2fa75e3f085f415e32ad131ae606d302192436d5ee4fd47896acfd060071a830`.
- B replacement seal SHA-256: `d9927501597ac88ac1bfd5a527b247c1d45b79c1428524ba5ae8d1c4e0f17657`.
- Each arm incurred one artifact-preservation repair iteration.

Final maintenance qualification:

| Metric | Arm A | Arm B |
|---|---:|---:|
| Arm-local tests | 8/8 PASS | 13/13 PASS |
| Visible evaluator | 6/6 PASS | 6/6 PASS |
| M3 common evaluator | 9/9 PASS | 9/9 PASS |
| Original hidden hostile replay | 5/5 PASS | 5/5 PASS |
| Compile | PASS | PASS |
| Python maintenance LOC + / - | +18 / -1 | +18 / -2 |
| Maintenance test LOC added | 24 | 37 |
| Schema/config lines added | 10 | 10 |
| Files touched | 7 | 7 |
| Prior established evaluator invariants broken | none after replacement seal | none after replacement seal |

## HSP-only ceremony / explicit structure

Arm B carried three HSP-specific contract artifacts totaling 16,625 bytes / 262 lines:
- initial pre-implementation holon contract;
- embodied-state contract;
- M3 maintenance delta contract.

Across the initial and maintenance contracts, at least 19 explicitly labeled local/seam/whole invariants were recorded, in addition to boundary, authority, state, effect, evidence, reuse, lowering, and nonclaim fields.

This mass is a real cost. It may be justified only by demonstrated protection/change quality; it is not counted as value merely because it exists.

## CSC findings

Detailed report: `evaluator/CSC_QA_REPORT_2026-09-02.md`, SHA-256 `7ee06e9ba6b5f3891fae81c15601d9001852ef2c1292c1eb12df5acb4303d985`.

### Arm A

A bounded successful `read_many` child returns four bytes of content from a ten-byte file but reports:

```json
{"content":"abcd","size_bytes":0,"truncated":false}
```

That parent evidence is internally inconsistent. A therefore does not survive final clean-promotion pressure.

### Arm B

B explicitly identified that seam and reports the ordinary bounded example coherently:

```json
{"content":"abcd","size_bytes":4,"truncated":true}
```

This is useful evidence that HSP's parent-requalification/evidence obligations changed what the implementation noticed.

However, B inferred `truncated` by comparing returned decoded UTF-8 bytes to raw source-file bytes without a normative definition of the metadata referent. On an unbounded six-byte CRLF file whose decoded returned content is four bytes, B reports `truncated:true` even though no byte-budget truncation occurred. Replacement decoding creates a similar referent hazard.

Under HSP's own exact-referent/evidence discipline, that inference is not fully earned. B therefore also fails final clean-promotion pressure.

## Adjudication

Per the frozen interpretation rules:
- both arms survived all frozen visible/hidden/maintenance evaluators;
- correctness alone therefore cannot decide the experiment;
- maintenance and permanent complexity must be examined;
- CSC produced counterevidence against clean promotion for both.

**Final Pass 346 verdict: NO WINNER.**

### Evidence in favor of HSP
- B's pre-implementation contract explicitly forced parent seam/evidence inspection and noticed the `read_many` metadata problem that A left untouched.
- B carried broader arm-local adversarial tests, including unsupported text paths, EOF ranges, invalid negative byte budget, parent success metadata, wire parsing, and imported schema exposure.
- B's first-green M3 maintenance interval was shorter than A's recorded first-green interval, although the preregistered interval starts at first code mutation and therefore excludes pre-code contract-authoring cost.

### Evidence against / pressure on HSP
- B's initial runtime patch was larger and slower than A's.
- HSP added 16.6 KB / 262 lines of contract mass.
- The extra parent metadata repair was not semantically closed: it chose an under-specified byte referent and generated false truncation under CRLF normalization.
- Therefore the additional ceremony did not yet buy a complete demonstrated consequence-preservation advantage.

### Narrow interpretation

The best-supported conclusion is not "HSP won" or "HSP failed." It is:

**HSP v0 supplied useful seam-discovery pressure in this bounded task, but the current contract/lowering discipline still allowed an unearned semantic choice at the discovered seam. That is exactly the next doctrine/engineering pressure point.**

## Post-experiment convergence seam

Before any live receiver promotion, define the parent read evidence contract explicitly rather than guessing:
1. establish whether metadata describes source bytes, selected pre-clipping bytes, returned bytes, or separate fields for each;
2. compute byte-budget truncation at the core point where selected pre-clipping encoded bytes are known;
3. expose explicit returned-byte and truncation evidence in the core response;
4. make every parent surface project those established fields directly;
5. requalify full/range/tail, CRLF, malformed-UTF-8 replacement, bounded/unbounded, and mixed `read_many` cases;
6. then perform a separate promotion review before touching the live receiver.

## Promotion ceiling

This result is local evidence about HSP v0 on the bounded PCMMAD Receiver read-composition dogfood only. It does not establish HSP generally, production readiness, compiler authority, HSP-DF selector authority, or CSC semantic authority.
