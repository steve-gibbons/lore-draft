# OBS Acceptance Skeleton — Public-draft placeholders + leak-scan self-reference

**OBS ID:** OBS-EXPORT-PLACEHOLDERS-AND-LEAKSCAN-SELFREF-001  
**Status:** `accepted`  
**Date of Gate A decision:** 2026-08-22  
**Authority:** Author Gate A (“Promote the recommended minimum”) recorded 2026-08-22.  
Agent has drafted this skeleton under AGENTS.md rules. **Author remains sole authority** for final status change to `accepted`, signature, and any public landing of the placeholder skeleton.

**Source candidate:** `OBS-EXPORT-PLACEHOLDERS-AND-LEAKSCAN-SELFREF.candidate.md`  
**SHA-256 of source candidate:** `f7ea2488c92c07a7cf6ce9df3a8a1e2a8e3bcffa894b730a9827388e78653595`

---

## Author disposition (Gate A)

Author directed promotion of the recommended minimum on 2026-08-22 (including this OBS as “accepted or light triage”).  
This skeleton records the intended acceptance content so the author can complete promotion + signature and decide the concrete export-path changes.

Until the author changes status and signs, this file remains a candidate.

---

## Intended accepted content

**Status (to be set by author):** `accepted`  
**Date accepted:** 2026-08-22  
**Authority note:** Human author only. Agents do not acquire promotion or signing rights.

### Synopsis
1. **Placeholder READMEs** for non-public / declared-but-empty directories are intentional and should be present on the public draft. They signal structure rather than leaving reviewers to infer layout from gaps.
2. **Leak-scan self-reference** (policy/genericize files matching their own private-marker patterns) is resolved by structural separation of concrete markers from exported policy docs (preferred) or by an audited pre-pass / explicit exclusion (acceptable short-term). Do not continue adding substitution rules whose `pattern:` lines themselves contain the matchable private markers.

### Normative implications on acceptance
- Public-export whitelist must allow *exactly* the placeholder README paths (and directory presence); never the directory contents.
- Export tooling adopts structural separation for private markers (or the short-term pre-pass) so the next export does not re-hit the self-reference.
- The placeholder skeleton already present in the working tree (`RELEASES/`, `ACTION_ITEMS/{open,resolved}/`, `LESSONS_LEARNED/candidates/`, `GUIDELINES/candidates/` + READMEs) is approved for inclusion in the next public export once the author lands it.

### What remains author implementation work
- Confirm or lightly edit the placeholder README texts.
- Update private-side export whitelist / `POLICY-EXPORT-*` to include exactly the new README paths.
- Implement the preferred structural separation (or short-term pre-pass) for private markers.
- Land the skeleton + this accepted OBS on the public draft via the publish pipeline.

---

## Remaining author actions for this item
- [ ] Review skeleton vs original candidate; edit if desired.
- [ ] Set status to `accepted` and record acceptance date / OMAAA note.
- [ ] Produce detached signature (Gate B).
- [ ] Confirm export whitelist + marker-separation approach.
- [ ] Include in the next `lore publish` / public-export run.

**Related ceremony:** `CEREMONY-2026-08-22-new-everything.runbook.candidate.md`
