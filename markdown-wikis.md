---
title: "Markdown-based Wikis & Team Handbooks"
description: "Run your team wiki or handbook as markdown files in a git repo: everyone can edit, changes get reviewed, history comes free. The full pattern."
---

# Markdown-based Wikis & Team Handbooks

A wiki is shared, linked, evolving knowledge. Wiki software has to build the hard parts itself: edit history, who-changed-what, proposing and reviewing changes, rollback. Here's the trick of the markdown-based version: **git already does all of that**, better than any wiki engine, and it's free.

So the pattern is markdown files plus `[[wiki-links]]` in a git repository, published so it reads like a website. Everything wiki-ish falls out:

- **Anyone can edit.** GitHub's web editor means zero install: click the pencil, change the page, save. Confident colleagues use [Obsidian locally](learn/tutorial-2.md).
- **History of everything.** Every change, every author, forever. `git blame` on your holiday policy is more entertaining than it sounds.
- **Review when it matters.** Most edits go straight in. Changes to the onboarding doc or the security policy go through a [pull request](learn/tutorial-3.md): proposed, discussed, approved, merged. Wikis bolt this on badly; git was *built* for it.
- **Rollback without drama.** Someone deleted the wrong section? It's in the history.

## Setting it up

1. **A repo per wiki.** Your team handbook is one repo. (At Life Itself ours works exactly this way, and so does this site.)
2. **An index page per section**: `index.md` files that link into the section's pages. Structure stays shallow; links do the organising.
3. **Publish it** with [Flowershow](https://flowershow.app) so it reads like a proper site with navigation and search, not like a code repository. "Edit this page" links take editors straight back to GitHub.
4. **Onboard people gently.** The web editor covers the timid; the [onboarding path](learn/onboarding.md) takes a newcomer from "what's markdown?" to confident contributor in a couple of hours.

## Wiki vs knowledge base vs handbook?

Same pattern, different emphasis. A [knowledge base](markdown-knowledge-bases.md) leans personal and emergent; a handbook leans curated and stable; a wiki sits in between. The files don't care what you call them. Start writing, decide later.

## The honest limits

Real-time co-editing isn't here: git collaboration is asynchronous (edit, commit, review). For a handbook that's a feature, since considered changes beat live cursor-fights. For meeting notes being typed by four people at once, use a scratchpad and paste the result into the wiki afterwards.

And if your team is allergic to anything resembling GitHub, start them on the web editor only. It's just forms and save buttons; the git machinery stays invisible until someone's curious.

The payoff for mild upfront friction: a handbook that survives tool churn, reorganisations and vendor pricing changes, because it's a folder of text your team owns. [The way of markdown](why.md), applied to the org.
