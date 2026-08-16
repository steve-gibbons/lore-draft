# Provenance - this is a curated public draft

This repository is a **derived, curated public draft** of the LORE governance scaffold. It was
produced from a private canonical LORE corpus by a single governed transformation, and carries
**clean single-commit history** - the private working history is intentionally not included.

## Verifiable backlink (OBJECT_REF ≠ OBJECT)
This public artifact references its origin without exposing it:

| Field | Value |
|---|---|
| Transformation | `TR-PUBLIC-EXPORT-001` |
| Record SHA-256 (pinned) | `bf271fb67abbc8ff85b0462301723058836421b7340b88cf6f341b91fbb6cb4b` |
| Custody | the private canonical LORE corpus (not publicly resolvable) |
| Public genesis commit | `1571b93` |

The reference is an **alias**, not the record. A party with access to the private corpus can
verify authenticity by hashing the transformation-record and confirming it equals the pinned
SHA-256 above. What the transformation included, excluded, and genericized is recorded there -
this public draft does not, and cannot, reconstruct the private source from this reference.

See [`META-CONTEXT/provenance-backref.object-ref.yaml`](META-CONTEXT/provenance-backref.object-ref.yaml)
for the structured reference.

> EXPERIMENTAL / PROVISIONAL - for evaluation of LORE and demonstration of principles only.
> Not production-ready; not for any other process.
