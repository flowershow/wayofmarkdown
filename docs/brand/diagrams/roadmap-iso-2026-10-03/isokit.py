"""The site's diagram language, as code (see docs/brand/diagram-language.md).

Taken from the front-page figure (docs/brand/round-4/makingsoftware/iso.py):
flat isometric plates in one orange line, a faint orange side, mono labels on
horizontal leader lines ending in a small arrow. Diagrams are inline SVG that
style themselves through the classes in CSS below, so they follow the site's
light and dark themes.
"""
import math

C, S = math.cos(math.radians(30)), math.sin(math.radians(30))

# Colours come from the site's tokens where they exist, with fallbacks so a
# diagram still looks right outside the site.
CSS = """
.ik { color: var(--color-foreground, #1b1b1d); font-family: 'IBM Plex Mono', ui-monospace, Menlo, monospace; }
.ik .side { fill: color-mix(in srgb, var(--wom-mark, #ff5a00) 26%, var(--color-background, #fbfbf9)); stroke: var(--wom-mark, #ff5a00); stroke-width: 1; }
.ik .top { fill: var(--color-background, #fbfbf9); stroke: var(--wom-mark, #ff5a00); stroke-width: 1.3; }
.ik .partial .top, .ik .partial .side { stroke-dasharray: 6 4; }
.ik .planned .top, .ik .planned .side { stroke: var(--site-muted, #8a8a90); stroke-dasharray: 2 4; }
.ik .planned .side { fill: var(--color-background, #fbfbf9); }
.ik .spine { stroke: var(--wom-mark, #ff5a00); stroke-width: 1; stroke-dasharray: 5 5; opacity: .7; }
.ik .lead { stroke: var(--wom-mark, #ff5a00); stroke-width: 1; }
.ik .arr { fill: var(--wom-mark, #ff5a00); }
.ik .num { fill: var(--wom-mark, #ff5a00); font-family: 'Newsreader', Georgia, serif; }
.ik .on { fill: currentColor; font-weight: 600; }
.ik .lab { fill: currentColor; font-size: 13px; }
.ik .planned .lab { fill: var(--site-muted, #8a8a90); }
.ik a:hover .top { fill: color-mix(in srgb, var(--wom-mark, #ff5a00) 10%, var(--color-background, #fbfbf9)); }
.ik a:hover .lab { fill: var(--color-accent, #cc4400); text-decoration: underline; }
"""


class Iso:
    """Isometric projection with its origin (plate corner 0,0 at z=0) at ox, oy.
    Screen y grows downward, so z is a downward screen offset."""

    def __init__(self, ox, oy):
        self.ox, self.oy = ox, oy

    def P(self, x, y, z=0):
        return (self.ox + (x - y) * C, self.oy + (x + y) * S + z)


def pts(*ps):
    return " ".join(f"{a:.1f},{b:.1f}" for a, b in ps)


def plate(iso, w, d, z, thick=6):
    """A plate w by d at depth z: two side faces, then the top face."""
    a, b, c, e = iso.P(0, 0, z), iso.P(w, 0, z), iso.P(w, d, z), iso.P(0, d, z)
    a2, b2, c2, e2 = [(p[0], p[1] + thick) for p in (a, b, c, e)]
    return (f'<polygon class="side" points="{pts(e, c, c2, e2)}"/>'
            f'<polygon class="side" points="{pts(c, b, b2, c2)}"/>'
            f'<polygon class="top" points="{pts(a, b, c, e)}"/>')


def text_on(iso, x, y, z, s, size=13, cls="on"):
    """Text lying flat on a plate, running along its x axis."""
    px, py = iso.P(x, y, z)
    return (f'<text class="{cls}" font-size="{size}" transform="translate({px:.1f},{py:.1f}) '
            f'matrix({C:.3f},{S:.3f},{-C:.3f},{S:.3f},0,0)">{s}</text>')


def leader(px, py, lx, s, side):
    """A horizontal leader from point (px, py) to a label at screen x = lx."""
    anchor, tx = ("end", lx - 8) if side == "L" else ("start", lx + 8)
    tip = 5 if side == "L" else -5
    return (f'<line class="lead" x1="{lx}" y1="{py:.1f}" x2="{px:.1f}" y2="{py:.1f}"/>'
            f'<path class="arr" d="M{px:.1f} {py:.1f} l{tip} -3 v6 z"/>'
            f'<text class="lab" x="{tx}" y="{py + 4:.1f}" text-anchor="{anchor}">{s}</text>')
