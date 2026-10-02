---
title: "Brand: The Way of Markdown"
publish: false
---

# The Way of Markdown

Brand, narrative and visual identity. Draft 3, 2026-10-02 (drafts 1 and 2 same day, superseded), distilled from [[vision]], [[naming]], the manifesto drafts, the voice profile and the tai chi work. Brief (draft 3: line, feel, three logos side by side, one full front page): https://claude.ai/artifact/Qq8iMaSEk3diuEihrcLhT6 Decisions still open are marked **[open]**.

**Sequence (beads under wom-b5o, each blocks the next):** 1 narrative (wom-b5o.1) → 2 visual round from direction 1 (wom-b5o.2) → 3 logo (wom-b5o.3) → 4 implement (wom-b5o.4). Subline (wom-bm9) and explainer (wom-b5o.6) wait on narrative; hero animation (wom-b5o.5) waits on logo.

**Start here (next session).** The narrative is drafted (see Narrative below, 2026-10-02). Once Rufus signs it off, next is the visual round from direction 1 (wom-b5o.2).

**Visual baseline: direction 1, blue and clean.** Rufus likes it: `docs/brand/direction-1-manual.html` (screenshot alongside). It's from brief draft 2: Source Serif headline with an italic blue phrase, JetBrains Mono caps labels, cobalt `#2449d8` line diagram on a dotted grid, figure numbers. Draft 3 "warmed it up" and lost it; that was a misreading of his feedback. The next visual round starts from this file, not from draft 3. The brush `#` mark is unproven ("looks a bit unclean with the text"). The logo gets its own section, separate from page directions.

## Design history and Rufus's reactions (read before the visual round)

All drafts were published to one artifact link, redeployed each time: https://claude.ai/artifact/Qq8iMaSEk3diuEihrcLhT6 (its version history keeps every draft). Sources are saved in `docs/brand/briefs/`. Open them locally in a browser.

| Draft | What it was | Rufus's reaction |
|---|---|---|
| 1 (artifact v1–2) | All-mono "plain text" page, cream paper, vermilion seal, three near-identical directions. Source not kept. | Rejected. "The colour feels off, kind of boring." The directions didn't inspire. Way Into AI had more personality and better spacing, and its headings weren't just mono. |
| 2 (v3) `briefs/2026-10-02-draft-2-six-directions.html` | Story, hero options, feel, mood board, six full-hero directions: 1 manual, 2 field guide, 3 dojo, 4 poster, 5 notebook, 6 editorial. | **Direction 1 (blue, clean) is the one he likes**; saved standalone at `docs/brand/direction-1-manual.html`. Direction 4 is interesting: the big type and the little ASCII syntax picture in the corner, but not the yellow. Bits of 5 could be used, but it didn't excite him. 2, 3 and 6 didn't land. Six options was too many. |
| 3 (v4) `briefs/2026-10-02-draft-3-identity-first.html` | Line, feel, three logos side by side, one full front page (direction 1 "warmed up" with some of 4). | Rejected as a direction. Warming up 1 lost the blue clean look he liked. The three options varied only by logo. The brush `#` mark is "really interesting" and is kept as the live logo candidate, though it looks a bit unclean beside text. |

**Keep**
- Direction 1: blue `#2449d8`, clean, Source Serif headline with an italic blue phrase, JetBrains Mono caps labels, line diagram on a dotted grid, "Fig. 001" labels.
- Way Into AI's markdown-style headings (`##` marker in the accent, mono heading text), its spacing and its personality.
- Direction 4's ASCII syntax picture as a detail; maybe its headline energy.
- The brush `#` as a logo candidate.
- The headline "Markdown is eating the world."
- His three-circle sketch (easy to publish / control your content / grows when you need it to) as a figure.

**Kill**
- Cream and vermilion.
- All-mono everything.
- Yellow pages.
- Warming direction 1 into peach and green.
- Elaborate 3D or WebGL animation.
- More than three options at a time.
- Options that differ only by logo.

**References and what he took from each**
- makingsoftware.com: elegant and explanatory, diagrams; "a really beautiful website". The model for a "how formats work" section (bead wom-w74).
- Wikimedia Thank You 2019 header (https://upload.wikimedia.org/wikipedia/donate/9/9a/Thank_You_2019_Header.svg): the beautiful isometric illustration and its colour. Direction 2 didn't capture it.
- code.storage: the page looks like markdown source, with `#` headings and ASCII tables. Its 3D blob is "far too elaborate for what we want".
- Notion: the bar for polish and accessibility ("doesn't look anywhere near as good as Notion").
- Way Into AI brief (https://claude.ai/artifact/DLpmX593GvBX214vHLxCb9): the process that worked. Directions side by side, story settled first.

## Settled so far

- **Name.** The Way of Markdown (2026-07, [[naming]]).
- **Headline.** **Markdown is eating the world.** (agreed 2026-10-02)
- **Synthesis (draft).** Easy (so simple every tool can implement it), you own it, it grows when you need it to. See Narrative.
- **Feel.** Warm, clear, a bit geeky, open, made by a person who is excited about this. See Feel below.
- **Not the point.** Markdown the syntax. Flowershow stays secondary ([[vision]]).

## What the site is for (Rufus, 2026-10-02)

You can learn markdown, and you can learn the tooling around it. But what will actually excite people is **seeing it applied to an area they care about**: how to switch from Notion to markdown, how Obsidian works, the note-taking ecosystem, publishing a site. People come for an application, not for a format. The job of the story is to make those application pages hang together as one coherent idea.

## Narrative (draft for Rufus to review, 2026-10-02, wom-b5o.1)

### The claim

**Markdown is eating the world.** It's happening, and you can see it: AI chat answers in it, Notion and Google Docs import and export it, GitHub, Obsidian and every docs tool run on it. The headline states something you can check. It isn't a call to arms.

### Why it's winning

Markdown is in the empty middle of Rufus's three circles (sketch: `docs/brand/three-circles-sketch.png`). Other formats get two of the three. Markdown gets all of them:

1. **Easy.** Easy to write, read and use, and easy to publish. The key part is less obvious: it's so simple that **every tool can implement it**. "Everyone can use it" is the wrong version of this point, because for years most people didn't. It was geeky. Machines took to it first, and AI most of all.
2. **You own it.** It's plain text in files you hold, open, readable in fifty years, and no app can lock it up.
3. **It grows when you need it to.** Tables, frontmatter, wikilinks, fenced blocks (mermaid, maths, data), raw HTML. You start with a note and end up with a site, a catalog or a database without changing format.

The ecosystem follows from 1 and 2. Every tool can implement it and nobody owns it, so the tools multiply and they compose. You don't get one app that does everything. You chain tools: Obsidian to write, Git for history, a publisher to put it online. That gets you *most* of what Notion or WordPress does, and some things they can't, such as owning the files, versioning everything and swapping any piece. Honest limit: real-time co-editing and polished databases are still weaker.

### The story: the tools caught up (why it's called the Way)

The format didn't change much. The tools around it did. Markdown's first UX was a text box on the web, plus READMEs and developer tools. Over twenty years an ecosystem of tools, much of it open source, kept improving: Obsidian with live preview, WYSIWYG editors, static site publishers, Git hosting, and now AI that writes markdown by default. Each tool may still be a bit behind its closed rival (Obsidian versus Notion, say), but it gets better every year. Together they compose into something no single app offers. That ecosystem, and the practice of putting it together to do what you need, is **the way** in the Way of Markdown. The story goes in the Why area and in a blog post (wom-bc1).

### Value proposition (for a visitor)

What you get by working this way:

- **Easy to use.** Learn it in ten minutes, and AI already writes it for you.
- **A huge ecosystem.** Whatever you want to do, there's a tool for it, and the tools work together.
- **You own it.** Your files, any tool, no lock-in.

What the site gives you: the way to do the things you already do (notes, docs, a website, a team wiki, leaving Notion) with markdown tools, plus enough understanding of the format and why it's winning to make good choices.

### Areas

Three, following Rufus's list. The claim joins them: each area takes one angle on "markdown is eating the world".

| Area | What's in it | Visitor's question |
|---|---|---|
| **Use it** | Applications and switching: leave Notion, how Obsidian works, notes, publish a site, team docs, a catalog. The centre of the site. | "Can I do my thing this way?" |
| **Learn it** | The format, nuts and bolts: basics, extensions, how markdown appears in each app, why AI speaks it. | "What is this, and how far does it go?" |
| **Why** | The claim argued: manifesto, vision, the worse-format-won story, the ecosystem map (wom-3m1). | "Why is this happening, and why should I care?" |

People arrive through **Use it** (a search for "Notion to markdown"), pick up **Learn it** along the way, and some go on to **Why**. The front page reverses this: claim first, then the ways in.

### Tone

Invitational, not didactic. "Find out why", never "here's why". Intriguing over explanatory: a line should make people want the next one. Honest limits, always ("most of what Notion does", never "everything"). The excitement is unironic, Rufus's own.

### Tensions, resolved

1. **Manifesto headline versus practice name.** The order is claim, then way. The headline observes what's happening, and the rest of the site is the practice of joining in. Manifesto energy stays in the headline and the Why area. The other areas are practical.
2. **Format brand versus application content.** The brand is about the format because the format is the one thing all the application pages share. The front page's first action is an application, so the format brand never stands between a visitor and what they came for.
3. **Three threads versus one story.** Three areas joined by the claim (above).
4. **Calm versus fun.** Narrative side: fun lives in the headline, the story and the voice, and the body stays calm and practical. How that splits in the visuals is for the visual round (wom-b5o.2).
5. **Breadth versus entry.** One list does both jobs. The front page's list of things you can do is the evidence that markdown is eating the world, and each item is a way in.

### Hero

Headline agreed. The hero copy is the narrative above, compressed: easy to use, easy to extend, a huge ecosystem (easy for machines, especially AI), open so you own it. Exact subline wording is deliberately loose. It's easy to change, and wordsmithing it before the page exists was a dead end (2026-10-02). Candidates so far, none chosen:

- "It started as a geeky shortcut for web text boxes. Now AI speaks it and the tools keep coming. Find out how it won, and how to make it work for you."
- "Easy to use, easy to extend, a huge ecosystem of tools, and you own it. Find out how to make it work for you."

Rejected: "Everything you do in Notion…" (untrue; most, not everything), "Here's why" (didactic), "so simple everyone can use it" (wrong point), "one open format, an ecosystem of tools that compose" (explanation, not message), "the format unlocks an ecosystem" ("of what?"), "the worse format won" (compares absolutes; the story is the tools improving).

## Sign-off

No sign-off decided. "Openness is the way" was an idea Rufus threw out, not a pick. "Own the source" stays inside the manifesto as an argument.

## Feel

Warm, clear, a bit geeky, open. Made by a person who is excited about this. Like Notion's friendliness, Wikipedia's openness, Making Software's clarity, and a poster's confidence in the headline. Not a technical manual, a terminal, a SaaS landing page, a monastery, or anything elaborate for its own sake (Rufus on code.storage: "far too elaborate for what we want").

## Audience

Non-technical but sophisticated. Notion-tired teams, note-takers, writers who now live in AI chat, people who want a website without a platform. Developers are welcome, but we don't write for them.

## Voice

Rufus. Position first, then the case. Enthusiasm unironic ("awesome"). Honest about limits, every time. Historical analogies. Jokes with an edge, aimed at platforms, never at readers. Full profile: `.claude/skills/write-like-me/references/voice-profile.md`.

## Name and line

**The Way of Markdown.** Decided 2026-07 ([[naming]]): a practice tradition, not a movement. "Markdown is awesome" is landing-page energy, not the brand.

Former tagline "Own the source. Compose with anything." is retired from the hero. "Own the source" lives on inside the manifesto.

## Attitude: calm body, cheeky edge

Decided 2026-10-02. The identity is a practice tradition: ink, paper, patience, craft. The edge comes from push hands. Tai chi does not fight; it yields and redirects. Markdown does not fight platforms either. They push, it lets them pass. The joke lands once, elegantly (the mark can redirect a platform block off the screen), then the site gets back to work. Manifesto energy lives in the voice, not the chrome.

Not: kung fu, kicks, loud colour. (This section originally also ruled out "eating the world" in the header; that line is now the agreed headline. See Tensions 1 and 4.)

## Illustration system

One per thing you can build: a site, a blog, a garden, a catalog, the Notion-shaped thing, a team's docs. Isometric panels in the Wikimedia style, ink outline, flat fills, small figures writing, linking and publishing. Hand-drawn SVG, versioned in the repo, never AI-generated. Illustrations may use two or three flat colours beyond the accent (indigo, green, orange are the Wikimedia set; ours to be chosen with the accent); the UI keeps to one accent. The same language draws the explainer video, so the two jobs share one style.

## Structure

Unchanged. Mostly flat, SEO slugs: guides `markdown-<x>`, per-app `markdown-in-<x>`, tutorials in `learn/`, reference in `kb/`, philosophy at `why` and `manifesto`. See AGENTS.md.

## Logo **[open; nothing recommended]**

Rufus on draft 3: the brush `#` is "really interesting", might work at the top of the page, but looks a bit unclean beside text. It's the live candidate to develop. The other two are unproven. The logo is explored in its own session, after the page direction (bead wom-b5o.3).


Three options in the brief, side by side:

- **A. Brush hash (recommended).** Markdown's `#`, written in four brush strokes with a loaded start and a dry tail. The `#` says markdown and the brush says "the way". It holds at 16 px. It writes itself once on load. The same glyph is the heading marker site-wide, so the logo is a system rather than a badge. Source: `docs/brand/hash-brush.svg`, generated by `docs/brand/hash-brush-gen.py`.
- **B. Blocks.** Four glyph tiles (`#` `*` `>` `-`) in green, orange, indigo and mustard that rearrange into a line, a column and a square. It's fun, but tile logos are common and at 16 px no markdown is left in it.
- **C. Practitioner.** The ink tai chi figure pressing out of an orange sun. It's warm and human, but it says nothing about markdown. Better as the site's character (hero, 404, manifesto, press kit) than as the logo.

## Visual identity **[open; baseline is direction 1]**

Drafts 1 and 2 are superseded. Draft 1 was all-mono with cream paper and a vermilion seal, and read as boring. Draft 2 showed six directions. Rufus found direction 1 (manual) the closest but cold, blue and technical. Direction 4 (poster) had energy and a good ASCII detail, though the yellow was too much. He wants no more than three options at a time, and judges best on full pages.

Draft 3 front page is direction 1 combined with some of direction 4, warmed up:

- **Type.** Bricolage Grotesque 800 for display (from 4). Source Serif 4 for body. JetBrains Mono for labels, code and headings.
- **Headings.** Markdown-style, as on Way Into AI and code.storage: mono uppercase with the brush hash as the marker, coloured green, orange or indigo per section.
- **Colour.** Warm paper `#fbf8f2`, ink `#1d1b19`, green `#1f8f62` as the UI accent, and orange `#ec7a3c` for highlights. Illustration fills are mint `#d3ecdf`, peach `#fbdcc8`, lavender `#dde0f4` and butter `#fff3d6`.
- **Graphics.** Flat fills with ink outlines, figure labels ("Fig. 001"), a dotted grid behind the hero, and an ASCII ecosystem diagram. Motion is small: the mark draws itself, and a few glyphs travel along the hero diagram's lines.
- **Sections.** Hero with the one-file-many-tools figure. "One open format" with the Unix paragraph, tool chips and the ASCII diagram. "What will you build?" as a six-cell grid with icons. "One file, two views" (raw and rendered). "Why it works" (the three-circle figure). "Start here" (three steps). Footer reads "~ Openness is the way ~".

The sibling constraint with Way Into AI is dropped (Rufus: people won't visit both).

## Mark and animation

Decided 2026-08-08: the mark is the syntax figure, written in Markdown punctuation. Still true. What changes: the Gemini video on the homepage is replaced by a hand-built SVG/JS animation again, with the push-hands beat **[open, recommended]**: the figure settles, a plain block slides in from the right, the figure yields and presses, the block drifts off the edge and dissolves into `#` `*` `>`. One breath, six to ten seconds, loops. Lessons from the nine previous versions are in [[2026-08-02-markdown-tai-chi-design]] and still apply: brush ribbons not lines, derived joints, no step cycle, measure proportions standing.

The small mark is the static ink figure in a seal. It must read at 32 px; the syntax figure needs 80 px, which is why there are two.

## Explainer video

Separate track from the mark. Sixty to ninety seconds, SVG-built, telling the basic story: a file, the same file in five apps, the same file published, the same file in fifty years. Sits on the homepage below the fold or on `why`. Storyboard first, build second.

## Model split

Fable for the brand brief, the visual direction choice, the mark animation and the explainer storyboard. Opus for site CSS once a direction is chosen, the asset rendering pipeline, OG cards and the explainer build from a finished storyboard.
