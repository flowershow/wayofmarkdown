---
title: "Markdown-based Databases & Catalogs"
description: "Build small databases and catalogs from markdown files: frontmatter as fields, folders as tables, Obsidian Bases for views, markdowndb for queries. The practical guide."
---

# Markdown-based Databases & Catalogs

A catalog of books. Team contacts. A project tracker. Recipes, film notes, a reading list. The reflex is to reach for Notion or Airtable, and hand another platform another slice of your life. The markdown-based alternative starts from one observation: a file with frontmatter *is* a record.

```md
---
name: Hermione Granger
house: Gryffindor
patronus: otter
---
Brightest witch of her age. Friend of [[Harry]].
```

A folder of these is a table. Fields, records, even relations (that wiki-link is a foreign key if you squint). What's missing is the query layer, and that's what the tools provide.

This idea has a name and a full essay behind it: [The Markdown Database Pattern](markdown-database.md) 🌟 This page is the practical version.

## The tools

**Obsidian Bases** is the headline: native database views (tables, cards, filters, sorting) over the frontmatter in your plain files. Point a Base at your folder and your book notes become a sortable library. Before Bases, the Dataview plugin did the same with a query language, and it's still there for power users.

**Publishing**: a catalog is more fun shared. Flowershow publishes [Bases to the web](https://www.youtube.com/watch?v=0_qr_qQVkxk), views and all, so your film log or team directory becomes a live page.

**For builders**: [markdowndb](https://github.com/flowershow/markdowndb) indexes a markdown folder into SQLite (frontmatter, tags, links, tasks) and gives you a JavaScript API. A real queryable database from plain files, in seconds, and you keep the files.

## Build one now

The hands-on walkthrough is [create a simple catalog of anything](learn/howtos/create-a-simple-catalog-of-anything.md): 20 minutes in Obsidian, from empty folder to a linked, structured character catalog with images. Do that once and you'll see catalog-shaped things everywhere.

A few conventions that pay off as it grows:

- **Consistent field names** across a folder (decide `status` vs `state` once)
- **One folder per "table"**: `books/`, `people/`, `projects/`
- **An index page** with a Base or list view as the folder's front door
- **Dates in frontmatter** (`created`, `finished`) so you can sort by them later

## The honest limits

The pattern shines up to a few thousand records and gets silly at a few hundred thousand. Complex relational needs (joins, rollups, aggregation across tables) belong in an actual database. And multi-user simultaneous editing is git-style asynchronous, with everything that implies.

But be honest about your actual case first. Most "databases" in most people's Notion are a few dozen rows with three fields. For that, plain files win on every axis that matters in five years: portability, durability, [AI-readability](markdown-in-chatgpt.md), and the freedom to change tools without a migration.

Related: [replacing Notion](markdown-notion-alternative.md) · [knowledge bases](markdown-knowledge-bases.md) · [the pattern essay](markdown-database.md)
