# Drift Audit

Use this reference when comparing a public package against a closed-source/internal version.

## Surface Map

Create a table with these rows when applicable:

| Surface | Public source | Closed-source source | Status | Notes |
|---|---|---|---|---|
| API/schema/contract | | | | |
| Generated output | | | | |
| README/docs/copy | | | | |
| Examples/fixtures | | | | |
| Tests | | | | |
| Package metadata | | | | |
| Release/export path | | | | |

## Status Labels

- `in_sync`: behavior, interface, or claim matches.
- `intentional_private`: internal capability is private by design and should stay out of the public package.
- `public_missing`: public package is under-documented or missing a needed capability.
- `closed_source_drift`: private implementation no longer satisfies the public contract.
- `risky_leakage`: public artifact exposes private details, unsupported claims, or confusing internal scaffolding.

## Audit Rules

- Compare behavior and contracts before comparing wording.
- Treat tests and fixtures as contract evidence.
- Treat generated outputs as first-class: stale generated copy can drift even when source looks correct.
- Do not assume private is more correct than public; identify the source of truth explicitly.
- When fixing, update the narrowest surface that restores contract clarity.
