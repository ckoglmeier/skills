---
name: evidence-to-claim-auditor
description: >
  Audit evidence, benchmarks, evals, experiments, customer proof, research findings, or diligence materials and translate them into honest claims. Use when asked what results prove, what can be said publicly or to investors/customers, whether a claim is overreaching, how to rewrite a takeaway, or what next test would substantiate a stronger claim.
---

# Evidence To Claim Auditor

## Overview

Use this skill to keep claims proportional to evidence. The job is to separate what is proven, suggested, unproven, contradicted, or still ambiguous, then rewrite the message so it is useful without overstating.

Default posture: be commercially useful and epistemically strict. Do not sand off the insight; downgrade the claim until it matches the evidence.

## Core Workflow

1. **Collect the evidence**
   - Identify source artifacts: eval outputs, benchmark tables, logs, experiment notes, deck claims, customer quotes, research docs, or model comparisons.
   - Capture dates, versions, sample sizes, baselines, domains, success criteria, and whether results are static evals, live runs, simulations, user anecdotes, or production data.
   - If the evidence is incomplete, proceed with caveats rather than inventing missing support.

2. **Normalize the evidence**
   - Build a short evidence table: source, what happened, baseline/comparison, strength, caveats.
   - Separate direct evidence from interpretation.
   - Distinguish "worked in this narrow setting" from "generalizes."

3. **Audit each claim**
   - Classify claims using the ladder in `references/claim-ladder.md`.
   - Mark each claim as `proven`, `suggested`, `not_shown`, `contradicted`, or `needs_more_evidence`.
   - Name the exact overreach when a claim is too strong.

4. **Look for alternative explanations**
   - Check whether the result could be caused by sample selection, easier tasks, data leakage, evaluation mismatch, prompt/runtime changes, human intervention, weak baselines, or domain specificity.
   - If a failure is informative, state what it narrows or redirects rather than treating it as pure negative signal.

5. **Rewrite the claims**
   - Provide a clean version the user can use in a deck, memo, launch note, investor update, or internal decision.
   - Prefer "shows", "suggests", "points toward", "does not yet show", and "the next test is" with precision.
   - Avoid laundering speculation through confident language.

6. **Define the next proof**
   - State the smallest next test that would upgrade the claim.
   - Include success criteria, baseline, domain, and anti-regression checks when relevant.

## Claim Standards

Read `references/claim-ladder.md` when the evidence is technical, quantitative, investor-facing, or likely to be reused.

Use stronger language only when the evidence supports it:

- "Proves" requires direct evidence against a meaningful baseline, with success criteria set before interpretation.
- "Shows" requires direct evidence in the stated scope.
- "Suggests" is appropriate for early, narrow, or noisy results.
- "Points toward" is appropriate when a result changes the next test but does not substantiate the thesis.
- "Does not yet show" is often the most valuable sentence in the audit.

## Output Shape

Use this structure unless the user asks for only a rewrite:

1. **Bottom line**: the cleanest honest read.
2. **Evidence table**: source, result, strength, caveat.
3. **Claim audit**: original claim, status, better claim.
4. **Message to use**: polished language for the intended audience.
5. **Next test**: what would upgrade or falsify the claim.

When editing a deck or document directly, still keep the audit in mind: every replacement sentence should preserve the evidence boundary.
