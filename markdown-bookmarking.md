---
title: "Markdown-based Bookmarking & Web Clipping"
description: "Save the web as markdown you own: clip pages to clean text with Obsidian Web Clipper or into.md, annotate them, and search them forever."
---

# Markdown-based Bookmarking & Web Clipping

Bookmarks rot. Links die (the average webpage lives a couple of years), read-later apps shut down or paywall your own highlights, and browser bookmark bars are where URLs go to be forgotten. The markdown-based fix changes what you save: **keep the content, not the pointer**. Clip pages as clean markdown into your own files, where they're searchable, annotatable and permanent.

## The tools

**[Obsidian Web Clipper](https://obsidian.md/clipper)**: the official browser extension. One click sends the current page to your vault as tidy markdown, with configurable templates for what metadata comes along. The daily driver.

**[into.md](kb/into-md.md)**: converts any URL to clean markdown; handy when you're not at your own machine or want to pipe pages programmatically.

**[Turndown](kb/turndown.md)**: the JavaScript HTML-to-markdown library, for when you're building your own clipping pipeline.

**Watch it done:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/d-Vte5vJCl0" title="Markdown for bookmarking and webclipping" frameborder="0" allowfullscreen></iframe>

## From clippings to knowledge

A clip with no thought attached is a hoarded page. The move that makes this system pay is small: **add one line of your own to every clip**, even just `saved because X claims the opposite of [[that other article]]`. Now it's a note in your [knowledge base](markdown-knowledge-bases.md), linked into your thinking, not a pile.

Frontmatter turns the pile into [a database](markdown-database.md):

```md
---
url: https://example.com/essay
saved: 2026-07-18
tags: [ai, formats]
status: to-read
---
```

An Obsidian Base over `clips/` gives you a read-later queue with views and filters: your own Instapaper, minus the company.

## A workflow that holds up

1. **Clip** anything worth keeping (generously; storage is free).
2. **One line of why**, at clip time, while you remember.
3. **Weekly**: skim `status: to-read`, read or delete, link the keepers into real notes.
4. Highlights and quotes go in as blockquotes with your commentary underneath, which is how a clipping graduates into thinking.

Your future self, searching a decade of clipped pages that no longer exist anywhere else on the web, will be quietly grateful.
