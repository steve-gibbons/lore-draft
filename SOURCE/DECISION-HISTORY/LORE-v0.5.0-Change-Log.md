# LORE v0.5.0 Change Log & Remediation Record

## Status
ACCEPTED & EXECUTED

## Verbatim Approval Authority
> "document your proposal as a change log entry, with supporting reasoning and this approval (verbatim) and then proceed"

---

# 1. Summary of Changes

This change log entry documents the remediation of package assembly structure, version lifecycle freeze (`v0.5.0`), inclusion of package-root `INCIDENT_LOG.md`, and dual-volume architecture (`SOURCE-VOLUMES/` for normative core volumes 0–4 and `EXTENDED-VOLUMES/` for extended draft modules 5–120).

---

# 2. Identified Gaps & Supporting Reasoning

### Gap 1: Version Lifecycle Freeze (`v0.5.0`)
- **Finding**: Incremental re-enrichment edits led to version creep (`v0.5.1`). The explicit target specification was release `v0.5.0`.
- **LORE Reasoning (`LIFECYCLE` Mechanics)**: Version designations must remain strictly frozen at the target release level (`v0.5.0`).
- **Remediation**: 
  - Updated `README.md` title to `# LORE v0.5.0 Package`.
  - Renamed release metadata directory to `LORE_v0.5.0_Release_Metadata_Bundle/` and updated zip archive to `LORE_v0.5.0_Release_Metadata_Bundle.zip`.
  - Reverted `CORPUS-MANIFEST.yaml` and `release-manifest.json` version strings to `v0.5.0`.

### Gap 2: Package-Root Incident Log Placement
- **Finding**: `INCIDENT_LOG.md` was created at repo root, but omitted from inside `LORE-v0.5-package/INCIDENT_LOG.md`.
- **LORE Reasoning (`EVIDENCE` Mechanics)**: Package distributions must be self-contained and independently verifiable without requiring external repository files.
- **Remediation**:
  - Placed `INCIDENT_LOG.md` directly inside `LORE-v0.5-package/INCIDENT_LOG.md` and registered it in `CORPUS-MANIFEST.yaml`.

### Gap 3: Dual-Volume Architecture (Normative 0–4 vs. Extended 5–120)
- **Finding**: Draft 2 contained 121 extended draft modules (Volumes 5 through 120) that were omitted from initial package extractions.
- **LORE Reasoning (`PROVENANCE` & `OBJECT_REF` Mechanics)**: Normative core volumes (0–4) must not be conflated with extended draft modules (5–120).
- **Remediation**:
  - Maintained `SOURCE-VOLUMES/` for normative core volumes 0, 1, 2, 3, and 4 (with anchor IDs).
  - Populated `EXTENDED-VOLUMES/` with all 121 draft volume modules (Volumes 5 through 120 from `Draft 2/`).
  - Categorized both sections in `CORPUS-MANIFEST.yaml`.

---

# 3. Verification Evidence

- **Reference Integrity**: 100% resolution of all normative and extended volume paths.
- **Cryptographic Evidence**: SHA-256 checksums updated and verified in `package-checksums.sha256`.
