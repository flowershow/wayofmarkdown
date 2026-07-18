---
title: "Brief: the visual roadmap (roadmap.sh-style)"
publish: false
---

# Brief: a real visual roadmap

Status: **draft for Rufus review** (2026-07-18). Owner issue: #63. Prototype: `/x-roadmap-experiment` (unlinked experiment page).

## Vision

One picture that shows the whole way of markdown: you *see* the path (boxes and connecting lines, roadmap.sh-style), you see where you are, you see what you can skip, and you click any box to go learn that thing. The same picture honestly shows the state of the site itself — which stations are built, partial, or planned — so it doubles as our public content roadmap. Engaging enough that it (or a slice of it) could sit on the landing page as the site's visual hook.

## What roadmap.sh actually does (anatomy)

- A vertical **spine** of core topics, with **branch clusters** hanging off each spine node left and right, connected by curved edges
- **Boxes are clickable** → resource panel/links
- **Personal progress**: tick done/in-progress/skip; per-user, stored client-side
- Distinct visual coding: recommended vs optional vs "pick one of these"
- It's a bespoke React+SVG app with an editor behind it

## Our version — goals and non-goals

**v1 goals**

1. Genuinely visual: boxes, edges, spatial layout — a map, not a styled list
2. Every node clickable → its page on this site
3. **Status colour-coding**: built ✅ / partial 🚧 / planned 🗺️ — learner guidance and public build-status in one (people skip what they know; nobody clicks into a stub unwarned)
4. Maintainable by future agents: the map is **data**, the picture is **generated** — no hand-tweaking pixels
5. Works within Flowershow constraints (no custom JS assumed), dark-mode friendly, usable on mobile (zoom/scroll is acceptable)

**Non-goals for v1**: per-user progress ticking (needs JS/localStorage — v2 candidate, worth checking Flowershow's script options); hover panels; an editor.

## Recommended approach: data → generator → inline SVG

A YAML file defines the map (nodes: id, label, url, status, lane; edges). A small python script (`scripts/roadmap-gen.py`) lays out and emits SVG with real `<a>` links and status colours, embedded in the page. Why this beats the alternatives:

- **vs hand-drawn SVG/excalidraw**: regenerable when content changes; status colours update by editing one YAML line
- **vs mermaid**: mermaid is quick but looks like a dev diagram, styling is limited, and link handling is inconsistent across renderers
- **vs HTML/CSS positioned boxes**: SVG handles edges/curves and scales as one drawing; CSS flowcharts fight responsiveness
- **vs React app**: not available inside Flowershow content, and overkill before the map is proven

It's also pleasingly on-message: the roadmap itself is plain-text data in the repo, and the picture is a view of it. (Cf. the coggle: hand-drawn maps rot; generated ones track the content.)

## Design language (v1)

- Spine: large rounded boxes, top→down, bold edges; branches: smaller boxes clustered beside their stage, thinner curved edges
- Status: filled green-ish border = built, amber dashed = partial/outline, grey dotted = planned; legend on the page
- Colours as CSS classes (not hardcoded fills) so light/dark themes both work
- Node text stays short; the click-through page does the talking

## Open questions for Rufus

1. Where does it live once good — replace `/roadmap`'s list (list moves below the picture?), and does a mini version go on the landing page?
2. How much of the site to map in v1: the spine + build-X branches (~25 nodes), or also Everywhere/side-quests (~40)?
3. Appetite for v2 interactivity (progress ticking) — worth investigating Flowershow custom-JS options?

## Related (spun out separately)

Visual "why markdown is awesome" page and the pluggability entry → content map / #59. Timeline page → own issue. Great-references collection → own issue.
