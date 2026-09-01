# Charts and diagrams

## Contents

- Engine decision and figure discipline
- ECharts, convergence, networks, and formal diagrams
- Comparisons, pipelines, historical views, and drill-down
- Visual honesty

## Engine decision

| Visual job | Preferred engine | Why |
|---|---|---|
| Time series, bars, scatter, waterfall | ECharts | Responsive scales, animation, tooltips |
| Source convergence or hub-and-spoke | ECharts `lines` + `scatter`, or `graph` | Layout and transition state stay data-driven |
| Interactive portfolio drill-down | ECharts + explicit JavaScript state | Smooth updates without leaving the slide |
| Linear ingestion pipeline | HTML/CSS flex or grid | Exact alignment and reliable labels |
| Strategy timeline | HTML/CSS grid | Editorial control and predictable spacing |
| Comparison, audit, status matrix | Semantic HTML `<table>` | Exact repeated fields remain aligned and accessible |
| Sequence, ER, state, class, C4, formal topology | Mermaid | Automatic layout preserves formal relationships |
| 15+ element architecture | Hybrid overview + focused detail | Orientation remains legible without losing depth |
| Technical draft | Mermaid | Fast authoring and automatic layout |
| Bespoke illustration | Custom SVG | Only when the image itself is unique |

## Figure discipline

- Write the figure's claim before selecting the engine.
- Give one figure one primary claim; state it in the slide title or a concise caption.
- Label meaningful edges with an action, payload, or transformation. An unlabeled arrow means only “related.”
- Use the same object names in the diagram, presenter copy, and drill-down state.
- Provide a readable fallback or textual equivalent when a library is unavailable.

## ECharts principles

- Use Canvas for presentation diagrams unless vector export is a requirement.
- Store nodes, links, labels, statuses, and chart values as data.
- Read colours from slide-level CSS variables so charts adapt to light and dark sections.
- Use stable `id` values and `setOption` updates for morphs and drill-downs.
- Disable roam, zoom, legends, axes, and tooltips when they do not support the slide's claim.
- Use subtle animation: approximately 600–1,200 ms with cubic easing.
- Keep chart labels short enough to remain inside nodes at the target viewport.

## Progressive convergence

For “many sources become one governed platform”:

1. Place sources in disciplined left/right lanes or aligned rows.
2. Keep the platform on a clear central axis.
3. Reveal links sequentially after nodes reach their final positions.
4. Use low-opacity connectors and stronger node hierarchy.
5. Preserve source identity; convergence means shared truth, not visual collapse.

Avoid arbitrary radial positions, crossing edges, connector lines through labels, and simultaneous motion of every element.

## Network and source-estate diagrams

- Use radial layouts only when the central relationship is genuinely the message.
- Prefer a ring with consistent node sizes and status-coloured borders.
- Reduce link opacity enough that nodes remain primary.
- If more than eight sources are shown, group by category, status, or ingestion method.
- When statuses matter more than relationships, replace the network with aligned status lanes.

## Formal technical diagrams

- Use Mermaid for sequence, ER, state, class, or C4 diagrams when the formal relationship is the message.
- Prefer top-down flow for complex topology; reserve left-to-right for simple linear sequences.
- Apply the deck palette through Mermaid's base theme, then verify label and edge contrast at presentation scale.
- If the figure needs extensive zooming or more than roughly 15 elements, show a smaller overview and move focused mechanisms to later slides or interactive detail.
- Replace Mermaid with ECharts or HTML/CSS when precise stagecraft, morphing, or brand-specific composition is more important than automatic layout.

## Comparison and matrices

- Use a semantic table when the audience must compare exact repeated fields.
- Use aligned typographic columns for lighter before/after comparisons.
- Use a chart only when magnitude or pattern—not the cell values—is the message.
- Keep vocabulary and scale consistent across both sides.

## Pipelines

- Use HTML/CSS for deterministic source → transfer → storage → transform → product → consumption sequences.
- Keep connectors behind nodes.
- Animate progress along the line; do not animate node position.
- Distinguish raw, governed, and output stages through labels or restrained fills.
- Use one pipeline per slide when the audience must understand the mechanism.

## Historical versus snapshot

Use a split composition:

- Left: a small stack of snapshot files representing overwrite-based history.
- Right: a continuous ECharts time series with retained periods.
- Caption the implication: queryable history enables comparison and trend analysis.

## Drill-down

Represent the hierarchy as explicit state:

```text
Portfolio → Sector → Property → Project → Cash flows
```

For each level, store title, explanatory copy, KPI values, chart labels, and chart values. Update the same chart instance rather than navigating to separate appendix slides. Provide Back, Drill deeper, and optional Guided demo controls. Label placeholder data as illustrative on every level.

## Visual honesty

- Do not encode unsupported precision.
- Do not use area, length, or colour as quantitative encodings unless a legend or label makes the mapping clear.
- Keep comparisons on consistent scales when the comparison is meaningful.
- Use annotations to explain why the pattern matters.
