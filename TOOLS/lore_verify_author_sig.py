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
                 fingerprint matches the artifact's declared provenance.signer_fpr when
                 the artifact declares one.

HOW A SIGNATURE IS FOUND (the resolution contract)
  The signature for an artifact is the SIBLING file `<artifact>.asc`. An in-file
  `provenance.signature` declaration is corroborating, not authoritative.

  It used to be the only route: "signed" meant "the artifact says it is signed", so an
  artifact that simply omitted the field was counted UNSIGNED and skipped - the artifact
  decided whether it got verified. That is KF-01 one level down (authority asserted, not
  authenticated), and it was not theoretical: no artifact in this corpus declares the
  field, and four decision records carry real detached signatures that the gate could not
  see. If a declaration and a sibling name different files, that is ambiguous provenance
  and fails rather than picking one.

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


def resolve_signature(path, declared_ref):
    """Decide which detached signature covers `path`.

    Returns (asc_path | None, source, error | None) where `source` is 'sibling',
    'declared', or None. A returned asc_path is guaranteed to exist on disk.

    Precedence, and why:
      sibling only    -> sibling. The fix. A signature sitting next to its artifact is a
                         signature, whether or not the artifact mentions it.
      both, agreeing  -> sibling. The declaration corroborates; nothing to resolve.
      both, differing -> error. Two answers to "what signs this?" is not a detail to
                         paper over by preferring one; the author has to say which.
      declared only   -> declared, if it exists. Keeps signatures that legitimately live
                         elsewhere working, and keeps the missing-file case a FAIL.
      neither         -> unsigned.

    AUTHOR RULINGS (2026-08-21), recorded so they are not re-litigated by inference:
      - Declaration is DEMOTED, not removed. "Demote is the better model." A declaration
        alone still resolves, so a signature that legitimately lives elsewhere keeps
        working; what it can no longer do is be the sole gate on whether verification
        happens at all.
      - Disagreement is a hard error, "until we can generalize better." Explicitly
        PROVISIONAL: the rule is right for a corpus with one signing hand and one
        convention, and is expected to be revisited when signatures need to describe
        richer arrangements (multiple signers, rotated keys, signatures over subsets).
        Treat a future change here as reopening a settled question, not overturning one.
    """
    sibling = path + '.asc'
    have_sibling = os.path.isfile(sibling)
    declared = os.path.join(REPO, declared_ref) if declared_ref else None

    if have_sibling and declared:
        if os.path.abspath(declared) != os.path.abspath(sibling):
            return None, None, (
                "ambiguous provenance - a sibling signature exists at %s but the artifact "
                "declares %s. Remove one, or make the declaration name the sibling."
                % (os.path.relpath(sibling, REPO), declared_ref))
        return sibling, 'sibling', None
    if have_sibling:
        return sibling, 'sibling', None
    if declared:
        if not os.path.isfile(declared):
            return None, None, "declared signature missing at %s" % declared_ref
        return declared, 'declared', None
    return None, None, None


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
        asc, source, err = resolve_signature(path, sig_ref)
        if err:
            print(f"[FAIL] {rel}: {err}")
            failed += 1
            continue
        if asc is None:
            unsigned += 1
            tag = 'FAIL' if args.strict else 'WARN'
            print(f"[{tag}] UNSIGNED author-only artifact (migration TODO): {rel}")
            if args.strict:
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
        print(f"[PASS] {rel}: {role} — {label} (lineage root {primary_fpr}) [{source}]")

    print(f"\nSummary: {accepted} accepted, {unsigned} unsigned, {failed} failed.")

    # A gate that examined nothing has asserted nothing. Reporting success for an empty
    # set is how this gate came to be green while seven signed .md artifacts — AGENTS.md
    # among them — went unverified, and while no KEYS/*.asc existed for it to verify
    # against. Under --strict, "I checked zero things" is not a pass.
    vacuous = args.strict and accepted == 0 and unsigned == 0 and failed == 0
    if vacuous:
        print()
        print("FAIL: --strict, but this gate verified nothing.")
        if not artifacts:
            print("  No author-only artifacts were found at all. Either the corpus")
            print("  genuinely holds none, or discovery is not reaching them")
            print("  (this gate scans .yaml/.yml/.json only).")
        print("  A green gate must mean a signature was checked, not that none was.")
        return 1

    print("NOTE: EXPERIMENTAL test-harness gate — replace with robust key management.")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
