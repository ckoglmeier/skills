---
name: discovery-pass-designer
description: "Designs a rigorous multi-model discovery or diligence pass — turns a research/evaluation objective into (1) a sectioned discovery prompt and (2) a per-leg model + runtime assignment. Use whenever you're about to run a big research, diligence, or concept-evaluation pass and want it structured into sections with the right-cost model on each leg (cheap retrieval, mid synthesis, strong judgment), OR when you need to hand a research pass to another model/provider (e.g. Codex/OpenAI) and bring it back. Trigger on: 'design a discovery pass', 'help me write a discovery/research prompt', 'which models should run each part of this', 'assign models to these research legs', 'split this across models', 'hand this off to Codex/GPT and synthesize here', or any request to plan a multi-stage, multi-model research effort. This is the design/authoring skill — it produces ready-to-run prompt artifacts, it does not execute the research itself."
---

# Discovery Pass Designer

## What this skill produces

Two artifacts, always:

1. **A sectioned discovery prompt** — the objective decomposed into sections, each with its own retrieve → synthesize → judge sub-structure. Reusable and model-agnostic.
2. **A model + runtime assignment** — which model runs each leg, at what effort, in what runtime (single-context, parallel subagents, or a split-provider handoff), and why.

You are designing the *pass*, not running it. The output is something a human can execute later, hand to a workflow, or paste into another model. Keep that portability in mind — artifacts should be self-contained enough to run without you in the room.

## The core idea

A good discovery pass separates three cognitively different jobs and puts a different-cost model on each:

- **Retrieve** — gather facts with sources. Low reasoning, needs live web. Cheapest capable model.
- **Synthesize** — write up what the evidence says without making the call. Mid model.
- **Judge** — make the actual decision the section exists to answer. Strongest model, highest effort on the hardest calls.

This is the throughline: *match the model to the cognitive load of the leg, not to the importance of the section.* A market-sizing section is important, but its retrieval leg is still just fact-gathering — don't spend judgment-tier tokens on it. See `references/model-tiering.md` for the full doctrine and current model choices per tier.

## Workflow

### 1. Distill the objective
Get to one sentence: *what decision does this pass inform?* If the input is fuzzy or folds several ideas together, name the interpretations and pick the sharpest one to structure around — don't silently average them. A pass built on a vague objective produces a vague report.

### 2. Choose the sections
Start from the canonical skeleton in `references/discovery-prompt-skeleton.md` and adapt — drop sections that don't apply, add domain-specific ones, reorder so later sections can lean on earlier findings. Each section gets: the retrieve prompt (what to search), the synthesize prompt (what to write up), and the judge prompt (the exact call + any required one-line verdict).

### 3. Assign models and effort per leg
Apply `references/model-tiering.md`. Default: retrieval → cheapest capable + web; synthesis → mid; judgment → strongest, with the highest effort reserved for the load-bearing calls (feasibility, the pivotal choice, the red team, the final verdict). The red team and the final synthesis run as **single high-effort agents with no delegation** — they need the whole picture in one head.

**Verify model IDs live before committing them.** Model lineups move fast; never write IDs from memory. Check the provider's model list (e.g. `curl https://api.anthropic.com/v1/models` with your key, the OpenAI models endpoint, or whatever gateway you route through) or the model picker in the environment that will run the pass, and stamp the verification date in the output. Inside Claude Code, subagents take tier aliases (`haiku` / `sonnet` / `opus`), so no ID lookup is needed there. This matters most for OpenAI/cross-provider handoffs where the 5.x line churns.

### 4. Choose the runtime / handoff
Pick how it will actually run — see `references/handoff-patterns.md`:
- **Single-context pass** — run the sections in one conversation. Simplest, cheapest, least parallel.
- **Parallel subagents** — fan sections out to subagents with a per-agent model (cheap for retrieve, mid for synthesize, strong for judge), then run the red team and verdict as single strong agents. Available anywhere subagents are; a scripted workflow runner is an upgrade only if the user has opted into one.
- **Split-provider handoff** — one provider does the legwork (e.g. Codex/OpenAI runs the sectioned prompt), the report comes back to a strong model here for the final synthesis. Use when the judgment-tier model is quota/credit-constrained, or to get a second provider's independent pass.

### 5. Emit the artifacts
Write the discovery prompt and the assignment as files (a numbered artifact folder is a good convention — see the parent methodology). For a handoff, produce a **single self-contained paste-in prompt**: embed the settled context so it needs no other files, keep retrieve/synth/judge visibly separate, label every claim, **carry the evidence forward (not just conclusions)**, and — critically — tell the legwork model to **STOP before the final verdict** so the synthesis model owns the call. These two disciplines are why the handoff produces something a second model can actually audit rather than rubber-stamp.

## Principles worth stating

- **Cheapest model that can do the leg.** Spending a strong model on retrieval is the most common waste. 
- **Keep evidence and judgment separate in the output.** A downstream synthesizer (or a skeptical human) needs to check whether each call actually follows from its evidence. Conclusions without their evidence can't be audited.
- **Log which model ran each leg.** Every executed pass should end with a model-tiering log — it makes fallbacks (e.g. a judgment model hitting quota and falling back to another) transparent, and lets you A/B models later.
- **Label every claim** Verified / Likely / Speculative-Unverified / Could-not-verify, with a source where verified. Unlabeled confidence is how a discovery report launders a guess into a fact.

## Reference files

- `references/discovery-prompt-skeleton.md` — the canonical section skeleton (problem, ICP, sizing, competitive teardown, regulatory, business model, buildability, wedge, GTM, trust/safety, red team, + verdict) with per-section retrieve/synth/judge guidance and how to adapt it.
- `references/model-tiering.md` — the tier doctrine, current per-tier model choices (Claude and OpenAI), effort mapping, live-ID verification, and the Fable↔Opus interchange note.
- `references/handoff-patterns.md` — single-context vs. parallel subagents vs. split-provider handoff; the single-paste orchestration-prompt recipe; carry-evidence-forward and stop-before-verdict.

For the full opinionated venture-evaluation methodology that composes this skill, see the `venture-concept-discovery` skill.
