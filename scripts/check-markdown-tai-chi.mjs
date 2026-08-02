#!/usr/bin/env node
// Checks for the tai chi gesture study at docs/prototypes/markdown-tai-chi.html.
//
// Two halves. The first is structural: the prototype must stay a single
// self-contained file with its review affordances intact. The second imports
// the prototype's own movement code — the block between the geometry:start
// and geometry:end markers is deliberately DOM-free — and asserts that the
// figure is anatomically coherent and that the step loops without a seam.
// Eyeballing a forty-second loop will not catch a limb that stretches for a
// tenth of a second, or a hand that detaches when it over-reaches. This will.

import { readFile, writeFile, unlink } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import process from "node:process";

const PROTOTYPE = "docs/prototypes/markdown-tai-chi.html";
const path = new URL(`../${PROTOTYPE}`, import.meta.url);

const failures = [];
const check = (condition, message) => { if (!condition) failures.push(message); };

let source;
try {
  source = await readFile(path, "utf8");
} catch {
  console.error(`FAIL: ${PROTOTYPE} does not exist`);
  process.exit(1);
}

/* -------------------------------------------------------------------- *
 * Structure
 * -------------------------------------------------------------------- */

check(/data-study-version="4"/.test(source), "version 4 marker missing");
check(/<svg[^>]+data-stage/.test(source), "no SVG stage");
check(/data-sheet/.test(source), "no pose-by-pose contact sheet");
check(/viewBox="0 16 1000 116"/.test(source), "stage is not the wide shallow strip");
check(/function frameStage\(/.test(source), "no responsive camera framing");
check(/\.band--hero[^}]*height:\s*88px/.test(source), "no preview at real hero size");
check(/data-view="strict-profile"/.test(source), "strict-profile marker missing");
check(/data-action="toggle-play"/.test(source), "no pause control");
check(/data-action="restart"/.test(source), "no restart control");
check(/data-action="toggle-trails"/.test(source), "no trail toggle");
check(/data-scrub/.test(source), "no scrub control");
check(/location\.hash/.test(source), "no #t= deep link for review");
check(/prefers-reduced-motion/.test(source), "no reduced-motion handling");
check(/prefers-color-scheme/.test(source), "no dark-scheme colours");
check(/TRAIL_LIFE_MS/.test(source), "trails do not dissolve");

// Self-contained.
check(!/<script[^>]+\bsrc=/.test(source), "remote script tag");
check(!/<link[^>]+stylesheet/.test(source), "remote stylesheet");
check(!/<(?:script|link|img)[^>]+(?:src|href)=["']https?:\/\//.test(source), "remote asset");

// The rendering decisions this study exists to test. A regression to strokes
// drawn straight along a skeleton should fail loudly.
check(/function brush\(/.test(source), "no variable-width brush stroke renderer");
check(/function ik\(/.test(source), "no IK: joints must be derived, not hand-placed");
check(/\.ink \{ fill:/.test(source), "figure is not drawn as filled brush strokes");
check(!/feTurbulence|feDisplacementMap/.test(source), "wobble filters are back");

// Markdown syntax is deliberately postponed until the gesture is right.
check(!/<text\b/.test(source), "glyph rendering has arrived before the gesture is settled");

for (const match of source.matchAll(/<script>([\s\S]*?)<\/script>/g)) {
  try {
    new Function(match[1]);
  } catch (error) {
    failures.push(`inline JavaScript does not parse (${error.message})`);
  }
}

/* -------------------------------------------------------------------- *
 * Movement
 * -------------------------------------------------------------------- */

const geometry = source.match(/\/\* geometry:start([\s\S]*?)\/\* geometry:end/);
if (!geometry) {
  failures.push("geometry:start / geometry:end markers missing");
} else {
  const module = join(tmpdir(), `tai-chi-geometry-${process.pid}.mjs`);
  const body = geometry[1].replace(/^[\s\S]*?\*\//, "");
  await writeFile(module, `${body}
export { pose, strokes, GROUND, STRIDE, THIGH, SHIN, UPPER_ARM, FOREARM };
`);

  let g = null;
  try {
    g = await import(`file://${module}`);
  } catch (error) {
    failures.push(`movement code did not load: ${error.message}`);
  } finally {
    await unlink(module).catch(() => {});
  }

  if (g) {
    const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
    const SAMPLES = 400;
    const poses = [];
    for (let i = 0; i <= SAMPLES; i += 1) poses.push({ t: i / SAMPLES, p: g.pose(i / SAMPLES, 0) });

    let stretch = 0;
    let detached = 0;
    let sunk = 0;
    let crownHigh = Infinity;
    let crownLow = -Infinity;

    for (const { p } of poses) {
      // Bones keep their length. Hand-authored joints always drift; derived
      // ones should not.
      for (const [joint, root, tip, upper, lower] of [
        [p.kneePlanted, p.hip, p.plantedAnkle, g.THIGH, g.SHIN],
        [p.kneeSwing, p.hip, p.swingAnkle, g.THIGH, g.SHIN],
        [p.elbowA, p.shoulderA, p.handA, g.UPPER_ARM, g.FOREARM],
        [p.elbowB, p.shoulderB, p.handB, g.UPPER_ARM, g.FOREARM]
      ]) {
        stretch = Math.max(stretch, Math.abs(dist(root, joint) - upper));
        detached = Math.max(detached, Math.abs(dist(joint, tip) - lower));
      }

      for (const f of [p.plantedFoot, p.swingFoot]) {
        sunk = Math.max(sunk, f.heel[1] - g.GROUND, f.toe[1] - g.GROUND);
      }

      crownHigh = Math.min(crownHigh, p.crown[1]);
      crownLow = Math.max(crownLow, p.crown[1]);
    }

    check(stretch < 0.5, `an upper limb stretches by ${stretch.toFixed(2)} units`);
    check(detached < 0.5, `a hand or foot detaches from its limb by ${detached.toFixed(2)} units`);
    check(sunk < 1.6, `a foot sinks ${sunk.toFixed(2)} units through the floor`);

    // The head stays quiet while the hips travel and settle.
    const bob = crownLow - crownHigh;
    check(bob < 7, `the head bobs ${bob.toFixed(1)} units; it should stay quiet`);

    // The loop must be seamless. Compare the end of one step with the start
    // of the next, in a common frame: the pelvis has advanced one stride and
    // the two legs have swapped roles.
    const eps = 1 / SAMPLES;
    const before = g.pose(1 - eps, 0);
    const beforeEarlier = g.pose(1 - 2 * eps, 0);
    const after = g.pose(0, 0);
    const afterLater = g.pose(eps, 0);

    const world = (p, point) => [point[0] + p.travel, point[1]];
    const seam = (name, b, a) => {
      const gap = dist([b[0] - g.STRIDE, b[1]], a);
      check(gap < 1.5, `${name} jumps ${gap.toFixed(2)} units at the step boundary`);
    };

    seam("the hip", world(before, before.hip), world(after, after.hip));
    seam("the head", world(before, before.crown), world(after, after.crown));
    seam("the upper hand", world(before, before.handA), world(after, after.handA));
    seam("the lower hand", world(before, before.handB), world(after, after.handB));
    // Legs swap: this step's planted foot becomes the next step's swinging one.
    seam("the planted foot", world(before, before.plantedAnkle), world(after, after.swingAnkle));
    seam("the stepping foot", world(before, before.swingAnkle), world(after, after.plantedAnkle));

    // Velocity continuity, so the loop does not visibly stutter either.
    const speedBefore = dist(beforeEarlier.handA, before.handA);
    const speedAfter = dist(after.handA, afterLater.handA);
    check(Math.abs(speedBefore - speedAfter) < 0.4,
      `hand speed jumps from ${speedBefore.toFixed(2)} to ${speedAfter.toFixed(2)} across the boundary`);

    // The pelvis advances exactly one stride per step, or the figure slides
    // instead of stepping.
    check(Math.abs((before.travel - after.travel) - g.STRIDE) < 1,
      "the pelvis does not advance one stride per step");

    // Every stroke is a closed, finite path.
    for (const { t, p } of [poses[0], poses[97], poses[201], poses[333]]) {
      for (const s of g.strokes(p)) {
        check(/^M-?[\d.]/.test(s.d) && s.d.endsWith("Z"), `malformed stroke path at t=${t.toFixed(2)}`);
        check(!/NaN|Infinity/.test(s.d), `non-finite stroke path at t=${t.toFixed(2)}`);
      }
    }
  }
}

/* -------------------------------------------------------------------- */

if (failures.length > 0) {
  console.error(`FAIL: ${PROTOTYPE}`);
  for (const message of failures) console.error(`  - ${message}`);
  process.exit(1);
}

console.log(`PASS: ${PROTOTYPE} — structure, anatomy and loop continuity`);
