"""Generate PNG icons and the social share image (run before build.py).
Requires Pillow. Uses DejaVu fonts (present on Ubuntu / GitHub runners)."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
INK, HL, CORAL, PAPER, INK2 = (20, 33, 61), (255, 216, 77), (255, 90, 78), (251, 250, 245), (59, 71, 99)
FONTS = ["/usr/share/fonts/truetype/dejavu/", "/usr/share/fonts/dejavu/"]


def font(name, size):
    for d in FONTS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def logo(size):
    s = size / 40.0
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([2 * s, 2 * s, 38 * s, 38 * s], radius=10 * s, fill=INK)
    w = max(1, round(3.4 * s))
    for a, b in [((11, 12), (11, 28)), ((11, 20), (20, 20)), ((20, 12), (20, 28))]:
        d.line([a[0] * s, a[1] * s, b[0] * s, b[1] * s], fill=HL, width=w)
        for x, y in (a, b):
            d.ellipse([x * s - w / 2, y * s - w / 2, x * s + w / 2, y * s + w / 2], fill=HL)
    d.ellipse([(28 - 2.6) * s, (26.5 - 2.6) * s, (28 + 2.6) * s, (26.5 + 2.6) * s], fill=CORAL)
    return im


def main():
    os.makedirs(IMG, exist_ok=True)
    for n in (192, 512):
        bg = Image.new("RGB", (n, n), INK)
        bg.paste(logo(n), (0, 0), logo(n))
        bg.save(os.path.join(IMG, f"icon-{n}.png"))
    W, H = 1200, 630
    og = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(og)
    for y in range(0, H, 36):
        d.line([0, y, W, y], fill=(236, 235, 228))
    lg = logo(84)
    og.paste(lg, (80, 130), lg)
    f1, f2, f3 = font("DejaVuSerif-Bold.ttf", 54), font("DejaVuSerif-Bold.ttf", 70), font("DejaVuSans.ttf", 26)
    d.text((184, 140), "High", font=f1, fill=INK)
    x = 184 + d.textlength("High", font=f1)
    d.text((x, 140), ".", font=f1, fill=CORAL)
    d.text((x + d.textlength(".", font=f1), 140), "School", font=f1, fill=INK)
    d.text((80, 260), "Everything high school,", font=f2, fill=INK)
    tw = d.textlength("in one place.", font=f2)
    d.rectangle([80, 382, 80 + tw, 420], fill=HL)
    d.text((80, 345), "in one place.", font=f2, fill=INK)
    d.text((80, 470), "Study guides · Test prep · GPA tools · College & scholarships · Online diplomas", font=f3, fill=INK2)
    og.save(os.path.join(IMG, "og.png"))
    print("images generated")


if __name__ == "__main__":
    main()
