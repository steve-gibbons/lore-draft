# LORE Volume 98 - Context Model, Meaning, and Situational Awareness

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents context.

The purpose is to address a fundamental challenge:

> Information without context can be technically correct while still producing incorrect decisions.

---

# 2. Core Principle

The governing principle:

> Meaning depends on context. A fact removed from its context may become misleading.

---

# 3. Context Philosophy

Systems frequently process:

- identities,
- permissions,
- data,
- events,
- policies,
- decisions.

However, these elements do not exist independently.

Their meaning depends on:

- environment,
- purpose,
- time,
- relationships,
- assumptions.

---

# 4. Context Definition

Context represents the conditions and circumstances that give meaning to an object, assertion, relationship, or decision.

---

# 5. Context Structure

Context may include:

```text id="m7q4vx"
Environment

+

Purpose

+

Time

+

Participants

+

Constraints

+

Relevant History
```

---

# 6. Context Example

The statement:

```text id="q8n5mp"
"Administrator access is allowed"
```

is incomplete.

Relevant context:

```text id="x6m3qw"
Who:

Security Administrator


Where:

Production Environment


When:

Approved Maintenance Window


Why:

Emergency Recovery
```

---

# 7. Context vs Data

Important distinction:

```text id="p9v5kr"
Data

=

Recorded information
```

```text id="r7n4kp"
Context

=

Meaning surrounding information
```

---

# 8. Context vs State

Another distinction:

```text id="v8m3qx"
State

=

What exists now
```

```text id="k4p8mw"
Context

=

Why the current state matters
```

---

# 9. Context Layers

Potential context layers:

## Technical Context

Examples:

- architecture,
- configuration,
- dependencies.

---

## Operational Context

Examples:

- current activity,
- maintenance,
- incidents.

---

## Security Context

Examples:

- threat level,
- authorization,
- risk.

---

## Organizational Context

Examples:

- ownership,
- responsibility,
- business purpose.

---

# 10. Context Preservation

Important context should survive:

- changes,
- migrations,
- recovery,
- handoffs.

---

# 11. Context Loss

A major failure mode:

```text id="wye826"
Information Preserved

+

Context Lost

=

Potentially Incorrect Meaning
```

---

# 12. Context and Automation

Automation frequently fails when it receives:

- valid data,
- invalid assumptions.

---

# 13. Context and AI Systems

AI systems make context especially important.

An agent should understand:

- what task it is performing,
- why it is performing it,
- what limitations apply,
- what information is relevant.

---

# 14. Context Windows

A practical challenge:

Systems often have limited context.

Therefore they must determine:

- what context matters,
- what can be omitted,
- what must be preserved.

---

# 15. Context Selection

Context selection should consider:

- decision impact,
- relevance,
- freshness,
- authority.

---

# 16. Context Security Risks

Potential attacks:

## Context Poisoning

Introducing misleading surrounding information.

---

## Context Stripping

Removing important conditions.

---

## Context Substitution

Replacing the original situation with a different one.

---

## Context Overload

Providing excessive irrelevant information.

---

# 17. Context Failure Modes

Potential failures:

## Missing Context

Decision lacks necessary information.

---

## Incorrect Context

Information is paired with the wrong situation.

---

## Stale Context

Conditions have changed.

---

## Hidden Context

Important assumptions are invisible.

---

# 18. Context and Trust

Trust decisions require context.

Example:

```text id="0mxrgi"
Evidence

+

Source

+

Context

=

Meaningful Confidence
```

---

# 19. Context Invariants

Candidate requirements:

## Invariant 1

Important assertions SHOULD preserve context.

---

## Invariant 2

Context SHOULD be attributable.

---

## Invariant 3

Context SHOULD have lifecycle awareness.

---

## Invariant 4

Context SHOULD remain distinguishable from data.

---

## Invariant 5

Context affecting decisions SHOULD be explainable.

---

# 20. Review Questions

Reviewers should challenge:

1. What context is necessary?
2. What context can be safely discarded?
3. How is context preserved?
4. How is context validated?
5. How does LORE prevent context manipulation?

---

# 21. Closing Principle

> Information answers "what." Context helps answer "what does it mean here, now, and for this purpose?"

---

LORE Volume 98 - Context Model, Meaning, and Situational Awareness v0.2.md

One-liner: **The log file said, "Everything is normal." The operator asked, "Compared to what?" The log file requested a context update.**
