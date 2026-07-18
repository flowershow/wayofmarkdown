---
title: "Markdown-based Digital Gardens"
description: "What a digital garden is — notes published while still growing — and how to grow one from your markdown notes with Obsidian and Flowershow."
---

# Markdown-based Digital Gardens

A digital garden is a public notebook: notes published while they're still growing, linked into a web you wander rather than a feed you scroll. Where a blog says "here is my finished post, timestamped", a garden says "here is my thinking so far, come back later and it'll be better".

The metaphor has a small intellectual tradition behind it (Mike Caulfield's "The Garden and the Stream" is the founding essay; Maggie Appleton keeps [a lovely history](https://maggieappleton.com/garden-history)), but the practice is simple: tend notes over time, in public, with links.

## Why gardens suit markdown perfectly

A garden is just a [knowledge base](markdown-knowledge-bases.md) with a public face, and every property gardens need is a property markdown files already have:

- **Notes, not posts**: small pages that grow by edits, which is exactly what a versioned file does.
- **Links over chronology**: `[[wiki-links]]` and backlinks make the garden wanderable; no dates required.
- **Imperfection on purpose**: gardens embrace half-finished thought. A frontmatter field like `status: seedling` (a garden convention: seedling → budding → evergreen) tells readers how baked a note is.
- **Longevity**: a garden is a decades-long project. Plain text is the only format you should trust with one.

## Growing one

1. **Tend notes in Obsidian** as usual: one idea per note, links everywhere.
2. **Mark what's public.** Simplest: a `garden/` folder (or publish the whole vault and keep private stuff elsewhere). Flowershow also respects `publish: false` frontmatter for per-note control.
3. **Publish with [Flowershow](https://flowershow.app)**: it renders wiki-links and backlinks properly, which matters more for gardens than for any other kind of site, since backlinks *are* the paths between beds. [Straight from Obsidian](https://www.youtube.com/watch?v=2jOYg0wCg1s) if you like.
4. **Add an entrance**: a short index page pointing at your best evergreens and your currently-growing patches.

The [tutorial series](learn/index.md) covers the mechanics; by the end of tutorial 2 you have a published garden, whether you call it that or not.

## Gardening habits that work

- Link first, organise later. The graph becomes the structure.
- When you learn something, improve the existing note instead of writing "part 2".
- Date nothing except in frontmatter. Freshness lives in the content, not the URL.
- Every so often, walk your own garden as a visitor and fix the paths that dead-end.

The quiet payoff: your half-formed notes attract better conversations than your polished posts, because readers can see where to push. Gardens are the most social form of [owning your content](why.md).
