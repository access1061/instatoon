from pathlib import Path
import math
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont


W, H = 1600, 900
OUT_DIR = Path("assets/2026-07-02")
FONT_REG = "C:/Windows/Fonts/NotoSansKR-VF.ttf"
FONT_BOLD = "C:/Windows/Fonts/malgunbd.ttf"

INK = (24, 24, 24)
MUTED = (90, 90, 90)
RED = (220, 72, 55)
BLUE = (45, 112, 190)
ORANGE = (232, 132, 48)
GREEN = (58, 145, 87)
PALE_RED = (255, 235, 232)
PALE_BLUE = (232, 244, 255)
PALE_ORANGE = (255, 243, 229)
PALE_GREEN = (235, 250, 241)


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


F_BODY = font(35)
F_SMALL = font(26)
F_TINY = font(22)
F_BOLD = font(40, True)
F_BIG = font(54, True)


def unique_path(base: Path) -> Path:
    if not base.exists():
        return base
    stem, suffix = base.stem, base.suffix
    n = 2
    while True:
        candidate = base.with_name(f"{stem}-v{n}{suffix}")
        if not candidate.exists():
            return candidate
        n += 1


def jitter(points, amount=2):
    out = []
    for x, y in points:
        out.append((x + random.randint(-amount, amount), y + random.randint(-amount, amount)))
    return out


def line(draw, points, fill=INK, width=3):
    draw.line(jitter(points), fill=fill, width=width, joint="curve")


def rect(draw, xy, outline=INK, width=3, fill=None, r=0):
    x1, y1, x2, y2 = xy
    if r:
        draw.rounded_rectangle((x1, y1, x2, y2), radius=r, outline=outline, width=width, fill=fill)
    else:
        draw.rectangle((x1, y1, x2, y2), outline=outline, width=width, fill=fill)


def text(draw, xy, s, f=F_BODY, fill=INK, anchor=None, align="left"):
    draw.multiline_text(xy, s, font=f, fill=fill, spacing=9, anchor=anchor, align=align)


def wrapped(draw, box, s, f=F_BODY, fill=INK, max_chars=18, align="left"):
    lines = []
    for para in s.split("\n"):
        lines.extend(textwrap.wrap(para, width=max_chars, break_long_words=False) or [""])
    text(draw, (box[0], box[1]), "\n".join(lines), f, fill, align=align)


def bubble(draw, xy, s, f=F_BODY, max_chars=16, fill=(255, 255, 255), accent=None):
    x1, y1, x2, y2 = xy
    rect(draw, xy, width=3, fill=fill, r=22)
    if accent:
        line(draw, [(x1 + 28, y1 + 12), (x2 - 28, y1 + 12)], fill=accent, width=4)
    wrapped(draw, (x1 + 24, y1 + 24, x2 - 24, y2 - 24), s, f=f, max_chars=max_chars)


def note(draw, xy, s, color=PALE_ORANGE, f=F_SMALL, max_chars=13):
    x1, y1, x2, y2 = xy
    rect(draw, xy, width=2, fill=color, r=10)
    wrapped(draw, (x1 + 18, y1 + 15, x2 - 18, y2 - 15), s, f=f, max_chars=max_chars)


def character(draw, x, y, pose="point", mood="focus", accent=BLUE):
    # Big head, small body, plain adult mini character.
    head = (x - 42, y - 135, x + 42, y - 52)
    draw.ellipse(head, outline=INK, width=3, fill=(255, 255, 255))
    # hair
    for i in range(8):
        xx = x - 34 + i * 10
        line(draw, [(xx, y - 128), (xx + 8, y - 112)], width=2)
    # round ears
    draw.ellipse((x - 50, y - 104, x - 38, y - 88), outline=INK, width=2)
    draw.ellipse((x + 38, y - 104, x + 50, y - 88), outline=INK, width=2)
    # face
    if mood == "worry":
        line(draw, [(x - 18, y - 92), (x - 10, y - 94)], width=2)
        line(draw, [(x + 10, y - 94), (x + 18, y - 92)], width=2)
        line(draw, [(x - 7, y - 75), (x + 7, y - 73)], width=2)
    else:
        draw.ellipse((x - 18, y - 94, x - 12, y - 88), fill=INK)
        draw.ellipse((x + 12, y - 94, x + 18, y - 88), fill=INK)
        line(draw, [(x - 6, y - 75), (x + 8, y - 77)], width=2)
    # torso
    rect(draw, (x - 30, y - 50, x + 30, y + 32), width=3, fill=(255, 255, 255), r=14)
    line(draw, [(x - 20, y - 30), (x + 20, y - 30)], fill=accent, width=3)
    # legs
    line(draw, [(x - 14, y + 32), (x - 22, y + 78)], width=4)
    line(draw, [(x + 14, y + 32), (x + 22, y + 78)], width=4)
    line(draw, [(x - 30, y + 78), (x - 12, y + 78)], width=4)
    line(draw, [(x + 12, y + 78), (x + 32, y + 78)], width=4)
    # arms
    if pose == "point":
        line(draw, [(x - 30, y - 20), (x - 76, y - 38)], width=4)
        line(draw, [(x + 30, y - 18), (x + 72, y - 48)], width=4)
        draw.ellipse((x + 68, y - 53, x + 80, y - 41), outline=INK, width=2)
    elif pose == "hold":
        line(draw, [(x - 30, y - 16), (x - 66, y + 10)], width=4)
        line(draw, [(x + 30, y - 16), (x + 66, y + 10)], width=4)
    elif pose == "pull":
        line(draw, [(x - 30, y - 18), (x - 92, y - 18)], width=4)
        line(draw, [(x + 30, y - 18), (x + 82, y - 18)], width=4)
    else:
        line(draw, [(x - 30, y - 18), (x - 56, y + 18)], width=4)
        line(draw, [(x + 30, y - 18), (x + 56, y + 18)], width=4)


def chip(draw, x, y, label="AI 칩", falling=False):
    rect(draw, (x - 70, y - 55, x + 70, y + 55), width=3, fill=(255, 255, 255), r=12)
    for i in range(5):
        line(draw, [(x - 94, y - 38 + i * 19), (x - 70, y - 38 + i * 19)], width=2)
        line(draw, [(x + 70, y - 38 + i * 19), (x + 94, y - 38 + i * 19)], width=2)
    text(draw, (x, y - 16), label, f=F_SMALL, anchor="mm", align="center")
    if falling:
        line(draw, [(x - 30, y + 78), (x + 10, y + 120), (x + 48, y + 88)], fill=RED, width=5)


def cloud(draw, x, y, label="Meta\nCompute", fill=PALE_BLUE):
    draw.ellipse((x - 120, y - 35, x - 45, y + 45), outline=INK, width=3, fill=fill)
    draw.ellipse((x - 70, y - 70, x + 20, y + 35), outline=INK, width=3, fill=fill)
    draw.ellipse((x - 5, y - 45, x + 98, y + 50), outline=INK, width=3, fill=fill)
    rect(draw, (x - 110, y - 10, x + 100, y + 52), width=0, fill=fill, r=0)
    line(draw, [(x - 105, y + 48), (x + 92, y + 48)], width=3)
    text(draw, (x, y + 6), label, f=F_SMALL, anchor="mm", align="center")


def arrow(draw, start, end, color=ORANGE, width=5):
    line(draw, [start, end], fill=color, width=width)
    sx, sy = start
    ex, ey = end
    ang = math.atan2(ey - sy, ex - sx)
    for da in (2.55, -2.55):
        p = (ex - 24 * math.cos(ang + da), ey - 24 * math.sin(ang + da))
        line(draw, [p, end], fill=color, width=width)


def footer(draw, page):
    text(draw, (80, 820), f"{page:02d}/08", f=F_TINY, fill=MUTED)
    line(draw, [(1380, 826), (1510, 826)], fill=(190, 190, 190), width=2)


def canvas():
    img = Image.new("RGB", (W, H), "white")
    return img, ImageDraw.Draw(img)


def page1():
    img, d = canvas()
    note(d, (80, 80, 360, 155), "7월 1일\n시장의 시선", PALE_BLUE, F_SMALL)
    character(d, 315, 640, "point", "focus", BLUE)
    cloud(d, 720, 290, "Meta\nCompute", PALE_BLUE)
    chip(d, 1060, 310, "AI 칩")
    arrow(d, (835, 310), (970, 310))
    bubble(d, (420, 520, 890, 700), "메타는 올랐는데,\n반도체는 왜 흔들렸지?", F_BODY, 15, accent=BLUE)
    note(d, (980, 535, 1390, 685), "핵심은\n'AI 컴퓨팅이 남을 수도 있다'\n라는 신호였어요.", PALE_ORANGE, F_SMALL, 16)
    footer(d, 1)
    return img


def page2():
    img, d = canvas()
    character(d, 255, 690, "hold", "focus", GREEN)
    cloud(d, 680, 260, "남는\nAI 컴퓨팅", PALE_GREEN)
    rect(d, (930, 190, 1290, 370), width=3, fill=(255, 255, 255), r=18)
    text(d, (1110, 245), "외부 고객에게\n빌려주는 사업", f=F_BODY, anchor="mm", align="center")
    arrow(d, (785, 265), (925, 270), GREEN)
    bubble(d, (330, 525, 760, 705), "메타 입장에선\n투자비를 수익원으로\n바꿀 기회예요.", F_SMALL, 15, accent=GREEN)
    note(d, (930, 495, 1360, 655), "그래서 Meta 주가는\n약 9~10% 급등", PALE_GREEN, F_BODY, 17)
    footer(d, 2)
    return img


def page3():
    img, d = canvas()
    # seesaw
    line(d, [(425, 500), (1180, 385)], width=5)
    line(d, [(800, 470), (760, 650), (840, 650), (800, 470)], width=4)
    chip(d, 460, 440, "칩 부족")
    cloud(d, 1130, 330, "남는\n용량", PALE_ORANGE)
    character(d, 780, 420, "pull", "worry", ORANGE)
    bubble(d, (130, 120, 610, 300), "투자자들이 믿던 전제:\nAI 수요는 항상 공급보다 많다", F_SMALL, 20, accent=BLUE)
    bubble(d, (910, 560, 1435, 710), "그런데 메타가\n'남는 용량'을 말하자\n전제가 흔들렸어요.", F_SMALL, 17, accent=ORANGE)
    footer(d, 3)
    return img


def page4():
    img, d = canvas()
    character(d, 260, 650, "point", "worry", RED)
    for i, (x, name, pct) in enumerate([(570, "마이크론", "-10%대"), (815, "인텔", "-9%"), (1060, "AMD", "-7%"), (1305, "엔비디아", "-1%대")]):
        chip(d, x, 310 + (i % 2) * 25, name, True)
        text(d, (x, 505 + (i % 2) * 25), pct, f=F_SMALL, fill=RED, anchor="mm")
    bubble(d, (115, 145, 520, 330), "시장은 바로\n반도체 공급망을\n다시 계산했어요.", F_BODY, 15, accent=RED)
    note(d, (610, 610, 1390, 745), "낙폭은 종목마다 달랐지만,\n공통 질문은 같았어요.\n'칩을 계속 이렇게 많이 살까?'", PALE_RED, F_SMALL, 24)
    footer(d, 4)
    return img


def page5():
    img, d = canvas()
    character(d, 300, 640, "pull", "worry", RED)
    rect(d, (560, 210, 830, 520), width=3, fill=(255, 255, 255), r=18)
    text(d, (695, 280), "GPU\n임대점", f=F_BODY, anchor="mm", align="center")
    line(d, [(600, 340), (790, 340)], width=3)
    cloud(d, 1110, 285, "Meta도\n임대?", PALE_BLUE)
    arrow(d, (980, 300), (850, 345), RED)
    bubble(d, (120, 120, 530, 300), "CoreWeave,\nNebius 같은 업체는\n직접 경쟁 우려가 커졌죠.", F_SMALL, 16, accent=RED)
    note(d, (930, 560, 1390, 700), "가격 경쟁?\n계약 가치 하락?\n그래서 더 크게 흔들림", PALE_RED, F_SMALL, 16)
    footer(d, 5)
    return img


def page6():
    img, d = canvas()
    character(d, 275, 640, "hold", "focus", BLUE)
    rect(d, (540, 205, 780, 500), width=3, fill=(255, 255, 255), r=20)
    text(d, (660, 260), "ChatGPT\n처리", f=F_SMALL, anchor="mm", align="center")
    chip(d, 1070, 315, "GPU")
    line(d, [(1040, 210), (1100, 420)], fill=RED, width=5)
    line(d, [(1100, 210), (1040, 420)], fill=RED, width=5)
    bubble(d, (100, 110, 560, 310), "추가 악재도 있었어요.\n오픈AI가 추론 비용을\n줄였다는 보도.", F_SMALL, 17, accent=BLUE)
    note(d, (810, 555, 1390, 705), "소프트웨어가 효율화되면\n같은 일을 더 적은 GPU로 할 수도 있다는 걱정", PALE_BLUE, F_SMALL, 23)
    footer(d, 6)
    return img


def page7():
    img, d = canvas()
    character(d, 300, 640, "point", "worry", ORANGE)
    rect(d, (560, 210, 940, 500), width=3, fill=(255, 255, 255), r=18)
    text(d, (750, 260), "공매도\n소식", f=F_BODY, anchor="mm", align="center")
    line(d, [(640, 350), (860, 430)], fill=RED, width=5)
    chip(d, 1180, 340, "AI 대표주", True)
    bubble(d, (115, 120, 520, 300), "여기에 마이클 버리의\nAI주 공매도 소식까지\n심리를 눌렀어요.", F_SMALL, 17, accent=ORANGE)
    note(d, (965, 585, 1390, 705), "뉴스 하나보다\n'의심이 겹친 날'에 가까움", PALE_ORANGE, F_SMALL, 17)
    footer(d, 7)
    return img


def page8():
    img, d = canvas()
    character(d, 290, 640, "hold", "focus", GREEN)
    rect(d, (520, 170, 1125, 610), width=3, fill=(255, 255, 255), r=18)
    wrapped(d, (585, 235, 1070, 500), "메타: 수익 다각화 기대\n반도체: '무한 수요' 서사 점검\n단서: 장기 AI 투자 흐름은 아직 남아 있음", F_BODY, max_chars=21)
    bubble(d, (115, 130, 485, 315), "결론은 폭락 신호라기보다\n기대치 재가격화에 가까워요.", F_SMALL, 15, accent=GREEN)
    note(d, (1160, 410, 1450, 595), "핵심 질문\n칩이 부족한가?\n아니면 남는가?", PALE_GREEN, F_SMALL, 13)
    footer(d, 8)
    return img


PAGES = [
    ("01-meta-ai-question.png", page1),
    ("02-meta-compute-revenue.png", page2),
    ("03-ai-demand-premise.png", page3),
    ("04-semiconductor-selloff.png", page4),
    ("05-gpu-rental-shock.png", page5),
    ("06-openai-efficiency.png", page6),
    ("07-shorting-sentiment.png", page7),
    ("08-summary-repricing.png", page8),
]


def main():
    random.seed(7)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    saved = []
    for name, maker in PAGES:
        path = unique_path(OUT_DIR / name)
        img = maker()
        img.save(path, "PNG", optimize=True)
        saved.append(path)
    for path in saved:
        print(path.as_posix())


if __name__ == "__main__":
    main()
