---
title: "Markdown-based Websites — the complete guide"
description: "How to build and publish a real website from plain markdown files: tools, publishing options, and the underrated superpower that markdown supports HTML."
---

# Markdown-based Websites

This is the flagship use case, and the one where the markdown-based approach most clearly beats the alternatives. A website built from markdown files is one you fully own, can edit anywhere, version with git, and move between tools -- and these days it's genuinely *easier* than wrestling a CMS.

> [!info]
> This is a guide-of-guides -- several parts, work through what you need.

## Part 1: What is a markdown-based website?

A folder of markdown files + a tool that turns them into web pages. That's the whole architecture. `index.md` becomes your home page, `about.md` becomes `/about`, folders become sections. Compare that to WordPress (a database, a server, plugins, updates...) or Squarespace (a subscription and a format you can never leave). Here, the "database" is files you can read in any editor, and the website is a *view* of them.

**Fastest possible start**: our [tutorial series](learn/index.md) takes you from zero to a published site -- create a GitHub repo, connect a publisher, done in minutes, no code, nothing to install.

## Part 2: The superpower nobody tells you about -- markdown supports HTML 🦸

This is the part that changes what you think markdown websites can be.

Markdown isn't a walled garden that ends where the syntax ends: **HTML is valid markdown**. Drop a `<div>`, an `<iframe>`, a styled block right into your `.md` file and it renders. Which means:

- Need a fancy landing-page hero, a two-column layout, an embedded video or map? Just write (or paste, or ask an AI for) the HTML, inline, in an otherwise plain markdown page.
- With a publisher that allows CSS frameworks (Flowershow supports Tailwind, for instance) you can style right in the markup.
- Your site can be 95% simple prose and 5% rich HTML exactly where it earns its keep -- you never hit a wall that forces you to "graduate" to a code project.

And here's the 2026 twist: **you don't even need to know HTML**, because AI writes it fluently and [AI speaks markdown](markdown-in-chatgpt.md). Describe what you want, paste the result into your markdown file:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qquv0Qq7luE" title="Edit a complex HTML site without knowing any code using Codex AI" frameborder="0" allowfullscreen></iframe>

(That video? Embedded with a plain HTML `<iframe>` in this markdown page. See? 😎)

## Part 3: Tools -- editing, hosting, publishing

The stack has three replaceable slots:

- **Edit**: any text editor. [Obsidian](markdown-knowledge-bases.md) if you want a lovely writing environment; VS Code if you're technical; the GitHub web editor if you want zero install.
- **Store & collaborate**: a git repository, usually GitHub -- free hosting of your files with full history, plus branches and reviews when a team shows up ([our tutorial](learn/tutorial-3.md)).
- **Publish**: the part that turns files into a site. [Flowershow](https://flowershow.app) is ours and is built for exactly this (point it at a repo or publish [straight from Obsidian](https://www.youtube.com/watch?v=2jOYg0wCg1s)); the wider ecosystem includes Hugo, Jekyll, Astro, Eleventy, MkDocs and more. The content doesn't care which you pick -- that's the point.

## Part 4: Where to go deep

- [Tutorial 1: create a website from scratch](learn/tutorials/create-a-website-from-scratch.md) -- the full hand-held walkthrough
- [Tutorial 2: edit locally with Obsidian + GitHub Desktop](learn/tutorials/edit-a-website-locally.md)
- Publish from the command line: <a href="https://www.youtube.com/watch?v=DdiFMDtZwPQ">Flowershow CLI in 2 minutes</a>
- Sibling guides: [blogs](markdown-blogs.md) · [docs sites](markdown-docs.md) · [digital gardens](markdown-digital-gardens.md)

## Why bother (the one-paragraph case)

Because in five years your Squarespace site will be a subscription you resent, your WordPress site will be a maintenance chore, and your markdown site will be... a folder of text files, still working, published by whatever the best tool is in five years. [Own the source](manifesto.md).
