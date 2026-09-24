# Runtime & Handoff Patterns

How a designed pass actually runs. Pick by available tooling, budget, and whether you want a second provider's independent pass.

## Pattern 1 — Single-context pass
Run the sections sequentially in one conversation, switching model per leg where the harness allows. Simplest and cheapest; no orchestration. Loses parallelism, and a long pass can strain one context window. Good for small passes (≤5 sections) or when workflow tooling isn't available.

## Pattern 2 — Parallel subagents (default)
Fan the sections out concurrently: per section, a cheap-model retrieve agent (web on) whose sourced findings feed a mid-model synthesis and a strong-model judgment. Launch all sections' retrieve agents in one batch, then their synth/judge legs as results land. Finish with the red team and the verdict as single strong agents at the highest effort, each given every section's Evidence + Judgment. Fastest wall-clock, keeps each leg in a fresh context, and needs nothing beyond subagents with a per-agent model setting (in Claude Code: `model: haiku | sonnet | opus`).

**Scripted-workflow variant:** if the user has explicitly opted into a workflow runner, the same shape is `pipeline(sections, retrieve, synthesize, judge)` then two single `agent()` calls. Don't reach for it without that opt-in — it can spawn a lot of agents.

Emit the tiering log at the end either way.

## Pattern 3 — Split-provider handoff
One provider does the legwork; the report comes back to a strong model in the primary environment for the final synthesis. The proven case: **Codex/OpenAI runs sections A–G, then the assembled report returns to Claude for a single Fable/Opus synthesis** (verdict, rubric, wedge, gates, plan).

Use it when:
- the judgment-tier model is quota- or credit-constrained (offload the bulk legwork elsewhere), or
- you want a genuinely independent provider's pass on the evidence before the primary model synthesizes.

### The single-paste orchestration prompt (the deliverable for a handoff)
Produce **one self-contained prompt** the other environment can run in a single paste. It must:

1. **Embed the settled context** — the concept definition, any already-decided findings, and the key comps — so it depends on no other files. The receiving model has none of your local artifacts.
2. **State the method inline** — retrieve → synthesize → judge per section, kept *visibly separate* in the output; label every claim Verified/Likely/Speculative/Could-not-verify with sources.
3. **Give the tiering conditionally** — "if your setup can route steps to different models, use [cheap]/[mid]/[strong]; otherwise run everything on your strongest available model." A single external session usually runs one model, so don't assume per-leg routing.
4. **Require web/search be on** for the retrieve legs, with a fallback model note if it can't browse — otherwise the legwork confabulates.
5. **Fix the output format** — per section: `Evidence` (retrieve+synthesize, sourced) then `Judgment` (the call + required one-liner).
6. **STOP before the verdict** — explicitly instruct the legwork model *not* to write the executive verdict/rubric/beachhead/plan. Those are produced downstream by the synthesis model from its report.

Keep a human-facing "how to run" note *above* the paste line (which model to start the session on, turn web on), clearly marked as not part of the paste.

## Two disciplines that make handoffs (and any pass) auditable

- **Carry the evidence forward, not just the conclusions.** When the report comes back, the synthesis model's job includes checking whether each judgment actually follows from its cited evidence. It can only do that if the `Evidence` blocks travel with the `Judgment` blocks. Conclusions alone can't be audited — they can only be trusted.
- **Stop before the verdict.** Separating the legwork from the final call means the synthesizer is a genuine second opinion that can *correct* a section whose judgment overreached, rather than inheriting and rubber-stamping it. If the same model does legwork and verdict, you lose that check.
