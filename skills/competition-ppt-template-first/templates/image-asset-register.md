# Image Asset Register

Register every image before it is used in a template or PPT. The role determines what may be changed and whether the image can support a factual claim.

```md
| Asset ID | File / URL | Asset role | What it shows | Truth status | Allowed transformation | Slide / slot | Aspect ratio and crop focus | Must stay recognizable? | Source / rights note | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-01 |  | `style-reference` |  | not evidence | color / material / composition reference only |  |  | No |  | available |
| A-02 |  | `template-underlay-source` |  |  | art direction / crop / tonal treatment |  |  | No |  | available |
| E-01 |  | `real-evidence` |  | verified evidence | crop / frame / non-destructive tonal adjustment only |  |  | Yes |  | available |
| S-01 |  | `replaceable-screenshot` |  | current product state | crop / contain / clean framing; do not synthesize UI content |  |  | Yes |  | available |
| D-01 |  | `decorative-cutout` |  | subject-specific support object | background removal / scale / placement |  |  | No |  | available |
```

## Role rules

- `style-reference`: never use as proof; extract only mood, composition, material, or typographic direction.
- `template-underlay-source`: may support the bottom visual template, but does not prove a claim by itself.
- `real-evidence`: use the supplied authentic image; never replace it with a generated equivalent. Preserve the meaningful region and attach a caption when required.
- `replaceable-screenshot`: keep interface text and controls truthful. Use clean framing and crop treatment, not generated fake UI.
- `decorative-cutout`: only use objects that belong to the subject. It may support the scene but must not become the primary evidence.

## Image-generation input record

For every generated or edited template, record:

- Generation / edit intent:
- Input assets and their registered roles:
- Exact page blueprint used:
- Prompt or art-direction record:
- Invariants that must be preserved:
- Output file path and selection status:
```
