---
name: competition-ppt-template-first
description: "Create polished competition, product, and technical PPTs through a content-to-template workflow: analyze supplied documents and user goals, map each slide's layout and asset zones, generate a subject-specific whole-slide background template for every page, then build an editable PPT with real evidence and rendered QA. Use when a deck must look intentionally designed rather than like generic dark-AI cards."
---

# Competition PPT: Template-First Workflow

Use this skill when a user wants an attractive competition, defense, product-showcase, technical-review, research, or course-presentation deck. The goal is not merely to fill a PPT with text. The goal is a coherent visual narrative in which every page has a purpose-built composition, the important text and evidence remain editable, and the visual system belongs to the actual subject rather than a default AI style.

Read the references needed for the selected mode before creating slides. For any supplied document or project package, read `references/content-to-template-analysis.md`, `references/source-ingestion.md`, `references/workflow.md`, `references/project-conventions.md`, and `references/quality-gates.md`; use `references/layout-archetypes.md` and `references/prompt-library.md` when planning layouts and visual templates.

## The Core Principle

Do not start by assembling generic rectangles, UI lines, and text boxes directly in PowerPoint. That approach usually produces a flat, repetitive, low-end deck.

Instead:

1. Split the supplied report, requirements, screenshots, data, and user requests into a content-to-deck analysis.
2. Decide what kind of deck it is, who must be convinced, what the story route is, and what must visibly appear on every page.
3. Build a slide map and a template contract for every page before drawing anything.
4. After that page's contract is complete, generate or art-direct one **whole-slide visual template image for every page**. The template must include the required visual anchor, real-asset zones, text zones, and subject-specific visual ingredients.
5. Turn the approved templates into a layered PPT: background, real images, editable text, and only the overlays that need to remain editable.
6. Render and inspect the finished deck, or at least the key pages changed in the current pass.

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
- Every content slide must use a bespoke generated or art-directed whole-slide template image as its bottom layer. A quiet technical template is still an image-generation deliverable, not permission to fall back to a flat background or a native card layout.
- Generate the page template only after its page blueprint states the exact content blocks, image slots, crop focus, text zones, and supporting visual ingredients. Do not invent a visual template first and try to force content into it later.
- A visual template must show the page's actual subject, visual anchor, text zones, and evidence zones. A darkened stock photo with a row of generic boxes is not a valid template.
- Do not default to black, navy, cyan glow, HUD lines, English micro-labels, or a cyber style because the project mentions AI. Choose color, material, light, and scene from the subject and use light, mid, and dark pages deliberately.
- Use richer, brighter visual templates on low-text pages. Use quieter, darker templates behind dense text or real screenshots.
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
3. Read each source using the appropriate document, PDF, spreadsheet, PPTX, or image workflow. Extract decision context, headings, verified numbers, figures, tables, diagrams, captions, visual assets, and asset paths. Render visual documents when layout or figures matter.
4. Complete `templates/content-analysis.md`: classify the deck, identify the audience decision, split content into narrative/proof/visual material, list visual ingredients, choose a subject-derived visual system, and state questions or assumptions.
5. Record usable facts in `templates/fact-registry.md`. Add stable fact IDs and source locators to claims that need proof.
6. Create `templates/slide-source-map.md` for all proposed pages. Record the primary conclusion, supporting facts/evidence, required real asset, visual role, and transition from the previous page.
7. Put uncertain, missing, or contradictory information in a `do not claim` list. Ask at most two focused questions when the missing answer changes the narrative, required real asset, or visual direction; otherwise reserve a replaceable zone and continue.

Do not finalize page copy, comparison values, award claims, system capabilities, or page templates until the available source material and content analysis have been checked. For missing material, reserve a replaceable zone or mark it as a future plan instead of inventing evidence.

### 1. Establish the fact contract

Create a concise fact registry from the proposal, report, data sheet, screenshots, awards, and user constraints. Separate material into:

- Verified facts that may appear as claims.
- Available real evidence: images, screenshots, certificates, charts, logs, recordings.
- Unknown or not-yet-final information. Reserve editable space for it; do not fabricate it.

### 2. Design the narrative and template contracts before the slides

Write the deck's judge takeaway in one sentence. Then create an ordered slide map. For each slide, capture:

- `Slide number and title`
- `Primary judgment sentence`
- `Evidence required`
- `Text blocks and word budget`
- `Visual hierarchy`
- `Template type`
- `Editable layers`
- `Risk to verify`

Use `templates/slide-blueprint.md`. For every slide, complete the template contract: page role, background scene, primary visual, supporting visual ingredients, exact real-asset slots, text zones, editable overlays, contrast mode, and avoid list. In report-grounded mode, include fact IDs and evidence IDs for slides that make evidence-based claims.

For a full deck, begin from `templates/deck-brief.md`, then create one slide blueprint per page. Keep the resulting files in the project structure described by `references/project-conventions.md`.

### 3. Choose a visual system from the subject

Choose a dominant tone, one support tone, one sharp accent, type hierarchy, texture/material motif, title behavior, and light/mid/dark distribution. Explain why this system belongs to the subject. Do not select a generic deep-blue technology system by default. Then map template intensity to the slide:

- Cover, transition, conclusion: cinematic or product-led and visually rich.
- Pain-point, story, or concept pages: an atmospheric scene plus a strong focal image.
- Technical comparison, iteration, system screenshots, evidence: quieter and more structured; darkness is optional, not automatic.

The deck should feel like one family, not the same layout repeated eleven times.

### 4. Generate the template image from the page contract

Each page must have a template contract before image generation. Generate or art-direct one bespoke 16:9 whole-slide template image for every page. Content pages use the full content-to-template route: layout analysis first, template image second, editable evidence and text last. Cover and closing pages use an independently composed hero or conclusion template rather than a dense content layout, but still have their own whole-slide visual background.

Dense technical, comparison, iteration, and screenshot pages must use a quieter generated template with intentionally reserved text and real-asset zones. Minimal editable captions, crop masks, highlights, or data callouts may sit above it, but native shapes may not replace the whole-slide template image. A template prompt must specify:

- Subject matter and visual metaphor.
- Background scene or surface, including why it belongs to the subject.
- The primary visual anchor and supporting visual ingredients.
- Where each information zone will be placed.
- Which exact zones will receive real images, including their required crop and aspect ratio.
- The required density and visual weight.
- The light/mid/dark mode, palette, material, and visual system selected in Step 3.
- `No readable text, no fake dashboard screenshots, no watermark.`

Treat the following as the image-generation execution contract:

1. Derive the prompt from the completed slide blueprint, including exact title zone, main-claim zone, each text block, real-image slot, aspect ratio, crop focus, primary visual, blank zones, palette, contrast, and avoid list.
2. Use the available image-generation capability to generate the template. Use an art-directed source image only when image generation is unavailable or the source can satisfy the same documented composition contract better.
3. Inspect it at 16:9 presentation size before placing any content. Reject it when reserved zones are missing, crowded, visually unrelated, or unable to support the specified crop and word budget.
4. Regenerate the entire bottom template when the composition is wrong. Do not conceal a poor template with extra card walls or new frames.

The template image may include integrated light, surfaces, device imagery, product details, material texture, people in context, camera optics, data atmosphere, illustration, or evidence-wall treatment. It should not look like a wireframe that was assembled from empty boxes, a dark stock image behind generic cards, or a repeated cyber-HUD layout.

Use the appropriate page prompt in `references/prompt-library.md`; adapt the subject matter and evidence zones rather than copying a previous page's composition.

### 5. Review the analysis and composition before production

For an important or ambiguous deck, show the content analysis, page map, and planned visual system before bulk generation. Then show the template preview. Check whether it has enough room for the planned text and real evidence, whether it has meaningful visual ingredients, and whether it belongs to the same deck without repeating the same dark-AI layout.

Do not convert a visibly cramped or structurally wrong template into a final PPT. Regenerate or simplify it first.

For a full deck with an unclear visual direction, make one representative **signature slide** first. It should be a real content page with the deck's expected density, visual ingredients, and real-asset slots, not an empty cover. If the user has already supplied an approved deck or a clear visual reference, record the relevant palette, title hierarchy, image treatment, and contrast distribution, then proceed directly.

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
- Its content role, visual anchor, real-asset slots, text zones, and background scene were planned in a page/template contract before production.
- Its whole-slide background template image was generated or art-directed from that contract after the layout analysis, including for quiet technical pages.
- Important factual claims are grounded in source material and traceable through a fact ID and source locator when appropriate.
- It uses a credible visual anchor when the page needs evidence and the material is available.
- All important text is readable, aligned, and inside its intended region.
- The page looks coherent in the rendered PPT, not merely in the editor.
- No placeholder notes, design comments, generated gibberish, or accidental English labels remain.
