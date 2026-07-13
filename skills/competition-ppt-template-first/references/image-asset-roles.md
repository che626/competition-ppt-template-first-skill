# Image Asset Roles

Use `templates/image-asset-register.md` at source intake. This prevents a common competition-PPT failure: generated background art, authentic screenshots, source images, and decorative objects are all treated as interchangeable.

## Classify before use

| Role | It can do | It cannot do |
| --- | --- | --- |
| `style-reference` | Set mood, composition, light, material, or page rhythm | Prove a project claim or become an uncredited factual image |
| `template-underlay-source` | Supply the background visual world for one page | Replace a real screenshot, certificate, chart, or measured result |
| `real-evidence` | Show authentic product behavior, samples, documents, certificates, or measured output | Be regenerated, relabeled, or materially altered |
| `replaceable-screenshot` | Show the actual system while remaining easy to update | Be converted into a synthetic dashboard or distorted until unreadable |
| `decorative-cutout` | Add a subject-specific physical object or material detail | Compete with the primary claim or fake evidence |

## Image-generation contract

1. Write the page blueprint first, then name every input image and its role in the prompt record.
2. Generate one deliberate template for each distinct page composition. Do not ask for generic variants and retrofit them to unrelated pages.
3. For image editing, list invariants explicitly: what must stay unchanged, which crop must remain recognizable, and which UI or evidence content cannot change.
4. Keep generated readable text, synthetic UI, and synthetic evidence out of template images.
5. Store the selected template, prompt, and input-role record inside the project. Keep rejected variants separate.

## Screenshot framing

Before inserting a system screenshot, record its aspect ratio, crop focus, whether the entire UI must remain readable, and the frame treatment from the deck tokens. Prefer clean framing, proportional contain/crop behavior, and clear captions. Do not redraw the screenshot merely to make it look more futuristic.
