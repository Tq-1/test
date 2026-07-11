# Contributing to T.E.S.T.

Contributions should improve repeatability, evidence quality, portability, or evaluation—not merely add more prose.

## Good contributions

- a real failure case and a focused instruction that prevents it;
- a domain adaptation grounded in authoritative practice;
- an auditor check with a test;
- a trigger or output eval that exposes false activation or weak behavior;
- an installation fix verified on a supported client;
- clearer templates that reduce skipped steps.

## Before opening a pull request

```bash
python skills/traceable-research/scripts/validate_skill.py .
python -m unittest discover -s tests -v
```

Then confirm:

- `skills/traceable-research/SKILL.md` remains under 500 lines;
- detailed material uses progressive disclosure in `references/`;
- scripts use the Python standard library unless a dependency is essential and documented;
- new behavior has a test or eval;
- examples do not contain private data or fabricated citations;
- English and Chinese user-facing docs remain materially aligned.

## Design rule

Prefer a concrete procedure, gotcha, template, or validator over generic advice. Explain the failure mode the change prevents.
