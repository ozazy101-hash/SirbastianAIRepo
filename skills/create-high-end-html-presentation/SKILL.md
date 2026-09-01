---
name: create-high-end-html-presentations
description: Create or redesign polished, interactive HTML slide presentations with strong narrative structure, brand-derived colour systems, editorial or cinematic art direction, ECharts-powered charts and diagrams, restrained motion, drill-down interactions, and self-contained delivery. Use for browser-based decks, HTML presentations, interactive senior-management briefings, data-storytelling slides, web presentations derived from a brand site or visual reference, and requests to replace fragile SVG diagrams with a charting or layout engine. Do not use when the required final artifact is PowerPoint or Google Slides.
---

# Create high-end HTML presentations

Build presentation-first HTML: a controlled 16:9 narrative with optional analytical depth, not a scrolling website or a dashboard split into slide-sized pages.

## Workflow

1. Define the communication job in one sentence: by the end, the audience should understand, believe, decide, or do what—and because of which central takeaway.
2. Inventory supplied content, evidence, data, brand references, output requirements, and known placeholders. Read [evidence-and-coverage.md](references/evidence-and-coverage.md), then map every required source item to a slide, evidence state, and source locator. Ask only when audience, purpose, or a materially consequential choice is missing.
3. Read [narrative-and-layout.md](references/narrative-and-layout.md), then map one claim and one visual job to each slide. Read [slide-compositions.md](references/slide-compositions.md) and choose a composition by communication job rather than filling a template sequence.
4. When a brand reference, website, screenshot, or palette is supplied, inspect it and read [design-system.md](references/design-system.md). Derive semantic colour roles and layout behaviour rather than copying isolated hex values.
5. Choose one primary design posture:
   - **Editorial** for restrained, light, formal, publication-led decks.
   - **Cinematic** for dark-room narrative emphasis and sparse high-impact moments.
   - **Hybrid** for alternating narrative and evidence sections.
   - **Operating** for denser technical or delivery detail.
   Default to editorial for senior-management and investment audiences unless the reference strongly indicates another posture.
6. Select the simplest reliable visual engine. Read [charts-and-diagrams.md](references/charts-and-diagrams.md) whenever the deck contains charts, architecture, networks, timelines, pipelines, or drill-downs.
7. Build the deck. Start with `scripts/scaffold_deck.py` when no host application exists; otherwise work inside the existing HTML presentation. Keep presentation content and chart data separate from rendering functions.
8. Add motion only after static composition is sound. Read [motion-and-interaction.md](references/motion-and-interaction.md) for progressive reveals, transitions, keyboard control, fullscreen, and drill-down state.
9. Package local dependencies. Use `scripts/inline_assets.py` when a single self-contained HTML file is required.
10. Read [qa-and-delivery.md](references/qa-and-delivery.md). Render every slide at the intended viewport, exercise every interactive path, inspect browser logs, and fix all clipping, overlap, wrapping, contrast, and transition defects before delivery.

## Visual engine choices

- Use **Apache ECharts Canvas** for quantitative charts, animated graphs, source-to-platform convergence, time-series history, and interactive drill-downs.
- Use **HTML/CSS layout** for linear pipelines, KPI typography, editorial timelines, and content whose alignment is more important than topology.
- Use **Mermaid** for formal sequence, ER, state, class, or topology diagrams when automatic layout matters more than precise art direction; restyle or replace it when the deck requires a bespoke visual hierarchy.
- Use **custom SVG** only when the visual itself is genuinely bespoke and neither a chart layout nor HTML/CSS expresses it cleanly.
- Prefer progressive convergence lanes, aligned rows, or staged links over free-form network edges. Every connector must communicate direction or grouping.
- Split architectures with roughly 15 or more elements into a concise overview plus progressive detail, focused follow-on slides, or an interactive drill-down.

## Design guardrails

- Treat colour as a system: background, surface, ink, muted text, rule, primary accent, secondary accent, warning, and negative.
- Do not assume a brand palette implies dark mode. Match the reference's balance of light and dark fields.
- Use one dominant composition per slide. Keep controls and analytical affordances visually subordinate to the claim.
- Make structure truthful: sequence markers indicate sequence, eyebrows classify content, and dividers mark real narrative seams.
- Prefer flat editorial structure over card grids, ornamental pills, glowing nodes, and dashboard chrome.
- Keep large type disciplined: shortening copy is preferable to shrinking it or allowing accidental wraps.
- Label all invented figures, trends, properties, and cash flows as illustrative at the point of use.
- Preserve optional depth: the main sequence must stand on its own even when nobody opens a drill-down.
- Keep prototypes visibly marked until the user approves the design and content.
- Run the specificity audit in [design-system.md](references/design-system.md): if the palette, typography, and composition could fit an unrelated deck unchanged, revise the generic choices.

## Reusable resources

- `assets/starter/deck.html`: neutral 16:9 starter with slide state, navigation, progressive fragments, theming, reduced-motion support, and an optional ECharts chart.
- `scripts/scaffold_deck.py`: create a new deck directory from the starter and optionally add a local ECharts bundle.
- `scripts/inline_assets.py`: inline local script and stylesheet dependencies into one deliverable HTML file.
- `scripts/validate_html_deck.py`: run structural and packaging checks before browser QA.

## Completion criteria

Finish only when the coverage map accounts for every required source item, the deck is audience-ready, every required claim is present, every chart matches its stated meaning, illustrative data is labelled, all interactive states work, all slides have been visually inspected, the specificity audit passes, and the delivered file opens without relying on undeclared local or remote dependencies.
