# Model Tiering Doctrine

Match the model to the **cognitive load of the leg**, not the importance of the section. This is the single highest-leverage cost decision in a discovery pass, and it follows one rule: cheapest models for research legs, strong models only for synthesis and judgment.

## The three tiers

| Tier | Job | Reasoning load | Needs web? | Model class |
|---|---|---|---|---|
| **Retrieve** | Gather facts + sources; do not conclude | Low | Yes | Cheapest capable |
| **Synthesize** | Write up what the evidence says; no final call | Medium | No | Mid |
| **Judge** | Make the section's decision | High | No | Strongest, effort scaled to the call |

## Current model choices (verify live before using — see below)

**Claude (in-session):**
- Retrieve → **Haiku**
- Synthesize → **Sonnet**
- Judge → **Fable** or **Opus** (highest effort — `max` — on the load-bearing calls: feasibility, the pivotal choice, red team, verdict)

**OpenAI (for split-provider handoff):**
- Retrieve → a `mini`/`nano`-class model *with web/search enabled* (or a search-native research model if the runtime can't browse)
- Synthesize → the flagship non-pro model
- Judge → the top reasoning/`pro` model, highest reasoning effort on the hard calls

Exact IDs churn monthly on the 5.x line — do not commit any ID from memory.

## Effort and structure rules

- **Scale effort within the judge tier.** Most `judge` legs run at `high`; reserve `max` for the calls that can sink the whole thesis — buildability/feasibility, the pivotal beachhead/wedge pick, the red team, and the final verdict.
- **Red team and final verdict are single agents, no delegation.** They must hold the entire picture in one context — don't pipeline them.
- **Everything else pipelines.** Sections run retrieve→synth→judge independently and concurrently; there's no barrier between sections unless a later section genuinely needs all prior results at once.

## Verify model IDs live — never from memory

Model lineups move fast enough that a remembered ID is often wrong or deprecated. Before committing the assignment, pull the current list from the provider or gateway that will run the pass:

```
curl -s https://api.anthropic.com/v1/models -H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01"
curl -s https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"
```

Pick the current tier members and **stamp the verification date** in the output (e.g. "Model IDs verified against the provider list on YYYY-MM-DD"). If the pass runs as Claude Code subagents, the tier aliases `haiku` / `sonnet` / `opus` resolve to current models on their own — record which models actually ran in the tiering log instead. If running later, re-verify. This is doubly important for cross-provider handoffs.

## Fable ↔ Opus interchange (judgment tier)

At the judgment tier, Fable and Opus are effectively interchangeable and make a safe mutual fallback — verified in practice: on the same prompts and same upstream evidence they reached the identical verdict and identical rubric scores. The one observed difference is that Fable sometimes surfaces extra specific evidence (e.g. catching two additional dead comps a parallel Opus run missed). So: if the primary judgment model hits a quota/credit wall mid-run, fall back to the other and **log the substitution** in the tiering log — the verdict is safe, and the log keeps the A/B honest.

## Always emit a model-tiering log

Every executed pass should end with a table of `leg → model → effort → what it did`, noting any fallbacks. It makes cost transparent, makes fallbacks auditable, and turns every run into a usable A/B of models against the same evidence.
