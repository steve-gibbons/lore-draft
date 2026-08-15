#!/usr/bin/env python3
"""
LORE prompt assembler  —  EXPERIMENTAL / PROVISIONAL (not production-ready).

Composes: governance kernel + role profile + lens card  ->  ready-to-paste prompt.
The kernel/profile lives in ONE place (profiles/*.txt) so no swapped "hat" can drift
from the governance rules. You swap only the lens.

Sole permitted use: evaluation of the LORE corpus itself and demonstration of principles.
Dependency-free (stdlib only), per AGENTS.md scope control. Path-independent: resolves its
data relative to this file, so it works from any working directory.

Usage:
  python3 TOOLS/lore_prompt.py --list
  python3 TOOLS/lore_prompt.py P1-SEC-THREATMODEL            # positional lens
  python3 TOOLS/lore_prompt.py --lens P6-LONGHORIZON --profile evaluator
"""
import argparse
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PANEL = os.path.join(REPO, 'META-CONTEXT', 'reviewer-panel')
PROFILE_DIR = os.path.join(PANEL, 'profiles')
LENSES_FILE = os.path.join(PANEL, 'lenses.md')
LENS_SLOT = '<<LENS CARD>>'
LENS_DELIM = re.compile(r'^###\s+LENS:\s+(\S+)\s*$', re.M)

BANNER = (
    "============================================================\n"
    "EXPERIMENTAL · PROVISIONAL WORK PRODUCT — NOT PRODUCTION-READY\n"
    "Sole permitted use: evaluation of the LORE corpus itself and\n"
    "demonstration of principles. Not suitable for any other process.\n"
    "============================================================"
)


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def load_lenses():
    if not os.path.exists(LENSES_FILE):
        return {}
    parts = LENS_DELIM.split(read(LENSES_FILE))
    # parts = [preamble, id1, body1, id2, body2, ...]
    return {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts), 2)}


def load_profiles():
    if not os.path.isdir(PROFILE_DIR):
        return {}
    return {os.path.splitext(f)[0]: os.path.join(PROFILE_DIR, f)
            for f in os.listdir(PROFILE_DIR) if f.endswith('.txt')}


def print_index(profiles, lenses, hint=False):
    print("Profiles: " + (", ".join(sorted(profiles)) or "(none)"))
    print("Lenses:")
    for lid in sorted(lenses):
        print("  - " + lid)
    if hint:
        print("\n(no lens given — pass one, e.g.:  python3 TOOLS/lore_prompt.py P1-SEC-THREATMODEL)")


def main():
    profiles = load_profiles()
    lenses = load_lenses()

    ap = argparse.ArgumentParser(description="Assemble a LORE hat prompt (EXPERIMENTAL).")
    ap.add_argument('lens_id', nargs='?', help='lens id (positional; alternative to --lens)')
    ap.add_argument('--profile', default='evaluator')
    ap.add_argument('--lens')
    ap.add_argument('--list', action='store_true', help='list profiles and lenses, then exit')
    args = ap.parse_args()

    lens = args.lens or args.lens_id

    if args.list or not lens:
        print_index(profiles, lenses, hint=(not lens and not args.list))
        return

    if lens not in lenses:
        sys.exit("Unknown lens '%s'. Available: %s" % (lens, ", ".join(sorted(lenses))))
    if args.profile not in profiles:
        sys.exit("Unknown profile '%s'. Available: %s" % (args.profile, ", ".join(sorted(profiles))))

    profile_text = read(profiles[args.profile])
    lens_text = lenses[lens]
    if LENS_SLOT in profile_text:
        composed = profile_text.replace(LENS_SLOT, lens_text)
    else:
        composed = profile_text + "\n\n----- ACTIVE LENS -----\n" + lens_text

    print(BANNER)
    print("[assembled: profile=%s · lens=%s]\n" % (args.profile, lens))
    print(composed)


if __name__ == '__main__':
    main()
