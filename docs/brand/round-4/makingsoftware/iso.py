"""Exploded isometric view of a markdown file, in the Making Software manner.
Writes iso.svg. Colours are classes; the page CSS maps them to the accent."""
import math, pathlib
C, S = math.cos(math.radians(30)), math.sin(math.radians(30))
OX, OY = 370, 30           # screen origin of plate corner (0,0) at z=0
W, D, GAP, T = 220, 140, 118, 5

def P(x, y, z):
    return (OX + (x - y) * C, OY + (x + y) * S + z)

def pts(*ps): return " ".join(f"{a:.1f},{b:.1f}" for a, b in ps)

def plate(z, cls="pl", thick=T):
    a, b, c, d = P(0,0,z), P(W,0,z), P(W,D,z), P(0,D,z)
    a2, b2, c2, d2 = [(p[0], p[1]+thick) for p in (a,b,c,d)]
    return (f'<polygon class="side" points="{pts(d,c,c2,d2)}"/>'
            f'<polygon class="side" points="{pts(c,b,b2,c2)}"/>'
            f'<polygon class="{cls}" points="{pts(a,b,c,d)}"/>')

def line(x0, x1, y, z, cls="ln"):
    (p, q) = P(x0, y, z), P(x1, y, z)
    return f'<line class="{cls}" x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}"/>'

def rect(x0, y0, x1, y1, z, cls="tint"):
    return f'<polygon class="{cls}" points="{pts(P(x0,y0,z),P(x1,y0,z),P(x1,y1,z),P(x0,y1,z))}"/>'

def text_on(x, y, z, s, size=9):
    # text laid along the plate's x axis
    px, py = P(x, y, z)
    return (f'<text class="on" font-size="{size}" transform="translate({px:.1f},{py:.1f}) '
            f'matrix({C:.3f},{S:.3f},{-C:.3f},{S:.3f},0,0)">{s}</text>')

def label(side, x, y, z, s, lx):
    # leader from a point on the layer to a caption at screen x = lx
    px, py = P(x, y, z)
    anchor = "end" if side == "L" else "start"
    tx = lx - 8 if side == "L" else lx + 8
    return (f'<line class="lead" x1="{lx}" y1="{py:.1f}" x2="{px:.1f}" y2="{py:.1f}"/>'
            f'<path class="arr" d="M{px:.1f} {py:.1f} l{-5 if side=="R" else 5} -3 v6 z"/>'
            f'<text class="lab" x="{tx}" y="{py+3.5:.1f}" text-anchor="{anchor}">{s}</text>')

layers = []  # bottom first
zs = [4*GAP, 3*GAP, 2*GAP, GAP, 0]   # screen z grows downward; top layer z=0
out = []
# dashed guides through the four corners
for (x, y) in [(0,0),(W,0),(W,D),(0,D)]:
    a, b = P(x,y,zs[-1]+T), P(x,y,zs[0])
    out.append(f'<line class="guide" x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>')

# 5 base: the file itself
z = zs[0]
g = [plate(z, "base", 9)]
g.append(text_on(18, 28, z, "notes.md", 13))
g.append(text_on(18, 48, z, "plain text · utf-8 · 1.2 kb", 8))
g.append(label("R", W, 60, z, "PLAIN TEXT FILE", 620))
layers.append(g)
# 4 frontmatter
z = zs[1]
g = [plate(z)]
g.append(text_on(18, 26, z, "---")); g.append(text_on(18, 44, z, "title: Weekly notes"))
g.append(text_on(18, 62, z, "tags: [plans, home]")); g.append(text_on(18, 80, z, "---"))
g.append(label("L", 0, 50, z, "FRONTMATTER", 150))
layers.append(g)
# 3 text and marks
z = zs[2]
g = [plate(z)]
g.append(text_on(18, 28, z, "# Weekly notes", 11))
for i, (a, b) in enumerate([(18,190),(18,150),(30,170),(30,120)]):
    g.append(line(a, b, 52 + i*18, z))
g.append(text_on(18, 124, z, "- [x] call the bank"))
g.append(label("R", W, 40, z, "HEADINGS, LISTS, EMPHASIS", 620))
layers.append(g)
# 2 links
z = zs[3]
g = [plate(z)]
nodes = [(60,50),(150,40),(110,100),(185,110)]
for (a,b) in [(0,1),(0,2),(2,3),(1,3)]:
    p, q = P(*nodes[a], z), P(*nodes[b], z)
    g.append(f'<line class="ln" x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}"/>')
for n in nodes:
    p = P(*n, z); g.append(f'<ellipse class="node" cx="{p[0]:.1f}" cy="{p[1]:.1f}" rx="7" ry="4"/>')
g.append(text_on(42, 74, z, "[[plan]]"))
g.append(label("L", 0, 100, z, "LINKS [[ ]]", 150))
layers.append(g)
# 1 top: rendered view, what any tool shows
z = zs[4]
g = [plate(z, "top")]
g.append(rect(16, 16, 120, 34, z, "tint"))
for i, (a, b) in enumerate([(16,200),(16,170),(16,190),(16,140),(16,180)]):
    g.append(line(a, b, 56 + i*16, z, "ln soft"))
g.append(label("R", W, 30, z, "RENDERED, BY ANY TOOL", 620))
layers.append(g)

body = "".join(out) + "".join("<g>" + "".join(l) + "</g>" for l in layers)
svg = (f'<svg class="iso" viewBox="0 0 800 700" role="img" aria-label="Exploded view of a markdown file: '
       f'a plain text file, its frontmatter, its headings and lists, its links, and the rendered page any tool can show.">'
       f'{body}</svg>')
(pathlib.Path(__file__).parent / "iso.svg").write_text(svg)
print("iso.svg", len(svg))
