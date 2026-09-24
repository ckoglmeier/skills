---
name: investor-profile
description: >
  Build comprehensive profiles on investors, potential acquirers, and strategic buyers — for meeting
  prep, deal evaluation, or acquisition target research. Covers thesis, portfolio, deal mechanics,
  key people, relationship intel, and public signal. Use whenever the user mentions an investor,
  fund, VC firm, angel, potential acquirer, strategic buyer, or says: "pull a profile on [firm]",
  "prep me for [investor] meeting", "background on [fund]", "research [acquirer]", "buyer profile
  for [name]", "we're meeting with [firm]", or any variation of needing to understand a firm before
  a conversation — whether the firm is investing, acquiring, or partnering. Also trigger when the
  user pastes a link to a firm's Twitter/X, LinkedIn, website, or Crunchbase. When in doubt, load
  it — firm context before a meeting prevents positioning mistakes.
---

# Investor & Acquirer Profile Skill

Build decision-ready intelligence on investors, investing firms, and potential acquirers. This is
not a LinkedIn summary or a Crunchbase dump — it's the brief you'd want in hand before walking
into a meeting or deciding whether a relationship is worth pursuing.

---

## Mode Detection

Before starting, determine whether this is an **Investor Profile** (someone who might invest in
you) or an **Acquirer Profile** (someone who might acquire your company or product). The research
pattern is the same; the scoring and framing differ.

**Signals for Acquirer Mode:**
- The user mentions "buyer," "acquirer," "acquisition target," or "who might buy us"
- The firm is a consulting company, PE-backed services firm, or strategic buyer (not a VC fund)
- The context is a sell-side process, trial-to-bid, or exit planning
- The firm name appears in a buyer universe or acquisition readiness document

If ambiguous, ask. If the context is clearly sell-side (e.g., working from the acquisition
readiness brief), default to Acquirer Mode without asking.

---

## Required First Step: Company Context

Before generating any profiles, check whether company context has been configured. Look for
`~/.claude/skill-data/investor-profile/company-context.md`. (Never store it inside the skill
folder — plugin updates replace that folder.)

**If the file exists**, load it and use it for all scoring, meeting prep, and relationship mapping.

**If the file does not exist**, ask the user for the following and save it:

```markdown
# Company Context for Profiles

**Company name:** [Name]
**One-line description:** [What the company does]
**Stage:** [Pre-seed / Seed / Series A / Growth / Exit-ready / etc.]
**Current process:** [Fundraising / Acquisition / Partnership / General]
**Round size or target consideration:** [Target raise amount or acquisition price range]
**Primary sectors/domains:** [e.g., "AI, enterprise software, workforce transformation"]
**Buyer personas:** [Who buys the product — e.g., "VPs of AI Transformation, CHROs, PE operating partners"]
**Key differentiator:** [One sentence on what makes this defensible]
**Founder background:** [Relevant operating/domain experience]
**Warm intro network:** [Companies, firms, or people the founder can get intros through]
```

This context drives the Fit Score rubric, meeting prep angles, and relationship mapping. It can
be updated anytime — just ask to "update company context." If the user works across several
companies, keep one file per company (`company-context-<slug>.md`) and ask which applies.

---

## Required Second Step: Profile Clarification

Before launching research, confirm or infer:

1. **Who**: Full name of the firm and/or individual. If only a person is given, determine whether they operate solo (angel) or represent a fund/firm.
2. **Mode**: Investor Profile or Acquirer Profile (see Mode Detection above).
3. **Sub-mode**: Is this meeting prep (time-sensitive, focused on rapport and positioning) or firm evaluation (deeper, focused on thesis/acquisition alignment and deal mechanics)?
4. **User's angle**: Why is the user engaging? Possible contexts include fundraise pitch, acquisition/exit conversation, co-invest opportunity, LP consideration, portfolio company intro, partnership, or general relationship building.

If the user provides a URL (Twitter/X, LinkedIn, website), extract the entity identity from the page before asking questions. If the context is obvious from the conversation, skip the clarification and go straight to research.

---

## How to Run It

**Check the toolbox first.** Before researching, look at what's available in the session and
use the best source for each job:
- **Connection lookup:** the `team-connections` skill if installed; otherwise any network or
  CRM tools (VouchFor, HubSpot, Salesforce); otherwise skip and say so.
- **Internal context:** email, calendar, Slack, Drive, or CRM connectors often hold prior
  threads with this firm — a 30-second search there beats an hour of web research.
- **LinkedIn:** a LinkedIn MCP or the user's logged-in browser gets past the login wall for
  partner histories and recent posts. Read-only, a handful of profiles — never bulk.
- **Web search/fetch:** always.

**Run the threads in parallel.** If your environment supports subagents, give each research
thread and the connection lookup to its own agent at the same time. Research threads are
retrieval work — use a fast, inexpensive model for them and have each return sourced facts, not
conclusions. Keep scoring, meeting prep, and the Top 3 in the main conversation on the strongest
model, since that is where the judgment happens. Without subagents, run the threads
sequentially in the same order.

**Stamp the date.** Put today's date under the title. Everything in this profile decays; the
reader needs to know when it was true.

---

## Research Strategy

### For Firms (Institutional Investors)

Deploy 3 research threads **plus** a connection lookup (see below):

**Thread 1 — Firm Identity & Thesis**
- Official name, founding year, HQ location
- Fund structure: fund number, vintage, reported AUM/fund size
- Stated thesis: sectors, stages, geography, check sizes
- Revealed thesis: what does the actual portfolio say vs. what they claim? Look for patterns in recent investments (last 18 months) that may diverge from stated positioning
- LP base signals (if available): endowment-backed, family office, fund-of-fund, corporate
- Logo and brand presence: firm website URL, notable branding or positioning language

**Thread 2 — Partners & Decision-Makers**
For each relevant partner (focus on who the user would actually meet):
- Name, title, background (2-3 sentence career narrative, not a resume)
- Board seats and active portfolio companies
- Personal investment thesis or focus areas within the firm
- Public voice: what they write, tweet, speak about — recurring themes and strong positions
- Communication style signals: data-first or narrative-first, formal or casual, contrarian or consensus-seeking
- Social and professional links: Twitter/X handle, LinkedIn, personal site, podcast appearances

**Thread 3 — Deal Mechanics**
- Typical deal structure: check size range, lead vs. follow preference, pro-rata behavior
- **Check size inference (critical for new or private funds):** Direct check size data is often
  unavailable, especially for newer funds. When it's missing, infer from multiple signals:
  1. **Round data:** If they led a $20M round, their check was likely $8-15M. If they co-led, divide accordingly.
  2. **Fund math:** A $400M fund deploying across 20-30 companies implies $10-20M average initial checks. A $100M fund implies $2-5M. Always show the math.
  3. **Stage focus:** Seed funds write $1-5M, Series A funds write $5-15M, growth funds write $15-50M+.
  4. **Distinguish personal angel activity from fund activity.** An investor who wrote $50K angel checks for a decade may now run a fund writing $10M+ checks. These are different vehicles with different economics — never conflate them.
  Always flag whether check size data is directly sourced or inferred, and show the reasoning.
- Decision process: solo partner decision, IC vote, how many meetings to term sheet
- Stage preference and any sector-specific entry points
- Co-investor patterns: who do they frequently syndicate with?
- Reputation signals: how are they perceived by founders? Known for being helpful, hands-off, difficult?

### For Acquirers (Strategic Buyers, PE-backed Firms, Consulting Companies)

Deploy 3 research threads **plus** a connection lookup:

**Thread 1 — Firm Identity & Strategic Posture**
- Official name, founding year, HQ, employee count, ownership structure
- Core business: what they do, who they serve, revenue model
- Growth strategy: organic vs. acquisitive, recent strategic pivots
- Ownership: PE-backed (which firm, what vintage), public, founder-owned, family office
- Current leadership and any recent leadership changes (new CEO = platform-building mode)

**Thread 2 — Acquisition History & Pattern**
- Precedent acquisitions: what have they bought, at what scale, and what happened post-close?
- Integration pattern: do they absorb acquisitions into the brand, run them standalone, or convert them into products? (This is the most important question for predicting what happens to your company post-acquisition.)
- Deal size range: what's their typical acquisition scale? Have they bought at the target's expected price range?
- What capability gaps exist that the target company fills?
- Any public statements about M&A strategy or "build vs. buy" posture

**Thread 3 — Acquisition Fit Assessment**
- How does the target company's IP/product fit into the acquirer's existing service portfolio?
- Where does the target company fill a gap vs. compete with existing capabilities?
- What's the acquirer's capacity to absorb and operate the methodology independently?
- Consulting talent depth: how many practitioners could be trained on the methodology?
- Client overlap: does the acquirer already serve the target company's buyer personas?

**Connection Lookup — run in parallel with all threads**

Delegate to the `team-connections` skill (see How to Run It for fallbacks). Pass the firm name and
each key person's name you've identified so far. It searches the team's combined LinkedIn
exports plus any connected network tools and returns tiered results (Direct, Vouched, One hop,
Cold) with the best connector for each. Use these directly to populate the Relationship Map section of the output.
A Vouched or Direct path to a decision-maker changes meeting prep significantly — note it in the
Top 3 Things to Cover if a warm intro is available.

### For Individual Investors (Angels / Solo GPs)

Collapse the above into 2 threads:

**Thread 1 — Identity, Thesis & Public Voice**
- Who they are: current role, operating background, how they got into investing
- Investment thesis: sectors, stages, check sizes, any stated frameworks
- Portfolio: notable investments, recent activity (last 12 months)
- Public voice: what they write and say, recurring themes, strong opinions
- Communication style and personality signals

**Thread 2 — Deal Mechanics**
- Check size range and typical deal involvement (advisor, board observer, passive).
  **If this person also manages a fund**, clearly separate their personal angel check sizes from
  fund check sizes — these are different vehicles. Infer fund check sizes from round data and
  fund math (see firm section above) when direct data isn't published.
- How they source deals: inbound, network referrals, specific communities
- Decision speed and process: fast-mover or deliberate? Reference checks?
- Co-investor patterns: who do they invest alongside frequently?

**Connection Lookup — run in parallel with the 2 threads above**

Delegate to the `team-connections` skill (see How to Run It for fallbacks). Pass the investor's
name and their known employer or fund.
Use the results to populate the Relationship Map. If a Direct or Vouched path exists, surface it
in the Top 3 Things to Cover.

---

## Source Priority

Use sources in this order:

1. **The entity's own words**: blog posts, Twitter/X threads, podcast transcripts, conference talks, published memos. These reveal actual beliefs, not PR positioning.
2. **Portfolio/acquisition data**: Crunchbase, PitchBook, Tracxn, CB Insights, AngelList for investment history and patterns.
3. **Firm's official presence**: website, fund letters, team bios, press releases.
4. **Third-party coverage**: TechCrunch profiles, The Information, Term Sheet, StrictlyVC, industry newsletters.
5. **Network signals**: co-investor patterns, LinkedIn connections, community affiliations.

**Avoid:**
- Treating the firm's marketing copy as ground truth — always cross-reference stated thesis against actual portfolio/acquisitions
- Information older than 2 years without flagging its age
- Unverified fund size or AUM figures — note the source and confidence level
- Generic descriptions that could apply to any investor ("they invest in great founders building category-defining companies")

---

## Output Format

**Brevity is a design constraint, not a nice-to-have.** Target ~200 lines for the full document.
Every sentence must add information the user wouldn't already know. If a line could be cut without
losing decision-relevant insight, cut it. The gold standard is a document you can read in under
5 minutes and walk into the meeting with a clear mental model.

Save the output as a markdown file in an `investor-profiles/` folder in the current working
directory (or wherever the user keeps these — ask once, then reuse), using the investor or firm
name as the filename (e.g., `gokul-rajaram.md`, `benchmark-capital.md`,
`west-monroe-acquirer.md`).

**For Investor Mode**, the document title should be:
`# [Name] — Investor Profile & [Company] Meeting Prep`

**For Acquirer Mode**, the document title should be:
`# [Name] — Acquirer Profile & [Company] Evaluation`

Produce the following sections in this exact order:

### 1. Top 3 Things to Cover

This is the most important section. It goes at the very top of the document, right after the title.
Three numbered items — each a bold one-line headline followed by 2-3 sentences of context. These
are the three things that, if the user only has 60 seconds to scan before walking into the room,
would most change how they position. They should synthesize the firm's thesis/strategy, the company's
angle, and the specific meeting dynamic into actionable insight — not just restate facts from
later sections.

**For Investor Mode:** Weight business-model alignment and thesis fit over mission/values alignment.
**For Acquirer Mode:** Weight acquisition precedents, integration pattern, and capability gap fit over general strategic alignment.

### 2. Profile

The factual foundation. Structure differs by mode:

**Investor Mode — Header block:**
```
**Type:** [VC Fund | Growth Equity | Angel | Solo GP | Family Office | Other]
**Stage:** [Pre-seed | Seed | Series A | Series B+ | Growth | Multi-stage]
**Sectors:** [Primary sectors, comma-separated]
**Geography:** [Investment geography]
**Check Size:** [Range, e.g., "$500K–$5M" or "$25K–$100K"]
**Fund Size:** [If known, with source; "Not disclosed" if unavailable]
**Website:** [URL]
```

**Acquirer Mode — Header block:**
```
**Type:** [Consulting Firm | PE-Backed Services | Strategic Buyer | PE Fund (Direct) | Other]
**Employees:** [Count]
**Ownership:** [PE-backed (firm name) | Public | Founder-owned | Family Office]
**Revenue:** [If known, with source]
**Sectors Served:** [Primary sectors, comma-separated]
**Geography:** [Operating geography]
**Acquisition Range:** [Typical deal size, inferred from precedents if not stated]
**Website:** [URL]
```

**Thesis/Strategy & Positioning** (2-3 paragraphs): What do they actually invest in or acquire, and why? Lead with the revealed pattern (portfolio/acquisition evidence), then note gaps between stated and revealed positioning. Include distinctive frameworks, beliefs, or contrarian positions. End with a one-line assessment.

**Key People** — Only profile decision-makers the user would actually meet or who control the
investment/acquisition decision. For the primary contact, use the full format. For secondary people,
cap at 2-3 lines (name, title, focus area, one style signal). Do not profile people without
decision authority unless they have direct deal influence.

For the primary decision-maker:
```
### [Name] — [Title]
**Background:** [2-3 sentence career narrative]
**Focus:** [Their specific focus areas within the firm]
**Board Seats / Key Accounts:** [Current notable boards or client relationships]
**Public Voice:** [Key themes from their writing/speaking]
**Style:** [Communication style signals]
**Twitter/X:** [@handle] | **LinkedIn:** [URL]
```

**Portfolio & Recent Activity** (Investor Mode) or **Acquisition History** (Acquirer Mode) —
notable investments/acquisitions, especially in domains relevant to the user's company.

**Deal Mechanics** — check size or acquisition range, deal structure patterns, decision process,
reputation signals.

**Relationship Map** — co-investor network or partnership ecosystem, warm intro paths from
the connection lookup — surface the tier, connector name/role, and any prior touchpoints.

### 3. Fit Score

Score how well this entity aligns with the user's company and current process.

**Investor Mode — Investor Fit Score:**

| Dimension | Weight | 1 (Weak) | 3 (Moderate) | 5 (Strong) |
|---|---|---|---|---|
| **Thesis alignment** | ~17% | No overlap with company's sectors | Adjacent interest | Thesis explicitly covers the domain |
| **Stage & check fit** | ~17% | Wrong stage or check size | Stage right but check marginal | Stage, check, and lead/follow all match |
| **Portfolio distribution value** | ~17% | Portfolio doesn't sell into company's buyers | Some overlap | Portfolio is a customer pipeline |
| **Operator credibility** | ~17% | Pure financial, no relevant ops background | Some ops experience | Deep domain operating experience |
| **Decision velocity & access** | ~17% | Large IC, slow, junior first touch | Moderate — 2-3 meetings | Solo/fast decision, senior in the room |
| **Signal value** | ~17% | Unknown — name doesn't move the needle | Recognized in niche | Tier-1 brand, de-risks next fundraise |

**Acquirer Mode — Acquisition Fit Score:**

| Dimension | Weight | 1 (Weak) | 3 (Moderate) | 5 (Strong) |
|---|---|---|---|---|
| **Capability gap fit** | ~20% | Acquirer already has this capability in-house | Adjacent gap — could use it but has workarounds | Clear, named gap that the target directly fills |
| **Deal size alignment** | ~15% | Target's price range is far outside acquirer's precedent range | Acquirer has done deals at this scale but rarely | Sweet spot — multiple precedent acquisitions at this size |
| **Integration capacity** | ~20% | Acquirer has no practitioners who could absorb the methodology | Has consulting talent but would need significant training | Has deep bench of practitioners ready to operationalize |
| **Precedent acquisitions** | ~15% | No acquisition history or only acqui-hires | Has acquired companies but different types | Has done this exact playbook — acquired IP, converted to product |
| **Strategic urgency** | ~15% | No visible pressure to add this capability | General interest but no forcing function | Active strategic priority — new leadership, competitive pressure, client demand |
| **Cultural/brand alignment** | ~15% | Very different market positioning and values | Some overlap but different registers | Natural brand extension — would feel like a coherent addition |

**Present as:**

```
## [Investor/Acquisition] Fit Score

| Dimension | Score | Rationale |
|---|---|---|
| [Dimension] | X/5 | [One line] |
| ... | ... | ... |
| **Total** | **XX/30** | |

**Verdict:** [Strong fit / Worth pursuing / Marginal fit / Likely pass]
```

**Verdict thresholds:**
- **25–30: Strong fit** — prioritize
- **19–24: Worth pursuing** — worth the meeting to probe gaps
- **13–18: Marginal fit** — pursue only if strategic value compensates
- **≤12: Likely pass** — time is better spent elsewhere

If score is ≤12, skip sections 4–10 — deliver the profile and score with a one-line pass explanation.

### 4. Why This Meeting Matters

3-5 bullet points, **one sentence each**. Connect the firm's thesis/strategy to the specific company.

### 5. Questions to Ask

9-10 questions in three groups:

**On their thesis/strategy** (3) — reference their own public positions and frameworks.
**On deal mechanics** (3) — direct and practical.
**On the company specifically** (3) — solicit honest feedback, phrased so they're advising not evaluating.

Each question includes a one-sentence "Why" note.

### 6. Key Points to Hit

5-6 points. Bold one-line headline + 2-3 sentences max. Include quotable lines. Sequenced in natural conversation order.

### 7. What to Avoid

5-6 bullets. One sentence per bullet. Name the mistake and why it fails with this entity.

### 8. Suggested Meeting Flow

Simple table with time blocks. Assume 30 minutes unless specified.

### 9. Tensions to Navigate

3 unresolved tensions. Bold name + 2-3 sentences.

### 10. Open Questions to Probe

5-6 intelligence gaps to probe in conversation.

### 11. Sources

All sources with hyperlinks. `[Short description](URL)` format.

---

## Quality Checks

Before delivering the final profile, verify:

- [ ] Company context is loaded and used to calibrate scoring, relationship map, and meeting prep
- [ ] Correct mode detected (Investor vs. Acquirer) and scoring rubric applied
- [ ] Fit Score dimensions are scored from evidence, not assumed — each rationale references a specific fact
- [ ] If Fit Score is ≤12, sections 4–10 are omitted with a one-line pass explanation
- [ ] Top 3 Things to Cover are genuinely actionable — synthesize firm + company + meeting dynamic
- [ ] "Why This Meeting Matters" connects the firm's specific thesis/strategy to the specific company
- [ ] Questions to Ask reference the firm's own public positions, not generic questions
- [ ] Key Points to Hit include specific quotable language
- [ ] What to Avoid is tailored to this firm's known preferences
- [ ] Tensions to Navigate surface real strategic tradeoffs
- [ ] Stated thesis/strategy is cross-referenced against actual portfolio/acquisitions — gaps noted
- [ ] Check sizes, fund data, or acquisition ranges include source attribution
- [ ] Key people profiles include their own public statements
- [ ] Relationship map populated from the connection lookup (or marked unavailable) — includes tier, connector, and action
- [ ] No generic filler — every sentence adds information the user wouldn't already know
- [ ] Document is ~200 lines or fewer
- [ ] As-of date under the title
- [ ] Information age flagged for anything older than 18 months

---

## Edge Cases

**The user gives you a list of firms to profile.** Don't generate full profiles for all of them upfront. Instead:

1. Produce a summary table first:

```
| Firm | Type | Mode | Sectors | Fit Score | Priority |
|---|---|---|---|---|---|
| [Name] | VC / Consulting / PE-Backed / etc. | Investor / Acquirer | [Primary sectors] | XX/30 | High / Medium / Low |
```

Score each on the appropriate Fit Score rubric using available information (mark dimensions as "est." when inferred). Sort by Fit Score descending.

2. Offer to generate full profiles for the top N by fit score. Ask: "Want me to start with the top 3 full profiles, or adjust the priority list first?"

3. Don't generate all full profiles upfront — the summary table is the decision-making tool.

---

## Common Failure Modes

- **Regurgitating the firm's About page** — the skill exists because users need more than marketing copy
- **Generic thesis descriptions** — "they invest in ambitious founders" tells nobody anything
- **Missing the revealed vs. stated thesis gap** — many firms say one thing and invest/acquire differently
- **Flat people profiles** — a title and background isn't enough; what do they care about, how do they communicate
- **No actionable relationship intel** — the profile should answer "how do I get warm to this person"
- **Conflating personal angel activity with fund activity** — always separate the vehicles
- **Overconfidence in unverified data** — fund sizes, AUM, and deal terms are often speculative; note confidence
- **Verbosity** — if exceeding ~200 lines, cut aggressively
- **Skipping company context** — without it, scoring and meeting prep are generic
- **Wrong mode** — using Investor Fit Score for an acquirer or vice versa produces misleading scores
- **Missing acquisition precedents** — for Acquirer Mode, the most valuable data point is "have they done this exact thing before, and what happened?" Don't skip it.
