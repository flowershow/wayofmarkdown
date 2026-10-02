#!/usr/bin/env python3
"""Hand-drawn style sketches for option 3. Ink lines with a wobble filter, pastel fills, Patrick Hand lettering."""
INK="#161616"; SKY="#bfe0f5"; GRASS="#cfe8c6"; SAND="#f1dfae"; RED="#e4572e"; BLUE="#ff5a00"; WHITE="#fffdf5"
HAND='font-family="Patrick Hand,Comic Sans MS,cursive"'
DEFS='''<defs><filter id="wob" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="1.6" xChannelSelector="R" yChannelSelector="G"/></filter></defs>'''
def svg(vb,body,label):
    return f'<svg viewBox="{vb}" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" {HAND} aria-label="{label}">{DEFS}<g filter="url(#wob)">{body}</g></svg>'
def fig(x,y,s=1.0,face=1,arm="down",shirt=None):
    """stick figure, head top at (x,y). s scale."""
    h=10*s
    o=[f'<circle cx="{x}" cy="{y+h}" r="{h}" fill="{WHITE}"/>']
    o.append(f'<path d="M{x} {y+2*h} v{30*s}"/>')
    o.append(f'<path d="M{x} {y+2*h+30*s} l{-9*s} {22*s} M{x} {y+2*h+30*s} l{9*s} {22*s}"/>')
    if arm=="up": o.append(f'<path d="M{x} {y+2*h+8*s} l{-10*s} {12*s} M{x} {y+2*h+8*s} l{14*face*s} {-14*s}"/>')
    elif arm=="hold": o.append(f'<path d="M{x} {y+2*h+8*s} l{14*face*s} {6*s} M{x} {y+2*h+8*s} l{14*face*s} {14*s}"/>')
    else: o.append(f'<path d="M{x} {y+2*h+8*s} l{-10*s} {16*s} M{x} {y+2*h+8*s} l{10*s} {16*s}"/>')
    # face
    o.append(f'<circle cx="{x-3*s*face}" cy="{y+h-1}" r="0.9" fill="{INK}" stroke="none"/><path d="M{x+1*face} {y+h+4} q{3*face} 2 {5*face} 0" stroke-width="1.2"/>')
    return "".join(o)
def page(x,y,w,h,label="",lines=3):
    o=[f'<path d="M{x} {y} h{w-8} l8 8 v{h-8} h{-w} z" fill="{WHITE}"/><path d="M{x+w-8} {y} v8 h8"/>']
    for i in range(lines): o.append(f'<path d="M{x+6} {y+14+i*7} h{w-14-(i%2)*8}" stroke-width="1.4"/>')
    if label: o.append(f'<text x="{x+w/2}" y="{y+h+12}" font-size="10" text-anchor="middle" fill="{INK}" stroke="none">{label}</text>')
    return "".join(o)
def arrow(x1,y1,x2,y2):
    import math
    a=math.atan2(y2-y1,x2-x1); l=7
    return f'<path d="M{x1} {y1} Q{(x1+x2)/2+6} {(y1+y2)/2-6} {x2} {y2}"/><path d="M{x2} {y2} l{-l*math.cos(a-0.5):.1f} {-l*math.sin(a-0.5):.1f} M{x2} {y2} l{-l*math.cos(a+0.5):.1f} {-l*math.sin(a+0.5):.1f}"/>'
def label(x,y,t,size=11,anchor="middle",color=INK):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" stroke="none">{t}</text>'

out={}
# HERO: one file, any tool, still yours
b=[]
b.append(fig(110,60,1.1,1,"hold"))
b.append(page(132,84,36,44,"notes.md",4))
# targets
b.append(f'<rect x="290" y="30" width="70" height="46" rx="4" fill="{SKY}"/><path d="M290 44h70"/><circle cx="297" cy="37" r="1.6" fill="{INK}" stroke="none"/><circle cx="303" cy="37" r="1.6" fill="{INK}" stroke="none"/>'+label(325,65,"WEBSITE",10))
b.append(f'<rect x="300" y="100" width="64" height="40" rx="3" fill="{WHITE}"/><path d="M292 140h80" stroke-width="2.2"/><path d="M312 110h40M312 118h30M312 126h36" stroke-width="1.3"/>'+label(332,158,"OBSIDIAN",10))
b.append(f'<rect x="318" y="168" width="24" height="42" rx="4" fill="{WHITE}"/><circle cx="330" cy="202" r="1.8" fill="{INK}" stroke="none"/><path d="M322 176h16M322 182h12" stroke-width="1.2"/>'+label(330,226,"PHONE",10))
# robot / AI
b.append(f'<rect x="450" y="60" width="44" height="40" rx="6" fill="{SAND}"/><circle cx="465" cy="76" r="3" fill="{INK}" stroke="none"/><circle cx="479" cy="76" r="3" fill="{INK}" stroke="none"/><path d="M462 90h20M472 60v-10M466 50h12"/>'+label(472,118,"AI CHAT",10))
# git box
b.append(f'<path d="M440 150h50v36h-50z M440 150l10-10h50l-10 10 M490 150l10-10v36l-10 10" fill="{WHITE}"/>'+label(466,206,"GIT (HISTORY)",10))
# arrows from file
b.append(arrow(170,100,288,60)); b.append(arrow(172,108,298,118)); b.append(arrow(168,118,316,185)); b.append(arrow(360,52,448,70)); b.append(arrow(366,120,438,160))
# second person reading website
b.append(fig(540,120,0.9,-1,"up"))
b.append(label(547,208,"!",14,"middle",RED))
# caption in sketch
b.append(label(300,250,"ONE FILE. ANY TOOL. STILL YOURS.",15))
out["HERO"]=svg("0 0 600 262","".join(b),"Sketch: a person holds a file called notes.md; arrows lead from it to a website, Obsidian, a phone, an AI chat and a git history box; a second person reads the website.")

# FORCES: two people pushing a wheel
b=[]
b.append(f'<circle cx="200" cy="120" r="70" fill="{SKY}" stroke-width="2.2"/><circle cx="200" cy="120" r="8" fill="{WHITE}"/>')
for a in (0,60,120): b.append(f'<path d="M200 120 l{70*__import__("math").cos(__import__("math").radians(a)):.1f} {70*__import__("math").sin(__import__("math").radians(a)):.1f} M200 120 l{-70*__import__("math").cos(__import__("math").radians(a)):.1f} {-70*__import__("math").sin(__import__("math").radians(a)):.1f}" stroke-width="1.2"/>')
b.append(fig(96,80,1.0,1,"up")); b.append(label(96,185,"PEOPLE",11)); b.append(label(96,199,"(easy to write)",9))
b.append(fig(304,80,1.0,-1,"up")); b.append(label(304,185,"TOOLS",11)); b.append(label(304,199,"(easy to read)",9))
b.append(f'<path d="M150 40 q50 -30 100 0" /><path d="M250 40 l-8 -6 M250 40 l-9 4"/>'+label(200,24,"MORE WRITERS",10))
b.append(f'<path d="M250 200 q-50 30 -100 0" /><path d="M150 200 l8 6 M150 200 l9 -4"/>'+label(200,232,"MORE TOOLS",10))
b.append(f'<rect x="362" y="118" width="34" height="30" rx="5" fill="{SAND}"/><circle cx="373" cy="130" r="2.4" fill="{INK}" stroke="none"/><circle cx="385" cy="130" r="2.4" fill="{INK}" stroke="none"/><path d="M370 140h14M379 118v-7"/>'+label(379,166,"AI, LATE",10)+label(379,178,"TO THE PARTY",9))
b.append(f'<path d="M358 130 l-18 -4" stroke-dasharray="3 3"/>')
b.append(label(200,262,"HOW A FORMAT ATE THE WORLD",14))
out["FORCES"]=svg("0 0 420 272","".join(b),"Sketch: two people, labelled people and tools, push a wheel round between them; more writers lead to more tools and back; a small robot labelled AI joins late.")

# ICONS for six cards
out["ICON_NOTION"]=svg("0 0 120 90",page(20,14,50,60,"",3)+f'<rect x="60" y="30" width="46" height="46" rx="3" fill="{SKY}"/><path d="M60 45h46M60 60h46M75 30v46M90 30v46" stroke-width="1.2"/>'+label(60,86,"docs + a little database",9),"Sketch: a page and a small table")
out["ICON_NOTES"]=svg("0 0 120 90",page(14,16,34,44,"",3)+page(44,24,34,44,"",3)+page(74,12,34,44,"",3)+f'<path d="M48 40 q-8 -14 -4 -22 M78 44 q6 -20 -4 -24" stroke-dasharray="2 3"/>'+label(60,86,"linked, in a folder",9),"Sketch: three linked pages")
out["ICON_SITE"]=svg("0 0 120 90",f'<rect x="20" y="14" width="80" height="56" rx="4" fill="{SKY}"/><path d="M20 28h80"/><circle cx="28" cy="21" r="2" fill="{INK}" stroke="none"/><circle cx="36" cy="21" r="2" fill="{INK}" stroke="none"/><path d="M32 42h40M32 52h28" stroke-width="1.3"/>'+label(60,86,"yourname.org",9),"Sketch: a browser window")
out["ICON_BLOG"]=svg("0 0 120 90",page(30,12,56,60,"",4)+f'<path d="M78 70 l22 -40 l8 4 l-22 40 z" fill="{SAND}"/><path d="M78 70 l-2 8 l8 -4"/>'+label(60,86,"write, publish, keep",9),"Sketch: a page and a pencil")
out["ICON_TEAM"]=svg("0 0 120 90",fig(40,10,0.6,1,"down")+fig(80,10,0.6,-1,"down")+page(50,46,20,24,"",2)+label(60,86,"shared, reviewed",9),"Sketch: two people and a shared page")
out["ICON_CAT"]=svg("0 0 120 90",f'<path d="M16 24h88M16 50h88M16 74h88" stroke-width="2"/>'+"".join(f'<rect x="{x}" y="{y}" width="12" height="22" rx="1" fill="{c}"/>' for x,y,c in [(24,28,SKY),(40,28,SAND),(56,28,GRASS),(74,28,SKY),(24,52,GRASS),(40,52,SKY),(60,52,SAND),(78,52,GRASS)])+label(60,86,"one file per thing",9),"Sketch: shelves of files")

# TABLE sketch for notion page
b=[]
for i,(n,h,c) in enumerate([("malfoy.md","Slytherin","-"),("potter.md","Gryffindor","Hedwig"),("granger.md","Gryffindor","Crookshanks")]):
    y=20+i*62; b.append(page(20,y,96,50,"",0)); b.append(label(30,y+16,n,10,"start",BLUE)); b.append(label(30,y+30,f"house: {h}",9,"start")); b.append(label(30,y+42,f"pet: {c}",9,"start"))
    b.append(arrow(120,y+25,152,110))
b.append(f'<rect x="160" y="60" width="300" height="104" rx="3" fill="{WHITE}"/><path d="M160 86h300M160 112h300M160 138h300M240 60v104M340 60v104" stroke-width="1.2"/>')
b.append(f'<rect x="160" y="60" width="300" height="26" fill="{SAND}" stroke="none" opacity=".7"/>')
for x,t in [(200,"FILE"),(290,"HOUSE"),(400,"PET")]: b.append(label(x,78,t,11))
for i,(n,h,c) in enumerate([("malfoy","Slytherin","-"),("potter","Gryffindor","Hedwig (owl)"),("granger","Gryffindor","Crookshanks")]):
    y=104+i*26; b.append(label(200,y,n,10,"middle",BLUE)); b.append(label(290,y,h,10)); b.append(label(400,y,c,10))
b.append(label(310,196,"THREE FILES = ONE TABLE",14))
b.append(label(310,212,"(Obsidian Bases draws it. Dataview did for years.)",9))
out["TABLE"]=svg("0 0 480 222","".join(b),"Sketch: three markdown files with frontmatter become one table with columns file, house and pet.")

# SCALE sketch: what you give up
b=[]
b.append(f'<path d="M200 190 h-40 M180 190 v-110" stroke-width="2.4"/><path d="M80 90 L280 70" stroke-width="2.4"/><circle cx="180" cy="80" r="4" fill="{INK}"/>')
b.append(f'<path d="M80 90 l-30 50 h60 z" fill="{SAND}"/><path d="M280 70 l-30 50 h60 z" fill="{SKY}"/>')
b.append(label(80,156,"YOU GIVE UP",11)); b.append(label(80,170,"live multiplayer",9)); b.append(label(80,182,"page permissions",9)); b.append(label(80,194,"huge databases",9))
b.append(label(280,136,"YOU GET",11)); b.append(label(280,150,"your files, forever",9)); b.append(label(280,162,"any tool, any time",9)); b.append(label(280,174,"no rent, no export button",9))
b.append(fig(368,140,0.7,-1,"up"))
b.append(label(180,214,"HONESTLY, IT TIPS. BUT NOT FOR EVERYONE.",13))
out["SCALE"]=svg("0 0 400 226","".join(b),"Sketch: a balance scale. The light side lists what you give up: live multiplayer, page permissions, huge databases. The heavy side lists what you get: your files forever, any tool any time, no rent.")

import pathlib
pathlib.Path("sketches.html").write_text("\n".join(f"<!--{k}-->\n{v}\n<!--/{k}-->" for k,v in out.items()))
print("sketches:",", ".join(out))
