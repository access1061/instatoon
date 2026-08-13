#!/usr/bin/env python3
"""Fit an image inside an exact Instagram 4:5 canvas without cropping."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


TARGET_SIZE = (1080, 1350)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fit an image to 1080x1350 using white padding; never crop or stretch."
    )
    parser.add_argument("input", type=Path, help="Source image path")
    parser.add_argument("output", type=Path, help="Destination PNG path")
    return parser.parse_args()


def fit_image(source: Path, destination: Path) -> None:
    if source.resolve() == destination.resolve():
        raise ValueError("Input and output paths must differ to preserve the source.")

    with Image.open(source) as opened:
        image = opened.convert("RGB")
        image.thumbnail(TARGET_SIZE, Image.Resampling.LANCZOS)

        canvas = Image.new("RGB", TARGET_SIZE, "white")
        offset = (
            (TARGET_SIZE[0] - image.width) // 2,
            (TARGET_SIZE[1] - image.height) // 2,
        )
        canvas.paste(image, offset)

        destination.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(destination, format="PNG", optimize=True)

    with Image.open(destination) as result:
        if result.size != TARGET_SIZE:
            raise RuntimeError(f"Unexpected output size: {result.size}")


def main() -> None:
    args = parse_args()
    fit_image(args.input, args.output)
    print(f"Saved {args.output} ({TARGET_SIZE[0]}x{TARGET_SIZE[1]})")


if __name__ == "__main__":
    main()
