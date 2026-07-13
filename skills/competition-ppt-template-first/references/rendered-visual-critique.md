# Rendered Visual Critique

Run this critique after the PPT has been exported to slide images. Evaluate the rendered result, not merely the editor's object bounds. Use `templates/rendered-visual-critique.md` to record findings.

## 1. Composition

Check balance, whitespace, rhythm, and grouping.

- Is the visual weight intentionally balanced or intentionally asymmetric?
- Is there enough macro space between unrelated groups and consistent micro space inside a group?
- Are large photos, dense text, and dark surfaces counterweighted rather than all pushed to one side?
- Does repetition create rhythm without turning the page into identical cards?
- Are related elements grouped by proximity, alignment, material, or clear visual continuity?

Rate `major` when the page is top-heavy, visually accidental, fragmented, or relies on a generic repeated-card wall. Fix the template or layout, not only a line or color.

## 2. Visual hierarchy

Check entry point, eye flow, weight, and emphasis.

- Does the viewer first notice the page's most judge-relevant claim or evidence?
- Does the eye move through the intended title -> evidence -> conclusion order without a dead end?
- Are size and contrast differences strong enough to distinguish title, claim, detail, caption, and metadata?
- Is there one primary emphasis zone, rather than several competing accent colors and bold blocks?

Rate `major` when decoration, background detail, or small labels overpower the primary claim. Rebuild the underlay or redistribute visual weight when needed.

## 3. Information density

Check cognitive load, content priority, scanning, and disclosure.

- Does the page make one clear judgment even when it contains multiple facts?
- Is evidence stronger than explanatory prose, and are secondary details visibly subordinate?
- Can the page be scanned in coherent blocks rather than read as a report paragraph?
- Is dense detail limited to the content needed for this page role, with optional elaboration left to speech or backup pages?

Rate `major` when unrelated facts compete at equal weight, body copy becomes a script, or empty decoration coexists with cramped explanations. Reflow, shorten, or use another layout family.

## 4. Typography

Check scale, readability, consistency, and contrast.

- Does every text role map to a deck token instead of an ad hoc font size or color?
- Is the hierarchy step between title, claim, body, and caption visibly meaningful?
- Is body copy readable at presentation size and safely within its intended zone?
- Are line breaks, alignment, weight, and caption offsets consistent?
- Does text contrast against the actual rendered background, not only against a nominal fill color?

Rate `major` when any text is clipped, too small, low contrast, accidentally wrapped, or visually detached from its evidence.

## Fix-and-verify rule

Do not call a deck visually complete after a review that merely says "looks good." Record at least the four ratings for every high-risk slide. When a `major` issue or user-reported defect exists, document the root cause, change the underlying layout/template or relevant token, re-render, and verify the affected slide again.
