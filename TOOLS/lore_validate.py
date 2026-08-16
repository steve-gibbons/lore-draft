#!/usr/bin/env python3
"""
LORE Corpus Workbench Validator (TOOLS/lore_validate.py)
Implements 10 minimum governance, structural, and schema checks per AGENTS v3 specification.
Standard Python 3 implementation with zero external dependencies.
"""

import sys
import os
import re
import json
import hashlib
import stat
import argparse

class SimpleYAMLParser:
    """Minimal recursive dependency-free YAML parser for dictionaries, lists, and scalars."""
    @staticmethod
    def parse(content):
        lines = content.splitlines()
        
        def parse_node(index, indent):
            res = None
            while index < len(lines):
                line = lines[index]
                # Strip comments unless in quotes
                comment_idx = line.find('#')
                if comment_idx != -1:
                    if not (line[:comment_idx].count('"') % 2 != 0 or line[:comment_idx].count("'") % 2 != 0):
                        line = line[:comment_idx]
                if not line.strip():
                    index += 1
                    continue
                
                cur_indent = len(line) - len(line.lstrip())
                if cur_indent < indent:
                    break
                
                stripped = line.strip()
                if stripped.startswith('- '):
                    if res is None: res = []
                    val = stripped[2:].strip().strip('"\'')
                    if val.lower() == 'true': val = True
                    elif val.lower() == 'false': val = False
                    if isinstance(res, list):
                        res.append(val)
                    index += 1
                elif ':' in stripped:
                    if res is None: res = {}
                    parts = stripped.split(':', 1)
                    key = parts[0].strip().strip('"\'')
                    val_str = parts[1].strip()
                    if not val_str:
                        child, next_idx = parse_node(index + 1, cur_indent + 1)
                        if isinstance(res, dict):
                            res[key] = child if child is not None else []
                        index = next_idx
                    else:
                        val = val_str.strip('"\'')
                        if val.lower() == 'true': val = True
                        elif val.lower() == 'false': val = False
                        elif val.startswith('[') and val.endswith(']'):
                            val = [i.strip().strip('"\'') for i in val[1:-1].split(',') if i.strip()]
                        if isinstance(res, dict):
                            res[key] = val
                        index += 1
                else:
                    index += 1
            return res, index

        res, _ = parse_node(0, 0)
        return res if res is not None else {}

def load_doc(filepath):
    """Load JSON or YAML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if filepath.endswith('.json'):
        return json.loads(content)
    else:
        try:
            return json.loads(content)
        except Exception:
            return SimpleYAMLParser.parse(content)

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

class LoreValidator:
    def __init__(self, repo_root):
        self.repo_root = repo_root
        self.agent_writable, self.author_only, self.transitions = get_registry(repo_root)
        self.all_statuses = (self.agent_writable or set()).union(self.author_only or set())

    def validate_file(self, filepath):
        doc = load_doc(filepath)
        errors = []
        
        # Check 1: Status Enum Check
        status = doc.get('status')
        if status:
            if status not in self.all_statuses:
                errors.append(f"Check 1 Fail: Status '{status}' is not in closed status enum.")

        # Check 2: Agent Status Emission Rule
        if status in self.author_only:
            provenance = doc.get('provenance', {})
            author_preseeded = False
            if isinstance(provenance, dict):
                author_preseeded = provenance.get('author_preseeded', False)
            if not author_preseeded:
                errors.append(f"Check 2 Fail: Author-only status '{status}' emitted without author preseed provenance.")

        # Check 3: Status Transition Check
        prev_status = doc.get('previous_status')
        if prev_status and status:
            allowed = self.transitions.get(prev_status, {}).get('allowed_next', [])
            if status not in allowed:
                errors.append(f"Check 3 Fail: Illegal status transition from '{prev_status}' to '{status}'. Allowed: {allowed}")

        # Check 4: Schema Conformance Check
        doc_type = doc.get('type')
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
        elif doc_type == 'object-ref':
            if 'target_id' not in doc: errors.append("Check 4 Fail: object-ref missing required field 'target_id'.")

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
        if doc_type == 'object-ref':
            target_id = doc.get('target_id')
            if not target_id or not isinstance(target_id, str):
                errors.append("Check 7 Fail: Invalid or missing target_id in object-ref.")

        # Check 8: Explicit Transformation Provenance
        if doc_type == 'transformation-record' or status in ('derived', 'generated'):
            inputs = doc.get('inputs')
            if not inputs or not isinstance(inputs, list) or len(inputs) == 0:
                errors.append("Check 8 Fail: Derived/generated artifact missing required 'inputs' list.")

        # Check 9: Uncertainty Preservation Check
        if doc_type == 'proposal-record' and status not in self.agent_writable:
            errors.append(f"Check 9 Fail: Unverified proposal must retain uncertainty status, got '{status}'.")

        return len(errors) == 0, errors

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
        skip = {'README.md', '.DS_Store'}
        errors = []
        if not os.path.exists(intake_raw):
            return True, []

        # Actual raw files on disk -> sha256 (paths relative to INTAKE/raw)
        actual = {}
        for root, dirs, files in os.walk(intake_raw):
            for f in files:
                if f in skip:
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

        for rel, sha in sorted(actual.items()):
            if rel not in expected:
                errors.append(f"Check 6 Fail: unrecorded raw file (not in manifest): '{rel}'.")
            elif expected[rel] != sha:
                errors.append(f"Check 6 Fail: raw evidence mutated (hash mismatch): '{rel}'.")
        for rel in sorted(expected):
            if rel not in actual:
                errors.append(f"Check 6 Fail: manifest evidence missing on disk: '{rel}'.")
        return len(errors) == 0, errors

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
    parser = argparse.ArgumentParser(description="LORE Corpus Workbench Standalone Validator")
    parser.add_argument("--path", help="Specific file or directory to validate")
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    validator = LoreValidator(repo_root)

    print("=== LORE Corpus Workbench Validator (10 Core Checks) ===")
    
    total_passed = 0
    total_failed = 0

    # 1. Validate INTAKE/raw Immutability (Check 6)
    c6_ok, c6_errs = validator.check_intake_raw_immutability()
    if c6_ok:
        print("[PASS] Check 6: INTAKE/raw Integrity (manifest)")
        total_passed += 1
    else:
        print("[FAIL] Check 6: INTAKE/raw Integrity (manifest)")
        for e in c6_errs: print(f"  - {e}")
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

    # 3. Test Fixtures
    pos_dir = os.path.join(repo_root, 'TESTS', 'fixtures', 'positive')
    neg_dir = os.path.join(repo_root, 'TESTS', 'fixtures', 'negative')

    pos_fixtures = [os.path.join(pos_dir, f) for f in os.listdir(pos_dir) if f.endswith(('.yaml', '.yml'))] if os.path.exists(pos_dir) else []
    neg_fixtures = [os.path.join(neg_dir, f) for f in os.listdir(neg_dir) if f.endswith(('.yaml', '.yml'))] if os.path.exists(neg_dir) else []

    print(f"\n--- Validating Positive Fixtures ({len(pos_fixtures)}) ---")
    for pf in sorted(pos_fixtures):
        fname = os.path.basename(pf)
        ok, errs = validator.validate_file(pf)
        if ok:
            print(f"[PASS] Positive Fixture: {fname}")
            total_passed += 1
        else:
            print(f"[FAIL] Positive Fixture: {fname}")
            for e in errs: print(f"  - {e}")
            total_failed += 1

    print(f"\n--- Validating Negative Fixtures ({len(neg_fixtures)}) ---")
    for nf in sorted(neg_fixtures):
        fname = os.path.basename(nf)
        ok, errs = validator.validate_file(nf)
        if not ok:
            print(f"[PASS] Negative Fixture Correctly Rejected: {fname}")
            total_passed += 1
        else:
            print(f"[FAIL] Negative Fixture Unexpectedly Passed: {fname}")
            total_failed += 1

    print(f"\nSummary: {total_passed} passed, {total_failed} failed.")
    if total_failed > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
