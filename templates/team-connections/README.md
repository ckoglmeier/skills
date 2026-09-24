# Team Connections

"Who do we know at X?" answered across everyone's network at once — founders, teammates, board members, advisors. Drop each person's LinkedIn connections export into one folder and the skill returns tiered warm paths (🟢 Direct, 🟣 Vouched, 🟡 One hop, ⚪ Cold), the best connector, and who should send.

- Works on LinkedIn CSV exports alone; enriched datasets and network tools (VouchFor, a CRM) are optional add-ons.
- A bundled Python script (standard library only) does the matching, so it's fast and deterministic even across tens of thousands of connections.
- Your data lives in `~/.claude/skill-data/team-connections/`, never in the skill folder or a repo.

Used as the connection-lookup step by `person-profile` and `investor-profile`.

See `skills/team-connections/SKILL.md` for setup and the full workflow.
