---
name: competition-ppt-template-first
description: "Create polished competition, product, and technical PPTs through a content-to-template workflow: analyze supplied documents and user goals, lock deck style tokens and image asset roles, map each slide's layout and asset zones, generate a subject-specific whole-slide background template for every page, then build an editable PPT with real evidence and rendered visual critique. Use when a deck must look intentionally designed rather than like generic dark-AI cards."
---

# Competition PPT: Template-First Workflow

Use this skill when a user wants an attractive competition, defense, product-showcase, technical-review, research, or course-presentation deck. The goal is not merely to fill a PPT with text. The goal is a coherent visual narrative in which every page has a purpose-built composition, the important text and evidence remain editable, and the visual system belongs to the actual subject rather than a default AI style.

Read the references needed for the selected mode before creating slides. For any supplied document or project package, read `references/content-to-template-analysis.md`, `references/source-ingestion.md`, `references/workflow.md`, `references/project-conventions.md`, and `references/quality-gates.md`; use `references/layout-archetypes.md`, `references/prompt-library.md`, `references/deck-token-system.md`, `references/image-asset-roles.md`, and `references/rendered-visual-critique.md` when planning layouts and visual templates.

## The Core Principle

Do not start by assembling generic rectangles, UI lines, and text boxes directly in PowerPoint. That approach usually produces a flat, repetitive, low-end deck.

Instead:

1. Split the supplied report, requirements, screenshots, data, and user requests into a content-to-deck analysis.
2. Decide what kind of deck it is, who must be convinced, what the story route is, and what must visibly appear on every page.
3. Lock the deck style tokens and register each image as style reference, template source, real evidence, replaceable screenshot, or decorative cutout.
4. Build a slide map, layout registry, and template contract for every page before drawing anything.
5. After that page's contract is complete, generate or art-direct one **whole-slide visual template image for every page**. The template must include the required visual anchor, real-asset zones, text zones, and subject-specific visual ingredients.
6. Turn the approved templates into a layered PPT: background, real images, editable text, and only the overlays that need to remain editable.
7. Render, critique composition/hierarchy/density/typography, fix at least one observed defect when needed, and re-inspect the affected pages.

The image template supplies composition, atmosphere, light, material, visual rhythm, and high-end detailing. The PPT layer supplies factual text, real screenshots, charts, and evidence.

## Select the Right Mode

Pick the smallest mode that still preserves the template-first principle:

| Mode | Use when | Typical output |
| --- | --- | --- |
| `Core deck` | A topic, brief, screenshots, or an existing deck needs a coherent presentation. | Content analysis, story route, page/template contracts, representative page where helpful, editable PPT, readability check. |
| `Report-grounded defense deck` | The user supplies a report, paper, technical document, or requirements package and wants the PPT derived from it. | Source manifest, content analysis, factual notes with locators for key claims, page-evidence map, per-page template contracts, editable PPT, rendered check. |
| `Single signature slide` | The user wants to test a visual direction or repair a key page. | Page purpose, visual-ingredient plan, template contract, editable PPT page, preview. |
| `Existing deck repair` | A PPT exists but its visual structure, content density, or evidence use is weak. | Diagnosis, rebuilt background template where necessary, revised editable page. |
| `Image/PDF to editable` | The user already has an image-based page and needs native text/images. | Object-level reconstruction plan; do not claim full editability when only a background image is retained. |

State the selected mode and the expected user approval point before producing a full deck or a major visual rebuild.

## Default Guardrails

- Facts, metrics, product capabilities, awards, and roadmap claims must come from the supplied source material. Never invent evidence to fill a layout.
- Do not create final pages immediately after receiving a topic or a document. First complete `templates/content-analysis.md`, then the story route, then a page/template contract for every proposed slide.
- If a report, product brief, or project folder is supplied, split it into decision context, narrative material, proof material, visual material, and gaps before choosing slide titles or backgrounds.
- Keep a source locator for metrics, model comparisons, awards, research findings, technical specifications, and other claims likely to be challenged. Keep ordinary narrative faithful to the source without forcing a complex citation system onto simple pages.
- The input document is the factual source, not the final slide copy. Condense and rewrite it into judge-facing language; do not paste report paragraphs onto slides.
- Important content slides should have one primary claim. The title, evidence, and conclusion should support it.
- Use a credible visual anchor on key content slides when evidence is available: a real screenshot, authentic sample image, measured chart, physical scene, or verified artifact.
- A generated image is a visual template, not a substitute for evidence. Do not use synthetic screenshots in place of real product evidence.
- Complete `templates/deck-style-tokens.md` before page-template production. Treat its color, type, spacing, image-treatment, and contrast-rhythm decisions as the deck's source of truth.
- Complete `templates/image-asset-register.md` before using images. Real evidence and replaceable screenshots must remain truthful; style references and decorative cutouts may never silently become evidence.
- Every content slide must use a bespoke generated or art-directed whole-slide template image as its bottom layer. A quiet technical template is still an image-generation deliverable, not permission to fall back to a flat background or a native card layout.
- Generate the page template only after its page blueprint states the exact content blocks, image slots, crop focus, text zones, and supporting visual ingredients. Do not invent a visual template first and try to force content into it later.
- A visual template must show the page's actual subject, visual anchor, text zones, and evidence zones. A darkened stock photo with a row of generic boxes is not a valid template.
- Do not default to black, navy, cyan glow, HUD lines, English micro-labels, or a cyber style because the project mentions AI. Choose color, material, light, and scene from the subject and use light, mid, and dark pages deliberately.
- Use richer, brighter visual templates on low-text pages. Use quieter, darker templates behind dense text or real screenshots.
- Vary composition while keeping deck tokens stable. Do not use one layout family more than twice in a row; record every page choice in `templates/layout-registry.md`.
- Keep title placement and hierarchy consistent across the deck. Use a page number, title, and optional short subtitle; do not put the title in a heavy framed box.
- Avoid generic HUD line art, repeated rounded cards, thick cyan outlines, empty grids, oversized decorative spheres, and a wall of identical components.
- Do not use English-only labels for a Chinese defense deck unless the term is genuinely required.
- Do not make body copy tiny merely to preserve a layout. Reflow the layout, shorten the copy, or use another archetype.
- If the user rejects the composition or the background template, rebuild the **entire underlay**. Do not keep layering fixes on top of a flawed template.
- When a page is confirmed, archive a copy before making any later alternative.

## Workflow

### 0. Analyze the project before planning pages

When the user supplies a report or project folder, prefer `Report-grounded defense deck` mode. When material is light or incomplete, begin with `Core deck` mode and record what is still missing. For a product showcase, select a product-led route rather than automatically using a competition-defense route.

1. Create the project folders with `scripts/init-report-grounded-deck.py` or manually follow `references/project-conventions.md`.
2. Inventory the available sources in `templates/source-manifest.md`: report, requirements, data files, screenshots, prior PPTs, awards, videos, and external evidence.
3. Read each source using the appropriate document, PDF, spreadsheet, PPTX, or image workflow. Extr…5994 tokens truncated…a designable deck brief

The deck must be derived from the project material and the user's requested outcome, not from the agent's general knowledge of the topic. Read `references/content-to-template-analysis.md` and `references/source-ingestion.md` before this stage.

The required route is:

```text
project documents and assets
  -> source manifest
  -> image-asset roles and deck style tokens
  -> content analysis: deck type, audience, story, visual ingredients, gaps
  -> extracted facts and evidence IDs
  -> audience-facing narrative route
  -> slide-source map and layout registry
  -> page blueprints plus template contracts
  -> visual templates and editable PPT
  -> rendered visual critique and fix-verification
```

This route prevents two common failures:

- A beautiful deck that makes claims the report does not support.
- A factually correct deck that pastes report paragraphs into tiny boxes.

## 1. Decide what kind of deck is being made

Before selecting a visual language, write the answer to these questions in `templates/content-analysis.md`:

- Is this primarily a competition defense, product showcase, technical review, research briefing, or project update?
- Who is the audience and what should they decide, believe, or remember?
- Which source material becomes narrative, proof, and visible subject matter?
- Which real asset must be large and recognizable?
- What visual setting, material, product, person, or scenario belongs to the subject?
- What is unknown enough to require a focused question?

Do not call a deck "AI style" and start from a dark blue background. A visual direction requires a subject-specific reason.

## 2. Inputs and source of truth

Before design begins, identify the source of truth for claims. This is usually the project report, dataset record, test report, code documentation, competition notice, and supplied screenshots. Never use visual polish as permission to make a claim that the materials do not support.

Build a fact registry with source locators and stable fact IDs:

| Fact ID | Claim or fact | Source locator | Evidence asset | Status |
| --- | --- | --- | --- | --- |
| F-01 | Model is deployed in the prototype | Technical report, Section 4.2 | E-03 product screenshot | Verified |
| F-02 | Industrial camera integration is planned | Roadmap, Phase 3 | None | Planned, not complete |

## 3. Build the argument, not a catalogue

The strongest defense decks are causal:

```text
real problem -> why existing practice breaks -> design response -> proof -> comparison -> next step
```

Do not lead with architecture, model names, or feature lists unless the judges already know why they matter. For each slide, write one sentence that the audience should remember. If the sentence cannot be stated, the slide is not yet ready for layout.

Before a page blueprint, create a slide-source map. The map links a page's conclusion to fact IDs, evidence IDs, and its speaker transition. It is the bridge between a long report and a concise defense deck.

## 4. Make a page blueprint and a template contract

Use `templates/slide-blueprint.md`. A blueprint must answer:

- What judgment should the judge make after this page?
- Which exact evidence proves it?
- Which component deserves the largest visual weight?
- Where will editable text sit?
- Where will real images sit?
- What is the background scene or quiet surface, and why does it belong to this page?
- What supporting object, material, detail crop, illustration, or artifact prevents the page from becoming empty?
- Is the template light, mid, or dark, and why?
- What must the template avoid?

Before the first page template, complete `templates/deck-style-tokens.md` and `templates/image-asset-register.md`. For every planned slide, add a row to `templates/layout-registry.md`: page role, layout family, reading order, primary visual anchor, asset slot, word budget, contrast mode, and structural relation to the previous page.

Do not repeat the same layout family more than twice in a row. The deck may vary its composition, but not its token system without a documented reason.

## 5. Select a visual system

Choose a system that belongs to the subject matter. For example, an AI-vision manufacturing project can mix real material, camera optics, process light, and restrained diagnostic cues; it does not need every page to be dark blue. A medical project might use clinical imaging and soft translucent layers; a product showcase may use the product's own colors and user context.

Keep these stable across the deck:

- Background family and contrast level
- Title position, page number, and hierarchy
- Accent-color logic
- Typography pairing and minimum body size
- Material/light motif
- Light / mid / dark distribution

Vary these between pages:

- Composition
- Visual anchor
- Evidence arrangement
- Ratio of image to text
- Template archetype

## 6. Design the whole slide before editing text

Generate or art-direct a bespoke 16:9 whole-slide template image from the completed page contract. Do this for every content page, including technical comparisons, iterations, and system screenshots. Those pages may use a quieter composition, but they may not skip template-image generation in favor of a flat background or a native card layout. Cover and closing pages use separately composed hero/conclusion templates instead of dense content layouts.

Include the actual subject matter in the visual, not only abstract decoration. A valid template has a background scene or purpose-designed surface, one primary visual, supporting visual ingredients, exact real-asset slots, text zones, and a clear contrast decision.

### Template prompt structure

```text
16:9 PPT template for [deck type] about [topic].
Page role: [what the audience must understand on this page].
Background scene or surface: [subject-specific setting / material / product context / quiet evidence surface].
Primary visual anchor: [real-world scene / device / product / sample / evidence metaphor].
Supporting visual ingredients: [relevant detail crop / object / artifact / material / illustration].
Composition: [title zone, exact real-asset slots and aspect ratios, body-copy zones, conclusion zone].
Style: [light / mid / dark mode, palette, material, lighting, texture] with a reason tied to the subject.
Density: [high / medium] with hierarchy and room for editable Chinese text.
This is the complete bottom-layer background image for this one specific slide. Respect every listed zone as a low-detail composition area. No readable text, fake UI screenshots, watermark, generic dark-AI HUD lines, repeated rounded-card wall, decorative sphere, or empty frames.
```

The visual template has two jobs: create a finished visual world and reserve space for reality. It does not need to contain the final copy.

## 7. Validate before PPT production

Inspect the template at presentation size. Reject it if:

- There is no place for the intended body copy.
- It forces real images into tiny decorative windows.
- It is mostly empty frames, line art, or a stock image darkened behind cards.
- It looks like a cover when it needs to carry dense evidence.
- It is too similar to the immediately previous page.
- Its palette was selected only because the topic includes AI.
- It does not visibly reserve the exact zones named in the page blueprint.
- It was generated before the page layout and content plan were decided.
- It ignores the deck tokens, asset roles, or layout-registry entry for the page.

## 8. Build a layered PPT

Recommended layer model:

| Layer | Role | Editable? |
| --- | --- | --- |
| Template image | Scene, composition, light, integrated frame language | Usually no |
| Real evidence | Screenshots, certificates, charts, samples | Yes, replaceable |
| Text | Title, claim, labels, explanation, metrics | Yes |
| Minimal overlays | Crop masks, captions, progress arrows, highlight markers | Yes when useful |

This is intentionally hybrid. A high-end page may use a single background image, yet still be a real PPT because its story, evidence, and key text are editable.

Do not replace the template image with a collection of native cards. Native elements are only small, editable overlays needed to add real evidence, factual text, crop masks, highlights, or future replacement points.

## 9. Revise structurally

Treat feedback as a structural signal:

- If text feels cramped, generate more text space.
- If content feels sparse, add meaningful evidence or enlarge the primary story, not random decoration.
- If the page feels generic, change the scene, visual anchor, and composition.
- If the background is wrong, replace the full background template. Do not stack new frames over old ones.

## 10. Run the rendered visual critique

After rendering, use `references/rendered-visual-critique.md` and record the result in `templates/rendered-visual-critique.md`. For each changed or high-risk slide, inspect:

1. Composition: balance, whitespace, rhythm, and grouping.
2. Visual hierarchy: entry point, eye flow, weight, and emphasis.
3. Information density: cognitive load, content priority, and scanning order.
4. Typography: token use, scale, contrast, wrapping, and evidence-caption attachment.

Record `pass`, `minor`, or `major` with an observation, a problem, and a specific fix. Re-render after any major fix. Do not approve a deck that still has an open major issue.

## 11. Archive decisions

Maintain three folders or labels:

- `working`: experiments and current drafts
- `approved`: pages explicitly confirmed by the user
- `retired`: rejected variants, kept only when useful for learning

Never silently replace an approved page.
