---
title: "Diagram language"
publish: false
---

# Diagram language (v1, 2026-10-03)

Taken from the front-page figure, "Inside a markdown file". Use it for explanatory diagrams; stick figures are parked for now (wom-b5o.15).

- **Plates.** Flat isometric slabs: a white top with an orange line (#ff5a00, about 1.2px) and a thin orange-tinted side. A plate is a thing: a file, a layer, a stage.
- **Leaders.** Horizontal orange hairlines from the thing to a label, ending in a small arrow. Labels are IBM Plex Mono, ink-coloured, no boxes.
- **Numbers** in Newsreader, orange. Text that lies on a plate runs along its long axis.
- **State.** Solid line = done; dashed = in progress; dotted grey = planned.
- **Ground.** On a page, sit diagrams straight on the paper or on the dot-grid panel with an orange edge (homepage). No shadows, no rounded corners, no extra colours, no emoji.
- **As code, never by hand.** Primitives: `scripts/isokit.py` (`Iso`, `plate`, `text_on`, `leader`, and the CSS). Inline SVG picks up the site's light and dark tokens; for `<img>` files, bake the colours in (see `scripts/build-site-art.py`).

In use: the homepage figure (`docs/brand/round-4/makingsoftware/iso.py`, to be moved onto `isokit`) and the roadmap (`scripts/roadmap-gen.py`).
