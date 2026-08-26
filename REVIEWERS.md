# LORE - Reviewer Access

> **EXPERIMENTAL / PROVISIONAL.** This curated public draft is for demonstration of
> principles only - not production-ready, not for any other use.

Formal review is conducted against the **full private corpus**, not this curated public draft.

**To request reviewer access to the private repository, contact the author:**

**Steve Gibbons — steve_gibbons@icloud.com**

A brief note on your background or the lens you would bring is helpful; access is granted at
the author's discretion.

## Default review path

Start with [`MAP.md`](MAP.md), then the spine it lists (`README`, `AGENTS`, `CORE-INVARIANTS`,
ontology and auth decisions, `KNOWN-FINDINGS`). That is enough for corpus coherence and governance
evaluation of this draft.

## Optional: deployment / agent-tooling isolation

If your lens is **security architecture, threat model, or runtime isolation of agent tools**, you
may also request a peek at a **separate private operational demo** (not part of this tree):

`steve-gibbons/lore-mcp-decomposition-demo`

- Three-tier MCP shape: adapter / server / author (author path never in containers)
- Quarantine store ≠ main store; promote remains human-gated
- Read `architecture.md` and `threat-model.md` first if access is granted

**Non-claims:** it does not extend CORE-INVARIANTS; it is not required to review this public draft;
it is not a production multi-tenant product. Mention that lens when you write the author so access
can be scoped appropriately.
