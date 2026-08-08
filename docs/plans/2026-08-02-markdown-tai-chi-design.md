---
title: "Design: Markdown tai chi hero animation"
publish: false
---

# Markdown tai chi hero animation

Status: approved for standalone prototyping on 2026-08-02. Tracked in GitHub issue #71.

Canonical handoff brief: [Tai chi hero animation brief](2026-08-02-markdown-tai-chi-brief.md). This file records the design history and superseded experiments.

## Where it landed

**The mark is the syntax figure** — the one written in Markdown punctuation. Decided 2026-08-08. It reads as Markdown, which is the whole point of the site, and the assembly is the idea rather than decoration on top of it.

It is on the homepage, in the navbar and in a press kit. The effort is finished; what follows is a map of where everything is, so nobody has to re-derive it.

### What is where

| File | What it is |
|---|---|
| `hero-mark.html` | The animated mark. Source of truth for every rendered asset. Embedded by the homepage in an iframe; `contentHide`. Supports `#t=` to freeze a moment and `#c=` to override the colour. |
| `tai-chi.html` | The full study: ink figure and syntax figure side by side, with contact sheets and review controls. Published, unlisted, noindexed. |
| `tai-chi-robe.html` | The robed figure, parked. A frozen snapshot that does not track changes to the study. It carries its own note on what is unsolved. |
| `scripts/check-tai-chi.mjs` | Imports the study's own movement code and asserts anatomy, proportions, planted feet, palm travel, loop continuity, the character set and the hair. Also lightly checks the parked robe file. |
| `index.md` + `custom.css` | The homepage hero. `showHero: false` plus a `.wom-hero` block; the `.wom-*` and `:has(.wom-hero)` rules in `custom.css` do the rest. |
| `assets/brand/` | Rendered assets: two GIFs, three SVGs, nine PNGs. All generated, none hand-drawn. |
| `press.md` | The public press kit at `/press`, laying the assets out with guidance. |
| `config.json` | `logo` points at `assets/brand/mark.svg` for the navbar. `contentHide` keeps the HTML studies out of listings. |

### Regenerating the brand assets

Everything in `assets/brand/` is a render of `hero-mark.html`. Nothing is drawn by hand, so a change to the figure means re-running this rather than editing files.

Frames come from headless Chrome, because virtual time does not advance `requestAnimationFrame` — hence the `#t=` seek. The GIF is assembled by ffmpeg through a generated palette; the default palette is much worse.

```bash
# 48 frames of the animation at 600x300, green on white
for i in $(seq 0 47); do
  t=$(python3 -c "print(f'{$i/48:.5f}')")
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
    --hide-scrollbars --window-size=600,300 --default-background-color=FFFFFFFF \
    --virtual-time-budget=1100 --screenshot="frames/g_$(printf %03d $i).png" \
    "file://$PWD/hero-mark.html#t=$t&c=16a34a"
done
ffmpeg -y -framerate 11 -i frames/g_%03d.png -vf "palettegen=max_colors=48:stats_mode=diff" pal.png
ffmpeg -y -framerate 11 -i frames/g_%03d.png -i pal.png \
  -lavfi "paletteuse=dither=bayer:bayer_scale=3" -loop 0 assets/brand/tai-chi-mark.gif
```

Use `c=111111` for the black GIF. The still PNGs are the same idea: an HTML page holding `<img src="mark-*.svg">` at a fixed height, screenshotted with `--default-background-color=00000000` for transparency. The SVG colour variants are a string replacement of the `fill` on `assets/brand/mark.svg`.

Two things that bit and will bite again. The canvas has to be taller than the mark's own aspect ratio, or the figure's feet are clipped at the bottom edge — check an actual frame, do not trust the export. And GIF only has one-bit transparency, so the animation is rendered on white; anyone needing transparency wants the SVG or the PNGs.

### The movement

An, the press-and-push from Grasp Sparrow's Tail, performed in place: the weight settles back, both palms draw down and in, then the weight rolls forward and the hands press out together. In the syntax version the characters blow in from the left, hold the figure long enough for it to make the move, and are thrown off along the push's own line.

### Known limitation

The syntax mark wants about 80 pixels of height to read; below that the characters stop being characters. The ink figure still holds at 56, which is why the navbar and small sizes use the still ink mark rather than the syntax one, and why `press.md` says so out loud.

### Still open

Nothing on this plan. If the robe is ever picked up again, `/tai-chi-robe.html` says what it needs.

## Version 9: proportions

Rufus asked whether the head was the right size and thought the legs looked long. Measuring rather than eyeballing settled it, and both instincts were right.

The bow stance hides proportion, because the legs are bent and the hip is sunk. Measured standing — leg bone plus foot, against hip-to-crown — the figure was **8.55 heads tall with legs at 54% of its height**. A real adult is about 7.5 heads with legs at 47 to 50%; 8 heads is the idealised figure-drawing convention. It had drifted into fashion-illustration territory without anyone noticing, because every version had been judged in the stance.

Corrected to 7.36 heads and 49.8%: the head scaled 11% about the base of the neck, the leg bones shortened from 27 to 23.5 each, the stance narrowed to suit, and the hip lowered so the feet stay planted. The arms were already right at 37.5% but had to come down slightly to stay right against the shorter body, and the leading hand's reach came in with them or the IK would have clamped and detached the hand. Landing a little under 7.5 is deliberate: a marginally large head reads better at 56 to 80 pixels, which is where this has to work.

The check now asserts all three ratios, so a later pose edit cannot quietly drift back. The lesson is the general one: a figure in a deep stance will hide its own proportions from you, and the only way to see them is to measure the standing equivalent.

## What this cost us, and what was worth knowing

Eight versions. The lessons that would transfer to the next thing like this:

**A stick figure is a property of the renderer, not the pose.** Versions 1 to 3 were tuned and re-tuned while every stroke was a uniform-width line run through the joint list. No amount of pose work can make that look like ink. Variable-width brush ribbons were the single biggest change in the whole effort, and they were available from the start.

**Derive joints, do not place them.** Hand-authored joints drift in length the moment you interpolate between poses. Two-bone IK fixed that for free and, more usefully, moved the authoring to where the movement actually lives — the arc each hand traces.

**Any step cycle reads as walking**, however slowly it is played. Removing travel altogether is what finally made the thing read as tai chi. This is also why the answer to "could it step?" stayed no.

**In strict profile, two of anything at the same height read as one thing.** The two palms needed offsetting, and the far shoulder had to be dropped and brought forward before the far arm stopped disappearing into the torso and re-emerging as a stray forearm.

**One small mark can carry the whole read.** The palm cocked back at the wrist is most of what says tai chi rather than somebody reaching for a door handle.

**Closed outlines overshoot at reversals.** Both the sleeves and the robe body were first drawn as single closed paths and both came out as scribbles, because the path has to turn back on itself at the cuff and the hem. Splitting each into open edges fixed it completely, first time.

**Even density beats even spacing.** Spacing the characters by each stroke's average width blotted the thick hips and thinned the fine face line in the same figure. Stepping along the arc by each character's own size fixed it.

**Outlines do not survive translation into sparse characters.** The syntax figure works because its strokes *are* the body. The robe's strokes are the *boundary* of a body, and an outline made of gaps is mostly gaps. That is why the syntax robe was tried and dropped in ten minutes rather than argued about.

**A syntax treatment is forgiving, and that is a trap.** It hid the robe's rigid hem and disconnected leg almost entirely. Building it would have banked a foundation we already knew was wrong.

**Make the motion assertable.** Fencing the pure geometry off behind markers so the check script can import it caught limbs stretching, hands detaching and loop seams that eyeballing a slow loop never would. Every assertion has to be verified by deliberately breaking the prototype: two of the first break-tests turned out to be no-ops that passed, which would have left the checks looking green and meaning nothing.

**Integrating into a themed site is a fight with someone else's CSS, and guessing at it wastes time.** Three things broke on the live homepage that no local preview could show, because all three were collisions with theme rules: the hero `h1` was hidden by `.rendered-mdx h1:first-child { display: none }`, the primary button's label was invisible because content links take the accent colour and that is the same green as the button, and the hero was squeezed into a third of the page by 16rem of padding reserved for a sidebar the site does not use. What finally worked was saving the live page, pointing it at the real stylesheets locally, and reading computed styles — `display`, `color`, `background` — instead of reasoning about specificity from the outside.

**Measure proportions standing, not in the pose.** A deep stance hides them. Nine versions in, the figure turned out to be 8.55 heads tall with legs at 54% of height, and nobody had spotted it because it was only ever judged in a bow stance.

**Being able to look at it mattered more than anything else.** Rendering each iteration with headless Chrome, and adding `#t=` deep links so any moment could be captured, is what turned this from guesswork into work.

## Rufus's movement brief, lightly tidied

I am imagining this ending up quite small, like 50 pixels high or 100 pixels. It is quite a small animation, and it flows left to right across the page. You really want the figure almost making a sequence of movements, going quite a way across the page, so the figures are not very high.

At some point it might assemble at the beginning out of different Markdown-related items: the hash mark used for headings, for example, or basically points and quite simple things. But maybe we do not start by doing this with punctuation symbols. Start by doing it with beautiful curving lines. Get the outline of a person right first.

The movement is completely side-on. Think of the pictures of Muybridge taking a picture of the horse. There is no three-dimensionality: we are seeing the flow of the movement across the page.

It should be graceful, like a Zen sketch. We are not putting in the detail of someone. It is not a full outline of them; it is the essential movement of the arms, the flow of the back into the head and the shape of the body. It is like a sketchbook of tai chi moves, with the whole sequence unfolding from left to right across an expanse of the page. <!-- voice-lint-ok: Rufus's original description -->

Later we can turn it into syntax, but first get that right.

## Version 8: the robe parked, the dissolution eased

Rufus's verdict on the robe: the rear leg disconnects from it, and there is no sense of the cloth moving. Both true, and both traceable to how it was built.

The hem is offset by a single lag taken from a pose sampled slightly earlier, so the whole skirt slides as one rigid shape rather than the cloth trailing through itself. Real flow needs progressive lag along the hem — the back trailing further than the front — and ideally a short settling chain rather than a fixed offset. The rear leg disconnects because the robe is a flat outline with no knowledge of a leg behind it; the hem would need to drape around the rear leg and be pushed by it. Neither is unreachable, but together they are a proper piece of work.

Parked at `tai-chi-robe.html` rather than deleted. A prototype you can still look at on a phone is much more likely to be picked up again than one buried in a commit, and the file carries its own note on exactly what is unsolved. It is a frozen snapshot and will not follow later changes to the live study; that is stated in the file so nobody is misled by it later.

The syntax dissolution was also slightly too quick. The scatter window is longer, the fade curve is less front-loaded, and the press now finishes a little earlier so there is a hold at full extension before the wind takes the characters.

## Version 7: the robe, and a tighter wind

Three changes on Rufus's notes.

**The wind was overdone at both ends.** The characters were thrown 80 to 250 units to the right, which read as a stream crossing the frame rather than a figure coming apart. They now travel a third of that and the fade outruns the travel: it disintegrates a short way and then goes. Arrival was pulled in from off-stage too — from that far out the characters read as a separate flock arriving rather than as the figure gathering itself.

**The arrival now flows into the movement.** The press starts at .17 while the last characters are still landing, so the body is already moving as they arrive and their targets are moving with it. Previously it assembled, paused, and then moved.

**Stepping: no.** Rufus asked whether a step would add flow. In An and in fixed-step push hands there is no step — the feet stay planted and the power is in the weight transfer. Moving-step push hands exists, but version 4 established that a step *cycle* reads as walking however slowly it plays, and removing it is what made this read as tai chi. Instead the feet now articulate under the weight: the front toe lifts as the weight leaves it and the rear foot rolls, heel lifting and pressing back down through the push.

**The robe.** A long robe over the same body, added below the bare figure rather than replacing it. It is drawn as outlines in the same brush language — a filled silhouette is what made the version 2 study heavy — and the hem hides the legs, which is where the bare figure is weakest and where the walking risk lived. The hem and cuffs are placed from a pose sampled 5.5% of a cycle earlier, so the cloth trails the weight instead of moving with it. That lag is the flow a step would have been trying to buy.

Two construction notes worth keeping. Both the sleeves and the robe body were first drawn as single closed outlines, and both came out as scribbles: a closed path has to reverse at the cuff and at the hem, and the spline overshoots the reversal badly. Splitting each into open edges — sleeve top, under and cuff; robe front, hem and back — fixed it completely. And the hem had to be widened well past the hips: over a bow stance a narrow hem leaves the feet stranded outside it, looking detached from the figure.

The head also gained a small bound topknot. At 56 pixels the bare skull read as a smudge; the knot gives it a silhouette to be recognised by.

Still open: whether the mark is the bare figure, the robed figure, or either of them in syntax; and the syntax version of the robe, which Rufus deferred.

## Version 6: the figure written in Markdown

The syntax version, added below the ink one rather than replacing it, so the two can be compared.

Both figures are drawn from the same body. `figure()` returns the stroke centrelines; the ink version outlines them as tapered brush strokes and the syntax version lays characters along them. The syntax figure cannot drift away from the ink one, because there is nothing for it to drift from.

Characters sit at fixed fractions of each stroke's arc length, so a given character keeps its identity and its place on the body for the whole movement rather than reshuffling every frame. Size follows the brush width, which carries the taper across into type: heavy structural marks — `#`, `>`, `*`, `+` — through the hips and thighs, fine punctuation out at the hands and face. Spacing steps along the arc by each character's own size. Keying it to the stroke average instead blotted the thick hips and thinned out the fine face line in the same figure; walking by local size gives even density everywhere. Ninety-four characters, spread across all fifteen marks in the set.

The cycle is the one Rufus described. The characters blow in from off-stage left, drifting, and settle into the gathered pose. The figure presses both palms out. Then the push throws them off along its own line, accelerating and fanning as they go, and they fade. The leading hand goes first and the rear foot last — both arriving and leaving — so the figure fills and empties in the direction of the movement rather than all at once.

The scatter direction comes from the leading hand's own path from gathered to settled, with the vertical component damped to just under half. Taken raw it threw the characters off at a noticeably steeper slope than the movement itself, because the hand rises more than the push does.

This also answers the question left open in version 5. The movement now plays once per cycle, between the arrival and the scattering, so it no longer needs to loop as a breath.

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
