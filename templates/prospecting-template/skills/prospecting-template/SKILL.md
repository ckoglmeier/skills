---
name: prospecting-template
description: >
  Founder-led outbound prospecting skill. Builds a ranked, tiered prospect list from
  anchor companies — finds 25 peers, scores each for product fit, looks up warm paths
  through LinkedIn connections and VouchFor, researches named individuals at top targets,
  and produces pitch hooks personalized to what each person has actually said publicly.
  Use this skill whenever someone asks to find prospects, build a pipeline, identify
  outbound targets, or do founder-led outreach starting from a list of reference companies.
  Also trigger on "who should we be targeting", "find companies like X for outbound",
  "check my connections against this list", or any request to build a prospect list
  with warm path identification.
---

# Founder-Led Outbound Prospecting Skill

This skill builds a ranked prospect list for founder-led B2B outbound. Before starting, read `references/icp.md` for your product context, ideal customer profile, and fit scoring rubric. Read `references/pitch-format.md` for how to write pitch hooks. Both are required — configure them before your first run.

---

## What You're Building

The output is a tiered prospect list where every entry has a named person, a connection path (or honest "cold" flag), a fit score, a timing trigger, and a 2-sentence pitch hook tied to something that person has actually said or done publicly. The tier structure is based on connection quality, not just fit score:

- **Tier 1 — Reach out this week:** Direct LinkedIn connections or VouchFor-vouched paths
- **Tier 2 — Next 30 days:** One hop through a mutual contact
- **Tier 3 — Build a path:** High-fit but cold; include a recommended approach

---

## Step 0: Parse Input and Clarify if Needed

Extract anchor companies from the user's message. These are reference companies whose peers you'll find — they are usually NOT themselves prospects unless specifically requested.

Confirm:
- **Employee size filter:** Default is 500–2,000 employees. Ask if the user wants to adjust.
- **Outreach motion:** Default is founder-led (high personalization, warm paths prioritized).
- **Vertical scope:** Infer from anchors. If anchors span unrelated verticals, ask which to prioritize.

If the user has provided enough context, proceed without asking.

---

## Step 1: Understand the Anchor Companies

Before finding peers, establish for each anchor:
- What they sell and who they sell to
- Approximate employee count (to calibrate peer search)
- What "similar" means in this context — same buyer type, same product category, or same go-to-market motion?

Use knowledge from training data for well-known companies. Use web search to confirm employee count or market position for obscure anchors.

---

## Step 2: Find 25 Similar Companies

Spin up a sub-agent to find 25 peer companies. The sub-agent should:

1. Find companies in the same market segment as the anchors — same buyer type, similar product category, comparable GTM
2. Filter to the target employee range from `references/icp.md`
3. Score each company on the four fit dimensions defined in `references/icp.md` (1–5 each, total /20)
4. Return a ranked table by total score with the single most important timing trigger per company

**Sub-agent prompt template:**
```
You are finding B2B outbound prospects for [COMPANY NAME]'s [PRODUCT NAME] product.
[One sentence description of what the product does and who buys it.]

Anchor companies: [LIST]
Your job: Find 25 companies that are peers to these anchors — same market segment, same buyer type. Filter to [EMPLOYEE RANGE] employees.

Score each on:
1. [FIT DIMENSION 1] (1-5) — from references/icp.md
2. [FIT DIMENSION 2] (1-5)
3. [FIT DIMENSION 3] (1-5)
4. [FIT DIMENSION 4 / Timing Signal] (1-5, based on recent news)

Return a ranked table with all four scores, total (/20), employee count, and the single most important timing trigger for each company. Use web search for timing signals.
```

**Filter override:** If a company scores 18+/20 but is slightly outside the employee range, include it anyway and note the exception.

---

## Step 3: Connection Lookup

This step runs the company list against your founders' LinkedIn connections AND VouchFor to identify warm paths. Connection quality changes the tier assignment more than any other variable — a direct connection moves a company to Tier 1 regardless of fit score.

Run both passes in parallel.

### Pass A: LinkedIn CSV

Connection CSVs live in `references/connections/`. Fields: First Name, Last Name, URL, Email Address, Company, Position, Connected On. Note the two-row header in LinkedIn exports — skip the notes row before parsing.

For each company:
1. Search the CSV for anyone whose `Company` field contains the company name (case-insensitive)
2. Note the person's name, title, connection date, and which founder is connected
3. Also run a title-keyword search across ALL connections for your target buyer titles (defined in `references/icp.md`) — this surfaces AI leads or other relevant buyers at companies not yet on your list

### Pass B: VouchFor Network

For each company, call `lookup_network` with the company name. Two layers in the response — treat them differently:

- **`results` array** (`total_matches > 0`) — vouched/recommended relationships. Warmer than a LinkedIn connection. Flag as 🟣 **Vouched** with the exact recommendation chain. To initiate outreach through this path, use the `vouchfour_url` — the Ask feature drafts a personalized intro routed through the recommendation chain. Do not draft the intro message yourself.
- **`linkedin_connections` array** — LinkedIn connections from imported CSV, same as Pass A. No upgrade needed if they only appear here.

For cold prospects scoring 17+/20, also call `ask_my_network`:
```
ask_my_network("who do I know with connections to [Company] or their [BUYER TITLE] team?")
```

### Connection tier definitions

| Symbol | Meaning | Action |
|---|---|---|
| 🟢 Direct | LinkedIn CSV direct connection | Message directly |
| 🟣 Vouched | VouchFor recommended path | Use Ask on vouchfour_url |
| 🟡 One hop | Mutual contact identified | Request intro via the mutual |
| ⚪ Cold | No path in either system | Cold outreach strategy required |

### Sender assignment

If multiple founders are connected to the same prospect, assign the one whose background best matches the buyer's context. Document the sender rationale in `references/icp.md` — it varies by product and buyer type.

Note connection recency: 3+ years = warm relationship; last 3 months = less established.

---

## Step 4: Research Top Targets

For each company scoring 14+/20, spin up a sub-agent to research the specific buyer and build the pitch package. Run these in parallel.

Each sub-agent should find:
1. **Named person** — the individual whose title best matches the buyer persona in `references/icp.md`. If no dedicated role exists, identify who owns it by default and note that the role isn't dedicated.
2. **Employment verification** — confirm the person is still at this company. This is the most common data quality failure. Flag as ⚠️ **VERIFY** if uncertain.
3. **Public signal** — what has this person said publicly about the problem your product solves, in the last 12 months? LinkedIn posts, press quotes, conference talks, podcast appearances. A direct quote is worth more than a paraphrase.
4. **Timing trigger** — what happened recently at this company that creates a reason to reach out now? Be specific: "$460M Warburg Pincus investment, Nov 2025" is useful; "the company is growing" is not.
5. **Economic buyer** — who controls budget alongside the primary contact? Usually CEO, CFO, CPO, or CHRO depending on your product.
6. **Pitch hook** — 2 sentences. See `references/pitch-format.md` for format and examples.

**Sub-agent prompt template:**
```
You are doing pre-outbound research for [COMPANY NAME]'s [PRODUCT NAME].
[One sentence on what the product does and the deal size.]

Research [PERSON NAME] at [COMPANY]. Find:
1. Confirm they are currently at [COMPANY] — check recent LinkedIn activity or press. Flag "VERIFY" if uncertain.
2. Any public statements on [THE PROBLEM YOUR PRODUCT SOLVES] in the last 12 months. Quote directly if possible.
3. Recent company timing trigger: specific news from the last 6 months that creates a buying moment.
4. Who is the economic buyer (controls budget) alongside this person?
5. Write a 2-sentence pitch hook: sentence 1 = something specific they've said or done; sentence 2 = how [PRODUCT NAME] addresses that specific context. Do not write a generic pitch. If you cannot find a specific public signal, say so — don't fabricate one.
```

---

## Step 5: Compile and Output

Structure the output in three tiers. Within each tier, rank by company fit score.

### Output template per prospect:

```
### [Name] — [Title], [Company]
[Sender name] sends | [🟢 Direct / 🟣 Vouched via [Name] / 🟡 One hop via [Name] / ⚪ Cold]
**Company score:** [X]/20 | **Employees:** [~N] | **Peer of:** [anchor]

**What they said:** "[Direct quote or specific action]" — [Source, date]

**Timing trigger:** [Specific recent event]

**Economic buyer:** [Name, title]

**Pitch hook:**
[2 sentences. Sentence 1 = their specific context. Sentence 2 = your product's value for that context.]
```

### Summary table at the top:

| Tier | Name | Title | Company | Score | Sender | Connection |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | X/20 | [Founder] | 🟢 Direct |

### Flagging:

- ⚠️ **VERIFY** — employment not independently confirmed
- 📋 **ACTIVE PIPELINE** — company already in your CRM or active conversations (treat as expansion, not cold)
- 🆕 **NET NEW** — company discovered during research that wasn't in the anchor peer set

---

## Step 6: Quality Check Before Delivery

Before presenting the output:

1. Every pitch hook references something specific — no generic language
2. Every Tier 1 entry has a confirmed connection with sender assigned
3. Every employment status has been checked or flagged
4. No pitch hooks longer than 3 sentences
5. The economic buyer is identified for every Tier 1 and Tier 2 prospect

A flagged gap is better than a confident error.

---

## Setup: Configuring This Skill for Your Company

Before first use, fill in the placeholder sections in:
- `references/icp.md` — your product description, ideal company profile, fit scoring rubric, and buyer title list
- `references/pitch-format.md` — add 3–5 good pitch hook examples from real outreach that worked, and 2–3 bad examples to avoid
- `references/connections/` — drop in each founder's LinkedIn CSV export (see README in that folder)

The skill works without VouchFor but is better with it. If `lookup_network` and `ask_my_network` aren't available in the session, skip Pass B and note "VouchFor not available — LinkedIn CSV only" in the output header.
