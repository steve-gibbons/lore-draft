# LORE Volume 75 — Capability, Permission, and Action Decision Model

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents the relationship between:

- principals,
- capabilities,
- permissions,
- actions,
- resources,
- and decisions.

The purpose is to prevent a common security failure:

> Confusing the ability to perform an action with the permission to perform an action in a specific context.

---

# 2. Core Principle

The governing principle:

> Capability describes what may be possible. Authorization determines whether it is appropriate now.

---

# 3. Capability Philosophy

Modern systems frequently combine:

- credentials,
- permissions,
- tokens,
- roles,
- policies,
- actions.

This creates ambiguity.

LORE separates:

```text id="m7q4vx"
Capability

=

Potential Ability
```

from:

```text id="q8n5mp"
Decision

=

Authorized Action
```

---

# 4. Capability Definition

A capability represents a bounded expression of possible authority.

A capability describes:

- actor,
- action class,
- target scope,
- constraints,
- origin,
- lifecycle.

---

# 5. Permission Definition

A permission represents an allowed operation within a policy framework.

Examples:

- read,
- write,
- execute,
- administer,
- deploy.

---

# 6. Action Definition

An action is an attempted operation.

Examples:

- read file,
- restart service,
- modify configuration,
- deploy application.

---

# 7. Resource Definition

A resource is the target affected by an action.

Examples:

- database,
- application,
- device,
- document,
- service.

---

# 8. Decision Model

A LORE-informed decision may evaluate:

```text id="x6m3qw"
Principal

+

Capability

+

Requested Action

+

Resource

+

Context

+

Evidence

=

Decision
```

---

# 9. Capability vs Permission

Important distinction:

```text id="p9v5kr"
Capability

describes authority possession
```

```text id="r7n4kp"
Permission

describes policy outcome
```

---

# 10. Capability vs Credential

Another important distinction:

```text id="v8m3qx"
Credential

proves or authenticates identity
```

```text id="k4p8mw"
Capability

represents bounded authority
```

---

# 11. Capability Validation

A capability evaluation may consider:

- issuer,
- holder,
- scope,
- expiration,
- revocation,
- context,
- evidence.

---

# 12. Action Context

The same capability may produce different outcomes depending on context.

Example:

```text id="wye826"
Capability:

restart service


Context:

scheduled maintenance

=

Allowed
```

```text id="fzbvqj"
Capability:

restart service


Context:

active customer outage

=

Requires additional review
```

---

# 13. Resource Context

Resources may influence decisions.

Examples:

- production vs development,
- critical vs non-critical,
- regulated vs unrestricted.

---

# 14. Policy Relationship

LORE does not replace policy engines.

Instead:

```text id="u4n8kc"
Policy Engine

asks:

Should this action occur?

|

LORE provides:

Meaning and context
```

---

# 15. Capability Discovery

Systems may need to answer:

- What capabilities exist?
- Who holds them?
- What scope do they cover?
- When do they expire?

---

# 16. Capability Delegation

Delegated capabilities should preserve:

- origin,
- constraints,
- lineage,
- purpose.

---

# 17. Capability Composition

Complex actions may require multiple capabilities.

Example:

```text id="9ax18t"
Deploy Application

requires:

Deployment Capability

+

Change Approval Capability

+

Environment Access Capability
```

---

# 18. Capability Conflict

Conflicting capabilities may exist.

Example:

```text id="h5m8qx"
Capability A:

Allow deployment


Capability B:

Deny deployment during freeze
```

---

# 19. Conflict Resolution

Resolution should consider:

- authority source,
- policy precedence,
- context,
- organizational rules.

---

# 20. Capability Revocation

Revocation should support:

- immediate invalidation,
- replacement,
- audit history.

---

# 21. Capability Lifetime

Capabilities should include:

- creation,
- activation,
- expiration,
- renewal,
- retirement.

---

# 22. Capability Security Risks

Potential attacks:

## Capability Theft

An attacker obtains valid authority.

---

## Capability Escalation

A capability becomes broader than intended.

---

## Capability Replay

An expired or invalid capability is reused.

---

## Capability Confusion

A capability is applied outside intended scope.

---

# 23. Action Decision Failure Modes

Potential failures:

## Missing Context

Decision lacks required information.

---

## Excessive Trust

Capability is accepted without validation.

---

## Hidden Policy

Decision cannot be explained.

---

## Ambiguous Scope

Action boundaries are unclear.

---

# 24. Decision Explainability

A decision should explain:

- requested action,
- evaluated capability,
- relevant policy,
- supporting evidence,
- final rationale.

---

# 25. Decision Invariants

Candidate requirements:

## Invariant 1

Actions SHOULD be evaluated against explicit authority.

---

## Invariant 2

Capabilities SHOULD have bounded scope.

---

## Invariant 3

Capabilities SHOULD have lifecycle controls.

---

## Invariant 4

Decision context SHOULD be preserved.

---

## Invariant 5

Authorization outcomes SHOULD be explainable.

---

# 26. Review Questions

Reviewers should challenge:

1. Is capability distinct from permission?
2. Is authority sufficiently bounded?
3. Can decisions be explained?
4. How are conflicts handled?
5. How are compromised capabilities recovered?

---

# 27. Closing Principle

The governing principle:

> Secure systems do not merely ask whether someone can act. They determine whether that action is justified, bounded, and appropriate.

---

LORE Volume 75 — Capability, Permission, and Action Decision Model v0.2.md
