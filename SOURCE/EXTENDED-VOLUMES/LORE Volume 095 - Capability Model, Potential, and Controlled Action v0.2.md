# LORE Volume 95 — Capability Model, Potential, and Controlled Action

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents capabilities.

The purpose is to address a fundamental security challenge:

> The ability to perform an action is not the same as the authority to perform that action.

---

# 2. Core Principle

The governing principle:

> Capability describes what can be done. Authority describes whether it should be done.

---

# 3. Capability Philosophy

Modern systems frequently combine:

- access,
- permission,
- privilege,
- functionality,
- execution ability.

These concepts are often treated as interchangeable.

They should not be.

---

# 4. Capability Definition

A capability represents a potential action available to a principal or system.

Examples:

- read data,
- modify configuration,
- invoke service,
- deploy software,
- control device.

---

# 5. Capability vs Authority

Important distinction:

```text id="m7q4vx"
Capability

=

Ability
```

```text id="q8n5mp"
Authority

=

Justified permission
```

---

# 6. Capability Example

A service account may possess:

```text id="x6m3qw"
Capability:

restart_service()
```

However:

```text id="p9v5kr"
Authority:

Allowed only during approved maintenance window
```

---

# 7. Capability Structure

A capability may include:

```text id="r7n4kp"
Action

+

Target

+

Scope

+

Conditions

+

Lifecycle
```

---

# 8. Capability Scope

Capabilities should define boundaries.

Examples:

- specific object,
- specific environment,
- specific time,
- specific purpose.

---

# 9. Capability Delegation

Capabilities may be delegated.

Delegation should preserve:

- original source,
- scope,
- constraints,
- expiration.

---

# 10. Capability Chains

Delegation may create chains.

Example:

```text id="v8m3qx"
Organization

delegates

Capability

to

Agent

delegates

Limited Capability

to

Task
```

---

# 11. Capability Escalation

A critical risk:

```text id="k4p8mw"
Small Capability

+

Combination

=

Large Authority
```

---

# 12. Capability Composition

Capabilities may combine.

Example:

```text id="wye826"
Read Database

+

Modify Application

=

Potential Deployment Impact
```

---

# 13. Capability Revocation

Capabilities require lifecycle controls.

Questions:

- Can it expire?
- Can it be revoked?
- Who can revoke it?
- What happens afterward?

---

# 14. Capability and Least Privilege

Least privilege requires understanding:

- what is needed,
- why it is needed,
- when it is needed.

---

# 15. Capability and Agents

Autonomous agents make capability management especially important.

An agent may have:

- tools,
- APIs,
- credentials,
- execution environments.

These should be treated as capabilities.

---

# 16. Capability Envelope

A mature system should define:

```text id="0mxrgi"
Agent

has

Capabilities

within

Authority Boundary

under

Context Constraints
```

---

# 17. Capability Security Risks

Potential attacks:

## Capability Theft

Obtaining unauthorized ability.

---

## Capability Leakage

Exposing capability beyond intended scope.

---

## Capability Confusion

Using a capability for the wrong purpose.

---

## Capability Accumulation

Privileges grow without review.

---

# 18. Capability Failure Modes

Potential failures:

## Excessive Capability

Too much potential power.

---

## Orphaned Capability

Capability remains without ownership.

---

## Invisible Capability

Capability exists but is undocumented.

---

## Permanent Temporary Capability

A short-term need becomes permanent access.

---

# 19. Capability Invariants

Candidate requirements:

## Invariant 1

Capabilities SHOULD have explicit scope.

---

## Invariant 2

Capabilities SHOULD have lifecycle.

---

## Invariant 3

Capabilities SHOULD be distinguishable from authority.

---

## Invariant 4

Delegated capabilities SHOULD preserve origin.

---

## Invariant 5

High-impact capabilities SHOULD have containment.

---

# 20. Review Questions

Reviewers should challenge:

1. What constitutes a capability?
2. How are capabilities discovered?
3. How are capabilities bounded?
4. How are capabilities revoked?
5. How are agent capabilities controlled?

---

# 21. Closing Principle

> The dangerous question is not only "what can this system do?" It is "why does it have the ability to do it?"

---

LORE Volume 95 — Capability Model, Potential, and Controlled Action v0.2.md

**Progress checkpoint: Volumes 91–95 completed in this pass (5 volumes). Approximately 8–13 additional core model volumes remain before this generated series reaches its planned endpoint.**

One-liner: **The security engineer asked the application, "Why do you have root?" The application replied, "Because someone once needed me to reboot a printer."**
