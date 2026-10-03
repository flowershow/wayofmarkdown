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
# SVG's own animation (no JavaScript). One cycle of CYCLE seconds: the ball
# runs the route and finishes at FINISH of the cycle, the burst fires at the
# last stage, then everything rests until the loop starts again. Hidden for
# readers who ask for reduced motion.
CYCLE, FINISH = 12, 0.78
ANIM_CSS = """
.ik .rail { stroke-dasharray: 10 7; animation: ik-flow 1.4s linear infinite; }
@keyframes ik-flow { to { stroke-dashoffset: -34; } }
.ik .ball { fill: var(--wom-mark, #ff5a00); }
.ik .spark { fill: var(--wom-mark, #ff5a00); }
.ik .ray { stroke: var(--wom-mark, #ff5a00); stroke-width: 1.5; stroke-linecap: round; }
@media (prefers-reduced-motion: reduce) {
  .ik .rail { animation: none; }
  .ik .moving { display: none; }
}
"""


def animation(tops, wire_paths):
    import math
    L, R = CX - SPINE_W / 2, CX + SPINE_W / 2
    # route: down the spine, round one edge of each box (alternating sides), on down
    d = f"M{CX} {tops[0] - 18:.1f} V{tops[0]:.1f}"
    for i, top in enumerate(tops):
        bottom = top + SPINE_H
        edge = L if i % 2 == 0 else R
        d += f" H{edge:.1f} V{bottom:.1f} H{CX}"
        if i + 1 < len(tops):
            d += f" V{tops[i + 1]:.1f}"
    end_x, end_y = CX, tops[-1] + SPINE_H
    t = f"0;{FINISH};1"
    ball = (f'<circle class="ball" r="6"><animateMotion dur="{CYCLE}s" repeatCount="indefinite" '
            f'path="{d}" keyPoints="0;1;1" keyTimes="{t}" calcMode="linear"/>'
            f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite" '
            f'values="0;1;1;0;0" keyTimes="0;0.02;{FINISH};{FINISH + 0.02};1"/></circle>')
    # burst: tracer rays fire out from the last box as the ball arrives
    cx, cy = CX, tops[-1] + SPINE_H / 2
    rays = []
    for k in range(16):
        a = 2 * math.pi * k / 16 + 0.2
        r0x, r0y = SPINE_W / 2 + 6, SPINE_H / 2 + 6
        x0, y0 = cx + math.cos(a) * r0x, cy + math.sin(a) * r0y
        reach = 26 + (k % 3) * 12
        x1, y1 = x0 + math.cos(a) * reach, y0 + math.sin(a) * reach
        f0, f1, f2 = FINISH, FINISH + 0.06, FINISH + 0.13
        kt = f"0;{f0};{f1};{f2};1"
        rays.append(
            f'<line class="ray" x1="{x0:.1f}" y1="{y0:.1f}" x2="{x0:.1f}" y2="{y0:.1f}" opacity="0">'
            f'<animate attributeName="x2" dur="{CYCLE}s" repeatCount="indefinite" values="{x0:.1f};{x0:.1f};{x1:.1f};{x1:.1f};{x0:.1f}" keyTimes="{kt}"/>'
            f'<animate attributeName="y2" dur="{CYCLE}s" repeatCount="indefinite" values="{y0:.1f};{y0:.1f};{y1:.1f};{y1:.1f};{y0:.1f}" keyTimes="{kt}"/>'
            f'<animate attributeName="x1" dur="{CYCLE}s" repeatCount="indefinite" values="{x0:.1f};{x0:.1f};{x0:.1f};{x1:.1f};{x0:.1f}" keyTimes="{kt}"/>'
            f'<animate attributeName="y1" dur="{CYCLE}s" repeatCount="indefinite" values="{y0:.1f};{y0:.1f};{y0:.1f};{y1:.1f};{y0:.1f}" keyTimes="{kt}"/>'
            f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite" values="0;0;1;0;0" keyTimes="{kt}"/>'
            f'</line>')
        rays.append(
            f'<circle class="spark" r="2.2" cx="{x0:.1f}" cy="{y0:.1f}" opacity="0">'
            f'<animate attributeName="cx" dur="{CYCLE}s" repeatCount="indefinite" values="{x0:.1f};{x0:.1f};{x1:.1f};{x1 + math.cos(a) * 10:.1f};{x0:.1f}" keyTimes="{kt}"/>'
            f'<animate attributeName="cy" dur="{CYCLE}s" repeatCount="indefinite" values="{y0:.1f};{y0:.1f};{y1:.1f};{y1 + math.sin(a) * 10 + 6:.1f};{y0:.1f}" keyTimes="{kt}"/>'
            f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite" values="0;0;1;0;0" keyTimes="{kt}"/>'
            f'</circle>')
    # dots that run out along the side-trip wires, staggered so a few move at once
    dots = []
    for i, (x1, y1, x2, y2) in enumerate(wire_paths):
        mx = (x1 + x2) / 2
        path = f"M{x1:.1f} {y1:.1f} H{mx:.1f} V{y2:.1f} H{x2:.1f}"
        run, dur = 2.6, CYCLE  # each dot runs for 2.6s, then waits out the cycle
        begin = (i * 1.37) % CYCLE
        f = run / dur
        dots.append(f'<circle class="spark" r="2.5" opacity="0">'
                    f'<animateMotion dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite" path="{path}" '
                    f'keyPoints="0;1;1" keyTimes="0;{f:.3f};1" calcMode="linear"/>'
                    f'<animate attributeName="opacity" dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite" '
                    f'values="0;1;1;0;0" keyTimes="0;{f * 0.1:.3f};{f * 0.8:.3f};{f:.3f};1"/>'
                    f'</circle>')
    return f'<g class="moving">{"".join(dots)}{ball}{"".join(rays)}</g>'


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
    motion = animation(tops, wire_paths)
    svg = (f'<svg class="ik ik-map" viewBox="0 0 {W} {y:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" '
           f'aria-label="The Markdown Roadmap: seven stages on a central line, each with optional side trips" '
           f'style="width:100%;height:auto">'
           f'<style>{CSS}{ANIM_CSS}</style>{rail}{"".join(wires)}{"".join(boxes)}{motion}</svg>')
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
