# Motion and interaction

## Motion hierarchy

Use motion to explain sequence, state, or causality:

1. Slide transition
2. Progressive content reveal
3. Diagram or chart update
4. Optional hover or tooltip detail

Do not make all four compete at once.

## Timing

- Slide fade/translate: 500–850 ms
- Chart update: 600–1,200 ms
- Pipeline stage cadence: 220–380 ms
- Guided drill-down cadence: 1,200–1,800 ms per level

Use a shared cubic easing curve. Avoid bounce, elastic motion, constant parallax, and decorative looping animation.

## Presentation controls

Support:

- Left/right arrows and Page Up/Page Down
- Space to reveal the next fragment, then advance
- Fullscreen shortcut
- URL hash or query state for shareable slide and design-variant links
- Visible on-screen navigation for non-keyboard use
- `prefers-reduced-motion`

Do not capture arrow keys while an input, textarea, or editable element has focus.

## Progressive reveals

- Reveal evidence in the order the presenter speaks about it.
- Start diagrams with a readable stable state.
- Use opacity and short vertical translation; avoid blur-heavy or large-distance movement.
- Keep unrevealed content faint only when its future position helps explain the structure. Otherwise hide it.

## Interactive depth

- Keep the main narrative linear and rehearsable.
- Add interactivity on selected “mini-application” slides only.
- Make Back and reset behaviour obvious.
- Preserve the current slide while the chart morphs.
- Provide a guided mode for demonstrating the full path without precise clicking.
- Use real data only when the user supplies it; otherwise label every value illustrative.

## Design variants

During prototyping, expose no more than five structurally distinct variants through a query parameter and a visually separate switcher. Remove or hide the switcher in the approved deliverable.
