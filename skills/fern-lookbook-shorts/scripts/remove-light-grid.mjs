import sharp from 'sharp';
import path from 'node:path';

const [input, output] = process.argv.slice(2);
if (!input || !output) {
  console.error('Usage: node remove-light-grid.mjs input.png output.png');
  process.exit(2);
}
if (path.resolve(input) === path.resolve(output)) throw new Error('Input and output must differ.');

const {data, info} = await sharp(input).ensureAlpha().raw().toBuffer({resolveWithObject: true});
const {width: w, height: h, channels} = info;
const seen = new Uint8Array(w * h);
const queue = new Int32Array(w * h);
let head = 0, tail = 0;

const isLightNeutral = (i) => {
  const o = i * channels, r = data[o], g = data[o + 1], b = data[o + 2];
  return Math.min(r, g, b) >= 218 && Math.max(r, g, b) - Math.min(r, g, b) <= 22;
};
const add = (i) => {
  if (i < 0 || i >= w * h || seen[i] || !isLightNeutral(i)) return;
  seen[i] = 1; queue[tail++] = i;
};
for (let x = 0; x < w; x++) { add(x); add((h - 1) * w + x); }
for (let y = 0; y < h; y++) { add(y * w); add(y * w + w - 1); }
while (head < tail) {
  const i = queue[head++], x = i % w;
  if (x > 0) add(i - 1); if (x + 1 < w) add(i + 1);
  if (i >= w) add(i - w); if (i + w < w * h) add(i + w);
}
for (let i = 0; i < w * h; i++) if (seen[i]) data[i * channels + 3] = 0;
await sharp(data, {raw: {width: w, height: h, channels}}).png().toFile(output);
console.log(`${output}: removed ${tail} connected light-grid pixels`);

