# Rendered PPT Quality Gates

Perform these checks on exported slide images, not just in the PowerPoint editor.

## Factual integrity

- Every metric, capability, award, and comparison claim is traceable to source material.
- Future plans are labeled as future plans.
- Real screenshots and certificates are never replaced by synthetic equivalents when the originals exist.
- No placeholder labels, production notes, or accidentally generated gibberish remain.

## Readability

- The title is readable at normal viewing size and matches the deck hierarchy.
- Body text is not smaller than the deck's defined minimum without a justified exception.
- No text crosses a border, is clipped, overlaps an image, or wraps into a visually accidental shape.
- Chinese copy is not replaced by unexplained English-only labels.
- Captions are attached to the evidence they describe.

## Composition

- There is one clear primary visual anchor.
- Content density matches the slide purpose: rich when needed, quiet when needed.
- Dense pages use a calmer background; light pages use a stronger scene.
- The page does not repeat the exact layout of its neighbors.
- Decoration supports the subject rather than filling empty space.
- At least 0.3 inch of visual breathing room separates unrelated content groups.
- The page is not merely a dark stock image with evenly spaced translucent boxes.
- The background scene, product, material, device, person, sample, or evidence treatment visibly belongs to the page subject.
- The deck does not default to the same black/navy/cyan "AI" treatment on every page unless that direction was explicitly approved.

## Template-first integrity

- Every content slide has an associated bespoke generated or art-directed whole-slide background template file; quiet technical pages are not exceptions.
- The visual underlay was designed for this page's content zones.
- The page blueprint includes a completed template contract before the template was generated.
- The template was generated after the layout analysis documented its text zones, real-asset slots, aspect ratios, and crop focus.
- New objects are not merely covering defects in an old background.
- Editable text and evidence align to intentional zones in the template.
- The template has no fake readable text or fake product screenshots.
- No content slide consists only of native shapes or cards on a flat/default background.

## Approval gate

Archive only pages that pass the rendered visual review and are explicitly approved by the user.

## Distribution check

Before publishing a release, validate the package as an installer sees it:

```powershell
.\scripts\validate-distribution.ps1
```

This verifies the YAML front matter and runs the local package through `npx skills add <local-path> --list`. After the remote release is visible, add `-Remote` to verify the GitHub clone path as well. A repository can look correct in GitHub while still being undiscoverable if `SKILL.md` front matter is malformed.
