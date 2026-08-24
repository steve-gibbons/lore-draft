# LORE Core - Minimal Invariants (normative)

> **Status: normative** - ratified by the author 2026-08-15 (agent-drafted under author direction);
> **invariants 12-13 added 2026-08-16** (canonical kernel, DECISION-ONTOLOGY-CANONICAL-KERNEL-001;
> author-ratified in-session under author authority; detached signature per DECISION-AUTH-IDENTITY pending);
> **invariants 14-15 added 2026-08-18** (core/deployment boundary + conservative engineering doctrine,
> PROP-ARCH-CORE-DEPLOYMENT-DOCTRINE-001; author-ratified in-session under author authority).
> EXPERIMENTAL / provisional. Addresses **KF-04** (define the TCB). Honest by design:
> it marks which invariants are *enforced* vs. merely *asserted* (see KNOWN-FINDINGS).

The **LORE Core** is the minimal set of invariants that must hold for a LORE corpus to be
trustworthy. Everything else is extension. Naming this core is the first step the design source
called for ("define the TCB for LORE"); *authenticating* it is the fast-follower.

## Invariants (the irreducible core)
1. **Closed status.** Every artifact `status` is drawn from the closed enum in
   `REGISTRIES/artifact-statuses.yaml`. - *enforced (validator Check 1)*
2. **Authority boundary.** Only the author (or a registered trusted signer) may assign author-only
   statuses (`accepted, normative, canonical, verified, released, superseded, deleted`).
   - *partially enforced (Check 2: signature reference + signer_fpr against REGISTRIES/trusted-signers.txt
     preferred; bare `author_preseeded: true` still accepted with deprecation warning — NEW-02 retirement
     pending; cryptographic verification of the signature is a separate CI gate; T5 key-custody open) (KF-01)*
3. **Uncertainty preservation.** Non-authoritative artifacts retain an uncertainty status
   (`candidate/unknown/unresolved/quarantined/evidence-only`). - *enforced for proposals (Check 9)*
4. **Explicit transformation provenance.** Every `derived`/`generated` artifact records inputs
   (path + SHA-256) and the transformation. - *enforced when present (Check 8)*
5. **INTAKE/raw integrity.** Raw evidence is never mutated once landed. - *manifest-verified
   (git-preservable SHA-256, Check 6); mutation is tamper-detectable. Forensic layer added:
   the manifest carries a detached OpenPGP signature verified against a trusted-signer root
   (`TOOLS/lore_verify_manifest_sig.py`) - an EXPERIMENTAL Track F test harness, replaceable.
   External witness (independent timestamp) still open (KF-06 / Option D).*
6. **Reference ≠ identity.** An `object-ref` is an alias to an object, never the object; ALIAS ≠
   IDENTITY. - *partial (Check 7 checks the id exists, not that it resolves - KF-08)*
7. **No fabrication.** Agents do not invent corpus content or fabricate provenance. - *asserted*
8. **Conversation states are not flattened.** A design / agent conversation carries at least four
   distinct states - *exploration → candidate → decision → artifact* - and each must stay
   distinguishable; distinctions must not be lost at the transcript boundary. *An invariant
   requirement of LORE's conversation / agent-trace governance use case.* - *asserted (procedural):
   realized by the status enums, decision/proposal records, and the assisted-evaluation procedure;
   not yet validator-enforced. Folded from C21, author decision 2026-08-15.*

9. **Executed is not success** *(LORE development / engineering scope)*. A LORE component MUST
   **return error information**, and its callers MUST **handle** it - errors are never swallowed, and
   execution is never assumed to be success (cf. GL-001: the `12/12 passed` that ran green on
   *corrupted* evidence, LL-001). This applies **at every trust boundary LORE owns** (GL-002): we do
   not control other systems' internals, but we impose it on the bits in scope for us. - *grounded in
   CS fundamentals (CSC101 - always check return values, always handle errors), elevated to LORE
   gospel; asserted (engineering discipline via component design + review), not corpus-validator-
   enforced. From C10, author decision 2026-08-15.*

10. **Representability precedes enforcement** *(from C02)*. LORE cannot reliably enforce a distinction
    it does not **represent**. A merely *named* distinction is asserted, not enforced - the diagnosis
    behind KF-01 (asserted authority) and KF-06 (advisory immutability, until represented as a manifest).
    *Represent, then enforce.* - *grounded in CS / infosec fundamentals (CSC101 / infosec101); asserted design law.*
11. **Authority has lineage** *(from C12)*. Authority is a traceable chain of origin and delegation, not
    mere possession; possession without lineage is not authority. LORE must be able to trace where
    authority came from. - *grounded in infosec fundamentals (chain of trust; CSC101 / infosec101);
    asserted - lineage is not yet cryptographically enforced (KF-01).*
12. **Ontology is represented and enforced** *(from P5-1; canonical model per
    DECISION-ONTOLOGY-CANONICAL-KERNEL-001)*. The ontology is three layers: (0) an abstract `object`
    base (never stored bare); (1) parts of speech + operators + punctuation; (2) the LORE types.
    Every concrete kind - `principal`, `policy`, `object-ref` (subkind `alias`), `relationship`,
    `act` (subkind `event`), `assertion` (subkinds `evidence`, `evaluation`, `context-hint`),
    `authority`, `capability` - has a schema in `SCHEMAS/` and is checked by the validator (Check 4)
    via `kind`(=type) + `subkind`, with each key distinction enforced (ASSERTION ≠ TRUTH,
    EVIDENCE ≠ AUTHORITY, authority-has-lineage, CONTEXT_HINT ≠ TRUSTED_CONTEXT, ALIAS ≠ IDENTITY).
    `thing` and `state` are derived projections, not stored. The ontology may be extended only by a
    registered **domain contract** (additive, namespaced, versioned; cannot relax a core check).
    - *enforced (Check 4); the direct application of invariant 10 (represent, then enforce); closes
    P5-1. Ratified 2026-08-16.*
13. **Accountability requires a human** *(from DECISION-ONTOLOGY-CANONICAL-KERNEL-001)*. A `thing`
    (any non-human principal, an agent included) cannot be held accountable; therefore it must never
    make permanent decisions nor take risky / irreversible actions on its own. The **Accountable**
    role - the **A** in RASIC - is always a **human** principal; agents may be Responsible, Support,
    Consulted, or Informed, never Accountable. - *the root justification for LORE's whole author-only
    authority boundary; partially enforced (Check 4 requires an `accountable` principal on
    destructive/external acts, and `principal_kind` distinguishes human from thing); full
    enforcement - that the accountable party resolves to a human, and human gate-clearing - is
    asserted via the gate/effect model. Ratified 2026-08-16.*

14. **Core/deployment boundary** *(from PROP-ARCH-CORE-DEPLOYMENT-DOCTRINE-001)*. **LORE-CORE**
    is stable: the semantic kernel, invariants, lifecycle states, and authority model do not change
    in response to deployment requirements. **LORE-DEPLOYMENT** is flexible: it configures which
    capabilities are active vs. passive, local policy overrides, and integration choices — within
    the bounds the core permits. Rules: (a) no "lite" distributions — a deployment must carry the
    full core; (b) passive compliance is valid — a core capability may be configured "off" by local
    policy without being absent; (c) flexibility lives in the policy layer — if a requirement cannot
    be met without changing LORE-CORE, that is a core change proposal, not a deployment config.
    - *asserted; architectural constraint on all LORE deployments and federation partners.*

15. **Conservative engineering doctrine** *(from PROP-ARCH-CORE-DEPLOYMENT-DOCTRINE-001)*. Four
    normative principles governing all LORE architectural and integration decisions:
    (a) **Fundamentals first** — default to established CS, infosec, and privacy fundamentals;
    novelty requires justification, boring requires none.
    (b) **Anti-novelty filter** — before adopting a new dependency, pattern, or integration: can
    this be done with something already proven? If yes, default to that. Novelty is a cost.
    (c) **We eat what we cook** — LORE's own repository management, state tracking, agent handoffs,
    and operating procedures must be governed by LORE policies. Not optional.
    (d) **"Boring" is a high-value attribute** — stable, predictable, auditable, maintainable
    systems are the goal; trustworthiness, not excitement.
    - *asserted; engineering discipline via architectural decisions and review.*

## Trusted Computing Base (what must be trusted for the above to hold)
- **The validator** (`TOOLS/lore_validate.py`) - the single enforcement point. *(KF-03: hand-rolled
  parser, no defense in depth.)*
- **The author's identity & judgment** - the root of authority. *(KF-01: identity bound to trusted-signers
  + signature reference in Check 2; cryptographic verification and key-custody (T5) still open.)*
- **Artifact integrity** - that files are what they claim. *(KF-06: hashes opt-in.)*

## Honest posture
Invariants **1, 3, 4** are reliably enforced (when fields are present). **Invariant 5 is now
manifest-verified** (git-preservable, tamper-detectable; KF-06 hardened). **Invariant 12 is now
enforced** (validator Check 4 over the canonical kinds via kind+subkind; closes P5-1).
**Invariant 13 (accountability) is partially enforced** (accountable-on-risky-acts + principal_kind;
the human-resolution + gate-clearing remain asserted via the gate/effect model). **Invariants 14–15**
(core/deployment boundary and conservative engineering doctrine) are **asserted** architectural and
engineering constraints. Invariant **2** is **partially enforced** (Check 2 representation binding; crypto gate separate;
migration grace for `author_preseeded` still live — NEW-02). Invariants **6, 7** and the added
rules **8–11** remain **asserted, not fully authenticated**. Completing authentication of the
authority boundary (retire grace path; T5 custody) remains LORE's primary hardening path for KF-01.
