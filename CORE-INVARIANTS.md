# LORE Core — Minimal Invariants (normative)

> **Status: normative** — ratified by the author 2026-08-15 (agent-drafted under author direction).
> EXPERIMENTAL / provisional. Addresses **KF-04** (define the TCB). Honest by design:
> it marks which invariants are *enforced* vs. merely *asserted* (see KNOWN-FINDINGS).

The **LORE Core** is the minimal set of invariants that must hold for a LORE corpus to be
trustworthy. Everything else is extension. Naming this core is the first step the design source
called for ("define the TCB for LORE"); *authenticating* it is the fast-follower.

## Invariants (the irreducible core)
1. **Closed status.** Every artifact `status` is drawn from the closed enum in
   `REGISTRIES/artifact-statuses.yaml`. — *enforced (validator Check 1)*
2. **Authority boundary.** Only the author (or a preseeded author fixture) may assign author-only
   statuses (`accepted, normative, canonical, verified, released, superseded, deleted`).
   — *asserted, not authenticated (KF-01)*
3. **Uncertainty preservation.** Non-authoritative artifacts retain an uncertainty status
   (`candidate/unknown/unresolved/quarantined/evidence-only`). — *enforced for proposals (Check 9)*
4. **Explicit transformation provenance.** Every `derived`/`generated` artifact records inputs
   (path + SHA-256) and the transformation. — *enforced when present (Check 8)*
5. **INTAKE/raw integrity.** Raw evidence is never mutated once landed. — *manifest-verified
   (git-preservable SHA-256, Check 6); mutation is tamper-detectable. Full forensic
   (signing / external witness) still open (KF-06).*
6. **Reference ≠ identity.** An `object-ref` is an alias to an object, never the object; ALIAS ≠
   IDENTITY. — *partial (Check 7 checks the id exists, not that it resolves — KF-08)*
7. **No fabrication.** Agents do not invent corpus content or fabricate provenance. — *asserted*
8. **Conversation states are not flattened.** A design / agent conversation carries at least four
   distinct states — *exploration → candidate → decision → artifact* — and each must stay
   distinguishable; distinctions must not be lost at the transcript boundary. *An invariant
   requirement of LORE's conversation / agent-trace governance use case.* — *asserted (procedural):
   realized by the status enums, decision/proposal records, and the assisted-evaluation procedure;
   not yet validator-enforced.*

9. **Executed is not success** *(LORE development / engineering scope)*. A LORE component MUST
   **return error information**, and its callers MUST **handle** it — errors are never swallowed, and
   execution is never assumed to be success. This applies **at every trust boundary LORE owns**
   (cf. invariant on context/trust crossings): we do not control other systems' internals, but we
   impose it on the bits in scope for us. — *grounded in CS fundamentals (CSC101 — always check return
   values, always handle errors), elevated to LORE gospel; asserted (engineering discipline via
   component design + review), not corpus-validator-enforced.*

10. **Representability precedes enforcement** *(from C02)*. LORE cannot reliably enforce a distinction
    it does not **represent**. A merely *named* distinction is asserted, not enforced — the diagnosis
    behind KF-01 (asserted authority) and KF-06 (advisory immutability, until represented as a manifest).
    *Represent, then enforce.* — *grounded in CS / infosec fundamentals (CSC101 / infosec101); asserted design law.*
11. **Authority has lineage** *(from C12)*. Authority is a traceable chain of origin and delegation, not
    mere possession; possession without lineage is not authority. LORE must be able to trace where
    authority came from. — *grounded in infosec fundamentals (chain of trust; CSC101 / infosec101);
    asserted — lineage is not yet cryptographically enforced (KF-01).*

## Trusted Computing Base (what must be trusted for the above to hold)
- **The validator** (`TOOLS/lore_validate.py`) — the single enforcement point. *(KF-03: hand-rolled
  parser, no defense in depth.)*
- **The author's identity & judgment** — the root of authority. *(KF-01: identity unauthenticated.)*
- **Artifact integrity** — that files are what they claim. *(KF-06: hashes opt-in.)*

## Honest posture
Invariants **1, 3, 4** are reliably enforced (when fields are present). **Invariant 5 is now
manifest-verified** (git-preservable, tamper-detectable; KF-06 hardened). Invariants **2, 6, 7** —
and the added rules **8–11** — remain **asserted, not authenticated** (KF-01). *Authenticating* this
core is LORE's primary hardening path.
