# Claim Ladder

Use this ladder to calibrate language.

## Status Labels

- `proven`: Direct evidence supports the claim in the exact stated scope against a meaningful baseline.
- `suggested`: Evidence points in the direction of the claim, but scope, sample size, baseline, or method is not yet strong enough.
- `not_shown`: The evidence does not address the claim, even if the claim may still be true.
- `contradicted`: Evidence cuts against the claim.
- `needs_more_evidence`: The claim could be supported, but the current artifact is missing key context.

## Language Mapping

| Evidence strength | Use | Avoid |
|---|---|---|
| Strong direct evidence | shows, demonstrates, validates in X setting | proves universally |
| Narrow direct evidence | shows in this domain, works on this benchmark | generalizes, establishes |
| Early/noisy evidence | suggests, points toward, is consistent with | shows, proves |
| Failure with useful signal | narrows the thesis, redirects the next test | failed, disproves, validates |
| Missing evidence | does not yet show, remains unproven | confirms, indicates |

## Audit Prompts

- What exactly happened?
- Compared to what?
- In what scope or domain?
- Was the success criterion known before the result?
- What would a skeptic say caused the result?
- What stronger claim is tempting but unsupported?
- What single test would make the claim meaningfully stronger?

## Common Overreach Patterns

- Turning a static eval into a live workflow claim.
- Turning one domain into a cross-domain claim.
- Treating "can learn examples" as "can operate robustly."
- Treating a product demo as customer proof.
- Treating cost reduction in one path as platform-wide efficiency.
- Treating absence of failure as evidence of safety.
