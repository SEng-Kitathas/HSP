# Authority Reconciliation — R4.4 + ICF-CS v1.1 — 2026-09-06

Status: **ACTIVE PROCESS-AUTHORITY RECONCILIATION; PROJECT/PRODUCT AUTHORITY UNCHANGED**

## Trigger
The operator directed inspection of `authority/rahl-sop/CURRENT.md`, verification of `authority/rahl-sop/releases/ICF_CS_V1_1/`, and reconciliation against this HSP project's current local authority before mutation.

## Verified carrier state
The local HSP checkout was first confirmed clean at commit `98955d24c89d2124723ba42e42324160b77d409c`, then fast-forwarded to the repository's current remote `main` carrier commit:

`ead64c3b79f8e66cb411ab597b17b20e68471a52`

The fast-forward added only the shared authority carrier under `authority/rahl-sop/`; no project source code changed in that remote commit.

### Current universal process stack
From `authority/rahl-sop/CURRENT.md`:
- Canonical sealed base: **Rahl Engineering Canonical SOP R4.4**
- R4.4 SHA-256: `04f3e94efe8c901cc83a12a9c8531be8a9bb350728b8f9eba53db0fd082b3bbc`
- Active additive doctrine: **Intent–Constraint–Frontier Continuity Standard (ICF-CS) v1.1**
- ICF-CS payload SHA-256: `f6f4ab2bafdb0ef2a7db1622a00462990baf980284d5b33827807caea1d41f63`
- Detached receipt SHA-256: `418346ed6373887b5b924e71ca2bf4b83effad20b7269ab40607f5d2750b970c`
- Distribution ZIP SHA-256: `2bb57b24967f80fc5dcf028eece142150ce5d6a1356f12e13cda26951ae19fe7`
- Receipt decision: `ACTIVE_BINDING_ADDITIVE_DOCTRINE`

## Verification performed
The release stack was verified before admission:
- distribution ZIP CRC: PASS;
- distribution verifier: PASS / `ACTIVE_BINDING_ADDITIVE_DOCTRINE`;
- external detached receipt and embedded receipt: exact same expected bytes after checkout-representation repair;
- R4.4 primary verifier: PASS / state `PROMOTED`;
- R4.4 hostile suite: 54/54 rejected;
- R4.4 deterministic seal: true;
- ICF-CS primary verifier: PASS;
- ICF-CS meta-verifier: PASS;
- ICF-CS hostile suite: 35/35 rejected;
- ICF-CS semantic pending: 0.

The complete readable load-bearing R4.4 + ICF-CS v1.1 authority surface was linearly read under the active semantic gate. Automated checks supported but did not substitute for that read.

## Checkout representation scar and repair
This Windows checkout had `core.autocrlf=true` and no authority-specific `.gitattributes`, so the correct Git-object LF bytes of `CURRENT.md`, `SHA256SUMS.txt`, and the detached receipt were rewritten to CRLF in the working tree.

Consequences:
- Git object / embedded receipt remained correct;
- working-tree detached receipt failed its own SHA-256 witness;
- semantic JSON was unchanged, but byte identity was not.

Repair:
- added `authority/rahl-sop/.gitattributes` as an exact-byte authority enclave;
- restored the three readable carrier files byte-for-byte from current Git objects.

This is a representation-policy repair, not a release-semantic mutation.

## Reconciliation against prior HSP local authority
The HSP project previously recorded a locally adopted artifact labeled R4.2 with SHA-256:

`6e8d48d311a089dd2076869b50168d8c68bfb8770819a7c1dd8cf5acafdcb86f`

Canonical R4.4 ancestry instead binds its canonical R4.2 predecessor to:

`eb167543e9ceb2ae01449f421d2916e61b7dd924270ea2e83e3364c9d808ce9a`

No surviving server-side R4.2 ZIP matching the HSP-local `6e8d48...` value was found. Therefore:

`SAME_VERSION_LABEL != SAME_ARTIFACT`

The older HSP-local R4.2 adoption record remains historical provenance only. It SHALL NOT be treated as byte-identical canonical ancestry for current R4.4.

## Rule-number collision handling
The HSP-local doctrine had used labels C24/C25 for:
- evidence-field referent closure;
- mutation-scope verification.

Canonical R4.4 uses C24/C25 for different canonical process obligations. Therefore local numeric labels are retired from authority use. Their semantics remain active under explicit HSP-local names:

### HSP-LDO-ER — Evidence Referent Closure
Consequence-bearing evidence fields require an explicit semantic referent before projection, inference, aggregation, promotion, or load-bearing use.

Key non-equivalences:
- `FIELD_PRESENT != REFERENT_DEFINED`
- `PROXY_VALUE != AUTHORIZED_SEMANTIC_REFERENT`
- `DERIVED_METADATA != EARNED_EVIDENCE`

### HSP-LDO-MS — Mutation-Scope Verification
Behavioral correctness and intended mutation scope are separate claims. Consequential mutation requires readback of actual changed paths/bytes/representation effects against the authorized mutation set.

Key non-equivalences:
- `GREEN_BEHAVIOR != INTENDED_MUTATION_SCOPE`
- `FORMAT_NORMALIZATION != AUTHORIZED_SEMANTIC_CHANGE`

These HSP-local obligations are project doctrine, not canonical R4.4 rule-number claims.

## Linear semantic-read doctrine reconciliation
The prior HSP additive doctrine:

> LINEAR HUMAN READ / SEMANTIC GATE

is semantically compatible with and generalized by canonical R4.4's linear semantic-read requirements and ledger/promotion interlocks. It remains valuable historical provenance but no longer needs to act as a competing universal process layer.

## Authority precedence after reconciliation
1. **Universal engineering/process authority:** R4.4 + active additive ICF-CS v1.1 from `authority/rahl-sop/`.
2. **HSP-local process obligations:** HSP-LDO-ER, HSP-LDO-MS, aggregate-digest referent scar, cross-plane readback rules, and other project-specific operational scars.
3. **HSP project/product/research authority:** unchanged; Pass 346 NO WINNER and all existing HSP claim ceilings remain intact.
4. **Qualified isolated candidates:** remain unpromoted until their own explicit promotion gate.

`CARRIER_PRESENT != PROJECT_SPECIFIC_AUTHORITY_REWRITE`

## Mutation boundary of this reconciliation
This adoption changes process-authority interpretation and local doctrine naming only. It does **not**:
- mutate the live receiver;
- promote bounded-read convergence;
- promote the continuity-envelope candidate;
- rescore Pass 346;
- create new HSP product/scientific authority.
