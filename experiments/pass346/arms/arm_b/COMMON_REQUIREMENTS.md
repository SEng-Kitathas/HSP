# Pass 346 Common Visible Requirements

Target consequence: repair the current PCMMAD Receiver bounded project-file read path on this isolated frozen copy only. Never modify the live receiver.

A caller must be able to read a project text file, optionally with a 1-based inclusive line range and a byte budget, and receive a bounded truthful result through parent surfaces without an internal 5xx, project-root escape, silent UTF-8 byte-ceiling violation, or false success.

Verified witnesses on the frozen mechanism:
- Valid ranged reads reach a `NameError: name 's' is not defined` and surface as HTTP 500.
- `max_bytes=3` can return `ééé` (6 UTF-8 bytes), violating the declared byte ceiling.
- Full read without a range succeeds, so the range witness is not a general read failure.

Frozen referents:
- project_id: authority-bearing project-root selector.
- path: project-relative file referent under that root.
- logical line: `str.splitlines()` element; requested indices are 1-based inclusive.
- max_bytes: hard upper bound on UTF-8 bytes of returned content, not character count.
- success: bounded read established and parent surface truthfully reports it.

Required invariants:
1. `len(content.encode("utf-8")) <= max_bytes` whenever bounded.
2. A valid requested line window must not cause an internal exception.
3. Parent success must correspond to an established bounded read.
4. Path authority remains project-root-bound.
5. Operation remains read-only.
6. Parent reuse must be tested; core-only green is insufficient for an integration claim.
7. `read_many` must preserve failed child status rather than manufacture success.

Do not invent stronger guarantees for atomic concurrent snapshots, binary support, arbitrary encoding preservation, production readiness, or general paradigm efficacy.

Add focused regression/integration tests in the isolated arm because the deployed target has no existing discovered test suite. Preserve commands, exits, diffs, test runtime, files/LOC, iterations, and residual gaps.
