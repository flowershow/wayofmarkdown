---
title: "Brief: tai chi hero animation"
publish: false
---

# Tai chi hero animation: canonical brief

Status: current handoff brief as of 2026-08-02. Tracked in GitHub issue #71. Read this before the longer design history in `2026-08-02-markdown-tai-chi-design.md`.

## The idea in one sentence

Create a small, beautiful animation for The Way of Markdown hero: a graceful side-on figure moves through a sequence of tai chi gestures from left to right across the page, initially drawn as sparse flowing lines and later potentially formed from Markdown syntax.

## Why we are doing it

The Way of Markdown needs stronger and more memorable branding. The animation should become a visual signature for the site rather than generic decoration. The connection is that a handful of plain marks can compose into something expressive, just as Markdown does.

The homepage may eventually need broader work: moving it towards pure HTML and Tailwind, removing the sidebar and Giscus comments, and reconsidering the whole hero. That is a related but larger homepage task. Do not let it block the animation study or quietly fold it into this scope.

## Rufus's brief

I am imagining this ending up quite small, like 50 pixels high or 100 pixels. It is quite a small animation, and it flows left to right across the page. You really want the figure almost making a sequence of movements, going quite a way across the page, so the figures are not very high.

At some point it might assemble at the beginning out of different Markdown-related items: the hash mark used for headings, for example, or basically points and quite simple things. But maybe we do not start by doing this with punctuation symbols. Start by doing it with beautiful curving lines. Get the outline of a person right first.

The movement is completely side-on. Think of the pictures of Muybridge taking a picture of the horse. There is no three-dimensionality: we are seeing the flow of the movement across the page.

It should be graceful, like a Zen sketch. We are not putting in the detail of someone. It is not a full outline of them; it is the essential movement of the arms, the flow of the back into the head and the shape of the body. It is like a sketchbook of tai chi moves, with the whole sequence unfolding from left to right across an expanse of the page. <!-- voice-lint-ok: Rufus's original description -->

Later we can turn it into syntax, but first get that right.

Earlier poses should continuously dissolve behind the live figure, provided the effect is genuinely beautiful.

## Current creative direction

### Scale and composition

- A wide, shallow strip across much of the page.
- Approximately 50–100 pixels high in its eventual hero setting; the working SVG may use a larger equivalent viewbox.
- The figure travels through substantial horizontal space instead of performing in place.
- Empty space is part of the composition. This is not a card, illustration panel or large centred logo.

### Human form

- A beautiful human gesture is the first requirement.
- Strict side profile throughout. No three-quarter turn and no attempt to fake depth by separating near and far limbs.
- Use only the essential curves: arms, back into head, body weight and legs.
- The eye should complete the figure, as it does in a confident ink sketch.
- Avoid a detailed face, costume rendering, filled silhouette or outlined cartoon body.
- Avoid the visual language of a stick figure, loading icon, wireframe skeleton or particle person.

### Movement

- A beautiful tai chi movement is the second requirement, and it must be studied from a strong visual reference rather than invented as generic arm waving.
- The phrase should feel grounded, slow, balanced and sinuous.
- Weight settles before the hands arrive. The head remains quiet. Hands follow broad continuous arcs.
- The feet and hips must show transfer of weight, not a walk cycle or dance step.
- The figure progresses from left to right through several related poses, like a moving Muybridge study.
- Retain a small number of earlier poses at their original positions and dissolve them continuously. They should resemble fading ink or a sketchbook sequence, not speed lines or motion blur.
- The exact named tai chi phrase is not locked. *Parting the Wild Horse's Mane* has been explored, but visual grace and side-on legibility matter more than keeping that choice.

### Line and atmosphere

- Begin with plain curving lines. Do not solve the Markdown treatment yet.
- Aim for the economy and confidence of a Zen brush sketch.
- Lines can vary in weight and dryness, but effects must stay subordinate to the gesture.
- No glow, particle field, enso backdrop, robe texture or decorative scenery is needed to make the idea work.

### Markdown comes second

Once the human form and motion are genuinely good, explore translating the line into Markdown syntax:

- parts of the stroke could resolve into `#`, `_`, `>`, brackets, backticks or points;
- the first pose might assemble from those marks at the beginning;
- punctuation could become brush texture rather than filling a solid body;
- the person must still read first and the Markdown construction second.

Do not use syntax to disguise weak anatomy or movement.

## What has already been tried

### Version 1: centred glyph figure

Markdown characters assembled into an articulated figure which performed a slow movement and dissolved. It demonstrated that SVG glyphs could form and animate a body, but it read as a stick figure and generic particle effect. The square, centred composition was also wrong for the desired hero.

### Version 2: robed Wudang silhouette

A denser figure used a dark robe, broad sleeves, coat tails, a topknot and a slightly three-quarter view. It explored *Parting the Wild Horse's Mane*. The added costume and Markdown mass made the result heavier and more detailed without making it beautiful. The three-quarter view directly contradicted the later strict side-on direction. Treat this as a discarded exploration, not the brief.

### Version 3: travelling ink gesture

The prototype was rebuilt as a 1000 by 140 SVG strip with an unfilled line figure, left-to-right travel and fading pose snapshots. The composition was right and the drawing was not: uniform-width lines run through a joint list, which is a stick figure however the poses are tuned, and the figure slid across the strip without ever taking a step.

### Version 4: brush strokes and real steps

The current state. Same strip, rebuilt three ways: tapered brush strokes instead of lines, joints derived by two-bone IK instead of hand-placed, and one step of Brush Knee and Push repeated across the page instead of a single slide. See the version 4 section of the design note for what each change fixed. Open questions are the forty-second crossing and the phrase repeating on one side rather than alternating.

## How to work on it

- Keep the experiment in the standalone HTML prototype. Do not integrate it into the homepage yet.
- Commit local versions as the work develops so Rufus can compare directions.
- Do not push merely to review the local animation; pushing `main` deploys the site.
- Make a concrete visual choice and implement it rather than asking Rufus to choose among every small option.
- Use actual reference material for both the human gesture and the movement.
- Review at the intended small size. A figure that only works when enlarged has not solved the brief.

Current files:

- Prototype: `docs/prototypes/markdown-tai-chi.html`
- Structural check: `scripts/check-markdown-tai-chi.mjs`
- Design history: `docs/plans/2026-08-02-markdown-tai-chi-design.md`
- Implementation notes: `docs/plans/2026-08-02-markdown-tai-chi.md`

## Definition of success

The study is ready for a Markdown treatment when:

- the first glance reads as a graceful human figure;
- the figure remains clear and elegant at roughly 50–100 pixels high;
- every pose is convincingly side-on;
- the movement reads as tai chi rather than walking, dancing or waving;
- the sequence unfolds across the width of the page;
- fading poses clarify the movement without cluttering it;
- the line work is memorable with all labels, controls and explanatory copy hidden;
- watching several loops remains calm rather than irritating.

Only after those conditions are met should the work proceed to syntax experiments and homepage integration.
