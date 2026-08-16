# LORE Volume 9 - Evidence, Provenance, and Trust Evaluation Model

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents:

- evidence,
- provenance,
- assertions,
- trust evaluation,
- and confidence.

The goal is to prevent a recurring failure pattern:

> Information becomes trusted because it exists, rather than because its origin, support, and applicability are understood.

---

# 2. Core Principle

The foundational distinction:

```text id="h7m2qd"
Assertion

≠

Evidence

≠

Truth
```

LORE does not attempt to create a universal truth database.

LORE records:

- what was asserted,
- by whom,
- when,
- under what conditions,
- supported by what evidence.

---

# 3. Assertion Model

An assertion is a statement made by some source.

Example:

```text id="m8q4vx"
"This server is owned by Organization A."
```

An assertion should include:

Potential attributes:

- issuer,
- subject,
- claim,
- timestamp,
- scope,
- lifecycle,
- supporting evidence.

---

# 4. Assertion Lifecycle

Assertions change over time.

Potential lifecycle:

```text id="p5w8zn"
Created

    |

Active

    |

Superseded

    |

Expired

    |

Withdrawn
```

---

# 5. Evidence Model

Evidence supports evaluation of an assertion.

Potential evidence types:

- measurement,
- observation,
- document,
- attestation,
- signature,
- external reference,
- operational record.

---

# 6. Evidence Is Contextual

Evidence does not have meaning independently.

Example:

A certificate may be valid evidence:

- for a specific domain,
- during a specific period,
- issued by a specific authority.

The same certificate may not be sufficient evidence elsewhere.

---

# 7. Provenance Model

Provenance describes origin and history.

Potential provenance attributes:

- creator,
- issuer,
- source system,
- transformation history,
- retrieval path,
- timestamps.

---

# 8. Provenance Chain Example

Example:

```text id="x8c4lm"
Measurement

    |

Generated Report

    |

Security Assertion

    |

Risk Decision
```

Each transition should preserve:

- source,
- transformation,
- responsibility.

---

# 9. Trust Evaluation

Trust is not a permanent property.

Trust depends on:

- source,
- evidence,
- context,
- time,
- purpose.

---

# 10. Trust Evaluation Model

Conceptually:

```text id="k7m3qs"
Trust Decision

=

Identity

+

Authority

+

Evidence

+

Context

+

Lifecycle
```

---

# 11. Trust Is Not Binary

LORE should avoid:

```text id="v5n8kp"
Trusted

or

Untrusted
```

as the only model.

Real systems require:

- confidence,
- scope,
- applicability,
- uncertainty.

---

# 12. Conflicting Assertions

Multiple sources may disagree.

Example:

```text id="q9m6rt"
Source A:

Device belongs to Team X


Source B:

Device belongs to Team Y
```

LORE should represent the conflict.

It should not silently select a winner.

---

# 13. Conflict Resolution

Resolution may depend on:

- authority,
- evidence quality,
- recency,
- context,
- domain rules.

---

# 14. Evidence Freshness

Evidence may become stale.

Examples:

- expired certificates,
- old inventories,
- outdated ownership records.

Therefore:

Evidence requires lifecycle.

---

# 15. Evidence Quality

Potential evaluation factors:

## Authority

Who produced it?

---

## Integrity

Can it be trusted as unchanged?

---

## Freshness

Is it current?

---

## Applicability

Does it apply to this situation?

---

## Completeness

Does it support the decision being made?

---

# 16. Provenance and Security

Provenance itself becomes an attack surface.

Potential attacks:

- forged history,
- missing history,
- misleading transformation chains,
- selective evidence disclosure.

---

# 17. Signed Objects

Potential mitigation:

Represent important objects as signed objects.

Example:

```text id="b4x7pm"
Object

+

Assertion

+

Evidence References

+

Signature

+

Lifecycle
```

---

# 18. Signed Objects Are Not Sufficient

A valid signature proves:

> This key signed this object.

It does not automatically prove:

- the claim is true,
- the issuer is appropriate,
- the context applies.

---

# 19. Agent Application

Evidence and provenance are especially important for agents.

An agent should be able to evaluate:

- Why does this information exist?
- Who provided it?
- How reliable is it?
- Is it current?
- Does it apply here?

---

# 20. Example Agent Decision

Without semantic evidence:

```text id="n8q5wc"
User Preference Record Exists

Therefore:

Use It
```

---

With LORE:

```text id="r6m3xz"
Preference Assertion

from

User

created

2 years ago

confidence:

high

valid for:

personal assistant recommendations

```

---

# 21. Review Questions

Reviewers should challenge:

1. Is evidence sufficiently separated from assertions?
2. How much provenance is necessary?
3. Can provenance become too expensive?
4. How are conflicting assertions represented?
5. Should trust evaluation be standardized?
6. Which objects require signatures?
7. How is stale evidence handled?

---

# 22. Evidence Principle

The governing principle:

> Information should carry enough history that a decision-maker can understand why it was considered trustworthy.

---

LORE Volume 9 - Evidence, Provenance, and Trust Evaluation Model v0.2.md
