# 竞赛答辩 PPT：整页模板优先 Skill

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](skills/competition-ppt-template-first/SKILL.md)
[![Workflow](https://img.shields.io/badge/Workflow-template--first-0f766e)](skills/competition-ppt-template-first/references/workflow.md)
[![License](https://img.shields.io/badge/License-MIT-f59e0b)](LICENSE)
[![skills.sh](https://skills.sh/b/che626/competition-ppt-template-first-skill)](https://skills.sh/che626/competition-ppt-template-first-skill)

> 先理清这套 PPT 要让谁相信什么、每页该出现什么，再把关键内容做成可编辑 PPT。

[English README](README.md)

## 它解决什么问题

常规的 AI 做 PPT 往往是“深色背景 + 一堆边框 + 小字 + 相同卡片”。页面虽然完整，但没有主体、没有场景、没有层次，也不适合竞赛答辩。

本 Skill 推荐先完成下面的基础链路：先把文档和用户要求拆成清晰的叙事与视觉任务，逐页分析内容与布局，再按该页布局生成对应的整页背景模板图，最后填入可编辑内容，而不是直接套深色背景和几个框。

1. 先整理报告、附件、截图、数据中能用的内容和待补材料，判断这是答辩、产品展示、技术汇报还是研究说明。
2. 先写清楚受众、要达成的判断、叙事路线，以及项目本身可以成为画面的产品、场景、材质、设备、人物、样本或证据。
3. 先锁定整套 PPT 的设计令牌：颜色、字号、间距、图片装帧、标题位置和深浅页面节奏；再登记每张图片是风格参考、底图来源、真实证据、可替换截图还是装饰物件。
4. 为每页写清楚：本页结论与内容分组、阅读顺序、视觉重心、背景图是什么、主图是什么、有什么辅助视觉物件、真实图片放哪里、文字放哪里、哪些内容必须可编辑、这一页禁止出现什么；并登记它与前后页的版式关系。
5. 所有内容页都必须在布局确定后，生成或设计一张专属的整页背景模板图；技术信息密集页也要生成安静、留白明确的模板图，不得改回纯底色加原生卡片。封面和结尾页使用独立的主视…16202 tokens truncated…es/image-asset-roles.md",
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
