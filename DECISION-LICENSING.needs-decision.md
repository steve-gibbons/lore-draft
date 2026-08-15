# Decision Record — LORE Licensing (NEEDS-DECISION)

> **Status: needs-decision** (proposed; agent-drafted under author direction). The author (sole
> authority) has deferred the final choice for fresh eyes. This record preserves the *why* — the
> tensions, options, and recommended direction we can articulate now — so the decision, when made,
> is made in context. EXPERIMENTAL / provisional. Relates to **KF-14** (add LICENSE) and **KF-05**.
>
> **Decision-maker:** Author.  **Decision:** pending.

## The tension (stated plainly)
LORE holds two objectives that pull against each other, and the license is where they collide:
- **Adoption** — a governance/provenance *standard* only matters if it's implementable everywhere,
  royalty-free (cf. W3C / IETF / OWASP; also the threat-modeling-framework norm).
- **Anti-capture** — an explicit, recurring objective (21 mentions in the design source). LORE must
  resist a single actor co-opting it.

Permissive licenses maximize adoption; strong copyleft maximizes anti-capture by making the thing
hard to embed — which strangles the adoption LORE needs. The resolution differs by time horizon.

## What we know now
- **Dual nature:** LORE is a *specification/model* (AGENTS.md, schemas) **and** *reference tooling*
  (validator, assembler) — these often warrant different licenses.
- **AI-generated provenance:** much of the corpus originated in AI design conversations. In the US,
  purely AI-generated content may not be copyrightable; the protectable claim is strongest over
  human curation/arrangement and directed code. This *favors* permissive long-haul terms and
  transparency (which LORE's provenance discipline supports).
- **Immature governance:** the succession / community-governance model that would protect against
  premature capture does not yet exist (KF-05, KF-14). Releasing permissively *now* releases LORE at
  its most capturable moment.

## Options and impacts
| Option | Adoption | Anti-capture | Fit for LORE |
|---|---|---|---|
| **Apache-2.0 (code) + CC BY 4.0 (spec)** | High | Medium (patent grant + trademark clause) | **Strong long-haul** — implementable everywhere, real anti-capture teeth without copyleft's tax |
| **MPL-2.0** | Med-High | Med-High (file-level copyleft returns improvements) | Reasonable middle if anti-capture > adoption |
| **(A)GPL** | Low (enterprises avoid it for embedded frameworks) | High | Poor — anti-capture by unusability defeats the point |
| **Provisional Evaluation license (near-term)** | Restricted (review/eval/cite) | High (retains control) | **Strong near-term** while the model forms |
| **BUSL-style change-date → open** | Restricted now, open later | High now | Right mechanic; corporate baggage is a mismatch |

## Recommended direction (pending author ratification)
- **Near-term:** a short **"LORE Provisional Evaluation" license** — source-available for review,
  evaluation, and citation; no commercial use; no redistribution-as-your-own or derivatives
  presented as LORE — **with a stated intent to relicense** on exiting draft.
- **Long-haul:** **Apache-2.0** for code/tooling **+ CC BY 4.0** for the specification/docs.
- **Rationale:** near-term restriction matches the provisional scope and buys time to build the
  governance that prevents capture (KF-05/14); the long-haul target maximizes adoption while
  Apache's patent/trademark provisions carry the anti-capture load without copyleft's friction.

## The direction LORE commits to (proposed for ratification)
LORE **pre-commits, transparently, to an open future**: restricted while it forms, and Apache-2.0 +
CC BY 4.0 once it exits draft. Stating this commitment *now* — before the openness is legally
compelled — is itself the anti-capture and long-horizon-accountability posture LORE preaches: a
watcher making itself accountable in advance. The commitment is the point; the exact change-trigger
is the open sub-decision.

## Open sub-decisions for the author
1. Ratify the near-term Provisional Evaluation license (or pick a named one: PolyForm NC, BUSL)?
2. Ratify the long-haul target (Apache-2.0 + CC BY 4.0), or weight anti-capture higher → MPL-2.0?
3. What triggers the relicense — a version milestone (e.g. v1.0), a governance milestone (succession
   model exists), or a date?

## Provenance
Derived from: this session's licensing dialog, the corpus objectives (adoption + anti-capture +
long-horizon), and findings KF-05 / KF-14. Evidence-only recommendation; the author decides.
