#!/usr/bin/env python3
"""Static release checks for the installable competition-PPT Skill package."""

from __future__ import annotations

import re
import sys
import argparse
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/content-to-template-analysis.md",
    "references/workflow.md",
    "references/source-ingestion.md",
    "references/layout-archetypes.md",
    "references/prompt-library.md",
    "references/project-conventions.md",
    "references/quality-gates.md",
    "references/deck-token-system.md",
    "references/image-asset-roles.md",
    "references/rendered-visual-critique.md",
    "templates/deck-brief.md",
    "templates/deck-style-tokens.md",
    "templates/content-analysis.md",
    "templates/fact-registry.md",
    "templates/image-asset-register.md",
    "templates/layout-registry.md",
    "templates/rendered-visual-critique.md",
    "templates/slide-blueprint.md",
    "templates/slide-source-map.md",
    "templates/source-manifest.md",
    "templates/revision-record.md",
    "scripts/init-report-grounded-deck.py",
    "scripts/validate-distribution.ps1",
)

MARKDOWN_LINK = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")

WORKFLOW_CONTRACT = {
    "SKILL.md": (
        "deck-style-tokens.md",
        "image-asset-register.md",
        "layout-registry.md",
        "rendered-visual-critique.md",
    ),
    "references/quality-gates.md": (
        "Deck-control integrity",
        "Rendered visual critique",
        "No layout family appears more than twice consecutively",
    ),
    "templates/slide-blueprint.md": (
        "Deck controls used on this page",
        "Entry point and eye flow",
    ),
    "scripts/init-report-grounded-deck.py": (
        "deck-style-tokens.md",
        "image-asset-register.md",
        "layout-registry.md",
        "rendered-visual-critique.md",
    ),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_front_matter() -> None:
    content = (PACKAGE_ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("SKILL.md must begin with YAML front matter")
    front_matter, _, _ = content[4:].partition("\n---\n")
    if not front_matter:
        fail("SKILL.md front matter is not closed")
    if not re.search(r"^name:\s*competition-ppt-template-first\s*$", front_matter, re.MULTILINE):
        fail("SKILL.md must expose name: competition-ppt-template-first")
    if not re.search(r'^description:\s*["\'].*["\']\s*$', front_matter, re.MULTILINE):
        fail("SKILL.md description must be a quoted YAML string")


def validate_required_files() -> None:
    for relative_path in REQUIRED_FILES:
        if not (PACKAGE_ROOT / relative_path).is_file():
            fail(f"missing required package file: {relative_path}")


def validate_markdown_links(search_root: Path) -> None:
    broken: list[str] = []
    for markdown_file in search_root.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        content = markdown_file.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(content):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not (markdown_file.parent / target).exists():
                broken.append(f"{markdown_file.relative_to(search_root)} -> {target}")
    if broken:
        fail("broken local Markdown links:\n  " + "\n  ".join(broken))


def validate_workflow_contract() -> None:
    for relative_path, required_phrases in WORKFLOW_CONTRACT.items():
        content = (PACKAGE_ROOT / relative_path).read_text(encoding="utf-8")
        for phrase in required_phrases:
            if phrase not in content:
                fail(f"workflow contract missing {phrase!r} in {relative_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate the installable competition-PPT Skill package."
    )
    parser.add_argument(
        "--repository-root",
        type=Path,
        help="Optional repository root for validating the GitHub-facing README files too.",
    )
    args = parser.parse_args()
    search_root = args.repository_root.resolve() if args.repository_root else PACKAGE_ROOT

    validate_front_matter()
    validate_required_files()
    validate_markdown_links(search_root)
    validate_workflow_contract()
    print("PACKAGE_STATIC_VALIDATION=OK")


if __name__ == "__main__":
    main()
