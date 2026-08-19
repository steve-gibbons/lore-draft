---
id: DECISION-ONTOLOGY-CANONICAL-KERNEL-001
type: decision-record
status: accepted
title: "Canonical LORE ontology: three layers (object → parts-of-speech → LORE types), with the accountability invariant"
decision_maker: "Author (Steve Gibbons), sole authority - ratified in-session 2026-08-16 (OMAAA)"
decided_at: "2026-08-16"
rationale: >
  Three vocabularies had diverged (the shipped seven-kind workbench kernel, the Vol 1 §3
  ontology, and the Check-4 enforcement built from Vol 1), and none had a base class or a
  linguistic grounding. This decision sets a THREE-LAYER type system: (0) `object` describes
  anything; (1) an ontological/linguistic layer of parts of speech + operators + punctuation;
  (2) the LORE-specific types that specialize layer 1. It restores fundamentals that were
  dropped in the rush to an end-to-end demo - `principal`, `policy`, and above all the
  ACCOUNTABILITY invariant (a thing cannot be accountable). Supersedes the enumerated set in
  DECISION-ONTOLOGY-ENFORCEABILITY-001 / CORE-INVARIANT 12 (both Vol 1-keyed). Surfaced by the
  Siri (macOS) read of the workbench code plus the author's parts-of-speech sidebar.
provenance:
  created_by: agent
  under_author_direction: true
  author_preseeded: true
  author_authority_token: "OMAAA (on my authority as author) - in-session ratification 2026-08-16"
  signature_pending: "Detached signature per DECISION-AUTH-IDENTITY remains the author's environment step (./lore sign); not agent-produced."
  inputs:
    - path: TOOLS/lore_common.py
      note: "KERNEL_KINDS (the shipped seven-kind kernel this reconciles)"
    - path: "LORE-v0.5-package/SOURCE-VOLUMES/LORE Volume 1 - Core Ontology and Semantic Model.md"
      sha256: fe6397caafd4efe68134a06bc59294638803f45af37963646f7a6ae4898302ce
    - path: WORKBENCH/CONTRACT.md
      note: "documents the seven-item semantic kernel + object-envelope"
    - path: DECISION-ONTOLOGY-ENFORCEABILITY.accepted.md
      note: "superseded set (Vol 1-keyed); this record re-keys it"
  transformation: "author design ruling: layered type system + accountability invariant, reconciling kernel, Vol 1, and Check-4 enforcement."
---

> **ACCEPTED - author-ratified in-session 2026-08-16 (OMAAA).** Agent-drafted under author
> direction; detached signature per `DECISION-AUTH-IDENTITY` pending. EXPERIMENTAL / provisional.
> Layer-1/2 placements marked *(proposed)* are the agent's mapping of the author's sketch and are
> open to correction; the layer model, the named placements, and the accountability invariant are
> author-confirmed.

# 1. The three-layer type system

```
Layer 2  LORE TYPES        the specific kinds LORE cares about (trust/governance vocabulary)
              ▲            e.g. principal, policy, assertion, evidence, evaluation,
              │            authority, capability, act, event, relationship, object-ref, alias
Layer 1  ONTOLOGICAL       parts of speech + operators + punctuation (generic grammar of "anything")
              ▲            nouns · verbs · operators · punctuation
              │
Layer 0  OBJECT            the abstract base: "describes anything" (envelope only:
                           id, kind, subkind?, status, provenance, content-sha). Never stored bare.
```

- **Layer 0 - `object`** is the abstract base (decision Q3). Everything is an object; nothing is
  stored as a bare object. Embodied by `WORKBENCH/schemas/object-envelope.yaml`.
- **Layer 1 - the ontological/linguistic layer** classifies any object by grammar: **nouns**
  (people, places, things, ideas), **verbs** (actions), **operators** (that relate/compose), and
  **punctuation** (structural markers). LORE Core *layers on top of* this; it does not reinvent it.
- **Layer 2 - LORE types** specialize layer 1 with the vocabulary LORE governs.

# 2. Parts of speech → LORE types

| Layer 1 (grammar) | Layer 2 (LORE types) | Notes |
|---|---|---|
| **noun** | `thing`, plus person / place / idea | `thing` is a noun (author-confirmed); nouns = people, places, things, ideas |
| noun (identity-bearing) | **`principal`** | a person or thing with an assigned identity - the basis for its authorization & capabilities, evaluated against policies |
| noun (rule) | **`policy`** | a kind of thing that governs authorization/capability decisions |
| noun (right) *(proposed)* | `authority`, `capability` | rights/permissions; **enforced separately** (see §4) |
| **verb** | **`act`** (action); **`event`** = an act with a **trigger** (temporal) | act = the verb LORE cares about; event ⊂ act |
| **operator** *(proposed)* | `relationship`, `object-ref` | relate/compose or indirect between nouns |
| **punctuation** *(proposed)* | `alias`, envelope framing | naming / structural markers; ALIAS ≠ IDENTITY |
| proposition *(proposed)* | `assertion` → `evidence`, `evaluation`, `context-hint` | a claim (subject+predicate); ASSERTION ≠ TRUTH |

*(proposed)* rows are the agent's placement of kinds the author didn't explicitly locate - confirm or move.

# 3. The object hierarchy (stored kinds)

```
object                         ABSTRACT (Layer 0; never stored bare)
├── principal                  identity-bearing noun; drives authz/capability via policy
├── policy                     rule-noun; governs decisions
├── thing                      = a noun / "what the chemistry exposes" — a projection (NOT stored; see §5)
├── object-ref                 pointer; OBJECT_REF ≠ OBJECT
│   └── (subkind) alias        named ref; ALIAS ≠ IDENTITY
├── relationship               typed edge: subject —predicate→ object
├── act                        a verb / action
│   └── (subkind) event        an act with a trigger (temporal)
├── assertion                  a claim; ASSERTION ≠ TRUTH (agent-writable status only)
│   ├── (subkind) evidence     assertion backed by observation (source/method/collected)
│   ├── (subkind) evaluation   assertion that judges (criteria/verdict/confidence)
│   └── (subkind) context-hint UNTRUSTED assertion handed off for interpretation  (#2 CONFIRMED)
├── authority                  right to grant/decide; has lineage — ENFORCED SEPARATELY
└── capability                 bounded permission to act — ENFORCED SEPARATELY
```

Subtyping encoded as **`kind` + `subkind`** (decision Q5).

# 4. The ACCOUNTABILITY invariant (candidate CORE-INVARIANT 13)

> **Accountability requires a human.** A `thing` (any non-human principal, an agent included)
> **cannot be held accountable**; therefore it **must never make permanent decisions nor take
> risky / irreversible actions on its own**. The **Accountable** role - the **A** in RASIC - is
> always a **human principal**. Agents may be Responsible, Support, Consulted, or Informed, never
> Accountable.

This is the *why* beneath LORE's entire authority model: author-only statuses, no unilateral
promotion, non-escalating break-glass, transport→quarantine-only. It ties the ontology
(`principal`, `thing`) to the governance boundary (`authority`, `capability`, gates). Proposed for
signature into `CORE-INVARIANTS.md` as invariant 13 (author to ratify + sign).

# 5. Derived projections (NOT stored) & `state` vs `status`
- **`thing`** and **`state`** are derived projections, not stored kinds (Q4). Multiple `state`s may
  hold for one object simultaneously.
- **`status`** = the single, closed, authority-gated governance lifecycle value
  (`REGISTRIES/artifact-statuses.yaml`); exactly one per object. **`state`** = derived, plural
  domain conditions. Different axes; never conflate.

# 6. Resolved design questions
| Q | Ruling |
|---|--------|
| 1 act/event | `act` = verb; `event` ⊂ `act` = act + trigger. |
| 2 context | **CONFIRMED** - `context-hint` is an untrusted `assertion` subkind; "trusted context" = a promoted assertion. |
| 3 object | **Abstract** base; all others are flavors of object. |
| 4 state | **Derived**, multiple simultaneous; distinct from `status`. |
| 5 subtyping | **`kind` + `subkind`**. |

# 7. Mapping (canonical ↔ kernel ↔ Vol 1 ↔ current Check 4)
| Canonical | Kernel | Vol 1 | Check 4 today | Delta |
|---|---|---|---|---|
| object (abstract) | — | object | object | make abstract, not a stored kind |
| principal | — | (principal, Vol 105) | **missing** | **add** |
| policy | — | (policy, Vol 114) | **missing** | **add** |
| object-ref / alias | — | object-ref / alias | ✅ / ✅ | alias→subkind |
| relationship | relationship | relationship | ✅ | keep |
| act / event | act | event | event | rename event→act; event→subkind(+trigger) |
| assertion | assertion | assertion | ✅ | keep |
| evidence / evaluation | evidence / evaluation | evidence / — | ✅ / **missing** | subkinds; **add evaluation** |
| context-hint | — | context | context | re-key under assertion |
| authority / capability | — | authority / capability | ✅ / ✅ | keep, separate enforcement |
| thing / state | thing / state (stored) | object / lifecycle | (object) / **missing** | **projections, not stored** |

# 8. Follow-up implementation - ✅ IMPLEMENTED 2026-08-16 (Phase 1 governance + Phase 2 workbench)
> All steps below are DONE. Validator 38/0, manifest `--check` clean, `demo.sh` smoke green.
> Residual: the author's detached signature over the settled state, and confirmation of the
> *(proposed)* layer-1/2 placements in §2.
1. `TOOLS/lore_common.py`: `KERNEL_KINDS` → canonical stored kinds + `SUBKINDS`; `thing`/`state`
   become projections. Add `principal`, `policy`.
2. Re-key `SCHEMAS/` + `lore_validate.py` Check 4 to the hierarchy (kind+subkind); add `principal`,
   `policy`, `evaluation`; fold `alias`→object-ref, `context`→assertion(context-hint); rename
   `event`→`act(+event)`; keep `authority`/`capability` separate.
3. **Rewrite CORE-INVARIANT 12** to name the canonical set; **add candidate CORE-INVARIANT 13**
   (accountability) for author signature.
4. Update `WORKBENCH/CONTRACT.md` + `lore_explain.py` (seven-item kernel → this layered model).
5. Re-point fixtures; regenerate manifest (T3.5 auto-indexes); re-validate.
6. Record Vol 1 §3 as superseded/conceptual by this canonical model.

# 9. Relationship to prior records & scope
Supersedes the enumerated set in `DECISION-ONTOLOGY-ENFORCEABILITY-001` and CORE-INVARIANT 12; the
*principle* (ontology represented + enforced, extended only via a domain contract) stands.
**Out of scope here:** the deployment/isolation architecture (surfaces → protocol/adapters →
kernel → repo/share; MCP/ACP/model-front-end containers; quarantine edge; author sign path) - that
is a separate concern; capture it in its own record (`DECISION-DEPLOYMENT-ISOLATION`) if desired.
Tracked in `INTEGRATIONS/OPEN-DECISIONS-REGISTER.md`.
