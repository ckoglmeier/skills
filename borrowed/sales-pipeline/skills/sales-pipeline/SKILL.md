---
name: sales-pipeline
description: >
  Autonomous sales pipeline automation: website visitor identification → intent scoring
  → suppression checks → campaign routing → dead deal resurrection → trigger prospecting
  → self-learning ICP optimization. Integrates with HubSpot, Instantly, and Brave Search.
  Uses machine learning on approval/rejection patterns to continuously refine the ICP.

  Use for: pipeline automation, deal resurrection, visitor intent scoring, ICP refinement.
---

# AI Sales Pipeline

Complete AI-powered sales pipeline automation: website visitor identification → intent scoring → suppression → campaign routing → dead deal resurrection → trigger prospecting → self-learning ICP optimization.

## Core Tools

### RB2B Pipeline Scripts
- **Webhook ingestion server** with intent scoring functionality
- **5-layer suppression checks** for email validation
- **Full pipeline orchestration** combining scoring, suppression, routing, and enrollment

### Deal Intelligence Scripts
- **Dead deal revival** using time decay, contact expansion, and champion tracking
- **Web signal monitoring** for new hires, funding announcements, and job postings
- **ML analyzer** for approval/rejection patterns to optimize ICP

## Data Flow

```
RB2B Webhooks → Intake → Suppression → Instantly (enrollment)
HubSpot CRM → Dead Deal Resurrection Module
Brave Search → Trigger Prospecting
Prospect DB → ICP Learning Recommendations
```

## Configuration

### Required Environment Variables
- `HUBSPOT_API_KEY` — HubSpot private app token
- `INSTANTLY_API_KEY` — Instantly.ai API credentials
- `BRAVE_SEARCH_API_KEY` — Brave Search for trigger prospecting

### Key Customization Points
- Intent scoring patterns
- Agency detection keywords
- Loss reason scoring
- Search queries for trigger prospecting
- Campaign routing configuration

## Setup

Requires Python 3.9+. Copy `.env.example` to `.env` and fill in credentials.

## Privacy

Remote telemetry is opt-in only. No code, file paths, or repo content is ever collected.
