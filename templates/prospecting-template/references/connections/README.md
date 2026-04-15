# LinkedIn Connections — Setup Instructions

This folder holds LinkedIn connection exports for each founder. The skill uses them to flag warm paths and assign the right sender to each outreach.

## How to add your connections

1. Go to LinkedIn → Settings → Data Privacy → Get a copy of your data
2. Select "Connections" and request the export
3. Download the CSV when LinkedIn emails you the link (usually within 10 minutes)
4. Rename it to match the founder (e.g., `alice.csv`, `bob.csv`) and drop it here

## CSV format

LinkedIn exports a file with a two-row header (a notes paragraph + the column row). The skill handles this automatically — just drop in the raw export as-is. The relevant fields are:

```
First Name, Last Name, URL, Email Address, Company, Position, Connected On
```

## What the skill does with it

For each prospect company, the skill searches the CSV for anyone currently listed at that company and flags:
- Which founder is connected
- How long they've been connected (recency affects warmth)
- Whether they match the target buyer title

A direct connection at the target company moves that prospect to Tier 1 regardless of fit score.

## VouchFor (additional layer)

The skill also queries the VouchFor network for each prospect company using `lookup_network`. This surfaces vouched recommendation paths that go beyond LinkedIn — people who can make a warm intro with an implicit endorsement. VouchFor is additive; the skill works without it.

## Placeholder files

Add a file per founder using any filename that makes sense for your team. Update the sender assignment table in `references/icp.md` to map each file to the right person.
