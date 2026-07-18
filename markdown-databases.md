---
title: "Markdown-based Databases & Catalogs"
description: "Files as records, frontmatter as fields, folders as tables: build small databases and catalogs from markdown — book lists, contacts, projects, anything."
---

# Markdown-based Databases & Catalogs

> [!note]
> Short version -- the full essay on this pattern already exists: [The Markdown Database Pattern](markdown-database.md) 🌟

A catalog of books. Team contacts. A project tracker. Recipes. You'd reach for Notion or Airtable -- but a markdown file with frontmatter *is* a record:

```md
---
name: Hermione Granger
house: Gryffindor
---
Brightest witch of her age. Friend of [[Harry]].
```

A folder of these is a table. Tools query and view it: Obsidian Bases (and Dataview before it) give you sortable tables and boards over your files; publish them with Flowershow and the web gets them too.

**Start here**: [make a simple catalog of anything in Obsidian](learn/howtos/create-a-simple-catalog-of-anything.md) -- hands-on, 20 minutes. Then read [the pattern in depth](markdown-database.md) for when it's the right tool (and when a real database is).
