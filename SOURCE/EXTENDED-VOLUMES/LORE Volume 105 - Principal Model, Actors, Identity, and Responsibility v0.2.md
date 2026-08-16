# LORE Volume 105 - Principal Model, Actors, Identity, and Responsibility

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents principals.

The purpose is to address a fundamental challenge:

> Systems must distinguish between things that exist, things that act, and things that are responsible.

---

# 2. Core Principle

The governing principle:

> An identity answers "who or what is acting." A principal answers "who or what may be held accountable for that action."

---

# 3. Principal Philosophy

Modern systems contain many actors:

- humans,
- applications,
- services,
- devices,
- organizations,
- automated agents,
- external systems.

These actors may all perform actions.

However, their authority and responsibility differ.

---

# 4. Principal Definition

A principal is an entity that can:

- initiate actions,
- receive authority,
- own relationships,
- make assertions,
- be evaluated for trust.

---

# 5. Principal Structure

A principal may include:

```text id="m7q4vx"
Identity

+

Type

+

Authority

+

Relationships

+

Lifecycle

+

Accountability
```

---

# 6. Principal Types

Potential principal categories:

## Human Principal

Examples:

- user,
- administrator,
- operator.

---

## Organizational Principal

Examples:

- company,
- department,
- team.

---

## Service Principal

Examples:

- application,
- daemon,
- API service.

---

## Autonomous Principal

Examples:

- AI agent,
- automated workflow,
- decision system.

---

# 7. Principal vs Identity

Important distinction:

```text id="q8n5mp"
Identity

=

Representation of an entity
```

```text id="x6m3qw"
Principal

=

Entity capable of meaningful action and accountability
```

---

# 8. Principal vs Account

Another important distinction:

```text id="p9v5kr"
Account

=

A mechanism for access
```

```text id="r7n4kp"
Principal

=

The entity represented by that access mechanism
```

---

# 9. Principal Example

A service account:

```text id="v8m3qx"
Account:

backup-service-prod
```

may represent:

```text id="k4p8mw"
Principal:

Enterprise Backup Automation Service
```

---

# 10. Principal Authority

Principals may receive:

- capabilities,
- delegated authority,
- permissions.

Authority should preserve:

- origin,
- scope,
- conditions.

---

# 11. Principal Accountability

Actions should be attributable.

Questions:

- Who acted?
- On whose behalf?
- With what authority?
- Under what conditions?

---

# 12. Principal Relationships

Principals participate in relationships:

Examples:

```text id="wye826"
Human

owns

Application
```

```text id="0mxrgi"
Organization

delegates

Authority

to

Agent
```

---

# 13. Principal Lifecycle

Principals change over time.

Events include:

- creation,
- activation,
- suspension,
- role change,
- retirement.

---

# 14. Principal and Agents

Autonomous agents create new challenges.

An agent may be:

- a tool,
- a service,
- a decision-maker,
- a delegated actor.

LORE must preserve distinctions among:

- creator,
- operator,
- owner,
- agent,
- affected party.

---

# 15. Principal Impersonation

A major security concern:

```text id="drq31j"
Actor claims:

"I am Principal X"
```

The system must evaluate:

- evidence,
- authority,
- context.

---

# 16. Principal Security Risks

Potential attacks:

## Principal Spoofing

Pretending to be another actor.

---

## Principal Confusion

Mixing identities and responsibilities.

---

## Principal Orphaning

Actions exist without accountable ownership.

---

## Principal Overreach

Actor exceeds intended authority.

---

# 17. Principal Failure Modes

Potential failures:

## Unknown Principal

An actor exists without recognition.

---

## Ambiguous Principal

Responsibility is unclear.

---

## Shared Principal

Multiple actors hide individual accountability.

---

## Stale Principal

Authority persists after relevance ends.

---

# 18. Principal Invariants

Candidate requirements:

## Invariant 1

Important actions SHOULD map to principals.

---

## Invariant 2

Principals SHOULD preserve accountability.

---

## Invariant 3

Principals SHOULD remain distinguishable from credentials.

---

## Invariant 4

Principal authority SHOULD have boundaries.

---

## Invariant 5

Principal lifecycle SHOULD be managed.

---

# 19. Review Questions

Reviewers should challenge:

1. What qualifies as a principal?
2. How are principals distinguished from identities?
3. How are autonomous agents represented?
4. How is accountability preserved?
5. Can every meaningful action be attributed?

---

# 20. Closing Principle

> A system that knows who authenticated is useful. A system that knows who acted, why they could act, and who is responsible is trustworthy.

---

LORE Volume 105 - Principal Model, Actors, Identity, and Responsibility v0.2.md

**Progress checkpoint: Volumes 101–105 completed in this pass (5 volumes). Approximately 0–5 additional core model volumes remain before this generated series reaches its planned endpoint.**

One-liner: **The audit log said, "User123 performed the action." The investigator asked, "Excellent. Who is User123?" The room became very interested in the difference between a name tag and a person.**
