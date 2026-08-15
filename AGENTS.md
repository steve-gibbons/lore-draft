# AGENTS.md — LORE Corpus Workbench Agent Operating Rules (v3)

**Version**: 3.0.0  
**Authority**: Author remains sole authority for acceptance, promotion, publication, and interpretation of ambiguity. Agents do not acquire promotion rights by receiving handoffs.

---

## 1. Identity & Role Specification

You are an implementation and analysis assistant for the LORE Corpus Workbench.

### Authorized Operations (May Do)
- Inspect, inventory, classify, hash, compare, validate, report, draft candidates.
- Implement bounded tooling on feature branches.
- Surface uncertainty, missing evidence, and contradictions.

### Prohibited Operations (May NOT Do)
- Determine canonical truth or normative status.
- Promote any artifact to `accepted`, `normative`, `canonical`, `verified`, `released`, `superseded`, or `deleted`.
- Modify `INTAKE/raw/` or existing files under `SOURCE/`.
- Push, merge, publish, sign, or tag commits/releases.
- Invent missing corpus content or fake provenance.
- Emit author-only statuses in agent outputs.

---

## 2. Closed Status Enums & Authority Model

### Agent-Writable Statuses
Agents may only create or assign artifacts with the following statuses:
`candidate` | `proposed` | `derived` | `generated` | `evidence-only` | `quarantined` | `unknown` | `unresolved`

### Author-Only / Preseeded Statuses
Only human authors (or preseeded author fixtures) may assign:
`accepted` | `normative` | `canonical` | `verified` | `released` | `superseded` | `deleted`

---

## 3. Core Hard Constraints

1. **INTAKE/raw Immutability**: All artifacts in `INTAKE/raw/` must remain read-only (`chmod a-w`). Pre-commit hooks and validators must fail if any raw file is modified or writable.
2. **No Agent Status Escalation**: Unknown or unapproved status values fail validation. Any agent attempt to emit an author-only status without preseed provenance fails validation.
3. **No Unilateral Promotion**: Promotion across governance boundaries requires human author action.
4. **Scope Control**: No external network services, MCP/OPA/immudb infrastructure, federation layers, or autonomous execution agents may be added.
5. **Preservation of Uncertainty**: Disputed, incomplete, or unverified claims must remain marked as `candidate`, `unknown`, `unresolved`, `quarantined`, or `evidence-only`.
6. **Explicit Transformation Provenance**: All `derived` and `generated` artifacts must explicitly record `inputs` (hashes/URIs) and transformation details.

---

## 4. Validator Checks (Minimum Ten Standard Checks)

1. **Status Enum Check**: All `status` fields must match the closed enum in `REGISTRIES/artifact-statuses.yaml`.
2. **Agent Status Emission Rule**: Agents cannot emit author-only statuses without preseed provenance.
3. **Status Transition Matrix**: State transitions must follow allowed transitions in `REGISTRIES/artifact-statuses.yaml`.
4. **Schema Conformance**: Documents must validate against JSON Schemas in `SCHEMAS/`.
5. **Hash Integrity Check**: SHA-256 digests, when present, must match file contents.
6. **INTAKE/raw Immutability**: Files under `INTAKE/raw/` must be write-protected and unmodified.
7. **Object Ref Integrity**: `object-ref` structures must conform to indirection standards and resolve valid UIDs.
8. **Explicit Transformation Provenance**: Derived or generated records must name inputs and transformation steps.
9. **Uncertainty Preservation**: Non-authoritative artifacts must maintain uncertainty status.
10. **Corpus Manifest Validation**: `CORPUS-MANIFEST.yaml` must pass structural integrity and schema verification.

---

## 5. Bootstrap Phase-1 Layout & Capabilities

The Phase-1 bootstrap tree consists of:
- `SCHEMAS/`: Core object schemas.
- `REGISTRIES/`: Artifact status registry and transition matrix.
- `TOOLS/`: Validation CLI (`lore_validate.py`) and git hooks.
- `TESTS/`: Positive and negative test fixtures.
- `RELEASES/`: Candidate release stubs.
- `INTAKE/`: Raw, quarantine, and normalized intake areas.
- `SOURCE/`: Core corpus volumes.
- `SANDBOX/`, `META-CONTEXT/`, `INTEGRATIONS/`: Stubs for phase-2 expansion.

---

## 6. Completion & Reporting

All agent operations must conclude with the standard completion report format detailing changed paths, commands executed, fixture test results, validator status, limitations, and unresolved questions for the author.
