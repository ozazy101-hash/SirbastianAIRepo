# Design system from a brand reference

## Extract behaviour before decoration

Inspect the reference at desktop presentation scale. Record:

- Dominant light/dark balance
- Page bands and section backgrounds
- Heading and body type families
- Heading scale and line length
- Content width and margins
- Rule weight, corner radius, and shadow strength
- Accent frequency
- Image treatment
- Navigation and button restraint

Do not infer “cinematic dark mode” from a dark logo or a single primary colour. Match how the brand allocates colour across the whole page.

## Write a design hypothesis

Before building, record one sentence connecting the design to the subject and audience. For example:

> A formal investment-strategy deck using paper-like light fields, aubergine editorial type, fine rules, and restrained teal signals so evidence feels governed rather than promotional.

Use the hypothesis to reject attractive choices that do not belong to this presentation.

## Convert colours into roles

Create semantic tokens rather than scattering hex values:

```css
:root {
  --bg: #ffffff;
  --surface: #f3f1f4;
  --surface-2: #ebe5ed;
  --ink: #2d1635;
  --muted: #665f68;
  --line: rgba(45, 22, 53, .17);
  --accent: #087e84;
  --accent-2: #6b3c77;
  --warning: #9a728f;
  --negative: #a55262;
}
```

Recalculate contrast after assigning roles. A colour that works as a logo fill may fail as body text or a chart line.

## Design postures

### Editorial

- White, grey, or pale brand-tinted fields dominate.
- Dark brand colour anchors headings, rules, and selective controls.
- Serif display type may pair with a neutral sans-serif body.
- Thin rules, square or lightly rounded geometry, and restrained motion carry the hierarchy.
- Use this for formal, investment, board, and strategy audiences.

### Cinematic

- Dark fields dominate; light evidence slides are rare.
- Large type and sparse composition create the pacing.
- Accent colour appears in controlled focal moments.
- Use when the room, subject, and reference support a dramatic delivery.

### Hybrid

- Use dark slides for narrative transitions and light slides for evidence.
- Make the alternation purposeful and section-based, not random.

### Operating

- Increase information density while preserving alignment and hierarchy.
- Use practical labels and restrained components.

## Typography

- Use no more than two families unless the brand requires more.
- Match the reference's typographic character before matching exact fonts.
- Keep title line breaks intentional and stable at the target viewport.
- Use uppercase tracked labels sparingly for section metadata.
- Use tabular numerals for KPI and financial figures when available.

## Specificity audit

Before delivery, ask:

- Could this palette and typography be transferred unchanged to an unrelated technology pitch?
- Does the composition reflect the content's actual domain, audience, and evidence?
- Do sequence numbers indicate sequence, eyebrow labels classify, and dividers mark real seams?
- Are surfaces, cards, pills, and shadows communicating hierarchy or merely filling space?
- Would the design remain recognisable if its most obvious accent colour disappeared?

Revise the generic answers. Prefer a few domain-specific decisions over a dense layer of decoration.

## RLAM case-study lesson

The useful lesson is not a fixed palette. It is the proportion: broad white and pale-lavender fields, aubergine editorial headings, fine rules, restrained teal signals, conventional alignment, and very limited dark-screen use. Apply the same extraction discipline to other brands.
