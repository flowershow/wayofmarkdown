# Homepage Layout Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the mixed homepage layout with one responsive HTML/Tailwind page whose animated mark sits centred below the title.

**Architecture:** `index.md` remains the `/` route and keeps all content and links, but uses `layout: plain` and owns one consistent page shell. `custom.css` loses the homepage-specific theme overrides; the standalone `hero-mark.html` animation remains unchanged.

**Tech Stack:** Flowershow Markdown/MDX, HTML, Tailwind utility classes, Python source regression check.

---

### Task 1: Add a homepage structure regression check

**Files:**
- Create: `scripts/check-homepage.py`
- Test: `scripts/check-homepage.py`

**Step 1:** Assert that `index.md` uses `layout: plain`, contains the complete section set and required destinations, places the animated mark after the H1 and before the lede, and no longer contains `.wom-hero` wrappers.

**Step 2:** Run `python3 scripts/check-homepage.py` and confirm it fails against the current page.

### Task 2: Rebuild the complete homepage

**Files:**
- Modify: `index.md`

**Step 1:** Replace the mixed Markdown/HTML layout with a single `max-w-6xl` HTML shell and responsive Tailwind sections.

**Step 2:** Preserve all current copy and link destinations while moving the mark directly below the centred H1.

**Step 3:** Run `python3 scripts/check-homepage.py` and confirm it passes.

### Task 3: Remove obsolete theme overrides

**Files:**
- Modify: `custom.css`

**Step 1:** Delete `.wom-hero`, `.wom-cta`, and homepage `:has(...)` rules made unnecessary by `layout: plain`.

**Step 2:** Run the homepage check again.

### Task 4: Verify, log and publish

**Files:**
- Modify: `docs/plans/v0.2.md`

**Step 1:** Run `node scripts/check-tai-chi.mjs`, `python3 scripts/voice-lint.py`, `python3 scripts/link-check.py`, and validate `config.json`.

**Step 2:** Render and inspect the homepage at desktop and mobile widths.

**Step 3:** Add a session entry to the v0.2 narrative log and review-log issue #57.

**Step 4:** Commit the immediate fix, push `main`, and spot-check the live URL.

