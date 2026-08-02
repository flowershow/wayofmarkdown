# Markdown Tai Chi Prototype Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a standalone review prototype that compares three treatments of a Markdown-character figure forming, performing a slow tai chi movement and releasing.

**Architecture:** A single excluded HTML file contains an inline SVG stage, embedded CSS and dependency-free JavaScript. Shared body keyframes drive all three visual treatments; review controls change rendering without changing the underlying motion.

**Tech Stack:** HTML, CSS, inline SVG, vanilla JavaScript, Node-based static assertions, existing repository lint scripts

---

### Task 1: Add structural prototype checks

**Files:**
- Create: `scripts/check-markdown-tai-chi.mjs`
- Test: `docs/prototypes/markdown-tai-chi.html`

**Step 1:** Write a Node script which reads the prototype and asserts that it contains an SVG stage, three named visual modes, pause/replay controls, a reduced-motion media query and no remote scripts or stylesheets.

**Step 2:** Run `node scripts/check-markdown-tai-chi.mjs` and verify it fails because the prototype does not exist.

**Step 3:** Create the minimal HTML shell with the required semantic and review-control elements.

**Step 4:** Run `node scripts/check-markdown-tai-chi.mjs` and verify it passes.

### Task 2: Build the shared figure and animation loop

**Files:**
- Modify: `docs/prototypes/markdown-tai-chi.html`
- Modify: `scripts/check-markdown-tai-chi.mjs`

**Step 1:** Extend the assertions to require source, compose, flow and release phase data plus a static fallback pose.

**Step 2:** Run the check and verify the new assertions fail.

**Step 3:** Add fixed body keyframes, eased interpolation, glyph assignment along body segments and the eight-second loop. Render a composed pose before JavaScript starts.

**Step 4:** Run the structural check and verify it passes.

### Task 3: Add and tune three visual treatments

**Files:**
- Modify: `docs/prototypes/markdown-tai-chi.html`
- Modify: `scripts/check-markdown-tai-chi.mjs`

**Step 1:** Extend the check to require `glyph-body`, `syntax-ribbons` and `source-constellation` renderers.

**Step 2:** Run it and verify it fails.

**Step 3:** Implement all three treatments over the shared motion data, with Glyph body selected by default and controls for switching live.

**Step 4:** Run the check and verify it passes.

### Task 4: Accessibility, responsive behaviour and visual review

**Files:**
- Modify: `docs/prototypes/markdown-tai-chi.html`
- Modify: `scripts/check-markdown-tai-chi.mjs`

**Step 1:** Add checks for a static reduced-motion state, keyboard-operable controls, responsive SVG sizing and light/dark colour tokens.

**Step 2:** Run the check and verify any missing requirements fail.

**Step 3:** Complete those behaviours, open the file at desktop and mobile sizes, and tune timing, spacing and glyph density against the design review criteria.

**Step 4:** Run `node scripts/check-markdown-tai-chi.mjs`, `python3 scripts/voice-lint.py` and `python3 scripts/link-check.py`; all must pass.

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
- Modify: `scripts/check-markdown-tai-chi.mjs`
- Test: `docs/prototypes/markdown-tai-chi.html`

**Step 1:** Replace the three-treatment assertions with checks for the chosen Wudang silhouette, Parting the Wild Horse's Mane keyframes, broad robe/sleeve/coat-tail regions, one-time composition and a continuous movement loop.

**Step 2:** Run `node scripts/check-markdown-tai-chi.mjs` and verify it fails against version 1.

### Task 7: Build the full human silhouette

**Files:**
- Modify: `docs/prototypes/markdown-tai-chi.html`

**Step 1:** Replace the sparse segment renderer with dense token fields for the robe, sleeves, legs, head and topknot. Keep the skeleton available only as a review overlay.

**Step 2:** Give sleeves and coat tails their own delayed keyframe interpolation so fabric follows the body rather than moving as rigid limbs.

**Step 3:** Render a deliberate static fallback using the settled silhouette.

**Step 4:** Run the structural check and fix any missing version 2 requirements.

### Task 8: Choreograph Parting the Wild Horse's Mane

**Files:**
- Modify: `docs/prototypes/markdown-tai-chi.html`

**Step 1:** Add cradle, sink, step, part and settle poses viewed near-side-on and facing right.

**Step 2:** Interpolate the weight transfer before the arm opening; keep the torso upright and the head quiet.

**Step 3:** Compose the figure once on load, then loop the completed movement without releasing it back into particles.

### Task 9: Review and commit version 2 locally

**Files:**
- Modify: `docs/prototypes/markdown-tai-chi.html`
- Modify: `scripts/check-markdown-tai-chi.mjs`

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

Rewrote `scripts/check-markdown-tai-chi.mjs`. The prototype's movement code is fenced by `geometry:start` / `geometry:end` markers and is DOM-free, so the check imports it directly and asserts bone lengths hold, hands stay attached, feet stay on the floor, the head stays quiet, and every joint plus the hand velocity is continuous across the step boundary. Each assertion was verified by deliberately breaking the prototype and confirming it failed.

### Task 13: Review affordances and responsive framing — done

Added a preview at true hero size next to the enlarged one, a pose-by-pose contact sheet of the phrase, a scrub bar, a speed control and `#t=` deep links. The stage height is fixed and the viewBox width derived from it, so a narrow screen sees less of the strip rather than a smaller figure — the camera travels with the figure. Baked a still bow stance into the markup as the no-JS fallback.

### Task 14: Rufus's call on tempo, alternation and syntax — open

Two questions the study cannot settle on its own. The crossing takes about forty seconds at a natural tai chi tempo; calm, but long for a hero loop. And the phrase repeats on one side instead of alternating left and right as the form proper does — cheap to add, but it doubles the pose data and is barely visible in strict profile. Both are worth a look before any Markdown syntax work begins.
