# Pass 346 — CSC Hostile QA Report — 2026-09-02

Status: **FINAL POST-DOMAIN QA FOR EXPERIMENT; BOTH ARMS REJECTED FOR CLEAN PROMOTION**

CSC here means Code Slop Cleanup, downstream hostile QA only. No dedicated CSC executable was present in the HSP repository, and the receiver environment had no `ruff` module installed. The QA therefore used the declared downstream role directly: byte/diff inspection, compile and regression evidence, AST/static inspection, and targeted counterexamples against existing response semantics. No new synthetic correctness score was introduced.

## Domain evidence entering CSC

Both replacement maintenance seals are byte-clean and pass:
- arm-local tests: A 8/8; B 13/13;
- common visible evaluator: A 6/6; B 6/6;
- hidden maintenance M3 evaluator: A 9/9; B 9/9;
- original hidden hostile replay: A 5/5; B 5/5;
- `compileall`: both pass;
- replacement seal tree identity: exact for every evaluator replay.

Final replacement maintenance tree hashes:
- A: `b702382494803c2157dd87a4dacf45926099cf58bd5e2ca6031bb868d8fad4da`
- B: `2fa75e3f085f415e32ad131ae606d302192436d5ee4fd47896acfd060071a830`

The first M3 seals are retained but invalidated for byte-clean adjudication because a text-edit path normalized 4,568 CRLFs in `pcmmad_lab_action_schema_ACTIVE.json`. Replacement seals restore insertion-only byte behavior and prove exact reconstruction of the initial schema when the inserted `tail_lines` bytes are removed.

## Static / code-slop inspection

Changed Python modules parse successfully. No TODO/FIXME/HACK markers or debug `print()` calls were found in the inspected changed core/wire/parent modules. The final inspected maximum source line length was 100 for A and 117 for B. `git diff --no-index --check` emitted only Windows line-ending warnings plus the expected nonzero status for differing trees; it emitted no whitespace-error diagnostics on stdout.

A is smaller in runtime code. B carries one additional path helper, one additional bounded-text helper relative to the frozen baseline, more tests, and 16,625 bytes / 262 lines of HSP-only contract/embodiment/maintenance documentation across three contract artifacts.

## CSC finding A-1 — false `read_many` success metadata

Existing parent response type `ReadManyFileEntry` / `ReadManyFileResult` includes `content`, `size_bytes`, and `truncated`.

Counterexample on a ten-byte UTF-8 file with `max_bytes_each=4`:

```json
{"content":"abcd","size_bytes":0,"truncated":false}
```

The returned content is four bytes and is bounded from a ten-byte source, yet A reports zero bytes and no truncation. This is internally inconsistent parent evidence.

Disposition: **CSC REJECT for clean promotion.** The frozen evaluators did not assert these fields, but the preregistered consequence requires truthful parent-surface results and coherent evidence. Green core/hidden checks therefore do not erase the counterevidence.

## CSC finding B-1 — improved ordinary case, but invented/incomplete truncation referent

B explicitly noticed the parent evidence seam and changed `ReadManyFileEntry.from_read_result` to report returned UTF-8 byte count and infer truncation by comparing returned encoded bytes with nested source-file `size_bytes`.

On the same ten-byte / four-byte bounded case B reports:

```json
{"content":"abcd","size_bytes":4,"truncated":true}
```

That is coherent for this ordinary UTF-8 case and is better evidence than A.

However, the source corpus does not normatively define whether `ReadManyFileResult.size_bytes` means raw source bytes, returned bytes, or another referent. More importantly, the truncation inference is not generally sound because `Path.read_text()` uses text decoding/newline normalization.

Counterexample: a six-byte raw CRLF file `a\r\nb\r\n`, read unbounded, becomes four returned UTF-8 bytes `a\nb\n`. B reports:

```json
{"content":"a\nb\n","size_bytes":4,"truncated":true}
```

No max-byte truncation occurred; the byte-count difference came from text-mode newline normalization. The same concern can arise under replacement decoding of malformed UTF-8. B's own initial contract required exact referents and forbade unjustified semantic strengthening, so treating raw source size as sufficient truncation evidence is not fully earned.

Disposition: **CSC REJECT for clean promotion.** This is narrower than A's defect and demonstrates useful seam discovery, but the repair is not semantically closed.

## Common inherited finding — metadata semantics are under-specified

The frozen code contains multiple read-many paths that attempt to project `size_bytes` / `truncated` from a core `FileReadResponse` which does not provide those fields at top level. The underlying response contract therefore needs an authoritative definition rather than another local guess.

Recommended convergence fix after the frozen experiment:
1. define the exact referent of returned-byte and truncation evidence;
2. compute truncation at the core selection/byte-bound point, where pre-clipping selected bytes are actually known;
3. expose that evidence explicitly in the core response or a dedicated bounded-read metadata object;
4. make every parent surface project the same established fields rather than infer them from raw file size;
5. requalify CRLF, malformed-UTF-8/replacement, full read, ranged read, tail read, and mixed read-many cases.

## CSC verdict

- Arm A: **REJECTED for clean promotion** — false parent success metadata remains.
- Arm B: **REJECTED for clean promotion** — parent metadata seam was identified and partially improved, but truncation semantics were inferred from a non-equivalent byte referent.
- Neither rejection erases the fact that both passed every frozen visible/hidden/M3 evaluator.
- CSC does not manufacture a winner or retroactively change the frozen evaluator.
