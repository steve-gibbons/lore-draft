# LORE Volume 106 — Authorization Model, Permission, and Justified Action

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents authorization.

The purpose is to address a fundamental challenge:

> Systems frequently determine whether an action is technically possible without determining whether the action is justified.

---

# 2. Core Principle

The governing principle:

> Authorization is not merely the presence of permission. Authorization is the justified relationship between a principal, an action, an object, and the applicable context.

---

# 3. Authorization Philosophy

Traditional authorization systems answer questions such as:

- Does this user have access?
- Does this role include permission?
- Is this operation allowed?

These are necessary questions.

However, complex systems require additional questions:

- Why does this permission exist?
- Who granted it?
- Under what conditions?
- For what purpose?
- Does it still apply?

---

# 4. Authorization Definition

Authorization represents the evaluation that determines whether a principal may perform an action against an object under specified conditions.

---

# 5. Authorization Structure

A complete authorization decision may include:

```text id="m7q4vx"
Principal

+

Action

+

Object

+

Capability

+

Policy

+

Context

+

Evidence

↓

Authorization Decision
```

---

# 6. Authorization vs Authentication

Important distinction:

```text id="q8n5mp"
Authentication

=

Who are you?
```

```text id="x6m3qw"
Authorization

=

What may you do?
```

---

# 7. Authorization vs Capability

Another distinction:

```text id="p9v5kr"
Capability

=

Potential ability
```

```text id="r7n4kp"
Authorization

=

Justified use of that ability
```

---

# 8. Authorization Example

A database administrator may have:

```text id="v8m3qx"
Capability:

modify_database()
```

Authorization requires:

```text id="k4p8mw"
Policy:

approved maintenance activity


Context:

production database


Evidence:

change ticket


Authority:

database operations team
```

---

# 9. Authorization Context

Authorization decisions depend on:

- identity,
- environment,
- time,
- purpose,
- risk,
- current conditions.

---

# 10. Authorization Scope

Authorization should define:

- what action,
- what object,
- what boundary,
- what duration.

---

# 11. Authorization Lifecycle

Authorization changes over time.

Events include:

- granting,
- modification,
- suspension,
- expiration,
- revocation.

---

# 12. Authorization and Delegation

Delegated authority must preserve:

- original grantor,
- delegated scope,
- limitations,
- expiration.

---

# 13. Authorization and Agents

Autonomous agents require explicit authorization boundaries.

Questions:

- What actions may the agent perform?
- For whom?
- Under what objective?
- With what evidence?
- When must it stop?

---

# 14. Authorization Explanation

A trustworthy system should explain:

Why was this action allowed?

Example:

```text id="wye826"
Allowed:

Deploy Application


Because:

Agent A

had

Deployment Capability

delegated by

Team B

under

Policy C

during

Approved Window D
```

---

# 15. Authorization Denial

Denials are also meaningful.

A denial should explain:

- what was requested,
- why it was denied,
- what requirement was missing.

---

# 16. Authorization Security Risks

Potential attacks:

## Privilege Escalation

Obtaining greater authority than intended.

---

## Permission Drift

Accumulating obsolete permissions.

---

## Authorization Bypass

Avoiding evaluation.

---

## Authority Laundering

Hiding the source of permission.

---

# 17. Authorization Failure Modes

Potential failures:

## Overbroad Authorization

Too much permitted behavior.

---

## Missing Authorization

No valid decision exists.

---

## Stale Authorization

Permission survives beyond need.

---

## Unexplainable Authorization

Nobody understands why access exists.

---

# 18. Authorization Invariants

Candidate requirements:

## Invariant 1

Authorization SHOULD identify the principal.

---

## Invariant 2

Authorization SHOULD identify the action and target.

---

## Invariant 3

Authorization SHOULD preserve policy context.

---

## Invariant 4

Authorization SHOULD be time-aware.

---

## Invariant 5

Authorization decisions SHOULD be explainable.

---

# 19. Review Questions

Reviewers should challenge:

1. How does LORE differ from existing authorization systems?
2. What information should inform authorization?
3. Where should authorization decisions occur?
4. How are delegated permissions evaluated?
5. How are excessive permissions discovered?

---

# 20. Closing Principle

> Permission answers "can this happen?" Authorization answers "should this happen, given everything we know?"

---

LORE Volume 106 — Authorization Model, Permission, and Justified Action v0.2.md

One-liner: **The access control system said, "Permission granted." The risk engine replied, "Wonderful. Now please explain why we wanted that permission in the first place."**
