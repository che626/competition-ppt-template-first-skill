# Competition PPT Template-First Skill

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](SKILL.md)
[![Workflow](https://img.shields.io/badge/Workflow-template--first-0f766e)](references/workflow.md)
[![PowerPoint](https://img.shields.io/badge/Output-editable%20PPTX-2563eb)](references/quality-gates.md)
[![License](https://img.shields.io/badge/License-MIT-f59e0b)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/che626/competition-ppt-template-first-skill?style=flat&logo=github&label=stars)](https://github.com/che626/competition-ppt-template-first-skill/stargazers)

> A high-end competition deck should be **art-directed first, editable where it matters**.

Chinese documentation: [README.zh-CN.md](README.zh-CN.md)

`competition-ppt-template-first` is a reusable Agent Skill for high-stakes competition and defense PPTs. It replaces the usual "dark background + generic components + tiny text" workflow with a reliable sequence:

```mermaid
flowchart LR
    A[Source report<br/>screenshots and evidence] --> B[Fact registry]
    B --> C[Story and slide map]
    C --> D[Whole-slide visual template]
    D --> E{Signature slide<br/>approved?}
    E -- Revise --> D
    E -- Yes --> F[Layered editable PPT]
    F --> G[Render and visual QA]
    G --> H[Approved-page archive]
```

The template image carries composition, atmosphere, material, light, and visual detail. The editable PPT layer carries the factual claim, real screenshots, charts, certificates, and the text the user may need to update.

## Why Template-First

| Conventional AI PPT | Template-first competition PPT |
| --- | --- |
| Starts with rectangles, cards, and text boxes | Starts with facts, a page argument, and a full-slide art direction |
| Reuses one layout until the deck becomes flat | Holds a stable visual system while varying slide archetypes |
| Uses generated images as fake proof | Reserves prominent zones for authentic screenshots and artifacts |
| Pursues full editability and accepts mediocre composition | Keeps critical facts editable while preserving a high-completion visual underlay |
| Repairs rejected pages with more overlays | Rebuilds the entire underlay when the template is structurally wrong |

## Install

Use any Skill-compatible agent installer, or copy this folder into the agent's skills directory. For installers based on the community `skills` CLI:

```bash
npx -y skills@latest add che626/competition-ppt-template-first-skill \
  --skill competition-ppt-template-first \
  --agent codex \
  --global
```

The skill entry point is [`SKILL.md`](SKILL.md). It is designed for Codex, Claude Code, Cursor, and other agents that recognize Agent Skills.

## Use It

Attach the report, evidence images, and any reference deck, then use a prompt such as:

```text
$competition-ppt-template-first
Read the project report and create an 11-page AI-vision competition defense deck.
Use the supplied screenshots as real evidence. First produce the fact registry,
slide map, and one representative template-first signature slide for approval.
```

More copy-ready prompts are in [`examples/prompt-recipes.md`](examples/prompt-recipes.md).

## What the Skill Produces

```text
competition-ppt/
  00_plan/       fact registry, deck brief, slide map
  01_templates/  approved 16:9 template images and prompt records
  02_build/      editable PPTX work files
  03_renders/    exported previews and QA notes
  04_approved/   explicitly confirmed pages
  99_retired/    rejected variants kept for traceability
```

The full folder convention is documented in [`references/project-conventions.md`](references/project-conventions.md).

## Included Playbook

| Resource | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Agent execution contract and mode selection |
| [`references/workflow.md`](references/workflow.md) | Fact-to-deck production method |
| [`references/layout-archetypes.md`](references/layout-archetypes.md) | Competition-specific page structures |
| [`references/prompt-library.md`](references/prompt-library.md) | Prompt patterns for visual templates |
| [`references/quality-gates.md`](references/quality-gates.md) | Rendered PPT acceptance checks |
| [`templates/deck-brief.md`](templates/deck-brief.md) | Deck-level planning template |
| [`templates/slide-blueprint.md`](templates/slide-blueprint.md) | Per-page content and layout blueprint |
| [`templates/revision-record.md`](templates/revision-record.md) | Feedback-to-structural-revision log |
| [`examples/ai-vision-defense-example.md`](examples/ai-vision-defense-example.md) | A generic 11-page AI vision map |

## Design Position

Dense but controlled. Rich enough to feel competition-grade, calm enough to be read by judges. Use scenes, materials, visual evidence, light, and typographic scale to build interest. Avoid generic cyberpunk frames, repeated rounded-card walls, fake UI screenshots, illegible generated text, and body copy reduced to microscopic size.

## Scope and Limits

- Best for innovation, AI, robotics, engineering, research, and product-defense decks.
- It is not a generic slide-template library or an automatic corporate-branding system.
- It does not invent metrics, achievements, or product capabilities.
- It intentionally keeps complex visual underlays as images when that is the best way to preserve quality; this is not the same as dropping a finished slide screenshot into PowerPoint.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or proposing an archetype. The repository accepts generalized, rights-cleared workflows and examples only; do not submit private project evidence.

## License

MIT. This repository contains no project screenshots, certificates, or proprietary competition material.
