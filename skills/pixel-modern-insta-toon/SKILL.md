---
name: pixel-modern-insta-toon
description: >-
  Korean manuscript and scenario adaptation into modern pixel-art insta-toon images. Use when the user asks for "dot", "pixel",
  "pixel art", "dot image", "modern chibi", "webtoon style", "Instagram toon", "Frieren-like mood without copying IP",
  or references a small cute pixel image but wants modern clothing, hair variation, glasses, hats, or situational accessories.
  Creates 1:1 or 4:5 modern daily-life pixel toon panels with chibi characters, limited colors, readable Korean speech bubbles,
  and IP-safe character design rather than copying a named character.
---

# Pixel Modern Insta Toon

## Core Definition

Create Korean insta-toon images in a modern pixel-art style. The style uses cute chibi proportions, chunky pixel edges, limited colors, and quiet everyday scenes. It may reference the mood and pixel texture of `assets/reference-dot-style.jpg`, but must not copy a named character, costume, pose, scene, or franchise-specific design.

Default output is a single 1:1 or 4:5 social image. Use 16:9 only when the user asks for a blog/header illustration or when matching the older hand-drawn skills.

## Read References

Read only the files needed for the task:

- `references/style-dna.md` - pixel-art visual rules, palette, background, text density, bans.
- `references/character-ip.md` - modern chibi character system, hair/accessory rules, IP safety.
- `references/composition-patterns.md` - 1 to 4 panel insta-toon structures.
- `references/prompt-template.md` - image generation prompt template.
- `references/qa-checklist.md` - verification and regeneration guidance.

## Workflow

### 1. Digest the Manuscript

Extract the main claim, emotional flow, and one visual anchor. Prefer situations that can be acted out by a modern chibi character: checking, waiting, sorting, comparing, posting, debugging, choosing, rejecting, or handing off.

If one image is enough, proceed with one image unless the user asks for a shot list first. If the manuscript naturally has setup, problem, turn, and conclusion, plan 3 to 4 separate images instead of crowding one canvas.

### 2. Plan the Toon

For each image, define:

- image role
- character action
- outfit and hair variation
- situational accessory
- exact Korean speech bubble or overlay text
- small labels, if any

Use accessories only when they clarify the situation. Limit accessories to 1 to 3 visible items.

### 3. Generate

Use built-in `image_gen` when the user asks to create, draw, generate, or output images. Generate each image separately. Do not combine multiple carousel pages into one image.

Prompt requirements:

- modern pixel-art insta-toon
- square or 4:5 vertical composition unless otherwise requested
- chibi modern human character
- modern clothing only
- hair may be long, short, bob, tied, or short cut depending on the scene
- glasses, hats, headset, backpack, badge, laptop, smartphone, coffee cup, notebook, checklist, or other modern accessories when useful
- readable Korean text, kept short
- no direct copy of any named anime, manga, game, or webtoon character

### 4. Verify

Use `references/qa-checklist.md`. Regenerate if the image copies a recognizable character, uses fantasy clothing, adds pointed ears, overuses accessories, becomes too painterly, or the Korean text is unreadable.

### 5. Save

Preserve the generated original, then copy the final image into:

```text
assets/YYYY-MM-DD/
```

Use ordered, descriptive filenames:

```text
01-topic-name.png
02-topic-name.png
```

Never overwrite existing assets. Add `-v2`, `-v3`, etc. when needed.

## Output Tone

Before generation, keep the shot plan compact. After generation, report the saved path, the image role, and any optional regeneration candidate. Do not over-explain style theory.
