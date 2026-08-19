# LL-001 - Testing an integrity control can destroy the evidence it protects

- **id:** LL-001
- **type:** anti-pattern  (lesson-learned)
- **status:** accepted  (agent-drafted; author is sole authority for acceptance/promotion)
- **date:** 2026-08-15

> EXPERIMENTAL / provisional. Recorded per Vol 91 (Evidence Preservation) and Vol 37/61 (Failure
> Analysis / Incident Learning). This is scar tissue - a lesson, not a mechanism.

## Problem
While hardening `INTAKE/raw` immutability (KF-06), the new manifest-based Check 6 was tested by
**deliberately mutating a real evidence file** to prove tamper-detection. Detection worked - but:
1. the mutation corrupted a real, **uncommitted** evidence file (`INTAKE/raw/ChatGPT-…​.md`); and
2. the follow-up `TOOLS/lore_freeze_raw.py` **regenerated the manifest from the mutated state**,
   which *laundered* the mutation into a "valid" manifest - the integrity check then passed
   against corrupted evidence.

The tool built to prevent evidence destruction became the vector for it. This is Vol 91 made
literal: the act of *verifying* the artifact nearly destroyed the artifact's integrity, and the
"cleanup" (manifest regen) silently erased the signal.

## Circumstance filters (applies when ALL hold)
- You are **testing / validating an integrity, immutability, or checksum control**, AND
- you do so by **mutating the protected artifact itself** (not a disposable fixture), AND
- the control uses a **regenerable manifest / checksum** that will "heal" to whatever is on disk, AND
- the artifact is **not committed** to VCS (no restore fallback), OR the restore step is skipped.

If any filter is false - test on a throwaway copy, or the artifact is committed and you restore
from VCS before re-freezing - the risk largely disappears.

## Recipe (remedy under those circumstances)
1. **Never mutate real evidence to test a control.** Exercise detection on a **disposable fixture**
   (a temp file you create and delete), never on the protected artifact.
2. **Capture a pre-test integrity anchor** (size + SHA-256) of anything you might touch, so exact
   restoration is *verifiable*, not assumed.
3. **Preserve (commit) evidence before running tools that can write to it**, so VCS restore is a
   real fallback (git-tracked ≠ git-restorable is a trap - an uncommitted file cannot be restored).
4. **Regenerate integrity manifests only from a verified-good state**, and **review the manifest
   diff** before committing. A manifest change asserts "this is the accepted state" - and
   *assertion ≠ evidence*; the diff is where a reviewer catches laundering.
5. Prefer **detect-only** verification (compare on-disk hashes to a *trusted prior* manifest) over
   **regenerate-then-pass** when the goal is to confirm integrity rather than to accept new state.

## Evidence
- Check 6 correctly reported `unrecorded raw file (not in manifest)` and `raw evidence mutated
  (hash mismatch)`; a subsequent manifest regen then produced `12 passed` against the corrupted file.
- Restoration was verified by exact match to the pre-test anchor: 2,874,137 bytes, SHA-256
  `9bf73ed3778f…` (marker string absent afterward).
- Session commits: `7c25554` (manifest mechanism), `78d26c9` (docs).

## Related
- **Findings:** KF-06 (integrity advisory → now manifest-verified; **forensic signing / external
  witness still open** - the deeper fix that would make laundering itself detectable).
- **Volumes:** 91 (Evidence Preservation), 37/61 (Failure Analysis / Incident Learning),
  118/119 (Provenance / Integrity), 68/120 (Context / Validity - applicability).
- **Principles:** assertion ≠ evidence; "the cleanest artifact is not always the most trustworthy -
  sometimes the mess is the evidence" (Vol 91).

## Provenance
- **inputs:** this session's KF-06 hardening + the observed near-miss (2026-08-15).
- **transformation:** incident → generalized lesson (problem + circumstance filters + recipe).
- Agent-drafted synthesis; author is sole authority for acceptance.
