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
  ["version 2 marker", /data-study-version="2"/],
  ["named Wild Horse movement", /data-reference-movement="parting-wild-horse-mane"/],
  ["pause control", /id="pause-animation"/],
  ["replay control", /id="replay-animation"/],
  ["reduced-motion fallback", /prefers-reduced-motion:\s*reduce/],
  ["one-time composition", /const\s+COMPOSE_ONCE_MS\s*=/],
  ["continuous movement loop", /const\s+MOVEMENT_LOOP_MS\s*=/],
  ["Wild Horse keyframes", /const\s+WILD_HORSE_KEYFRAMES\s*=/],
  ["Wudang body regions", /const\s+WUDANG_PARTS\s*=/],
  ["fabric lag", /const\s+FABRIC_LAG\s*=/],
  ["static fallback figure", /id="static-figure"/],
  ["static SVG fallback can be hidden", /#static-figure\[hidden\]\s*\{[^}]*display:\s*none/],
  ["robe field renderer", /function\s+renderRobeField\s*\(/],
  ["sleeve field renderer", /function\s+renderSleeveField\s*\(/],
  ["coat-tail renderer", /function\s+renderCoatTails\s*\(/],
  ["topknot region", /data-region="topknot"/],
  ["robe region", /data-region="robe"/],
  ["sleeve regions", /data-region="sleeves"/],
  ["coat-tail regions", /data-region="coat-tails"/],
  ["responsive mobile layout", /@media\s*\(max-width:\s*760px\)/],
  ["dark colour treatment", /@media\s*\(prefers-color-scheme:\s*dark\)/],
  ["labelled review controls", /aria-label="Animation review controls"/],
];

const failures = checks
  .filter(([, pattern]) => !pattern.test(source))
  .map(([label]) => label);

if (/\bstaticFigure\.hidden\s*=/.test(source)) {
  failures.push("SVG layers do not use the unsupported .hidden property");
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
