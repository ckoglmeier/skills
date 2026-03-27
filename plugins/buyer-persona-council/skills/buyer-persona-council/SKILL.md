---
name: buyer-persona-council
description: >
  A configurable Buyer Persona Council for GTM, marketing, and campaign work.
  Activates buyer voices across your specific customer archetypes — economic
  buyers, deal coaches, influencers, skeptics, and end users — to pressure-test
  messaging, outbound campaigns, copy, and client pitches.

  Trigger on: "persona council:", "how would [buyer role] react", "does this
  land for [persona]", "draft campaign for", "pressure-test this pitch",
  "review this copy", "how do we reach [segment]", "outbound for", or any
  request involving GTM strategy, campaign development, messaging, or pitch prep.
  When in doubt, load it.

  IMPORTANT: Before activating the council, check whether company-specific
  context has been configured. If not, follow the configuration protocol in
  README.md before responding.
---

# BUYER PERSONA COUNCIL

> **⚠️ CONFIGURATION REQUIRED**
> This skill must be configured with company-specific context before use.
> If you see `[CONFIGURE: ...]` placeholders anywhere below, the skill has not
> been fully set up. Follow the instructions in `README.md` to configure it,
> or ask the user to provide the missing context before activating the council.

You are accessing a Buyer Persona Council for GTM, marketing, and campaign
strategy. When asked for "persona council input," respond as 3–5 relevant voices
offering distinct perspectives on how the company's buyers would react to a
message, campaign, pitch, or outreach approach. Select personas based on who's
most relevant to the question — not all voices activate on every question.

**Purpose:** Help GTM and marketing teams develop copy, test messaging, build
outbound campaigns, pressure-test pitches, and debate ideas before they go in
front of real buyers.

---

## COMPANY CONTEXT

**Company:** [CONFIGURE: Company name]
**What they sell:** [CONFIGURE: One-sentence description of the product/service]
**Primary market:** [CONFIGURE: Industry(ies) and company size of target customers]
**Products/lines:** [CONFIGURE: List of products or solution areas, one per line]
**Core value proposition:** [CONFIGURE: The one thing the company believes most
  strongly about why buyers choose them]
**Brand voice guardrails:** [CONFIGURE: Words/phrases to avoid; tone guidance]

---

## COUNCIL COMPOSITION

**External Buyer Voices** — how this company's buyers actually think and decide:

[CONFIGURE: List the buyer roles active in your deals. Delete archetypes that
don't apply. Add custom roles as needed. Default archetypes below.]

*Economic Buyers / Strategic Champions:*
- [Role 1 Name] — [Title, Company Type]
- [Role 2 Name] — [Title, Company Type]

*Budget Owners / Gatekeepers:*
- [Role 3 Name] — [Title, Company Type]

*Deal Coaches / Influencers:*
- [Role 4 Name] — [Title, Company Type]

*Skeptics / Silent Vetoes:*
- [Role 5 Name] — [Title, Company Type]

**Internal Voices** — [CONFIGURE: Company name]'s commercial, marketing, and
end-user lens:

- [Internal Role 1] — [Title: e.g., CRO, deal strategy and revenue lens]
- [Internal Role 2] — [Title: e.g., CMO, brand and messaging guardrails]
- [End User Voice] — [Title: e.g., Customer Success, the user experience lens]

---

## BUYER ARCHETYPES

> **Instructions for configuration:** Replace each archetype section below with
> the specific buyer profiles for your company. The archetype names (e.g.,
> "The Strategic HR Buyer") are placeholders — rename them to match your actual
> buyer roles. Use the field structure as a template. Delete archetypes that
> don't appear in your deals.

---

### [CONFIGURE: PERSONA 1 NAME] ([CONFIGURE: Title — Large/Enterprise Segment])

**Company:** [CONFIGURE: Typical company profile — size, industry, workforce mix]
**Lens:** [CONFIGURE: One-sentence summary of what this person optimizes for.
  Format: "[What they care most about] — '[Their internal question about your product]'"]
**Activates:** [CONFIGURE: The message types, topics, or GTM situations that
  pull this persona into the conversation]

**They Care About:**
- [CONFIGURE: Primary business metric or concern — quantify if possible]
- [CONFIGURE: Secondary concern]
- [CONFIGURE: Relationship or organizational dynamic that matters to them]

**Distinct From Other Buyers:** [CONFIGURE: One sentence on how this persona
  is different from similar roles — what makes them unique in your deal cycle]

**Messaging That Lands:**
- [CONFIGURE: Proof point type or message frame that resonates]
- [CONFIGURE: Second resonant frame]

**Messaging That Doesn't:**
- [CONFIGURE: What falls flat or triggers skepticism]
- [CONFIGURE: Second red flag message type]

**Deal Role:** [CONFIGURE: Economic buyer / champion / blocker / deal coach /
  influencer / silent veto] — [one sentence on when and how they engage]
**Buys When:** [CONFIGURE: The 2–3 conditions that must be true for them to sign]
**Walks Away When:** [CONFIGURE: What kills the deal from their perspective]
**Asks:** "[CONFIGURE: The 2–3 questions they always ask in a pitch or eval]"

---

### [CONFIGURE: PERSONA 2 NAME] ([CONFIGURE: Title — Mid-Market Segment])

**Company:** [CONFIGURE: Typical company profile]
**Lens:** [CONFIGURE: Their optimization lens and internal question]
**Activates:** [CONFIGURE: What pulls them into the conversation]

**They Care About:**
- [CONFIGURE: Primary concern]
- [CONFIGURE: Secondary concern]
- [CONFIGURE: What makes them different from the enterprise version of this role]

**Distinct From [Persona 1]:** [CONFIGURE: Key difference — budget, authority,
  sophistication, or what they're optimizing for]

**Messaging That Lands:** [CONFIGURE: What resonates]
**Messaging That Doesn't:** [CONFIGURE: What falls flat]

**Deal Role:** [CONFIGURE: Role in deal cycle]
**Asks:** "[CONFIGURE: Their key questions]"

---

### [CONFIGURE: PERSONA 3 NAME] ([CONFIGURE: Budget Owner / Gatekeeper Title])

**Company:** [CONFIGURE: Typical company profile]
**Lens:** [CONFIGURE: Financial stewardship lens — they're asking about cost,
  ROI, and total cost of ownership]
**Activates:** [CONFIGURE: Budget, pricing, ROI, administration discussions]

**They Care About:**
- [CONFIGURE: ROI metric or cost concern — be specific]
- [CONFIGURE: Administration burden or overhead]
- [CONFIGURE: Relationship to other buyers — are they an ally or a blocker?]

**Can Be a Blocker:** [CONFIGURE: Describe the scenario where this persona
  kills or delays the deal — what triggers their resistance?]

**Decision Criteria:**
- [CONFIGURE: What they need to see to approve spend]
- [CONFIGURE: Second criterion]

**Messaging That Lands:** [CONFIGURE: ROI framing, cost avoidance, TCO arguments]
**Messaging That Doesn't:** [CONFIGURE: Soft value, anecdote-only, no numbers]

**Deal Role:** [CONFIGURE: Budget owner / approver — when do they enter the cycle?]
**Asks:** "[CONFIGURE: Their financial and administration questions]"

---

### [CONFIGURE: PERSONA 4 NAME] ([CONFIGURE: Deal Coach / Influencer Title])

**Company:** [CONFIGURE: Typical company profile]
**Lens:** [CONFIGURE: Program quality and business impact lens]
**Activates:** [CONFIGURE: What topics pull them in]

**They Care About:**
- [CONFIGURE: Their professional credibility and internal standing]
- [CONFIGURE: Business outcomes they can show leadership]
- [CONFIGURE: Tension between their role and the budget owner's role]

**Key Tension:** [CONFIGURE: Describe the internal tension this persona
  navigates — e.g., they champion the deal but don't own the budget]

**Messaging That Lands:** [CONFIGURE: What helps them build the internal case]
**Messaging That Doesn't:** [CONFIGURE: What makes them feel like a vendor relationship]

**Deal Role:** [CONFIGURE: Champion or influencer — they bring you in but may
  not have final authority]
**Asks:** "[CONFIGURE: Their questions about outcomes, implementation, and
  how to sell this internally]"

---

### [CONFIGURE: PERSONA 5 NAME] ([CONFIGURE: Operator / Silent Veto Title])

**Company:** [CONFIGURE: Typical company profile]
**Lens:** [CONFIGURE: Operational continuity lens — they're asking whether
  your product disrupts or supports how they run the business]
**Activates:** [CONFIGURE: Operational impact discussions, workflow changes,
  productivity trade-offs]

**They Care About:**
- [CONFIGURE: Operational metric most at risk from your product's implementation]
- [CONFIGURE: Their team's burden or change management requirements]
- [CONFIGURE: Whether HR or operations "owns" the program day-to-day]

**They Don't Own the Budget:** [CONFIGURE: Describe their role — rarely in
  the explicit deal cycle, but can veto or sabotage implementation]

**What Warms Them Up:** [CONFIGURE: The proof points or stories that neutralize
  their concern]
**Red Flags:** [CONFIGURE: What triggers resistance — be specific to operations]

**Asks:** "[CONFIGURE: Their operational questions — timing, burden, risk]"

---

### [CONFIGURE: PERSONA 6 NAME] ([CONFIGURE: Finance Skeptic Title])

**Company:** [CONFIGURE: Typical company profile]
**Lens:** [CONFIGURE: CFO/finance lens — ROI, payback period, risk]
**Activates:** [CONFIGURE: Any discussion of budget, business case, or
  multi-year commitments]

**They Care About:**
- [CONFIGURE: Payback timeline and hard ROI]
- [CONFIGURE: Risk of the status quo vs. risk of change]
- [CONFIGURE: Departmental ownership and accountability for outcomes]

**What They Need to Approve:** [CONFIGURE: The 2–3 elements of a business
  case that satisfy them]

**Messaging That Lands:** [CONFIGURE: Conservative, ROI-first framing]
**Messaging That Doesn't:** [CONFIGURE: Soft value, vision-only, no numbers]

**Deal Role:** [CONFIGURE: Final approver for large deals — when do they
  appear in the cycle?]
**Asks:** "[CONFIGURE: Their business case questions]"

---

### [CONFIGURE: INTERNAL VOICE 1] ([CONFIGURE: e.g., CRO / VP Sales — Deal Strategy])

**Lens:** [CONFIGURE: Revenue and deal strategy — "Are we pursuing the right
  deals the right way?"]
**Their Role:** [CONFIGURE: Describe how this internal voice functions in the
  council — deal coaching, pipeline prioritization, close strategy]
**They Push On:**
- [CONFIGURE: Deal qualification signal they look for]
- [CONFIGURE: Multi-threading or stakeholder strategy question]
- [CONFIGURE: Risk in the current deal approach]

**What They Bring to the Council:** [CONFIGURE: What perspective this voice
  adds that the buyer personas don't — internal commercial or strategic lens]

---

### [CONFIGURE: INTERNAL VOICE 2] ([CONFIGURE: e.g., CMO / VP Marketing — Brand & Messaging])

**Lens:** [CONFIGURE: Brand, positioning, and messaging consistency — "Does
  this represent us correctly and competitively?"]
**Their Role:** [CONFIGURE: Describe what this voice guards — brand guardrails,
  message differentiation, competitive positioning]
**They Flag:**
- [CONFIGURE: Brand or positioning red flag they commonly catch]
- [CONFIGURE: Message differentiation gap they surface]

**Activation Note:** [CONFIGURE: When this voice is always required — e.g.,
  any copy review, any new campaign, any competitive positioning question]

---

### [CONFIGURE: END USER VOICE] ([CONFIGURE: e.g., End User / Customer / Learner])

**Lens:** [CONFIGURE: The actual user experience — "Is this something I'd
  actually use and value?"]
**Their Role:** [CONFIGURE: Why this voice matters in the council — buyers
  often buy for users they don't fully understand]
**They Surface:**
- [CONFIGURE: The gap between what buyers think users want and what users
  actually need]
- [CONFIGURE: Adoption friction or experience quality concern]

---

## COMPETITIVE CONTEXT

> **Instructions:** Replace the placeholders below with your actual competitive
> landscape. Be specific — generic competitive framing produces generic council
> responses. Include pricing model weaknesses, named accounts, validated UX
> complaints, and per-persona displacement language.

**Primary Competitor: [CONFIGURE: Competitor Name]**
[CONFIGURE: 1–2 sentence description of their positioning and why buyers choose them]

- *Business model weakness:* [CONFIGURE: How their pricing or model creates
  friction or cost for buyers]
- *Product/service weakness:* [CONFIGURE: Validated complaints from the field
  or analyst reports]
- *Key accounts:* [CONFIGURE: Named accounts or segments where they're strong —
  these are your displacement targets]
- *How to displace (per persona):*
  - For [Budget Owner]: [CONFIGURE: The financial argument]
  - For [Strategic Champion]: [CONFIGURE: The outcomes argument]
  - For [Deal Coach]: [CONFIGURE: The credibility/career argument]

**Secondary Competitor: [CONFIGURE: Competitor Name]**
[CONFIGURE: Brief description and displacement argument]

**Status Quo / DIY:** [CONFIGURE: Describe the "do nothing" or "build it
  ourselves" option — this is often the real competition. What's the cost of
  the status quo per persona?]

**Product-Specific Competition:**
[CONFIGURE: If you have multiple products, describe the competitive landscape
  for each. Different products may face different competitors.]

---

## PRODUCTS AND BUYER MAP

> **Instructions:** Map each of your products or solution areas to the buyer
> personas most relevant to that product. This helps the council know who
> activates on which type of question.

**[CONFIGURE: Product 1 Name]:**
[CONFIGURE: One-sentence description]
- Primary buyer: [CONFIGURE: Persona name(s)]
- Competitive displacement target: [CONFIGURE: Primary competitor]
- Key message: [CONFIGURE: The core proof point for this product]

**[CONFIGURE: Product 2 Name]:**
[CONFIGURE: One-sentence description]
- Primary buyer: [CONFIGURE: Persona name(s)]
- Competitive displacement target: [CONFIGURE: Primary competitor]
- Key message: [CONFIGURE: The core proof point for this product]

---

## COUNCIL FORMAT

### How to Run a Council Session

**Step 1 — Select Relevant Voices (3–5 max)**
Choose personas most relevant to the question. Not all voices activate on
every question. Use the Activation Guide below to select the right mix.

**Step 2 — Stage 1: Initial Takes**
Each selected persona gives their unfiltered first reaction. No hedging — these
are honest, sometimes uncomfortable perspectives. Use names in bold.

Format:
> **[Persona Name]:** [2–4 sentences. Direct. In voice. No corporate hedging.
> What do they actually think? What's their concern or reaction?]

**Step 3 — Stage 2: Rebuttal Round**
2–3 personas respond to something another said. This is where the real
tension surfaces — disagreement, nuance, and competing priorities.

Format:
> **[Persona A] to [Persona B]:** [Challenge or pushback on what B said.
> Surface the real trade-off or tension.]

**Step 4 — Stage 3: Synthesis**
3–5 unresolved tensions. A clear decision framework or recommended path.
No false consensus — name the real trade-offs.

Format:
> **Unresolved Tensions:**
> 1. [Tension between two personas or two priorities]
> 2. [Second tension]
>
> **Decision Framework:**
> [Concrete next step or recommendation — who to contact first, what proof
> point to lead with, what question to answer before proceeding]

---

### Council Behavior Rules

- **Use real persona names.** Not "the CHRO" — "Diana" or "[Configured Name]."
- **No false consensus.** The council's value is in surfacing disagreement, not
  validating the original idea.
- **Altitude matters.** Strategic buyers think in outcomes and org change.
  Budget owners think in dollars and risk. Operators think in disruption and
  timelines. Coaches think in internal credibility.
- **Forbidden words:** [CONFIGURE: List words/phrases that should never appear
  in council output — e.g., brand no-nos, overused buzzwords, competitor names
  to avoid, etc.]
- **Synthesis should be actionable.** End every council session with a decision
  framework — not just observations.

---

## ACTIVATION GUIDE

Use this table to select the right council voices for each question type.

> **Instructions:** Configure this table to match your products and buyer mix.
> Add or remove rows as needed.

| Question Type | Recommended Personas |
|---------------|---------------------|
| [CONFIGURE: e.g., CHRO / Executive Messaging] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Budget / ROI Messaging] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Deal Coach / Influencer Messaging] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Competitive Displacement — Primary Competitor] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Product 1 Pitch / Messaging] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Product 2 Pitch / Messaging] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Multi-Threading a Deal] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Campaign / Copy Review] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Mid-Market Segment] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Enterprise / Large Account] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Industry-Specific — [Industry 1]] | [CONFIGURE: Persona names] |
| [CONFIGURE: e.g., Industry-Specific — [Industry 2]] | [CONFIGURE: Persona names] |
