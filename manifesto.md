---
title: "The Markdown Manifesto"
description: "Markdown is eating the world. Choose markdown and you choose freedom, power and simplicity — and the most awesome ecosystem of tooling in the world."
created: 2026-01-26
authors: ["Rufus Pollock"]
---

# The Markdown Manifesto

*[Rufus Pollock](/about) · first drafted January 2026, evolving since — [history](https://github.com/flowershow/wayofmarkdown/commits/main/manifesto.md)*

> X ❤️ markdown

Use Markdown *everywhere*.

Markdown is *eating the world*.

So simple everyone can use it, so simple every tool can implement it.

---

We believe markdown is *awesome*.

We believe the markdown ecosystem can take over the world. It can become *the* standard format for sharing text-based information -- and even for creating mini-databases and catalogs. Move over Notion, markdown is here!

Choose markdown and you choose freedom, power and simplicity -- and the most awesome ecosystem of tooling in the world.

Choosing markdown means *you* owning your content, rather than someone else's tool or platform owning you.

AI ❤️ markdown

Version control ❤️ markdown

Docs ❤️ markdown

Yes, markdown started out as the geek underdog that just showed up in text areas on the internet. But it's like the punk teenager become slick yuppie adult. Markdown is sexy now. Markdown is slick. WYSIWYG markdown is everywhere (think Obsidian, think tiptap, think Substack).

## What is markdown?

Wait, i hear you ask. What actually *is* markdown, and why is it so awesome?

Markdown is plain text plus a few conventions for formatting: `# heading`, `**bold**`, `[link](url)`. That's more or less it -- [ten minutes and you know it](basics.md).

And that minimalism is exactly why it's awesome:

- It's the minimal extension beyond plain text -- so it keeps everything great about plain text (readable anywhere, durable forever, works with *every* tool that handles text: git, grep, AI, etc etc)
- Human usable *and* machine usable (especially for AI!)
- Open and implementable by anyone -- which is why it's implemented everywhere
- And the markdown-specific tooling is now very, very strong

## Markdown with superpowers (aka markdown is extensible)

We aren't just talking about basic, CommonMark-standardized markdown here. Because the awesome thing is that markdown is so simply extensible.

First off, you *can* just put HTML in markdown. Need some fancy layout? No problem -- roll up your HTML and you're done. ([This matters more than people realise](markdown-websites.md).)

But that's not all. Markdown has those triple-backtick sections, and someone came up with the neat idea of labelling them -- which means you can embed entire other tools inside your markdown, as long as they're plain text too. Label a block `mermaid` and you've got diagrams. Label it `python` and you've got highlighted code.

And then there's just other stuff, from task lists with `- [ ]` (made famous by GitHub) to tables:

```md
| I am | a table |
|------|---------|
| How cool | is that! |
```

## Markdown-based X: the rise of the markdown ecosystem

> It's not about the format, it's about the tools. And the tools need a common language. <!-- voice-lint-ok: Rufus's original line -->

What you care about is *doing* something, not the format. You want to take notes, publish a site, run your team's docs. So really it's about markdown-based X: the markdown-based notetaking app, the markdown-based documentation tool, markdown-based messaging in a chat app.

But the underlying format matters because we need to connect between tools and between people. It may not matter *which* language you speak -- it matters enormously that you're all speaking the same one. All these tools want to interconnect; all these users want to learn only one format. So just as english took over the world, markdown is taking over the world.

That's why this site has a guide for each markdown-based X -- [websites, blogs, knowledge bases, databases, and the rest](markdown-based.md) -- and a map of [everywhere markdown already lives](everywhere.md), from Google Docs to WhatsApp to (almost) Apple Notes.

## AI ❤️ markdown (and why that's revolutionary)

- Token economics: markdown is the minimal viable syntax beyond plain text, and tokens matter
- Every AI reads and writes it natively -- it's what they were trained on
- Tool interoperability: you copy and paste into and out of AI chat *all the time*, and markdown is the format that survives the trip

More on this: [markdown in ChatGPT, Claude and friends](markdown-in-chatgpt.md).

## What "freedom" means here

- **Tool freedom**: use the tool you want. Combine tools. Swap tools.
- **Content freedom**: own your content -- and therefore be free to leave, go elsewhere, or do things your own way.

## To the haters and critics

Yes, markdown can't do complex structures -- grids, blocks, elaborate layouts. That's completely right.

And that's partly its beauty. It makes you keep things simple. And if you really do need more, [HTML is right there](markdown-websites.md).

## The short version

Write in markdown. Store in markdown. Build on markdown.

Own the source, and the whole ecosystem is yours. 🚀

Agree? [Fly the badge](badges.md): **We ❤ Markdown**.

---

*Credit where due: markdown was created by John Gruber with Aaron Swartz -- internet legends both. Convinced? [Why markdown-based](why.md) has the full argument; [start building](markdown-based.md) has the practice.*
