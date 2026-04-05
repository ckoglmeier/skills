# CK Skills Library

Public Claude Code skills — borrowed from the community and generic templates. Install any skill by copying its raw URL into your Claude Code project, or use the `claude /plugin install` command.

## Borrowed Skills

Skills adapted from public repos by other builders.

| Skill | Description | Install |
|---|---|---|
| content-ops | Expert panel scoring and iterative content improvement (90/100 target) | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/content-ops.md) |
| outbound-engine | Cold email + Instantly.ai automation with ICP definition and expert panel scoring | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/outbound-engine.md) |
| revenue-intelligence | Gong call analysis, GA4/HubSpot attribution, unified client reporting | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/revenue-intelligence.md) |
| sales-pipeline | Visitor → intent score → deal routing + self-learning ICP | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/sales-pipeline.md) |
| team-ops | "Elon Algorithm" team audits + meeting action extractor | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/team-ops.md) |
| growth-engine | A/B experimentation with bootstrap CI + auto-playbook | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/growth-engine.md) |
| finance-ops | CFO briefings from QuickBooks exports + codebase cost estimator | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/finance-ops.md) |
| conversion-ops | Landing page CRO audits + survey-to-lead-magnet engine | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/conversion-ops.md) |

### CTO Team (12 sub-skills from [alirezarezvani/claude-cto-team](https://github.com/alirezarezvani/claude-cto-team))

| Skill | Description | Install |
|---|---|---|
| cto-team: antipattern-detector | Spots failure patterns across architecture, timeline, team, process & tech | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-antipattern-detector.md) |
| cto-team: architecture-pattern-selector | Recommends monolith vs. microservices vs. serverless based on real constraints | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-architecture-pattern-selector.md) |
| cto-team: assumption-challenger | Stress-tests plans across timeline, resource, technical, business & external | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-assumption-challenger.md) |
| cto-team: clarification-protocol | Generates 2-3 sharp questions to cut through vague requirements | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-clarification-protocol.md) |
| cto-team: cost-estimator | TCO frameworks with 2024-2025 infra pricing and build-vs-buy analysis | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-cost-estimator.md) |
| cto-team: delegation-prompt-crafter | Structures prompts in CONTEXT/TASK/REQUIREMENTS format | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-delegation-prompt-crafter.md) |
| cto-team: ml-cv-specialist | ML system design, model selection, API vs. self-hosted, CV pipelines | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-ml-cv-specialist.md) |
| cto-team: request-analyzer | Classifies intent and routes to the right specialist | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-request-analyzer.md) |
| cto-team: roadmap-generator | MVP → Scale → Advanced roadmaps with epic/story/task breakdowns | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-roadmap-generator.md) |
| cto-team: scalability-advisor | 4-stage scaling framework (startup → enterprise) with bottleneck detection | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-scalability-advisor.md) |
| cto-team: tech-stack-recommender | Technology selection across frontend, backend, database, and infra | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-tech-stack-recommender.md) |
| cto-team: validation-report-generator | 8-section validation reports with GOOD / NEEDS MAJOR WORK / BAD verdicts | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/cto-team-validation-report-generator.md) |

## Templates

Generic skills that work for anyone with minimal or no configuration.

| Skill | Description | Install |
|---|---|---|
| exec-feedback | Template for first-pass document feedback in any executive's voice — configure once, use forever | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/exec-feedback.md) |
| find-skills | Helps discover and install agent skills | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/published/find-skills.md) |

---

## Installing as a Claude Code Marketplace

Add to your `~/.claude/settings.json`:

```json
"extraKnownMarketplaces": {
  "ck-skills": {
    "source": { "source": "github", "repo": "ckoglmeier/skills" }
  }
}
```
