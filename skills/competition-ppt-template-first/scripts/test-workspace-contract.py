#!/usr/bin/env python3
"""Smoke-test the report-grounded workspace contract for this Skill."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
INITIALIZER = SKILL_ROOT / "scripts" / "init-report-grounded-deck.py"

EXPECTED_TEMPLATES = {
    "speaker-map.md": "00_plan/speaker-map.md",
    "data-evidence-plan.md": "00_plan/data-evidence-plan.md",
    "layout-registry.md": "00_plan/layout-registry.md",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    for template_name in EXPECTED_TEMPLATES:
        if not (SKILL_ROOT / "templates" / template_name).is_file():
            fail(f"missing template: {template_name}")

    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    for phrase in ("speaker-map.md", "data-evidence-plan.md", "page rhythm"):
        if phrase not in skill_text:
            fail(f"SKILL.md is missing workflow phrase: {phrase}")

    with tempfile.TemporaryDirectory(prefix="competition-ppt-contract-") as temp_dir:
        workspace = Path(temp_dir) / "deck"
        result = subprocess.run(
            [sys.executable, str(INITIALIZER), str(workspace)],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            fail(f"initializer failed:\n{result.stdout}\n{result.stderr}")

        for template_name, relative_path in EXPECTED_TEMPLATES.items():
            target = workspace / relative_path
            if not target.is_file():
                fail(f"initializer did not create {relative_path}")
            if not target.read_text(encoding="utf-8").strip():
                fail(f"initialized template is empty: {relative_path}")

        layout_registry = (workspace / EXPECTED_TEMPLATES["layout-registry.md"]).read_text(encoding="utf-8")
        if "Page rhythm" not in layout_registry:
            fail("layout registry does not expose Page rhythm")

    print("WORKSPACE_CONTRACT_TEST=OK")


if __name__ == "__main__":
    main()
