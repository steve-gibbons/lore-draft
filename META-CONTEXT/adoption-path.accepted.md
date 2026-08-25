# Minimal Viable Adoption Path for LORE

> **Status: accepted**  
> **Addresses:** KF-13 (No integration surface / adoption path / scale story)  
> **Authority:** Accepted by author 2026-08-25.  
> **Date:** 2026-08-24 (drafted) / 2026-08-25 (accepted)

## Purpose
Provide a concrete, low-friction path for an organization or individual to start using LORE without requiring the full future federation, API surface, or enterprise connectors. This is the "first useful step" that was missing.

## Audience
- Security / architecture teams evaluating LORE for design records and agent governance
- Maintainers of AI-agent workflows who need auditable authority and evidence
- Reviewers who need a clear on-ramp before deeper engagement

## Minimal Viable Adoption (three levels)

### Level 0 - Read-only evaluation (zero install cost)
1. Clone or browse the public draft repository.
2. Point any capable agent at the top-level directory and issue:
   > Use LORE to evaluate LORE.
3. Compare the agent's findings against `KNOWN-FINDINGS.md`.
4. Run the validator locally if desired:
   ```bash
   python3 TOOLS/lore_validate.py
   ```
No schema changes, no new infrastructure, no commitment.

### Level 1 - Local governed notebook (single maintainer or small team)
1. Fork or clone the public draft (or the private canonical tree if authorized).
2. Install the pre-commit hook (see `DEVELOPMENT.md`).
3. Treat `INTAKE/raw/` as the immutable landing zone for external evidence.
4. Create design decisions, proposals, and evaluations as LORE records using the existing schemas and status enum.
5. Use `lore validate` (or the python entry point) before every commit.
6. Promote only under human author authority (signature-bound per DECISION-AUTH-IDENTITY).

This level already delivers:
- closed status transitions
- authority boundary (author-only statuses)
- transformation provenance
- evidence integrity via the raw manifest
- self-describing ontology

### Level 2 - Team or project-scoped use (still flat-file)
1. Share a single LORE corpus repository among a small set of humans.
2. Register additional trusted signers in `REGISTRIES/trusted-signers.txt`.
3. Adopt the reviewer-panel hats (`TOOLS/lore_prompt.py`) for structured reviews.
4. Keep the corpus under the same validator and status rules.
5. Use git history + the SHA-256 manifests as the audit trail.

No new runtime services are required. Scale remains "one validator + one repo".

## What is deliberately out of scope for MVP
- Real-time APIs or MCP servers (phase-2 design only)
- Automatic federation or cross-corpus trust
- Enterprise connectors (IAM, GRC, CMDB)
- Multi-tenant or multi-organization governance
- Event-sourcing projection stores beyond the existing file + git model

These remain future work; the MVP path does not depend on them.

## Success criteria for this finding
- A new reader can go from "what is LORE?" to "I can keep my next design decision under LORE governance" in under one working session.
- The path is explicit in the repository and does not require private knowledge.
- No change to the core invariants or validator is required for Level 0/1.

## Related
- `README.md` orientation table
- `DEVELOPMENT.md` local setup
- `AGENTS.md` authority model
- `CORE-INVARIANTS.md`
- KF-07 (agent-consumption contract remains phase-2)
- KF-09 / KF-15 (prior-art and data-architecture mappings; both accepted)

## Provenance
Drafted 2026-08-24 as the first fast-follower clean-up item for KF-13. Agent-generated under author direction. Accepted by author 2026-08-25.
