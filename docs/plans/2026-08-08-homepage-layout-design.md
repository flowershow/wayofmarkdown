---
title: "Design: coherent plain-layout homepage"
publish: false
---

# Coherent plain-layout homepage

Approved by Rufus on 2026-08-08.

## Problem

The animated-mark hero was added inside Flowershow's normal article layout. Making that hero wide required a chain of homepage-only overrides in `custom.css`; later elements were then forced back into a `65ch` reading column. The hero, source/rendered demo, captions, card grid and prose consequently follow different alignment rules.

## Design

Rebuild the complete homepage as HTML with Tailwind utility classes and set `layout: plain` in frontmatter. Flowershow continues to supply the site navbar and footer, while the page owns its layout from top to bottom.

Use one centred `max-w-6xl` shell with consistent horizontal padding. The hero is centred: title first, animated syntax mark immediately below it, followed by the tagline, short explanation and calls to action. The source/rendered demonstration uses two equal columns on larger screens and stacks on narrow screens. Long-form prose stays inside a narrower measure; guide and route choices use responsive grids.

Retain all current homepage wording and destinations. This pass fixes structure and responsiveness; further visual embellishment belongs in a separate commit.

Remove the obsolete `.wom-hero` and homepage `:has(...)` rules from `custom.css`. Keep the existing animation iframe and its own reduced-motion behaviour.

## Verification

- A source-level check asserts `layout: plain`, the title/logo order, required sections and removal of the old hero wrapper.
- Run the tai-chi check, voice lint and link check.
- Render locally at desktop and mobile widths, then spot-check the deployed homepage after pushing.

