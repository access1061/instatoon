# 9:16 layer generation prompts

Use both the strongest Fern identity image and the user's layout reference as image inputs. Generate files separately; never ask one generation to serve as all production layers.

## Character layer

```text
Create one standalone 9:16 full-body character cutout.

Character continuity:
Preserve the supplied Fern identity: very long deep-purple hair with straight bangs, violet eyes, pale skin, calm reserved expression, oversized matte-black hooded techwear, silver zippers and chains, and restrained violet accents. Preserve the supplied staff when requested.

Pose and framing:
Head-to-toe fashion pose from a subtly low camera angle. Both shoes and their cast shadow are fully visible. Natural hands and anatomy. Keep hair, staff, hands, and feet inside safe margins. The figure is dominant but leaves one clean side rail for later captions.

Layer policy:
Transparent background. Character and complete staff only. No floor, cast shadow, paper, abstract letters, registration marks, text, logo, or watermark. Keep generous transparent padding.

Output:
Single RGBA PNG, crisp detailed cel shading, complete full-body silhouette.
```

Verify actual alpha after generation. If a checkerboard is baked into RGB, create a real mask before accepting the layer.

## Background layer

```text
Create only a reusable 9:16 fashion-editorial background plate. No person, face, body, staff, silhouette portrait, pose-specific shadow, readable text, logo, or watermark.

Use warm off-white textured paper, near-black, cobalt and restrained violet, oversized abstract condensed-serif shapes that form no words, sparse registration marks, subtle distressed ink, a clean floor plane, a right caption rail, and clear top/bottom lockup zones. Keep the center-right quiet enough for a full-body character.
```

## Effects layers

Generate shadow, monochrome secondary portrait, particles, grain, and light wipes separately on transparency when they need independent motion. Prefer deterministic SVG for rules, labels, specimen cards, and exact typography.
