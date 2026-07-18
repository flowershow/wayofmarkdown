---
title: "How to use Markdown in Notion — import, export and shortcuts"
description: "Notion supports markdown three ways: live shortcuts as you type, pasting markdown in, and importing/exporting .md files. What round-trips cleanly and what doesn't."
---

# How to use Markdown in Notion

Notion is a blocks app, not a markdown app. But markdown is how you get things in and out of it, and honestly it's how a lot of us would prefer to leave. Here's how the two worlds connect.

## Three ways markdown works in Notion

**1. Type it.** Markdown shortcuts convert live as you write: `# ` becomes a heading, `- ` a bullet, `[]` a to-do, `` ` `` code, `**bold**` bold. Muscle memory from any markdown editor mostly carries over.

**2. Paste it.** Paste a chunk of markdown and Notion converts it to blocks -- headings, lists, tables, code blocks all come through. This is great combined with [AI chats](markdown-in-chatgpt.md): draft anywhere, paste into Notion for the team.

**3. Import / export files.** `Import → Markdown` brings in `.md` files as pages. And any page can go the other way: `••• → Export → Markdown & CSV` -- or export your *entire workspace* at once from Settings.

## What survives the round trip (and what doesn't)

Export is where you meet the difference between blocks and files:

- **Clean**: headings, lists, to-dos, quotes, code, simple tables, links.
- **Lossy**: databases become CSV files (plus per-row markdown pages); toggles flatten out; columns and layout vanish; synced blocks unsync; comments don't come; internal links may point at exported filenames.

It's decent (much better than most tools manage) but it's an *exit*, not a sync. Notion's format is Notion; markdown is the doorway.

## The escape hatch reading of all this

What markdown export really gives you is an exit. Your notes can leave. And once you know they can leave, the next question is whether they needed to live in a proprietary blocks database in the first place: most of what most people do in Notion (notes, docs, wikis, even light databases) works in plain markdown files with the right tools on top.

We wrote up that whole pattern: [The Markdown Database Pattern](markdown-database.md), and the practical guide to [markdown-based Notion alternatives](markdown-based.md): files you own, tools you choose, no export button needed because there's nothing to export *from*.

More apps: [markdown everywhere](everywhere.md) 🌍
