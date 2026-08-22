# Still-image motion and TTS

## Baseline without masks

- Use 30 fps, 1080x1920, H.264 High, yuv420p, AAC, and `+faststart`.
- Keep total zoom within 1.00-1.04 over 6-15 seconds.
- Pan no more than 2% of frame height. Anchor the motion around the eyes, not the canvas center.
- Use one short 4-8 frame accent move per spoken beat: cobalt/violet wipe, underline, label reveal, or secondary portrait pulse.
- Fade in over 0.15-0.25 s and out over 0.25-0.40 s.

## Layered motion

When a transparent character cutout and clean background exist:

- Background: scale 1.02, travel 6-12 px.
- Masthead and print marks: travel 12-24 px in the opposite direction.
- Character: scale 1.00-1.015, travel 2-6 px.
- Foreground grain/light: travel 18-36 px at low opacity.
- Never deform the face, hair, hands, shoes, or staff.

## TTS synchronization

1. Measure audio duration with `ffprobe`.
2. Split narration into semantic beats, not equal time blocks.
3. Use ASS for Korean captions; render at most two lines and 12-18 Korean characters per line when practical.
4. Place captions in the reserved side rail or lower-middle safe zone; never cover eyes, hands, staff head, or footwear.
5. Reveal the main editorial label on the first keyword and the closing lockup during the last 0.6-1.0 s.
6. Generate QA frames at 20%, 50%, and 80% of duration.

Use Remotion instead of the baseline renderer when word-level highlighting, responsive typography, reusable components, or several coordinated layers are required.

