# Decision Record - LORE Licensing (DECIDED)

> **Status: accepted - direction decided, provisional in legal form** (author-ratified 2026-08-15;
> agent-drafted under author direction). The author (sole authority) reviewed with fresh eyes and
> ratified the direction below; what remains is non-substantive legal polish, not a pending choice.
> Relates to **KF-14** (add LICENSE) and **KF-05** (governance / succession).
>
> **Decision-maker:** Author.  **Decision (2026-08-15):** near-term = the Provisional Evaluation
> license (drafted at `LICENSE.DRAFT.md`, *by principals only*); long-haul = Apache-2.0 (code/tooling)
> + CC BY 4.0 (spec/docs); **trigger = the v1.0.0 milestone, gated on governance lock-in** (v1.0.0 does not ship until the succession / anti-capture governance model is locked). Remaining is implementation only:
> legal review of the provisional text, rename `LICENSE.DRAFT.md → LICENSE`, and the non-license
> anti-capture controls noted below.

## The tension (stated plainly)
LORE holds two objectives that pull against each other, and the license is where they collide:
- **Adoption** - a governance/provenance *standard* only matters if it's implementable everywhere,
  royalty-free (cf. W3C / IETF / OWASP; also the threat-modeling-framework norm).
- **Anti-capture** - an explicit, recurring objective (21 mentions in the design source). LORE must
  resist a single actor co-opting it.

Permissive licenses maximize adoption; strong copyleft maximizes anti-capture by making the thing
hard to embed - which strangles the adoption LORE needs. The resolution differs by time horizon.

## What we know now
- **Dual nature:** LORE is a *specification/model* (AGENTS.md, schemas) **and** *reference tooling*
  (validator, assembler) - these often warrant different licenses.
- **AI-generated provenance:** much of the corpus originated in AI design conversations. In the US,
  purely AI-generated content may not be copyrightable; the protectable claim is strongest over
  human curation, arrangement, and directed code, not over mere prompting (cf. US Copyright Office
  AI guidance). This *favors* permissive long-haul terms and transparency (which LORE's provenance
  discipline supports).
- **Immature governance:** the succession / community-governance model that would protect against
  premature capture does not yet exist (KF-05, KF-14). Releasing permissively *now* releases LORE at
  its most capturable moment.

## Options and impacts
| Option | Adoption | Anti-capture | Fit for LORE |
|---|---|---|---|
| **Apache-2.0 (code) + CC BY 4.0 (spec)** | High | Low-Medium (contributor patent grant; trademark rights withheld, not a capture defense) | **Strong long-haul** - implementable everywhere; patent grant + attribution, but capture must be handled outside the license |
| **MPL-2.0** | Med-High | Med-High (file-level copyleft returns improvements) | Reasonable middle if anti-capture > adoption |
| **(A)GPL** | Low (enterprises avoid it for embedded frameworks) | High | Poor - anti-capture by unusability defeats the point |
| **Provisional Evaluation license (near-term)** | Restricted (review/eval/cite) | High (retains control) | **Strong near-term** while the model forms |
| **BUSL-style change-date → open** | Restricted now, open later | High now | Right mechanic; corporate baggage is a mismatch |

## Decided direction (author-ratified 2026-08-15)
- **Near-term:** a short **"LORE Provisional Evaluation" license** - source-available for review,
  evaluation, and citation; no commercial use; no redistribution-as-your-own or derivatives
  presented as LORE - **with a stated intent to relicense** on exiting draft.
- **Long-haul:** **Apache-2.0** for code/tooling **+ CC BY 4.0** for the specification/docs.
- **Rationale:** near-term restriction matches the provisional scope and buys time to build the
  governance that prevents capture (KF-05/14). For the long-haul target, Apache-2.0 supplies a
  contributor patent grant and *preserves* (does not license) trademark rights, and CC BY 4.0
  supports broad reuse with attribution - together maximizing adoption. Neither license alone
  prevents governance, brand, or ecosystem capture, so anti-capture is **not** delegated to license
  terms: it requires separate trademark, conformance, and stewardship controls (see below).

## The commitment (author-ratified)
LORE **pre-commits, transparently, to an open future**: restricted while it forms, and Apache-2.0 +
CC BY 4.0 once it exits draft at **v1.0.0**. Stating this commitment *now* - before the openness is
legally compelled - is itself the anti-capture and long-horizon-accountability posture LORE
preaches: a watcher making itself accountable in advance. The commitment is the point, and the
change-trigger is set: the v1.0.0 milestone, which is itself gated on governance lock-in - LORE does
not go open until the mechanism that prevents capture actually exists.

## Resolved sub-decisions
1. **Near-term license: ratified** - the Provisional Evaluation license (`LICENSE.DRAFT.md`), not a
   named NC/BUSL license.
2. **Long-haul target: ratified** - Apache-2.0 + CC BY 4.0 (adoption weighted above MPL-2.0's
   stronger copyleft).
3. **Relicense trigger: ratified** - the v1.0.0 milestone, *gated on governance lock-in*: v1.0.0 does
   not ship until the succession / anti-capture governance model is functionally locked. The
   auditable version tag carries a structural precondition rather than standing as an arbitrary
   state - reconciling "mechanically bindable" with "triggered by a structural reality."

## Remaining implementation work (non-substantive)
- **Legal review of the provisional text:** state grants, prohibitions, term, revocation/change
  mechanics, governing law, and treatment of contributions; and *explicitly* permit ordinary
  evaluation activities so "source-available for review" is not ambiguous - quoting excerpts,
  mirroring an unmodified copy, filing issues/patches, running the tooling internally, and
  publishing independent critique.
- **Rename `LICENSE.DRAFT.md → LICENSE`** at ratification of the final text.
- **Non-license anti-capture controls** (tracked under KF-05 governance; not blocking this decision).
  Licenses address only part of the capture surface (name/mark, governance, standards, and
  implementation capture). The controls that cover the rest:
  - *Trademark policy* - reserve the "LORE" name/marks; allow descriptive/nominative use; gate
    claims like "official," "certified," or "LORE-compatible" on conformance.
  - *Conformance governance* - define how an implementation earns compatibility status via published,
    versioned tests.
  - *Stewardship / succession* - an authority-transfer process, contributor policy, and amendment
    rules before the project depends on a single author.
  - *Specification versioning* - anyone may fork under CC BY, but only an authorized steward may
    publish a version as the *canonical* LORE specification.

## Provenance
Derived from: this session's licensing dialog, the corpus objectives (adoption + anti-capture +
long-horizon), and findings KF-05 / KF-14. External review (Perplexity, 2026-08-15) contributed the
Apache-2.0 / CC BY 4.0 trademark-and-patent correction and the non-license anti-capture control
stack; external review (Gemini, 2026-08-15) prompted gating the v1.0.0 relicense trigger on
governance lock-in. Evidence-and-decision record; the author is the sole authority.
