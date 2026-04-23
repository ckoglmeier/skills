# Professional Voice — Template

A skill template for building a per-person "professional voice" skill. Drop it into Claude Code, fill in your own patterns, and every future draft-this-for-me request will sound like you — not like generic AI slop.

## Why this exists

AI writing is uniformly mid. The problem is averaging: the model produces the median of everything it's seen, which erases the specific cadence, word choices, and posture that make your writing yours.

A voice skill fixes that by giving Claude an explicit set of rules about how YOU write. It's small (one file, ~120 lines) and it compounds — every future skill that drafts or edits on your behalf pulls from it automatically.

## Who this is for

- Founders who ghostwrite a lot (Slack, email, LinkedIn posts, strategy docs) and want their own voice preserved
- Execs whose chief of staff drafts for them
- Anyone building agent workflows where drafts land in their voice

## What's in this playbook

- `skills/professional-voice/SKILL.md` — the template. Placeholders are in `[BRACKETS]`. Replace them with your patterns.

## How to customize

1. **Copy the template** to your private skills directory (e.g. `~/.claude/skills/my-voice/SKILL.md`). Rename `professional-voice` to `[yourname]-professional-voice` in the frontmatter.

2. **Gather 10–15 real examples** of your own writing: Slack messages, emails, doc comments, strategy briefs. Paste them into a Claude session and ask: "Extract the specific patterns — sentence length, word choices, punctuation habits, opening patterns, closing patterns, things I consistently avoid."

3. **Fill in the bracketed sections** with what Claude extracted plus your own calibration. Key areas:
   - **Core Instincts** — your writing philosophy in 3–5 rules. Not universal truths; your actual quirks.
   - **Style Rules** — Oxford comma? Em dashes? Sentence length targets? Be specific.
   - **Never list** — phrases you genuinely don't use. The AI-isms are universal; your own never-list makes it personal.
   - **Calibration lines** — 5 real sentences from your own writing that the model can check its ear against.

4. **Test it.** Ask Claude to write a Slack message or email in your voice. If it sounds off, identify what's wrong and add a rule.

5. **Iterate.** Voice skills get better with use. Every time a draft lands wrong, add a rule to prevent the specific failure.

## Companion skills

Voice skills are most useful alongside a **context skill** — a compact summary of your role, team, and current priorities. The context skill tells Claude *what* to say; the voice skill tells it *how*. Together they're cheap to build and dramatically improve every future drafting request.

## Example — CK's voice

This playbook was extracted from Chandler Koglmeier's `ck-professional-voice` skill. The structure (format breakdowns, audience table, self-check) is universal; the specific rules (lead with thesis, em dashes for emphasis, Oxford comma non-negotiable, `[CK TAKE]` flag) are CK's. Yours should be different in the specifics and similar in the shape.

---

*The model writes well.*
*But only you know the way*
*Your own voice should land.*

*— from CK's desk*
