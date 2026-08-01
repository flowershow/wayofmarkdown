---
title: "Design: Markdown tai chi hero animation"
publish: false
---

# Markdown tai chi hero animation

Status: approved for standalone prototyping on 2026-08-02. Tracked in GitHub issue #71.

## Purpose

Create a memorable visual signature for The Way of Markdown: plain Markdown syntax composing into something expressive and useful. The first prototype stays separate from the homepage. We will decide how to integrate it only after the motion and visual language work on their own.

## Core sequence

The animation is a centred, self-contained “living mark” with a roughly eight-second loop:

1. **Source** — Markdown characters and short tokens float in a loose field.
2. **Compose** — the fragments gather into a recognisable human figure.
3. **Flow** — the figure performs one slow, grounded tai chi movement.
4. **Release** — its form loosens back into source characters before the loop restarts.

The first read should be a person moving. The second read should be that the person is made from Markdown. This avoids a generic particle animation and keeps the project idea legible.

## Visual directions to compare

The standalone file should expose three treatments built from the same motion data:

### 1. Glyph body — recommended

Markdown characters sit along a simple articulated figure. Larger structural tokens such as `#`, `>`, `[]` and backticks define the torso and joints; lighter punctuation traces the limbs. This should be the clearest human form and the first version to polish.

### 2. Syntax ribbons

Short Markdown phrases follow curved paths through the torso and limbs. This treatment may feel more calligraphic and fluid, though it risks becoming harder to read at small sizes.

### 3. Source constellation

Individual symbols form a sparse point-cloud silhouette, with faint connecting strokes. This is the most abstract treatment and may work well as a quiet static mark, but is less likely to communicate Markdown immediately.

The directions are variations, not three separate animation systems. Shared timing and body motion make comparison cheap and keep the experiment focused.

## Composition

- Square stage that scales from roughly 280px to 560px.
- Transparent or softly tinted background so it can later sit above a hero title.
- A single green accent drawn from the current site, supported by neutral ink colours.
- Plenty of empty space around the figure. No particles behind hero text.
- No words, logo text or calls to action inside the animation itself.

## Motion character

The movement should feel balanced, deliberate and human: weight shifts before arms move; the head stays calm; hands trace broad arcs; nothing snaps or bounces. It is an evocation of tai chi rather than an instructional depiction of a named form.

The loop should pause briefly at the fully formed pose so the figure and Markdown construction can be understood. Formation and release should be quieter than the central movement.

## Prototype architecture

Create one standalone file at `docs/prototypes/markdown-tai-chi.html` containing its HTML, CSS and JavaScript. Use inline SVG for crisp, responsive typography and paths. A small JavaScript animation loop interpolates a fixed set of body keyframes and maps glyphs to body segments. No framework or external dependency is needed.

The file should include simple development controls for switching visual treatments, pausing, replaying and showing the construction skeleton. These controls are for review and will not be part of any eventual homepage version.

## Accessibility and resilience

- Under `prefers-reduced-motion: reduce`, show the strongest composed pose without automatic movement.
- Treat the visual as decorative in a future hero; it must not carry information unavailable in text.
- Keep contrast readable in light and dark colour schemes.
- If JavaScript fails, the inline SVG should still display a composed static figure.

## Review criteria

The prototype succeeds when:

- the figure reads as a person within one second;
- the Markdown construction becomes apparent without explanation;
- the movement feels calm and grounded rather than like a loading spinner;
- at least one treatment remains clear at mobile size;
- the loop does not become irritating after several repetitions;
- reduced-motion mode produces a deliberate static mark;
- the result feels specific enough to become part of the Way of Markdown identity.

## Out of scope

- Editing `index.md` or replacing the Flowershow hero
- Removing homepage comments or changing page chrome
- Rebuilding the homepage in HTML/Tailwind
- Choosing a permanent logo
- Adding an animation library before the motion direction is validated

