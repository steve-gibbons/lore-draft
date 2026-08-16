#!/usr/bin/env python3
"""
LORE - verify detached signatures on AUTHOR-ONLY artifacts (KF-01 enforcement gate).

EXPERIMENTAL / provisional TEST HARNESS (DECISION-AUTH-IDENTITY.accepted.md, Option C).
Explicitly intended to be replaced by robust key management (hardware token / HSM,
rotation, revocation, multi-party custody). Not production trust infrastructure.

WHY THIS IS SEPARATE FROM THE CORE VALIDATOR
  The core validator (TOOLS/lore_validate.py) is zero-dependency and runs everywhere,
  so its Check 2 only confirms the *representation*: an author-only artifact names a
  registered signer and its detached .asc exists. THIS tool does the cryptography -
  GOODSIG/VALIDSIG, signer role, and lineage to a `root` - and is the enforcement gate
  run in CI and locally. Verification needs only the PUBLIC key (KEYS/*.asc); it never
  touches a secret, so it runs fine in CI. (CORE-INVARIANT 10: represent, then enforce.)

WHAT A PASS PROVES, per author-only artifact
  1. INTEGRITY - the artifact bytes are what was signed (any edit after signing fails).
  2. ROLE      - the signing-key fingerprint is listed in REGISTRIES/trusted-signers.txt
                 with an allowed role (default: `root`; --accept-delegated also allows
                 `delegated:agent` for lower-trust author-only artifacts).
  3. LINEAGE   - the signature chains to a `root` key (CORE-INVARIANT 11), and the signing
                 fingerprint matches the artifact's declared provenance.signer_fpr.

WHAT IT DOES NOT PROVE
  That a `root` key is held by the *legitimate* author (key custody / binding is the
  deeper KF-01 track: T5), nor that git history wasn't rewritten.

MIGRATION
  Author-only artifacts that carry no signature yet are reported as UNSIGNED (migration
  TODO), a warning by default. Run with --strict (the v1.0.0 posture) to make any unsigned
  author-only artifact a hard failure. TESTS/fixtures/ is skipped (placeholder signatures).

Exit 0 = all checked signatures accepted (and, under --strict, none unsigned).
Dependency-free apart from stdlib + `gpg`.
"""
import argparse
import json
import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SIGNERS = os.path.join(REPO, 'REGISTRIES', 'trusted-signers.txt')
STATUS_REG = os.path.join(REPO, 'REGISTRIES', 'artifact-statuses.yaml')
SKIP_DIRS = {'.git', 'TESTS', 'INTAKE'}


def load_trusted():
    """Return {fpr_upper: (role, label)} from the registry."""
    trusted = {}
    if not os.path.isfile(SIGNERS):
        return trusted
    with open(SIGNERS, encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(None, 2)
            if len(parts) < 2:
                continue
            trusted[parts[0].upper().replace(' ', '')] = (parts[1], parts[2] if len(parts) > 2 else '')
    return trusted


def author_only_statuses():
    """Read the author_only enum from the status registry (tiny hand-parse, no yaml dep)."""
    out = set()
    if not os.path.isfile(STATUS_REG):
        return out
    in_block = False
    for line in open(STATUS_REG, encoding='utf-8'):
        if re.match(r'\s*author_only:\s*$', line):
            in_block = True
            continue
        if in_block:
            m = re.match(r'\s*-\s*(\S+)', line)
            if m:
                out.add(m.group(1).strip().strip('"\''))
            elif line.strip() and not line.startswith(' '):
                break
    return out


def artifact_status_and_prov(path):
    """Return (status, signature_ref, signer_fpr) from a yaml/json artifact (shallow)."""
    try:
        txt = open(path, encoding='utf-8').read()
    except Exception:
        return None, None, None
    if path.endswith('.json'):
        try:
            d = json.loads(txt)
            prov = d.get('provenance', {}) or {}
            return d.get('status'), prov.get('signature'), prov.get('signer_fpr')
        except Exception:
            return None, None, None
    status = sig = fpr = None
    for line in txt.splitlines():
        m = re.match(r'status:\s*["\']?([A-Za-z0-9_-]+)', line)
        if m and status is None:
            status = m.group(1)
        m = re.match(r'\s+signature:\s*["\']?([^"\'\s]+)', line)
        if m:
            sig = m.group(1)
        m = re.match(r'\s+signer_fpr:\s*["\']?([0-9A-Fa-f ]{40,})', line)
        if m:
            fpr = m.group(1)
    return status, sig, fpr


def find_author_only_artifacts(statuses):
    hits = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(('.yaml', '.yml', '.json')):
                continue
            p = os.path.join(root, f)
            status, sig, fpr = artifact_status_and_prov(p)
            if status in statuses:
                hits.append((p, sig, fpr))
    return hits


def gpg_verify(artifact_path, asc_path):
    """Return (ok, signing_fpr, primary_fpr, raw) using gpg --status-fd."""
    try:
        proc = subprocess.run(
            ['gpg', '--status-fd', '1', '--verify', asc_path, artifact_path],
            capture_output=True, text=True,
        )
    except FileNotFoundError:
        return None, None, None, 'gpg not found on PATH'
    m = re.search(
        r'^\[GNUPG:\] VALIDSIG ([0-9A-Fa-f]{40})(?: \S+){8} ([0-9A-Fa-f]{40})',
        proc.stdout, re.MULTILINE)
    good = '[GNUPG:] GOODSIG' in proc.stdout
    if good and m:
        return True, m.group(1).upper(), m.group(2).upper(), proc.stdout + proc.stderr
    return False, None, None, proc.stdout + proc.stderr


def main():
    ap = argparse.ArgumentParser(description="Verify signatures on author-only artifacts (KF-01).")
    ap.add_argument('--strict', action='store_true',
                    help="Treat any UNSIGNED author-only artifact as a failure (v1.0.0 posture).")
    ap.add_argument('--accept-delegated', action='store_true',
                    help="Also accept role `delegated:agent` (lower-trust author-only artifacts).")
    args = ap.parse_args()

    trusted = load_trusted()
    roots = {f for f, (r, _) in trusted.items() if r == 'root'}
    allowed_roles = {'root'} | ({'delegated:agent'} if args.accept_delegated else set())
    if not roots:
        print("FAIL: no `root` signer in REGISTRIES/trusted-signers.txt")
        return 2

    statuses = author_only_statuses()
    if not statuses:
        print("FAIL: could not read author_only enum from REGISTRIES/artifact-statuses.yaml")
        return 2

    artifacts = find_author_only_artifacts(statuses)
    print(f"=== LORE author-only signature gate ({len(artifacts)} artifact(s)) ===")
    failed = unsigned = accepted = 0

    for path, sig_ref, fpr in sorted(artifacts):
        rel = os.path.relpath(path, REPO)
        if not sig_ref:
            unsigned += 1
            tag = 'FAIL' if args.strict else 'WARN'
            print(f"[{tag}] UNSIGNED author-only artifact (migration TODO): {rel}")
            if args.strict:
                failed += 1
            continue
        asc = os.path.join(REPO, sig_ref)
        if not os.path.isfile(asc):
            print(f"[FAIL] {rel}: detached signature missing at {sig_ref}")
            failed += 1
            continue
        ok, signing_fpr, primary_fpr, raw = gpg_verify(path, asc)
        if ok is None:
            print(f"[FAIL] {rel}: {raw}")
            failed += 1
            continue
        if not ok:
            print(f"[FAIL] {rel}: not a good signature over the current bytes (edited since signing?)")
            failed += 1
            continue
        declared = (fpr or '').upper().replace(' ', '')
        if declared and declared != signing_fpr:
            print(f"[FAIL] {rel}: signer_fpr {declared} != actual signing key {signing_fpr}")
            failed += 1
            continue
        if primary_fpr not in roots:
            print(f"[FAIL] {rel}: signature does not chain to a trusted root (lineage broken); primary {primary_fpr}")
            failed += 1
            continue
        if signing_fpr not in trusted:
            print(f"[FAIL] {rel}: signing key {signing_fpr} not listed in trusted-signers")
            failed += 1
            continue
        role, label = trusted[signing_fpr]
        if role not in allowed_roles:
            print(f"[FAIL] {rel}: signed by role `{role}`, requires: {' or '.join(sorted(allowed_roles))}")
            failed += 1
            continue
        accepted += 1
        print(f"[PASS] {rel}: {role} — {label} (lineage root {primary_fpr})")

    print(f"\nSummary: {accepted} accepted, {unsigned} unsigned, {failed} failed.")
    print("NOTE: EXPERIMENTAL test-harness gate — replace with robust key management.")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
