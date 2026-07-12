# Competition PPT Template-First Skill

`competition-ppt-template-first` is a reusable skill for creating high-end competition and defense PPTs without falling into the usual "background + generic components + tiny text" trap.

Chinese documentation: [README.zh-CN.md](README.zh-CN.md)

It turns the workflow used for a successful AI vision competition deck into a repeatable method:

1. Ground the story in the source report and real evidence.
2. Plan every page before drawing it.
3. Generate a complete 16:9 visual template for the page.
4. Rebuild the approved image as a layered, editable PowerPoint.
5. Render and revise until the actual PPT is readable and visually coherent.

The result keeps the premium feel of an art-directed image while retaining editable factual content, real screenshots, charts, and award materials.

## When to use it

- Innovation and entrepreneurship competitions
- Technical product defenses
- AI, robotics, engineering, research, or industry project showcases
- Any high-stakes Chinese PPT that needs to look designed, not assembled

## What makes this different

| Conventional approach | Template-first approach |
| --- | --- |
| Start with PPT rectangles and text boxes | Start with a fact map and a page-level visual composition |
| Reuse one card layout everywhere | Use a stable visual system with varied slide archetypes |
| Use generated images as fake evidence | Reserve real screenshots and artifacts for evidence zones |
| Make everything editable, then accept mediocre design | Keep the template visual, but make facts and evidence editable |
| Patch rejected pages with extra frames | Regenerate the whole underlay when the composition is wrong |

## Installation

Clone this repository or place its folder in your Codex skills directory. The skill entry point is [`SKILL.md`](SKILL.md).

```text
competition-ppt-template-first-skill/
  SKILL.md
  references/
  templates/
  examples/
```

## Expected inputs

- A report, proposal, or source document
- Competition requirements and page-count target
- Real screenshots, charts, product photos, certificates, or test results when available
- A reference deck or visual direction, if the user has one

The skill explicitly distinguishes verified facts from missing material. Missing material becomes a planned editable region, never a fabricated claim.

## Typical output

- `fact-registry.md`: verified claims and evidence inventory
- `slide-map.md`: page-by-page story and visual plan
- Approved 16:9 template images
- Editable `.pptx` slides with separate background, evidence, and text layers
- Rendered previews plus a QA record

## Design philosophy

The preferred balance is dense but controlled: rich enough to feel competition-grade, calm enough to be read by judges. Use scene, material, light, credible imagery, and typographic scale to create visual interest. Avoid generic cyberpunk frames, repeated card walls, and tiny text.

See [`references/workflow.md`](references/workflow.md) for the full method and [`examples/ai-vision-defense-example.md`](examples/ai-vision-defense-example.md) for a generic AI-vision deck map.

## License

MIT. The skill contains no project screenshots, certificates, or proprietary competition material.
