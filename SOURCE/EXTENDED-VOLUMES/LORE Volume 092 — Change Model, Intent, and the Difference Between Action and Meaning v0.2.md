# LORE Volume 92 — Change Model, Intent, and the Difference Between Action and Meaning

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents change.

The purpose is to address a fundamental challenge:

> A system can record that something changed without understanding why it changed.

---

# 2. Core Principle

The governing principle:

> A change is not fully understood until the action, intent, authority, and resulting state are connected.

---

# 3. Change Philosophy

Systems experience constant change:

- configuration changes,
- ownership changes,
- authority changes,
- software updates,
- policy changes,
- operational decisions.

Recording the event alone is insufficient.

---

# 4. Change Definition

A change represents a transition from one meaningful state to another.

A complete change model includes:

```text id="m7q4vx"
Previous State

↓

Change Event

↓

New State

+

Intent

+

Authority

+

Context
```

---

# 5. Change vs Action

Important distinction:

```text id="q8n5mp"
Action

=

Something happened
```

```text id="x6m3qw"
Change

=

The resulting state transition
```

---

Example:

A command is executed.

The command is the action.

The modified access policy is the change.

---

# 6. Intent Model

Intent answers:

- Why was this change made?
- What outcome was expected?
- What constraints applied?

---

# 7. Intent vs Outcome

A critical distinction:

```text id="p9v5kr"
Good Intent

≠

Good Outcome
```

---

Example:

A security exception may be created to restore availability.

The intent may be valid.

The resulting exposure may still require review.

---

# 8. Authorized Change

A change should identify:

- initiating principal,
- approving authority,
- applicable policy,
- supporting evidence.

---

# 9. Unauthorized Change

A change may be unauthorized even if:

- technically successful,
- operationally useful,
- performed by a powerful account.

---

# 10. Change Context

A change requires context:

Examples:

- environment,
- timing,
- urgency,
- affected objects,
- dependencies.

---

# 11. Change History

A system should preserve:

- previous state,
- new state,
- actor,
- timestamp,
- rationale.

---

# 12. Change Reversal

Reversal is not always simple.

A later change may depend on the original change.

Example:

```text id="r7n4kp"
Change A

↓

Change B

↓

Attempted rollback
```

The system must understand dependencies.

---

# 13. Change and Lifecycle

Changes drive lifecycle transitions.

Examples:

- activation,
- suspension,
- expiration,
- retirement.

---

# 14. Change and Trust

Trust decisions often depend on recent changes.

Example:

```text id="v8m3qx"
Trusted System

+

Unknown Configuration Change

=

Reduced Confidence
```

---

# 15. Change Provenance

A change should preserve:

- who initiated it,
- what authorized it,
- what evidence supported it,
- what resulted.

---

# 16. Change in Autonomous Systems

Autonomous agents create new challenges.

Questions:

- Did the agent intend this action?
- Was the action within purpose?
- Was authority appropriate?
- Was the resulting state expected?

---

# 17. Change Review

Important changes may require:

- review,
- approval,
- validation.

---

# 18. Change Security Risks

Potential attacks:

## Change Injection

Introducing unauthorized modifications.

---

## Change Obfuscation

Hiding important modifications.

---

## Change Replay

Applying old changes incorrectly.

---

## Change Drift

Accumulating undocumented differences.

---

# 19. Change Failure Modes

Potential failures:

## Unknown Change

Something changed without attribution.

---

## Unintended Change

The action produced unexpected results.

---

## Incomplete Change

Only part of the intended transition occurred.

---

## Misinterpreted Change

The event was understood incorrectly.

---

# 20. Change Invariants

Candidate requirements:

## Invariant 1

Important changes SHOULD be attributable.

---

## Invariant 2

Changes SHOULD preserve before-and-after state.

---

## Invariant 3

Intent SHOULD remain distinguishable from outcome.

---

## Invariant 4

Authority for changes SHOULD be inspectable.

---

## Invariant 5

Significant changes SHOULD preserve history.

---

# 21. Review Questions

Reviewers should challenge:

1. What changes matter?
2. How is intent represented?
3. How are unexpected outcomes handled?
4. How are autonomous changes reviewed?
5. How do we distinguish improvement from harmful mutation?

---

# 22. Closing Principle

> A system that records only what changed can answer "what happened." A trustworthy system should also help answer "why did it happen?"

---

LORE Volume 92 — Change Model, Intent, and the Difference Between Action and Meaning v0.2.md

One-liner: **The change request said "minor update." The diff replied, "Define minor." The incident commander quietly opened a fresh coffee.**
