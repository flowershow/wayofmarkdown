---
title: "Design: Markdown tai chi hero animation"
publish: false
---

# Markdown tai chi hero animation

Status: approved for standalone prototyping on 2026-08-02. Tracked in GitHub issue #71.

Canonical handoff brief: [Tai chi hero animation brief](2026-08-02-markdown-tai-chi-brief.md). This file records the design history and superseded experiments.

## Rufus's movement brief, lightly tidied

I am imagining this ending up quite small, like 50 pixels high or 100 pixels. It is quite a small animation, and it flows left to right across the page. You really want the figure almost making a sequence of movements, going quite a way across the page, so the figures are not very high.

At some point it might assemble at the beginning out of different Markdown-related items: the hash mark used for headings, for example, or basically points and quite simple things. But maybe we do not start by doing this with punctuation symbols. Start by doing it with beautiful curving lines. Get the outline of a person right first.

The movement is completely side-on. Think of the pictures of Muybridge taking a picture of the horse. There is no three-dimensionality: we are seeing the flow of the movement across the page.

It should be graceful, like a Zen sketch. We are not putting in the detail of someone. It is not a full outline of them; it is the essential movement of the arms, the flow of the back into the head and the shape of the body. It is like a sketchbook of tai chi moves, with the whole sequence unfolding from left to right across an expanse of the page. <!-- voice-lint-ok: Rufus's original description -->

Later we can turn it into syntax, but first get that right.

## Version 5 decision: one movement, in place

Rufus's call after version 4: drop the crossing entirely. No travel, no sequence, no repetition across the page. One movement, and something closer to push hands — a figure pressing both palms out in front of it.

The movement is **An**, the press-and-push from Grasp Sparrow's Tail. The weight settles back onto the rear leg, both palms draw down and in toward the waist, then the weight rolls forward into the front leg and both hands press out together at chest height. The feet never move. Everything visible is the weight rolling back and forward between them.

This turned out to fix a problem version 4 could not solve. The travelling version had a step cycle in it, and a step cycle read as walking however slowly it was played. Removing travel removes the walk, and what is left is unmistakably a tai chi gesture.

Composition changes with it. The wide 1000-unit strip existed to give the figure somewhere to travel; with no travel it was mostly empty page. The mark is now a compact frame of roughly 200 by 118 units, sized to run at 56 to 104 pixels high, which can sit beside a headline rather than stretching under one. The dissolving pose-ghosts are gone too: with the figure staying put they would have piled on top of each other.

Two drawing decisions carry the double push. The palms are offset — the far one lower, shorter and lighter — because in strict profile two hands at the same height read as one thick hand. And the far shoulder is dropped and brought forward so the far arm clears the torso and reads for its whole length instead of vanishing into the body and re-emerging as a stray forearm.

The gesture loops rather than playing once. "One movement, no repetition" is about not repeating it across the page; the movement itself is a breath in and out, and it is natural for it to keep breathing. There are holds at each end so it settles rather than cycling like a machine. If Rufus wants it to play once and rest, that is a small change.

## Version 4 decision: brush strokes, derived joints, real steps

Version 3 had the right composition and the wrong drawing. Rufus's verdict was that it had no elegance, beauty or flow. Three specific causes, each fixed:

**It was a stick figure by construction.** Every stroke was a uniform-width line run through the joint list. A body drawn that way cannot look like ink no matter how the poses are tuned. The figure is now built from tapered brush strokes: each limb is the filled outline of a variable-width ribbon, thick through the hips and thighs and drawn out to nothing at the extremities. One unbroken stroke runs from the base of the spine, up the back, around the skull and over the crown — the "flow of the back into the head" from the brief — and a second fine stroke closes the face back to the throat.

**The poses were hand-placed joint by joint**, so limbs changed length as the animation interpolated between them. Joints are now derived by two-bone IK from a small number of authored targets: the hand arcs, the pelvis glide and the stepping foot. Bones keep their length automatically, and the movement is authored where it belongs — in the path each hand traces.

**The figure never took a step.** It slid 850 units across the strip in a single phrase. It now performs one step of Brush Knee and Push and repeats it, advancing one stride each time, crossing the strip in twenty-two steps of about two seconds. The pelvis withdraws slightly before it commits, which is the weight transfer the earlier versions were missing entirely. Every couple of steps the settled stance is left behind as an ink ghost that dries out over eleven seconds.

Two smaller decisions carry more weight than their size suggests. The hands are kept in separate bands of the body — upper hand at shoulder height, lower hand at the waist — because in strict profile two hands at the same height read as a knot rather than a gesture. And each arm stroke runs on past the wrist into a short palm mark, cocked back. That one mark is most of what makes the figure read as tai chi rather than as somebody out walking.

The prototype also gained what the review needed: a preview at true hero size alongside the enlarged one, a pose-by-pose contact sheet of the phrase, a scrub bar, and `#t=` deep links so any moment can be captured or shared. On a screen too narrow to show the whole strip, the camera travels with the figure instead of shrinking it.

Still open, and worth Rufus's eye before any syntax work: the crossing takes about forty seconds at its natural tempo, which is calm but long for a hero loop; and the phrase repeats on the same side rather than alternating left and right as the form proper does.

## Version 3 decision: motion before figure, figure before syntax

Version 2 solved the wrong problem. Adding a robe, a filled silhouette and more Markdown texture made the figure heavier and more detailed, while the desired mark is small, horizontal and light. The next study returns to the movement itself.

Use a wide strip, approximately 1000 by 140 units, which can eventually sit at 50–100 pixels high in a homepage hero. A single figure travels from left to right in strict profile. Draw it as a Zen gesture study with only the essential curves: the line of the back and head, two arms, the grounded leg and the stepping leg. There is no costume, face, filled silhouette or three-quarter perspective.

The figure moves through one short tai chi phrase as it crosses the strip. Sample earlier poses at their actual positions and let three or four of them dissolve continuously behind the live figure. This borrows the legibility of [Muybridge's sequential motion studies](https://www.metmuseum.org/art/collection/search/700109) without leaving a static row of clones. The traces should feel like drying brush marks rather than speed lines.

Markdown syntax is deliberately postponed. First make the profile, weight transfer, hand arcs and timing beautiful as plain ink. Only after this works should we test replacing parts of the stroke with `#`, `_`, `>` and other source marks, or assembling the first pose from them.

Version 3 review criteria:

- the strip remains legible at 80–100 pixels high;
- every pose is unmistakably side-on;
- the head stays quiet while the hips travel and settle;
- arms describe long, unbroken arcs without looking like waving;
- feet show a grounded transfer of weight rather than a walk cycle;
- old poses dissolve gracefully and never crowd the live figure;
- the work still looks intentional with all text and controls hidden.

## Version 2 decision: form before syntax

The first prototype established that SVG characters can gather into and animate with an articulated figure. It did not establish the visual identity: the sparse construction reads as a stick figure, the body has no beautiful outer contour, and the movement is generic rather than recognisably tai chi.

Version 2 starts from two concrete references:

- **Human form and clothing**: the dark-robed Wudang master in [Master Huangshan's Wudang tai chi demonstration](https://www.youtube.com/watch?v=ziP_Yra06mo). Use the long coat, broad sleeves, low centre of gravity, restrained topknot and trailing hem as visual cues. Create an original figure from those cues rather than tracing a video frame.
- **Movement**: [Parting the Wild Horse's Mane](https://www.youtube.com/watch?v=ehOPk1lrPoU). It gives the short loop a clear sequence: cradle, sink, step, transfer weight, part the arms, settle.

Show the master facing right, almost side-on but turned about 10–15 degrees towards the viewer. A strict profile causes the arms and legs to overlap; the slight turn preserves the side-on weight transfer while keeping the whole gesture legible.

The body should become a full calligraphic silhouette rather than a decorated skeleton. Dense Markdown characters form the mass of the robe and limbs. Larger structural tokens define its outer contour. Sleeves and coat tails follow the hands and hips with a small delay, making the fabric part of the movement. The face stays minimal; posture, topknot and clothing carry the character.

Characters assemble into the figure once when the study loads. The completed figure then repeats the movement without dissolving between loops. This lets the viewer watch the tai chi rather than waiting through an effect on every cycle.

## Purpose

Create a memorable visual signature for The Way of Markdown: plain Markdown syntax composing into something expressive and useful. The first prototype stays separate from the homepage. We will decide how to integrate it only after the motion and visual language work on their own.

## Version 1 core sequence

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

## Version 2 movement keyframes

The movement is a simplified, side-on study of Parting the Wild Horse's Mane rather than an instructional reproduction:

1. **Cradle** — weight held over the rear leg; hands hold an implied ball near the torso.
2. **Sink** — hips settle before anything reaches; the front heel becomes light.
3. **Step** — the front foot glides forward while the hands cross and gather.
4. **Part** — weight travels into the front leg; the leading forearm rises and opens while the trailing hand settles towards the hip.
5. **Settle** — head quiet, shoulders dropped, sleeves and coat hem arriving just after the body.
6. **Return** — the figure breathes back through the same pathway to the cradle pose.

The torso should stay vertical and the head should travel only slightly. Most visible motion comes from the weight transfer, opening arms and delayed fabric. Use a ten- to twelve-second loop with short holds at cradle and settle.

## Version 2 rendering model

Keep the shared articulated skeleton, but use it only as hidden construction. Render broad body regions over it:

- a tapered robe body between shoulders and hem;
- two wide sleeves around the arm paths;
- overlapping coat tails which lag the hips;
- substantial trouser and lower-leg shapes;
- a small head profile and topknot.

Populate those regions with roughly 140–180 Markdown tokens. Torso tokens interpolate within the robe envelope; limb tokens sit in several rows across each segment instead of a single line. This preserves readable Markdown texture while creating enough mass for the person and clothing to read first.

## Prototype architecture

Create one standalone file at `tai-chi.html` (live at `/tai-chi.html`) containing its HTML, CSS and JavaScript. Use inline SVG for crisp, responsive typography and paths. A small JavaScript animation loop interpolates a fixed set of body keyframes and maps glyphs to body segments. No framework or external dependency is needed.

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
