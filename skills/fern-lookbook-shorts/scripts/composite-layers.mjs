import sharp from 'sharp';
import fs from 'node:fs/promises';
import path from 'node:path';

const [manifestPath, output] = process.argv.slice(2);
if (!manifestPath || !output) {
  console.error('Usage: node composite-layers.mjs layers.json preview.png');
  process.exit(2);
}
const root = path.dirname(path.resolve(manifestPath));
const manifest = JSON.parse(await fs.readFile(manifestPath, 'utf8'));
const layers = [...manifest.layers].sort((a, b) => a.z - b.z);
const background = layers.shift();
if (!background) throw new Error('Manifest has no layers.');

let base = sharp(path.join(root, background.file)).resize(manifest.canvas.width, manifest.canvas.height, {fit: 'fill'});
const overlays = layers.map((layer) => ({input: path.join(root, layer.file), top: 0, left: 0, blend: 'over'}));
await base.composite(overlays).png().toFile(output);
console.log(output);
