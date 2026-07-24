# QA Checklist

## Must Pass

- Output is 1:1 or 4:5 unless another ratio was requested.
- Image reads as pixel art: blocky edges, clustered highlights, limited palette.
- Character is a modern human chibi, not a fantasy or copied franchise character.
- Ears are rounded human ears.
- Clothing is modern daily-life or workwear.
- Hair variation fits the scene: long, bob, tied, short, or bangs.
- Accessories are context-relevant and limited to 1 to 3.
- Character performs the core action instead of posing decoratively.
- Korean text is short, readable, and close to the requested wording.
- Scene is not crowded; background supports the story without stealing focus.
- Reference image is used only for texture/mood, not copied.
- Final image is saved under `assets/YYYY-MM-DD/` without overwriting an existing file.

## Failure Signals

- Looks like a recognizable named character or a direct derivative.
- Uses plant-on-head motif, fantasy costume, elf ears, magic props, or the reference image's exact pairing/composition.
- Looks like smooth vector art, painterly anime, or 3D render instead of pixel art.
- Too many props or accessories make the image hard to read.
- Text is too long, misspelled, or visually cramped.
- Character does not act out the manuscript's meaning.

## Iteration

- If IP similarity is high, change hair, palette, outfit, pose, and scene together.
- If fantasy cues appear, restate "modern clothing only" and list forbidden fantasy elements.
- If text fails, reduce to one shorter speech bubble and one label.
- If the image is too busy, remove background objects and keep one action.
- If pixel effect is weak, emphasize "crisp blocky pixel edges, visible stair-step silhouette, limited palette, clustered square highlights."
