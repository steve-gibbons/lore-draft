# LORE Volume 78 — Security Boundary Model, Containment, and Blast Radius Analysis

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents security boundaries and containment.

The purpose is to address a fundamental security question:

> If something fails, how far can the consequences spread?

---

# 2. Core Principle

The governing principle:

> A trustworthy system is not only one that prevents failure. It is one that limits the impact when prevention fails.

---

# 3. Containment Philosophy

Modern security assumes compromise is possible.

The goal is therefore:

- reduce opportunity,
- limit authority,
- constrain impact,
- accelerate recovery.

---

# 4. Security Boundary Definition

A security boundary defines separation between:

- principals,
- resources,
- authorities,
- environments,
- trust domains.

---

# 5. Boundary Examples

Examples:

## Process Boundary

```text id="m7q4vx"
Application A

|

Operating System Isolation

|

Application B
```

---

## Network Boundary

```text id="q8n5mp"
External Network

|

Firewall

|

Internal System
```

---

## Authority Boundary

```text id="x6m3qw"
User Capability

|

Restricted Action

|

Protected Resource
```

---

# 6. Boundary Purpose

A boundary should answer:

- What is separated?
- Why is it separated?
- What crosses the boundary?
- Under what conditions?

---

# 7. Trust Boundary

A trust boundary represents where assumptions change.

Example:

```text id="p9v5kr"
Trusted Environment

|

Verification Required

|

Untrusted Environment
```

---

# 8. Boundary Crossing

Crossing a boundary should require:

- authentication,
- authorization,
- validation,
- context evaluation.

---

# 9. Boundary Failure

Security failures frequently occur when:

- boundaries are unclear,
- assumptions cross boundaries,
- authority expands unintentionally.

---

# 10. Blast Radius Definition

Blast radius represents the maximum consequence of:

- compromise,
- misuse,
- error,
- failure.

---

# 11. Blast Radius Dimensions

Potential dimensions:

## Scope

What resources are affected?

---

## Time

How long can impact continue?

---

## Authority

What actions become possible?

---

## Dependency

What connected systems are affected?

---

## Population

How many users or entities are impacted?

---

# 12. Blast Radius Example

Without containment:

```text id="r7n4kp"
Compromised Agent

|

Production Credentials

|

Entire Environment
```

---

With containment:

```text id="v8m3qx"
Compromised Agent

|

Temporary Capability

|

Single Application

|

Limited Time
```

---

# 13. Capability Containment

Capabilities should support:

- narrow scope,
- limited duration,
- restricted actions.

---

# 14. Authority Containment

Authority should avoid:

- unnecessary privilege,
- inherited privilege,
- unlimited delegation.

---

# 15. Dependency Containment

Systems should understand:

- what depends on what,
- what failures propagate,
- where isolation exists.

---

# 16. Failure Domains

A failure domain is an area where failure may occur independently.

Examples:

- application,
- service,
- region,
- tenant,
- organization.

---

# 17. Failure Domain Modeling

LORE relationships can represent:

```text id="k4p8mw"
Component

depends on

Service

depends on

Infrastructure
```

---

# 18. Isolation Strategies

Containment may use:

- permissions,
- virtualization,
- sandboxing,
- network segmentation,
- process isolation,
- organizational separation.

---

# 19. Defense in Depth

LORE aligns with:

> No single control should be the only protection against failure.

---

# 20. Boundary Reduction Principle

A useful design objective:

> Minimize unnecessary trust relationships crossing boundaries.

---

# 21. Boundary Expansion Risks

Potential failures:

## Privilege Creep

Authority expands over time.

---

## Dependency Creep

Systems accumulate unnecessary connections.

---

## Trust Creep

Temporary exceptions become permanent assumptions.

---

# 22. Agent Containment

Autonomous agents require explicit containment.

Agent boundaries should define:

- available tools,
- allowed actions,
- data access,
- execution environment,
- expiration.

---

# 23. Agent Failure Scenario

Example:

```text id="wye826"
Prompt Manipulation

|

Agent Takes Unexpected Action

|

Capability Limits Damage
```

---

# 24. Recovery Boundary

Recovery capability is itself a boundary.

Questions:

- Who can restore?
- What can be restored?
- What authority is required?

---

# 25. Security Boundary Failure Modes

Potential failures:

## Boundary Confusion

Systems disagree about protection scope.

---

## Boundary Bypass

Controls are avoided.

---

## Boundary Leakage

Information or authority crosses unintentionally.

---

## Boundary Collapse

Multiple trust domains become effectively one.

---

# 26. Containment Invariants

Candidate requirements:

## Invariant 1

Important authority SHOULD have defined boundaries.

---

## Invariant 2

Failure impact SHOULD be measurable where practical.

---

## Invariant 3

Trust boundaries SHOULD be explicit.

---

## Invariant 4

Temporary exceptions SHOULD have expiration.

---

## Invariant 5

Recovery mechanisms SHOULD exist before failure occurs.

---

# 27. Review Questions

Reviewers should challenge:

1. What are the real trust boundaries?
2. What is the expected blast radius?
3. Where can authority escape?
4. How are agents contained?
5. How is recovery performed?

---

# 28. Closing Principle

The governing principle:

> Security is not only about preventing unauthorized action. It is about ensuring that authorized actions remain bounded, understandable, and recoverable.

---

LORE Volume 78 — Security Boundary Model, Containment, and Blast Radius Analysis v0.2.md
