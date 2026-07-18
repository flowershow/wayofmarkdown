---
title: "The Markdown Database Pattern"
description: "Treat a folder of markdown files as records in a database — the pattern behind Obsidian Bases, Notion-style workflows without lock-in, and more."
created: 2023-05-02
---

# The Markdown Database Pattern

Your filesystem is already a database. Most tools just don't treat it that way.

This is the core insight behind one of the most useful — and underused — patterns in software: treating a collection of markdown files not as documents to be rendered, but as records in a database.

Call it the **Markdown Database Pattern**.

---

## Why naming matters

In software, naming a pattern is not a trivial act. Christopher Alexander, who pioneered the idea of design patterns in architecture, argued that naming a pattern gives you something to think *with* — a concept you can reach for, share, and build on. The Gang of Four did the same for object-oriented design. Martin Fowler for enterprise architecture.

The Markdown Database Pattern deserves a name for the same reason: it is a recurring solution to a recurring problem, it works across many different contexts, and once you see it you start seeing it everywhere.

---

## The problem

The standard approach to content management forces a false choice.

On one side: a CMS. You get structured data — fields, types, queries — but your content is locked in a proprietary database, dependent on an admin interface, tied to a platform. The prose is second-class.

On the other side: plain markdown files. You get freedom — plain text, version control, write in any editor, host anywhere. But you give up queryability. You cannot ask "show me everything tagged *research* written since January." You cannot filter, sort, or aggregate. You have documents, not data.

The Markdown Database Pattern refuses this trade-off.

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

**Consequences**: You get portability (plain files go anywhere), version control (git works perfectly on plain text), stack independence (no framework required), and full queryability over your collection. You give up scale (this pattern is not for millions of records) and complex relational data (this is not a replacement for a relational database). It is a *lightweight* database — powerful within its range, and honest about its limits.

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

You now have a movies database. Query it:

```sql
SELECT * FROM files WHERE year < 1980;
SELECT * FROM files WHERE director = 'George Lucas';
SELECT * FROM file_tags WHERE tag = 'space-opera';
```

The prose is still prose — readable, writable in any editor, stored in git. The structured layer is fully queryable. You did not have to choose.

---

## Where you see this pattern

Once you name it, you start seeing it everywhere.

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

The pattern can be implemented with surprisingly little code. Parse frontmatter, walk a directory tree, write results to SQLite. A weekend project.

Or use a tool built for it. [MarkdownDB](https://github.com/flowershow/markdowndb) indexes a folder of markdown files into SQLite, extracts frontmatter, tags, links, and tasks, and gives you a JavaScript API to query the result. A real queryable database from plain text files in seconds — without giving up the files.

---

## The pattern predates the tools

What matters here is not any particular implementation. It is the pattern itself — the recognition that markdown files have a structured layer waiting to be used, and that treating them as database records is a legitimate, powerful, and underexplored design choice.

Plain text has a long future. Markdown is everywhere. The data was always there.

You just needed a name for it.

---

Around 750 words. The structure follows the classic pattern format (name → problem → solution → consequences → example → context) but reads as an essay rather than a spec. The ending deliberately lands on the idea rather than the tool.

Want to tweak anything — tone, any section, the example?

## Colophon

Originally notes in https://github.com/flowershow/markdowndb/issues/7 and elsewhere
