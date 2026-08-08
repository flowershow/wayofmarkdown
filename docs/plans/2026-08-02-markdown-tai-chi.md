# Markdown Tai Chi Prototype Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a standalone review prototype that compares three treatments of a Markdown-character figure forming, performing a slow tai chi movement and releasing.

**Architecture:** A single excluded HTML file contains an inline SVG stage, embedded CSS and dependency-free JavaScript. Shared body keyframes drive all three visual treatments; review controls change rendering without changing the underlying motion.

**Tech Stack:** HTML, CSS, inline SVG, vanilla JavaScript, Node-based static assertions, existing repository lint scripts

---

### Task 1: Add structural prototype checks

**Files:**
- Create: `scripts/check-tai-chi.mjs`
- Test: `tai-chi.html` (live at `/tai-chi.html`)

**Step 1:** Write a Node script which reads the prototype and asserts that it contains an SVG stage, three named visual modes, pause/replay controls, a reduced-motion media query and no remote scripts or stylesheets.

**Step 2:** Run `node scripts/check-tai-chi.mjs` and verify it fails because the prototype does not exist.

**Step 3:** Create the minimal HTML shell with the required semantic and review-control elements.

**Step 4:** Run `node scripts/check-tai-chi.mjs` and verify it passes.

### Task 2: Build the shared figure and animation loop

**Files:**
- Modify: `tai-chi.html` (live at `/tai-chi.html`)
- Modify: `scripts/check-tai-chi.mjs`

**Step 1:** Extend the assertions to require source, compose, flow and release phase data plus a static fallback pose.

**Step 2:** Run the check and verify the new assertions fail.

**Step 3:** Add fixed body keyframes, eased interpolation, glyph assignment along body segments and the eight-second loop. Render a composed pose before JavaScript starts.

**Step 4:** Run the structural check and verify it passes.

### Task 3: Add and tune three visual treatments

**Files:**
- Modify: `tai-chi.html` (live at `/tai-chi.html`)
- Modify: `scripts/check-tai-chi.mjs`

**Step 1:** Extend the check to require `glyph-body`, `syntax-ribbons` and `source-constellation` renderers.

**Step 2:** Run it and verify it fails.

**Step 3:** Implement all three treatments over the shared motion data, with Glyph body selected by default and controls for switching live.

**Step 4:** Run the check and verify it passes.

### Task 4: Accessibility, responsive behaviour and visual review

**Files:**
- Modify: `tai-chi.html` (live at `/tai-chi.html`)
- Modify: `scripts/check-tai-chi.mjs`

**Step 1:** Add checks for a static reduced-motion state, keyboard-operable controls, responsive SVG sizing and light/dark colour tokens.

**Step 2:** Run the check and verify any missing requirements fail.

**Step 3:** Complete those behaviours, open the file at desktop and mobile sizes, and tune timing, spacing and glyph density against the design review criteria.

**Step 4:** Run `node scripts/check-tai-chi.mjs`, `python3 scripts/voice-lint.py` and `python3 scripts/link-check.py`; all must pass.

### Task 5: Record and share the prototype

**Files:**
- Modify: `docs/plans/v0.2.md`

**Step 1:** Add a narrative log entry linking the design, plan and prototype.

**Step 2:** Commit the design documents separately from the prototype implementation using `docs:` and `home:` prefixes.

**Step 3:** Push `main` and add a concise work-session comment to review log issue #57, with issue #71 linked.

---

## Version 2 revision: Wudang silhouette and named movement

### Task 6: Replace the visual acceptance checks

**Files:**
- Modify: `scripts/check-tai-chi.mjs`
- Test: `tai-chi.html` (live at `/tai-chi.html`)

**Step 1:** Replace the three-treatment assertions with checks for the chosen Wudang silhouette, Parting the Wild Horse's Mane keyframes, broad robe/sleeve/coat-tail regions, one-time composition and a continuous movement loop.

**Step 2:** Run `node scripts/check-tai-chi.mjs` and verify it fails against version 1.

### Task 7: Build the full human silhouette

**Files:**
- Modify: `tai-chi.html` (live at `/tai-chi.html`)

**Step 1:** Replace the sparse segment renderer with dense token fields for the robe, sleeves, legs, head and topknot. Keep the skeleton available only as a review overlay.

**Step 2:** Give sleeves and coat tails their own delayed keyframe interpolation so fabric follows the body rather than moving as rigid limbs.

**Step 3:** Render a deliberate static fallback using the settled silhouette.

**Step 4:** Run the structural check and fix any missing version 2 requirements.

### Task 8: Choreograph Parting the Wild Horse's Mane

**Files:**
- Modify: `tai-chi.html` (live at `/tai-chi.html`)

**Step 1:** Add cradle, sink, step, part and settle poses viewed near-side-on and facing right.

**Step 2:** Interpolate the weight transfer before the arm opening; keep the torso upright and the head quiet.

**Step 3:** Compose the figure once on load, then loop the completed movement without releasing it back into particles.

### Task 9: Review and commit version 2 locally

**Files:**
- Modify: `tai-chi.html` (live at `/tai-chi.html`)
- Modify: `scripts/check-tai-chi.mjs`

**Step 1:** Check the moving figure at desktop and 390px mobile sizes, including pause/replay, skeleton overlay and reduced-motion behaviour.

**Step 2:** Run the prototype check, voice lint, link check and `git diff --check`.

**Step 3:** Commit the HTML revision and its checks as a distinct local version. Do not integrate the homepage or push during the review phase.

---

## Version 4 revision: brush strokes, derived joints, real steps

Done on 2026-08-02 after Rufus judged version 3 to have no elegance or flow. Tasks 10 to 13 are complete; task 14 is the open one.

### Task 10: Replace the drawing model — done

Uniform-width polylines through the joint list gave a stick figure by construction. Added `brush()`, which outlines a variable-width ribbon along a Catmull-Rom spline, and `ik()`, which derives elbows and knees from two-bone inverse kinematics. The figure is now nine tapered strokes, with the spine running unbroken from the sacrum over the crown. The turbulence filters are gone; the taper does the work they were faking.

### Task 11: Replace the sliding travel with real steps — done

The figure performs one step of Brush Knee and Push and repeats it, advancing one stride per step and crossing the strip in twenty-two steps. Movement is authored as cyclic Catmull-Rom tracks — pelvis glide, foot swing, foot lift and angle, hip height, lean, and one arc per hand — so velocity is continuous across the step boundary. The pelvis withdraws about five units before it commits forward, which is the weight transfer earlier versions had no equivalent of.

### Task 12: Make the movement verifiable — done

Rewrote `scripts/check-tai-chi.mjs`. The prototype's movement code is fenced by `geometry:start` / `geometry:end` markers and is DOM-free, so the check imports it directly and asserts bone lengths hold, hands stay attached, feet stay on the floor, the head stays quiet, and every joint plus the hand velocity is continuous across the step boundary. Each assertion was verified by deliberately breaking the prototype and confirming it failed.

### Task 13: Review affordances and responsive framing — done

Added a preview at true hero size next to the enlarged one, a pose-by-pose contact sheet of the phrase, a scrub bar, a speed control and `#t=` deep links. The stage height is fixed and the viewBox width derived from it, so a narrow screen sees less of the strip rather than a smaller figure — the camera travels with the figure. Baked a still bow stance into the markup as the no-JS fallback.

### Task 14: Rufus's call on tempo, alternation and syntax — open

Two questions the study cannot settle on its own. The crossing takes about forty seconds at a natural tai chi tempo; calm, but long for a hero loop. And the phrase repeats on one side instead of alternating left and right as the form proper does — cheap to add, but it doubles the pose data and is barely visible in strict profile. Both are worth a look before any Markdown syntax work begins.

---

## Version 5 revision: one movement, in place

Done on 2026-08-08 on Rufus's call: no crossing, one movement, something closer to push hands.

### Task 15: Replace the movement — done

The travelling Brush Knee and Push phrase is gone. In its place is An — press and push — performed in a fixed bow stance: weight settles back, both palms draw down and in, weight rolls forward, both palms press out together. The feet are constants; all visible motion is the weight rolling between them. This also removed the step cycle, which was what kept the earlier versions reading as walking.

### Task 16: Rework the composition — done

The 1000-unit strip existed to give the figure room to travel, so it went with the travel. The mark is now roughly 200 by 118 units, previewed at 56, 80 and 104 pixels and shown in place beside a headline. The dissolving pose-ghosts are gone: with the figure staying put they would have piled up on each other.

### Task 17: Make the double push read — done

Two fixes. The palms are offset, the far one lower, shorter and lighter, because in strict profile two hands at the same height read as one thick hand. And the far shoulder is dropped and brought forward so the far arm clears the torso instead of vanishing into it and re-emerging as a stray forearm.

### Task 18: Retarget the checks — done

`scripts/check-tai-chi.mjs` lost its stride and step-boundary assertions and gained ones that fit a gesture in place: the feet must not move at all, the palms must stay in the same band, the leading palm must finish well in front of the shoulder and travel a real distance, and the loop must be seamless in position and velocity. Stride and trail machinery are now asserted *absent* so they cannot creep back. Each assertion was verified by breaking the prototype, with a no-op control to confirm they do not simply fail on everything.

### Task 19: Rufus's call on looping and syntax — open

The gesture currently loops, on the reading that "no repetition" meant not repeating it across the page, and that a breath in and out naturally continues. If it should instead play once and rest in the settled push, that is a small change. Then: syntax.

---

## Version 6: the syntax figure

Done on 2026-08-08. The ink version is untouched and stays above it on the page.

### Task 20: One body, two renderings — done

Split `figure()` out to return the stroke centrelines. `strokes()` outlines them as brush ribbons; the new glyph layout lays Markdown punctuation along them. Neither rendering owns the body, so they cannot diverge.

### Task 21: Lay the characters — done

Characters sit at fixed fractions of arc length so each keeps its identity and its place across the movement. Size follows brush width; spacing steps along the arc by each character's own size, which is what keeps the thick hips from blotting and the fine face line from falling apart. Ninety-four characters over fifteen marks.

### Task 22: The wind — done

Arrive from off-stage left with drift, settle, press, then scatter along the push's own line, accelerating and fading. Leading hand first, rear foot last, in both directions. The scatter vector is the leading hand's path from gathered to settled with the vertical damped to .45, because the hand rises more steeply than the push does.

### Task 23: Checks — done

Dropped the assertion that banned `<text>`. Added: the character set must be Markdown punctuation, the count must stay in a legible band, the layout must stay finite and stable across the movement, and every character must sit near the body. Verified by breaking each one; the count bound needed the spacing floor removed as well before it would fire.

### Task 24: Open — which one, and where

Whether the mark should be the ink figure, the syntax figure, or the syntax figure resolving into ink. And then homepage integration, which is still untouched.

---

## Version 8: head, and the decision

Done on 2026-08-08.

### Task 25: The skull — done

The head was the weakest part of the syntax figure: the skull got few characters and read as a scatter. Three changes. The topknot became a chain of points down a tail with progressive lag, each link trailing a little more than the one above, so the hair moves through itself as the body moves — a small, controllable version of exactly what the robe hem needed and never got. A single `*` sits under the brow as an eye, carried by a new `single` flag on a stroke that always yields exactly one character. And the face and hair take a `density` factor so they get more characters than their width alone would earn.

### Task 26: The mark is the syntax figure — decided

Rufus's call. It reads as Markdown, which is the point of the site.

### Task 27: Homepage integration — open

The only remaining piece, and out of scope from the beginning. Everything else on this plan is closed.

---

## Version 10: homepage integration

Done on 2026-08-08. This closes the plan.

### Task 27: The hero — done

The Flowershow hero is generated from frontmatter and has nowhere to put a mark, so `index.md` sets `showHero: false` and rebuilds the hero in content: a `.wom-hero` block with the mark, an `h1`, the lede, and the two CTAs, styled from `custom.css`.

The animation is embedded as an iframe to `/hero-mark.html`. Markdown reliably passes iframes through — the videos page proves it — but there is no evidence it passes `<script>`, and the homepage is the wrong place to find out. The iframe also isolates the animation from the page.

The mark uses the brand green rather than ink because an iframe cannot see the parent's `data-theme`, so it cannot follow the site's light and dark modes. Green reads on both. `hero-mark.html` also gained the same `#t=` seek as the study, without which a headless browser cannot capture it at all — virtual time does not advance requestAnimationFrame.

### Task 28: The navbar mark — done

The navbar was still wearing Flowershow's default logo, served from their asset host. Replaced with `assets/brand/mark.svg`: the ink figure in the settled push, brand green, tightly cropped, set via `logo` in `config.json`.

Static, not animated, and not a GIF. Motion in chrome is inescapable — it is on every page and cannot be scrolled past — and it contradicts a mark whose whole quality is slow and settled. The navbar renders at 32 pixels, well under the roughly 80 the syntax figure needs. So the identity is responsive: the animated syntax figure is the full mark at hero size, and a static ink silhouette is the small mark.

One consequence worth noting: the `h1` is now "The Way of Markdown" alone, with "Own the source. Compose with anything." demoted to a lede. The `title` tag still carries the full string, so search results are unchanged, but the on-page `h1` is shorter than it was.
