# Family Assistant — Claude Skill

A persistent family context skill for [Claude Code](https://claude.ai/code) and [Cowork](https://claude.ai). Set it up once. From then on, Claude carries your family's logistics — dietary needs, medical considerations, travel preferences, activity interests, pet care — into every relevant conversation automatically.

No more re-explaining that someone is gluten-free, that a child has medical equipment, or that you prefer houses over hotels. The skill loads the context and surfaces the right considerations without being asked.

---

## What It Does

Once set up, the Family Assistant skill:

- Surfaces dietary restrictions whenever food, restaurants, or meals come up
- Includes relevant medical gear in every packing list
- Flags activities or environments that conflict with documented needs (medical, sensory, accessibility)
- Adjusts recommendations for infants, young kids, or teenagers automatically
- Reminds you about pet care when you're planning travel
- Defaults to your preferred airlines, loyalty programs, and accommodation types
- Weights activity recommendations toward what your family actually enjoys
- Optionally keeps your financial goals and life priorities in view for major decisions

---

## Files

```
ck-family/
├── SKILL.md            ← Skill logic and behavior rules (Claude reads this)
└── family-context.md   ← Your family data (populated during setup, you can edit directly)
```

---

## Installation

### Claude Code

1. Copy the `ck-family/` folder into your Claude skills directory:
   ```
   ~/.claude/skills/ck-family/
   ```

2. That's it. The skill will be available in any Claude Code session.

### Cowork (Desktop App)

1. In your selected workspace folder, create a `.claude/skills/` directory if it doesn't exist.

2. Copy the `ck-family/` folder into `.claude/skills/`:
   ```
   [your workspace]/.claude/skills/ck-family/
   ```

3. The skill will be available the next time you open a Cowork session in that workspace.

---

## First-Run Setup

The first time Claude loads this skill, it will detect that setup hasn't been completed and run a **guided interview**. The interview covers:

1. **Family members** — names, roles, ages, dietary needs, medical conditions
2. **Pets** — species, travel habits, care arrangements
3. **Home base & recurring locations** — primary residence, seasonal homes, frequently visited places
4. **Travel preferences** — accommodation type, preferred airlines, loyalty programs, constraints
5. **Interests & activity profile** — what the family enjoys, what to avoid
6. **Financial context & life goals** *(optional)* — for families who want help thinking through major decisions

The interview takes about 5 minutes. Answers are saved to `family-context.md` and reloaded automatically in every future session.

---

## Triggering the Skill

The skill loads automatically when Claude detects a family-related request. Triggers include:

- Mentioning a family member by name
- Asking about travel, trips, or packing
- Planning meals, restaurants, or activities
- Discussing schedules, accommodations, or logistics
- Mentioning your home, a seasonal location, or a recurring destination

You can also trigger it explicitly by saying: *"load my family context"* or *"use my family assistant skill."*

---

## Updating Your Context

Life changes. To update the skill:

**Tell Claude directly:**
> "My daughter is now on a dairy-free diet."
> "We got a new dog — his name is Biscuit."
> "We moved to Austin."

Claude will update `family-context.md` immediately.

**Re-run a section of the interview:**
> "Update my travel preferences."
> "Let's redo the medical section."

**Edit the file manually:**
Open `family-context.md` in any text editor. The format is plain Markdown. Make your changes and save. Claude will pick them up the next time it loads the skill.

**Re-run the full setup:**
Change `SETUP_COMPLETE: false` in `family-context.md` and reload. Claude will run the full interview again.

---

## Privacy

Your family data lives in `family-context.md` on your local machine (or your selected workspace folder). It is not sent to any server independently — it's loaded into your Claude session the same way any other file would be.

Do not commit `family-context.md` to a public repository. If you're sharing this skill on GitHub, add `family-context.md` to your `.gitignore`.

```
# .gitignore
family-context.md
```

---

## Customization

The skill is designed to be modified. Common customizations:

- **Add recurring planning prompts** — e.g., always suggest checking school calendars before recommending travel dates
- **Add domain-specific context** — e.g., a section for elder care logistics, special education IEP details, or religious/cultural observances
- **Adjust the trigger description** in `SKILL.md`'s frontmatter to match your family's vocabulary or locations
- **Extend the financial section** with more structured frameworks if you want the skill to assist with investment or career decisions

---

## Credits

Built as a generic family planning skill template. Designed for use with [Claude Code](https://claude.ai/code) and [Cowork](https://claude.ai).

Contributions welcome. Open an issue or PR if you've made an improvement worth sharing.
