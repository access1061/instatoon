import sharp from 'sharp';
import path from 'node:path';

const [input, output] = process.argv.slice(2);
if (!input || !output) {
  console.error('Usage: node prepare-lookbook.mjs input.png output.png');
  process.exit(2);
}
if (path.resolve(input) === path.resolve(output)) {
  throw new Error('Input and output must differ to preserve the source.');
}

await sharp(input)
  .rotate()
  .resize(1080, 1920, {
    fit: 'contain',
    position: 'centre',
    background: {r: 242, g: 238, b: 229, alpha: 1},
    withoutEnlargement: false,
  })
  .png({compressionLevel: 9})
  .toFile(output);

const meta = await sharp(output).metadata();
if (meta.width !== 1080 || meta.height !== 1920) {
  throw new Error(`Unexpected output size: ${meta.width}x${meta.height}`);
}
console.log(`${output}: ${meta.width}x${meta.height}`);

