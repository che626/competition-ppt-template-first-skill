---
name: competition-ppt-template-first
description: "Create polished, competition-focused PPTs through a practical template-first workflow: organize available material, plan the story, design key pages as full visual templates, then build an editable PPT with real evidence and readability checks. Scales from simple project showcases to report-grounded technical defenses."
---

# Competition PPT: Template-First Workflow

Use this skill when a user wants an attractive competition, defense, project-showcase, or course-presentation deck. The goal is not merely to fill a PPT with text. The goal is a coherent visual narrative in which the important text and evidence remain editable without making the workflow heavier than the project requires.

Read the references needed for the selected mode before creating slides. For report-grounded work, read `references/source-ingestion.md`, `references/workflow.md`, `references/project-conventions.md`, and `references/quality-gates.md`; use `references/layout-archetypes.md` and `references/prompt-library.md` when planning layouts and visual templates.

## The Core Principle

Do not start by assembling generic rectangles, UI lines, and text boxes directly in PowerPoint. That approach usually produces a flat, repetitive, low-end deck.

Instead:

1. Organize the supplied report, requirements, data, screenshots, and available evidence.
2. Decide what the audience should remember and what each important page needs to prove.
3. Build a concise slide plan before drawing anything.
4. Generate or art-direct a **whole-slide visual template image** for visually important pages; keep dense technical pages quieter when that serves the content better.
5. Turn the approved direction into a layered PPT: background, real images, editable text, and only the overlays that need to remain editable.
6. Render and inspect the finished deck, or at least the key pages changed in the current pass.

The image template supplies composition, atmosphere, light, material, visual rhythm, and high-end detailing. The PPT layer supplies factual text, real screenshots, charts, and evidence.

## Select the Right Mode

Pick the smallest mode that still preserves the template-first principle:

| Mode | Use when | Typical output |
| --- | --- | --- |
| `Core deck` | A topic, brief, screenshots, or an existing deck needs a coherent presentation. | Material note, slide plan, representative page where helpful, editable PPT, readability check. |
| `Report-grounded defense deck` | The user supplies a report, paper, technical document, or requirements package and wants the PPT derived from it. | Source manifest, factual notes with locators for key claims, page-evidence map where needed, editable PPT, rendered check. |
| `Single signature slide` | The user wants to test a visual direction or repair a key page. | Concise page plan, template or art direction, editable PPT page, preview. |
| `Existing deck repair` | A PPT exists but its visual structure, content density, or evidence use is weak. | Diagnosis, rebuilt background template where necessary, revised editable page. |
| `Image/PDF to editable` | The user already has an image-based page and needs native text/images. | Object-level reconstruction plan; do not claim full editability when only a background image is retained. |

State the selected mode and the expected user approval point before producing a full deck or a major visual rebuild.

## Default Guardrails

- Facts, metrics, product capabilities, awards, and roadmap claims must come from the supplied source material. Never invent evidence to fill a layout.
- Keep a source locator for metrics, model comparisons, awards, research findings, technical specifications, and other claims likely to be challenged. Keep ordinary narrative faithful to the source without forcing a complex citation system onto simple pages.
- The input document is the factual source, not the final slide copy. Condense and rewrite it into judge-facing language; do not paste report paragraphs onto slides.
- Important content slides should have one primary claim. The title, evidence, and conclusion should support it.
- Use a credible visual anchor on key content slides when evidence is available: a real screenshot, authentic sample image, measured chart, physical scene, or verified artifact.
- A generated image is a visual template, not a substitute for evidence. Do not use synthetic screenshots in place of real product evidence.
- Use richer, brighter visual templates on low-text pages. Use quieter, darker templates behind dense text or real screenshots.
- Keep title placement and hierarchy consistent across the deck. Use a page number, title, and optional short subtitle; do not put the title in a heavy framed box.
- Avoid generic HUD line art, repeated rounded cards, thick cyan outlines, empty grids, oversized decorative spheres, and a wall of identical components.
- Do not use English-only labels for a Chinese defense deck unless the term is genuinely required.
- Do not make body copy tiny merely to preserve a layout. Reflow the layout, shorten the copy, or use another archetype.
- If the user rejects the composition or the background template, rebuild the **entire underlay**. Do not keep layering fixes on top of a flawed template.
- When a page is confirmed, archive a copy before making any later alternative.

## Workflow

### 0. Ingest the project material

When the user supplies a report or project folder, prefer `Report-grounded defense deck` mode. When material is light or incomplete, begin with `Core deck` mode and record what is still missing.

1. Create the project folders with `scripts/init-report-grounded-deck.py` or manually follow `references/project-conventions.md`.
2. Inventory the available sources in `templates/source-manifest.md`: report, requirements, data files, screenshots, prior PPTs, awards, videos, and external evidence.
3. Read each source using the appropriate document, PDF, spreadsheet, PPTX, or image workflow. Extract headings, verified numbers, figures, tables, diagrams, captions, and asset paths. Render visual documents when layout or figures matter.
4. Record usable facts in `templates/fact-registry.md`. Add stable fact IDs and source locators to claims that need proof.
5. Create `templates/slide-source-map.md` for pages with metrics, comparisons, awards, or important technical claims. Record the primary conclusion, supporting facts/evidence, and the transition from the previous page.
6. Put uncertain, missing, or contradictory information in a `do not claim` list. Ask one focused question only when the missing decision materially changes the deck; otherwise reserve a replaceable zone and continue.

Do not finalize page copy, comparison values, award claims, or system capabilities until the available source material has been checked. For missing material, reserve a replaceable zone or mark it as a future plan instead of inventing evidence.

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

Use `templates/slide-blueprint.md`. In report-grounded mode, include fact IDs and evidence IDs for slides that make evidence-based claims.

For a full deck, begin from `templates/deck-brief.md`, then create one slide blueprint per page. Keep the resulting files in the project structure described by `references/project-conventions.md`.

### 3. Choose a visual system

Choose a dominant background tone, one support tone, one sharp accent, type hierarchy, texture/material motif, and title behavior. Then map template intensity to the slide:

- Cover, transition, conclusion: cinematic and visually rich.
- Pain-point, story, or concept pages: an atmospheric scene plus a strong focal image.
- Technical comparison, iteration, system screenshots, evidence: quieter, darker, more structured.

The deck should feel like one family, not the same layout repeated eleven times.

### 4. Generate the template image first

Generate a 16:9 template image for pages whose visual underlay matters, such as cover, pain-point, concept, solution, milestone, award, and conclusion pages. For dense technical, comparison, or screenshot pages, use a quieter template or a carefully designed native layout when that produces a clearer result. A template prompt should specify:

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

Do not convert a visibly cramped or structurally wrong template into a final PPT. Regenerate or simplify it first.

For a full deck with an unclear visual direction, make one representative **signature slide** first. It should be a real content page with the deck's expected density, not an empty cover. If the user has already supplied an approved deck or a clear visual reference, record the relevant palette, title hierarchy, and image treatment, then proceed directly.

### 6. Rebuild as a layered editable PPT

Use this layer order:

1. Whole-slide template background.
2. Non-editable decorative elements that are part of the template.
3. Real screenshots, photos, certificates, charts, and evidence images.
4. Editable headings, body copy, metrics, captions, and conclusion lines.
5. Only the smallest number of editable accent elements needed for future replacement.

Do not chase full editability at the expense of visual quality. The factual content and real evidence must be easy to replace; the visual underlay may remain a single image.

### 7. Render, inspect, revise, archive

Render the actual PPT to images when possible. Check the changed and high-risk pages against `references/quality-gates.md`, then revise. Archive versions the user has confirmed.

For substantial revisions, record feedback, root cause, structural change, and output path using `templates/revision-record.md`. Do not replace a confirmed page without preserving an approved copy.

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

A page is ready to deliver when:

- It communicates one judge-relevant conclusion.
- Important factual claims are grounded in source material and traceable through a fact ID and source locator when appropriate.
- It uses a credible visual anchor when the page needs evidence and the material is available.
- All important text is readable, aligned, and inside its intended region.
- The page looks coherent in the rendered PPT, not merely in the editor.
- No placeholder notes, design comments, generated gibberish, or accidental English labels remain.
