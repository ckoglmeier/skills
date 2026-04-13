# Investment Council

A four-voice advisory council for pressure-testing investment deals. Runs after a single-pass evaluation is complete and surfaces the tensions that analysis alone can't resolve.

## The Four Voices

| Voice | Role | Output |
|---|---|---|
| **Bull** | Thesis Advocate — finds the upside case | Score (X/50) |
| **Bear** | Risk Analyst — finds the failure mode | Score (X/50) |
| **Calibrator** | Base Rate Analyst — checks against historical outcomes | Score (X/50) |
| **CFO** | Portfolio Construction & Sizing — checks the book, recommends check size | Verdict (Deploy/Defer/Pass) |

## How It Works

Three stages, every time:

1. **Independent Takes** — each voice evaluates blind, without seeing the others
2. **Rebuttals** — direct challenges, leading with contradiction (not agreement)
3. **Synthesis** — score spread, consensus range, key tensions, the one question only you can answer

The council does NOT replace your rubric. It stress-tests it.

## When to Use

- After any deal evaluation where the score lands in the ambiguous zone
- When you want to separate "good company" from "good investment"
- When you need to check whether thesis fit is creating false comfort
- Before committing capital on a deal that *feels* right but you can't articulate why

## Setup

1. Copy `SKILL.md` into your Claude Code skills directory
2. Customize the five elements listed in the CUSTOMIZATION section:
   - Scoring rubric scale
   - Your active thesis clusters
   - Your check size tiers
   - Portfolio data access (for the Calibrator and CFO)
   - Your kill criteria (for the Bear)
3. Run: `council: [deal name]` or `run the council on [deal]`

## Key Design Decisions

**The CFO doesn't score.** Deal quality is the Bull/Bear/Calibrator's job. The CFO answers a different question: "can the portfolio absorb this, and at what size?" Mixing deal quality and portfolio construction in one score hides information.

**High divergence is signal, not noise.** When the spread exceeds 10 points, it means the deal's risk profile is genuinely ambiguous. The right response is a smaller position or a pass — not averaging the scores and pretending you have consensus.

**Rebuttals lead with contradiction.** If a rebuttal opens with "I agree with Bear, but..." it's not a rebuttal. The most useful thinking happens when voices are forced to defend their position against a direct challenge.

---

*Built for angel deal evaluation. Adapts to any investment context with the right reference files.*
