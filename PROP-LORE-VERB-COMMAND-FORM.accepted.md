# PROP-LORE-VERB-COMMAND-FORM.accepted.md

**Status:** accepted
**Date:** 2026-08-23
**Authority:** author
**Decision / proposition ID:** PROP-LORE-VERB-COMMAND-FORM-001
**Prior candidate:** PROP-LORE-VERB-COMMAND-FORM.candidate.md (2026-08-18)

---

## Decision

Agents operating under LORE MUST prefer the unified CLI form

    lore <verb> [args...]

whenever the corresponding verb is registered under the lore entry-point.

Fall back to the explicit python3 TOOLS/lore_*.py path only when:

- the unified lore entry-point is absent, or
- the required verb has not yet been registered.

Agents MUST NOT invent verbs. Missing verbs are to be surfaced so they can be registered deliberately.

## Rationale

- Reduces path hard-coding and surface-specific drift across agent surfaces.
- Clarifies the public/private tool boundary (only deliberately registered verbs appear under lore).
- Preserves the "do not - Preserves the "do not - Preserves the "do not - P b- Preserves the "do not - Preserves the "do not - Preserves- - Preserves the "do not - Preserves the binary.
- Does not change any tool behaviour — only preferred invocation form.
- Does not grant agents new authority.

## Provenance

- Author request 2026-08-18.
- Candidate drafted 2026-08-18; rule landed via PR #1 on lore-draft and is already present in AGENTS.md on both private and public mains.
- Accepted 2026-08-23 by author signature.
