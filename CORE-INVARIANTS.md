# LORE Core — Minimal Invariants (proposed / DRAFT)

> **Status: proposed** (agent-drafted under author direction). NOT normative until the author
> accepts. EXPERIMENTAL / provisional. Addresses **KF-04** (define the TCB). Honest by design:
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

## Trusted Computing Base (what must be trusted for the above to hold)
- **The validator** (`TOOLS/lore_validate.py`) — the single enforcement point. *(KF-03: hand-rolled
  parser, no defense in depth.)*
- **The author's identity & judgment** — the root of authority. *(KF-01: identity unauthenticated.)*
- **Artifact integrity** — that files are what they claim. *(KF-06: hashes opt-in.)*

## Honest posture
Invariants **1, 3, 4** are reliably enforced (when fields are present). Invariants **2, 5, 6, 7**
are **asserted, not authenticated** — the central finding (KF-01). Minimizing this core and then
*authenticating* it is LORE's primary hardening path.
