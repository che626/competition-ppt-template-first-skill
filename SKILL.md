---
name: competition-ppt-template-first
description: "Create polished, competition-grade defense PPTs through a template-first workflow: ground the narrative in source material, plan each slide, generate a complete visual template image, then rebuild it as an editable PPT with real evidence and strict visual QA. Use for innovation competitions, technical defenses, project showcases, and any deck that must look designed rather than assembled from generic cards."
---

# Competition PPT: Template-First Workflow

Use this skill when a user wants an attractive, high-stakes competition or defense deck. The goal is not merely to fill a PPT with text. The goal is a coherent visual narrative in which every page looks intentionally art-directed while the important text and evidence remain editable.

Read `references/source-ingestion.md`, `references/workflow.md`, `references/layout-archetypes.md`, `references/project-conventions.md`, `references/prompt-library.md`, and `references/quality-gates.md` before creating slides.

## The Core Principle

Do not start by assembling generic rectangles, UI lines, and text boxes directly in PowerPoint. That approach usually produces a flat, repetitive, low-end deck.

Instead:

1. Ingest the supplied report, requirements, data, and evidence into a traceable source map.
2. Extract facts, evidence, constraints, and the answer the judges should remember.
3. Build a slide blueprint before drawing anything.
4. Generate or art-direct a **whole-slide visual template image** for each page.
5. Turn the approved template into a layered PPT: background, real images, editable text, and only the overlays that need to remain editable.
6. Render and inspect every page before calling it finished.

The image template supplies composition, atmosphere, light, material, visual rhythm, and high-end detailing. The PPT layer supplies factual text, real screenshots, charts, and evidence.

## Select the Right Mode

Pick the smallest mode that still preserves the template-first principle:

| Mode | Use when | Required output |
| --- | --- | --- |
| `Full defense deck` | A report or project needs a complete competition presentation. | Fact registry, slide map, approved sample, layered PPT, rendered QA. |
| `Report-grounded defense deck` | The user supplies a project report, proposal, paper, technical document, or requirements package and wants the PPT derived from it. | Source manifest, fact registry with source locators, slide-source map, approved sample, layered PPT, rendered QA. |
| `Single signature slide` | The user wants to test a visual direction or repair a key page. | Slide blueprint, template image, editable PPT page, preview. |
| `Existing deck repair` | A PPT exists but its visual structure, content density, or evidence use is weak. | Diagnosis, rebuilt background template where necessary, revised editable page. |
| `Image/PDF to editable` | The user already has an image-based page and needs native text/images. | Object-level reconstruction plan; do not claim full editability when only a background image is retained. |

State the selected mode and the expected user approval point before producing non-trivial slide output.

## Non-Negotiable Rules

- Facts, metrics, product capabilities, awards, and roadmap claims must come from the supplied source material. Never invent evidence to fill a layout.
- Every non-trivial claim must have a source locator: document name plus section, page, table, figure, sheet, or asset identifier. A claim without a locator is not allowed onto a final slide.
- The input document is the factual source, not the final slide copy. Condense and rewrite it into judge-facing language; do not paste report paragraphs onto slides.
- Every content slide has one primary claim. The title, evidence, and conclusion must all support that claim.
- Put at least one credible visual anchor on every slide: a real screenshot, authentic sample image, measured chart, physical scene, or verified artifact.
- A generated image is a visual template, not a substitute for evidence. Do not use synthetic screenshots in place of real product evidence.
- Use richer, brighter visual templates on low-text pages. Use quieter, darker templates behind dense text or real screenshots.
- Keep title placement and hierarchy consistent across the deck. Use a page number, title, and optional short subtitle; do not put the title in a heavy framed box.
- Avoid generic HUD line art, repeated rounded cards, thick cyan outlines, empty grids, oversized decorative spheres, and a wall of identical components.
- Do not use English-only labels for a Chinese defense deck unless the term is genuinely required.
- Do not make body copy tiny merely to preserve a layout. Reflow the layout, shorten the copy, or use another archetype.
- If the user rejects the composition or the background template, rebuild the **entire underlay**. Do not keep layering fixes on top of a flawed template.
- After a page is confirmed, archive a copy and do not modify it unless the user explicitly reopens it.

## Required Workflow

### 0. Ingest the project material

When the user supplies a report or project folder, start in `Report-grounded defense deck` mode.

1. Create the project folders with `scripts/init-report-grounded-deck.py` or manually follow `references/project-conventions.md`.
2. Inventory every source in `templates/source-manifest.md`: report, requirements, data files, screenshots, prior PPTs, awards, videos, and external evidence.
3. Read each source using the appropriate document, PDF, spreadsheet, PPTX, or image workflow. Extract headings, verified numbers, figures, tables, diagrams, captions, and asset paths. Render visual documents when layout or figures matter.
4. Record only usable facts in `templates/fact-registry.md`, including a stable fact ID and source locator.
5. Create `templates/slide-source-map.md` before planning page visuals. Every page must state its primary conclusion, fact IDs, evidence IDs, and the transition from the previous page.
6. Put uncertain, missing, or contradictory information in a `do not claim` list. Ask one focused question only when the missing decision materially changes the deck; otherwise reserve a replaceable zone and continue.

Do not generate page copy, comparison values, award claims, or system capabilities until this ingestion gate is complete.

### 1. Establish the fact contract

Create a concise fact registry from the proposal, report, data sheet, screenshots, awards, and user constraints. Separate material into:

- Verified facts that may appear as claims.
- Available real evidence: images, screenshots, certificates, charts, logs, recordings.
- Unknown or not-yet-final information. Reserve editable space for it; do not fabricate it.

### 2. Design the narrative before the slides

Write the deck's judge takeaway in one sentence. Then create an ordered slide map. For each slide, capture:

- `Slide number and title`
- `Primary judgment sentence`
- `Evidence required`
- `Text blocks and word budget`
- `Visual hierarchy`
- `Template type`
- `Editable layers`
- `Risk to verify`

Use `templates/slide-blueprint.md`. In report-grounded mode, every blueprint must include the fact IDs and evidence IDs from `templates/slide-source-map.md`.

For a full deck, begin from `templates/deck-brief.md`, then create one slide blueprint per page. Keep the resulting files in the project structure described by `references/project-conventions.md`.

### 3. Choose a visual system

Choose a dominant background tone, one support tone, one sharp accent, type hierarchy, texture/material motif, and title behavior. Then map template intensity to the slide:

- Cover, transition, conclusion: cinematic and visually rich.
- Pain-point, story, or concept pages: an atmospheric scene plus a strong focal image.
- Technical comparison, iteration, system screenshots, evidence: quieter, darker, more structured.

The deck should feel like one family, not the same layout repeated eleven times.

### 4. Generate the template image first

Generate one 16:9 template image per slide before building the PPT. The prompt must specify:

- Subject matter and visual metaphor.
- Where each information zone will be placed.
- Which zones will receive real images.
- The required density and visual weight.
- The visual system selected in Step 3.
- `No readable text, no fake dashboard screenshots, no watermark.`

The template image may include integrated light, surfaces, device imagery, fabric, camera optics, data atmosphere, or evidence-wall treatment. It should not look like a wireframe that was assembled from empty boxes.

Use the appropriate page prompt in `references/prompt-library.md`; adapt the subject matter and evidence zones rather than copying a previous page's composition.

### 5. Review composition before production

Show the template preview. Check whether it has enough room for the planned text and real evidence, whether it feels visually finished, and whether it belongs to the same deck.

Do not convert an unapproved or visibly cramped template into a PPT. Regenerate it first.

For a full deck, generate exactly one representative **signature slide** first. It should be a real content page with the deck's expected density, not an empty cover. After the user approves its visual language, record the approved palette, title hierarchy, image treatment, and template-generation method in the project brief before creating the remaining pages.

### 6. Rebuild as a layered editable PPT

Use this layer order:

1. Whole-slide template background.
2. Non-editable decorative elements that are part of the template.
3. Real screenshots, photos, certificates, charts, and evidence images.
4. Editable headings, body copy, metrics, captions, and conclusion lines.
5. Only the smallest number of editable accent elements needed for future replacement.

Do not chase full editability at the expense of visual quality. The factual content and real evidence must be easy to replace; the visual underlay may remain a single image.

### 7. Render, inspect, revise, archive

Render the actual PPT to images. Check it against `references/quality-gates.md`, then revise. Archive only versions the user has confirmed.

For each revision, record: feedback, root cause, structural change, and output path using `templates/revision-record.md`. Do not replace a confirmed page without preserving an approved copy.

## Feedback Translation Rules

Translate user feedback into a design change, not a cosmetic patch:

| User feedback | Required interpretation |
| --- | --- |
| "Too empty" | Increase visual evidence, enlarge meaningful text, introduce a strong scene or evidence composition; do not add random filler. |
| "Too many boxes" | Replace repeated cards with a single visual structure, asymmetry, image-led composition, or integrated surfaces. |
| "Style is not unified" | Reuse palette, title hierarchy, texture, lighting, and accent logic, not necessarily the exact previous layout. |
| "Not enough room for text" | Regenerate the template with deliberate blank zones; do not compress text into tiny labels. |
| "Background is wrong" | Regenerate the bottom template and rebuild the page; do not simply cover old frames with new objects. |
| "Use real pictures" | Replace generated placeholders with authentic supplied images while retaining the visual structure. |

## Completion Criteria

A page is complete only when:

- It communicates one judge-relevant conclusion.
- Every factual statement is grounded in source material and traceable through its fact ID and source locator.
- It contains at least one credible visual anchor.
- All important text is readable, aligned, and inside its intended region.
- The page looks coherent in the rendered PPT, not merely in the editor.
- No placeholder notes, design comments, generated gibberish, or accidental English labels remain.
