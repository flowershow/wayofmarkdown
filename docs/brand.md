---
title: "Brand: The Way of Markdown"
publish: false
---

# The Way of Markdown

Brand, narrative and visual identity. Draft 1, 2026-10-02, distilled from [[vision]], [[naming]], the manifesto drafts, the voice profile and the tai chi work. Brief with mood board and visual directions: https://claude.ai/artifact/Qq8iMaSEk3diuEihrcLhT6 Decisions still open are marked **[open]**.

## Narrative

> Markdown is an amazing format. But what matters is what it permits: the website, the notes, the knowledge base, the thing that looks like Notion, all built from plain files you own, with tools you can swap. Markdown already won, quietly. This site shows the way to use it.

Three threads, one practice:

- **The syntax.** Ten minutes, reference-flavoured. Necessary, not the point.
- **The way.** The real curriculum: how to use the ecosystem to build what you actually want, organised by use case (site, blog, garden, catalog, Notion replacement), not by tool.
- **The proof.** Markdown is everywhere already: Google Docs, Apple Notes, Slack, GitHub, every AI chat. Ubiquity is the argument.

The ad-length version: *Markdown is great. But who cares about a format? What matters is what you can build with it, and that you own it afterwards.*

## Promise

Go from zero to a published thing you own, and understand why that was a good idea.

## Audience

Non-technical but sophisticated. Notion-tired teams, note-takers, writers who now live in AI chat, people who want a website without a platform. Developers are welcome, but we don't write for them.

## Voice

Rufus. Position first, then the case. Enthusiasm unironic ("awesome"). Honest about limits, every time. Historical analogies. Jokes with an edge, aimed at platforms, never at readers. Full profile: `.claude/skills/write-like-me/references/voice-profile.md`.

## Name and line

**The Way of Markdown.** Decided 2026-07 ([[naming]]): a practice tradition, not a movement. "Markdown is awesome" is landing-page energy, not the brand.

Tagline: **Own the source. Compose with anything.** First half is settled. Second half **[open]**: candidates in the brief (Use any tool / Build anything / Bring any tool / Plug in anything).

## Attitude: calm body, cheeky edge

Decided 2026-10-02. The identity is a practice tradition: ink, paper, patience, craft. The edge comes from push hands. Tai chi does not fight; it yields and redirects. Markdown does not fight platforms either. They push, it lets them pass. The joke lands once, elegantly (the mark can redirect a platform block off the screen), then the site gets back to work. Manifesto energy lives in the voice, not the chrome.

Not: kung fu, kicks, loud colour, "eating the world" in the header.

## Structure

Unchanged. Mostly flat, SEO slugs: guides `markdown-<x>`, per-app `markdown-in-<x>`, tutorials in `learn/`, reference in `kb/`, philosophy at `why` and `manifesto`. See AGENTS.md.

## Visual identity: "the source"

Direction **[open, recommended]**: the site shows its own source. Markdown is the one format where the raw text is already readable, so the design makes that visible instead of hiding it.

- **Type:** monospace carries the site, structure and prose alike. Geist Mono (Google Fonts), with a humanist sans (Source Sans 3) held in reserve for long prose if mono fatigues in testing. Headings show their `#` markers in the accent. No serif: that is Way Into AI's voice.
- **Colour:** warm paper `#f7f5f0`, sumi ink `#1c1b19`, muted `#6b675f`, rule `#e4e0d8`. One accent, seal vermilion `#c43b2a` (wash `#f8e3df`), used the way a seal is used: once per page, to mark what is owned or chosen. Dark: paper `#141311`, ink `#ebe7df`, vermilion `#e8705f`. Green `#16a34a` is retired as the brand accent and kept only as the roadmap's "built" status colour.
- **Form:** hairline rules, no cards, no shadows, square corners. Empty space is part of the composition. Raw and rendered side by side as the signature device, with a raw/rendered toggle where the page can carry one.
- **Mark:** the ink tai chi figure (`assets/brand/mark.svg`) as a white figure on a vermilion seal square for navbar, favicon and social. The animated syntax figure stays the hero, redone (see Mark below).
- **Not:** stock illustration, gradients, rounded cards, emoji as structure, AI-generated video.

Sibling rule: Way Into AI is mono structure, serif voice, cool paper, editor's blue, `##` markers. The Way of Markdown is mono throughout, warm paper, vermilion seal, `#` markers, ink figure. Same family, different person.

## Mark and animation

Decided 2026-08-08: the mark is the syntax figure, written in Markdown punctuation. Still true. What changes: the Gemini video on the homepage is replaced by a hand-built SVG/JS animation again, with the push-hands beat **[open, recommended]**: the figure settles, a plain block slides in from the right, the figure yields and presses, the block drifts off the edge and dissolves into `#` `*` `>`. One breath, six to ten seconds, loops. Lessons from the nine previous versions are in [[2026-08-02-markdown-tai-chi-design]] and still apply: brush ribbons not lines, derived joints, no step cycle, measure proportions standing.

The small mark is the static ink figure in a seal. It must read at 32 px; the syntax figure needs 80 px, which is why there are two.

## Explainer video

Separate track from the mark. Sixty to ninety seconds, SVG-built, telling the basic story: a file, the same file in five apps, the same file published, the same file in fifty years. Sits on the homepage below the fold or on `why`. Storyboard first, build second.

## Model split

Fable for the brand brief, the visual direction choice, the mark animation and the explainer storyboard. Opus for site CSS once a direction is chosen, the asset rendering pipeline, OG cards and the explainer build from a finished storyboard.
