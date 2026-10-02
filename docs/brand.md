---
title: "Brand: The Way of Markdown"
publish: false
---

# The Way of Markdown

Brand, narrative and visual identity. Draft 3, 2026-10-02 (drafts 1 and 2 same day, superseded), distilled from [[vision]], [[naming]], the manifesto drafts, the voice profile and the tai chi work. Brief (draft 3: line, feel, three logos side by side, one full front page): https://claude.ai/artifact/Qq8iMaSEk3diuEihrcLhT6 Decisions still open are marked **[open]**.

**Sequence (beads under wom-b5o, each blocks the next):** 1 narrative (wom-b5o.1) → 2 visual round from direction 1 (wom-b5o.2) → 3 logo (wom-b5o.3) → 4 implement (wom-b5o.4). Subline (wom-bm9) and explainer (wom-b5o.6) wait on narrative; hero animation (wom-b5o.5) waits on logo.

**Start here (next session).** The visual direction is decided (2026-10-02, wom-b5o.2 closed). Read "Design direction" below; it is the spec. The working mock is https://claude.ai/artifact/PiAxmgGNG5Prsn1GhV4VMm (three pages: front, the Replacing Notion guide, and a design-basis page with tokens and components; source `docs/brand/round-3/opt4/`, built by `build.py` from `*.src.html`, `sketches.py` and `twoviews.svg`). Earlier rounds stay for comparison: round 3 compare https://claude.ai/artifact/5HpEiFyf47X5QGgWgKUZzL, option 1 https://claude.ai/artifact/WrGGWVdezcUmwMjAC7rpii, mood board https://claude.ai/artifact/KyALRZTDrC7e5fEs4KX2s6, reference gallery https://claude.ai/artifact/3yFuLuEBGzVquzbyCS2MLJ. Open items are beads under wom-b5o (see "Open questions and todos"). Next in sequence: logo (wom-b5o.3), then implement (wom-b5o.4). Before acting on Rufus's design feedback, restate it as keep / change / kill.


## Design history and Rufus's reactions (read before the visual round)

All drafts were published to one artifact link, redeployed each time: https://claude.ai/artifact/Qq8iMaSEk3diuEihrcLhT6 (its version history keeps every draft). Sources are saved in `docs/brand/briefs/`. Open them locally in a browser.

| Draft | What it was | Rufus's reaction |
|---|---|---|
| 1 (artifact v1–2) | All-mono "plain text" page, cream paper, vermilion seal, three near-identical directions. Source not kept. | Rejected. "The colour feels off, kind of boring." The directions didn't inspire. Way Into AI had more personality and better spacing, and its headings weren't just mono. |
| 2 (v3) `briefs/2026-10-02-draft-2-six-directions.html` | Story, hero options, feel, mood board, six full-hero directions: 1 manual, 2 field guide, 3 dojo, 4 poster, 5 notebook, 6 editorial. | **Direction 1 (blue, clean) is the one he likes**; saved standalone at `docs/brand/direction-1-manual.html`. Direction 4 is interesting: the big type and the little ASCII syntax picture in the corner, but not the yellow. Bits of 5 could be used, but it didn't excite him. 2, 3 and 6 didn't land. Six options was too many. |
| 3 (v4) `briefs/2026-10-02-draft-3-identity-first.html` | Line, feel, three logos side by side, one full front page (direction 1 "warmed up" with some of 4). | Rejected as a direction. Warming up 1 lost the blue clean look he liked. The three options varied only by logo. The brush `#` mark is "really interesting" and is kept as the live logo candidate, though it looks a bit unclean beside text. |
| Round 2 (new artifact, 2026-10-02) `round-2/` | Three full pages from direction 1: A manual, B poster, C source. Compare page with side-by-side and full-size views. | Awaiting reaction. |

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
- **Headline shape (agreed 2026-10-02).** Kicker, small mono: *Markdown is eating the world.* H1: **The Way of Markdown.** H2: *There's a better way to do your notes, docs and site. It's plain text.* H3, quieter, carries the philosophy: *A practical guide to doing it with files you own, and the philosophy underneath: simple, open, yours.* H2 and H3 wording loose; the shape is fixed. "Eating the world" is the thesis and an essay title, for the Why page and the kicker, never the big type.
- **The feel (agreed 2026-10-02): a manual.** See "The feel" below.
- **Narrative (draft 4).** Two forces (simple for people, simple for tools) fed each other until markdown was everywhere; the tools matured, so you can switch. See Narrative.
- **Feel.** Warm, clear, a bit geeky, open, made by a person who is excited about this. See Feel below.
- **Not the point.** Markdown the syntax. Flowershow stays secondary ([[vision]]).

## What the site is for (Rufus, 2026-10-02)

You can learn markdown, and you can learn the tooling around it. But what will actually excite people is **seeing it applied to an area they care about**: how to switch from Notion to markdown, how Obsidian works, the note-taking ecosystem, publishing a site. People come for an application, not for a format. The job of the story is to make those application pages hang together as one coherent idea.

## Narrative (agreed 2026-10-02, wom-b5o.1; joining sentence still open)

Source: Rufus's dictation, verbatim in `docs/raw/2026-10-02-brand-dictation.md`. Quote from there when writing the Why pages, the explainer or the blog post.

### The offer line

> The tools are good now. You can switch, and you own your files.

Rufus, 2026-10-02: "the essence of the main offer we're making." This is the reason to care, in the reader's terms. The site shows people how to switch to markdown-based tools for the things they want to do, and gives the geeks something to send their friends.

**"You own your files" means files over app.** It's about not being locked in. If you own the files, you can use any app you like, including the best ones and the latest AI, and you benefit as the ecosystem grows. Privacy people are welcome, but privacy isn't the point. Where the line appears, an asterisk or follow-up can say so.

### The joining sentence **[open, deliberately]**

The narrative doesn't depend on one sentence. That's why it's a narrative. Short candidates, for later:

1. "Simple enough for people to write and every tool to speak. Now the tools are good enough to switch to."
2. "Simple enough for people to write and every tool to speak, AI included."
3. "Everyone's tools speak markdown now. Time to switch."

### The claim

**Markdown is eating the world.** It's meant to make people ask "what is that?". Underneath, the site is calmer and practical, and that gap is deliberate. The claim is checkable: AI chat answers in markdown, Google Docs imports and exports it, and GitHub, Obsidian and most docs tools run on it.

### The story: how it ate the world

This is the key non-obvious point and the spine of the site. It's a candidate for the explainer animation (wom-b5o.6) and the blog post (wom-bc1). Nobody cares about formats, any more than they care about TCP/IP. You care about what it enables. Markdown is one of the rare cases where the format made the difference.

It isn't a straight line. **Two forces met and fed each other:**

- **Simple for people.** Humans could write it by hand, so web text areas and developer docs systems took it as their source format (Rufus was writing markdown in 2006). Familiarity spread: today even non-technical people use markdown-style formatting in WhatsApp or Discord.
- **Simple for tools.** Plain, limited, closer to CSV than to JSON, open so nobody controls it, extensible so builders could add what they needed. Any tool could support it. Rufus's three circles (`docs/brand/three-circles-sketch.png`: easy, open, extensible) are the builder's view of this.

More people writing it meant more tools supporting it, and more tools meant more people writing it. That flywheel reached critical mass well before AI. Meanwhile the tools kept improving: the first markdown UX was a bare text box, and now there's Obsidian with live preview and bases, WYSIWYG editors, publishers and Git hosting. Some of it is open source (Pandoc, static site generators, Git), some closed but file-based (Obsidian). Each may still be a step behind its closed rival, but the gap closes every year.

**AI amplifies it, and didn't cause it.** Markdown was everywhere before AI. Language models now write it almost by default, which adds one more huge tool that speaks it. That's worth a big item on the site, without claiming AI is the reason.

**The result for you: you can switch.** The ecosystem has matured. Most of what you do in Notion, Google Docs or WordPress you can do with markdown tools, combining them instead of living inside one monolithic app, and keeping the files.

The two forces belong on the Why page. The result leads on the front page.

### Why this is hard to say

Worth knowing before anyone tries to compress the story again. It took a day of back and forth (2026-10-02), and each failed version failed in one of these ways:

1. **The core idea is a loop.** People could write markdown, so tools supported it. Tools supported it, so more people wrote it. That ran until critical mass, and the tools matured. Sentences are linear, so every compression distorted it ("everyone uses it", "the worse format won", "AI is why it's everywhere").
2. **The cause and the payoff are for different people.** It happened for builders' reasons (simple, open, extensible). It matters to users for a different reason (the tools are good now, so you can switch and own your files). One line has to carry both the mechanism and the reason to care.
3. **It's a paradox.** A format matters even though nobody cares about formats. People care about using the internet to bank or buy clothes, not about TCP/IP. Use that analogy lightly: the geeks get it, everyone else just wants the result.

So: tell the loop as a picture (flywheel diagram, explainer animation), lead with the payoff for readers, and keep the mechanism for the Why area. Blog posts: wom-bc1 (how the tools caught up) and wom-d2x (why this is hard to say).

### Value proposition

The only public list. Everything else in this doc is internal structure.

- **Easy.** You can learn it in under ten minutes, AI already writes it, and it goes further than you think.
- **A whole ecosystem of tools.** Whatever you want to do (notes, docs, a site, a catalogue, a Notion replacement), there are good tools for it, and you can combine them instead of being stuck in one monolithic app.
- **It's yours, and it grows with you.** Plain files you own, so you're free to switch, upgrade and adapt, and it grows from a note to a site to a database without changing format.

The offer, in Rufus's words: how to do the workflows you already want using markdown, and why it's showing up everywhere.

### Why "the Way" (two meanings)

1. **A guide.** A practical way of organising your tooling: what to adopt and what to use for notes, docs, a site or a catalogue. The site is, at heart, a how-to guide, with an edge.
2. **A philosophy.** Openness and simplicity, the Unix idea that simple pieces beat complex monoliths like Notion or Google Docs. If your stuff is in markdown, you're always free to upgrade, switch and adapt (to the next tool, or to AI). The Obsidian "file over app" idea.

Like the Tao, it's a philosophy and also something you practise. The way covers all the markdown-based ways to get things done, shown one application at a time, rather than one recipe for composing tools.

### Areas

Three. Each maps to part of the joining sentence and to one meaning of the Way.

| Area | What's in it | Visitor's question | Maps to |
|---|---|---|---|
| **Use it** | Applications and switching: Obsidian, notes, publish a site, team docs, a catalogue, leave Notion. The centre of the site. | "Can I do my thing this way?" | "you can switch"; the Way as guide |
| **Learn it** | The format, nuts and bolts: basics, extensions, markdown in each app, why AI speaks it. The ground floor of the guide. | "What is this, and how far does it go?" | "simple enough"; the Way as guide |
| **Why** | The story above in full, the three circles, AI, the manifesto, the ecosystem map (wom-3m1). | "What's going on, and why should I care?" | "every tool can build on it"; the Way as philosophy |

People arrive through **Use it** or **Learn it** (a search for "Obsidian publish" or "markdown for ChatGPT"), and some go on to **Why**. The front page reverses this: claim, then the reader's story, then the ways in.

### Audience on the page


- **The early sweet spot** (Obsidian users, people partway in, evangelists) already believes the format story. What they get: the practical guide to go further, discoveries outside their own territory ("I didn't know that tool supports markdown"), and links to send friends and colleagues (how to copy markdown out of Google Docs, how to leave Notion). Write pages to be forwarded.
- **The markdown core group** (an important early audience) may come for the Why itself: the thesis, the story, the inspiration. The Why area is a destination, not only background.
- **The wider non-technical audience** gets steps 3 to 5 and the value proposition first. The builders' story waits on the Why page for anyone who wonders why.

### Tone

Invitational, not didactic: "find out why", never "here's why". Intriguing over explanatory: a line should make people want the next one. Honest limits, always ("most of what Notion does", never "everything"). Rufus's excitement is unironic and a bit evangelical, and that's fine.

### Tensions, resolved

1. **Manifesto headline versus practice name.** "The Way" carries both meanings: the philosophy (the claim, the Why area) and the practice (the guide, Use it and Learn it). The headline is loud on purpose. The rest of the site is practical.
2. **Format brand versus application content.** The story explains why the format matters even to people who don't care about formats. The front page's first action is still an application.
3. **Three threads versus one story.** One joining sentence, one story (the chain above), three areas.
4. **Calm versus fun.** Narrative side: fun lives in the headline, the story and the voice, and the body stays calm and practical. The visual split is for the visual round (wom-b5o.2).
5. **Breadth versus entry.** One list does both jobs. The front page's list of things you can do is the evidence that markdown is eating the world, and each item is a way in.

### Hero

Headline agreed. Under it, the hero compresses the reader's story and the value proposition. Exact subline wording is deliberately loose: it's easy to change, and wordsmithing it before the page exists was a dead end (2026-10-02). The joining sentence is itself a subline candidate. Others, none chosen:

- "It started as a geeky shortcut for web text boxes. Now AI speaks it and the tools keep coming. Find out how it happened, and how to make it work for you."

Rejected: "Everything you do in Notion…" (untrue; most, not everything), "Here's why" (didactic), "so simple everyone can use it" (wrong point: every *tool*), "one open format, an ecosystem of tools that compose" (explanation, not message), "the format unlocks an ecosystem" ("of what?"), "the worse format won" (compares absolutes; the story is the tools improving), "the way is composing tools" (too narrow), "created by a couple of geeks in a weekend" (unsourced; Gruber with Swartz's input, 2004).

### Claims status

Confirmed by Rufus 2026-10-02: Google Docs imports and exports markdown; Notion exports markdown (Rufus has used it); LLMs write markdown almost by default; you can learn the basics in under ten minutes; the tools gap closes every year. WhatsApp and Discord formatting is markdown-*style* (Discord is close to markdown; WhatsApp uses its own `*bold*` variant), so say "markdown-style" in print.

## Sign-off

No sign-off decided. "Openness is the way" was an idea Rufus threw out, not a pick. "Own the source" stays inside the manifesto as an argument.

## Feel (earlier wording, superseded by "The feel" below)

Warm, clear, a bit geeky, open. Made by a person who is excited about this. Like Notion's friendliness, Wikipedia's openness, Making Software's clarity, and a poster's confidence in the headline. Not a technical manual, a terminal, a SaaS landing page, a monastery, or anything elaborate for its own sake (Rufus on code.storage: "far too elaborate for what we want").

## Audience

Non-technical but sophisticated, eventually: Notion-tired teams, note-takers, writers who now live in AI chat, people who want a website without a platform. Honestly, the early sweet spot is the geekier end: Obsidian users, people already partway in, and evangelists who'll pass it on (Rufus, 2026-10-02). Write so the first group can follow and the second group wants to share it. Developers are welcome, but we don't write for them.

## Voice

Rufus. Position first, then the case. Enthusiasm unironic ("awesome"). Honest about limits, every time. Historical analogies. Jokes with an edge, aimed at platforms, never at readers. Full profile: `.claude/skills/write-like-me/references/voice-profile.md`.

## Name and line

**The Way of Markdown.** Decided 2026-07 ([[naming]]): a practice tradition, not a movement. "Markdown is awesome" is landing-page energy, not the brand.

Former tagline "Own the source. Compose with anything." is retired from the hero. "Own the source" lives on inside the manifesto.

## Attitude: calm body, cheeky edge

Decided 2026-10-02. The identity is a practice tradition: ink, paper, patience, craft. The edge comes from push hands. Tai chi does not fight; it yields and redirects. Markdown does not fight platforms either. They push, it lets them pass. The joke lands once, elegantly (the mark can redirect a platform block off the screen), then the site gets back to work. Manifesto energy lives in the voice, not the chrome.

Not: kung fu, kicks, loud colour. (This section originally also ruled out "eating the world" in the header; that line is now the agreed headline. See Tensions 1 and 4.)

## The feel (agreed 2026-10-02)

**A manual for a way of working, written by someone who finds it genuinely exciting.** Rufus: "pretty good now, write it down."

Tone: calm *and* passionate. Friendly, informal, a bit jokey, with an evangelical edge. The passion is for simplicity, craft, openness, freedom. Not "cheeky" (his word to drop). PostHog's no-nonsense tone turned down a notch; "a bit too arf-arf for us".

On the page:

1. **It's a manual, with two halves that weigh the same.** One half explains from the ground up, makingsoftware style: what formats are, what they enable, how adoption actually happens (economics and social dynamics, TCP/IP as the analogy). Essays in that register are the Hacker News door; the markdown-databases intro proved it. The other half is practical how-to guides, and "replacing Notion" is the biggest of them. The design has to carry both: detailed explaining and higher-level how-tos.
2. **Explain by showing.** Figures, diagrams, raw beside rendered. The viz explains the concept, cleverly and beautifully (code.storage). The diagram is the argument (makingsoftware). "Demonstrate, don't proclaim" ([[vision]]).
3. **Light paper, air, fine lines.** What his kept references share: makingsoftware, code.storage, Co-Star, cosmos.so. Faint grids, mono caps labels, an elegant display face, nothing cramped. Notion-level polish.
4. **One colour, two at most, warmed by illustration.** Blue `#2449d8` looks good and stays the working colour; one alternative gets tried in the visual round. Warmth comes from drawn panels with people in them, Wikimedia-style flat fills with ink outlines, using the site colours plus tints. Diagrams in blue means links need their own treatment (underline, or the second colour).
5. **More human than makingsoftware.** Beautiful but cold, "technical diagrams". People doing things in the illustrations. The tai chi figure as the site's character.
6. **Embeds and screenshots follow the style.** A screenshot of another app (Obsidian's dark table, say) breaks the page. Where we can, redraw it in house style as a figure; where we can't, frame it as a figure with a caption. Illustrations and embeds are one system.
7. **The humour is in the words.** Footnotes, captions, the manifesto's asides. Never in the layout.

Wording note: "Leave Notion" is negative; nobody wants to leave. Say "Replacing Notion" or "a markdown Notion": Notion, with content you own.

## Design direction (decided 2026-10-02)

The spec for implementation (wom-b5o.4). Source of truth for values is `docs/brand/round-3/opt4/site.css` and `sketches.py`; this section says what and why.

**In one line.** Devouring Details' page (a white sheet on a grey ground, big quiet grotesk, one orange) carrying Sketchplanations-style explanatory drawings, redrawn in the site's own fonts and lines so the two don't clash. Rufus, 2026-10-02: "number 2 is the best", "we really want 2 + 3's drawings", then "there's too much of a clash ... keep the drawing, the spaciousness, the informality, but have the font be like option 2".

### Page
- **Ground and sheet.** Page background light grey `#ececec`; content on a white sheet, max width 1040px, generous padding (up to 96px sides on desktop), 64px top margin. The sheet is the page; nothing full-bleed.
- **Masthead.** Orange dot, site name in sans, under it a mono caps kicker with a `#` mark (`# MARKDOWN IS EATING THE WORLD` on the front page; the breadcrumb `# USE IT / 01` on guide pages). Nav as a short vertical list top right (Use it, Learn it, Why, Manifesto, About). **Nav is not final** (Rufus: "not yet sure about navbar"); option 1's horizontal mono bar is the alternative.
- **Side ruler.** A fixed column of small tick marks at the left edge, from Devouring Details. Decorative for now; could become a page-position indicator. Keep or drop at implementation.
- **No running line.** The orange horizontal line with a chip was tried and killed ("annoying, unhelpful").

### Colour
- **One colour: orange `#ff5a00`.** Chosen over blue at page scale. Used for: kicker and section labels, figure titles, numbers, links, primary button fill, panel edges, and the one accent fill inside drawings (pale `#ffd3bb`).
- Ink `#111`, muted `#6b6b6b`, rules `#dcdcdc`, soft orange `#fff1e8` for the honesty callout.
- Blue `#2449d8` is retired from the UI. It may survive in the few technical line diagrams (see Illustration) if they need a second colour; decide then.
- **Dot grid** `#d6d6d6`, 9px pitch, as the background of every figure panel and card. Rufus wants it "quite tight, tighter than option 1" and possibly finer still (todo).

### Type
- **Sans: Inter** (400, 500, 600). Body 19px / 1.5 on the front page, 17px on long reading pages is fine. Display: H1 weight 500 at up to 58px, letter-spacing -0.025em; section H2 weight 500 at 26 to 34px; card and list H3 weight 500 at 19 to 22px. Nothing bold-heavy.
- **Mono: JetBrains Mono** for every label: kicker, `## SECTION` labels, figure titles (`FIG. 1 · ONE FILE, ANY TOOL`), numbers, buttons, table headers, metadata, code. 10.5 to 11px, letter-spacing 0.08 to 0.1em, uppercase.
- **Serif italic: Source Serif 4 italic**, only for the emphasised phrase in a lead sentence ("*It's plain text.*", "*how*", "*is*"). One or two per page.
- **Markdown marks.** The kicker takes a `#`, section labels take `##`, in orange. From option 1 and Way Into AI. Rufus: "merge the ## headings style from option 1 in some way". Keep light.
- Hand fonts (Patrick Hand, Caveat) are out. They caused the clash.

### Layout
- **Front page order.** Masthead → H1, H2, H3, two buttons (one column, max 60ch) → hero figure panel (max 820px) → "Use it" six cards → "Learn it" figure left, text right → "Why" text left, figure right (or alternate) → "Start here" three cards → footer.
- **Grid sections** (six things, three steps) are centred: `## LABEL`, centred H2, centred sub, then a 3-column grid of cards. From option 3's layout, in option 2's type.
- **Figure + text rows** are two columns, figure on the left where it makes sense (from option 1).
- **Guide pages.** Title and mono meta, a lead paragraph at 21 to 26px, body at 19px in a 62ch column, mono `##`-style H2s, a sticky right column with "On this page" and "Next". Tables with mono caps headers and an orange rule. Code blocks on `#fafafa` with 12px radius. The honest-limits block on soft orange, 14px radius, with a mono caps title. Figures as panels, captioned.

### Components
- **Figure panel.** White with the dot grid, 1px orange edge, square corners, 12 to 14px padding. Top left a mono orange title `FIG. n · TITLE` (CSS counter). Caption below in 14px muted sans. Every illustration lives in one.
- **Card.** Same surface and edge as the panel. Centred: mono number (`01 · START HERE`), icon (96px tall), H3, one-line description. Hover thickens the edge.
- **Buttons.** Mono caps 11px, 9px by 12px padding, 1px ink border; primary is orange fill, white text. No radius.
- **Links in prose.** Orange, no underline on guide pages (sheet is quiet enough); underline is fine in dense text.

### Illustration
- **Two kinds.** (1) *Sketches*: friendly explanatory drawings with stick figures, the main kind, everywhere a figure is needed. (2) *Technical line diagrams* (option 1 style: fine lines, boxes, dashed connectors): only for ground-up explainers such as what a format is, bytes in a file, how markup works. Rufus finds them cold and too small elsewhere, "unless animated".
- **Sketch style.** Ink `#111` lines at 1.5px, round caps and joins, no wobble filter, no hand lettering. Labels in JetBrains Mono caps, 8 to 10px. Fills: white, neutral grey `#f0f0f0`, and the pale orange `#ffd3bb` as the single accent. No cream, no pale blue, no green.
- **Stick figures stay.** Rufus: "we need stick figures, maybe just a bit more polished, but def keep". Round head with a dot eye and a small smile, single-line body and limbs, one arm doing something (holding, pointing, waving). Polish is a todo.
- **Generated, not drawn.** All sketches are produced by `sketches.py` (and the hero by code too), so the style is reproducible and editable. Hand-drawn illustration is off the table for this project. If a sketch can't be coded well, it doesn't exist yet.
- **Existing scenes.** Hero "one file, any tool"; "one file, two views"; "two forces" (people and tools push a wheel, AI joins late); six card icons; guide figures "three files, one table" and "not a free lunch" (a balance). Each panel is one idea, one caption.
- The Wikimedia isometric idea and the tai chi figure are not in this system yet. The tai chi figure stays the logo and character candidate (wom-b5o.3); whether it appears inside sketches is open.

### Headline, on every mock
Kicker `# MARKDOWN IS EATING THE WORLD` · H1 **The Way of Markdown** · H2 *There's a better way to do your notes, docs and site. It's plain text.* · H3 *A practical guide to doing it with files you own, and the philosophy underneath: simple, open, yours.* H2 and H3 wording still loose (wom-bm9).

### Wording rules that came out of the design
- "A markdown Notion" / "Replacing Notion", never "Leave Notion" (negative; nobody wants to leave).
- Six things, in this order: a markdown Notion (start here), notes, a website, a blog, team docs and wikis, a catalogue or database.
- Captions say the point of the figure in one plain sentence; the figure title is a label, not a sentence.

## Open questions and todos (2026-10-02)

Each is a bead under wom-b5o unless noted. Minor ones are logged, not blocking.

1. **Logo** (wom-b5o.3): own session. Brush `#` and the tai chi figure are the candidates; how a mark sits in this masthead is part of the brief.
2. **Nav bar**: vertical list (current) or option 1's horizontal mono bar. Rufus unsure. Decide at implementation with a side-by-side.
3. **Dot grid finer**: try 7 or 8px pitch and a lighter dot; check it doesn't shimmer on retina.
4. **Stick figure polish**: consistent proportions, better hands and posture, a small set of poses in `sketches.py`.
5. **Sketch library**: one scene per guide and per Why page; a style note so new sketches match. Decide whether the tai chi figure is the recurring person.
6. **Technical diagrams**: a small set for the ground-up explainers, in the panel system, possibly animated so they aren't "too small and fancy".
7. **Guide page**: Rufus hasn't given detailed notes on the guide mock yet; expect a pass on it when implementation starts.
8. **Side ruler**: keep as decoration, make it a position indicator, or drop.
9. **Subline wording** (wom-bm9) and sign-off line: still open, not blocking.
10. **Implement** (wom-b5o.4): custom.css from `site.css` tokens, homepage, guide template, panels and cards as reusable HTML.

## Structure

Unchanged. Mostly flat, SEO slugs: guides `markdown-<x>`, per-app `markdown-in-<x>`, tutorials in `learn/`, reference in `kb/`, philosophy at `why` and `manifesto`. See AGENTS.md.

## Logo **[open; nothing recommended]**

Rufus on draft 3: the brush `#` is "really interesting", might work at the top of the page, but looks a bit unclean beside text. It's the live candidate to develop. The tai chi figure is the other. The logo is explored in its own session (wom-b5o.3), now that the page direction is decided. Earlier brief options for the record: A brush hash (`docs/brand/hash-brush.svg`, generated by `hash-brush-gen.py`); B four glyph tiles (common, loses markdown at 16px); C the ink tai chi figure in an orange sun (warm, says nothing about markdown; better as the site's character).

## Mark and animation

Decided 2026-08-08: the mark is the syntax figure, written in Markdown punctuation. Still true. What changes: the Gemini video on the homepage is replaced by a hand-built SVG/JS animation again, with the push-hands beat **[open, recommended]**: the figure settles, a plain block slides in from the right, the figure yields and presses, the block drifts off the edge and dissolves into `#` `*` `>`. One breath, six to ten seconds, loops. Lessons from the nine previous versions are in [[2026-08-02-markdown-tai-chi-design]] and still apply: brush ribbons not lines, derived joints, no step cycle, measure proportions standing.

The small mark is the static ink figure in a seal. It must read at 32 px; the syntax figure needs 80 px, which is why there are two.

## Explainer video

Separate track from the mark. Sixty to ninety seconds, SVG-built, telling the basic story: a file, the same file in five apps, the same file published, the same file in fifty years. Sits on the homepage below the fold or on `why`. Storyboard first, build second.

## Model split

Fable for the brand brief, the visual direction choice, the mark animation and the explainer storyboard. Opus for site CSS once a direction is chosen, the asset rendering pipeline, OG cards and the explainer build from a finished storyboard.
