#!/usr/bin/env node
// Checks for the tai chi gesture study published at /tai-chi.html.
//
// Two halves. The first is structural: the prototype must stay a single
// self-contained file with its review affordances intact. The second imports
// the prototype's own movement code — the block between the geometry:start
// and geometry:end markers is deliberately DOM-free — and asserts that the
// figure is anatomically coherent and that the gesture loops without a seam.
// Eyeballing a slow loop will not catch a limb that stretches for a tenth of
// a second, or a hand that detaches when it over-reaches. This will.

import { readFile, writeFile, unlink } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import process from "node:process";

const PROTOTYPE = "tai-chi.html";
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

check(/data-study-version="5"/.test(source), "version 5 marker missing");
check(/data-movement="press-and-push"/.test(source), "movement marker missing");
check(/data-view="strict-profile"/.test(source), "strict-profile marker missing");
check(/<svg[^>]+data-stage/.test(source), "no SVG stage");
check(/data-sheet/.test(source), "no pose-by-pose contact sheet");
check(/viewBox="0 14 200 118"/.test(source), "mark is not the compact in-place frame");
check(/\.size-80 \.tai-chi-mark \{ height: 80px/.test(source), "no preview at real running size");
check(/class="hero"/.test(source), "no in-context preview beside a headline");
check(/data-action="toggle-play"/.test(source), "no pause control");
check(/data-action="restart"/.test(source), "no restart control");
check(/data-scrub/.test(source), "no scrub control");
check(/location\.hash/.test(source), "no #t= deep link for review");
check(/prefers-reduced-motion/.test(source), "no reduced-motion handling");
check(/prefers-color-scheme/.test(source), "no dark-scheme colours");
// Published but deliberately unlisted: an unfinished study should not be
// indexed, and the sitemap alone will not stop that.
check(/name="robots"[^>]*noindex/.test(source), "published study is missing its noindex");

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

// The movement is one gesture in place. Travel, stepping and dissolving
// pose-ghosts were all deliberately removed; their machinery should not
// creep back in.
check(!/\bSTRIDE\b/.test(source), "stride is back: the movement should not travel");
check(!/TRAIL_LIFE_MS|dropTrail/.test(source), "pose trails are back");

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
export { pose, strokes, GROUND, THIGH, SHIN, UPPER_ARM, FOREARM, REAR_ANKLE, FRONT_ANKLE };
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
    let footDrift = 0;
    let handGap = 0;
    const reachA = { min: Infinity, max: -Infinity };

    for (const { p } of poses) {
      // Bones keep their length. Hand-authored joints always drift; derived
      // ones should not.
      for (const [joint, root, tip, upper, lower] of [
        [p.kneeRear, p.hip, p.rearAnkle, g.THIGH, g.SHIN],
        [p.kneeFront, p.hip, p.frontAnkle, g.THIGH, g.SHIN],
        [p.elbowA, p.shoulderA, p.handA, g.UPPER_ARM, g.FOREARM],
        [p.elbowB, p.shoulderB, p.handB, g.UPPER_ARM, g.FOREARM]
      ]) {
        stretch = Math.max(stretch, Math.abs(dist(root, joint) - upper));
        detached = Math.max(detached, Math.abs(dist(joint, tip) - lower));
      }

      // The feet are planted for the whole movement. This is the difference
      // between a gesture in place and a step.
      footDrift = Math.max(footDrift,
        dist(p.rearAnkle, g.REAR_ANKLE), dist(p.frontAnkle, g.FRONT_ANKLE));

      for (const f of [p.rearFoot, p.frontFoot]) {
        sunk = Math.max(sunk, f.heel[1] - g.GROUND, f.toe[1] - g.GROUND);
      }

      crownHigh = Math.min(crownHigh, p.crown[1]);
      crownLow = Math.max(crownLow, p.crown[1]);

      // Both palms belong to one gesture, so they must stay in the same
      // band. If they drift apart the mark reads as one hand up and one
      // hand down, which is a different movement entirely.
      handGap = Math.max(handGap, Math.abs(p.handA[1] - p.handB[1]));

      // How far the leading palm is in front of its shoulder.
      const reach = p.handA[0] - p.shoulderA[0];
      reachA.min = Math.min(reachA.min, reach);
      reachA.max = Math.max(reachA.max, reach);
    }

    check(stretch < 0.5, `an upper limb stretches by ${stretch.toFixed(2)} units`);
    check(detached < 0.5, `a hand or foot detaches from its limb by ${detached.toFixed(2)} units`);
    check(sunk < 1.6, `a foot sinks ${sunk.toFixed(2)} units through the floor`);
    check(footDrift < 0.01, `a foot moves ${footDrift.toFixed(2)} units; the movement is in place`);
    check(handGap < 16, `the palms drift ${handGap.toFixed(1)} units apart; they should press as a pair`);

    // The head stays quiet while the weight rolls back and forward.
    const bob = crownLow - crownHigh;
    check(bob < 7, `the head bobs ${bob.toFixed(1)} units; it should stay quiet`);

    // The gesture has to actually be a push. The palm must finish well in
    // front of the shoulder and come well back in — otherwise the mark is
    // technically animated and visually inert.
    check(reachA.max > 32, `the palm only reaches ${reachA.max.toFixed(1)} units in front of the shoulder`);
    check(reachA.max - reachA.min > 22, `the palm only travels ${(reachA.max - reachA.min).toFixed(1)} units; the push is too small to read`);

    // The loop must be seamless in position and in velocity, or the gesture
    // visibly restarts instead of breathing.
    const eps = 1 / SAMPLES;
    const end = g.pose(1 - eps, 0);
    const endEarlier = g.pose(1 - 2 * eps, 0);
    const start = g.pose(0, 0);
    const startLater = g.pose(eps, 0);

    for (const [name, key] of [
      ["the hip", "hip"], ["the head", "crown"],
      ["the leading palm", "handA"], ["the trailing palm", "handB"]
    ]) {
      const gap = dist(end[key], start[key]);
      check(gap < 1.2, `${name} jumps ${gap.toFixed(2)} units at the loop seam`);
    }

    const speedBefore = dist(endEarlier.handA, end.handA);
    const speedAfter = dist(start.handA, startLater.handA);
    check(Math.abs(speedBefore - speedAfter) < 0.4,
      `palm speed jumps from ${speedBefore.toFixed(2)} to ${speedAfter.toFixed(2)} across the loop seam`);

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
