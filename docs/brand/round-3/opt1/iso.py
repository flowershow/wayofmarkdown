#!/usr/bin/env python3
"""Generate the isometric hero panel (flat fills, ink outlines, one or two colours) as hero-iso.svg.
Wikimedia-style: little scene of a file travelling from a desk to a screen to a published page, with two people."""
import math
INK="#1a1a1a"; BLUE="#2449d8"; T1="#dbe3fb"; T2="#eef1fb"; ORANGE="#ec7a3c"; T3="#fbe3d4"; WHITE="#fff"; FLOOR="#f3f5fc"
OX,OY=300,95; S=1.22   # origin in SVG space
def P(x,y,z=0):
    """isometric projection: x to the right-down, y to the left-down, z up"""
    return (OX+S*(x-y)*math.cos(math.radians(30)), OY+S*(x+y)*math.sin(math.radians(30))-S*z)
def poly(pts,fill,stroke=INK,sw=1.3):
    d=" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)
    return f'<polygon points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def box(x,y,z,w,d,h,top,left,right):
    """cuboid at (x,y,z) size w (along x), d (along y), h (up). faces: top, left(front-left, along x), right(front-right, along y)"""
    out=[]
    out.append(poly([P(x,y+d,z),P(x+w,y+d,z),P(x+w,y+d,z+h),P(x,y+d,z+h)],left))     # face facing viewer-left (y=d side)
    out.append(poly([P(x+w,y+d,z),P(x+w,y,z),P(x+w,y,z+h),P(x+w,y+d,z+h)],right))     # face facing viewer-right (x=w side)
    out.append(poly([P(x,y,z+h),P(x+w,y,z+h),P(x+w,y+d,z+h),P(x,y+d,z+h)],top))
    return "\n".join(out)
def person(x,y,z,shirt,facing=1):
    """simple figure standing at (x,y,z): legs, body, head. drawn in screen space around P(x,y,z)"""
    cx,cy=P(x,y,z); s=1.0
    g=[]
    g.append(f'<rect x="{cx-7*s:.1f}" y="{cy-22*s:.1f}" width="{6*s:.1f}" height="{20*s:.1f}" rx="2" fill="{BLUE}" stroke="{INK}" stroke-width="1.2"/>')
    g.append(f'<rect x="{cx+1*s:.1f}" y="{cy-22*s:.1f}" width="{6*s:.1f}" height="{20*s:.1f}" rx="2" fill="{BLUE}" stroke="{INK}" stroke-width="1.2"/>')
    g.append(f'<rect x="{cx-10*s:.1f}" y="{cy-46*s:.1f}" width="{20*s:.1f}" height="{26*s:.1f}" rx="5" fill="{shirt}" stroke="{INK}" stroke-width="1.2"/>')
    g.append(f'<circle cx="{cx:.1f}" cy="{cy-55*s:.1f}" r="{8.5*s:.1f}" fill="{WHITE}" stroke="{INK}" stroke-width="1.2"/>')
    g.append(f'<path d="M{cx-8.5*s:.1f} {cy-57*s:.1f} q{8.5*s:.1f} -9 {17*s:.1f} 0" fill="{INK}" stroke="{INK}" stroke-width="1.2"/>')  # hair
    # arm reaching
    g.append(f'<path d="M{cx+9*s:.1f} {cy-40*s:.1f} l{12*facing*s:.1f} -6" stroke="{INK}" stroke-width="3.2" stroke-linecap="round" fill="none"/>')
    g.append(f'<path d="M{cx+9*s:.1f} {cy-40*s:.1f} l{12*facing*s:.1f} -6" stroke="{shirt}" stroke-width="1.6" stroke-linecap="round" fill="none"/>')
    return "\n".join(g)
def sheet(x,y,z,w,d,lines=3):
    """a flat page lying on a surface with text lines"""
    out=[poly([P(x,y,z),P(x+w,y,z),P(x+w,y+d,z),P(x,y+d,z)],WHITE,INK,1.1)]
    for i in range(lines):
        a=P(x+4,y+4+i*7,z); b=P(x+w-6-(i%2)*8,y+4+i*7,z)
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{BLUE}" stroke-width="1.6" stroke-linecap="round"/>')
    return "\n".join(out)
svg=[]
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 380" font-family="JetBrains Mono,monospace" aria-label="Isometric scene: a person writes a markdown file at a desk; the same file appears on a screen, in a shared folder, and on a published web page; a second person reads it.">')
# floor
svg.append(poly([P(-10,-10),P(300,-10),P(300,230),P(-10,230)],FLOOR,"#c9d2f0",1))
# floor grid dots
for gx in range(0,300,20):
    for gy in range(0,230,20):
        a=P(gx,gy); svg.append(f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="0.9" fill="#c9d2f0"/>')
# path on floor from desk to screen to web (dashed)
pts=[P(80,150,0.5),P(128,150,0.5),P(128,112,0.5),P(215,112,0.5),P(215,45,0.5)]
d="M"+" L".join(f"{a:.1f} {b:.1f}" for a,b in pts)
svg.append(f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="1.4" stroke-dasharray="4 4"/>')
# desk (back left) with sheet and laptop
svg.append(box(20,120,0,60,50,22,T1,T2,T1))
svg.append(sheet(26,132,22,26,30,4))
svg.append(box(54,128,22,22,30,2,WHITE,T1,T1))                       # laptop base
svg.append(poly([P(54,128,24),P(76,128,24),P(76,128,44),P(54,128,44)],BLUE,INK,1.2)) # laptop screen (vertical along x)
svg.append(poly([P(57,128,27),P(73,128,27),P(73,128,41),P(57,128,41)],WHITE,"none",0))
# writer person, in front of desk
svg.append(person(45,185,0,ORANGE,1))
# screen monitor (middle)
svg.append(box(120,60,0,8,50,2,T1,T2,T1))
svg.append(poly([P(124,60,2),P(124,110,2),P(124,110,46),P(124,60,46)],WHITE,INK,1.3))   # monitor face along y
svg.append(poly([P(124,66,8),P(124,104,8),P(124,104,40),P(124,66,40)],T2,"none",0))
for i in range(4):
    a=P(124,70,34-i*7); b=P(124,70+(26 if i%2==0 else 18),34-i*7)
    svg.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{BLUE}" stroke-width="1.8" stroke-linecap="round"/>')
# file label floating above path midpoint
m=P(128,150,46)
svg.append(f'<path d="M{m[0]-16:.1f} {m[1]-22:.1f} h22 l8 8 v26 h-30 z" fill="{WHITE}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>')
svg.append(f'<path d="M{m[0]+6:.1f} {m[1]-22:.1f} v8 h8" fill="none" stroke="{INK}" stroke-width="1.2"/>')
svg.append(f'<text x="{m[0]-1:.1f}" y="{m[1]+1:.1f}" font-size="7" fill="{BLUE}" font-weight="700" text-anchor="middle">notes</text><text x="{m[0]-1:.1f}" y="{m[1]+9:.1f}" font-size="7" fill="{BLUE}" font-weight="700" text-anchor="middle">.md</text>')
# folder / repo box (back right)
svg.append(box(195,10,0,40,30,26,T1,BLUE,T1))
svg.append(f'<text x="{P(215,25,27)[0]:.1f}" y="{P(215,25,27)[1]+3:.1f}" font-size="7.5" fill="{INK}" text-anchor="middle" font-weight="700">GIT</text>')
# published page billboard (front right) with flag
svg.append(box(226,168,0,10,4,70,T1,T1,T1))  # post
svg.append(poly([P(206,170,40),P(266,170,40),P(266,170,92),P(206,170,92)],WHITE,INK,1.3))  # sign face along x
svg.append(poly([P(210,170,84),P(262,170,84),P(262,170,76),P(210,170,76)],BLUE,"none",0))
for i in range(3):
    a=P(210,170,70-i*8); b=P(210+(44 if i%2==0 else 30),170,70-i*8)
    svg.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{T1}" stroke-width="3" stroke-linecap="round"/>')
svg.append(f'<text x="{P(236,170,80)[0]:.1f}" y="{P(236,170,80)[1]+2:.1f}" font-size="6.5" fill="{WHITE}" text-anchor="middle" font-weight="700">YOURSITE.ORG</text>')
# flag on top
t=P(236,170,92); svg.append(f'<path d="M{t[0]:.1f} {t[1]:.1f} v-18 l16 5 l-16 5" fill="{ORANGE}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>')
# reader person, front right
svg.append(person(275,135,0,BLUE,-1))
# corner marks
svg.append(f'<g stroke="{BLUE}" stroke-width="1.4" fill="none"><path d="M14 14h8M14 14v8"/><path d="M586 14h-8M586 14v8"/><path d="M14 366h8M14 366v-8"/><path d="M586 366h-8M586 366v-8"/></g>')
svg.append('</svg>')
open('hero-iso.svg','w').write("\n".join(svg)); print('svg ok')
