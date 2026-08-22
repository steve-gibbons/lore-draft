# Ceremony 2026-08-22 — decision points (key state)

**Status:** evidence / process log (not an accepted record)  
**Rule:** append a row at every branch cut, policy amend, accept/sign, or public SHA pin. Do not rewrite history; add a line.

## Key state (this ceremony)

| Role | Fingerprint | Notes |
|------|-------------|-------|
| Author primary (root lineage) | `7309F037A9457C7601C7F3BF068354FBD9B04B5C` | D9B04B5C; published in `KEYS/` |
| Active signing subkey | `69FADB148F4DCAC85FD59E183E5A2E38850E0C22` | 69FADB14; used for all 2026-08-22 `lore sign` |
| Public checkout | `~/Developer/lore-public` → `steve-gibbons/lore-draft` | |
| Private checkout | `~/Developer/lore` → `steve-gibbons/lore` | |

Unusable / missing-secret subkeys remain listed in `REGISTRIES/trusted-signers.txt`. They are not used here.

## Log

| When (UTC) | Point | Private SHA | Public SHA (`lore-draft`) | Signer | What |
|------------|-------|-------------|---------------------------|--------|------|
| 2026-08-22 | Gate A | (pre-package) | `dffb11c` | — | Author: promote recommended minimum |
| 2026-08-22 | Gate B OBS-001 | `1606891` | `dffb11c` | 69FADB14 | accept + detach-sign |
| 2026-08-22 | Gate B IBMBOB-001 | `f767bf4` | `dffb11c` | 69FADB14 | accept + detach-sign |
| 2026-08-22 | Gate B PROP-001 | `49c0907` | `dffb11c` | 69FADB14 | accept + detach-sign (`lore publish` spec; verb not implemented) |
| 2026-08-22 | Export order | `c722df4` | `dffb11c` | — | PRESERVE before leak-scan; skip-copy PRESERVE paths |
| 2026-08-22T17:31Z | Leak-scan amend | `2d944dc` | `dffb11c` | — | Drop public-identity patterns; keep path/URL/non-public mail |
| 2026-08-22T17:43Z | Whitelist Gate B | `43b7276` | `dffb11c` | — | OBS/IBMBOB/PROP accepted+.asc + DECISION-POINTS.md on whitelist |
| 2026-08-22T17:54Z | Public export | `43b7276` | `f2ab129` | — | lore-draft overlay; leak-scan CLEAN; manifest rebuilt on published tree |
| 2026-08-22T18:16Z | TR-002 accepted | `49082f1` | `f2ab129` | 69FADB14 | signed TR-PUBLIC-EXPORT-002.accepted.yaml |
| 2026-08-22T18:31Z | Whitelist TR-002 | `c5f1279` | `e54e567` | — | accepted TR yaml+.asc on whitelist for public overlay |
| 2026-08-22T18:34Z | Public TR overlay | `c5f1279` | `8467838` | — | TR-002 accepted+.asc + whitelist yaml on lore-draft |
| 2026-08-22T18:45Z | CI always() | `649c266` | `8467838` | — | signature convention + LL-004 no longer muted |
| 2026-08-22T18:46Z | Public gitignore | `649c266` | `cf2869a` | — | Developer path note + extensionless iCloud hole |
| 2026-08-22T18:49Z | Public KEYS | `649c266` | `bd787d0` | — | current bundle + 69FADB14; D9B04B5C.asc alias |
| 2026-08-22T18:52Z | Gate D nits | `9931b91` | `bd787d0` | — | private KEYS alias, README, MMETA typo, runbook executed banner |
| 2026-08-22T19:05Z | lore publish | `f628244` | `8847d5f` | — | compose export+manifest+validate; no commit/push/TR-promote |
| 2026-08-22T19:16Z | Public publish overlay | `f628244` | `23d4d59` | — | lore publish live; leak-scan CLEAN; validate 48/0 |
| 2026-08-22T19:23Z | Tree-local verbs + TR next | `a23bcec` | `23d4d59` | — | dispatcher/CI skip missing tools; next export is TR-003 (002 accepted stays) |
| 2026-08-22T19:39Z | Public overlay | `a23bcec` | `ac9741d` | — | tree-local dispatcher+CI; TR-003.draft; TR-002 still accepted |
| 2026-08-22T20:00Z | TR-003 accepted | `5e835a6` | `ac9741d` | 69FADB14 | signed TR-003 |
| 2026-08-22T20:01Z | TR template verbs | `17be150` | `ac9741d` | -- | generator verbs |
| 2026-08-22T20:04Z | Whitelist TR-003 | `6ecd264` | `ac9741d` | -- | TR-003 yaml+asc |
| 2026-08-22T20:22Z | Public export | `5ac867a` | `e381186` | -- | lore publish; TR-003 on lore-draft |
| 2026-08-22T20:29Z | TR-004 receipt | `54896f4` | `e381186` | 69FADB14 | accept TR-004 private only; no re-export |
| 2026-08-22T21:10Z | QA CI hole | `54896f4` | `e381186` | — | lore_yaml absent on public; local PyYAML hid it |
| 2026-08-22T21:30Z | Whitelist TCB | *(this commit)* | `e381186` | — | TOOLS/lore_yaml.py + OBS-EXPORT-TCB-CLOSURE candidate; AI-003 stays open |

## Next line (template)

```
| YYYY-MM-DDTHH:MMZ | <point> | <private SHA> | <public SHA or —> | 69FADB14 or — | <one line> |
```
