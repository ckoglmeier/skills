---
name: growth-engine
description: >
  Autonomous marketing experimentation framework based on Karpathy's autoresearch pattern.
  Creates experiments with hypotheses, logs data points, runs statistical analysis
  (bootstrap CI + Mann-Whitney U), auto-promotes winners (p<0.05 + ≥15% lift) to a
  living playbook, and suggests next experiments. Supports batch mode (up to 10 variants).
  Tracks experiments across content, email, LinkedIn, SEO, and blog agents.

  Use for: A/B tests, multivariate experiments, weekly scorecards, campaign pacing,
  playbook review before creating new content.
---

# Growth Engine

Autonomous growth experimentation framework based on Karpathy's autoresearch pattern applied to marketing. Creates experiments with hypotheses, logs data points, runs statistical analysis (bootstrap CI + Mann-Whitney U), auto-promotes winners to a living playbook, and suggests next experiments. Supports batch mode (up to 10 variants simultaneously).

## When to Use

- Creating or managing A/B or multivariate experiments for any marketing channel
- Logging experiment data points after content is published or campaigns run
- Scoring experiments to determine statistical winners
- Checking the playbook for proven best practices before creating new content
- Generating weekly scorecards across all channels
- Monitoring campaign pacing and health

**Do NOT use for:** one-off content creation, non-experiment analytics, or campaign setup in external platforms.

## Workflow

1. **Before creating content:** `playbook` → apply proven rules
2. **When publishing:** `log` → record which variant was used and its metrics
3. **Periodically:** `score` → check if experiments have reached statistical significance
4. **Weekly:** `autogrowth-weekly-scorecard.py` → review all channels
5. **After completing experiments:** `suggest` → pick the next variable to test

## Commands

```bash
# Create an experiment
python3 experiment-engine.py create --agent <name> --hypothesis "..." --variable "<var>" --variants '["a","b"]' --metric "<metric>" --cycle-hours 24

# Log a data point
python3 experiment-engine.py log --agent <name> --experiment-id <EXP-ID> --variant "<variant>" --metrics '{"metric": value}'

# Score an experiment
python3 experiment-engine.py score --agent <name> --experiment-id <EXP-ID>

# Check the playbook
python3 experiment-engine.py playbook --agent <name>

# Suggest next experiments
python3 experiment-engine.py suggest --agent <name>

# Weekly scorecard
python3 autogrowth-weekly-scorecard.py [--weeks N] [--output file.md]

# Campaign pacing
python3 pacing-alert.py [--json]
```

## Promotion Criteria

Winners auto-promote to the playbook. Requires **p < 0.05 AND ≥ 15% lift**.

Statuses: `running` → `trending` → `keep` (winner) or `discard` (loser)

## Configuration

| Variable | Default | Description |
|---|---|---|
| `GROWTH_ENGINE_DATA_DIR` | `./data/experiments` | Data directory |
| `GROWTH_ENGINE_AGENTS` | `content,email,linkedin,seo,blog` | Tracked agents |
| `P_WINNER` | `0.05` | p-value threshold for winner |
| `LIFT_WIN` | `15.0` | Minimum % lift for keep decision |
| `BOOTSTRAP_ITERATIONS` | `1000` | Bootstrap resamples for CI |
| `BATCH_MODE_MAX_VARIANTS` | `10` | Max variants in batch mode |

## Dependencies

```
pip install numpy scipy
```

## Privacy

Remote telemetry is opt-in only. No code, file paths, or repo content is ever collected.
