# LL-002 - Operator context-confusion: distinguish trusted input surfaces

- **id:** LL-002
- **type:** anti-pattern  (lesson-learned)
- **status:** accepted  (in lifecycle: `candidates/` → author accepts → normative)
- **date:** 2026-08-15

> EXPERIMENTAL / provisional. Human-factors root of the evidence-mutation lessons (see LL-001,
> Vol 91). Approach accepted by author 2026-08-15; content entering the governed lifecycle.

## Problem
An operator running several look-alike assistant / terminal windows types (or pastes) input into
the **wrong** client - injecting content into the wrong trusted context. When the human is the
transport layer between LLMs (copy-paste pipelines), a mis-targeted window silently corrupts
provenance: content lands in the wrong conversation/corpus, and the mistake is easy to miss. This is
the human-factors substrate of the copypasta evidence near-misses (Vol 91) and of LL-001.

## Circumstance filters (applies when ALL hold)
- Multiple concurrent assistant / terminal / editor surfaces are open, AND
- the surfaces are **visually similar** (no distinct per-surface identity), AND
- the workflow is high-velocity / fatigued / repetitive (human-as-data-pipe, late-night, boring), AND
- input is typed or pasted **through** surfaces rather than isolated per task.

## Recipe (remedy under those circumstances)
1. Give each trusted input surface an **unmistakable visual identity** - a distinct color/theme:
   - **Browser clients:** one **browser profile per client** (distinct chrome color + avatar). *[primary]*
   - **macOS:** one **Space per client** with a distinct wallpaper; full-screen each.
   - Optional: a focused-window **colored-border** utility keyed per app.
2. Make **"which context am I in?"** a required pre-input check - the visual identity is the answer.
3. Prefer **task-isolated** surfaces over type-through pipelines where provenance matters.
4. Treat the visual cue as a *hint*, not proof: **CONTEXT_HINT ≠ TRUSTED_CONTEXT** - the cue lowers
   error rate; it does not authenticate the destination.

## Evidence
- The copypasta near-misses (Vol 91 anecdote): expedient edits in the wrong place, after midnight.
- Operator self-report (2026-08-15): "I often find myself typing into the wrong window."
- Multiple distinct assistant clients in active use (ChatGPT, Claude, Gemini, Perplexity, Grok) -
  see `INTAKE/raw/Gemini Integration/`, `INTAKE/raw/Perplexity Integration/` - raising confusion risk.

## Related
- **Volumes:** 62 / 79 (Human Factors, Usability), 91 (Evidence Preservation).
- **Concepts:** C08 (CONTEXT_HINT ≠ TRUSTED_CONTEXT), C22 (operator cognitive budget / human redline).
- **Lessons:** LL-001 (the downstream evidence-integrity failure this helps prevent).

## Lifecycle
- **candidate** (this file) → author review → **accepted** (promote out of `candidates/`) →
  **normative** (author-only). Promotion is author-only; this lesson does not self-promote.

## Provenance
- **inputs:** operator self-report; LL-001; Vol 91 anecdote; INTAKE/raw Gemini/Perplexity reports.
- **transformation:** human-factors observation → generalized lesson. Agent-drafted; author ratifies.
