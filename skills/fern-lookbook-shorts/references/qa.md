# QA checklist

- Output is exactly 1080x1920 and 9:16 without stretching.
- The full head, hair, both hands, both shoes, and requested staff are visible.
- Face, hair, outfit, and hardware match the Fern reference.
- No generated gibberish, copied logo, franchise name, or watermark remains.
- `character.png` and all effect plates have a real alpha channel; a visible checkerboard is a failure.
- `layers.json` references existing files and the flattened preview can be regenerated from them.
- Masthead, side rail, captions, and bottom lockup have distinct hierarchy.
- Foreground overlay copy does not collide with the staff head; place masthead behind the character or outside its bounding box.
- Text does not cover the eyes, hands, staff head, or shoes.
- Motion is subtle enough that line art stays stable and no edge reveals the canvas.
- Video has H.264 yuv420p video, AAC audio, correct duration, and `faststart`.
- QA frames at 20%, 50%, and 80% are readable and visually balanced.
