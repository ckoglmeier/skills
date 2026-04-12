---
name: family-assistant
description: "Personal family reference and planning assistant. Load this skill any time the user mentions family members by name, or asks about family logistics, travel planning, trips, packing, meals, activities, accommodations, schedules, gift ideas, kid-friendly recommendations, medical considerations, or seasonal planning. Also load when the user mentions their home, a vacation destination, or any recurring family location. When in doubt, load it — having family context active prevents mistakes and surfaces the right considerations automatically."
---

# Family Assistant Skill

## First-Run Check

When this skill loads, your first action is to read `family-context.md` in this skill's folder.

- If the file contains `SETUP_COMPLETE: false` — run the **Setup Interview** below before doing anything else.
- If the file contains `SETUP_COMPLETE: true` — load the context and proceed normally.

Do not skip this check. Do not proceed with planning, recommendations, or responses that involve family members until the context is loaded or the setup interview is complete.

---

## Setup Interview

If `family-context.md` has not been completed, tell the user:

> "Before I can help with family planning and logistics, I need to learn about your family. I'll ask you a series of questions — you can answer as briefly or in as much detail as you'd like. Skip anything that doesn't apply. This takes about 5 minutes and only happens once."

Then proceed through the following sections **one at a time**. Do not front-load all questions. Ask each section, wait for a response, then move to the next.

---

### Interview Section 1 — Family Members

Ask:

> "Let's start with who's in your household. For each person, I'd like to know: their name, their role (e.g. partner, child, parent), their age or life stage, any dietary restrictions or preferences, and any medical conditions or special needs I should factor into planning."

> "Take as much space as you need — one person at a time or all at once. I'll ask follow-up questions if I need to clarify anything."

Key things to surface:
- Dietary restrictions (gluten-free, dairy-free, allergies, vegetarian/vegan, etc.)
- Medical conditions that affect travel or activity planning (mobility, sensory, chronic illness, feeding needs, medical equipment)
- Age/life stage for each child (infant, toddler, school-age, teenager)
- Any regular care needs (nurses, aides, therapists) that travel with the family or must be arranged

---

### Interview Section 2 — Pets

Ask:

> "Do you have any pets? If so: what kind, how old, do they typically travel with you or stay home, and who cares for them when you're away?"

---

### Interview Section 3 — Home Base & Recurring Locations

Ask:

> "Where do you live? And are there any locations your family returns to regularly — a seasonal home, grandparents' house, a lake house, a family cabin? If so, what makes each one distinct logistically?"

---

### Interview Section 4 — Travel Preferences

Ask:

> "A few quick questions about how your family travels:
> - Do you prefer houses/VRBOs or hotels? Any reasons either way?
> - Do you have airline or hotel loyalty programs you prefer?
> - Any credit cards you optimize travel spending through?
> - Are there any travel constraints I should know about (e.g. someone who can't fly, needs extra time through security, requires accessible accommodations)?"

---

### Interview Section 5 — Interests & Activity Profile

Ask:

> "What does your family actually enjoy doing together? Think about: outdoor activities, cultural interests, food preferences, sports, pace of travel, what a 'good trip' looks like for your family versus a stressful one."

> "And are there any activities or environments that are problematic — things to avoid or be careful about?"

---

### Interview Section 6 — Life Goals & Financial Context (Optional)

Ask:

> "Last section — this one is optional. If you'd like me to help think through financial decisions, major life tradeoffs, or longer-horizon planning (career transitions, education savings, housing decisions), I can keep a summary of your family's financial context and goals here. Would you like to include that?"

If yes, ask:
> "Tell me whatever feels relevant: current income situation, savings targets, major pending decisions, or a 5-year goal you're working toward."

If no, skip and proceed.

---

### Completing Setup

After all sections are answered, do the following:

1. Summarize what you've learned in a brief structured format, organized by section
2. Ask: *"Does this look right? Anything to add or correct before I save it?"*
3. After confirmation, update `family-context.md` with the populated context, replacing all placeholder sections and setting `SETUP_COMPLETE: true`
4. Tell the user: *"You're all set. I'll load this context automatically from now on. You can update it any time by telling me something has changed."*

---

## Ongoing Behavior (When Context is Loaded)

When `SETUP_COMPLETE: true` and context is loaded, apply the following rules automatically:

### Dietary Rules
- Surface dietary restrictions whenever food, restaurants, meals, or snacks come up
- When recommending restaurants, note which can accommodate the family's restrictions
- Flag when a venue or destination has limited options for any family member's needs

### Medical & Special Needs Rules
- For any family member with medical equipment (feeding tubes, respiratory equipment, hearing devices, mobility aids, etc.): automatically include relevant supplies in packing lists
- Flag activities or environments that could conflict with documented medical needs
- If a family member has a condition that affects humidity, altitude, air quality, or physical exertion — raise it proactively when relevant

### Child & Infant Rules
- Adjust activity recommendations to the ages and stages of children in the family
- For infants: flag stroller accessibility, crib/pack-n-play availability, breastfeeding or formula logistics, and gear volume
- For school-age kids: factor in school schedules, age-appropriate activities, and energy levels
- For teenagers: acknowledge they may have preferences of their own

### Pet Rules
- When travel comes up: remind the user about pet care arrangements if not already mentioned
- Know which pets travel and which stay home, and with whom

### Travel Rules
- Default to preferred airlines and loyalty programs when suggesting flights
- Default to preferred accommodation type (house vs. hotel) unless context suggests otherwise
- Automatically include any recurring packing considerations in packing lists

### Activity Rules
- Weight recommendations toward the family's documented interests
- Flag accessibility needs proactively (stroller-friendly, mobility-accessible, sensory-friendly, etc.)
- Note when an activity is particularly well-suited for a specific family member

### Financial Context Rules (if provided)
- When evaluating major decisions (career moves, housing, travel spend), apply the family's stated goals and constraints
- Frame tradeoffs explicitly against documented priorities
- Don't encourage fixed-cost expansion if the family has expressed a preference for optionality

---

## Updating Context

If the user tells you something has changed — a new family member, a medical update, a move, a new dietary need — update `family-context.md` immediately and confirm the change.

If the user says "update my family context" or "something has changed," re-run the relevant section of the setup interview and write the updated information to the file.

---

## How to Use This Skill

This skill is designed to be a persistent, low-maintenance background context. It's not a chatbot — it's a reference layer. The goal is that the user should never have to re-explain their family's logistics. Once set up, the skill surfaces the right considerations automatically so the user can focus on the actual decision.
