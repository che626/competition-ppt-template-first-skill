# Source Ingestion: Project Documents to Defense Route

## Goal

Transform a project package into a concise defense or product route without inventing claims or dumping report text into slides. The output of this phase is not a PPT. It is a traceable content-and-visual base that makes later page and template decisions clear.

## What to collect

Use `templates/source-manifest.md` to record every supplied item:

| Source type | Extract | Use in the deck |
| --- | --- | --- |
| `.docx` / Markdown / proposal | headings, claims, tables, captions, conclusions | narrative, fact IDs, tables, speaker logic |
| PDF | text plus rendered pages where charts, figures, or layout matter | page citations, charts, figures, award evidence |
| `.pptx` | slide intent, reusable media, speaker notes, approved visual rules | reference style, reusable evidence, prior claims to verify |
| `.xlsx` / CSV | verified metrics, units, dates, comparisons | charts, model comparison, KPI evidence |
| screenshots / photos / video frames | subject, aspect ratio, credibility, visible labels | real visual anchors and evidence zones |
| competition brief | judging dimensions, required sections, time/page constraints | deck order and emphasis |

## Required extraction sequence

1. Create a source manifest and give every source an ID such as `S-01`, `S-02`.
2. Read document structure before writing any slide copy: title, abstract, problem, user or operating scene, method, product, results, limitations, roadmap, awards, appendices.
3. Classify the deck and audience before choosing layouts. Decide whether it is primarily a competition defense, product showcase, technical review, research briefing, or project update.
4. Fill `templates/content-analysis.md`: identify the audience decision, narrative material, proof material, visual material, visual ingredients, gaps, questions, and a subject-derived visual direction.
5. Extract facts into the fact registry. Each fact gets `F-xx`, a source locator, status, and allowed wording.
6. Extract visual evidence into the evidence inventory. Each image, figure, chart, screenshot, certificate, table, product view, or sample gets `E-xx`, plus the page role and crop focus it can support.
7. Mark all unsupported, outdated, ambiguous, or contradictory claims in the do-not-claim section.
8. Build the slide-source map. A slide cannot be templated until its conclusion, real-asset needs, visual anchor, and story transition are visible.

## Source locator format

Use a locator another person can find without guessing:

- Word / Markdown: `S-01 / 3.2 Model deployment / paragraph 2`
- PDF: `S-02 / p.14 / Table 3`
- Spreadsheet: `S-03 / Metrics / B8:F12`
- PPTX: `S-04 / Slide 7 / screenshot cluster`
- Asset: `S-05 / system-dashboard.png / upper navigation`

Avoid vague locators such as `the report`, `user said`, or `some screenshot`.

## Convert a report into a defense narrative

A report normally follows a documentation order. A defense should follow a judge's decision order:

```text
Why this problem matters
  -> what is fundamentally broken
  -> how the design responds
  -> why the technical choice is credible
  -> what has actually been built and verified
  -> why it is differentiated
  -> what the next grounded step is
```

Do not copy chapters directly into slides. Reorder facts to support this route. Keep one judge-facing conclusion per page and give every page a transition that makes the next page feel necessary. For a product showcase, use the product route in `references/content-to-template-analysis.md`: context -> product reveal -> key experience -> proof -> rollout.

## Input quality rules

- Preserve original files. The project work folder stores manifests and extracted notes, not destructive rewrites of user documents.
- Use supplied screenshots and figures whenever they prove a claim better than generated imagery.
- If a document contains an attractive but unverified claim, keep the original wording in the notes but do not promote it to a slide claim.
- Future work must be visually and verbally separated from completed work.
- When source material is late or incomplete, reserve a clearly replaceable evidence zone instead of fabricating a result.
- A supplied product, sample, device, screenshot, person, environment, material, or document should become a visual ingredient in the page plan when it explains the subject better than generic decoration.

## Exit criteria

Do not move into visual template generation until:

- Every planned page has a primary conclusion.
- `content-analysis.md` states the deck type, audience decision, narrative route, visual ingredients, style rationale, and any focused questions or assumptions.
- Every conclusion has fact IDs or is labeled as a future plan.
- Real evidence is mapped to the pages that need it.
- Every page has a visual anchor, real-asset requirement, and template contract in its page blueprint.
- Contradictions and missing information are visible in the fact registry.
- The deck brief states page count, target audience, judging focus, and language.
