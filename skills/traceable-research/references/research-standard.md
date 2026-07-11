# T.E.S.T. Research Standard

Load this reference for `deep` or `high-stakes` work, when sources conflict, or when the task spans several evidence types.

## 1. Evidence is claim-relative

A source is not globally “good” or “bad.” Judge it for the exact claim.

Examples:

- Vendor documentation is strong evidence for a documented API parameter, but weak evidence for real-world reliability.
- A randomized trial may be strong for a narrow intervention and population, but weak for long-term outcomes or a different population.
- A customer review is weak for market-wide prevalence, but useful as a lead for recurring usability problems.
- A statute is primary legal text, while a regulator FAQ may be clearer but can omit nuance.

## 2. Source quality rubric

Score each dimension, then record the total from 0–12. Use the score to prioritize scrutiny, not to automate truth.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Authority | Unknown or clearly unqualified | Relevant but informal | Recognized expert/institution | Canonical authority or original record |
| Directness | Repeats an unsourced claim | Secondary summary | Detailed secondary analysis | Original data, document, observation, or method |
| Recency | Obsolete for the claim | Date unclear or partly stale | Current enough | Current and explicitly version/date matched |
| Method transparency | None | Partial | Reproducible/inspectable | — |
| Independence | Same origin or undisclosed | Possible dependency/conflict | Independent origin and incentives disclosed | — |

Maximum: 12.

Record conflicts of interest separately. A high score does not erase a direct financial or institutional incentive.

## 3. Source hierarchy by task

### Current product or software comparison

Prefer:

1. official pricing, specification, changelog, status, and security pages;
2. independent benchmarks with reproducible methods;
3. issue trackers, incident reports, and user reports for failure modes;
4. reputable reviews for hands-on context;
5. aggregators only for discovery.

Verify plan names, currencies, billing periods, regions, taxes, availability, version, and retrieval date.

### Scientific or technical literature

Prefer:

1. primary studies and datasets;
2. systematic reviews, meta-analyses, standards, and consensus statements;
3. replication or critique;
4. narrative reviews and expert commentary;
5. press coverage only for discovery.

Record peer-review status, study design, sample/population, outcome, effect size, uncertainty, limitations, funding, and whether the evidence generalizes.

### Law, regulation, and policy

Prefer:

1. enacted text, court decisions, regulations, official registers, and regulator publications;
2. authoritative guidance and legislative history;
3. reputable legal analysis;
4. news summaries for context.

Record jurisdiction, effective date, amendments, exceptions, and whether guidance is binding. Do not present general research as personalized legal advice.

### Companies, markets, and news

Prefer:

1. filings, audited reports, official statistics, transcripts, and direct announcements;
2. independent reporting with named evidence;
3. specialist analysis with transparent methods;
4. social posts as leads or direct statements, not independent verification.

Separate event date from publication date. Treat company claims as claims by the company unless independently corroborated.

### Medical, financial, and safety questions

Use `high-stakes` mode. Prefer current official guidance, systematic evidence, and direct records. State limitations and the boundary between general information and professional advice. Do not infer individualized diagnosis, treatment, legal status, or investment suitability without the required professional context.

## 4. Claim states

Use exactly one state per claim:

- `verified` — supported by at least two independent sources, with at least one direct/primary source for a decision-critical claim; no unresolved credible contradiction.
- `supported` — credible evidence exists, but corroboration, directness, or coverage is incomplete.
- `contested` — credible sources materially disagree, or the result is method-sensitive.
- `unverified` — plausible or reported, but inspected evidence is insufficient.
- `inference` — reasoned conclusion derived from cited evidence; the inference itself is not directly stated by a source.

Confidence is separate:

- `high` — strong direct evidence, good agreement, current, and scope-matched.
- `medium` — useful evidence with one or more meaningful limitations.
- `low` — sparse, indirect, stale, conflicting, or weakly matched evidence.

Never map status to confidence mechanically.

## 5. Contradiction protocol

Create a contradiction record whenever two credible sources differ on a material point.

Check in this order:

1. **Identity** — same entity, product, intervention, or policy?
2. **Definition** — same meaning of the term or outcome?
3. **Population** — same users, geography, sample, or eligibility?
4. **Time** — same period, version, effective date, or market condition?
5. **Measure** — same units, denominator, baseline, and methodology?
6. **Provenance** — independent evidence or a shared upstream source?
7. **Correction** — later amendment, erratum, retraction, or changelog?
8. **Incentive** — material conflicts of interest?
9. **Precision** — does one source make a narrower claim that both can satisfy?

Classify the remaining conflict as factual, methodological, definitional, temporal, scope-related, or value-based.

## 6. Research passes and stop conditions

A robust search usually includes:

- discovery/map;
- primary evidence;
- disconfirming evidence;
- recency/update;
- citation-backtracking for decision-critical claims.

Stop when one of these is true:

- the last search pass adds no new decision-relevant claim;
- new sources repeat the same upstream evidence;
- all decision-critical claims have adequate support or are explicitly unresolved;
- the evidence ceiling is reached;
- the agreed budget or deadline is reached.

Document the stop reason. Do not claim exhaustive coverage unless the search space truly permits it.

## 7. High-stakes strengthening

For `high-stakes` work:

- require primary or official evidence for all critical claims;
- seek at least two independent sources when feasible;
- use exact dates, jurisdiction/population, and version;
- include contraindications, exceptions, downside scenarios, and uncertainty;
- distinguish informational synthesis from personalized professional advice;
- state urgent escalation conditions when safety may be involved;
- avoid recommending irreversible action from low-confidence evidence;
- provide a “what to verify with a qualified professional” section.

## 8. Ethical and security limits

- Do not collect unnecessary personal data.
- Do not paste secrets, private tokens, or confidential records into public ledgers.
- Do not run code copied from an untrusted source merely to inspect it.
- Respect access controls and terms; do not bypass paywalls or authentication.
- Use minimal quotations and preserve attribution.
- Record when a source could not be accessed in full.
