# Copy-Ready Prompt Recipes

## 1. Full competition deck from a report

```text
$competition-ppt-template-first
Read [report path], [competition requirements], and all files in [assets folder].
Create a [page count]-page Chinese competition defense deck for [competition name].
All claims must be traceable to the report. Use the supplied screenshots and artifacts as real evidence.
Before creating the deck, write a deck brief, fact registry, and page-by-page blueprint.
Then generate one dense representative signature-slide template for approval.
Do not start bulk slide production until the signature slide is approved.
```

## 1A. Feed a complete project package into the skill

```text
$competition-ppt-template-first
Use report-grounded defense-deck mode. Read every document in [project materials folder],
the competition brief at [path], and the real screenshots in [assets folder].
First initialize a report-grounded workspace. Then give each document a source ID,
extract verified facts and evidence IDs with exact section/page/table locators, and create a slide-source map.
For every proposed slide, show: the judge question, the page conclusion, its fact IDs,
its real evidence, and the transition to the next page.
Only after I confirm this route should you generate the signature-slide template.
```

## 2. Repair a weak existing page

```text
$competition-ppt-template-first
Review [PPTX or exported page image] against the source report and the existing deck style.
This page feels [too empty / too boxy / too generic / unable to hold text].
Diagnose whether the problem is content, composition, or the bottom template.
If the bottom template is wrong, regenerate the whole template and rebuild the editable page;
do not cover the old layout with new frames. Preserve the previous page as retired.
```

## 3. Build a system-showcase page from real screenshots

```text
$competition-ppt-template-first
Use the real screenshots in [folder] to design one [title] competition-defense page.
The screenshots are the main proof and must remain recognizable. First tell me which screenshots
will be used and where they will sit. Generate a quiet dark template around their required aspect ratios,
then build the layered editable PPT and render a preview for QA.
```

## 4. Build an evidence / awards page

```text
$competition-ppt-template-first
Create an awards-and-results page using the real papers, certificates, and records in [folder].
Group the artifacts by what they prove, not only by file type. Use a readable evidence-wall composition
with a concise argument column. Do not generate replacement certificates or put the real documents in tiny slots.
```
