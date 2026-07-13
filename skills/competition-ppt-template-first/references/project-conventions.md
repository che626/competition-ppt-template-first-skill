# Project Conventions and Approval State

## Why project state matters

A competition deck is iterative. Without a predictable folder structure, an agent can lose the approved template, overwrite the good version, or mix rejected experiments with final assets. Use one task folder per deck.

```text
competition-ppt/
  00_intake/
    source-manifest.md
    image-asset-register.md
    extraction-notes.md
    supplied-assets/
  00_plan/
    content-analysis.md
    deck-brief.md
    deck-style-tokens.md
    fact-registry.md
    slide-source-map.md
    layout-registry.md
    slide-map.md
    revision-record.md
  01_templates/
    01_cover_template.png
    02_pain-points_template.png
    prompt-records/
  02_build/
    01_cover_editable.pptx
    02_pain-points_editable.pptx
  03_renders/
    01_cover_preview.png
    02_pain-points_preview.png
    qa.md
    rendered-visual-critique.md
  04_approved/
    01_cover_approved.pptx
    02_pain-points_approved.pptx
  99_retired/
    02_pain-points_template_rejected.png
```

## State model

| State | Meaning | Agent action |
| --- | --- | --- |
| `planned` | Content and evidence are mapped, no visual decision yet. | Build the content analysis. |
| `analyzed` | Deck type, audience decision, narrative route, visual ingredients, questions, and style rationale are recorded. | Build the narrative, slide-source map, and page/template contracts. |
| `ingested` | Documents, assets, source locators, and do-not-claim items are recorded. | Confirm the content analysis and template contracts. |
| `template-review` | The whole-slide template has been generated. | Show it; do not build the final page until it is viable. |
| `build-review` | The layered PPT and render exist. | Inspect readability, source fidelity, and visual fit. |
| `visual-critique` | The rendered deck has composition, hierarchy, density, and typography findings. | Fix open major issues and re-render the affected pages. |
| `approved` | The user explicitly accepts the page. | Copy to `04_approved`; preserve it. |
| `retired` | The user rejects the visual or the template cannot carry content. | Move artifacts to `99_retired`; record why. |

## Naming rules

- Prefix page files with two digits: `01_`, `02_`, `10_`.
- Use semantic English or pinyin slugs after the page number; names must remain easy to sort and search.
- Use `_template`, `_editable`, `_preview`, `_approved`, and `_rejected` suffixes consistently.
- Do not overwrite an approved artifact. Create a new version only after the user reopens the page.

## User-visible progress

For a full deck, communicate one active stage at a time:

1. Source intake and content analysis
2. Fact registry, narrative route, and slide-source map
3. Style tokens, image roles, layout registry, and page/template contracts
4. Representative-template approval and template production
5. Editable PPT build, rendered visual critique, and approved archive

Use file paths as completion evidence. Do not mark a stage complete solely because a chat response was written.
