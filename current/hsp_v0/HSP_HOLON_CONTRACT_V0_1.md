# Minimum HSP v0 Holon Contract

Status: **normative for this bounded research package only**  
Authority: **none over production, promotion, or external projects**

## Definition

A holon is a software unit treated as both:

- a **whole**, with its own purpose, boundary, invariants, effects, failures, and evidence; and
- a **part**, with an explicit contract governing lawful reuse inside a larger whole.

The contract does not make code valid by being present. It makes the obligations inspectable and rejectable.

## Minimum required fields

1. **Identity** — stable `holon_id`, version, exact referent, purpose, status, risk tier, and lineage.
2. **Boundary** — provided capabilities, required capabilities, inputs, outputs, and forbidden claims.
3. **Authority** — owners, explicit grants, forbidden powers, currentness rule, consequence-side check, and `emergent_authority: false`.
4. **State** — owner, mutable state, persistence boundary, concurrency rule, and currentness rule.
5. **Effects** — target, preconditions, required authority, executor, failure modes, fallback, and separate attempted/established/observed/acknowledged outcome fields.
6. **Invariants** — local, whole, and seam invariants.
7. **Composition** — children, bindings, exported requirements, seam obligations, authority conflicts, and closure status.
8. **Evidence** — claim, epistemic status, witness, currentness, independence, counterevidence, and assurance ceiling.
9. **Failure/recovery** — explicit failure boundary; fallback cannot inherit authority merely because the primary path failed.
10. **Reuse** — exported assumptions and guarantees plus mandatory requalification in every new parent.
11. **Lowering** — exact host language/mechanisms, correspondence from semantic obligation to code, residual gaps, and tests.
12. **Nonclaims** — explicit limits on what this holon and its evidence establish.

## Composition laws

### C1 — Part validity is not whole validity

Individually valid children do not establish a valid parent. The parent must discharge every child requirement or export it, qualify every new seam, resolve authority/state ownership, and establish parent invariants.

### C2 — Whole validity is not reusable-part validity

A valid whole reused under a new parent must be requalified against the new referent, authority, state, timing, failure, and evidence context.

### C3 — Closure is explicit

For every required capability of every child, the composition lists exactly one internal binding or exported requirement. A silently dropped requirement invalidates closure.

### C4 — Guarantees are earned

A parent guarantee must be traceable to child guarantees, discharged assumptions, seam invariants, authority checks, and observed outcomes. Source count and label agreement are not proof.

### C5 — Authority does not union

Combining children does not union their powers. Conflicting or ambiguous authority yields `OPEN` or `REJECTED`, never an implicit stronger grant. Emergent capability may be observed; emergent authority is forbidden.

### C6 — Evidence retains provenance

Composition preserves each claim's status (`VERIFIED`, `OBSERVED`, `INFERRED`, `HYPOTHESIZED`, `UNKNOWN`), witness, currentness, independence, and counterevidence. Flattening these into a boolean pass is invalid.

### C7 — Fallback is a separate effect route

Fallback requires its own authority and recovery analysis. A write grant cannot become delete authority; an unavailable primary route does not justify a more destructive route.

### C8 — Outcome stages remain separate

Attempted, established, observed, and acknowledged are distinct. Attempting an effect cannot be reported as success.

### C9 — Referent is exact

Identity, authority, evidence, and execution must bind the same exact target. Alias resolution must be explicit and current. Wrong-referent execution is a contract failure.

### C10 — Host lowering is strongest-available, not magical

The lowering uses native types, modules, visibility, ownership, exceptions/results, tests, and tooling where the host supports them. Residual semantic gaps remain explicit. No arbitrary-language or universal-proof claim is permitted.

## Risk tiers

| Tier | Typical consequence | Minimum burden |
|---|---|---|
| A | local, reversible, low-risk | direct interface, local invariants, idiomatic code, focused tests |
| B | multi-file, persistent state, nontrivial effects | full boundary/state/effect/seam contract and adversarial tests |
| C | authority, concurrency, durability, retry/protocol, irreversible or high consequence | full contract, exact referents, currentness, independent evidence where possible, fallback/outcome proof, hostile campaign |

## State machine

`DRAFT -> QUALIFIED -> EMBODIED -> HOSTILE_TESTED -> OBSERVED`

At any stage, contradictory evidence or a context change may move the contract to `OPEN`, `REJECTED`, or `STALE`. Only `OBSERVED` means the claimed consequence was witnessed inside the declared scope. It still grants no production or promotion authority.

## CSC location

CSC runs after embodiment and domain verification as final hostile QA. It may reject the artifact for applicable quality failures. It cannot create a missing semantic contract, resolve an unknown referent, invent authority, or convert an attempted effect into an observed outcome.
