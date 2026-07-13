# Content-to-Template Analysis

## Purpose

When the user supplies a report, product brief, competition requirements, screenshots, or a reference deck, do not jump from extracted text to PPT production. First turn the material into a designable brief that explains what the deck is, what decision it needs to create, and what every page must visibly contain.

The output of this phase is a content-and-template analysis, not a generic outline and not a visual mood board.

## 1. Classify the deck before choosing a layout

Pick one primary story type. A deck may contain supporting pages from other types, but it must have one dominant route.

| Story type | Audience needs to believe | Default narrative route | Visual priority |
| --- | --- | --- | --- |
| Competition defense | The project solves a real problem and is credible. | problem -> response -> proof -> product -> next step | real evidence and judge-facing conclusion |
| Product showcase | The product is useful, differentiated, and ready for its scenario. | user context -> product reveal -> key experience -> proof -> rollout | product, user scene, interface or physical detail |
| Technical project review | The method and validation are sound. | challenge -> method -> technical decision -> verification -> limitation | real diagrams, data, and implementation artifacts |
| Research / paper briefing | The finding is meaningful and well-supported. | question -> method -> finding -> implication | figure, chart, sample, and concise interpretation |
| Project update | The audience can decide what is done and what happens next. | objective -> progress -> evidence -> blocker -> decision | milestones, screenshots, and ownership |

If the material does not make the story type, audience, page limit, or desired outcome clear, ask at most two focused questions before visual production. Ask only questions that materially change the deck. For example:

- "This is a product showcase or a competition defense? The visual route differs: product reveal first versus problem-and-proof first."
- "Which real screenshots, photos, or product renders must appear as the primary evidence?"

If the answer is not critical, record a reasonable assumption in the content analysis and keep the affected zone replaceable.

## 2. Split a supplied document into presentation material

Read the structure before copying any wording. Extract and label:

1. **Decision context**: audience, competition criteria, required sections, page/time limit, and the action the audience should take.
2. **Narrative material**: problem, user or scene, approach, implementation, proof, differentiation, limitation, next step.
3. **Proof material**: numbers, tables, model comparisons, screenshots, product photos, certificates, papers, logs, and demonstrations.
4. **Visual material**: what can become a large real image, a central transformation, a comparison, a material texture, or a scenario scene.
5. **Gaps**: content that is unsupported, still evolving, contradictory, or missing the necessary real asset.

Do not treat document headings as slide headings. Reorder the material into an audience decision route.

## 3. Produce the content analysis before page design

Fill `templates/content-analysis.md`. It must contain:

- What this deck is and who it is for.
- The one decision or impression it needs to create.
- The primary story type and the narrative route.
- A content inventory: verified claims, real visual assets, required inserts, and gaps.
- A visual-ingredient inventory: product, material, environment, process, people, device, sample, chart, or document that belongs in the visual world.
- A style decision with a reason. Do not write only "technology style" or "premium dark blue".
- The questions to ask, or explicit assumptions when no question is needed.

Show this analysis to the user before bulk template generation when the deck is important, the source is ambiguous, or the visual direction is not already approved. If the user asks for direct production and the material is clear, save the analysis in the project folder and continue.

## 4. Analyze the layout, then design a template contract for every page

Before generating a page image, finish the slide's content plan and layout analysis inside the page blueprint. Then write a template contract. The image-generation prompt must encode the completed contract; it must never be generated before the layout is decided. It must specify all of the following:

| Field | Required decision |
| --- | --- |
| Page role | Why this page exists in the story and what it must make the audience believe. |
| Background scene | A project-specific setting, material, product context, or deliberately quiet surface. Never just "dark technology background." |
| Primary visual | The one largest image, product, object, chart, real screenshot, or evidence artifact. |
| Supporting visual ingredients | Relevant object, detail crop, material, annotation, illustration, or document cluster that prevents the page from becoming empty. |
| Real-asset slots | Exact supplied screenshot/photo/chart/certificate to insert, its aspect ratio, crop focus, and position. |
| Text zones | Title, main claim, detail blocks, and conclusion: location, maximum amount, and relative size. |
| Editable overlays | Only labels, captions, crops, highlights, or data that must remain editable. |
| Contrast and palette | Light / mid / dark mode and why it helps this page. |
| Avoid list | What would make this page generic, cramped, or off-topic. |

A valid template image has a visible subject and a planned composition. It is not a stock photo darkened behind three rectangles, a line-art wireframe, or a single repeated card layout.

Every content page needs one bespoke whole-slide template image derived from this contract. Technical, comparison, and screenshot pages use a quieter template image, not a native-layout exception. Cover and closing pages use their own hero/conclusion template contract rather than the dense content-page pattern.

## 5. Choose style from the subject, not from the word "AI"

Do not default to black, navy, cyan glow, HUD lines, or English micro-labels because a project mentions AI. Choose a visual system from the actual subject and vary page contrast deliberately.

| Subject | Useful visual direction | Avoid |
| --- | --- | --- |
| Physical product / hardware | product studio, material close-up, process setting, controlled highlights | abstract data tunnel with no product |
| AI vision / manufacturing | real material or process, camera optics, sample detail, restrained diagnostic cues | every page as dark blue cyber UI |
| Consumer application | real user context, product color, daylight, clean editorial composition | industrial HUD treatment |
| Medical / health | clinical whitespace, imaging, humane detail, calm green/blue support | aggressive neon or gaming visual language |
| Culture / education | editorial imagery, paper/material texture, warm neutral or vivid subject color | generic corporate technology template |
| Sustainability / agriculture | site imagery, natural material, daylight, green/earth accents | dark machine-space without a scenario |

Keep title behavior and typography stable, but use at least two contrast modes when the content benefits from it. Cover, transition, product reveal, and conclusion can be rich; evidence-heavy pages may be quiet; not every page should be dark.

## 6. Product showcase route

For a product display, do not start with a feature catalogue. Plan the pages around the product's visible value:

```text
real user or operating scene
  -> product reveal and one-sentence promise
  -> key interaction or workflow
  -> proof, details, or comparison
  -> deployment / adoption path
```

Use the actual product, interface, physical object, or prototype as the largest visual whenever it exists. A feature page must show a product detail or interaction state, not merely a list of functions.

## 7. Template acceptance gate

Before building an editable PPT page, inspect the template against its contract. Regenerate the underlay when any answer is no:

- Does the image visibly belong to this project's subject and this page's message?
- Is the primary visual large enough to matter?
- Are the real-image and text zones intentional, not improvised afterward?
- Does the composition have enough visual ingredients without turning into decorative clutter?
- Is this page structurally different from adjacent pages while still in the same visual family?
- Does the palette serve the content rather than repeating a default dark-AI style?
- Was this background template generated only after the page's content zones, real-asset slots, and layout were recorded?
- Can every real screenshot and editable text block sit in its planned zone without adding a new card wall over the template?
