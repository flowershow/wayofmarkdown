---
title: "The Markdown Database Pattern"
description: "Treat a folder of markdown files as records in a database — the pattern behind Obsidian Bases, Notion-style workflows without lock-in, and more."
created: 2023-05-02
---

# The Markdown Database Pattern

*[Rufus Pollock](/about) · begun 2023, maintained since — [history](https://github.com/flowershow/wayofmarkdown/commits/main/markdown-database.md)*

Your filesystem is already a database.

This is the insight behind one of the most useful (and underused) patterns: treating a collection of markdown files as records in a database. Leveraging Markdown's support for "frontmatter" we can add rich metadata to free text and get a notion-like database experience with content that you control and access on your own hard disk.

We call it the **Markdown Database Pattern**.

---

## The problem

The standard approach to content management creates a painful choice.

**On one side: a CMS, or Notion or other proprietary system**. You get structured data — fields, types, queries — but your content is locked in a proprietary database, dependent on an admin interface, tied to a platform. And prose is second-class.

**On the other side: plain markdown files**. You get freedom — plain text, version control, write in any editor, host anywhere. But you give up queryability. You cannot ask "show me everything tagged *research* written since January." You cannot filter, sort, or aggregate. You have documents, not data.

The Markdown Database Pattern solves this trade-off and gives you **the best of both worlds: markdown files with metadata mean you own the content but you get rich structured metadata along with free text.**

---

## The pattern

**Name**: Markdown Database Pattern

**Problem**: You want content that is both human-readable rich text *and* structured queryable data — without locking yourself into a platform or sacrificing the simplicity of plain files.

**Solution**: Treat a collection of markdown files as a database. Each file is a record. Frontmatter fields are columns. Directories are natural groupings — tables, if you want them to be. Tags, links, and tasks embedded in the document body become additional queryable relations.

**The mapping:**

```
Filesystem              Database
──────────────────────────────────
markdown file      →    record
frontmatter field  →    column
directory          →    table
#tag               →    tag relation
[[wikilink]]       →    link relation
- [ ] task         →    task relation
```

**Consequences**: You get portability (plain files go anywhere), version control (git works perfectly on plain text), stack independence (no framework required), and full queryability over your collection. You give up scale (this pattern is not for millions of records) and complex relational data (this is not a replacement for a relational database). It is a *lightweight* database — powerful within its range, and honest about its limits. <!-- voice-lint-ok: original phrasing -->

---

## An example

A folder of movie notes:

```
movies/
  return-of-the-jedi.md
  a-new-hope.md
  the-empire-strikes-back.md
```

Each file:

```md
---
year: 1983
director: Richard Marquand
budget_m: 32.7
tags: [sci-fi, space-opera]
---

# Return of the Jedi

A long time ago in a galaxy far, far away...
```

That folder is a database. You just need a tool to read the structured layer. Point [MarkdownDB](https://github.com/flowershow/markdowndb) at it and you get `files` and `file_tags` tables to query:

```sql
SELECT * FROM files WHERE year < 1980;
SELECT * FROM files WHERE director = 'George Lucas';
SELECT * FROM file_tags WHERE tag = 'space-opera';
```

This isn't a live demo — nothing on this page runs the query. The point is that the query is *possible*: index the folder once and the structured layer is there. The prose is still prose — readable, writable in any editor, stored in git.

## Seeing it without code

SQL is one way in. The friendlier one: open the same folder in Obsidian and point a [Base](https://help.obsidian.md/bases) at it. The frontmatter shows up as a sortable, filterable table, no query language required.

![[table2.png]]

Here it's a handful of character files, rendered as a table. The [practical guide](markdown-databases-guide.md) covers the tools; the [step-by-step tutorial](learn/howtos/create-a-simple-catalog-of-anything.md) builds one from an empty folder in about 20 minutes.

---

## Where you see this pattern

Once described you can start seeing it everywhere.

A personal notes folder with frontmatter is a Markdown Database. A team wiki where every page has a `status` and `owner` field is a Markdown Database. A blog where posts carry `date`, `tags`, and `author` metadata is a Markdown Database — it just might not know it yet.

The pattern fits naturally wherever individual records have both a prose side and a data side:

- Blogs and articles
- Personal knowledge bases and digital gardens
- Team wikis and internal documentation
- Research notes and reading lists
- Recipe collections, travel logs, project retrospectives

The sweet spot is collections up to roughly ten thousand files. Beyond that, reach for a real database. Below that, this pattern gives you almost everything a database does at a fraction of the complexity — and none of the lock-in.

---

## Implementing it

The pattern can be implemented with surprisingly little code. Parse frontmatter, walk a directory tree, write results to JSON or SQLite or whatever.

Or use a tool built for it. [MarkdownDB](https://github.com/flowershow/markdowndb) indexes a folder of markdown files into SQLite, extracts frontmatter, tags, links, and tasks, and gives you a JavaScript API to query the result. A real queryable database from plain text files in seconds — without giving up the files.

---

## The pattern predates the tools

What matters here is not any particular implementation. It is the pattern itself — the recognition that markdown files have a structured layer waiting to be used, and that treating them as database records is a legitimate, powerful, and underexplored design choice.

Plain text has a long future. Markdown is everywhere. And frontmatter add the data.

---

**Build one:** [Markdown-based databases & catalogs](markdown-databases-guide.md) — the practical guide to the tools and conventions, with a step-by-step tutorial at the end.

## Colophon

Originally notes in the markdowndb project and elsewhere e.g. https://github.com/flowershow/markdowndb/issues/7
