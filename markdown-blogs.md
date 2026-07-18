---
title: "Markdown-based Blogs"
description: "A blog is a folder of dated markdown posts plus a publisher. How to set one up in minutes, and why it outlasts every platform."
---

# Markdown-based Blogs

A blog is the most naturally markdown-shaped thing there is: a folder of posts, one file each, a date in each file, newest first. Every blogging platform ever built is essentially this plus an editor plus lock-in. Some of them charge you monthly for the privilege.

## The pattern

```
blog/
  2026-07-18-why-i-left-substack.md
  2026-06-02-markdown-databases.md
```

Each post is a markdown file with a little frontmatter:

```md
---
title: Why I left Substack
date: 2026-07-18
---
It started, as these things do, with an email about "monetisation features"...
```

A publisher renders the folder as a blog listing and each file as a post. Feeds, dates, archives: the tool's job, from your files.

## Setting one up

With Flowershow it takes about thirty seconds, and I mean that literally:

<iframe width="560" height="315" src="https://www.youtube.com/embed/0NGvcuXTris" title="Blog listing with Flowershow in 30 seconds" frameborder="0" allowfullscreen></iframe>

The recipe: make a `blog/` folder in your site repo, add posts with `title` and `date` frontmatter, and the listing page appears. If you don't have a site repo yet, [tutorial 1](learn/tutorials/create-a-website-from-scratch.md) gets you one in ten minutes. Prefer another tool? Hugo, Jekyll, Astro and Eleventy all eat the same folder of dated markdown, which is rather the point.

Write the posts wherever you like. [Obsidian](markdown-in-obsidian.md) is lovely for drafting; so is drafting [in an AI chat](markdown-in-chatgpt.md) and pasting the markdown straight in.

## Why this beats the platforms

**Your archive is yours.** The internet is littered with dead blogging platforms and the posts that died with them (pour one out for Posterous, and Geocities before it). A folder of markdown moves with you. When Substack eventually annoys you, your escape is `git clone`.

**No platform tax.** No one inserts a subscribe popup between you and your readers, takes a cut, or decides your niche violates something.

**It compounds with everything else here.** Your blog can live in the same repo as your [knowledge base](markdown-knowledge-bases.md) and [website](markdown-websites.md). Posts can wiki-link to notes. AI tools can [work directly on your drafts](kb/ai-editing.md).

The honest trade-off: platforms bring built-in discovery (Substack's network, Medium's feed) and you'll have to do your own distribution. For most people who stick with blogging, that trade looks better every year they own their archive.
