---
name: content-ops
description: >
  Expert panel scoring and iterative content improvement engine. Assembles 7–10 domain
  experts to evaluate and improve content (copy, landing pages, strategy docs, titles,
  charts, candidate evaluations) using content-specific rubrics. Recurses until quality
  reaches 90/100 or 3 rounds complete. Humanizer expert weighted 1.5x. Adds rejection
  patterns to references/patterns.md when scoring another skill's output.

  Trigger on: "expert panel this," "score this," "rate these variants," "quality check
  this," "which version is better," "expert score," "evaluate this."
---

# Expert Panel — Quality-Scored Content Production

The Expert Panel is a general-purpose evaluation tool that assembles domain experts to score and iteratively improve content across multiple formats. It handles copy, landing pages, strategy docs, titles, charts, and evaluations, recursing until quality reaches 90+ (maximum 3 iterations).

## Core Process

- **Intake:** Collects artifact type, offer context, and variants
- **Auto-assembly:** Builds 7–10 tailored experts using pre-built panels, always including an AI Writing Detector (weighted 1.5x) and Brand Voice Match expert
- **Scoring & Iteration:** Uses content-specific rubrics and executes a recursive loop until reaching 90 aggregate score or completing 3 rounds
- **Output:** Displays winning score and final content first, followed by collapsible scoring history
- **Pattern Learning:** Adds patterns to `references/patterns.md` when scoring another skill's output

## Scoring Rules

- Brutally honest assessment; no padding scores
- Minimum 90/100 target (non-negotiable unless impossible)
- Maximum 3 improvement rounds
- All iterations shown in output for transparency
- Pattern-based point docks applied before expert scoring
- Humanizer expert scores weighted 1.5x

## Trigger Phrases

"Expert panel this," "score this," "rate these variants," "quality check this," "which version is better," "expert score," "evaluate this."
