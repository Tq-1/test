#!/usr/bin/env python3
"""Create a T.E.S.T. research workspace from bundled templates."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

VALID_MODES = ("quick", "standard", "deep", "high-stakes")


def slugify(text: str, max_length: int = 64) -> str:
    """Create a conservative filesystem-safe slug."""
    value = text.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[-\s_]+", "-", value).strip("-")
    if not value:
        value = "research"
    return value[:max_length].rstrip("-") or "research"


def render_template(source: Path, destination: Path, replacements: dict[str, str]) -> None:
    text = source.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    destination.write_text(text, encoding="utf-8")


def create_workspace(question: str, mode: str, output: Path, force: bool = False) -> list[Path]:
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode {mode!r}; choose from {', '.join(VALID_MODES)}")

    skill_root = Path(__file__).resolve().parent.parent
    assets = skill_root / "assets"
    required = {
        "research-plan.md": assets / "research-plan.md",
        "source-ledger.csv": assets / "source-ledger.csv",
        "claim-ledger.csv": assets / "claim-ledger.csv",
        "brief.md": assets / "research-brief.md",
    }
    missing = [str(path) for path in required.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing bundled templates: " + ", ".join(missing))

    output = output.expanduser().resolve()
    if output.exists() and any(output.iterdir()) and not force:
        raise FileExistsError(
            f"{output} is not empty. Choose another path or pass --force to replace template files."
        )
    output.mkdir(parents=True, exist_ok=True)

    replacements = {
        "QUESTION": question.strip(),
        "MODE": mode,
        "DATE": date.today().isoformat(),
    }
    created: list[Path] = []
    for name, source in required.items():
        target = output / name
        if target.exists() and not force:
            raise FileExistsError(f"{target} already exists; pass --force to replace it")
        if source.suffix == ".csv":
            shutil.copyfile(source, target)
        else:
            render_template(source, target, replacements)
        created.append(target)

    workspace_readme = output / "README.md"
    workspace_readme.write_text(
        "\n".join(
            [
                f"# T.E.S.T. workspace: {question.strip()}",
                "",
                f"- Mode: `{mode}`",
                f"- Created: `{date.today().isoformat()}`",
                "",
                "## Workflow",
                "",
                "1. Complete `research-plan.md` before broad searching.",
                "2. Record inspected sources in `source-ledger.csv`.",
                "3. Record atomic material claims in `claim-ledger.csv`.",
                "4. Draft `brief.md` from the claim ledger.",
                "5. Run the audit before delivery:",
                "",
                "```bash",
                f"python path/to/traceable-research/scripts/audit_research.py {output}",
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )
    created.append(workspace_readme)
    return created


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a T.E.S.T. research workspace from bundled templates."
    )
    parser.add_argument("question", help="The research question or decision.")
    parser.add_argument(
        "--mode",
        choices=VALID_MODES,
        default="standard",
        help="Research mode (default: standard).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Output directory. Defaults to research/<question-slug>.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing template files in the output directory.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output = args.out or Path("research") / slugify(args.question)
    try:
        created = create_workspace(args.question, args.mode, output, args.force)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(f"Created T.E.S.T. workspace at {created[0].parent}")
    for path in created:
        print(f"  - {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
