---
name: revenue-intelligence
description: >
  AI-powered revenue analytics suite. Analyzes Gong sales call transcripts for
  objections, buying signals, competitive mentions, and pricing discussions. Maps
  content pieces to closed deals using GA4 + HubSpot attribution (first-touch, linear,
  time-decay). Generates unified client reports combining GA4, HubSpot, Ahrefs, and
  Gong with anomaly detection.

  Use for: call analysis, content ROI attribution, revenue reporting, client dashboards.
---

# AI Revenue Intelligence

## Primary Tools

### Gong-to-Insight Pipeline
Analyzes sales call transcripts to identify objections, buying signals, competitive mentions, and pricing discussions. Can process local files or pull directly from the Gong API, outputting structured JSON insights.

### Revenue Attribution Mapper
Connects content pieces to closed deals using GA4 and HubSpot data. Supports multiple attribution models:
- **First-touch** — credit to first content interaction
- **Linear** — equal credit across all touchpoints
- **Time-decay** — more credit to recent touchpoints

Calculates cost-per-acquisition metrics to demonstrate content ROI.

### Multi-Source Client Report Generator
Creates unified reports combining data from GA4, HubSpot, Ahrefs, and Gong. Reports can be exported as markdown or JSON with optional anomaly detection.

## Recommended Cadence

- **Weekly:** Call transcript analysis for objection patterns
- **Monthly:** Content ROI reporting and attribution analysis
- **Quarterly:** Gap analysis to identify missing content in the buyer journey

## Configuration

Setup requires environment variables for API access:
- `GONG_API_KEY` — Gong API credentials
- `HUBSPOT_API_KEY` — HubSpot private app token
- `GA4_PROPERTY_ID` — Google Analytics 4 property
- `AHREFS_API_KEY` — Optional, for SEO data enrichment

## Privacy

Remote telemetry is opt-in only. No code, file paths, or repo content is ever collected. Usage logged locally to `~/.ai-marketing-skills/analytics/`.
