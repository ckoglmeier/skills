---
name: team-ops
description: >
  AI team performance analysis and meeting intelligence. Runs ruthless performance audits
  using the "Elon Algorithm" (5 steps: question requirements → delete redundancies →
  simplify workflows → accelerate bottlenecks → automate what's possible). Stack ranks
  A/B/C players with scorecards, OKR alignment, and workforce planning. Also extracts
  action items, decisions, and follow-ups from meeting transcripts with optional HubSpot
  task creation.

  Use for: team audits, stack ranking, OKR reviews, meeting debriefs.
---

# AI Team Ops

AI-powered team performance analysis and meeting intelligence: ruthless performance audits using the "Elon Algorithm" + automatic extraction of action items, decisions, and follow-ups from meeting transcripts.

## When to Use

- Evaluating team performance against OKRs/KPIs with a structured framework
- Stack ranking team members to identify A/B/C players
- Finding redundant roles, bottlenecks, and automation opportunities in your org
- Extracting action items and decisions from meeting transcripts
- Processing batch meeting notes into structured follow-up lists
- Pushing meeting action items to CRM (HubSpot) as tasks

## Tools

### Team Performance Audit
**Script:** `team_performance_audit.py`

Applies the 5-step Elon Algorithm:
1. Question requirements — challenge every role and deliverable
2. Delete redundancies — identify overlapping responsibilities
3. Simplify workflows — remove unnecessary process steps
4. Accelerate bottlenecks — find and fix what's slowing the team
5. Automate what's possible — surface automation opportunities

Scores each team member on: velocity, quality, independence, initiative.
Outputs: executive summary + individual scorecards + org recommendations.

### Meeting Action Extractor
**Script:** `meeting_action_extractor.py`

Extracts from meeting transcripts:
- Decisions (who + context)
- Action items (owner + deadline + priority)
- Open questions
- Key insights / quotes
- Follow-up meetings needed
- Implicit commitments
- Confidence scores per item

Output: Structured JSON or Markdown + optional HubSpot CRM task push.

## Configuration

### Required
- `ANTHROPIC_API_KEY` — Claude for analysis (default provider)

### Optional
- `OPENAI_API_KEY` — Alternative LLM provider
- `HUBSPOT_API_KEY` — Push meeting action items as HubSpot tasks
- `LLM_PROVIDER` — `anthropic` (default) or `openai`
- `LLM_MODEL` — Model name override

## Privacy

Remote telemetry is opt-in only. No code, file paths, or repo content is ever collected. Usage logged locally to `~/.ai-marketing-skills/analytics/`.
