---
id: DECISION-DEPLOYMENT-UPDATE-MODEL-001
type: decision-record
status: accepted
title: "Normative deployment & update model: snapshot + periodic handoff, NOT realtime"
decision_maker: "Author (Steve Gibbons), sole authority - ratified in-session 2026-08-16"
decided_at: "2026-08-16"
rationale: >
  Consumers must not carry realtime-update expectations for a LORE corpus. LORE is consumed as a
  point-in-time SNAPSHOT and updated by PERIODIC, rarely-interrupting conversation handoffs (an
  "edition" cadence, not a live feed). This matches the corpus's own direction - offline-default
  federation (P6-1 / candidate LH-R8), caching where "a cached object is not a new authority
  source" (Vol 7 §16), reduced-trust handoffs via CONTEXT_HINT (Vol 1 §17-18), and the recognised
  human-transport reality (INCIDENT_LOG §3.5). Documenting it prevents the failure mode of
  assuming live sync, which neither the interstellar/long-horizon envelope nor the everyday
  clone-the-repo case can provide.
provenance:
  created_by: agent
  under_author_direction: true
  author_preseeded: true
  signature_pending: "Ratified in-session by the author on stated authority 2026-08-16; detached signature per DECISION-AUTH-IDENTITY remains the author's environment step (not an agent-produced signature). A future author-signed edit may also mirror a short statement into README/AGENTS as normative text."
  inputs:
    - path: SOURCE/long-horizon-rationale.accepted.md
      sha256: af45ec8f82831baf70bd7f7619afa139e367aad689312b28a057f24dd6cf312b
    - path: "LORE-v0.5-package/SOURCE-VOLUMES/LORE Volume 1 - Core Ontology and Semantic Model.md"
      sha256: fe6397caafd4efe68134a06bc59294638803f45af37963646f7a6ae4898302ce
    - path: "LORE-v0.5-package/SOURCE-VOLUMES/LORE Volume 2 - Trust, Security, and Authorization.md"
      sha256: 215a3a35efa0220435f4824b21d194e83256f6a0f5881091e96f3226ce4e3aa7
    - path: "LORE-v0.5-package/EXTENDED-VOLUMES/LORE Volume 7 - Identifier, Namespace, and Federation Model v0.2.md"
      sha256: bcae1c8807f91a21614772e24fa2fcd1e1db51f545ecf5b6c9e9bdb789c487f7
    - path: INCIDENT_LOG.md
      sha256: f5fec8214ed43b375e349da416ad44fbdd92a9dde4b670f3707db650c7e04e00
---

> **ACCEPTED - author-ratified in-session 2026-08-16 on stated author authority.** Agent-drafted
> under author direction; the detached signature per `DECISION-AUTH-IDENTITY` remains the author's
> step (see `provenance.signature_pending`). EXPERIMENTAL / provisional like the rest of the corpus.

# 1. Decision (proposed)

LORE's normative deployment and update model is **snapshot deployment + periodic
conversation-handoff updates**, and is explicitly **not realtime**.

## 1.1 Snapshot deployment
A consumer deploys a **point-in-time snapshot** of the corpus - a clone/copy at a released
version. The snapshot is **self-contained and operable offline**; it assumes no live connection
to a source of truth. A snapshot is identified by its **version/edition** (and should be pinnable
to a manifest hash, now that `CORPUS-MANIFEST.yaml` is generated - T3.5). What you deployed is
what you run until you take a new snapshot.

## 1.2 Periodic conversation-handoff updates
Updates propagate as **periodic, batched handoffs** - an *edition* cadence, **rarely
interrupting** normal operation. A handoff is not a hot-patch: it lands at **reduced trust**
(`CONTEXT_HINT` / `evidence-only` / `quarantined`; Vol 1 §17-18) and is **reviewed and promoted
on the consumer's own schedule**. Between editions the deployed snapshot is stable and unchanged.

## 1.3 No realtime expectations
Consumers **MUST NOT** expect realtime propagation. **Bounded staleness is the normal, designed
condition**, not a fault: federation revocation/propagation is not instantaneous (Vol 7 §18,
Vol 36 §17), a cached object "is not a new authority source" (Vol 7 §16), and the transport may
literally be a human moving text between contexts (INCIDENT_LOG §3.5). Freshness is therefore a
property to **reason about** (trust decay, Vol 2 §8), never a guarantee to assume.

# 2. Why (expectation-setting)

The single most damaging wrong assumption a consumer can make is "this is live." It is not - not
at interstellar distances (the long-horizon envelope, candidate LH-R8 offline-default), and not
on a laptop that cloned the repo last month. Stating the model plainly means a consumer knows to
ask *"which edition am I on, and when was it cut?"* rather than assuming continuous truth.

# 3. Implications

- **Edition labelling.** Every snapshot should carry a legible version/edition + cut date; a
  consumer must be able to answer which edition it holds. (The generated manifest gives a stable
  hashable index to anchor this.)
- **Reduced-trust intake.** Handoffs enter as `evidence-only`/`quarantined` and are promoted by
  the consumer's authority - never auto-accepted (preserves the authority boundary across the gap).
- **History across editions.** Supersede-not-delete means an edition bump preserves prior
  rationale, so a consumer can reconstruct *why* between editions.
- **Aligns the roadmap.** This is the everyday, terrestrial statement of the same property the
  long-horizon findings need (P6-1 offline-default; candidate LH-R8) - one model, both scales.

# 4. Where this belongs once ratified (author-signed edits)

- A short normative statement in `README.md` / `AGENTS.md` (the deployment/consumption model).
- Fold **LH-R8 (offline-default)** into `SOURCE/long-horizon-rationale.accepted.md` as the
  long-horizon face of the same rule.
- Operational note added now (non-normative) in `REPO-OPERATING-NOTES.md`.

# 5. Provenance & scope
Drafted under author direction (2026-08-16). Grounded in the cited artifacts; no realtime/live-sync
capability is claimed anywhere in the corpus. Tracked in `INTEGRATIONS/OPEN-DECISIONS-REGISTER.md`.
Author is sole authority for ratification and signature.
