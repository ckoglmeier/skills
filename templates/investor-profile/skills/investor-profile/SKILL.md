---
name: investor-profile
description: >
  Build comprehensive investor profiles — firms, funds, angels, and their partners — for meeting
  prep or evaluation. Covers thesis, portfolio, deal mechanics, partner backgrounds, relationship
  intel, and public signal. Use this skill whenever the user mentions an investor, fund, VC firm,
  angel, or says things like: "pull a profile on [firm]", "who is [investor]", "prep me for
  [investor] meeting", "background on [fund]", "what does [firm] invest in", "investor profile
  for [name]", "we're meeting with [firm]", "look up [investor]", or any variation of needing to
  understand an investing entity before a conversation or decision. Also trigger when the user
  pastes a link to an investor's Twitter/X, LinkedIn, website, or Crunchbase. When in doubt,
  load it — having investor context before a meeting prevents positioning mistakes and surfaces
  non-obvious connection points.
---

# Investor Profile Skill

Build decision-ready intelligence on investors and investing firms. This is not a LinkedIn summary
or a Crunchbase dump — it's the brief you'd want in hand before walking into a meeting or deciding
whether a relationship is worth pursuing.

---

## Required First Step: Company Context

Before generating any profiles, check whether company context has been configured. Look for a file
at `company-context.md` in the `investor-profile-outputs/` folder alongside this skill.

**If the file exists**, load it and use it for all scoring, meeting prep, and relationship mapping.

**If the file does not exist**, ask the user for the following and save it:

```markdown
# Company Context for Investor Profiles

**Company name:** [Name]
**One-line description:** [What the company does]
**Stage:** [Pre-seed / Seed / Series A / etc.]
**Round size:** [Target raise amount]
**Target check size from investors:** [e.g., "$500K–$2M"]
**Primary sectors/domains:** [e.g., "AI, enterprise software, workforce transformation"]
**Buyer personas:** [Who buys the product — e.g., "VPs of AI Transformation, CHROs, PE operating partners"]
**Key differentiator:** [One sentence on what makes this defensible]
**Founder background:** [Relevant operating/domain experience]
**Warm intro network:** [Companies, firms, or people the founder can get intros through — e.g., "Guild Education investor base, YC alumni network"]
```

This context drives the Fit Score rubric, meeting prep angles, and relationship mapping. It can
be updated anytime — just ask to "update company context."

---

## Optional Integrations

The skill works standalone with web search. These integrations enhance it when available:

- **VouchFor (`lookup_network`, `ask_my_network`):** Searches the user's professional network for
  direct connections to the investor, their firm, or their portfolio companies. Surfaces warm intro
  paths that web research alone can't find. If VouchFor tools are available, use them automatically
  during Thread 3 (Deal Mechanics & Relationship Intel) for every profile. If the tools aren't
  available, skip gracefully — the Relationship Map still works from web research and company context.

---

## Required Second Step: Profile Clarification

Before launching research, confirm or infer:

1. **Who**: Full name of the firm and/or individual. If only a person is given, determine whether they operate solo (angel) or represent a fund.
2. **Mode**: Is this meeting prep (time-sensitive, focused on rapport and positioning) or firm evaluation (deeper, focused on thesis alignment and deal mechanics)?
3. **User's angle**: Why is the user engaging? Possible contexts include co-invest opportunity, LP consideration, fundraise pitch, portfolio company intro, partnership, or general relationship building.

If the user provides a URL (Twitter/X, LinkedIn, website), extract the entity identity from the page before asking questions. If the context is obvious from the conversation, skip the clarification and go straight to research.

---

## Research Strategy

### For Firms (Institutional Investors)

Deploy 3 research threads:

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

**Thread 3 — Deal Mechanics & Relationship Intel**
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
- Portfolio overlap with the user's network (companies, people, sectors — reference company context)
- Warm intro paths: shared connections, shared portfolio companies, shared LPs or advisors
- **VouchFor network lookup (if available):** Use `lookup_network` to check if the user knows anyone
  at the investor's firm (search by firm name). Also use `ask_my_network` to find people in the
  user's network who have experience with this investor, firm, or relevant domain (e.g., "who has
  experience with [firm name]?" or "who knows about seed-stage fundraising in [sector]?"). Surface
  any direct connections, mutual contacts, or domain experts who could facilitate a warm intro or
  provide back-channel intel. Include VouchFor results in the Relationship Map section under a
  "**Network Connections**" sub-heading.
- Reputation signals: how are they perceived by founders? Known for being helpful, hands-off, difficult?

### For Individual Investors (Angels / Solo GPs)

Collapse the above into 2 threads:

**Thread 1 — Identity, Thesis & Public Voice**
- Who they are: current role, operating background, how they got into investing
- Investment thesis: sectors, stages, check sizes, any stated frameworks
- Portfolio: notable investments, recent activity (last 12 months)
- Public voice: what they write and say, recurring themes, strong opinions
- Communication style and personality signals

**Thread 2 — Deal Mechanics & Relationship Intel**
- Check size range and typical deal involvement (advisor, board observer, passive).
  **If this person also manages a fund**, clearly separate their personal angel check sizes from
  fund check sizes — these are different vehicles. Infer fund check sizes from round data and
  fund math (see firm section above) when direct data isn't published.
- How they source deals: inbound, network referrals, specific communities
- Decision speed and process: fast-mover or deliberate? Reference checks?
- Co-investor patterns: who do they invest alongside frequently?
- Network overlap with the user: shared connections, shared investments, shared communities
- **VouchFor network lookup (if available):** Same as firm research — use `lookup_network` (by
  person name and/or company) and `ask_my_network` (by expertise/domain) to find direct connections
  and warm intro paths. Include results in the Relationship Map.
- Warm intro paths

---

## Source Priority

Use sources in this order:

1. **The investor's own words**: blog posts, Twitter/X threads, podcast transcripts, conference talks, published memos. These reveal actual beliefs, not PR positioning.
2. **Portfolio data**: Crunchbase, PitchBook, Tracxn, CB Insights, AngelList for investment history and patterns.
3. **Firm's official presence**: website, fund letters, team bios, press releases.
4. **Third-party coverage**: TechCrunch profiles, The Information, Term Sheet, StrictlyVC, industry newsletters.
5. **Network signals**: co-investor patterns, LinkedIn connections, community affiliations.

**Avoid:**
- Treating the firm's marketing copy as ground truth — always cross-reference stated thesis against actual portfolio
- Information older than 2 years without flagging its age
- Unverified fund size or AUM figures — note the source and confidence level
- Generic descriptions that could apply to any investor ("they invest in great founders building category-defining companies")

---

## Output Format

**Brevity is a design constraint, not a nice-to-have.** Target ~200 lines for the full document.
Every sentence must add information the user wouldn't already know. If a line could be cut without
losing decision-relevant insight, cut it. The gold standard is a document you can read in under
5 minutes and walk into the meeting with a clear mental model.

Save the output as a markdown file to the `investor-profile-outputs/` folder alongside this skill,
using the investor or firm name as the filename (e.g., `gokul-rajaram.md`, `benchmark-capital.md`).

The document title should be: `# [Name] — Investor Profile & [Company] Meeting Prep`
(where [Company] is the company name from company context)

Produce the following sections in this exact order:

### 1. Top 3 Things to Cover

This is the most important section. It goes at the very top of the document, right after the title.
Three numbered items — each a bold one-line headline followed by 2-3 sentences of context. These
are the three things that, if the user only has 60 seconds to scan before walking into the room,
would most change how they position. They should synthesize the investor's thesis, the company's
angle, and the specific meeting dynamic into actionable insight — not just restate facts from
later sections.

Think of this as: what are the three things that, if missed, the meeting goes sideways?

**Weight business-model alignment and thesis fit over mission/values alignment.** The user already
knows their own mission. What they need is: how does this investor's investment logic map to the
company's business model, market position, and growth mechanics?

### 2. Investor Profile

The factual foundation. Includes:

**Header block:**
```
**Type:** [VC Fund | Growth Equity | Angel | Solo GP | Family Office | Other]
**Stage:** [Pre-seed | Seed | Series A | Series B+ | Growth | Multi-stage]
**Sectors:** [Primary sectors, comma-separated]
**Geography:** [Investment geography]
**Check Size:** [Range, e.g., "$500K–$5M" or "$25K–$100K"]
**Fund Size:** [If known, with source; "Not disclosed" if unavailable]
**Website:** [URL]
```

**Thesis & Positioning** (2-3 paragraphs): What do they actually invest in and why? Lead with the
revealed thesis (portfolio evidence), then note gaps between stated and revealed positioning.
Include distinctive frameworks, beliefs, or contrarian positions. End with a one-line
"Revealed vs. Stated Gap" assessment.

**Key People** — Only profile decision-makers the user would actually meet or who control the
investment decision. For the primary contact, use the full format below. For secondary partners,
cap at 2-3 lines (name, title, focus area, one style signal). Do not profile associates,
principals, or operating partners unless they have direct deal authority.

For the primary decision-maker:
```
### [Name] — [Title]
**Background:** [2-3 sentence career narrative]
**Focus:** [Their specific focus areas within the firm]
**Board Seats:** [Current notable boards]
**Public Voice:** [Key themes from their writing/speaking]
**Style:** [Communication style signals]
**Twitter/X:** [@handle] | **LinkedIn:** [URL]
```

**Portfolio & Recent Activity** — notable investments, especially in domains relevant to the user's
company (reference company context for relevant sectors). Recent activity (last 12-18 months),
exits or markdowns.

**Deal Mechanics** — check size, lead vs. follow, decision process, pro-rata behavior, founder
reputation. Use prose, not just bullet points — the user needs to understand *how* they operate,
not just the parameters.

**Relationship Map** — co-investor network, portfolio overlap with the user's network (reference
company context for warm intro sources), warm intro paths (specific and actionable), any prior
touchpoints.

### 3. Investor Fit Score

Score how well this investor aligns with the user's company and fundraising needs. This is the
inverse of deal grading — instead of "does this deal fit my thesis," it's "does this investor
fit my company's needs." Score each dimension 1–5 using company context to calibrate the anchors.

**Scoring dimensions:**

| Dimension | Weight | 1 (Weak) | 3 (Moderate) | 5 (Strong) |
|---|---|---|---|---|
| **Thesis alignment** | ~17% | Investor's thesis has no overlap with the company's sectors or domain | Adjacent interest — invests in related sectors but not the core intersection | Thesis explicitly covers the company's domain and market |
| **Stage & check fit** | ~17% | Wrong stage or check size doesn't match the round | Stage is right but check size is marginal, or vice versa | Stage, check size, and lead/follow preference all match the current raise |
| **Portfolio distribution value** | ~17% | Portfolio companies don't sell into the company's buyer personas | Some portfolio overlap with the company's ICP but not concentrated | Portfolio is a customer pipeline — companies selling into exactly the same buyers |
| **Operator credibility** | ~17% | Pure financial investor with no relevant operating background | Some operating experience but not in the company's domain | Deep operating experience in the company's domain — can advise on product, GTM, or pricing |
| **Decision velocity & access** | ~17% | Large IC, slow process, or junior partner as first touch | Moderate process — 2-3 meetings, small IC | Solo decision or two-person partnership; fast-moving; senior decision-maker in the room |
| **Signal value** | ~17% | Unknown fund/angel — name on cap table doesn't move the needle with next-round investors, buyers, or recruits | Recognized in their niche but not broadly — some downstream credibility | Tier-1 brand that de-risks the next fundraise, opens buyer doors, and attracts senior talent |

**Present as:**

```
## Investor Fit Score

| Dimension | Score | Rationale |
|---|---|---|
| Thesis alignment | X/5 | [One line] |
| Stage & check fit | X/5 | [One line] |
| Portfolio distribution value | X/5 | [One line] |
| Operator credibility | X/5 | [One line] |
| Decision velocity & access | X/5 | [One line] |
| Signal value | X/5 | [One line] |
| **Total** | **XX/30** | |

**Verdict:** [Strong fit / Worth pursuing / Marginal fit / Likely pass]
```

**Verdict thresholds:**
- **25–30: Strong fit** — this investor checks every box; prioritize the meeting
- **19–24: Worth pursuing** — real alignment on most dimensions; worth the meeting to probe gaps
- **13–18: Marginal fit** — one or two dimensions align but structural gaps exist; pursue only if strategic value (intros, credibility) compensates
- **≤12: Likely pass** — poor fit on fundamentals; time is better spent elsewhere

Place this section immediately after the Investor Profile and before the meeting prep sections.
If the score is ≤12, skip sections 4–10 (meeting prep) — just deliver the profile and score with
a one-line note on why it's not worth the meeting time.

### 4. Why This Meeting Matters

3-5 bullet points, **one sentence each**. Connect the investor's thesis to the specific company.
Map their frameworks, beliefs, and portfolio patterns to the company's product, market, and
strategy. This is the "so what" — why is there a fit here, and what makes it non-obvious?

### 5. Questions to Ask

9-10 questions organized in three groups:

**On their thesis** (3 questions) — establish shared language, surface the gap the company fills,
let the investor articulate the problem before you present the solution. These should reference
the investor's own public positions and frameworks.

**On fund mechanics** (3 questions) — sector focus, decision structure, portfolio strategy. Direct
and practical — these determine whether this is an investment conversation or a strategic
relationship conversation.

**On the company specifically** (3 questions) — ask *after* showing the product. Solicit honest
product feedback, roadmap advice using their frameworks, and direct asks for distribution or intros.
These should be phrased so the investor is giving advice, not evaluating a pitch.

Each question should include a **one-sentence** "Why" note — what the answer reveals. Not a paragraph.

### 6. Key Points to Hit

5-6 points. Each is a **bold one-line headline** followed by **2-3 sentences max** — punchy, not
scripted. Include one quotable line the user can actually say in the room. Sequenced in natural
conversation order. Do NOT write full paragraphs — if it reads like a script, it's too long.

### 7. What to Avoid

5-6 bullets. **One sentence per bullet.** Name the mistake and why it fails with this person.
No paragraphs — these are tripwires, not essays.

### 8. Suggested Meeting Flow

A simple table with time blocks and focus areas. Assume a 30-minute meeting unless the user
specifies otherwise. The flow should reflect the key points and questions above in a natural
conversational arc — don't just restate the sections in time blocks.

### 9. Tensions to Navigate

3 unresolved tensions. Each: **bold tension name**, then 2-3 sentences covering both sides and how
it might surface. Keep tight — these are flags, not analysis.

### 10. Open Questions to Probe

5-6 specific questions that couldn't be answered by research alone. These are things to probe in
conversation — fund mechanics, sector appetite, decision structure, or relationship dynamics that
only the investor can clarify. Different from "Questions to Ask" — these are intelligence gaps,
not conversation tools.

### 11. Sources

List all sources used with hyperlinks. Keep it clean — `[Short description](URL)` format.

---

## Quality Checks

Before delivering the final profile, verify:

- [ ] Company context is loaded and used to calibrate the Fit Score, relationship map, and meeting prep
- [ ] Investor Fit Score dimensions are scored from evidence in the profile, not assumed — each rationale references a specific fact
- [ ] If Investor Fit Score is ≤12, sections 4–10 are omitted and a one-line pass explanation is provided
- [ ] Top 3 Things to Cover are genuinely actionable — they synthesize investor + company + meeting dynamic, not just restate profile facts
- [ ] "Why This Meeting Matters" connects the investor's specific thesis/frameworks to the specific company, not generic fit language
- [ ] Questions to Ask reference the investor's own public positions, frameworks, or portfolio — not generic VC questions
- [ ] Key Points to Hit include specific language the user can use (quotable lines, not just themes)
- [ ] What to Avoid is tailored to this investor's known preferences and filters — not generic meeting advice
- [ ] Tensions to Navigate surface real strategic tradeoffs to decide before or during the meeting
- [ ] Stated thesis is cross-referenced against actual portfolio — any gaps are noted
- [ ] Check sizes and fund data include source attribution
- [ ] Partner profiles include their own public statements, not just third-party descriptions
- [ ] Relationship map includes at least one actionable warm intro path (or explicitly notes none found)
- [ ] No generic filler — every sentence adds information the user wouldn't already know
- [ ] Document is ~200 lines or fewer — if longer, cut non-decision-makers from Key People, tighten Key Points, shorten What to Avoid bullets
- [ ] Information age is flagged for anything older than 18 months

---

## Common Failure Modes

- **Regurgitating the firm's About page** — the skill exists precisely because users need more than marketing copy
- **Generic thesis descriptions** — "they invest in ambitious founders" tells nobody anything; specifics about sectors, stages, and contrarian positions matter
- **Missing the revealed vs. stated thesis gap** — many firms say one thing and invest differently; surfacing this is high-value
- **Flat partner profiles** — a title and background isn't enough; what do they *care about*, how do they *communicate*, what *topics* light them up
- **No actionable relationship intel** — the profile should answer "how do I get warm to this person" concretely
- **Conflating personal angel activity with fund activity** — an investor who wrote $50K angel checks for years may now manage a $400M fund writing $10M+ checks. If you report the angel check size as the fund's check size, the user walks into the meeting with the wrong mental model of the investor's capacity and decision-making. Always separate the vehicles.
- **Overconfidence in unverified data** — fund sizes, AUM, and deal terms are often speculative; always note confidence level
- **Verbosity** — if the document exceeds ~200 lines, something is too long. Partner profiles for non-decision-makers, paragraph-length "What to Avoid" bullets, and scripted Key Points are the usual culprits. Cut aggressively.
- **Skipping company context** — without knowing the user's company, stage, buyers, and domain, the Fit Score and meeting prep are generic and low-value. Always load or create company context first.
