# LORE Workbench Harness v0.1 (mini-effort)

Thin local-first CLI + optional transport for LORE-shaped records and administrivia handoffs.

**This is workbench administrivia / first glue — not LORE core.**

## Quick start

```bash
chmod +x lore
./lore init --generate-token
./lore create assertion --stdin <<'EOF'
claim: "example"
subject_ref: "thing:local:demo"
EOF
./lore list
./lore handoff create --from agent:a --to agent:b --objective-ref "assertion:local:…"
./lore serve          # http://127.0.0.1:22469
```

## Contracts

- `CONTRACT.md` — scope, non-goals, acceptance criteria
- `INTERFACE-CONTRACTS.md` — CLI, object envelope, handoff, HTTP, auth, events

## Layout after `init`

```text
.lore/
├── config.yaml
├── objects/{principal,policy,object-ref,relationship,act,assertion,authority,capability,handoff}/
├── events/events.ndjson
├── cache/
└── secrets/token.json    # verifier only
```

## Auth

Bearer token (`lore_…`) authorizes **transport into quarantine only**.  
Preferred verifier: Argon2id (optional `argon2-cffi`).  
Fallback: `hashlib.scrypt` (stdlib).

## Port

Default listener: **127.0.0.1:22469**

## Existing governance path

`validate`, `freeze`, `sign`, `verify`, `reseal`, `status`, `prompt` remain the governance verbs and continue to dispatch to the repo’s existing `TOOLS/` scripts when present.
