# T.E.S.T. — Traceable Evidence Synthesis Toolkit

<p align="center">
  <strong>Turn vague questions into source-grounded, decision-ready briefs.</strong><br>
  A universal Agent Skill for research, comparison, verification, literature review, and current-information analysis.
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.en.md">English</a> ·
  <a href="skills/traceable-research/SKILL.md">Skill instructions</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent%20Skills-compatible-111827">
  <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776AB">
  <img alt="Dependencies" src="https://img.shields.io/badge/dependencies-zero-success">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
</p>

---

## Why T.E.S.T.?

Most weak research answers fail before the writing starts. They search without a plan, treat snippets as evidence, cite secondary summaries instead of original sources, hide conflicting evidence, or attach citations after drafting.

**T.E.S.T.** makes the research process explicit and auditable:

```text
Question → Scope → Source map → Source ledger → Claim ledger
         → Contradiction check → Citation audit → Decision-ready brief
```

It is intentionally domain-neutral. Use it for:

- product and tool comparisons;
- scientific or technical literature surveys;
- market, policy, company, and industry research;
- fact-checking and claim verification;
- travel, hobby, and personal decision research;
- any task where recency, uncertainty, or conflicting sources matters.

## What makes this a real Skill

- **Precise activation rules:** strong “use when” and “do not use when” boundaries.
- **Repeatable procedure:** a ten-stage workflow with stop conditions and quality gates.
- **Evidence model:** source quality, claim status, independence, recency, and contradiction handling.
- **Reusable tooling:** zero-dependency Python scripts to create a workspace and audit the result.
- **Progressive disclosure:** concise core instructions plus focused references and templates.
- **Evaluation assets:** trigger tests and output-quality cases in English and Chinese.
- **Cross-client packaging:** Agent Skills layout plus Claude and Codex plugin manifests.
- **CI validation:** automated tests for scripts, manifests, references, and Skill structure.

## Quick start

### Open Skills CLI

```bash
npx skills add Tq-1/test --skill traceable-research
```

### Claude Code

```text
/plugin marketplace add Tq-1/test
/plugin install traceable-research@tq1-skills
```

### Codex

```bash
codex plugin marketplace add Tq-1/test
```

Then open the plugin directory, search for **T.E.S.T.**, and install it.

### Manual installation

Copy the self-contained [`skills/traceable-research`](skills/traceable-research) directory into the skills directory used by your agent.

## Use it

Invoke the Skill directly or describe a research task naturally:

```text
Use T.E.S.T. to compare local-first note-taking apps for a research team.
Separate verified facts from inference, include current pricing dates, and recommend one.
```

For a multi-source task, initialize a research workspace:

```bash
python skills/traceable-research/scripts/init_workspace.py \
  "Which local-first note app best fits a five-person research team?" \
  --mode standard \
  --out research/note-apps
```

After filling the ledgers and brief, run the audit:

```bash
python skills/traceable-research/scripts/audit_research.py research/note-apps --strict
```

Validate the repository itself:

```bash
python skills/traceable-research/scripts/validate_skill.py .
python -m unittest discover -s tests -v
```

## Research modes

| Mode | Best for | Default evidence target |
|---|---|---|
| `quick` | Orientation and low-stakes questions | A small set of direct, recent sources |
| `standard` | Most comparisons and reports | Primary sources plus independent challenge sources |
| `deep` | Literature reviews and strategic decisions | Broad coverage, explicit saturation and contradiction analysis |
| `high-stakes` | Legal, medical, financial, safety, or irreversible decisions | Primary or official evidence, stronger triangulation, explicit limitations |

Source counts are targets, not quotas. T.E.S.T. stops when additional searching no longer changes the conclusion, when the evidence ceiling is reached, or when the agreed research budget is exhausted.

## Repository layout

```text
.
├── README.md                         # Chinese landing page shown by GitHub
├── README.zh-CN.md                   # canonical Chinese README
├── README.en.md                      # English README
├── SKILL.md                          # root compatibility entry
├── skills/traceable-research/
│   ├── SKILL.md                      # canonical Agent Skill
│   ├── scripts/
│   │   ├── init_workspace.py
│   │   ├── audit_research.py
│   │   └── validate_skill.py
│   ├── references/
│   │   ├── research-standard.md
│   │   └── output-contract.md
│   └── assets/
│       ├── research-plan.md
│       ├── source-ledger.csv
│       ├── claim-ledger.csv
│       └── research-brief.md
├── evals/
├── tests/
├── .claude-plugin/
├── .codex-plugin/
└── .github/workflows/
```

## Output quality contract

A finished T.E.S.T. brief should make it easy to answer:

1. What is the answer, in one paragraph?
2. Which claims are verified, supported, contested, inferred, or unresolved?
3. Which sources directly support each important claim?
4. How current is the evidence?
5. What changed because contradictory evidence was considered?
6. What should the reader do next?
7. What would most likely change the recommendation?

The bundled auditor checks structure and referential integrity. It cannot decide whether a source is truthful or whether a conclusion is wise; those remain research judgments.

## Design principles

- **Evidence before prose**
- **Primary before derivative**
- **Claims before conclusions**
- **Contradictions before confidence**
- **Dates before “latest”**
- **Audits before delivery**
- **Uncertainty stated, never hidden**

## License

MIT. See [`LICENSE`](LICENSE).
