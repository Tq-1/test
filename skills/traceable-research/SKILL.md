---
name: traceable-research
description: Conducts evidence-first research and turns ambiguous questions into source-grounded, decision-ready briefs. Use when the user asks to research, compare, investigate, verify, fact-check, survey literature, evaluate options, analyze current or niche information, or produce a cited report. Especially useful when recency, conflicting sources, uncertainty, or high-stakes claims matter. Do not use for simple stable facts, pure creative writing, or summarizing only user-provided text unless external verification is requested.
license: MIT
compatibility: Works with skills-compatible agents. Web access is recommended for current or external research; bundled Python scripts require Python 3.10+ and use only the standard library.
metadata:
  author: Tq-1
  version: "1.0.0"
  repository: "https://github.com/Tq-1/test"
---

# T.E.S.T. — Traceable Evidence Synthesis Toolkit

Turn a question into a traceable chain:

```text
scope → sources → claims → contradictions → synthesis → audit → decision
```

The objective is not “more links.” The objective is a conclusion whose important factual claims can be traced to direct evidence, whose uncertainties are visible, and whose recommendation follows from the evidence.

## Activation boundary

Use this skill for research, comparison, verification, fact-checking, literature surveys, current-information questions, due diligence, and decision briefs.

Do not activate it for:

- simple, stable facts that need no investigation;
- pure brainstorming or creative writing;
- translation or rewriting;
- summarizing only material supplied by the user, unless external verification is requested;
- tasks where another domain skill already supplies a stricter evidence protocol.

## Non-negotiable rules

1. **Evidence before prose.** Do not draft a confident answer and then search for citations that appear to support it.
2. **Atomic claims.** Split compound statements so each externally verifiable claim can be supported precisely.
3. **Primary before derivative.** Prefer original documentation, datasets, papers, filings, laws, standards, official announcements, and direct records.
4. **No citation laundering.** A secondary article that links to a primary source is not a substitute for reading the primary source.
5. **Snippets are discovery, not evidence.** Search-result text, AI summaries, and social previews may locate a source but do not support a final claim.
6. **Separate fact, inference, and recommendation.** Label inferences and make the reasoning bridge explicit.
7. **Normalize time.** Distinguish publication date, event date, effective date, data period, version, and retrieval date.
8. **Test independence.** Syndicated copies, articles repeating one press release, and multiple pages from one organization are not independent corroboration.
9. **Surface conflict.** Do not average away disagreement. Explain what conflicts, why, and which evidence deserves more weight.
10. **Never invent access.** If a source is unavailable, paywalled, truncated, or not inspected, say so and lower confidence.

## Select a research mode

Default to `standard` unless the task clearly calls for another mode.

| Mode | Use when | Minimum behavior |
|---|---|---|
| `quick` | Low-stakes orientation | Direct sources, current dates, concise uncertainty note |
| `standard` | Most comparisons and reports | Primary evidence, independent challenge search, claim ledger |
| `deep` | Literature review or strategic decision | Broad source map, saturation check, explicit contradiction analysis |
| `high-stakes` | Legal, medical, financial, safety, or irreversible decisions | Official/primary sources, stronger triangulation, limitations and professional-review boundary |

Targets are not quotas. Stop when additional sources no longer change material claims, the evidence ceiling is reached, or the agreed scope is exhausted.

Read [`references/research-standard.md`](references/research-standard.md) for detailed source grading, claim states, domain adaptations, and high-stakes requirements.

## Workflow

### 1. Frame the decision

Extract or state:

- the exact question;
- who will use the answer and what decision it informs;
- geography, population, product tier, or other scope;
- time horizon and required freshness;
- constraints and evaluation criteria;
- desired output form;
- research mode.

Ask at most one clarifying question only when the answer would materially change the research path. Otherwise state reasonable assumptions and proceed.

For multi-source work, initialize a workspace:

```bash
python scripts/init_workspace.py "QUESTION" --mode standard --out research/SLUG
```

### 2. Write the answerability plan

Before searching, define:

- subquestions that together answer the main question;
- claims that would change the recommendation;
- source types most likely to answer each subquestion;
- known ambiguity, terminology, and date/version traps;
- stopping conditions;
- what cannot be concluded from available evidence.

Use `assets/research-plan.md` as the default structure.

### 3. Build a source map

Search in passes rather than one undirected sweep:

1. **Map pass** — establish vocabulary, major actors, canonical documents, and competing positions.
2. **Primary pass** — retrieve original evidence for decision-critical claims.
3. **Challenge pass** — actively seek disconfirming evidence, failures, limitations, retractions, counterexamples, and credible alternatives.
4. **Freshness pass** — verify whether newer data, versions, rules, prices, office-holders, schedules, or corrections supersede earlier material.

Do not let a popular tertiary page define the entire source set.

### 4. Maintain the source ledger

Record every source that may affect the answer in `source-ledger.csv`.

For each source capture:

- stable source ID;
- title, publisher, and URL or identifier;
- source type and whether it is primary;
- publication/effective/data dates;
- retrieval date;
- quality score;
- relevance and limitations;
- conflicts of interest or access limitations.

Grade sources using the rubric in `references/research-standard.md`. Scores guide attention; they do not replace judgment.

### 5. Extract claims, not impressions

Populate `claim-ledger.csv` with one material claim per row.

For each claim record:

- exact claim text;
- claim type;
- status: `verified`, `supported`, `contested`, `unverified`, or `inference`;
- confidence: `high`, `medium`, or `low`;
- supporting source IDs;
- contradictory claim IDs or source IDs;
- caveats and reasoning notes.

A claim is not `verified` merely because two pages repeat it. Corroboration must be independent, and at least one source should be direct or primary for decision-critical claims.

### 6. Reconcile contradictions

When sources disagree:

1. confirm they address the same population, definition, period, version, and metric;
2. compare directness, authority, method transparency, recency, sample size, and incentives;
3. check for later corrections, retractions, amendments, or changed definitions;
4. preserve credible minority evidence;
5. state whether the disagreement is factual, methodological, definitional, temporal, or value-based;
6. lower confidence when the conflict cannot be resolved.

Never hide disagreement behind vague wording such as “sources vary.”

### 7. Derive the answer

Synthesize from the claim ledger, not from memory of browsing.

- Lead with the answer that best fits the evidence and user criteria.
- Explain the few claims that actually drive the conclusion.
- Distinguish observed facts from your inference.
- Make trade-offs explicit.
- Give a recommendation only when the evidence supports one.
- State what new evidence would most likely change the conclusion.

For comparisons, use weighted criteria only when weights come from the user or are stated as assumptions.

### 8. Cite at claim level

Use the host client’s native citation format when available. Otherwise use source IDs such as `[S001]` and include a source list.

A citation must support the exact nearby claim. Avoid:

- one citation after a paragraph containing several unrelated claims;
- citing a homepage when a specific document exists;
- citing a source for a stronger claim than it makes;
- citing the same originating source through multiple intermediaries;
- long quotations when a concise paraphrase is enough.

### 9. Run the audit

For a workspace created by the bundled tool:

```bash
python scripts/audit_research.py research/SLUG --strict
```

Fix all errors. Review every warning. The audit checks structure, IDs, dates, source references, claim-state requirements, and brief citations; it cannot determine truth.

Then perform the human/agent completion gate below.

### 10. Deliver a decision-ready brief

Read [`references/output-contract.md`](references/output-contract.md) and choose the smallest output form that answers the task.

Default structure:

1. **Answer / executive summary**
2. **Key findings**
3. **Evidence and trade-offs**
4. **Contradictions and uncertainty**
5. **Recommendation or next action**
6. **Sources / last verified**

Keep the result proportional to the user’s need. Do not expose the full ledger unless it adds value or the user requests auditability.

## Completion gate

Before delivery, verify:

- [ ] The question, scope, geography, and time horizon are explicit.
- [ ] Current claims include concrete verification dates.
- [ ] Every decision-critical factual claim has direct support.
- [ ] Primary sources were inspected where reasonably available.
- [ ] Source independence was checked.
- [ ] Conflicting evidence was sought and addressed.
- [ ] Facts, inferences, and recommendations are distinguishable.
- [ ] Confidence matches evidence quality and agreement.
- [ ] Unknowns and inaccessible evidence are visible.
- [ ] Citations support the exact claims beside them.
- [ ] The recommendation follows the user’s criteria.
- [ ] The answer states what could change the conclusion.

## High-value gotchas

- Publication date is not necessarily event date or data period.
- “Official” can establish what an organization says, not whether the claim is independently true.
- A peer-reviewed paper can still be weak evidence for a different population or outcome.
- A preprint may be current but not yet peer reviewed; label it.
- Product prices, availability, laws, APIs, schedules, and leadership roles require current verification.
- Review sites may have affiliate incentives; use them for experience signals, not sole support for specifications.
- Absence of evidence is not evidence of absence unless the search space and reporting process make that inference reasonable.
- Consensus language requires evidence about the field, not merely several agreeing sources.
- Numerical comparisons require matching units, denominators, baselines, and time periods.
- A source can be high quality but irrelevant to the exact claim.

## Failure behavior

When the evidence is insufficient:

1. answer the parts that are supportable;
2. mark unresolved claims explicitly;
3. explain what was searched or inspected;
4. identify the missing evidence;
5. provide the safest next step;
6. do not manufacture certainty to satisfy the requested format.
