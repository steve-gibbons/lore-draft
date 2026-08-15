# LORE Volume 66 — Capability Model and Authorization Architecture

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents capability, authority, delegation, and authorization relationships.

The purpose is not to replace authorization systems.

The purpose is to provide a semantic model that makes authority:

- explicit,
- bounded,
- explainable,
- transferable,
- revocable.

---

# 2. Core Principle

The governing principle:

> Authority should be represented as an intentional relationship, not inferred from possession or identity.

---

# 3. Authorization Philosophy

Traditional authorization often answers:

> Is this principal allowed to perform this action?

LORE adds:

> Why does this principal have this authority, under what conditions, and for how long?

---

# 4. Identity Is Not Authority

A foundational distinction:

```text
Identity

≠

Authority
```

Knowing who a principal is does not determine what that principal may do.

---

# 5. Capability Model

A capability represents bounded authority.

A capability should include:

- subject,
- action,
- target,
- constraints,
- purpose,
- validity period,
- issuer,
- evidence.

---

# 6. Capability Structure

Example:

```yaml
CAPABILITY:

  subject:
    Agent_A

  action:
    deploy

  target:
    Application_X

  constraints:
    environment:
      staging

    expiration:
      24_hours

  issued_by:
    Engineering_Manager
```

---

# 7. Capability Boundaries

A useful capability should answer:

- Who may act?
- What may they do?
- Against what?
- Under what conditions?
- Until when?

---

# 8. Least Authority Principle

LORE follows the principle:

> The safest authority is the smallest authority sufficient for the intended purpose.

---

# 9. Capability Scope

Scope may include:

- object,
- hierarchy,
- namespace,
- environment,
- geographic region,
- time,
- purpose.

---

# 10. Hierarchical Scope

Many systems require structured scope.

Example:

```text
Organization

└── Department

    └── Application

        └── Component
```

A capability may apply at different levels.

---

# 11. Pattern-Based Scope

Some environments require matching rules.

Examples:

```text
production.database.read.*

```

or:

```text
device.home.sensor.*
```

---

# 12. Pattern Matching Risks

Flexible matching creates risk.

Potential failures:

- unintended expansion,
- ambiguous interpretation,
- hidden privilege.

---

# 13. Capability Delegation

Capabilities may be delegated.

Delegation should preserve:

- original authority,
- delegation chain,
- limitations,
- expiration.

---

# 14. Delegation Chain

Example:

```text
Organization

|

Administrator

|

Automation Agent

|

Temporary Capability
```

---

# 15. Delegation Principle

Delegation should not create more authority than the delegator possesses.

---

# 16. Capability Attenuation

A delegated capability should be able to become smaller.

Example:

```text
Original:

Deploy Applications


Delegated:

Deploy Application X

```

---

# 17. Capability Revocation

Capabilities require:

- expiration,
- revocation,
- replacement,
- historical tracking.

---

# 18. Tickets and Temporary Authority

LORE may model concepts similar to:

- Kerberos tickets,
- temporary credentials,
- cloud session tokens.

The key distinction:

LORE describes the semantic relationship behind the authority.

---

# 19. Authentication Tickets vs Capabilities

Important distinction:

```text
Credential

proves identity
```

```text
Capability

grants bounded authority
```

---

# 20. Server-Side Authorization

LORE should support server-side authorization decisions.

A service may ask:

- Is this capability valid?
- Is the purpose appropriate?
- Is the relationship current?
- Is the evidence sufficient?

---

# 21. Policy Engine Relationship

A policy engine may consume LORE context.

Example:

```text
Request

|

Policy Engine

|

LORE Context

|

Decision
```

---

# 22. Plugin and Extension Isolation

Capabilities should support isolated extension models.

Examples:

- plugins,
- agents,
- automation modules,
- external tools.

---

# 23. Agent Authorization

Agents require explicit authority.

An agent should not inherit:

- human identity,
- unrestricted permissions,
- implicit trust.

---

# 24. Agent Capability Example

```text
Human Principal

delegates

Research Capability

to

AI Agent

with:

read-only access

specific sources

expiration
```

---

# 25. MCP and Tool Authorization Considerations

Tool-based agent systems introduce new authority boundaries.

Questions:

- Which tools may an agent call?
- For what purpose?
- With what limits?
- Who approved access?

LORE may provide semantic context for these decisions.

---

# 26. Capability Failure Modes

Potential failures:

## Authority Creep

Capabilities expand over time.

---

## Delegation Laundering

Authority becomes unclear through many transfers.

---

## Forgotten Expiration

Temporary authority becomes permanent.

---

## Scope Confusion

A capability applies more broadly than intended.

---

# 27. Capability Security Questions

Reviewers should challenge:

1. Is authority explicit?
2. Can capability scope be inspected?
3. Can delegation be traced?
4. Can misuse be contained?
5. Can authority be recovered?

---

# 28. Authorization Invariants

Candidate requirements:

## Invariant 1

Authority MUST have an identifiable source.

---

## Invariant 2

Delegation MUST preserve lineage.

---

## Invariant 3

Capabilities MUST support expiration or revocation.

---

## Invariant 4

Capabilities SHOULD be as narrow as practical.

---

## Invariant 5

Authority decisions SHOULD be explainable.

---

# 29. Closing Principle

The governing principle:

> The goal of authorization is not merely deciding what is allowed. It is making authority understandable, bounded, and accountable.

---

LORE Volume 66 — Capability Model and Authorization Architecture v0.2.md
