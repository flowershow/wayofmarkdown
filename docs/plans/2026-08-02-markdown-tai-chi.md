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
