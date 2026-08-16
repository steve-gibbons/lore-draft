# LORE Volume 116 - Accountability Model, Responsibility, and Attribution of Consequence

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents accountability.

The purpose is to address a fundamental challenge:

> Systems can identify actions and actors, but they often fail to preserve responsibility for consequences.

---

# 2. Core Principle

The governing principle:

> Accountability connects actions, decisions, authority, and consequences to the principals responsible for them.

---

# 3. Accountability Philosophy

Modern systems frequently separate:

- who performed an action,
- who authorized the action,
- who benefited from the action,
- who was responsible for the outcome.

These separations are sometimes necessary.

They become dangerous when responsibility disappears.

---

# 4. Accountability Definition

Accountability represents the relationship between:

- an action,
- a decision,
- the authority enabling it,
- the principal responsible,
- and the resulting consequence.

---

# 5. Accountability Structure

A complete accountability relationship may include:

```text id="m7q4vx"
Action

+

Actor

+

Authority Source

+

Decision Basis

+

Responsible Principal

+

Outcome

+

Review
```

---

# 6. Accountability vs Attribution

Important distinction:

```text id="q8n5mp"
Attribution

=

Who performed the action
```

```text id="x6m3qw"
Accountability

=

Who remains responsible for the consequence
```

---

# 7. Accountability Example

An automated deployment occurs.

Attribution:

```text id="p9v5kr"
Deployment Agent

performed

release action
```

Accountability:

```text id="r7n4kp"
Engineering Owner

accepted

deployment authority

under

approved process
```

---

# 8. Accountability Chain

Complex systems require preserved chains:

```text id="v8m3qx"
Outcome

↓

Action

↓

Actor

↓

Authority

↓

Delegator

↓

Responsible Owner
```

---

# 9. Accountability and Delegation

Delegation does not eliminate responsibility.

Example:

```text id="k4p8mw"
Manager

delegates

deployment authority

to

automation system
```

The manager may no longer perform the action.

The accountability relationship remains.

---

# 10. Accountability and Autonomous Agents

Autonomous systems introduce difficult questions:

- Who owns the agent?
- Who approved its capabilities?
- Who defined objectives?
- Who accepted operating risk?
- Who reviews unexpected outcomes?

---

# 11. Accountability and Intent

Intent matters.

Two identical actions may have different accountability depending on:

- purpose,
- authorization,
- context,
- expectations.

---

# 12. Accountability and Consequences

A mature system should connect:

```text id="wye826"
Decision

+

Action

+

Impact

=

Accountability Record
```

---

# 13. Accountability and Exceptions

Exceptions require clear ownership.

An exception should identify:

- who requested it,
- who approved it,
- why it exists,
- when it expires,
- who accepts the risk.

---

# 14. Accountability Security Risks

Potential attacks:

## Accountability Laundering

Separating action from responsibility.

---

## Responsibility Diffusion

Many participants exist, but nobody owns the outcome.

---

## False Attribution

Assigning actions to the wrong principal.

---

## Accountability Avoidance

Designing systems where no accountable entity exists.

---

# 15. Accountability Failure Modes

Potential failures:

## Unowned Action

An action occurs without responsible ownership.

---

## Invisible Authority Chain

The source of permission cannot be determined.

---

## Broken Attribution

The actor cannot be identified.

---

## Lost Context

The reason for responsibility assignment disappears.

---

# 16. Accountability Invariants

Candidate requirements:

## Invariant 1

Important actions SHOULD have accountable ownership.

---

## Invariant 2

Accountability SHOULD survive delegation.

---

## Invariant 3

Authority sources SHOULD remain visible.

---

## Invariant 4

Consequences SHOULD map back to decisions.

---

## Invariant 5

Accountability SHOULD remain reviewable.

---

# 17. Review Questions

Reviewers should challenge:

1. Can every meaningful action have accountability?
2. How should autonomous agents be assigned responsibility?
3. When does delegation transfer responsibility?
4. How is shared accountability represented?
5. How does LORE prevent responsibility gaps?

---

# 18. Closing Principle

> A system that records who acted is traceable. A system that records who was responsible is accountable.

---

LORE Volume 116 - Accountability Model, Responsibility, and Attribution of Consequence v0.2.md

One-liner: **The project manager asked, "Who owns this failure?" The room went silent. The ticketing system helpfully created a new ticket titled `Determine Owner Of Ownership Question`.**

(And the TPS report is right where it belongs: filed under "critical artifacts that everyone needs, nobody remembers creating, and somehow always require the correct cover sheet." 😉)
