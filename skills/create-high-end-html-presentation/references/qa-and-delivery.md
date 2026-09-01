# QA and delivery

## Static checks

Run `scripts/validate_html_deck.py` and resolve every error. Review warnings intentionally.

Confirm:

- Valid document shell and viewport metadata
- Language metadata and a self-contained favicon
- At least two uniquely identified slides and exactly one active slide in source
- Keyboard and pointer navigation
- Reduced-motion handling
- Visible focus styling, descriptive title, and accessible control labels
- No unresolved template tokens
- No undeclared remote or local dependencies
- Illustrative labels wherever figures are invented
- Captions for figures and accessible alternatives or fallbacks for charts

## Visual review

Serve the output locally and inspect every slide individually at the intended presentation viewport, normally 1440×810 or 1920×1080.

For every slide, check:

- No overlap, clipping, overflow, or unintended wrapping
- Consistent outer margins and alignment
- Readable body text, labels, footnotes, and controls
- Sufficient contrast in both slide and chart elements
- Clean connector routing and legible node labels
- Chart values, titles, units, axes, and tooltips agree
- Fixed controls do not cover slide content
- The selected composition matches the slide's communication job

Do not rely on a contact sheet alone; inspect full-size slides.

## Interaction review

Exercise:

- Previous and next slide
- Fragment reveal order
- Architecture before/after state
- Every pipeline animation
- Every drill-down level and reset path
- Variant switching, if retained
- Fullscreen and reduced-motion behaviour

Open a fresh browser tab after the final code change and confirm the browser log is clean.

## Coverage and specificity

- Reconcile the final deck against the source coverage map.
- Confirm each number's evidence state, unit, and date or period.
- Apply the specificity audit in `design-system.md`.
- Confirm that structural devices carry meaning: markers order, labels classify, and dividers separate real sections.

## Packaging

Prefer a single self-contained HTML file when practical. Otherwise deliver one HTML file with a clearly named local asset folder. Never leave silent CDN dependencies in a supposedly offline deck.

Use `scripts/inline_assets.py` to inline local JavaScript and CSS. Keep third-party licence notices intact when bundling libraries.

## Handoff

Deliver only audience-facing artifacts. State:

- Which version is recommended
- Which numbers are illustrative or awaiting replacement
- Whether the file is self-contained
- Which interactions are available

Keep the prototype marked until the user approves it for production use.
