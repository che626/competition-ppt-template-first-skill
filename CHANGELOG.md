# Changelog

## 0.6.0 - 2026-07-13

- Made the per-page image-template flow mandatory: analyze the exact slide layout first, generate one bespoke whole-slide background template image from that plan, then place editable text and real evidence.
- Removed the native-layout exception for dense technical, comparison, iteration, and screenshot pages; these now require quieter generated templates with documented evidence and text zones.
- Added a template image execution contract, acceptance record, and rendered QA checks for layout-derived background templates.
- Clarified the cover and closing as separately composed hero/conclusion pages, while retaining their own whole-slide visual backgrounds.

## 0.5.0 - 2026-07-13

- Added a mandatory content-to-template analysis before page production: deck type, audience decision, narrative route, visual-ingredient inventory, gaps, questions, and style rationale.
- Added a per-page template contract covering the background scene, primary visual, supporting visual ingredients, real-asset slots, text zones, contrast mode, and avoid list.
- Added product-showcase routing so product, prototype, and real interface states become the visual anchor instead of a generic feature catalogue.
- Removed the implicit dark-blue/cyan AI default. Templates must derive their palette, scene, material, and light/dark distribution from the subject and page role.
- Added content analysis to report-grounded workspace initialization, public documentation, prompt recipes, visual prompts, and rendered QA.

## 0.4.3 - 2026-07-13

- Reframed the public workflow as a practical core path plus an optional report-grounded path.
- Limited detailed source tracking to metrics, comparisons, awards, and other claims that need proof.
- Clarified that full-page visual templates are most useful on visual-led pages, while dense technical pages may use quieter layouts.
- Relaxed unnecessary production gates while preserving the no-fabrication rule and editable evidence layers.

## 0.4.2 - 2026-07-12

- Fixed installed-package validation so unrelated global Skills are not scanned.

## 0.4.1 - 2026-07-12

- Added release-maintenance validation for package structure, front matter, and local Markdown links.
- Added a GitHub Actions workflow to run the static checks on every push and pull request.
- Added `.gitattributes` to keep text files normalized as LF across operating systems.

## 0.4.0 - 2026-07-12

- Moved the installable Skill into `skills/competition-ppt-template-first/`.
- Ensured the `skills` CLI installs references, templates, examples, scripts, and discovery metadata with `SKILL.md`.
- Kept the repository root as a GitHub-facing homepage and release surface.

## 0.3.0 - 2026-07-12

- Added report-grounded defense-deck mode for turning project documents and evidence into a traceable PPT route.
- Added mandatory source ingestion, source locators, fact IDs, evidence IDs, and slide-source mapping.
- Added source-manifest and slide-source-map templates plus a workspace initialization script.
- Added document-to-defense prompt recipes and source-ingestion documentation.

## 0.2.1 - 2026-07-12

- Fixed strict YAML parsing for `SKILL.md` discovery by the `skills` CLI.
- Added a `skills.sh` installation-count badge and local/remote installer-discovery smoke test.

## 0.2.0 - 2026-07-12

- Added an Agent Skill discovery descriptor at `agents/openai.yaml`.
- Added a GitHub-ready bilingual project homepage with install and usage examples.
- Added project-state conventions, a deck brief, revision record, and copy-ready prompt recipes.
- Added a domain-aware template-image prompt library.
- Added a signature-slide approval gate before full-deck production.
- Added contribution guidance for rights-cleared, reusable methods.

## 0.1.0 - 2026-07-12

- Initial template-first competition PPT workflow.
