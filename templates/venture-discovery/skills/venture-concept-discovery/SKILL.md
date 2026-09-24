---
name: venture-concept-discovery
description: "End-to-end diligence on a raw venture or product concept — takes a fuzzy startup/product idea and produces an evidence-grounded discovery report with a GO / RESHAPE-THE-WEDGE / NO-GO verdict, a scored rubric, a committed wedge/beachhead, pre-committed kill gates, and a concrete 90-day discovery plan. Use whenever someone brings a new business or product idea and wants to know whether it's real and in what shape — 'is there a business here', 'should we build X', 'discovery on this concept', 'evaluate this startup idea', 'pressure-test this venture', 'what's the wedge', 'is this venture-shaped', or a multi-framing brainstorm that needs to become a testable thesis. Works for consumer, prosumer, and B2B concepts. Runs the pass with tiered models, and when evidence contradicts the pitch it reshapes the wedge rather than just scoring it low. Composes the discovery-pass-designer skill for the authoring stage."
---

# Venture Concept Discovery

Turn a raw concept into a decision. The output is not a research dump — it's a verdict with the evidence and the next moves behind it.

## The five stages

### 1. Frame the concept
Distill the idea to a **testable thesis**: one wedge, one ICP, one payer, one monetization. Raw concepts often fold several ideas together (a "family OS" that's also a neobank that's also a wealth advisor) — don't average them; pick the sharpest starting wedge and name what you're setting aside. Two questions to answer up front, because they determine everything downstream:
- **Who is the payer, and are they the same person as the sufferer?** A huge, emotionally real pain felt by someone with no money or authority to buy is not a monetizable pain. This mismatch is the most common reason a "obvious" concept has no business.
- **What is the acute trigger** (if any) that turns the chronic condition into a purchase, and can you reach the buyer at that moment?

### 2. Author the discovery pass
Use the **`discovery-pass-designer`** skill to build the sectioned prompt and the model/runtime assignment. The venture skeleton (problem, ICP, sizing, competitive+graveyard teardown, regulatory, business model, buildability, wedge, GTM, trust/safety, red team, verdict) is its `references/discovery-prompt-skeleton.md`. Front-load any settled context so no leg re-litigates it.

### 3. Execute with tiered models
Run the pass per the assignment (cheap retrieve → mid synth → strong judge; red team and verdict as single high-effort agents). Pick the runtime — single-context, parallel subagents, or split-provider handoff — from the designer skill's `references/handoff-patterns.md`. Emit a model-tiering log.

### 4. Synthesize the verdict
Produce the decision using `references/rubric-and-verdict.md`: the executive verdict (GO / RESHAPE-THE-WEDGE / NO-GO) with a single sentence to remember, the 7-dimension scored rubric, the committed wedge/beachhead, pre-committed kill gates, and a concrete 90-day discovery plan (interview segments with counts and specific recruiting channels, plus the riskiest "go" assumptions each paired with a falsifiable test).

### 5. Reshape the wedge (the loop that makes this worth doing)
A low score is usually not a NO — it's a *wrong-wedge* signal. Before concluding NO-GO, run the reframes in `references/reshape-loop.md` (payer≠sufferer → bill the party with money/authority; D2C → B2B2C through whoever already touches the trigger; linear-labor → agentic force-multiplier; roll-up → single-wedge depth) and re-run the sections the reframe changes. Only call NO-GO when *every* reframe hits the same structural wall (uninsurable, unbuildable mechanic, category revenue ceiling). In one reference pass, reshaping turned a dead consumer neobank for family caregivers into a defensible B2B coordination tool.

## Interpretation doctrines (what separates diligence from cheerleading)

- **Separate the payer from the sufferer.** (Stated above because it's that important.)
- **Falsify with the graveyard.** The strongest evidence is dead and stalled comps. If several companies tried this exact thing and died, "the market is huge" is a red flag, not a green one — find out what killed them and whether you've solved it.
- **Emotionally-real ≠ monetizable.** These are different claims requiring different evidence. A pain can be devastating and still support no subscription.
- **TAM-of-unpaid-labor is not TAM.** A trillion-dollar valuation of unpaid caregiving hours is a hole in the economy, not liquid dollars available for your product. Size bottoms-up against what comps actually earn.
- **Distribution is usually the silent killer.** Every scaled comp tends to ride an institutional channel; if the only channel you have is D2C paid acquisition into a crisis moment, that's often disqualifying on its own.
- **Name the honest ceiling.** "Bad venture outcome" and "bad business" are different. A concept can be un-venture-shaped (category tops out at ~$50M/yr) yet a fine bootstrapped software business. Say which it is.

## Output convention
Break the work into its own folder with numbered artifacts and a README index, so the reasoning is reconstructable and the prompt is reusable. The reference layout:

```
<concept>/
├── README.md                 # index + current status/verdict in one glance
├── 01_seed_research.md        # initial landscape scan
├── 02_discovery_prompt.md     # the reusable sectioned prompt
├── 03_discovery_report.md     # primary deliverable: verdict, rubric, plan
├── 04_..._framing.md          # any reshape memo (e.g. the agentic reframe)
└── 05+/06+                    # reshaped prompt + handoff artifacts, if any
```

Keep the README's status line current — a reader should learn the verdict and where things stand in one glance.

## Reference files
- `references/rubric-and-verdict.md` — the 7-dimension rubric, the verdict format, kill gates, and the 90-day-plan structure.
- `references/reshape-loop.md` — the reframes, adjacency/analog mapping, and when to stop reshaping and call NO-GO.

Depends on the `discovery-pass-designer` skill for stages 2–3.
