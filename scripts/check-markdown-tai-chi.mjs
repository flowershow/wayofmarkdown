import { readFileSync } from "node:fs";

const prototypePath = new URL("../docs/prototypes/markdown-tai-chi.html", import.meta.url);

let source;
try {
  source = readFileSync(prototypePath, "utf8");
} catch {
  console.error("FAIL: docs/prototypes/markdown-tai-chi.html does not exist");
  process.exit(1);
}

const checks = [
  ["inline SVG stage", /<svg[^>]+id="motion-stage"/],
  ["version 3 marker", /data-study-version="3"/],
  ["wide shallow viewbox", /viewBox="0 0 1000 140"/],
  ["gesture-first marker", /data-rendering="gesture-lines"/],
  ["profile movement marker", /data-view="strict-profile"/],
  ["pause control", /id="pause-animation"/],
  ["replay control", /id="replay-animation"/],
  ["reduced-motion fallback", /prefers-reduced-motion:\s*reduce/],
  ["continuous movement loop", /const\s+MOVEMENT_LOOP_MS\s*=/],
  ["dissolving trail lifetime", /const\s+TRAIL_LIFETIME_MS\s*=/],
  ["trail sampling interval", /const\s+TRAIL_SAMPLE_MS\s*=/],
  ["tai chi gesture keyframes", /const\s+TAI_CHI_KEYFRAMES\s*=/],
  ["live gesture layer", /id="live-gesture"/],
  ["dissolving trail layer", /id="gesture-trails"/],
  ["spine gesture", /data-stroke="spine"/],
  ["leading arm gesture", /data-stroke="lead-arm"/],
  ["following arm gesture", /data-stroke="following-arm"/],
  ["grounded leg gesture", /data-stroke="grounded-leg"/],
  ["stepping leg gesture", /data-stroke="stepping-leg"/],
  ["snapshot trail renderer", /function\s+captureTrail\s*\(/],
  ["trail fade renderer", /function\s+renderTrails\s*\(/],
  ["static reduced-motion pose", /id="static-gesture"/],
  ["responsive mobile layout", /@media\s*\(max-width:\s*760px\)/],
  ["dark colour treatment", /@media\s*\(prefers-color-scheme:\s*dark\)/],
  ["labelled review controls", /aria-label="Animation review controls"/],
];

const failures = checks
  .filter(([, pattern]) => !pattern.test(source))
  .map(([label]) => label);

if (/<text\b[^>]*class=["'][^"']*(?:glyph|token)/.test(source)) {
  failures.push("version 3 postpones Markdown glyph rendering");
}

if (/<(?:script|link)[^>]+(?:src|href)=["']https?:\/\//.test(source)) {
  failures.push("no remote scripts or stylesheets");
}

for (const match of source.matchAll(/<script>([\s\S]*?)<\/script>/g)) {
  try {
    new Function(match[1]);
  } catch (error) {
    failures.push(`valid inline JavaScript (${error.message})`);
  }
}

if (failures.length > 0) {
  console.error(`FAIL: ${failures.join(", ")}`);
  process.exit(1);
}

console.log(`PASS: ${checks.length + 1} prototype structure checks`);
