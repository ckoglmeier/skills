---
name: team-connections
description: >
  Find warm paths into any company or person through your team's combined network — LinkedIn
  connection exports from founders, teammates, board members, and advisors, plus an optional
  enriched dataset and optional network tools (e.g. VouchFor). Returns tiered results (🟢 Direct,
  🟣 Vouched, 🟡 One hop, ⚪ Cold), names the best connector for each path, and picks who should
  send the outreach. Use whenever a workflow needs "who do we know at X?" — prospect lists,
  investor or acquirer meeting prep, partnership outreach, hiring, or advisory asks. Trigger on:
  "who do we know at [company]", "warm path to [company/person]", "do we have a connection to
  [person]", "look up connections for [list]", "who can intro us to X". Also serves as the
  connection-lookup subroutine for person-profile, investor-profile, and prospecting skills.
---

# Team Connections

The shared network layer for a team's outreach. Other skills delegate "who do we know?" here
instead of each parsing CSVs their own way. Works standalone or as a subroutine — the logic is
the same; only the amount of surrounding prose changes.

---

## Setup (first run only)

All team data lives **outside the skill folder** so plugin updates never wipe it and it never
gets committed:

```
~/.claude/skill-data/team-connections/
├── config.md                 # team roster + routing rules (below)
└── connections/
    ├── connections_alex.csv  # one LinkedIn export per contributor
    └── connections_sam.csv
```

If `config.md` is missing, ask the user for the fields below, write the file, and tell them where
to drop the CSVs (LinkedIn → Settings → Data privacy → Get a copy of your data → Connections).
Don't ask for anything you can infer from the conversation.

```markdown
# Team Connections Config

**Team / company:** [Name]
**Connections folder:** ~/.claude/skill-data/team-connections/connections

## Contributors
| File suffix | Name | Role | Can send outreach? | Best-fit buyers / audiences |
|---|---|---|---|---|
| alex | Alex Rivera | Co-founder, CEO | yes | CEOs, CHROs, people leaders |
| sam  | Sam Lee | Co-founder, CTO | yes | CTOs, heads of AI/data/eng |
| pat  | Pat Kim | Board member | no (connector only) | — |

## Title keywords to scan for (optional)
head of ai, chief ai, vp ai, ai transformation, ai strategy

## Enriched dataset (optional)
**Path:** [CSV with linkedin_profile_url, current_title, current_company, confidence, resolved_at]
**Refresh command:** [command that re-resolves stale rows, if you have one]
```

---

## Lookup workflow

Run the three passes in parallel.

### Pass A — Team CSVs (always)

Run the bundled script. It handles LinkedIn's preamble rows, dedupes people who appear in several
contributors' exports, normalizes company names ("Acme Corp" = "Acme Corporation"), overlays the
enriched dataset if configured, and scans titles for the configured keywords:

```bash
python3 <skill-dir>/scripts/lookup.py --dir <connections folder> \
  --company "Acme" --company "Globex" \
  --person "Jane Smith" \
  --keywords "<keywords from config>" \
  --enriched "<enriched path, if configured>"
```

Output is JSON. Per match: name, title/company from the export, `current_title` /
`current_company` / `freshness` when enriched, `via` (every contributor connected to them, with
dates), `years_connected`, and `status`:
- `current` — at the target company now
- `moved_on` — the export says they were there but enriched data says they've left. Still useful
  (a former insider can often intro), but never present them as a current employee.

Read the JSON; don't dump it on the user.

**Freshness:** Title and company in a raw LinkedIn export reflect the moment it was exported and
go stale fast. When results matter (prospect lists, meeting prep) and rows come back `stale` or
`unresolved`, either run the configured refresh command for up to ~20 rows, or verify the top
2–3 contacts with a quick web search. Past ~20 stale rows, say so and recommend a bulk
enrichment run rather than doing it inline.

### Pass B — Network tools (if available)

Check what's connected in the session (search the tool list for "network", "vouch", "crm",
"contacts"). With VouchFor: `lookup_network(company)` per target, and for high-priority cold
targets `ask_my_network("who do I know with connections to [Company] or its leadership?")`.
A CRM connector (HubSpot, Salesforce, etc.) can also show prior touchpoints — include them as
context on the path.

If none are available, note it in the header and move on — the skill works fully on CSVs alone.

### Pass C — One-hop inference (cheap, targeted)

For high-priority targets with no Direct path, check whether any Direct connection *used to work*
at the target (`moved_on` rows) or currently works alongside the target person. Those are 🟡 One
hop candidates. Don't speculate beyond what the data shows.

---

## Tiers

| Tier | Criteria | Action |
|---|---|---|
| 🟢 **Direct** | In a contributor's CSV and `current` at the target | Message directly, or ask that contributor to intro |
| 🟣 **Vouched** | Network tool returns a recommendation chain | Use the tool's own intro flow (e.g. VouchFor Ask via `vouchfour_url`) — don't draft around it |
| 🟡 **One hop** | A Direct connection is a known former colleague or current peer of the target | Ask the contributor for an intro through that person |
| ⚪ **Cold** | Nothing in any source | Cold outreach, or skip |

A Vouched path outranks Direct as the lead path — it carries an endorsement. Show both when both
exist.

**Connection age matters:** 3+ years connected = established; under ~3 months = thin, say so.

---

## Connector vs. sender

Two different roles — always name the connector; the sender is a downstream call.

- **Connector** — whose network the path runs through. Any contributor.
- **Sender** — who sends the outreach. Only contributors marked "can send" in config. Pick by the
  best-fit column against the target's role; tie-break on the older connection. If the connector
  can send, they're usually both.

Flag non-founder connectors explicitly — a board member's intro reads differently than a founder's:

> 🟢 Direct (via **Pat Kim**, board member) — Jane Smith, Head of AI at Acme

---

## Output

**Header (standalone use):**
```
## Connection Lookup: [target(s)]
*Contributors loaded: alex (2,940), sam (930) · Enriched: 7,606 rows, 78% resolved · Network tools: VouchFor / none*
```

**5+ targets — lead with a scan table:**

| Company | Best path | Contact | Connector | Sender |
|---|---|---|---|---|
| Acme | 🟢 Direct | Jane Smith, Head of AI | Alex | Alex |
| Globex | 🟣 Vouched | Lee Jones, CAIO | VouchFor via Josh Scott | Sam |
| Initech | ⚪ Cold | — | — | — |

**Per-target block:**
```
### [Company]
**Best path:** [tier] — [Person, Title] | connector: [Name, Role] | sender: [Name]
Also: [secondary paths, one line each]
- [Person] ([Title]) — [contributor]'s connection since [Mon YYYY] · [freshness if not fresh] · [URL]
```
Cold targets get one line: `### Initech — ⚪ No path found`.

**Keyword-scan hits** at companies not on the list go in a closing "Potential additions" table
(person, title, company, connector) — useful leads, clearly separated from the answer.

As a **subroutine**, skip the header and prose; return the per-target blocks for the caller to
fold into its own document.

---

## Guardrails

- Connection data is personal information. Keep the CSVs in the skill-data folder, never in a
  repo, and don't paste bulk contact lists into chat — surface only the people relevant to the ask.
- Never claim someone is currently at a company on the strength of an old export alone.
- A LinkedIn connection is not a relationship. Say how old and how corroborated a path is, and let
  the user judge its warmth.
