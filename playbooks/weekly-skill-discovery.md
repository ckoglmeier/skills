# Weekly Skill Discovery + Build

A repeatable workflow for finding and building Cowork skills from your actual work patterns. Run it weekly (or whenever you notice yourself doing the same thing for the third time).

---

## Getting Started

**What you need:** A Cowork session with your Slack and Glean connectors active. The prompt scans your recent activity to find automation candidates, so it works best when it can see what you've actually been doing.

**First time setup:**

1. Open a new Cowork session
2. Make sure your Slack and Glean (or equivalent doc search) MCPs are connected — the discovery phase needs these to scan your recent work
3. If you want the skill discovery to run automatically, set it up as a scheduled task (ask Claude: "schedule this to run every Monday at 9am"). Otherwise, just paste the prompt below into a session whenever you want to run it
4. Select a folder for outputs — this is where your .skill files will land

**What to expect:** The first phase takes 2-3 minutes (scanning your activity). After you pick a candidate, the full build cycle — plan, draft, test, grade, iterate, package — takes 30-60 minutes depending on skill complexity. You stay in the loop at two points: approving the plan, and picking which candidate to build. Everything else runs autonomously.

**Start here if you don't have skills yet:** Before running the discovery prompt, build two foundational skills that make everything else better. First, a **[your-name]-writing-voice** skill — give Claude 10-15 examples of your actual writing (Slack messages, emails, doc comments, strategy briefs) and have it extract your tone, sentence patterns, and style rules. Second, a **[your-name]-context** skill — a compact summary of your role, team, priorities, key people you work with, and what you're currently working on. These two skills are small (each takes ~15 minutes to build) and they compound: every future skill that drafts in your voice or needs to understand your work context will pull from them automatically. Once you have those, the discovery prompt below will produce dramatically better results because the skills it builds will already know how you write and what you care about.

**Tips from experience:**

- The best skill candidates are workflows you've done 3+ times where you catch yourself thinking "I did this exact thing last week." Multi-step chains (running 3 tools in sequence, applying the same review framework to different inputs) are higher-value than single-step automations.
- The with/without comparison in step 4 is the quality gate. If the skill doesn't demonstrably beat the no-skill baseline, it's not worth shipping. Don't skip this.
- The real-world test in step 6 is where the best improvements come from. Synthetic test cases miss the messy edges of real data — missing fields, ambiguous inputs, formats you didn't anticipate.
- Your first skill will take the longest. After that, you develop intuition for what makes a good SKILL.md and the cycle gets faster.

---

## The Prompt

> Scan my recent work and do two things:
>
> **Part 1: Suggest updates to existing skills.** Look at how I've used my current skills in the last 7 days. For each skill I used, check: did it miss something? Did I have to manually fix or supplement its output? Did the real-world input expose a gap the skill doesn't handle? If so, name the skill, describe the gap in one sentence, and propose the specific edit. Present these first.
>
> **Part 2: Suggest new skill candidates.** Look at the last 7 days — Slack activity, docs I've shared or reviewed, tools I've used, and any workflow I've done manually more than twice that isn't covered by an existing skill. For each candidate, name it, rate it High/Medium/Low based on (time saved per use × frequency per week), and describe what the skill would automate in one sentence. Present the top 3-5 candidates.
>
> Ask me which updates to make and/or which new skill to build.
>
> **For skill updates**, make the edit, run a quick before/after test on the case that surfaced the gap, and repackage the .skill file.
>
> **For new skill builds**, follow this process — in order, no shortcuts:
>
> 1. **Show me a plan before you build.** Outline the skill's phases, what inputs it expects, what it produces, and which existing skills it chains or references. Get my sign-off before writing anything.
> 2. **Draft the skill.** Create a SKILL.md with a references/ directory. Use progressive disclosure — the SKILL.md orchestrates, the reference files hold the details.
> 3. **Create 2 test scenarios** that stress-test different failure modes. One should be a strong input where the skill should shine. One should be a tricky input that tests edge cases — missing data, ambiguous inputs, or a case where the right answer is "no."
> 4. **Run evals with and without the skill.** For each test scenario, produce output two ways: once following the skill's full pipeline, once doing your best without it. The with-skill version must be demonstrably better on every dimension that matters.
> 5. **Grade the delta.** Write 3-5 assertions per test scenario (specific, binary, single-run gradeable — no comparatives across runs). Score both versions. If the with-skill version doesn't beat the without-skill version, fix the skill and re-run.
> 6. **Run one real-world test** if possible. Use actual data from my work — a real doc, a real deal, a real request — not just the synthetic scenarios. This is where the best improvements surface.
> 7. **Iterate.** Fix what the evals and real-world test surfaced. Re-run until the skill passes.
> 8. **Package it** as a .skill file and deliver it.
>
> Throughout: don't over-engineer the first version. Ship something tight, test it against reality, and improve from there. The iteration loop matters more than the first draft.
