---
name: finance-ops
description: >
  AI-powered financial analysis suite. Generates executive CFO briefings from QuickBooks
  exports (P&L, Balance Sheet, General Ledger, Cash Flow, etc.) with anomaly detection,
  burn rate, runway analysis, and scenario modeling. Also estimates codebase development
  costs with organizational overhead and AI ROI analysis.

  Trigger on: "CFO briefing", "financial analysis", "cost briefing", "expense review",
  "runway analysis", "burn rate", "cost estimate", "how much would this cost to build",
  "development cost", "Claude ROI".
---

# AI Finance Ops

Two tools: CFO Briefing Generator and Codebase Cost Estimator.

---

## Tool 1: CFO Briefing Generator

Generate executive financial summaries from QuickBooks exports.

### Workflow

#### 1. Ingest Files

Place QuickBooks export files (CSV, XLSX, XLS) in a working directory. Accepted report types (P&L alone is sufficient):

- **P&L Summary** — Revenue, COGS, expenses, net income (MOST IMPORTANT)
- **P&L by Customer** — Revenue breakdown by client
- **Balance Sheet** — Assets, liabilities, equity
- **General Ledger** — All account transactions
- **Expenses by Vendor** — Vendor-level expense breakdown
- **Cash Flow Statement** — Operating/investing/financing flows

#### 2. Run Analysis

```bash
python3 scripts/cfo-analyzer.py --input ./data/uploads/ [--period YYYY-MM]
```

The script auto-detects file types, computes all KPIs, compares to prior period, and outputs a formatted executive summary with emoji status indicators (🟢🟡🔴).

#### 3. Scenario Modeling (Optional)

```bash
python3 scripts/scenario-modeler.py --input ./data/financial-latest.json
```

Generates 12-month projections for base / bull / bear cases.

---

## Tool 2: Codebase Cost Estimator

Estimate full development cost of a codebase.

### Workflow

1. **Analyze** — catalog LOC by language, architectural complexity, testing coverage
2. **Calculate hours** — apply productivity rates from `references/rates.md` with overhead multipliers
3. **Research rates** — current market rates for the relevant tech stack (low/median/high)
4. **Org overhead** — convert raw dev hours to calendar time across company types (Solo → Enterprise)
5. **Full team cost** — supporting role ratios and team multipliers with role-by-role breakdown
6. **Output** — full estimate using template in `references/output-template.md`
7. **AI ROI** (optional) — if built with AI assistance, calculate speed multiplier vs human developer and cost savings

### Key Principles

- Always show ranges (low/avg/high), never a single number
- Search for CURRENT year market rates
- Include confidence level and key assumptions
- Highlight highest-complexity areas that drive cost

## Privacy

Remote telemetry is opt-in only. No code, file paths, or repo content is ever collected. Usage logged locally to `~/.ai-marketing-skills/analytics/`.
