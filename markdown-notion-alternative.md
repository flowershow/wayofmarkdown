---
title: "Replace Notion with Markdown — the escape guide"
description: "Most of what you do in Notion — docs, wikis, light databases — works as markdown files with the right tools. How to escape, and what you trade."
---

# Replacing Notion with Markdown

> [!note]
> Short version for now -- full guide coming (this one deserves it).

Notion is genuinely good software. It's also a proprietary blocks database that owns your notes, your wiki and your little databases, rented back to you monthly. Most of what most people use it for works in plain markdown:

- **Docs & notes** → markdown files, obviously. [Obsidian](markdown-knowledge-bases.md) gives you the nice editor.
- **Wikis** → files + `[[wiki-links]]` ([guide](markdown-wikis.md)).
- **Databases** → the interesting one. Files with frontmatter fields *are* records; tools give you table/board/gallery views over them. Obsidian **Bases** does exactly this natively now -- and you can even [publish Bases to the web](https://www.youtube.com/watch?v=0_qr_qQVkxk). Full pattern: [The Markdown Database Pattern](markdown-database.md).
- **Sharing/publishing** → Flowershow or any static publisher.

**What you give up, honestly**: real-time multiplayer editing, granular permissions, heavy relational databases. If those are your core, stay. If what you have is notes, docs and lists -- you can own them.

**Getting out**: Notion [exports to markdown](markdown-in-notion.md) (with quirks -- covered there). Export, tidy, open in Obsidian, breathe.
