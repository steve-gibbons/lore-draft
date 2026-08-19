#!/usr/bin/env python3
"""
LORE Corpus Workbench Validator (TOOLS/lore_validate.py)
Implements 10 minimum governance, structural, and schema checks per AGENTS v3 specification.
Standard Python 3 implementation with zero external dependencies.

YAML parsing: delegates to lore_common.load_simple_yaml (single shared fallback parser).
lore_build_manifest imports load_doc from here as the single source of truth (KF-03).
"""

import sys
import os
import re
import json
import hashlib
import stat
import argparse

sys.path.insert(0, os.path.dirname(__file__))
from lore_common import load_simple_yaml as _load_simple_yaml


def load_doc(filepath):
    """Load JSON or YAML file. Single parser source of truth (KF-03, shared with lore_common)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if filepath.endswith('.json'):
        return json.loads(content)
    # Try JSON first (some .yaml files are actually JSON), then YAML fallback.
    try:
        return json.loads(content)
    except Exception:
        return _load_simple_yaml(content)

def get_registry(repo_root):
    reg_path = os.path.join(repo_root, 'REGISTRIES', 'artifact-statuses.yaml')
    if not os.path.exists(reg_path):
        return None, None, {}
    reg_doc = load_doc(reg_path)
    enums = reg_doc.get('enum', {})
    agent_writable = set(enums.get('agent_writable', []))
    author_only = set(enums.get('author_only', []))
    transitions = reg_doc.get('transitions', {})
    return agent_writable, author_only, transitions

def load_trusted_signers(repo_root):
    """Return {fpr_upper: role} from REGISTRIES/trusted-signers.txt.

    Dependency-free: the core validator reads this registry to confirm that a
    signature *reference* on an author-only artifact names a REGISTERED signer
    (Check 2, KF-01). It does NOT do cryptography - the actual gpg verification
    (GOODSIG/VALIDSIG, lineage to a root, role policy) is the separate CI gate
    TOOLS/lore_verify_author_sig.py. This split keeps the core 10 checks
    zero-dependency while still moving author-only status from a self-asserted
    boolean to a signature bound to a known key. (CORE-INVARIANT 10: represent,
    then enforce.)
    """
    signers = {}
    path = os.path.join(repo_root, 'REGISTRIES', 'trusted-signers.txt')
    if not os.path.isfile(path):
        return signers
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(None, 2)
            if len(parts) < 2:
                continue
            fpr = parts[0].upper().replace(' ', '')
            signers[fpr] = parts[1]
    return signers

class LoreValidator:
    def __init__(self, repo_root):
        self.repo_root = repo_root
        self.agent_writable, self.author_only, self.transitions = get_registry(repo_root)
        self.all_statuses = (self.agent_writable or set()).union(self.author_only or set())
        self.trusted_signers = load_trusted_signers(repo_root)
        # Per-run cache for Check 7 local object resolution.
        # None = not yet scanned. dict = {id: True} for every id found in workbench.
        self._obj_id_cache = None  # type: ignore[assignment]

    def _build_obj_id_cache(self):
        """Walk ~/.lore/objects once per validator run and index all object ids."""
        cache = {}
        lore_home = os.environ.get('LORE_HOME', os.path.expanduser('~/.lore'))
        objects_base = os.path.join(lore_home, 'objects')
        if not os.path.isdir(objects_base):
            return None  # No local workbench present
        for dirpath, _dirs, files in os.walk(objects_base):
            for fname in files:
                if not fname.endswith(('.yaml', '.json')):
                    continue
                fpath = os.path.join(dirpath, fname)
                try:
                    with open(fpath, encoding='utf-8') as _fh:
                        txt = _fh.read()
                    d = json.loads(txt) if fpath.endswith('.json') else _load_simple_yaml(txt)
                    oid = (d or {}).get('lore', {}).get('id')
                    if oid:
                        cache[oid] = True
                except Exception:
                    pass
        return cache

    def _resolve_id_locally(self, target_id: str):
        """Return True if target_id found locally, False if not, None if no workbench.
        Builds the cache on first call; subsequent calls are O(1) dict lookups."""
        if self._obj_id_cache is None:
            self._obj_id_cache = self._build_obj_id_cache()
        if self._obj_id_cache is None:
            return None  # No local workbench — nothing to check
        return self._obj_id_cache.get(target_id, False)

    def validate_file(self, filepath):
        doc = load_doc(filepath)
        errors = []
        warnings = []

        # Check 1: Status Enum Check
        status = doc.get('status')
        if status:
            if status not in self.all_statuses:
                errors.append(f"Check 1 Fail: Status '{status}' is not in closed status enum.")

        # Check 2: Author-only Emission Rule (KF-01 - authenticated, not self-asserted).
        # Authority to hold an author-only status must be BOUND to a registered signer,
        # not minted by a self-written boolean. The core check (dependency-free) verifies
        # the REPRESENTATION: a signature reference naming a signer in the trusted-signers
        # registry, whose detached .asc exists on disk. The CRYPTO enforcement (that the
        # signature actually verifies, chains to a root, and carries an allowed role) is
        # the separate CI gate TOOLS/lore_verify_author_sig.py. During migration, a bare
        # `author_preseeded: true` is still accepted but DEPRECATED (warning) - it must be
        # replaced by a signature before v1.0.0 (DECISION-AUTH-IDENTITY.accepted.md).
        if status in self.author_only:
            provenance = doc.get('provenance', {})
            if not isinstance(provenance, dict):
                provenance = {}
            sig_ref = provenance.get('signature')
            signer_fpr = provenance.get('signer_fpr')
            author_preseeded = provenance.get('author_preseeded', False)

            if sig_ref or signer_fpr:
                # Authenticated path: both the reference and the signer id are required.
                if not (sig_ref and signer_fpr):
                    errors.append(f"Check 2 Fail: Author-only status '{status}' has an "
                                  "incomplete signature reference (need both "
                                  "provenance.signature and provenance.signer_fpr).")
                else:
                    fpr = str(signer_fpr).upper().replace(' ', '')
                    asc_path = os.path.join(self.repo_root, sig_ref)
                    if fpr not in self.trusted_signers:
                        errors.append(f"Check 2 Fail: Author-only status '{status}' signed by "
                                      f"'{fpr}', which is not in REGISTRIES/trusted-signers.txt "
                                      "(unregistered signer - possible forgery).")
                    elif not os.path.isfile(asc_path):
                        errors.append(f"Check 2 Fail: Author-only status '{status}' references "
                                      f"signature '{sig_ref}', but that detached .asc is missing.")
                    # else: representation valid; crypto validity is the CI gate's job.
            elif author_preseeded is True:
                warnings.append(f"Check 2 (migration): Author-only status '{status}' relies on "
                                "the deprecated `author_preseeded` boolean with no signature. "
                                "Sign it (provenance.signature + signer_fpr) before v1.0.0 - "
                                "see DECISION-AUTH-IDENTITY.accepted.md.")
            else:
                errors.append(f"Check 2 Fail: Author-only status '{status}' emitted without "
                              "author authority (no signature reference, no preseed provenance).")

        # Check 3: Status Transition Check
        prev_status = doc.get('previous_status')
        if prev_status and status:
            allowed = self.transitions.get(prev_status, {}).get('allowed_next', [])
            if status not in allowed:
                errors.append(f"Check 3 Fail: Illegal status transition from '{prev_status}' to '{status}'. Allowed: {allowed}")

        # Check 4: Schema Conformance Check
        doc_type = doc.get('type')
        subkind = doc.get('subkind')
        if doc_type == 'transformation-record':
            if 'inputs' not in doc: errors.append("Check 4 Fail: transformation-record missing required field 'inputs'.")
            if 'transformation' not in doc: errors.append("Check 4 Fail: transformation-record missing required field 'transformation'.")
        elif doc_type == 'proposal-record':
            if 'proposer' not in doc: errors.append("Check 4 Fail: proposal-record missing required field 'proposer'.")
            if 'summary' not in doc: errors.append("Check 4 Fail: proposal-record missing required field 'summary'.")
        elif doc_type == 'decision-record':
            if 'decision_maker' not in doc: errors.append("Check 4 Fail: decision-record missing required field 'decision_maker'.")
            if 'rationale' not in doc: errors.append("Check 4 Fail: decision-record missing required field 'rationale'.")
        elif doc_type == 'anti-pattern':
            if 'problem' not in doc: errors.append("Check 4 Fail: anti-pattern missing required field 'problem'.")
            if 'remedy' not in doc: errors.append("Check 4 Fail: anti-pattern missing required field 'remedy'.")
        elif doc_type == 'break-glass-record':
            if 'actor' not in doc: errors.append("Check 4 Fail: break-glass-record missing required field 'actor'.")
            if 'reason' not in doc: errors.append("Check 4 Fail: break-glass-record missing required field 'reason'.")
            if 'scope' not in doc: errors.append("Check 4 Fail: break-glass-record missing required field 'scope'.")
        # --- Canonical ontology (DECISION-ONTOLOGY-CANONICAL-KERNEL-001): abstract `object` base;
        #     concrete flavors keyed by `type`(=kind) + optional `subkind`. ---
        elif doc_type == 'object':
            # Layer-0 ABSTRACT base: describes anything; never stored bare.
            errors.append("Check 4 Fail: 'object' is the ABSTRACT base kind and must not be stored "
                          "directly - use a concrete flavor (principal, policy, object-ref, "
                          "relationship, act, assertion, authority, capability).")
        elif doc_type == 'principal':
            # Identity-bearing noun: identity is the basis for authz/capability (via policy).
            if 'identity' not in doc:
                errors.append("Check 4 Fail: principal missing required field 'identity'.")
            if doc.get('principal_kind') not in ('human', 'thing', 'organization', 'service'):
                errors.append("Check 4 Fail: principal missing/invalid 'principal_kind' "
                              "(human|thing|organization|service) - accountability depends on it "
                              "(invariant 13: only a human principal can be Accountable).")
        elif doc_type == 'policy':
            # Rule-noun: governs authorization/capability decisions.
            for rf in ('statement', 'applies_to'):
                if rf not in doc:
                    errors.append(f"Check 4 Fail: policy missing required field '{rf}'.")
        elif doc_type == 'object-ref':
            # Pointer; OBJECT_REF != OBJECT. subkind 'alias' = a named ref; ALIAS != IDENTITY.
            if 'target_id' not in doc:
                errors.append("Check 4 Fail: object-ref missing required field 'target_id'.")
            if subkind == 'alias':
                for rf in ('alias', 'alias_type', 'resolves_to', 'owner', 'resolution_history'):
                    if rf not in doc:
                        errors.append(f"Check 4 Fail: object-ref/alias missing required field '{rf}' "
                                      "(ALIAS != IDENTITY: preserve type/resolution/ownership/history, Vol 2 §19).")
        elif doc_type == 'relationship':
            # Explicit, typed edge (Vol 1 §19): subject -predicate-> object.
            for rf in ('subject', 'predicate', 'object'):
                if rf not in doc:
                    errors.append(f"Check 4 Fail: relationship missing required field '{rf}' "
                                  "(relationships must be explicit and typed, Vol 1 §19).")
        elif doc_type == 'act':
            # Verb. subkind 'event' = an act with a trigger (temporal).
            for rf in ('actor', 'action'):
                if rf not in doc:
                    errors.append(f"Check 4 Fail: act missing required field '{rf}'.")
            if subkind == 'event' and 'trigger' not in doc:
                errors.append("Check 4 Fail: act/event missing required 'trigger' "
                              "(an event is an act with a trigger).")
            # Accountability (invariant 13): a risky/permanent act must name who is accountable.
            if doc.get('effect') in ('destructive', 'external') and 'accountable' not in doc:
                errors.append(f"Check 4 Fail: act with effect '{doc.get('effect')}' must name an "
                              "'accountable' principal (invariant 13: a thing cannot be accountable).")
        elif doc_type == 'assertion':
            # A claim; ASSERTION != TRUTH -> agent-writable status only. Subkinds below.
            if 'claim' not in doc:
                errors.append("Check 4 Fail: assertion missing required field 'claim'.")
            if status and self.agent_writable and status not in self.agent_writable:
                errors.append(f"Check 4 Fail: ASSERTION != TRUTH - an assertion (and its subkinds) "
                              f"must hold an agent-writable status, not '{status}' (Vol 1 §9).")
            if subkind == 'evidence':
                for rf in ('source', 'method', 'collected'):
                    if rf not in doc:
                        errors.append(f"Check 4 Fail: assertion/evidence missing contextual field "
                                      f"'{rf}' (evidence is contextual, Vol 1 §11).")
            elif subkind == 'evaluation':
                for rf in ('criteria', 'verdict'):
                    if rf not in doc:
                        errors.append(f"Check 4 Fail: assertion/evaluation missing required field '{rf}'.")
            elif subkind == 'context-hint':
                if 'purpose' not in doc:
                    errors.append("Check 4 Fail: assertion/context-hint missing required 'purpose' "
                                  "(untrusted handoff; CONTEXT_HINT != TRUSTED_CONTEXT, Vol 1 §17-18).")
        elif doc_type == 'authority':
            # Right to grant/decide; MUST have lineage (invariant 11) - enforced separately.
            for rf in ('issuer', 'subject', 'scope', 'derives_from'):
                if rf not in doc:
                    errors.append(f"Check 4 Fail: authority missing required field '{rf}' "
                                  "(authority has lineage - possession without lineage is not authority, invariant 11).")
        elif doc_type == 'capability':
            # Bounded permission; MUST have explicit scope (Vol 2 §28) - enforced separately.
            for rf in ('issuer', 'holder', 'action', 'scope'):
                if rf not in doc:
                    errors.append(f"Check 4 Fail: capability missing required field '{rf}' "
                                  "(capabilities MUST have explicit scope, Vol 2 §28 Inv 1).")
            if 'expiration' not in doc:
                warnings.append("Check 4 (recommended): capability has no 'expiration' - "
                                "capabilities SHOULD be time-bounded (Vol 2 §6/§13).")

        # Check 5: Hash & Provenance Check
        sha256 = doc.get('sha256')
        rel_path = doc.get('path')
        if sha256 and rel_path:
            target_file = os.path.join(self.repo_root, rel_path)
            if os.path.exists(target_file):
                with open(target_file, 'rb') as tf:
                    actual_hash = hashlib.sha256(tf.read()).hexdigest()
                if actual_hash.lower() != sha256.lower():
                    errors.append(f"Check 5 Fail: SHA256 mismatch for '{rel_path}'. Expected {sha256}, got {actual_hash}.")

        # Check 7: Object Ref Integrity Check
        # Validates target_id format and, when the local workbench objects dir is present,
        # warns (ADVISORY — non-blocking) if the referenced object is not found locally.
        # The warning is clearly labelled [advisory] to prevent operators from treating an
        # unresolved reference as a validated dependency relationship.
        if doc_type == 'object-ref':
            target_id = doc.get('target_id')
            if not target_id or not isinstance(target_id, str):
                errors.append("Check 7 Fail: Invalid or missing target_id in object-ref.")
            else:
                # Best-effort local resolution using a per-run cache (built lazily).
                # Uses the per-instance cache self._obj_id_cache so each validator
                # instantiation pays the scan cost at most once, not once per object-ref.
                found_locally = self._resolve_id_locally(target_id)
                if found_locally is False:  # None means "no local workbench to check"
                    warnings.append(
                        f"[advisory] Check 7: object-ref target_id '{target_id}' not found "
                        "in local workbench objects — may be a remote or future reference. "
                        "This warning is non-blocking; it does not validate the reference exists."
                    )

        # Check 8: Explicit Transformation Provenance
        if doc_type == 'transformation-record' or status in ('derived', 'generated'):
            inputs = doc.get('inputs')
            if not inputs or not isinstance(inputs, list) or len(inputs) == 0:
                errors.append("Check 8 Fail: Derived/generated artifact missing required 'inputs' list.")

        # Check 9: Uncertainty Preservation Check
        if doc_type == 'proposal-record' and status not in self.agent_writable:
            errors.append(f"Check 9 Fail: Unverified proposal must retain uncertainty status, got '{status}'.")

        return len(errors) == 0, errors, warnings

    def check_intake_raw_immutability(self):
        """Check 6: INTAKE/raw content integrity via a git-preservable SHA-256 manifest.

        Replaces filesystem-permission checks (chmod a-w), which git does not preserve -
        so they could not survive a fresh checkout or pass in CI (see KF-06). The manifest
        `INTAKE/RAW-MANIFEST.sha256` records the hash of every raw evidence file; this check
        detects mutation, unrecorded arrivals, and deleted evidence. It travels with the repo
        and is tamper-detectable in git history. Regenerate with TOOLS/lore_freeze_raw.py.
        (chmod a-w is still applied locally as advisory defense-in-depth, but is not required.)
        """
        intake_raw = os.path.join(self.repo_root, 'INTAKE', 'raw')
        manifest_path = os.path.join(self.repo_root, 'INTAKE', 'RAW-MANIFEST.sha256')
        skip_names = {'README.md', '.DS_Store'}
        skip_suffixes = {'.gdoc'}  # live Drive sync pointers — content races sync process
        errors = []
        if not os.path.exists(intake_raw):
            # No raw directory at all. If a manifest exists its entries would all be
            # "missing on disk" — that is a real problem, not a vacuous pass.
            if os.path.exists(manifest_path):
                return False, [
                    "Check 6 Fail: INTAKE/RAW-MANIFEST.sha256 exists but INTAKE/raw "
                    "directory is absent — manifest entries cannot be verified."
                ]
            return True, []

        # Actual raw files on disk -> sha256 (paths relative to INTAKE/raw)
        actual = {}
        excluded = []
        for root, dirs, files in os.walk(intake_raw):
            for f in files:
                if f in skip_names:
                    continue
                if any(f.endswith(s) for s in skip_suffixes):
                    rel = os.path.relpath(os.path.join(root, f), intake_raw)
                    excluded.append(rel)
                    continue
                full_p = os.path.join(root, f)
                rel = os.path.relpath(full_p, intake_raw)
                with open(full_p, 'rb') as fh:
                    actual[rel] = hashlib.sha256(fh.read()).hexdigest()

        # Expected from the manifest
        expected = {}
        if os.path.exists(manifest_path):
            with open(manifest_path, encoding='utf-8') as mh:
                for line in mh:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split(None, 1)  # "<sha256>  <relative-path>"
                    if len(parts) == 2:
                        expected[parts[1].strip()] = parts[0].strip().lower()

        if actual and not expected:
            return False, ["Check 6 Fail: raw evidence present but INTAKE/RAW-MANIFEST.sha256 "
                           "is missing (run TOOLS/lore_freeze_raw.py)."]

        # Warn about excluded files — they exist in INTAKE/raw but are outside the
        # integrity boundary. This is intentional but must be visible to the author.
        warnings = []
        for rel in sorted(excluded):
            warnings.append(f"Check 6 Warn: '{rel}' excluded from integrity check (live sync artifact — not verifiable).")

        for rel, sha in sorted(actual.items()):
            if rel not in expected:
                errors.append(f"Check 6 Fail: unrecorded raw file (not in manifest): '{rel}'.")
            elif expected[rel] != sha:
                errors.append(f"Check 6 Fail: raw evidence mutated (hash mismatch): '{rel}'.")
        for rel in sorted(expected):
            if rel not in actual:
                errors.append(f"Check 6 Fail: manifest evidence missing on disk: '{rel}'.")

        all_messages = warnings + errors
        return len(errors) == 0, all_messages

    def check_corpus_manifest(self):
        """Check 10: Corpus Manifest Integrity Check."""
        manifest_path = os.path.join(self.repo_root, 'CORPUS-MANIFEST.yaml')
        errors = []
        if not os.path.exists(manifest_path):
            return False, ["Check 10 Fail: CORPUS-MANIFEST.yaml does not exist."]
        
        doc = load_doc(manifest_path)
        required_fields = ['corpus', 'version', 'status', 'schemas', 'registries']
        for rf in required_fields:
            if rf not in doc:
                errors.append(f"Check 10 Fail: CORPUS-MANIFEST.yaml missing required field '{rf}'.")
        
        for reg in doc.get('registries', []):
            if not os.path.exists(os.path.join(self.repo_root, reg)):
                errors.append(f"Check 10 Fail: Registry path '{reg}' referenced in manifest does not exist.")

        return len(errors) == 0, errors

def main():
    parser = argparse.ArgumentParser(
        description="LORE Corpus Workbench Standalone Validator",
        epilog=(
            "Single-artifact mode:  --file path/to/artifact.yaml\n"
            "                       --stdin  (reads YAML/JSON from stdin)\n"
            "Full corpus mode (default): runs all 10 checks + fixtures."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--path", help="Directory to scan (default: full fixture suite)")
    parser.add_argument("--file", metavar="FILE",
                        help="Validate a single artifact file and exit")
    parser.add_argument("--stdin", action="store_true",
                        help="Read a single artifact from stdin and validate it")
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    validator = LoreValidator(repo_root)

    # --- Single-artifact mode (--file or --stdin) ----------------------------
    if args.file or args.stdin:
        if args.stdin:
            import tempfile
            content = sys.stdin.read()
            # write to a temp file so validate_file can open it by path
            suffix = ".yaml"
            with tempfile.NamedTemporaryFile(mode='w', suffix=suffix,
                                             delete=False, encoding='utf-8') as tmp:
                tmp.write(content)
                tmp_path = tmp.name
            filepath = tmp_path
            label = "<stdin>"
        else:
            filepath = os.path.abspath(args.file)
            label = args.file
            if not os.path.isfile(filepath):
                print(f"Error: file not found: {filepath}", file=sys.stderr)
                sys.exit(2)

        ok, errs, warns = validator.validate_file(filepath)

        if args.stdin:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass

        tag = "[PASS]" if ok else "[FAIL]"
        print(f"{tag} {label}")
        for w in warns:
            print(f"  ~ {w}")
        for e in errs:
            print(f"  - {e}")
        sys.exit(0 if ok else 1)

    # --- Full corpus mode (default) ------------------------------------------
    print("=== LORE Corpus Workbench Validator (10 Core Checks) ===")

    total_passed = 0
    total_failed = 0

    # 1. Validate INTAKE/raw Immutability (Check 6)
    c6_ok, c6_msgs = validator.check_intake_raw_immutability()
    if c6_ok:
        print("[PASS] Check 6: INTAKE/raw Integrity (manifest)")
        for m in c6_msgs: print(f"  ~ {m}")  # warnings only on pass
        total_passed += 1
    else:
        print("[FAIL] Check 6: INTAKE/raw Integrity (manifest)")
        for m in c6_msgs:
            prefix = "  ~ " if "Warn:" in m else "  - "
            print(f"{prefix}{m}")
        total_failed += 1

    # 2. Validate Corpus Manifest Integrity (Check 10)
    c10_ok, c10_errs = validator.check_corpus_manifest()
    if c10_ok:
        print("[PASS] Check 10: Corpus Manifest Integrity")
        total_passed += 1
    else:
        print("[FAIL] Check 10: Corpus Manifest Integrity")
        for e in c10_errs: print(f"  - {e}")
        total_failed += 1

    # 3. Test Fixtures (or --path override)
    if args.path:
        # validate all YAML/JSON files under a given directory
        target_dir = os.path.abspath(args.path)
        target_files = []
        for dirpath, _, files in os.walk(target_dir):
            for f in sorted(files):
                if f.endswith(('.yaml', '.yml', '.json')):
                    target_files.append(os.path.join(dirpath, f))
        print(f"\n--- Validating files under {target_dir} ({len(target_files)}) ---")
        for fp in target_files:
            fname = os.path.relpath(fp, target_dir)
            ok, errs, warns = validator.validate_file(fp)
            tag = "[PASS]" if ok else "[FAIL]"
            print(f"{tag} {fname}")
            for w in warns: print(f"  ~ {w}")
            for e in errs: print(f"  - {e}")
            total_passed, total_failed = (
                (total_passed + 1, total_failed) if ok else (total_passed, total_failed + 1)
            )
    else:
        pos_dir = os.path.join(repo_root, 'TESTS', 'fixtures', 'positive')
        neg_dir = os.path.join(repo_root, 'TESTS', 'fixtures', 'negative')

        pos_fixtures = sorted(
            [os.path.join(pos_dir, f) for f in os.listdir(pos_dir)
             if f.endswith(('.yaml', '.yml'))]
        ) if os.path.exists(pos_dir) else []
        neg_fixtures = sorted(
            [os.path.join(neg_dir, f) for f in os.listdir(neg_dir)
             if f.endswith(('.yaml', '.yml'))]
        ) if os.path.exists(neg_dir) else []

        print(f"\n--- Validating Positive Fixtures ({len(pos_fixtures)}) ---")
        for pf in pos_fixtures:
            fname = os.path.basename(pf)
            ok, errs, warns = validator.validate_file(pf)
            if ok:
                print(f"[PASS] Positive Fixture: {fname}")
                for w in warns: print(f"  ~ {w}")
                total_passed += 1
            else:
                print(f"[FAIL] Positive Fixture: {fname}")
                for e in errs: print(f"  - {e}")
                total_failed += 1

        print(f"\n--- Validating Negative Fixtures ({len(neg_fixtures)}) ---")
        for nf in neg_fixtures:
            fname = os.path.basename(nf)
            ok, errs, warns = validator.validate_file(nf)
            if not ok:
                print(f"[PASS] Negative Fixture Correctly Rejected: {fname}")
                total_passed += 1
            else:
                print(f"[FAIL] Negative Fixture Unexpectedly Passed: {fname}")
                total_failed += 1

    print(f"\nSummary: {total_passed} passed, {total_failed} failed.")
    sys.exit(1 if total_failed > 0 else 0)

if __name__ == '__main__':
    main()
