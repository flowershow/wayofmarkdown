---
title: "Diagram language"
publish: false
---

# Diagram language (v1, 2026-10-03)

Two modes, one style. Stick figures are parked for now (wom-b5o.15).

- **Anatomy** (isometric): "what's inside X". Plates are parts of one thing; leaders name the parts. From the front-page figure, "Inside a markdown file".
- **Map** (flat, a technical drawing): routes, flows, roadmaps. A heavy orange rail is the main way; stops are square boxes on it with an orange serif number; optional side trips are lighter boxes joined by dotted right-angled wires. Used by the roadmap (roadmap.sh's grammar, in our style). Don't use anatomy mode for a route: leader labels read as captions, not destinations. The isometric roadmap that taught us this is backed up in `docs/brand/diagrams/roadmap-iso-2026-10-03/`.

Shared style:

- **Plates** (anatomy). Flat isometric slabs: a white top with an orange line (#ff5a00, about 1.2px) and a thin orange-tinted side. A plate is a thing: a file, a layer, a stage.
- **Leaders** (anatomy). Horizontal orange hairlines from the thing to a label, ending in a small arrow. Labels are IBM Plex Mono, ink-coloured, no boxes.
- **Numbers** in Newsreader, orange. Text that lies on a plate runs along its long axis.
- **State.** Solid line = done; dashed = in progress; dotted grey = planned.
- **Ground.** On a page, sit diagrams straight on the paper or on the dot-grid panel with an orange edge (homepage). No shadows, no rounded corners, no extra colours, no emoji.
- **As code, never by hand.** Primitives: `scripts/isokit.py` (anatomy: `Iso`, `plate`, `text_on`, `leader`; map: `box`, `wire`; and the CSS). A wide diagram goes in `<div class="ik-wide">` to break out of the text column. Inline SVG picks up the site's light and dark tokens; for `<img>` files, bake the colours in (see `scripts/build-site-art.py`).

In use: the homepage figure (`docs/brand/round-4/makingsoftware/iso.py`, to be moved onto `isokit`) and the roadmap (`scripts/roadmap-gen.py`).

## Motion

Map diagrams can move, gently, while the drawing itself stays still: one ball runs the route (round the edge of each stop), each stop lights up as the ball arrives and stays lit, dots run out to that stop's side trips at the same speed (about 80px a second), and a burst of tracers marks the destination. Then a short rest, everything resets, and the loop restarts (about 37 seconds for the roadmap). Everything moving sits in `<g class="moving">` and is hidden under `prefers-reduced-motion`.

**CSS animation only.** SVG's own animation tags (`<animate>`, `<animateMotion>`) break Flowershow pages: the renderer lower-cases them and the rest of the page after the diagram disappears (found 2026-10-03, reverted). Use CSS keyframes, `offset-path` for things that travel along a line, and `stroke-dashoffset` for tracers. See `animation()` in `scripts/roadmap-gen.py`.
