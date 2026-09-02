# Pass 346 Forge-Lane Inference Run — 2026-09-02

Status: INFERENCE COMPLETED; PATCHES NOT APPLIED; ARMS NOT SEALED

## Execution record
- Successful job: `job-59c99e6569a7`
- Execution mode: `bench`
- Agent role: `pass346-two-arm-isolated-inference`
- Local model ID recorded by execution plane: `forge-coder-same-gguf-b77b39f1`
- Return code: `0`
- Stderr: empty
- Arm execution occurred concurrently against separate HTTP model lanes.

## Arm A
- Lane: `127.0.0.1:8113`
- Model alias: `hsp-pass346-arm-a`
- Elapsed: `875.8247826099396 s`
- Prompt tokens: `14045`
- Completion tokens: `683`
- Total tokens: `14728`
- Raw response SHA-256: `9d7f95dd68067bbec5b55d9af971c5d438a55dbb246ffc92789c7ac9a73a67dc`
- In-memory response-text SHA-256 reported by runner: `dbe5a7dd42e790c80342c31afe4a9a13a508abbcc9c52b467257bbff7c6540fc`
- Persisted response-text file has different byte hash because Windows newline translation occurred on write; raw JSON is the canonical response evidence.

## Arm B
- Lane: `127.0.0.1:8114`
- Model alias: `hsp-pass346-arm-b`
- Elapsed: `1228.237508058548 s`
- Prompt tokens: `16966`
- Completion tokens: `1594`
- Total tokens: `18560`
- Raw response SHA-256: `e67987b6ffe483fe5e8623a87e6103bd401d0338bb48cd882ee5b2ed6252095b`
- In-memory response-text SHA-256 reported by runner: `cfc8c9f107786ac35b55b36afc96c442d2aa75198ef242af776909b4debd96ce`
- Persisted response-text file has different byte hash because Windows newline translation occurred on write; raw JSON is the canonical response evidence.

## Isolation audit
- Two distinct local HTTP lanes were used concurrently: ports `8113` and `8114`.
- Arm A and Arm B had separate prompts and separate model aliases.
- No model response patch was applied to either frozen target during this inference run.
- Source comparison against `target_snapshot_v0_2` found **zero changed source files and zero missing source files** in both arms.
- Each arm accumulated eight `__pycache__/*.pyc` files from inspection/import activity. These are runtime byproducts, not source mutations, and are excluded from source-state adjudication.
- Therefore the frozen 60-file source baseline remains intact for both arms.

## Qualification boundary
This run establishes that independent-lane inference occurred and produced two distinct proposal artifacts. It does **not** establish:
- a valid implementation,
- a passing visible evaluator,
- an arm seal,
- a hidden-evaluator result,
- a CSC pass,
- or a Pass 346 winner.

The next admissible step is to audit each proposal against its arm contract, apply only within the corresponding isolated arm if admissible, run visible/domain tests, and seal each arm independently before hidden-evaluator reveal.
