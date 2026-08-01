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
  ["glyph body mode", /data-mode="glyph-body"/],
  ["syntax ribbons mode", /data-mode="syntax-ribbons"/],
  ["source constellation mode", /data-mode="source-constellation"/],
  ["pause control", /id="pause-animation"/],
  ["replay control", /id="replay-animation"/],
  ["reduced-motion fallback", /prefers-reduced-motion:\s*reduce/],
  ["source phase", /const\s+PHASE_SOURCE\s*=/],
  ["compose phase", /const\s+PHASE_COMPOSE\s*=/],
  ["flow phase", /const\s+PHASE_FLOW\s*=/],
  ["release phase", /const\s+PHASE_RELEASE\s*=/],
  ["body keyframes", /const\s+BODY_KEYFRAMES\s*=/],
  ["static fallback figure", /id="static-figure"/],
  ["static SVG fallback can be hidden", /#static-figure\[hidden\]\s*\{[^}]*display:\s*none/],
  ["SVG mode visibility uses attributes", /toggleAttribute\("hidden",/],
  ["glyph body renderer", /function\s+renderGlyphBody\s*\(/],
  ["syntax ribbons renderer", /function\s+renderSyntaxRibbons\s*\(/],
  ["source constellation renderer", /function\s+renderSourceConstellation\s*\(/],
  ["responsive mobile layout", /@media\s*\(max-width:\s*760px\)/],
  ["dark colour treatment", /@media\s*\(prefers-color-scheme:\s*dark\)/],
  ["labelled review controls", /aria-label="Animation review controls"/],
];

const failures = checks
  .filter(([, pattern]) => !pattern.test(source))
  .map(([label]) => label);

if (/\b(?:glyphLayer|ribbonLayer|constellationLayer|staticFigure)\.hidden\s*=/.test(source)) {
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
