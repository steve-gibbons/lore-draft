---
id: DECISION-INTAKE-SCOPE-AND-TRANSPORT-001
type: decision-record
status: accepted
title: "INTAKE scope, transport paths, and design intent: explicit two-path model"
decision_maker: "Author (Steve Gibbons), sole authority - ratified in-session 2026-08-18"
decided_at: "2026-08-18"
rationale: >
  The heavy intake path (INTAKE/raw → RAW-MANIFEST → author signature → validator) was designed
  for a specific class of material: governed evidence, candidate/accepted decisions, and anything
  that must carry immutability + authority + provenance guarantees. Applying it to ordinary source,
  scratch analysis, and discussion artifacts creates process friction that is an unintended
  consequence, not the design goal. This decision reaffirms design intent, names the two-path
  model explicitly, and rejects "move everything through INTAKE" as a valid operating assumption.
  Physical separation of INTAKE from git is deferred as optional hardening only.
prior_candidate: INTAKE/DECISION-INTAKE-SCOPE-AND-TRANSPORT.candidate.md
---

# Decision — INTAKE Scope, Transport Paths, and Design Intent

**Decision ID:** DECISION-INTAKE-SCOPE-AND-TRANSPORT-001
**Status:** `accepted` — ratified by the author (Steve Gibbons), 2026-08-18, on author authority.
**Category:** Governance process / intake / transport
**Layer:** Process and boundary rules (does not alter CORE-INVARIANTS text; clarifies intended application)
**Date captured:** 2026-08-17
**Date accepted:** 2026-08-18

**Related:**
- LIVE-01 / NEW-01 (manifest registration gaps)
- `INTAKE/raw/OBS-MAINTENANCE-LIVE01-AND-NEW-TRIAGE.candidate.md`
- `INTAKE/raw/DECISION-INTAKE-SCOPE-AND-TRANSPORT.accepted.md` (raw evidence copy, preserved)
- `INTAKE/raw/DECISION-INTAKE-SCOPE-AND-TRANSPORT.candidate.md` (raw evidence copy, preserved)

---

## 1. Synopsis

**Decision:** Clarify the original design intent of `INTAKE/raw` + `RAW-MANIFEST` + signature,
record the tension created when that heavy path is applied to ordinary source and discussion
material, and adopt an explicit two-path model:

- **Heavy path** (INTAKE/raw → RAW-MANIFEST → author signature → validator) — reserved for
  material that requires governed immutability, authority, and provenance.
- **Light path** (ordinary git, copy, or other trusted transport) — the default for working
  source, scratch analysis, discussion artifacts, and anything not yet (or never) treated as
  governed evidence or a status-bearing decision.

Moving `INTAKE` out of git-backed storage is **not** the primary resolution; it is an optional
later hardening step. Scope clarification is the higher-leverage fix.

---

## 2. Design Intent (what INTAKE was for)

`INTAKE/raw` + manifest registration + author signature exist to serve a specific class of material:

1. Externally sourced or agent-produced **evidence** that must not be silently rewritten.
2. **Candidate decisions**, proposals, and other status-bearing records where who may promote
   and who may sign matters.
3. Material that will later be treated as part of the **governed corpus** and must therefore
   carry a verifiable registration event.

The model deliberately separates:

- presence on disk / in a working tree, from
- registration under the authority model (manifest entry + signature + validator green).

Agents may stage; only the author (or an explicitly authorized process) closes registration.
This is consistent with sole-authority rules and with the anti-forgery posture in
`DECISION-AUTH-IDENTITY.accepted.md` and CORE-INVARIANTS.

---

## 3. Tension / Unintended Consequence (recorded, not resolved by reversal)

When the only reliable bridge between environments is the full intake path, the heavy mechanism
is applied to material it was never optimized for: ordinary source trees, scratch analysis,
discussion notes, and ephemeral working files whose primary need is "get this from A to B,"
not "register this under the authority model."

That friction is an **unintended consequence**, not the design goal.

A secondary observation: keeping `INTAKE` inside the git-backed private root is acceptable for
a sole-author / small-trust model, provided the process rule stays sharp —
**presence in the tree ≠ registered**. Physical separation would strengthen immutability claims
but adds operational cost and does not by itself stop heavy-path scope creep.

---

## 4. Decision

1. **Reaffirm design intent.** The heavy path exists for governed evidence, candidate/accepted
   decisions, and other material that requires immutability + authority + provenance guarantees.
2. **Adopt an explicit two-path rule:**
   - **Heavy path** — required when the material is (or is intended to become) governed evidence
     or a status-bearing decision record.
   - **Light path** — default for ordinary source, working files, scratch analysis, and discussion
     artifacts. Light-path material may later be promoted into the heavy path if and when it needs
     governance registration; until then it travels by ordinary means.
3. **Reject "move everything through INTAKE"** as an operating assumption.
4. **Defer** physical separation of INTAKE from git-backed storage. Optional hardening only —
   not required to close the present tension.
5. **Process norm:** When staging material that *does* belong on the heavy path, use
   INTAKE/raw + manifest + signature + validator. When it does not, use light path.

---

## 5. What This Decision Does Not Do

- Does not weaken immutability or signature requirements for material on the heavy path.
- Does not authorize agents to promote statuses or to sign.
- Does not change CORE-INVARIANTS or the closed status set.
- Does not require or forbid moving INTAKE out of git.
- Does not auto-close LIVE-01 or any existing manifest gap.

---

## 6. Provenance

- **Candidate drafted:** agent, 2026-08-17, from session observation on intake friction.
- **Accepted:** Author (Steve Gibbons), 2026-08-18, on author authority. Accepted as written;
  no amendments from candidate text.
- Raw evidence copies preserved in `INTAKE/raw/` per Vol 91 (supersede-not-delete).

---

*End of accepted decision record.*
