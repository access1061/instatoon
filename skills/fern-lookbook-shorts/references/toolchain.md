# Toolchain

## Required baseline

- FFmpeg/ffprobe: still-image loop, zoompan, overlay, subtitles, fades, grain, audio muxing, H.264 output.
- ImageGen: reference-aware generation and semantic edits.

## Recommended

- Sharp (Node): non-destructive resize/pad, alpha compositing, masks, color operations, and metadata validation.
- Remotion + React: frame-accurate CSS/SVG typography, captions, reusable scene components, audio-aware animation, and batch rendering. Check its current license before commercial-scale use.

## Optional enhancement

- OpenCV: deterministic masks, morphology, optical flow, image blending, and inspection.
- Background-removal or segmentation models: export transparent character layers.
- Monocular depth models: split a still into depth bands for conservative parallax.

Do not install large model weights automatically. Confirm disk, GPU, license, and network constraints first.

