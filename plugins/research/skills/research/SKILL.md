---
name: research
description: >
  Run deep, multi-agent research on any strategic question. Handles the full workflow:
  internal recon (Slack + internal docs), parallel web research agents, progress monitoring,
  and synthesis into a polished prose document.

  Trigger automatically for requests like: "research X", "dig into Y", "do a competitive
  analysis of Z", "help me size the market for", "should we build/buy/partner for", "pull
  together everything we know about", "I need a landscape on", "what do we know about
  [company]", "find companies similar to X", "who else has solved this", "who should I be
  talking to in this space", "find analogs to our model", "build a list of companies worth
  getting introduced to", or any request to investigate a topic, market, or strategic
  question. When in doubt, load it — structured multi-agent research almost always beats
  ad hoc searching.
---

# Research — Multi-Agent Research Orchestrator

Deep research for the most common strategic questions: market sizing, competitive analysis,
build/buy/partner decisions, company deep dives, industry trend research, and analog mapping
(finding companies that have solved structurally similar problems in adjacent domains, with
investor rosters and intro paths). Uses parallel agents, checks internal sources first, and
delivers prose-first synthesis documents.

---

## Step 0: Company Context Check (Run First, Every Time)

Before doing anything else, check whether company context has been configured.

### How to check:
Read `references/company-context.md` and look for the line:
```
CONFIGURED: YES
```

### If NOT configured → Run the Setup Wizard

Walk the user through setup by asking these questions. Ask them one group at a time,
wait for answers, then move to the next group. Don't ask all at once.

**Group 1 — Company basics:**
- What's the company name?
- What does it do? (One or two sentences: business model, what problem it solves, who it serves.)

**Group 2 — Customers and product:**
- Who are the company's customers? (Type of buyer, industry, size.)
- What are the main products or services?
- Are there any internal terms, acronyms, or product names Claude should know?

**Group 3 — Competitive landscape:**
- Who are the main competitors?
- Is there a particular market or vertical the company focuses on?

**Group 4 — Research preferences:**
- Who typically uses research outputs? (e.g., executive team, product, sales)
- Any preferences on output format or communication style?

Once all questions are answered, write the responses into `references/company-context.md`
using the template structure in that file, and change the `CONFIGURED:` line to `YES`.

Confirm to the user: "Context saved. You won't need to go through this again unless
you want to update it. Starting your research now."

Then proceed to Phase 0.

### If configured → Proceed directly to Phase 0

Read the configured context and load it into memory. Pass relevant portions to every
research agent launched during this session.

### Updating context later

If the user says something like "update our company context", "add to the context",
or "our main competitor is now X", re-open `references/company-context.md`, make the
update, and confirm what changed. The user doesn't need to redo the full wizard.

---

## Phase 0: Internal Recon

Before planning or launching any web research, **check what the organization already knows.**
This prevents agents from re-researching ground already covered and often surfaces the most
relevant context faster than any web search.

### Search internal sources (run in parallel):

1. **Internal docs** — Use the `search` tool with 2–3 relevant queries. Look for: prior
   analyses, strategy docs, memos, product briefs related to the topic.

2. **Slack** — Use `slack_search_public_and_private` with 2–3 queries. Look for: recent
   discussions, decisions, shared links, or data points on the topic.

3. **Meetings** — Use `meeting_lookup` if the topic has likely been discussed recently.

### What to do with internal findings:

- **Summarize for the user:** "I found X internal docs and Y Slack threads on this.
  Key existing context: [2–3 sentence summary]. Proceeding to fill the gaps with
  external research."
- **Pass to research agents** as pre-loaded context so they build on existing work
  rather than duplicate it.
- **Identify the gaps** — what does the organization *not* already know?

If internal recon finds the question is already well-answered internally, say so and
ask whether to proceed with external research or synthesize what already exists.

---

## Phase 1: Plan the Research

### 1. Identify the research type

Match the user's request to one of the five research types and read the corresponding
reference file for section guidance:

| Type | When to use | Reference file |
|------|-------------|----------------|
| **Market Sizing** | TAM/SAM/SOM, territory analysis, opportunity sizing | `references/market-sizing.md` |
| **Competitive Analysis** | Landscape scans, competitor profiles, positioning against rivals in the same domain | `references/competitive-analysis.md` |
| **Build/Buy/Partner** | Capability gap decisions, M&A targets, partnership evaluation | `references/build-buy-partner.md` |
| **Company Deep Dive** | Single-company profile — public earnings, M&A target, or partner | `references/company-deep-dive.md` |
| **Industry & Trend** | Market dynamics, emerging trends, how a space is shifting | `references/industry-trend.md` |
| **Analog Mapping** | Find companies that solved a structurally similar problem in a *different* domain; map their investors and identify intro paths | `references/analog-mapping.md` |

**Choosing between Competitive Analysis and Analog Mapping:** Competitive Analysis = rivals in your domain. Analog Mapping = companies that have cracked a similar structural problem elsewhere. The output goal is also different — Competitive Analysis informs positioning; Analog Mapping generates warm introductions.

If the request blends types, plan agents for each.

### 2. Understand the question

- What exactly are we trying to learn?
- Who will use this research and for what decision?
- What's the time horizon and urgency?

### 3. Decompose into agent workstreams

Each agent should have:
- A clear, non-overlapping scope
- 3–6 specific sections to write (drawn from the reference template for the research type)
- A target output of ~500–1,500 lines of markdown

### 4. Plan the synthesis agent

Runs AFTER all research agents complete. Reads all outputs and produces a single
coherent prose document with cross-cutting insights, contradictions, and a clear
recommendation or "so what."

### 5. Present the plan

```
## Research Plan: [Topic]

**Research type:** [Market Sizing / Competitive Analysis / Build/Buy/Partner / Company Deep Dive / Industry & Trend / Hybrid]
**Decision this informs:** [What question does this answer?]

### Agent 1: [Name]
**Scope:** [1–2 sentence scope]
**Sections:**
1. [Section name]
2. [Section name]
3. ...
**Output file:** research/[topic]/[agent-name].md

### Agent 2: [Name]
...

### Synthesis Agent
**Runs after:** All research agents complete
**Output file:** research/[topic]/synthesis.md
```

**Wait for user approval before proceeding.** Do NOT launch agents until confirmed.

---

## Phase 2: Create Skeleton Files

Once the user approves the plan:

1. **Create the output directory:** `research/[topic]/`

2. **For each research agent, create a skeleton markdown file:**

```markdown
# [Agent Name]: [Scope Title]

**Status:** IN PROGRESS
**Last updated:** [timestamp]

---

## CRITICAL INSTRUCTIONS FOR AGENT

> **YOU WILL BE STOPPED AND RELAUNCHED IF YOU VIOLATE THIS PROTOCOL.**
>
> The ONLY acceptable pattern is: **Search -> Edit -> Search -> Edit -> Search -> Edit.**
> NEVER: Search -> Search. NO EXCEPTIONS. NOT EVEN ONCE.
>
> After EVERY search or fetch, IMMEDIATELY Edit this file with what you learned.
> If you do two searches in a row without an Edit to this file, you are VIOLATING THE
> PROTOCOL and will be killed.
>
> Work through sections in order. For each section:
> 1. Search/fetch for information
> 2. IMMEDIATELY write findings to this file under that section
> 3. Search/fetch for more information on the same section
> 4. IMMEDIATELY update this file with additional findings
> 5. Move to next section only after writing current section
>
> If a web fetch returns a 403 error, WRITE WHAT YOU HAVE before trying another URL.
>
> Every number needs a source. Every source needs a clickable URL inline.
> Do NOT collect sources at the end — put them inline with the facts.
>
> When you are DONE with all sections, change "Status: IN PROGRESS" to "Status: COMPLETE".

---

## Company Context

[Paste relevant sections from references/company-context.md here]

---

## Internal Research Findings (from Phase 0)

[Paste relevant internal docs/Slack findings here, or "None found."]

---

## 1. [First Section Name]

[To be filled by research agent]

## 2. [Second Section Name]

[To be filled by research agent]

...
```

3. **Also create the synthesis skeleton** with similar critical instructions, noting it
   should read from the other agent output files.

---

## Phase 3: Launch Research Agents

Launch ALL research agents in parallel using the Task tool with `run_in_background: true`.

Each agent prompt MUST include:

1. **The research question and their specific scope** — be precise about boundaries
2. **The exact file path they must write to** — absolute path
3. **The section list they must complete** — numbered, in order
4. **Company context** — paste the relevant sections from `references/company-context.md`
5. **Internal findings from Phase 0** — any relevant docs or discussions found internally
6. **The critical write protocol** — copy verbatim:

```
CRITICAL WRITE PROTOCOL — READ THIS BEFORE DOING ANYTHING:

YOU WILL BE STOPPED AND RELAUNCHED IF YOU VIOLATE THIS PROTOCOL.

The ONLY acceptable pattern is: Search -> Edit -> Search -> Edit -> Search -> Edit.
NEVER: Search -> Search. NO EXCEPTIONS. NOT EVEN ONCE.

You MUST Edit your output file after EVERY SINGLE search or web fetch.
If you do two searches in a row without an Edit to your file, you are VIOLATING THE
PROTOCOL and will be killed.

Work through your sections IN ORDER (1, 2, 3...). For each section:
1. Do ONE search or web fetch
2. IMMEDIATELY Edit the file to write what you learned under that section
3. Do another search if needed
4. IMMEDIATELY Edit the file again with additional findings
5. Only move to the next section after the current one has real content

If a web fetch returns a 403 error, do NOT try multiple alternative URLs before writing.
Write what you have so far, THEN try another URL, THEN write again.

Every quantitative claim needs an inline source URL: [Source Name](https://url.com)
Do NOT put sources at the bottom. Inline only.

When ALL sections are complete, change the file's Status line from "IN PROGRESS" to "COMPLETE".
```

7. **Use `subagent_type: "general-purpose"`** for all research agents

**IMPORTANT:** Use `run_in_background: true` for all research agents so they run in parallel.

After launching, tell the user how many agents are running and their output file paths.

---

## Phase 4: Monitor Progress

### Check-in 1: ~30 seconds after launch
- Read each agent's output file to verify they've started writing
- Report: which agents have started, which haven't
- Flag any agent with an empty file — it may be stuck in a research loop

### Check-in 2: ~2 minutes after launch
- Read each agent's output file
- Report: approximate progress (which sections have content, rough line counts)
- Flag any agent that hasn't progressed since last check

### Check-in 3: ~5 minutes after launch
- Report: which agents are complete (Status: COMPLETE), which are still working
- **STUCK AGENT RULE:** If an agent's line count has NOT increased between two
  consecutive check-ins, stop it immediately with TaskStop and relaunch

### Subsequent check-ins: Every 5 minutes

**How to check:** Use `wc -l` via Bash on all agent output files for a quick line count
comparison. Then Read specific files only if you need to see section progress.

**How to report (keep it concise):**
```
Agent check-in [#N]:
- Agent 1 (Market sizing): ~120 lines, sections 1–3 done, working on 4/6
- Agent 2 (Competitive): ~80 lines, sections 1–2 done, working on 3/5
- Agent 3 (Industry): COMPLETE (185 lines)
```

### Stuck Agent Recovery

1. **Stop the agent** immediately with TaskStop. Do not wait — it won't self-correct.
2. **Read the output file** to see what sections are already complete.
3. **Check the agent's process output** (TaskOutput) to extract any useful data found
   but never written to file.
4. **Relaunch with a new agent** that:
   - Is told which sections are already complete and to skip them
   - Is given any useful data extracted from the stuck agent's search results
   - Has even stricter write protocol: "You WILL be stopped if you do two searches
     without an Edit. NO EXCEPTIONS."
   - Starts by writing pre-loaded data to the file FIRST, then searches for more
5. **Monitor the relaunched agent** on the same check-in schedule.

---

## Phase 5: Synthesis

Once ALL research agents are complete (or user decides to proceed with what's available):

1. **Launch the synthesis agent** (foreground or background per user preference)

2. The synthesis agent MUST:
   - Read ALL research agent output files and all internal findings from Phase 0
   - Identify cross-cutting themes, contradictions, and gaps
   - Produce a single coherent **prose-first document** (not bullets) with:
     - **Opening thesis** — 2–3 sentences stating the key finding or recommendation
     - **Context** — why this question matters, what decision it informs
     - **Key findings** — organized by theme, not by agent
     - **Tensions and contradictions** — found across sources
     - **Confidence assessment** — what's well-supported vs. needs validation
     - **Recommended next steps** — concrete and actionable
   - Follow the write protocol (write after every read)
   - Match the communication style preferences from `references/company-context.md`

3. **For Analog Mapping**, the synthesis follows a different structure than the standard
   thesis/findings/implications format — see `references/analog-mapping.md` for the
   required output format. Key differences: per-company entries with investors and intro
   paths, a cross-cutting investor network map, and ordered next steps with specific intro
   angles. Do NOT default to bullet lists or competitive positioning framing.

4. **Report to user** when synthesis is complete with a 2–3 sentence summary of the
   key finding.

---

## Key Rules

1. **Run the Company Context Check (Step 0) before anything else.** Every session.
2. **Never launch agents without user approval of the plan.**
3. **Always run Phase 0 (internal recon) before planning web research.**
4. **Every agent gets company context and internal findings.**
5. **Every agent gets the critical write protocol verbatim.**
6. **Monitor proactively.** Check in on schedule without waiting for the user to ask.
7. **Kill stuck agents immediately.** If line count hasn't changed across two check-ins,
   TaskStop and relaunch. Agents do NOT self-correct.
8. **Synthesis output is prose, not bullets** — unless the user's style preferences
   explicitly call for something different.
9. **Agents cannot run Bash.** They have: WebSearch, WebFetch, Read, Write, Edit,
   Glob, Grep. Parse PDFs in the main session before launching agents.
10. **Every number needs an inline source URL.** No orphaned facts.
11. **Pre-load data on relaunch.** Extract useful findings from a stuck agent's output
    before relaunching — prevents re-researching the same ground.
12. **Analog Mapping ≠ Competitive Analysis.** The companies found are not competitors —
    they operate in different domains. Do not frame the synthesis as positioning or
    differentiation analysis. The output goal is warm introductions and pattern learning.
