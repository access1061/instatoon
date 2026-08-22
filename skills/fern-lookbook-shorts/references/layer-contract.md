# Layer contract

Every project is a folder, not one flattened image.

| z | File | Purpose | Alpha |
|---:|---|---|---|
| 0 | `background.png` | Paper, abstract masthead shapes, floor | no |
| 10 | `rear-effects.png` | Shadow, secondary silhouette, particles | yes |
| 20 | `character.png` | Complete Fern and requested staff | yes |
| 30 | `front-effects.png` | Light, grain accents, wipes | yes |
| 40 | `overlay.svg` / `overlay.png` | Editable masthead, rails, metadata | yes |
| 50 | `captions.ass` | TTS captions and timed emphasis | n/a |

Use exactly `1080x1920` for every raster plate. Store positions, opacity, blend intent, and motion in `layers.json`. A missing optional layer is allowed; silently flattening required layers is not.

## Generation order

1. Generate or approve a flattened visual anchor.
2. Generate the character alone. Verify actual alpha; checkerboard pixels are not transparency.
3. Generate the clean background without people, shadows tied to a specific pose, or readable text.
4. Build exact typography as editable SVG. Rasterize only for preview or FFmpeg input.
5. Add rear/front effects as separate transparent plates.
6. Composite a preview and compare it to the anchor.

## Reuse

- New narration: replace `captions.ass` and audio only.
- New colorway: recolor SVG and effect plates; preserve the character master.
- New pose: replace `character.png`, shadow, and character motion only.
- New campaign: replace background and overlay copy while preserving project dimensions and safe zones.

