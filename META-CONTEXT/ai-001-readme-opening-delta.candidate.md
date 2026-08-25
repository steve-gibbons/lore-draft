# AI-001 Candidate: README Opening Delta

> **Status: candidate**  
> **Addresses:** AI-001 (README vs 3/5/9 pitch pages)  
> **Date:** 2026-08-24  
> **Intent:** Raise slots 1, 2, 4, 5, and 7 without turning the README into a slide deck.

## Proposed replacement for the current opening block

Replace the existing material from the title through the first "No prior exposure needed" paragraph with the following. Everything after "## Try it (no install)" stays unchanged.

---

```markdown
# LORE - a governed-memory experiment

> **EXPERIMENTAL / PROVISIONAL.** For evaluation and demonstration of principles only - not
> production-ready. The licensing direction is recorded in
> [`DECISION-LICENSING.accepted.md`](DECISION-LICENSING.accepted.md) (evaluation-only now →
> Apache-2.0 + CC BY 4.0 at the **v1.0.0** milestone; the draft license text lives in the public
> draft repo).

> **Maintainers / developers:** local setup - clone, hooks, validator - is in
> [`DEVELOPMENT.md`](DEVELOPMENT.md).  **Reviewers:** start at [`REVIEWERS.md`](REVIEWERS.md).

**The problem.** Information survives. Context does not. When a decision, an assumption, or an
authority claim moves between people or agents, the *why*, the *who*, and the remaining uncertainty
are routinely stripped away. What remains looks complete and is not.

**The insight.** Trust is not a property of an artifact. It is a relationship among identity,
authority, evidence, and the boundary that crossed. Without those relationships made explicit and
unforgeable, later readers (human or agent) cannot tell justified action from plausible invention.

**What LORE is.** A small, self-contained framework for recording not just *what* a project decided,
but **why**, **who had the authority to decide it**, and **what is still uncertain** - in a form
that both people and AI agents can read, and that neither can quietly rewrite. Think "version control
for reasoning and authority," aimed especially at AI-agent workflows.

**Three load-bearing distinctions**
- **Thing ≠ reference** (ALIAS ≠ IDENTITY) - a pointer is never the object.
- **Claim ≠ evidence** (ASSERTION ≠ TRUTH) - an assertion stays agent-writable until human authority
  promotes it.
- **Authority ≠ capability** - the right to decide is not the same as the ability to act; both must
  carry lineage.

**One worked boundary failure.** An agent receives a design decision marked `accepted` from another
workbench. The status field is present, the text is coherent, and the file validates. Nothing in the
record binds the status to a registered signer. The receiving side promotes it. Later audit cannot
tell whether the original human actually authorized the decision or whether the status was simply
copied. LORE's Check 2 and the trusted-signers registry exist to make that forgery detectable.

**What LORE is not (explicit non-goals for this stage)**
- Not a live multi-tenant service or real-time collaboration platform.
- Not a replacement for enterprise GRC, IAM, or records-management systems.
- Not production-ready governance; the public draft is a freeze-cut evaluation artifact with bounded
  lag behind the private canonical tree.

This is the **public curated draft** of LORE (not the private canonical tree). Ask "which edition am
I on?" - see the release tag and `CORPUS-MANIFEST.yaml` `version:` field.

No prior exposure needed. Start below.
```

---

## Rationale for each addition

| Slot | Addition | Why it belongs in the README |
|------|----------|------------------------------|
| 1 Problem | "Information survives. Context does not." + short expansion | Must survive the 3-page cut; currently only implied |
| 2 Insight | "Trust is not a property of an artifact..." | Makes the relational claim explicit |
| 4 Distinctions | Three named distinctions with LORE terms | Packages material already present but scattered |
| 5 Boundary failure | Signature-less `accepted` status crossing workbenches | Concrete micro-scenario; directly motivates Check 2 |
| 7 Non-goals | Three explicit bullets | Converts existing provisional language into a clear list |

## What was deliberately left alone
- The "Try it" self-eval prompt (already strong mechanism desire)
- The audience table and directory map (architecture + expansion)
- All links into AGENTS, CORE-INVARIANTS, KNOWN-FINDINGS, etc.
- The experimental / provisional banner and licensing pointer

## Next step if accepted
Author reviews, edits if needed, then either:
1. Applies the delta directly to `README.md`, or
2. Promotes this candidate and opens a short PR that performs the replacement.

## Provenance
Drafted 2026-08-24 to close AI-001 gaps identified in the 3/5/9 mapping. Agent-generated under author direction. Status remains `candidate`.
