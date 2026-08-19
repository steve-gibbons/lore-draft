---
id: DECISION-PROSE-RECONCILIATION-001
type: decision-record
status: accepted
title: "Prose <-> reality reconciliation (accumulated but unexecuted description drift)"
decision_maker: "Author (Steve Gibbons), sole authority - ratified in-session 2026-08-16"
decided_at: "2026-08-16"
rationale: >
  This session added software/artifacts (two evidence-only evaluations, a domain-contract
  sketch) and surfaced design intent in conversation, but the corpus's own governing and
  operational prose was not reconciled to match. LORE names this exact failure mode
  (CORE-INVARIANT 9 "executed is not success"; 10 "representability precedes enforcement"):
  a description that no longer matches reality is itself a defect. This record is the tiered
  reconciliation ledger. Tier 1 and Tier 2 (non-normative corrections/traceability) are
  executed with this commit; Tier 3 (normative evolution) is recorded here as proposals for
  author ratification and is NOT executed.
provenance:
  created_by: agent
  under_author_direction: true
  author_preseeded: true
  signature_pending: "Detached signature per DECISION-AUTH-IDENTITY to be attached by the author; recorded here as in-session author ratification, not an agent-produced cryptographic signature."
  inputs:
    - path: INTAKE/eval-P4-P6-interstellar-federation.evidence-only.md
    - path: INTAKE/eval-P1-P6-full-panel.evidence-only.md
    - path: SANDBOX/domain-contract-model.candidate.md
    - path: REPO-OPERATING-NOTES.md
    - path: INTEGRATIONS/OPEN-DECISIONS-REGISTER.md
    - path: META-CONTEXT/self-assessment/KNOWN-FINDINGS.md
  transformation: "consistency audit of governing/operational prose against artifacts added this session and decisions taken in conversation."
---

> **PROPOSED. Agent-drafted; confers no authorization.** Only the author may accept this or
> promote any status. Tier 1 & Tier 2 below are agent-writable maintenance to **non-normative**
> prose and are applied with this commit; Tier 3 touches **normative/authority** prose and is
> left as a proposal.

# 1. Why this exists

We have been "doing things in software" faster than we have updated the description. Every item
below is a place where the prose and the reality diverged during this session. Left alone, each
is a latent trust failure: a future reader (human or agent) who believes the description would be
wrong.

**Scope of authority honored:** an agent may correct/extend non-normative prose (operating notes,
the agent-maintained open-decisions register, the evidence-only self-assessment) and draft
proposals; it may **not** rewrite normative/authority prose (`AGENTS.md`, `CORE-INVARIANTS.md`) or
promote statuses. Tiering follows that line.

# 2. The reconciliation ledger

## Tier 1 - Correctness (prose is now factually wrong or points at nothing). **Executed.**

| # | Where | Was (prose) | Is (reality) | Fix applied |
|---|-------|-------------|--------------|-------------|
| T1.1 | `REPO-OPERATING-NOTES.md` §Validation | "expected: 12 passed, 0 failed" | validator reports **14 passed, 0 failed** (12 fixtures + manifest + signer checks) | count corrected to 14 |
| T1.2 | `SANDBOX/example-domain-contract.clinical.DRAFT.yaml` + model | referenced `REGISTRIES/domains.yaml`, `REGISTRIES/domains-revocations.yaml`, `domains/clinical/schemas/*` as if present | none of those paths exist | annotated inline as **PROPOSED / does-not-exist-yet** so the prose no longer asserts existence |
| T1.3 | new `type: domain-contract` | used in the sketch | unknown to any registry/manifest | recorded as a **proposed type** here + in the open-decisions register (not added to the enforced manifest until ratified) |

## Tier 2 - Traceability (governed record lags what we actually found/decided). **Executed.**

| # | Where | Gap | Fix applied |
|---|-------|-----|-------------|
| T2.1 | `INTEGRATIONS/OPEN-DECISIONS-REGISTER.md` | the open decisions generated this session were untracked | added rows: ontology-enforceability, domain-contract governance |
| T2.2 | `META-CONTEXT/self-assessment/KNOWN-FINDINGS.md` | net-new findings (P5-1 ontology↔schema disjunction; P6-1 offline-default; P6-2 crypto-agility; P6-3 succession primitive; P6-4 ontology drift; external-review items: intake-poison permanence, reviewer-DoS, unbounded self-eval) not acknowledged | added a **staged-findings pointer** to the two `INTAKE/eval-*.evidence-only.md` files, pending author triage into numbered KF entries |

## Tier 3 - Normative evolution (needs author ratification). **NOT executed - proposed only.**

These change authority/normative prose and are decisions for the author:

- **T3.1 Ontology enforceability.** Author stated the schema/ontology is *intended to be
  enforced and extended via a domain contract*. Proposed: promote this to a governed decision and,
  if accepted, add a core invariant ("the ontology is representable and enforced, extended only
  within a domain contract"). Closes finding P5-1 at the doctrine level.
- **T3.2 `AGENTS.md` §3.4 scope wording.** It currently reads "No ... federation layers ... may be
  added." The domain-contract work is a *phase-2 design sketch*, not added infrastructure, but the
  wording and the accumulated direction should be reconciled (e.g., "no federation infrastructure
  is *activated* in phase-1; phase-2 design may be *sketched* under governance"). Author's call.
- **T3.3 Candidate core invariants from the panel.** Consider crypto-agility / signature temporal
  validity (P6-2) and offline-default federation (P6-1) as invariant or roadmap items.
- **T3.4 Graduate `domain-contract`.** If the model is accepted, move
  `SANDBOX/domain-contract.schema.DRAFT.json` into `SCHEMAS/`, register it in
  `CORPUS-MANIFEST.yaml`, and create `REGISTRIES/domains.yaml` - turning T1.2/T1.3 dangling
  references into real, enforced representation ("represent, then enforce").
- **T3.5 Generate the machine-readable manifest during build/test (author suggestion, 2026-08-16).**
  `CORPUS-MANIFEST.yaml` is currently hand-maintained, which is precisely how it drifts from
  reality (the class of defect this whole record addresses). Proposed: make the manifest a
  **`generated` artifact** produced by a build/test step (e.g. `TOOLS/lore_build_manifest.py`),
  run in CI and by the validator, so the index is *derived from* the corpus rather than asserted
  about it - and a stale/hand-edited manifest becomes a check failure. Aligns with CORE-INVARIANT
  10 (represent, then enforce) and moves manifest integrity from asserted to enforced. This
  supersedes the "register it in CORPUS-MANIFEST.yaml" step of T3.4: if the manifest is generated,
  graduating a schema means the generator picks it up, not a hand edit.

# 3. Companion action

`ACTION_ITEMS/open/AI-002-core-and-extended-volume-sanity-check.md` - a tracked action to revisit
the core (Vol 0-4) and extended (Vol 5-120) volumes for a sanity check, since this session read
only a targeted subset and the ontology↔schema disjunction (P5-1) suggests the volumes and the
enforced layer need a full cross-check.

# 4. Decision requested

Author to: (a) confirm Tier 1/Tier 2 reconciliations, (b) accept/modify/reject each Tier 3
proposal, (c) set priority on AI-002. On acceptance, flip this record to `accepted` and open the
Tier 3 items as their own decision records.

---

# 5. Author ratification & outcomes (2026-08-16)

Ratified in-session by the author (sole authority). Signature per `DECISION-AUTH-IDENTITY`
pending (see provenance). Outcomes:

| Item | Ruling | What was done |
|------|--------|---------------|
| **T1** correctness | ✅ ratified | applied (12→14 count fix; sketch dangling-ref annotations) |
| **T2** traceability | ✅ ratified | applied (open-decisions rows; KNOWN-FINDINGS pointer) |
| **T3.1** ontology enforceability | ✅ approved | `DECISION-ONTOLOGY-ENFORCEABILITY-001` accepted; **CORE-INVARIANT 12 ratified 2026-08-16** into `CORE-INVARIANTS.md`; all 10 Vol 1 §3 primitives enforced (validator 32/0) |
| **T3.2** AGENTS §3.4 wording | ✅ approved | **applied to `AGENTS.md` 2026-08-16** (activated/added infrastructure vs phase-2 design sketches) |
| **T3.3** crypto-agility + offline-default | ✅ approved | **LH-R7 + LH-R8 folded into `SOURCE/long-horizon-rationale.accepted.md` 2026-08-16** |
| **T3.4** graduate domain-contract | ⏸ **HELD** | on hold - "sleeping on it"; no schema graduation performed |
| **T3.5** generate the manifest | ✅ approved | **implemented**: `TOOLS/lore_build_manifest.py` (+ `--check`); `CORPUS-MANIFEST.yaml` regenerated (now accurate: 9 schemas, 2 registries, 16 tools); CI runs `--check`; validator 14/14 |
| **AI-002** volume sanity check | rescoped | per author: extended volumes (>~10) are derived from base docs + conversation nuggets (big effort / marginal gain) → core-only sanity check; extended = spot-check at most |

## T3.2 - proposed `AGENTS.md` §3.4 replacement wording (NOT applied; author-signed edit)

> **4. Scope Control**: No external network services, MCP/OPA/immudb infrastructure, federation
> layers, or autonomous execution agents may be **activated or added as running infrastructure**
> in phase-1. Phase-2 *designs* (e.g. the domain-contract and federation models) MAY be drafted as
> `candidate`/`proposed` artifacts under governance; they confer no authorization and add nothing
> to the enforced core until the author accepts (and signs) them.

## T3.3 - candidate long-horizon requirements (for `SOURCE/long-horizon-rationale.accepted.md`)

- **LH-R7 Cryptographic agility** *(candidate)* - integrity must survive its algorithms:
  signature/artifact formats carry an algorithm id + agility path; archival material is
  periodically re-attested; a signature's temporal validity is representable. *(from P6-2)*
- **LH-R8 Offline-default operation** *(candidate)* - federation/resolution must treat partition
  as the base case, not a failure mode: bounded-staleness trust, offline-verifiable revocation,
  eventual reconciliation. *(from P6-1)*
