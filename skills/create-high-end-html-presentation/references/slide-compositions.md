# Slide composition library

A composition is a communication structure, not a fixed template. It defines what receives attention, how evidence is arranged, and how much content the slide can carry. Adapt its proportions, type, colour, and imagery to the deck's design system.

## Contents

- Selection rule
- Title field, section threshold, and thesis field
- Split argument, evidence chart, and metric proof
- Diagram stage, comparison field, and demonstration stage
- Decision close
- Sequence, variation, and starter primitives

## Selection rule

Choose the composition after writing the slide's claim and visual job:

| Communication job | Default composition |
|---|---|
| Establish the premise | Title field |
| Mark a genuine narrative shift | Section threshold |
| State or resolve one important idea | Thesis field |
| Relate explanation and evidence | Split argument |
| Prove with a quantitative pattern | Evidence chart |
| Prove with a few decisive measures | Metric proof |
| Explain mechanism or topology | Diagram stage |
| Compare alternatives or states | Comparison field |
| Demonstrate interactive depth | Demonstration stage |
| State the implication or decision | Decision close |

## 1. Title field

**Job:** establish subject, tension, and promise.

**Anatomy:** restrained metadata, one strong title, optional one-sentence promise. Keep the title and negative space dominant.

**Limit:** no agenda grid, architecture, or KPI inventory.

## 2. Section threshold

**Job:** signal a real change of question, time horizon, or argument.

**Anatomy:** section proposition, short orientation line, distinctive but related field treatment.

**Limit:** use sparingly. A divider without a narrative seam wastes a slide.

## 3. Thesis field

**Job:** make one idea memorable or resolve the previous evidence.

**Anatomy:** takeaway title, one supporting sentence or a single visual motif, generous negative space.

**Limit:** if the support requires a list, choose split argument or evidence chart.

## 4. Split argument

**Job:** connect explanation with evidence, cause with effect, or before with after.

**Anatomy:** asymmetrical 35/65 or 40/60 field; one side frames the claim, the other carries the visual evidence. A rule or whitespace establishes the seam.

**Limit:** each side must play a different role. Two equal text boxes are not an argument.

## 5. Evidence chart

**Job:** reveal a quantitative pattern and its consequence.

**Anatomy:** takeaway title, dominant chart, short annotation, compact source and evidence state. Remove non-essential axes, legends, and tooltips.

**Limit:** one analytical question per chart slide. Small multiples are acceptable only when their shared scale enables comparison.

## 6. Metric proof

**Job:** substantiate progress or scale with two to four decisive measures.

**Anatomy:** one headline claim followed by aligned numbers with definitions, dates, and states. Use rules or spacing rather than repeated dashboard cards.

**Limit:** numbers must form one proof set. Unrelated KPIs belong on separate slides.

## 7. Diagram stage

**Job:** explain movement, convergence, dependency, sequence, or transformation.

**Anatomy:** claim-stating title, one dominant diagram, minimal stage labels, and a caption that states what the mechanism proves. Reveal in speaking order when sequence matters.

**Limit:** an architecture with roughly 15 or more elements becomes an overview plus focused detail slides or drill-down states.

## 8. Comparison field

**Job:** make differences, trade-offs, or change visible.

**Anatomy:** aligned columns, rows, or mirrored fields with identical comparison dimensions. Use semantic HTML tables when exact repeated fields matter.

**Limit:** preserve common scales and vocabulary. Do not compare through unrelated card shapes or inconsistent encodings.

## 9. Demonstration stage

**Job:** let the presenter explore one analytical path without abandoning the narrative.

**Anatomy:** stable title and context, dominant interactive visual, subordinate Back/Reset/Guided controls, visible current level, and an explicit illustrative label when required.

**Limit:** one interaction model per slide. The default state must already communicate the main claim.

## 10. Decision close

**Job:** resolve the opening and state the implication, recommendation, or decision.

**Anatomy:** conclusion phrased as an action or direction, one supporting proof line, and optional next step.

**Limit:** do not introduce new evidence or end with a generic thank-you.

## Sequence and variation

- Vary adjacent silhouettes when the narrative permits: text field → diagram → evidence chart → metric proof.
- Repeat a composition when repetition itself communicates comparison or cadence.
- Keep one dominant composition per slide; embedded panels remain subordinate.
- Add a slide rather than miniaturising two full compositions into one viewport.

## Starter primitives

The starter supplies neutral classes for these jobs: `.title-slide`, `.metric-line`, `.split-field`, `.comparison-field`, `.diagram-stage`, `.quote-stage`, `.chart-layout`, and `.close-slide`. Treat them as layout scaffolding. Brand-derived tokens and the claim determine the final appearance.
