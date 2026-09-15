---
name: fern-lookbook-shorts
description: Create and edit 9:16 full-body Fern-inspired fantasy fashion lookbook images, analyze reference posters for pose, palette, typography, and overlays, and turn layered still artwork into TTS-driven vertical shorts. Use when the user asks for Fern lookbooks, editorial character posters, refer1-style layouts, fixed-image animation, parallax, motion typography, ASS captions, TTS synchronization, or 1080x1920 Shorts/Reels output.
---

# Fern Lookbook Shorts

Build every deliverable as reusable 9:16 layers, then animate without damaging the character design. Treat generated lettering as disposable; render final readable text during compositing.

## Workflow

1. Inspect every supplied Fern image and visual reference with actual image input.
2. Read `references/visual-dna.md` before planning the image.
3. Read `references/layer-contract.md`. Separate immutable character traits, adaptable pose, background language, exact overlay copy, and motion intent.
4. Generate the layers independently using `references/image-prompt.md`: transparent character, text-free background, optional shadow/effect plates, and overlay artwork.
5. Verify every raster layer at `1080x1920`; never stretch. Reject fake checkerboards as transparency and verify an alpha channel.
6. Create `layers.json`, keeping source layers, editable SVG overlays, and a flattened preview. Use `scripts/composite-layers.mjs` for the preview.
7. Reserve the top 12%, bottom 18%, and a side rail for platform UI and captions.
8. For TTS video, read `references/motion-and-tts.md`, then use `scripts/render-lookbook-short.ps1` as the deterministic baseline.
9. Run `scripts/audit-toolchain.ps1` and the checks in `references/qa.md` before delivery.

## Editing rules

- Preserve the source face, long purple hair, violet eyes, black oversized techwear, silver hardware, calm expression, and any requested staff.
- Prefer a complete head-to-toe silhouette and visible ground contact. Never crop feet for a “full-body” request.
- Use the reference for visual grammar, not copied logos, franchise names, or readable wording.
- Keep generated-image typography abstract or absent. Render exact Korean and Latin copy with ASS, SVG, Sharp, or Remotion.
- Limit the palette to warm paper white, near-black, cobalt, and Fern violet unless the user specifies otherwise.
- Keep one dominant masthead, one vertical rail, one metadata block, and one closing lockup. Remove decoration that competes with the face or TTS captions.
- Animate layers at different speeds only when masks or clean plates exist. Otherwise use a subtle 1.00-1.04 camera move to avoid warped anatomy.
- Never discard layers after flattening. The preview is derivative; `layers.json` and source layers are the reusable master.

## Tool routing

- Use ImageGen for semantic restyling, pose changes, background replacement, and character-consistent variants.
- Use Sharp for deterministic resize, padding, compositing, alpha, masks, color adjustments, and metadata checks.
- Use FFmpeg for camera motion, overlays, ASS captions, audio muxing, fades, grain, and final encoding.
- Use Remotion when frame-accurate React/CSS/SVG typography, reusable scenes, word-level captions, or many variants justify a project scaffold.
- Treat segmentation/depth tools as optional enhancement. Do not block the baseline pipeline on model downloads.

## Outputs

Save under `assets/YYYY-MM-DD/` and preserve prior versions:

- `fern-lookbook-9x16-source.png`
- `fern-lookbook-9x16.png` at exactly `1080x1920`
- `layers/background.png`, `layers/character.png`, `layers/overlay.svg`, `layers/overlay.png`, and `layers.json`
- `fern-lookbook-short.ass`
- `fern-lookbook-short-9x16.mp4`
- `instagram-caption-fern-lookbook.md`

Use `-v2`, `-v3`, and so on when a name already exists.
