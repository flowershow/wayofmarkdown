---
title: "Newcomer website review — July 2026"
publish: false
---

# Newcomer website review (2026-07-29)

External review, conducted from the perspective of a first-time visitor with no prior
markdown experience. Source: `life-itself/asdra-personal`. Recorded here because it drove
the nav and homepage changes of 2026-07-29.

Complements [[site-critique-2026-07]], which graded the *presentation* layer (visual
identity, proof, engagement loops) and waved IA through at 4.5. This one is entirely about
IA and naming — the axis a cold reader can see and we can't.

## The review, as received

**Homepage — too many choices, too fast.** A 7-item menu and an ungrouped sidebar arrive
before the visitor has a reason to pick a path.

**Demo.** The raw/rendered pane is a good asset but static; the real playground is buried
behind a small link on a separate page, and the example isn't the "Notion style" thing the
site promises. Suggestion: embed the live playground on the homepage, add a richer example.

**Roadmap.** Its "pick your path" is the best thing on the site and sits on a page most
first-time visitors never open. Suggestion: bring a simplified version to the homepage.

**Learn.** Sounds like a general hub; teaches one thing (building a website). Suggestion:
rename to "Website Tutorial", or add tracks for knowledge bases and leaving Notion.

**Guides.** Genuinely useful. The "pattern behind all of them" section is the clearest
statement of the site's philosophy anywhere.

**Everywhere.** Proves the pillar better than the homepage does, but the nav label doesn't
hint that a detailed comparison table is behind it. Suggestion: relabel.

**Knowledge Base.** Redundant against Everywhere; the page is really tools, workflows,
essays, Git/GitHub and reference — a help section, not an example of building a knowledge
base. Suggestion: rename to "Reference" or "Help", drop the duplicated apps section.

**Why.** Good page. Strong opener, clear argument, ends on the MOGF stack.

**Manifesto.** Redundant against Why. Suggestion: merge into Why as a toggle or alternate
version.

## Assessment

Right, and verified against the files:

- **"Learn" is mislabelled.** `learn/index.md` is titled "Learn: Build a Markdown-based
  Website" — one MOGF arc. The nav promised a hub.
- **"Knowledge Base" was the sharpest catch.** We ship `markdown-knowledge-bases.md` about
  *building* one and a nav tab meaning *our help section*. Same words, two meanings, one
  navbar — and the two pages competed for the same search term.
- **"Everywhere" hides its best asset** — a real three-tier compatibility table.
- **The roadmap's path-picker was stranded.**

Pushed back on:

- **Merging Manifesto into Why.** Different registers: Why is the reasoned case, the
  Manifesto is the shareable advocacy artifact the launch kit is built around. Rufus's
  call, 2026-07-29: keep both the page and its nav tab.
- **The kb/Everywhere "duplication"** was already a one-line signpost, not a duplicate
  section. Tightened rather than removed.
- **Sidebar grouping** is not ours to fix directly. Flowershow builds the sidebar from the
  file tree and our top level is deliberately flat for SEO slugs, so the ungrouped sidebar
  is a direct cost of the slug convention. Already a v0.2 carryover needing a Flowershow
  feature; an outside reviewer hitting it independently raises its priority.

What the review implied but didn't say — and the reason the fix was consolidation rather
than addition:

- **The homepage had three separate path-pickers**: the 6-tile "Why markdown wins" grid,
  the 8-tile "What will you build?" grid, and the 4-branch "Start where you are" list, plus
  a 7-item nav, a flat sidebar and two competing hero CTAs (one of them *Read the
  manifesto*, an odd ask of someone who arrived eight seconds ago). The problem was never
  missing guidance. It was unranked guidance, and adding the roadmap picker as a fourth
  grid would have made it worse. That the reviewer didn't register the guidance already
  there *is* the finding.
- **`basics.md` wasn't in the nav** — plausibly the highest-value page for exactly this
  persona, reachable only via a tile or the footer.
- **Every rename proposed was zero-risk**: nav labels in `config.json`, not filenames. No
  URL changes, no redirects, no SEO cost.

## What was done (2026-07-29)

- Nav labels: Learn → **Tutorials**, Everywhere → **Markdown in apps**, Knowledge Base →
  **Reference**. Manifesto tab kept. URLs unchanged throughout.
- `kb/index.md` retitled to "Markdown Reference: tools, workflows and help", ending the
  keyword collision with the knowledge-base guide; apps section folded into one signpost
  line pointing at both the guide and Everywhere.
- Footer: "Knowledge base" now points at the guide; "Reference" added for `/kb`.
- Homepage: hero secondary CTA swapped from the manifesto to Markdown basics; the "Why
  markdown wins" tile grid became a paragraph (same six links, one fewer picker); "Start
  where you are" became "Start here", carrying the roadmap's two entrances.

## Not done, deliberately

- **Live playground on the homepage** (review's strongest ask). Deferred: three recent
  commits were spent taming hero height, and a large embed fights that directly. Revisit
  with the Notion-style example as its own piece of work.
- **Extra Learn tracks** for knowledge bases and Notion-leavers. Real content work, not a
  rename — belongs in the v0.2 growth-content stream.
- **Sidebar grouping.** Blocked on Flowershow. Worth checking whether `showSidebar` can be
  set per-page, so the homepage at least stops showing a flat 40-item list to first-time
  visitors.
