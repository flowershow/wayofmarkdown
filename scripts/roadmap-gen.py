#!/usr/bin/env python3
"""Generate the visual roadmap SVG from map data (see docs/briefs/visual-roadmap.md).

Usage: python3 scripts/roadmap-gen.py            # regenerates the SVG inside roadmap.md
The map is data (scripts/roadmap-map.json); the picture is a generated view of it.
Drawn in the map mode of the site diagram language (scripts/isokit.py): built is a
solid orange line, partial dashed, planned dotted grey. The earlier isometric
version is backed up in docs/brand/diagrams/roadmap-iso-2026-10-03/.
"""
import json
import html
import os

import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from isokit import CSS, box, wire  # noqa: E402

# Map mode (docs/brand/diagram-language.md): a heavy orange rail down the
# middle with the stages on it; optional side trips in lighter boxes either
# side, joined by dotted right-angled wires.
W = 1000
CX = W // 2
SPINE_W, SPINE_H = 260, 58
BR_W, BR_H = 200, 38
STAGE_GAP = 44
BR_GAP = 10
BR_XOFF = 70  # gap between a stage box and its side trips
CIRCLED = dict(zip("⓪①②③④⑤⑥⑦⑧⑨", "0123456789"))
EMOJI = re.compile("[\\U0001F000-\\U0001FFFF\\u2600-\\u27BF\\u2B00-\\u2BFF\\uFE0F\\u2728]")


def clean(label):
    """Drop emoji; the diagram is mono type and orange line, nothing else."""
    return EMOJI.sub("", label).strip()


# --- motion -------------------------------------------------------------------
# CSS animation only: Flowershow's renderer drops SVG's own animation tags
# (and the rest of the page with them). One cycle of CYCLE seconds: the ball
# runs the route and arrives at FINISH, the burst fires at the last stage, then
# a rest before the loop. Hidden for readers who ask for reduced motion.
CYCLE, FINISH = 12, 78  # seconds; percent of the cycle


def animation(tops, wire_paths):
    import math
    L, R = CX - SPINE_W / 2, CX + SPINE_W / 2
    d = f"M{CX} {tops[0] - 18:.1f} V{tops[0]:.1f}"
    for i, top in enumerate(tops):
        bottom = top + SPINE_H
        edge = L if i % 2 == 0 else R
        d += f" H{edge:.1f} V{bottom:.1f} H{CX}"
        if i + 1 < len(tops):
            d += f" V{tops[i + 1]:.1f}"
    css = [
        ".ik .rail { stroke-dasharray: 10 7; animation: ik-flow 1.4s linear infinite; }",
        "@keyframes ik-flow { to { stroke-dashoffset: -34; } }",
        ".ik .ball, .ik .spark { fill: var(--wom-mark, #ff5a00); }",
        f'.ik .ball {{ offset-path: path("{d}"); offset-rotate: 0deg; animation: ik-run {CYCLE}s linear infinite; }}',
        f"@keyframes ik-run {{ 0% {{ offset-distance: 0%; opacity: 0; }} 2% {{ opacity: 1; }} "
        f"{FINISH}% {{ offset-distance: 100%; opacity: 1; }} {FINISH + 2}% {{ offset-distance: 100%; opacity: 0; }} "
        f"100% {{ offset-distance: 100%; opacity: 0; }} }}",
        ".ik .ray { stroke: var(--wom-mark, #ff5a00); stroke-width: 1.6; stroke-linecap: round; "
        f"stroke-dasharray: 22 200; stroke-dashoffset: 22; opacity: 0; animation: ik-burst {CYCLE}s linear infinite; }}",
        f"@keyframes ik-burst {{ 0%, {FINISH}% {{ stroke-dashoffset: 22; opacity: 0; }} {FINISH + 1}% {{ opacity: 1; }} "
        f"{FINISH + 12}% {{ stroke-dashoffset: -100; opacity: 0; }} 100% {{ stroke-dashoffset: -100; opacity: 0; }} }}",
        ".ik .spark { opacity: 0; offset-rotate: 0deg; }",
        f"@keyframes ik-trip {{ 0% {{ offset-distance: 0%; opacity: 0; }} 2% {{ opacity: 1; }} "
        f"18% {{ offset-distance: 100%; opacity: 1; }} 22%, 100% {{ offset-distance: 100%; opacity: 0; }} }}",
        "@media (prefers-reduced-motion: reduce) { .ik .rail { animation: none; } .ik .moving { display: none; } }",
    ]
    els = []
    # burst rays from the last box, as the ball arrives
    cx, cy = CX, tops[-1] + SPINE_H / 2
    for k in range(16):
        a = 2 * math.pi * k / 16 + 0.2
        x0 = cx + math.cos(a) * (SPINE_W / 2 + 6)
        y0 = cy + math.sin(a) * (SPINE_H / 2 + 6)
        reach = 34 + (k % 3) * 14
        x1, y1 = x0 + math.cos(a) * reach, y0 + math.sin(a) * reach
        els.append(f'<line class="ray" pathLength="100" x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}"/>')
    # dots that run out along the side-trip wires, staggered through the cycle
    for i, (x1, y1, x2, y2) in enumerate(wire_paths):
        mx = (x1 + x2) / 2
        css.append(f'.ik .trip{i} {{ offset-path: path("M{x1:.1f} {y1:.1f} H{mx:.1f} V{y2:.1f} H{x2:.1f}"); '
                   f'animation: ik-trip {CYCLE}s linear {-(i * 1.37) % CYCLE:.2f}s infinite; }}')
        els.append(f'<circle class="spark trip{i}" r="2.5"/>')
    els.append('<circle class="ball" r="6"/>')
    return "\n".join(css), f'<g class="moving">{"".join(els)}</g>'


def main():
    here = os.path.dirname(__file__)
    data = json.load(open(os.path.join(here, "roadmap-map.json")))
    wires, boxes, y = [], [], 24
    first_mid = last_mid = None
    tops = []        # y of each stage box top, for the ball's route
    wire_paths = []  # (x1, y1, x2, y2) for the flowing dots
    for stage in data["stages"]:
        branches = stage.get("branches", [])
        left = [b for b in branches if b.get("side") == "left"]
        right = [b for b in branches if b.get("side") != "left"]
        n = max(len(left), len(right))
        cluster_h = n * (BR_H + BR_GAP) - BR_GAP if n else 0
        stage_h = max(SPINE_H, cluster_h)
        sy = y + (stage_h - SPINE_H) / 2
        mid = sy + SPINE_H / 2
        tops.append(sy)
        first_mid = mid if first_mid is None else first_mid
        last_mid = mid
        title = clean(stage["label"])
        num = CIRCLED.get(title[:1])
        title = title[1:].strip() if num else title
        lines = [html.escape(t) for t in title.split("\\n")]
        boxes.append(f'<a href="{stage["url"]}">'
                     f'{box(CX - SPINE_W / 2, sy, SPINE_W, SPINE_H, lines, "stop " + stage["status"], num)}</a>')
        for side, items in (("left", left), ("right", right)):
            by = y + (stage_h - (len(items) * (BR_H + BR_GAP) - BR_GAP)) / 2
            for b in items:
                bx = CX - SPINE_W / 2 - BR_XOFF - BR_W if side == "left" else CX + SPINE_W / 2 + BR_XOFF
                x1 = CX - SPINE_W / 2 if side == "left" else CX + SPINE_W / 2
                x2 = bx + BR_W if side == "left" else bx
                wires.append(wire(x1, mid, x2, by + BR_H / 2))
                wire_paths.append((x1, mid, x2, by + BR_H / 2))
                lab = [html.escape(clean(b["label"]))]
                boxes.append(f'<a href="{b["url"]}">{box(bx, by, BR_W, BR_H, lab, "side-stop " + b["status"], size=13)}</a>')
                by += BR_H + BR_GAP
        y += stage_h + STAGE_GAP
    y -= STAGE_GAP - 24
    rail = f'<line class="rail" x1="{CX}" y1="{first_mid:.1f}" x2="{CX}" y2="{last_mid:.1f}"/>'
    anim_css, motion = animation(tops, wire_paths)
    svg = (f'<svg class="ik ik-map" viewBox="0 0 {W} {y:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" '
           f'aria-label="The Markdown Roadmap: seven stages on a central line, each with optional side trips" '
           f'style="width:100%;height:auto">'
           f'<style>{CSS}{anim_css}</style>{rail}{"".join(wires)}{"".join(boxes)}{motion}</svg>')
    block = f"""<!-- ROADMAP-SVG-START (generated by scripts/roadmap-gen.py from scripts/roadmap-map.json — edit the data, then regenerate; do not edit the SVG by hand) -->
<div class="ik-wide">
{svg}
</div>
<!-- ROADMAP-SVG-END -->"""
    out = os.path.join(here, "..", "roadmap.md")
    page = open(out).read()
    import re as _re
    new = _re.sub(r"<!-- ROADMAP-SVG-START.*?<!-- ROADMAP-SVG-END -->", lambda m: block, page, flags=_re.S)
    assert "ROADMAP-SVG-START" in new, "markers missing in roadmap.md"
    open(out, "w").write(new)
    print(f"updated roadmap.md ({y:.0f}px tall, {sum(len(s.get('branches', [])) + 1 for s in data['stages'])} nodes)")


if __name__ == "__main__":
    main()
