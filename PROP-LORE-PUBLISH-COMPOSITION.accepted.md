# PROP Acceptance Skeleton — `lore publish` as composed multi-verb pipeline

**Decision / Prop ID:** PROP-LORE-PUBLISH-COMPOSITION-001  
**Status:** `accepted`  
**Date of Gate A decision:** 2026-08-22  
**Authority:** Author Gate A (“Promote the recommended minimum”) recorded 2026-08-22.  
Agent has drafted this skeleton under AGENTS.md rules. **Author remains sole authority** for final status change to `accepted`, signature, and any implementation.

**Source candidate:** `PROP-LORE-PUBLISH-COMPOSITION.candidate.md`  
**SHA-256 of source candidate:** `48da6fd88881c29f3e20f0b070dec2c219a403ea6fb706f9da13b73861270ee9`

---

## Author disposition (Gate A)

Author directed promotion of the recommended minimum on 2026-08-22.  
This skeleton records the intended acceptance content so the author can:

1. Review / lightly edit if needed.
2. Change status to `accepted` under author authority.
3. Produce the detached OpenPGP signature (Gate B).
4. Land the accepted record on the private corpus and (after export) on the public draft.

Until the author performs steps 2–3, this file remains a candidate.

---

## Intended accepted content (verbatim from candidate, ready for promotion)

**Status (to be set by author):** `accepted`  
**Date accepted:** 2026-08-22  
**Authority note:** Human author only. Agents do not acquire promotion or signing rights.

### Synopsis
Accept the composition of `lore publish` as a multi-verb pipeline that orchestrates existing `lore` verbs and fails closed. The verb eliminates required multi-step author choreography for turning a private corpus into the public draft while deliberately excluding commit/push, TR promotion, signing, and any status escalation.

### CLI
```text
lore publish [--dry-run] [--staging DIR] [--target DIR]
```

### Normative pipeline order
1. `lore export` (leak-scan CLEAN required; full relative paths)
2. `lore build-manifest` on staging
3. `lore validate` on staging (0 failed)
4. Review surface (`--dry-run` stops here with diff)
5. Materialize staging → target (only if gates passed and not dry-run)
6. `lore build-manifest` on target
7. `lore validate` on target
8. TR draft refresh (no auto-promote, no git commit/push)

### Explicitly out of scope (author-only)
- git commit / git push
- Promote TR draft → accepted
- Sign, tag, or cut a release
- Any status escalation to author-only statuses

### Design constraints (normative)
1. Orchestration only — prefer existing verbs.
2. Fail closed.
3. Staging is truth until materialize.
4. Manifest from the published tree only.
5. Preferred command form `lore publish`.
6. Preserve path correctness (full repo-relative paths).

### Implementation note
Register `publish` in the private `lore` dispatcher. Implementation lives private-side until a deliberate public subset is chosen. Reuse existing `lore_build_manifest.py` and export policy set.

### Acceptance tests (author)
1. `lore publish --dry-run` → CLEAN leak-scan, regenerated staging manifest, validate 0 failed, readable diff.
2. Live run materializes only after gates; target CORPUS-MANIFEST matches published tree.
3. No automatic git commit/push or TR promotion.
4. Deliberate failure aborts before target write.

---

## Remaining author actions for this item
- [ ] Review skeleton vs original candidate; edit if desired.
- [ ] Set status to `accepted` and record acceptance date / OMAAA note.
- [ ] Produce detached signature (Gate B).
- [ ] Register / land on private corpus.
- [ ] After publish pipeline runs, ensure the accepted record appears on public draft.

**Related ceremony:** `CEREMONY-2026-08-22-new-everything.runbook.candidate.md`
