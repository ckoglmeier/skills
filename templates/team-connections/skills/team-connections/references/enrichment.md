# Enrichment — keeping current titles current

LinkedIn exports freeze each person's title and company at export time. Enrichment re-resolves
them into `enriched.csv`, which `lookup.py` overlays automatically. Everything lives in
`~/.claude/skill-data/team-connections/`.

```
enriched.csv      one row per person: export fields + current_title/company, confidence, resolved_at
overrides.json    hand-verified corrections; always win (see format below)
pending.jsonl     the current research queue
results.jsonl     research results waiting to merge
backups/          a copy of enriched.csv before every merge
```

## The loop

```bash
S=<skill-dir>/scripts
python3 $S/enrich.py ingest                 # pick up new/changed exports (safe to re-run)
python3 $S/enrich.py status                 # fresh / stale / low / never_attempted
python3 $S/enrich.py queue --limit 20 [--company Acme] [--keywords "head of ai,cfo"]
#   → resolve pending.jsonl by ONE of the two paths below → results.jsonl
python3 $S/enrich.py merge                  # backs up, validates, merges, re-applies overrides
```

`ingest --seed old.csv` imports enrichment from an earlier dataset that uses the same column
names (`linkedin_profile_url`, `current_title`, `current_company`, `confidence`, `resolved_at`).

Queue priority: target companies first, then never-attempted before failed, then people several
teammates know, then title-keyword matches.

## Path A — Perplexity API (bulk, preferred)

If `PERPLEXITY_API_KEY` is set:

```bash
python3 $S/enrich.py perplexity --rpm 40    # sequential, rate-limited, appends to results.jsonl
```

The default of 40 requests/minute stays under Perplexity's tier-1 cap. Don't raise it unless
the account tier is higher. Costs are roughly $0.002 per person on `sonar`. Batches of 100–300
work well; check `status` and spot-check a few `high` rows between batches.

## Path B — Web-search subagents (no API key; small batches)

For each line in `pending.jsonl`, run one subagent on a fast, inexpensive model, 8 at a time,
with the prompt below. Collect each agent's JSON, add the person's `linkedin_profile_url`, and
append it as one line to `results.jsonl`. Web search resolves far fewer people than Perplexity
(expect roughly 10–40% usable), so keep this path to targeted batches of 20–50 and suggest
Path A for anything bigger.

```
Find the CURRENT job title and employer for this person. Return ONLY a JSON object.

Name: {full_name}
LinkedIn: {linkedin_profile_url}
Old hint (from an outdated export): {title_hint} at {company_hint}

Rules:
- Anchor identity on the LinkedIn URL when given; a same-name stranger is worse than no answer.
- Ambiguous, multiple matches, or not found → confidence "low", blank title/company, reason in notes.
- A recent post announcing a move beats a stale headline or company bio.
- One or two searches. Never invent a title or company.

{"current_title": "", "current_company": "", "confidence": "high|medium|low", "notes": ""}
```

Confidence: **high** = the LinkedIn URL or two independent recent sources confirm the role;
**medium** = one credible source, unambiguous identity; **low** = anything less.

Before merging, discard any record with every field empty — that agent didn't actually
search. `merge` enforces this too, and it never downgrades a verified row with a failed retry.

## Overrides

For people the searches keep getting wrong (common names, board-only roles, recent moves),
add a hand-verified entry to `overrides.json`. Overrides re-apply after every ingest and merge:

```json
{"overrides": [
  {"match": {"linkedin_url": "https://linkedin.com/in/jane-doe"},
   "current_title": "Operating Partner", "current_company": "Example Capital",
   "confidence": "high", "notes": "confirmed on call 2026-09"},
  {"match": {"full_name": "Sam Lee", "company_hint": "Globex"},
   "current_title": "CFO", "current_company": "Initech", "confidence": "high"}
]}
```

## Invariants

- Only the script writes `enriched.csv`. Never edit it by hand. Use overrides for corrections.
- A blank is always better than a wrong match.
- All of this is personal data. It stays in skill-data and is never committed or pasted into chat.
