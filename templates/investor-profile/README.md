# Investor Profile Skill

Builds decision-ready intelligence on investors, funds, angels, and potential acquirers for meeting prep or firm evaluation.

## Current capabilities

- Web research across Crunchbase, PitchBook, Tracxn, firm websites, Twitter/X, podcasts, and news, run as parallel threads (cheap model for retrieval, strong model for scoring and prep)
- Investor mode and Acquirer mode (strategic buyers, PE-backed firms, consultancies), each with its own 30-point fit score
- Dual-mode: meeting prep (rapport + positioning) or firm evaluation (thesis alignment + deal mechanics)
- Warm intro paths via the `team-connections` skill, plus any connected CRM, email, or network tools
- Handles both institutional firms (multi-partner VC, growth equity) and individual investors (angels, solo GPs)
- Structured output: header block, thesis analysis (revealed vs. stated), partner profiles with public voice, deal mechanics, relationship mapping, and meeting prep brief

## Optional: LinkedIn MCP integration

**Repo:** https://github.com/stickerdaniel/linkedin-mcp-server

This open-source MCP server provides authenticated LinkedIn access via browser automation. When connected, it would upgrade the skill's data quality significantly — especially for partner profiles, recent activity, and relationship mapping.

### What it adds

| Tool | What it provides for this skill |
|------|------|
| `get_person_profile` | First-party career data, skills, recent posts, contact info. Posts are the highest-signal source for current thinking and thesis evolution. |
| `get_company_profile` | Firm identity, company posts (portfolio highlights, thesis signaling), and open roles (hiring signals reveal thesis direction better than websites). |
| `search_people` | Discover full partner roster at a firm, then pull individual profiles for each. |
| `get_sidebar_profiles` | Surface related investors and potential co-investor relationships from LinkedIn's recommendation engine. |
| `get_company_posts` | Recent firm-level content — portfolio announcements, event participation, thought leadership. |

### How to install

**Prerequisites:** `uv` (Python package manager)

```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.local/bin/env

# First run — opens browser for LinkedIn login (supports 2FA)
uvx linkedin-scraper-mcp@latest --login

# If uvx not on PATH, use direct path
~/.local/bin/uvx linkedin-scraper-mcp@latest --login
```

**Claude Desktop config** (`~/Library/Application Support/Claude/claude_desktop_config.json on macOS; or `claude mcp add` for Claude Code`):

```json
{
  "mcpServers": {
    "linkedin": {
      "command": "uvx",
      "args": ["linkedin-scraper-mcp@latest"],
      "env": { "UV_HTTP_TIMEOUT": "300" }
    }
  }
}
```

Restart Claude Desktop after adding the config.

### How the skill uses it

The skill checks for LinkedIn tools at the start of research. When they're present it:

1. Uses `get_person_profile` as the primary source for individual investor profiles (request sections: `experience`, `education`, `skills`, `posts`, `contact_info`, `certifications`, `interests`)
2. Uses `get_company_profile` with `posts` and `jobs` for firm profiles
3. Uses `search_people` to discover the partner roster before pulling individual profiles
4. Uses connection/endorsement data for warm intro path mapping
5. Promotes LinkedIn to source priority #1 (above web search) when available
6. Falls back gracefully to web search when the MCP is not connected

### Caveats

- LinkedIn ToS technically prohibits automation. Low-volume use (a few profiles before meetings) is safe; bulk scraping is not.
- The MCP controls a real Chromium browser — first launch requires manual login.
- Sessions can expire; re-authenticate with `--login` flag when needed.
- No built-in rate limiting — keep usage reasonable.

---

Partner's name typed,
Their map unfolds like a deck —
Warm intro, warm room.

— from CK's desk
