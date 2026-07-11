# T.E.S.T. Output Contract

Choose the smallest format that supports the decision. The source and claim ledgers are working artifacts; the final answer should be readable without them.

## Universal requirements

Every final output must include:

- a direct answer or an explicit statement that evidence is insufficient;
- scope and freshness when they materially affect the answer;
- claim-level citations for important factual statements;
- visible separation of fact, inference, and recommendation;
- material contradictions and uncertainty;
- a practical next step;
- the date or period through which current information was verified.

## A. Rapid research answer

Use for `quick` mode.

```markdown
## Answer
[Direct answer in 2–5 sentences, with citations.]

## Why
[Two to four decision-driving findings.]

## Caveats
[Material uncertainty, scope, and verification date.]

## Sources
[Short source list if native inline citations are unavailable.]
```

## B. Decision brief

Default for `standard` mode.

```markdown
# [Decision or question]

**Scope:** [population/geography/version/time period]  
**Last verified:** [YYYY-MM-DD]  
**Confidence:** [high / medium / low, with one-line reason]

## Executive answer
[Answer and recommendation.]

## Decision-driving findings
1. **[Finding]** — [evidence and citation]
2. **[Finding]** — [evidence and citation]
3. **[Finding]** — [evidence and citation]

## Options and trade-offs
| Option | Best for | Evidence-backed strengths | Risks / limitations |
|---|---|---|---|

## Contradictions and uncertainty
[What disagrees, why, and how it affected confidence.]

## Recommendation
[Action, conditions, and fallback.]

## What could change this conclusion
[Most decision-relevant missing or future evidence.]

## Sources
[Source IDs with titles, publishers, dates, and URLs/identifiers.]
```

## C. Comparison matrix

Use only after normalizing units, time periods, tiers, and geography.

```markdown
| Criterion | Weight/importance | Option A | Option B | Evidence |
|---|---:|---|---|---|
```

Do not invent weights. Ask for them or state them as assumptions. Avoid false precision: use qualitative ratings when the evidence does not support exact scores.

## D. Literature or evidence review

```markdown
## Review question and scope
## Search and selection approach
## Evidence map
## Findings by theme
## Quality and limitations
## Conflicting results
## Gaps
## Conclusion
## Included sources
```

Do not call a review “systematic” unless the protocol, search coverage, inclusion criteria, and reproducibility justify that term.

## E. Fact-check

```markdown
## Claim
[Exact claim.]

## Verdict
[Supported / Misleading / Contested / Unsupported / Unverifiable]

## Evidence
[Atomic subclaims and direct sources.]

## Context
[Definitions, dates, denominator, omitted qualifiers.]

## Confidence and limitations
[What remains uncertain.]
```

Avoid a binary true/false label when the claim mixes accurate and inaccurate elements.

## Citation fallback

When the client has no native citation syntax:

- cite source IDs inline, e.g. `[S001]`;
- place the citation immediately after the supported claim;
- list sources in this format:

```markdown
- **[S001]** Publisher. “Title.” Published/effective YYYY-MM-DD.
  Retrieved YYYY-MM-DD. URL or stable identifier.
```

Do not cite a source that was only discovered but not inspected.

## Confidence language

Use calibrated language:

- High: “The evidence consistently shows…”
- Medium: “The available evidence suggests…”
- Low: “Limited evidence indicates…”
- Contested: “Credible sources disagree…”
- Inference: “Taken together, these sources imply…”

Avoid “proves,” “definitive,” “everyone agrees,” or “no risk” unless the evidence truly warrants it.
