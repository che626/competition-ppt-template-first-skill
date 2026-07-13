#!/usr/bin/env python3
"""Create the traceable workspace used by the report-grounded deck workflow."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TEMPLATE_NAMES = (
    "content-analysis.md",
    "deck-brief.md",
    "fact-registry.md",
    "source-manifest.md",
    "slide-source-map.md",
    "slide-blueprint.md",
    "revision-record.md",
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize a project folder for a report-grounded competition PPT."
    )
    parser.add_argument("output", type=Path, help="New or existing deck workspace")
    parser.add_argument(
        "--source-folder",
        type=Path,
        help="Optional folder containing user-supplied source files; it is recorded but never copied.",
    )
    args = parser.parse_args()

    if args.source_folder and not args.source_folder.exists():
        parser.error(f"Source folder does not exist: {args.source_folder}")

    skill_root = Path(__file__).resolve().parents[1]
    template_root = skill_root / "templates"
    output = args.output.resolve()

    directories = {
        "00_intake": output / "00_intake",
        "00_plan": output / "00_plan",
        "01_templates": output / "01_templates" / "prompt-records",
        "02_build": output / "02_build",
        "03_renders": output / "03_renders",
        "04_approved": output / "04_approved",
        "99_retired": output / "99_retired",
    }
    for directory in directories.values():
        directory.mkdir(parents=True, exist_ok=True)

    destinations = {
        "content-analysis.md": directories["00_plan"] / "content-analysis.md",
        "deck-brief.md": directories["00_plan"] / "deck-brief.md",
        "fact-registry.md": directories["00_plan"] / "fact-registry.md",
        "source-manifest.md": directories["00_intake"] / "source-manifest.md",
        "slide-source-map.md": directories["00_plan"] / "slide-source-map.md",
        "slide-blueprint.md": directories["00_plan"] / "slide-blueprint.md",
        "revision-record.md": directories["00_plan"] / "revision-record.md",
    }
    for name in TEMPLATE_NAMES:
        target = destinations[name]
        if not target.exists():
            shutil.copy2(template_root / name, target)

    extraction_notes = directories["00_intake"] / "extraction-notes.md"
    if not extraction_notes.exists():
        extraction_notes.write_text(
            "# Extraction Notes\n\n"
            "Record document structure, source locators, ambiguous claims, and assets that need visual review.\n",
            encoding="utf-8",
        )

    readme = output / "README.md"
    if not readme.exists():
        source_note = str(args.source_folder.resolve()) if args.source_folder else "Not set"
        readme.write_text(
            "# Report-Grounded Competition PPT Workspace\n\n"
            f"Source folder: `{source_note}`\n\n"
            "1. Fill `00_intake/source-manifest.md`.\n"
            "2. Split the material into a deck decision in `00_plan/content-analysis.md`.\n"
            "3. Extract verified facts into `00_plan/fact-registry.md`.\n"
            "4. Build `00_plan/slide-source-map.md` and template contracts before any template image.\n"
            "5. Create one slide blueprint per page, then approve a representative template slide.\n",
            encoding="utf-8",
        )

    print(f"Initialized: {output}")
    print("Next: complete 00_intake/source-manifest.md and 00_plan/content-analysis.md")


if __name__ == "__main__":
    main()
