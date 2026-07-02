from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SRC = Path(
    r"C:\Users\Administrator\.codex\generated_images\019f2153-d964-7fc0-a241-38ba2baca8e5\ig_025f27de536adda0016a45fca93150819181a6c64ce7d26d15.png"
)
OUT_DIR = Path("assets/2026-07-02")
FONT_REG = "C:/Windows/Fonts/NotoSansKR-VF.ttf"
FONT_BOLD = "C:/Windows/Fonts/malgunbd.ttf"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix
    version = 2
    while True:
        candidate = path.with_name(f"{stem}-v{version}{suffix}")
        if not candidate.exists():
            return candidate
        version += 1


def font(size: int, bold: bool = False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def clean_white_background(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if r > 238 and g > 238 and b > 238:
                px[x, y] = (255, 255, 255)
    return img


def draw_text(draw: ImageDraw.ImageDraw, xy, text, size=46, bold=False, fill=(24, 24, 24)):
    draw.multiline_text(
        xy,
        text,
        font=font(size, bold),
        fill=fill,
        spacing=12,
        align="left",
    )


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = clean_white_background(Image.open(SRC))
    raw_path = unique_path(OUT_DIR / "01-style-sample-news-toon-raw.png")
    final_path = unique_path(OUT_DIR / "01-style-sample-news-toon.png")

    img.save(raw_path, "PNG", optimize=True)

    draw = ImageDraw.Draw(img)
    draw_text(draw, (180, 205), "메타는\n올랐는데...", 54)
    draw_text(draw, (1135, 215), "반도체는\n왜 흔들렸지?", 54)
    img.save(final_path, "PNG", optimize=True)
    print(raw_path.as_posix())
    print(final_path.as_posix())


if __name__ == "__main__":
    main()
