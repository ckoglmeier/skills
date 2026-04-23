# CK Skills Library

Public Claude Code skills — borrowed from the community and generic templates. Install any skill by copying its raw URL into your Claude Code project, or use the `claude /plugin install` command.

## Repo layout

- **`borrowed/`** — Third-party plugins mirrored from other public repos. Credit in each SKILL.md.
- **`templates/`** — Generic, shareable plugins that work for anyone with minimal configuration. These are safe to reference from other marketplaces (e.g. classroom pulls several of these via `git-subdir`).
- **`playbooks/`** — Little prompts, workflows and skills.  

## Borrowed Skills

Skills adapted from public repos by other builders.

| Skill | Description | Install |
|---|---|---|
| content-ops | Expert panel scoring and iterative content improvement (90/100 target) | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/content-ops/skills/content-ops/SKILL.md) |
| outbound-engine | Cold email + Instantly.ai automation with ICP definition and expert panel scoring | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/outbound-engine/skills/outbound-engine/SKILL.md) |
| revenue-intelligence | Gong call analysis, GA4/HubSpot attribution, unified client reporting | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/revenue-intelligence/skills/revenue-intelligence/SKILL.md) |
| sales-pipeline | Visitor → intent score → deal routing + self-learning ICP | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/sales-pipeline/skills/sales-pipeline/SKILL.md) |
| team-ops | "Elon Algorithm" team audits + meeting action extractor | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/team-ops/skills/team-ops/SKILL.md) |
| growth-engine | A/B experimentation with bootstrap CI + auto-playbook | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/growth-engine/skills/growth-engine/SKILL.md) |
| finance-ops | CFO briefings from QuickBooks exports + codebase cost estimator | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/finance-ops/skills/finance-ops/SKILL.md) |
| conversion-ops | Landing page CRO audits + survey-to-lead-magnet engine | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/conversion-ops/skills/conversion-ops/SKILL.md) |

### CTO Team (12 sub-skills from [alirezarezvani/claude-cto-team](https://github.com/alirezarezvani/claude-cto-team))

| Skill | Description | Install |
|---|---|---|
| cto-team: antipattern-detector | Spots failure patterns across architecture, timeline, team, process & tech | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/antipattern-detector/SKILL.md) |
| cto-team: architecture-pattern-selector | Recommends monolith vs. microservices vs. serverless based on real constraints | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/architecture-pattern-selector/SKILL.md) |
| cto-team: assumption-challenger | Stress-tests plans across timeline, resource, technical, business & external | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/assumption-challenger/SKILL.md) |
| cto-team: clarification-protocol | Generates 2-3 sharp questions to cut through vague requirements | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/clarification-protocol/SKILL.md) |
| cto-team: cost-estimator | TCO frameworks with 2024-2025 infra pricing and build-vs-buy analysis | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/cost-estimator/SKILL.md) |
| cto-team: delegation-prompt-crafter | Structures prompts in CONTEXT/TASK/REQUIREMENTS format | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/delegation-prompt-crafter/SKILL.md) |
| cto-team: ml-cv-specialist | ML system design, model selection, API vs. self-hosted, CV pipelines | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/ml-cv-specialist/SKILL.md) |
| cto-team: request-analyzer | Classifies intent and routes to the right specialist | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/request-analyzer/SKILL.md) |
| cto-team: roadmap-generator | MVP → Scale → Advanced roadmaps with epic/story/task breakdowns | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/roadmap-generator/SKILL.md) |
| cto-team: scalability-advisor | 4-stage scaling framework (startup → enterprise) with bottleneck detection | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/scalability-advisor/SKILL.md) |
| cto-team: tech-stack-recommender | Technology selection across frontend, backend, database, and infra | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/tech-stack-recommender/SKILL.md) |
| cto-team: validation-report-generator | 8-section validation reports with GOOD / NEEDS MAJOR WORK / BAD verdicts | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/borrowed/cto-team/skills/validation-report-generator/SKILL.md) |

## Templates

Generic skills that work for anyone with minimal or no configuration.

| Skill | Description | Install |
|---|---|---|
| exec-feedback | Template for first-pass document feedback in any executive's voice — configure once, use forever | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/exec-feedback/skills/exec-feedback/SKILL.md) |
| investment-council | Four-voice advisory council (Bull, Bear, Calibrator, CFO) for pressure-testing investment deals with independent takes, rebuttals, and synthesis | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/investment-council/skills/investment-council/SKILL.md) |
| investor-profile | Decision-ready intelligence on investors, funds, and angels — thesis, portfolio, deal mechanics, partner backgrounds, and meeting prep | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/investor-profile/skills/investor-profile/SKILL.md) |
| person-profile | Pre-meeting intelligence on an individual — career narrative, what they care about, public voice, network influence, and meeting hooks | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/person-profile/skills/person-profile/SKILL.md) |
| prospecting-template | Founder-led outbound: ranked tier list of 25 peers from anchor companies, product-fit scoring, warm paths via LinkedIn + VouchFor, personalized pitch hooks | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/prospecting-template/skills/prospecting-template/SKILL.md) |

### Research Assistant (15 sub-skills)

Multi-agent research orchestrator. Each sub-skill is a structured research type with opinionated frameworks that produce decision-ready output.

| Skill | Description | Install |
|---|---|---|
| research-assistant: research | Orchestrator — routes to the right research type and runs parallel agents | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/research/SKILL.md) |
| research-assistant: competitive-analysis | Competitor positioning, moats, and Signal vs. Noise framework | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/competitive-analysis/SKILL.md) |
| research-assistant: industry-trend | Industry momentum, tailwinds/headwinds, Momentum framework | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/industry-trend/SKILL.md) |
| research-assistant: market-sizing | TAM/SAM/SOM with TAM Skepticism framework | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/market-sizing/SKILL.md) |
| research-assistant: analog-mapping | Find companies that solved structurally similar problems | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/analog-mapping/SKILL.md) |
| research-assistant: build-buy-partner | Build vs. buy vs. partner decision framework | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/build-buy-partner/SKILL.md) |
| research-assistant: company-deep-dive | Business Model Anatomy and full company profile | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/company-deep-dive/SKILL.md) |
| research-assistant: company-financials | Financial analysis from public data | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/company-financials/SKILL.md) |
| research-assistant: technology-landscape | Tech stack analysis and vendor landscape | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/technology-landscape/SKILL.md) |
| research-assistant: regulatory-landscape | Regulatory risk, compliance landscape, and jurisdiction mapping | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/regulatory-landscape/SKILL.md) |
| research-assistant: due-diligence | Structured DD for investment or partnership decisions | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/due-diligence/SKILL.md) |
| research-assistant: person-profile | Background, career arc, and POV synthesis on a specific person | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/person-profile/SKILL.md) |
| research-assistant: ecosystem-map | Map vendors, players, and relationships in a market | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/ecosystem-map/SKILL.md) |
| research-assistant: synthesis | Synthesize outputs from multiple research runs into one doc | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/synthesis/SKILL.md) |
| research-assistant: eval | Evaluate and score a vendor, partner, or solution | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/research-assistant/skills/eval/SKILL.md) |

### Strategy Feedback (5 sub-skills)

Strategy pressure-testing toolkit with advisory councils, classic frameworks, and competitive intel context. Configure once per company.

| Skill | Description | Install |
|---|---|---|
| strategy-feedback: strategy-orchestrator | Session orchestrator — routes strategy questions to the right council or framework | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/template-strategy-feedback/skills/strategy-orchestrator/SKILL.md) |
| strategy-feedback: strategy-council | Advisory council that stress-tests strategy from multiple senior personas | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/template-strategy-feedback/skills/strategy-council/SKILL.md) |
| strategy-feedback: buyer-persona-council | Buyer persona council for GTM and positioning pressure-testing | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/template-strategy-feedback/skills/buyer-persona-council/SKILL.md) |
| strategy-feedback: competitive-intel | Competitive context loader with structured company profile templates | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/template-strategy-feedback/skills/competitive-intel/SKILL.md) |
| strategy-feedback: strategy-frameworks | 14 classic strategy frameworks (Porter's Five Forces, Seven Powers, Blue Ocean, JTBD, etc.) | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/templates/template-strategy-feedback/skills/strategy-frameworks/SKILL.md) |

---

## Playbooks

Personal plugins and reusable workflows. Unlike `templates/`, the contents of `playbooks/` are not meant to be referenced as generic marketplace plugins — they're CK-specific or require meaningful per-user configuration.

### Personal plugins

| Plugin | Description | Install |
|---|---|---|
| family-assistant | Persistent family logistics assistant — load family context once, surface dietary, medical, travel, and activity considerations automatically | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/playbooks/family-assistant/skills/ck-family/SKILL.md) |
| professional-voice | Template for a per-person voice skill — fill in your patterns once, every future draft lands in your voice instead of generic AI | [SKILL.md](https://raw.githubusercontent.com/ckoglmeier/skills/main/playbooks/professional-voice/skills/professional-voice/SKILL.md) · [README](https://github.com/ckoglmeier/skills/blob/main/playbooks/professional-voice/README.md) |

### Reusable workflows

Prompts and how-to guides. Not Claude Code plugins — copy-paste into any session.

| Playbook | Description |
|---|---|
| [weekly-skill-discovery](https://github.com/ckoglmeier/skills/blob/main/playbooks/weekly-skill-discovery.md) | Weekly workflow for scanning your recent activity, finding automation candidates, and building new skills end-to-end with evals |

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
