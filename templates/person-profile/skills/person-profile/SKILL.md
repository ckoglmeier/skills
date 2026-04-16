---
name: person-profile
description: >
  Build comprehensive profiles on individuals for meeting prep, hiring evaluation, partnership
  assessment, or key-person due diligence. Covers career narrative, what they care about, public
  voice, network and influence, and actionable meeting prep. Use this skill whenever the user
  mentions a person and wants background — "prep me for a meeting with X", "background on X",
  "who is X", "person profile for X", "research [person]", "tell me about [person]", "I'm
  meeting with [person]", or any variation of needing to understand someone before a conversation
  or decision. Also trigger when the user pastes a LinkedIn or Twitter/X URL for an individual.
  When in doubt, load it — having person context before a meeting prevents positioning mistakes
  and surfaces non-obvious connection points.
---

# Person Profile Skill

Build decision-ready intelligence on an individual. This is not a LinkedIn summary or a resume
reformat — it's the brief you'd want in hand before walking into a meeting or deciding whether
a relationship is worth pursuing.

---

## Required First Step: Context Clarification

Before launching research, confirm or infer:

1. **Who**: Full name, current role, and organization. If the user provides a URL (LinkedIn,
   Twitter/X, personal site), extract the identity from the page before asking questions.
2. **Mode**: Is this meeting prep (time-sensitive, focused on rapport and positioning), hiring
   evaluation, partnership assessment, or general due diligence?
3. **User's angle**: Why is the user engaging this person? Possible contexts include investor
   pitch, co-invest conversation, candidate evaluation, partnership, sales meeting, board
   relationship, or general relationship building.
4. **What matters most**: Any specific dimensions the user cares about (e.g., "I need to
   understand their investment thesis" or "how do they make hiring decisions" or "what's their
   communication style").

If the context is obvious from the conversation, skip the clarification and go straight to
research. Don't force the user to answer questions when the intent is clear.

---

## Research Strategy

Deploy 2 research threads:

**Thread 1 — Professional Background & Network**

- Current role: what they actually do day-to-day, not just their title. How long in role, scope
  of responsibility, what they're building or managing.
- Career trajectory: the narrative of how they got here. Major transitions and what each move
  reveals about their priorities and decision-making patterns. Don't list jobs — tell the story.
- Key accomplishments: what they're actually known for in their field. Specific outcomes, not
  vague claims. Quantify where possible.
- Education and formative experiences: only include if relevant to the meeting context or if it
  reveals something non-obvious about their worldview.
- Network and influence: board seats, advisory roles, investment activity (if any), professional
  affiliations, and key relationships visible from public sources. Focus on connections relevant
  to the user's context.
- Digital presence: Twitter/X handle, LinkedIn URL, personal site, podcast appearances. Note
  activity level — are they a regular poster or a lurker?

**Thread 2 — Public Voice & Style**

- What they write and say publicly: recurring themes, strong positions, pet topics, contrarian
  views. Pull specific quotes or positions — not just "they care about AI."
- Communication style: how they talk and present. Direct or diplomatic? Data-first or
  narrative-first? Optimist or skeptic? Formal or casual? Look for patterns in their writing,
  speaking, and public interactions.
- Recent activity (last 6-12 months): what have they been focused on, writing about, building,
  or speaking about? Recent moves signal current priorities better than bios.
- Personality signals: what lights them up? What do they publicly push back on? Any known strong
  preferences or dislikes?

---

## Source Priority

Use sources in this order:

1. **The person's own words**: LinkedIn posts, published articles, podcast interviews, conference
   talks, Twitter/X threads, Substack, personal blog. These reveal actual beliefs and priorities
   better than anything written about them.
2. **Professional records**: company bio, board listings, SEC filings (if officer of a public
   company), Crunchbase, PitchBook.
3. **Organizational context**: press releases, company announcements, alumni networks.
4. **Third-party coverage**: news articles, industry profiles, conference speaker bios, podcast
   guest intros.

**Avoid:**
- Personal social media unrelated to professional work
- Unverified claims or gossip
- Information older than 2 years without flagging its age
- Overweighting job titles vs. actual demonstrated work
- Generic descriptions that could apply to anyone ("passionate leader who cares about innovation")

---

## Optional Integrations

The skill works standalone with web search. These integrations enhance it when available:

- **VouchFor (`lookup_network`, `ask_my_network`):** Searches the user's professional network
  for direct connections to this person, their company, or their domain. Surfaces warm intro
  paths and back-channel intel sources. If available, use automatically during Thread 1 research.
  If unavailable, skip gracefully — the profile still works from web research.

---

## Output Format

**Brevity is a design constraint.** Target 80-150 lines for the full document. Every sentence
must add information the user wouldn't already know. The gold standard is a document you can
read in under 3 minutes and walk into the meeting with a clear mental model of who this person
is, what they care about, and how to connect with them.

Save the output as a markdown file using the person's name as the filename (e.g.,
`jane-smith.md`, `gokul-rajaram.md`).

The document title should be: `# [Name] — Person Profile`

If the mode is meeting prep, append the meeting context:
`# [Name] — Person Profile & Meeting Prep`

Produce the following sections:

### 1. One-Line Summary

Who is this person in one sentence? Role, organization, and what they're known for. Not a title
— a characterization. Good: "Product leader turned prolific AI angel investor, known for the
'builder + seller' framework and contrarian bets on category-defining founders." Bad: "Managing
Partner at Marathon Management Partners."

### 2. Career Narrative

2-3 paragraphs telling the story of their career. Not a resume — a narrative that explains how
they got where they are, what drives them, and what the arc reveals about their priorities. Look
for the throughline: what connects their moves?

### 3. What They Care About

Based on their own public statements — not inferred from their job title. Key topics, positions,
and priorities. Include specific quotes or positions where possible. This section answers: "If I
only have 5 minutes, what should I know about how this person thinks?"

### 4. Network & Influence

Key affiliations, board seats, investment activity, and relationships that matter for the user's
context. Don't list every board seat — highlight the ones that create connection points or reveal
priorities. Include co-investor patterns if relevant.

### 5. Recent Activity

What they've been doing in the last 6-12 months. New roles, investments, published writing,
speaking appearances, company launches, strategic moves. Recent activity signals current
priorities better than bios.

### 6. Connection Points

Shared experiences, interests, contacts, or contexts that create natural rapport between the
user and this person. Be specific — "you both invested in edtech" is weak; "you both built
enterprise sales motions selling to CHROs" is strong.

If VouchFor data is available, include network connections here under a "Network Connections"
sub-heading.

### 7. Meeting Prep Brief (if mode is meeting prep)

Only include this section if the user's context is meeting prep. Structure it as:

**3 Things to Know** — The three things that, if missed, change how the meeting goes. Bold
one-line headline + 2-3 sentences of context each. These should synthesize the person's
priorities, the user's angle, and the specific meeting dynamic.

**Conversation Starters** — 3 concrete openers with a one-line note on why each will land with
this specific person. Not generic small talk — starters grounded in what they've recently said,
built, or cared about publicly.

**Style Notes** — How to be heard by this person. Direct or warm up first? Lead with data or
narrative? Ask questions or present a thesis? Short section, 3-5 lines.

**Watch-Fors** — What to avoid. Known sensitivities, strong dislikes, topics that create
friction, past conflicts. 3-5 bullets, one sentence each.

### 8. Open Questions

What we couldn't verify or find. Intelligence gaps that the user might want to probe in
conversation or through other channels. 3-5 specific items.

### 9. Sources

List all sources used with hyperlinks. `[Short description](URL)` format.

---

## Quality Checks

Before delivering the final profile, verify:

- [ ] One-line summary characterizes the person, not just their title
- [ ] Career narrative tells a story with a throughline, not a chronological resume
- [ ] "What They Care About" draws from their own public statements, not inferences from job titles
- [ ] Connection points are specific to the user's context, not generic
- [ ] Meeting prep brief (if included) has actionable conversation starters grounded in the person's recent public positions
- [ ] Watch-fors are specific to this person, not generic meeting advice
- [ ] Information age is flagged for anything older than 18 months
- [ ] No generic filler — every sentence adds information the user wouldn't already know
- [ ] Document is 80-150 lines — if longer, tighten career narrative, trim secondary affiliations, shorten watch-fors

---

## Common Failure Modes

- **Reducing profiles to a chronological resume** — a list of jobs is not a profile; the narrative arc is what matters
- **Ignoring their own public statements** — what they write and say is higher-signal than what others say about them
- **Relying on stale information without noting its age** — a 2019 blog post may not reflect 2026 priorities
- **Overweighting job titles vs. actual demonstrated work** — "CEO of X" tells the user nothing; "built X from 0 to $100M ARR by selling to CHROs" is useful
- **Generic conversation starters** — "ask about their career journey" is useless; "you both built enterprise GTM motions selling workforce transformation to F500 CHROs — open with that shared context" is actionable
- **Skipping connection points** — the profile should answer "how do I connect with this person" concretely
- **Padding with organizational boilerplate** — the user doesn't need a paragraph about the company's mission statement; they need to understand the person
