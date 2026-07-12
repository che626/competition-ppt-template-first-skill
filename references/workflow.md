# Template-First Competition PPT Workflow

## 0. Source ingestion: turn documents into a slideable evidence base

The deck must be derived from the project material, not from the agent's general knowledge of the topic. Read `references/source-ingestion.md` before this stage.

The required route is:

```text
project documents and assets
  -> source manifest
  -> extracted facts and evidence IDs
  -> judge-facing narrative route
  -> slide-source map
  -> page blueprints
  -> visual templates and editable PPT
```

This route prevents two common failures:

- A beautiful deck that makes claims the report does not support.
- A factually correct deck that pastes report paragraphs into tiny boxes.

## 1. Inputs and source of truth

Before design begins, identify the source of truth for claims. This is usually the project report, dataset record, test report, code documentation, competition notice, and supplied screenshots. Never use visual polish as permission to make a claim that the materials do not support.

Build a fact registry with source locators and stable fact IDs:

| Fact ID | Claim or fact | Source locator | Evidence asset | Status |
| --- | --- | --- | --- | --- |
| F-01 | Model is deployed in the prototype | Technical report, Section 4.2 | E-03 product screenshot | Verified |
| F-02 | Industrial camera integration is planned | Roadmap, Phase 3 | None | Planned, not complete |

## 2. Build the argument, not a catalogue

The strongest defense decks are causal:

```text
real problem -> why existing practice breaks -> design response -> proof -> comparison -> next step
```

Do not lead with architecture, model names, or feature lists unless the judges already know why they matter. For each slide, write one sentence that the audience should remember. If the sentence cannot be stated, the slide is not yet ready for layout.

Before a page blueprint, create a slide-source map. The map links a page's conclusion to fact IDs, evidence IDs, and its speaker transition. It is the bridge between a long report and a concise defense deck.

## 3. Make a page blueprint

Use `templates/slide-blueprint.md`. A blueprint must answer:

- What judgment should the judge make after this page?
- Which exact evidence proves it?
- Which component deserves the largest visual weight?
- Where will editable text sit?
- Where will real images sit?
- Is the template rich or quiet, and why?

## 4. Select a visual system

Choose a system that belongs to the subject matter. For example, an AI-vision manufacturing project can use dark machine-space, textile macro texture, camera optics, diagnostic light, and restrained cyan/gold signals. A medical project might use clinical imaging and soft translucent layers instead.

Keep these stable across the deck:

- Background family and contrast level
- Title position, page number, and hierarchy
- Accent-color logic
- Typography pairing and minimum body size
- Material/light motif

Vary these between pages:

- Composition
- Visual anchor
- Evidence arrangement
- Ratio of image to text
- Template archetype

## 5. Design the whole slide before editing text

Generate or art-direct a 16:9 template with deliberate content zones. Include the actual subject matter in the visual, not only abstract decoration.

### Template prompt structure

```text
Premium 16:9 competition-defense PPT template for [topic].
Visual narrative: [what the slide needs to communicate].
Main visual: [real-world scene / device / product / evidence metaphor].
Composition: [location of title, evidence areas, text areas, conclusion zone].
Style: [palette, material, lighting, texture].
Density: [high / medium] but with clear hierarchy and breathing room.
Leave intentional dark, low-detail zones for editable Chinese text and real images.
No readable text, no fake UI screenshot, no watermark, no generic empty HUD boxes,
no repeated rounded-card wall, no decorative sphere.
```

The visual template has two jobs: create a finished visual world and reserve space for reality. It does not need to contain the final copy.

## 6. Validate before PPT production

Inspect the template at presentation size. Reject it if:

- There is no place for the intended body copy.
- It forces real images into tiny decorative windows.
- It is mostly empty frames or line art.
- It looks like a cover when it needs to carry dense evidence.
- It is too similar to the immediately previous page.

## 7. Build a layered PPT

Recommended layer model:

| Layer | Role | Editable? |
| --- | --- | --- |
| Template image | Scene, composition, light, integrated frame language | Usually no |
| Real evidence | Screenshots, certificates, charts, samples | Yes, replaceable |
| Text | Title, claim, labels, explanation, metrics | Yes |
| Minimal overlays | Crop masks, captions, progress arrows, highlight markers | Yes when useful |

This is intentionally hybrid. A high-end page may use a single background image, yet still be a real PPT because its story, evidence, and key text are editable.

## 8. Revise structurally

Treat feedback as a structural signal:

- If text feels cramped, generate more text space.
- If content feels sparse, add meaningful evidence or enlarge the primary story, not random decoration.
- If the page feels generic, change the scene, visual anchor, and composition.
- If the background is wrong, replace the full background template. Do not stack new frames over old ones.

## 9. Archive decisions

Maintain three folders or labels:

- `working`: experiments and current drafts
- `approved`: pages explicitly confirmed by the user
- `retired`: rejected variants, kept only when useful for learning

Never silently replace an approved page.
