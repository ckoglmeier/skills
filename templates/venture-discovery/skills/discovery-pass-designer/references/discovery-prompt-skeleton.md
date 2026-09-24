# Discovery Prompt Skeleton

The canonical section set for evaluating a venture/product concept or any "should this exist, and in what shape" question. Adapt per objective — drop what doesn't apply, add domain-specific sections, reorder so later sections lean on earlier findings. Not every pass needs all of these; a pure market-research pass might use only a–d, a feasibility pass only e/g/k.

Each section decomposes into three legs:
- **Retrieve** — what to search for (facts + sources + dates; do not conclude).
- **Synthesize** — write up what the evidence says (no final call).
- **Judge** — the exact decision the section exists to make, plus any required one-line verdict.

## The sections

**a. Problem & urgency.** Retrieve: who has the pain, how many, how acute, what they do today (the substitutes). Judge: is the pain acute/crisis-driven (painkiller) or chronic-and-tolerated (vitamin), and what does that imply for go-to-market? A vitamin sold to a chronic population is a different company than a painkiller sold at a trigger moment.

**b. ICP & segmentation.** Retrieve: candidate customer segments, sizes, current spend, existing tools. Judge: the sharpest wedge ICP and which choice forecloses which expansion. Name the *payer* explicitly — it is not always the sufferer.

**c. Market sizing.** Retrieve: population counts, price comps, comparable-company revenue ceilings. Judge: bottoms-up SOM (not top-down TAM), sanity-checked against what the closest comps actually earn. Beware TAM that is really a valuation of unpaid labor or an aspirational denominator — those are not liquid dollars.

**d. Competitive & analog teardown.** Retrieve: direct competitors, adjacent players, and — critically — the **graveyard** (dead or stalled attempts at this exact thing). Judge: causal analysis of why the dead ones died; what the survivors' revealed behavior tells you; whether the winning playbook from an analog actually transfers.

**e. Regulatory & legal feasibility.** Retrieve: every regime a feature might trigger (licensing, money transmission, professional liability, privacy, mandatory reporting). Judge: which features trigger which regime; whether a narrower design electively avoids the hard ones; is the risk insurable.

**f. Business model options.** Retrieve: pricing comps and financing shapes/ceilings for the category and its analogs. Judge: the pricing model for the first 12–18 months, and the honest financing shape — venture-scaleable vs. bootstrapped/strategic infrastructure business.

**g. Build vs. partner / buildability.** Retrieve: does the headline mechanic actually exist on current rails/tech? What's shipped, what's brittle, what's unsolved. Judge: buildable-now / buildable-brittle / not-yet, and own-vs-rent for the hard infrastructure. The most dangerous assumption is usually a mechanic the pitch treats as trivial that doesn't exist yet.

**h. Wedge & sequencing.** Judge (often needs no separate retrieval — synthesizes a–g): which single feature ships first, to which single ICP, monetized how, and what is explicitly NOT built in year one even though it's in the brief. Guards against the roll-up trap (breadth before depth).

**i. GTM & distribution.** Retrieve: how comparable companies actually reach the buyer; which channels are open vs. occupied/consolidating. Judge: is channel distribution a prerequisite (i.e. is D2C disqualifying)? Pick the beachhead channel. Distribution is the most common silent killer — every scaled comp usually rides an institutional channel.

**j. Trust, safety & brand.** Retrieve: the failure modes (fraud, disputes, harm) and how incumbents handle them. Judge: the liability/trust posture; where a read-only or bounded design de-risks vs. a full-control design.

**k. Red team.** A single high-effort agent, no delegation. Steelman the case that the concept is a mirage — attack every load-bearing assumption in its strongest form, then test each attack for overreach. Score each attack Fatal / Wounding / Survivable. End by naming precisely what, if anything, survives all attacks — the smallest true version worth building.

**Final — verdict, rubric, plan.** A single high-effort agent. Produces the executive verdict, the scored rubric, the committed wedge/beachhead, pre-committed kill gates, and a concrete near-term discovery plan. See the `venture-concept-discovery` skill's `references/rubric-and-verdict.md` for the exact output structure.

## Section-authoring notes

- **Front-load the settled context.** If the pass inherits prior findings ("the consumer version is already dead"), state them as settled at the top so no leg re-litigates them.
- **Demand a one-liner where a section makes a discrete call** (BUILDABLE-NOW/…, BEACHHEAD = X, Fatal/Wounding/Survivable). One-liners make the report skimmable and force the model off the fence.
- **Order for dependency.** Put buildability and regulatory early if they can kill the whole thing; put wedge/sequencing and the verdict last so they can see everything.
