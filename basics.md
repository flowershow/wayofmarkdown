---
title: Markdown Basics
description: "Learn markdown in ten minutes: headings, bold, links, lists, code, tables, frontmatter. The complete beginner's guide with examples."
---

# Markdown Basics

Markdown is a lightweight markup language with plain text formatting syntax. It is easy to use and deployed all over the web -- GitHub, Reddit, Stack Overflow, [and everywhere else](everywhere.md).

In Markdown you control the display of the document: formatting words as bold or italic, adding images, and creating lists are just a few of the things you can do. Mostly, Markdown is just regular text with a few non-alphabetic characters thrown in, like `##` or `**`.

## Why plain text?

First, plain text is awesome 😎 Plain text never goes out of fashion -- plain text files written thirty years ago are still readable on your modern computer (unlike more complex formats). You can also create and use plain text almost anywhere.

But... plain text has no formatting like bold, italic, or bullet lists etc. Plain text needs conventions for "headings", lists, etc. Wouldn't it be cool if we had a way to add this to plain text *and* this then could be converted to HTML or something that does actually look good? Enter Markdown. 🦸

## Learn by doing

Reading this page takes ten minutes. If you prefer interactive exercises:

- [markdowntutorial.com](https://www.markdowntutorial.com/) -- easy, interactive
- [CommonMark tutorial](https://commonmark.org/help/tutorial/) -- ten minutes of exercises

## The syntax

### Text basics

`usual text` usual text  
`*italic text*` *italic text*  
`**bold text**` **bold text**  
`~~crossed through~~` ~~crossed through~~  
`---` on its own line gives a horizontal rule:

---

To force a line break, end a line with two spaces.

### Headings

```md
# Heading 1
## Heading 2
### Heading 3 (and so on to 6)
```

One `# Heading 1` per page, at the top, is the usual convention.

### Links and images

`https://example.com` -- bare URLs auto-link in most tools  
`[link text](https://example.com)` -- [a proper link](https://example.com)  
`![alt text](image.png)` -- an image (the `!` in front is the difference)

Many markdown tools (Obsidian, Flowershow, wikis) also support `[[wiki-links]]`: double brackets around a page name links to that page. Not part of core markdown, but everywhere in [knowledge-base land](markdown-knowledge-bases.md).

### Lists

```md
- item 1
- item 2
  - item 2a (indent two spaces to nest)

1. first
2. second
```

- item 1
- item 2
  - item 2a

Task lists (GitHub, Obsidian and friends -- [not everywhere](everywhere.md)):

```md
- [ ] not done yet
- [x] done
```

### Quotes

```md
Santa Claus said:

> Happy Christmas, hohoho
```

Santa Claus said:

> Happy Christmas, hohoho

### Code

Inline code goes in single backticks: `` `like this` ``.

Multi-line code goes between triple-backtick lines, and you can name the language for syntax highlighting:

````md
```python
print('hello world')
```
````

Renders as:

```python
print('hello world')
```

### Tables

```md
| Name | Awesome? |
|------|----------|
| Markdown | Yes |
| .docx | No |
```

| Name | Awesome? |
|------|----------|
| Markdown | Yes |
| .docx | No |

## Advanced features

Formatting text with Markdown is as easy as using Notepad, and the syntax extends easily. Some extras worth knowing:

> [!warning]
> These aren't always supported -- check your tool before relying on them.

### Frontmatter

**Frontmatter** is metadata at the top of a file, between two `---` lines:

```md
---
title: 5 minute markdown guide
date: 2026-07-18
author: Rufus
---
```

Tools use it for page titles, dates, and anything else -- it's also how markdown files [act like database records](markdown-database.md).

### Callouts

```md
> [!info]
> My important message here.
```

> [!info]
> My important message here.

Several types exist (info, warning, tip...) -- see the [Flowershow syntax docs](https://flowershow.app/docs/syntax) for the full set.

### HTML

And the escape hatch for everything else: plain HTML is valid markdown. If the syntax can't do it, `<html>` can -- [this matters more than you'd think](markdown-websites.md).

## That's it

Truly, that's the bulk of markdown. You now know enough to write anything on [most of the internet](everywhere.md) -- and to start [building things](markdown-based.md). If you're joining a team that works this way, carry on with the [onboarding path](learn/onboarding.md) 🚀
