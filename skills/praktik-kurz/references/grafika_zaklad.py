# Základ pro grafiku kurzu PRAKTIK-AI (postup: references/grafika.md).
# Zkopíruj do <složka kurzu>/grafika/vykresli_grafiku.py, dopiš funkce obrázků a spusť ze složky grafika.
# Vzor hotové grafiky: kurz B1001 (09_Kurzy/TEST1_PodkladyKurzu/B1001PravidlaAI/grafika).
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1600, 900
SS = 2  # kreslí se ve dvojnásobném rozlišení a zmenšuje (hladké hrany)
F = r"C:\Windows\Fonts\segoeui.ttf"     # Regular: veškerý běžný text
FB = r"C:\Windows\Fonts\seguisb.ttf"    # Semibold: nadpisy a popisky

BG = "#FFFFFF"
TEXT = "#1F2933"
MUTED = "#52606D"
LINE = "#CBD2D9"
PANEL = "#F5F7FA"
BLUE = "#1F5FA8"
RED = "#C62828"
AMBER = "#E0A100"
GREEN = "#2E7D32"

# Jednotná typografie: dva řezy, pevná škála velikostí
TITLE, HEAD_L, HEAD, BODY, NOTE = 44, 36, 30, 27, 22
# Jednotné tloušťky čar
STROKE, ACCENT, ARROW = 2, 3, 4

_fonts = {}


def font(size, bold=False):
    if bold:
        size = TITLE if size >= 44 else HEAD_L if size >= 36 else HEAD if size >= 30 else BODY
    else:
        size = NOTE if size <= 22 else BODY
    key = (size, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FB if bold else F, size * SS)
        _fonts[key].logical = size
    return _fonts[key]


class Draw:
    """Kreslí v logických souřadnicích 1600 × 900 do plátna SS× většího."""

    def __init__(self, im):
        self.d = ImageDraw.Draw(im)

    @staticmethod
    def _s(v):
        if isinstance(v, (list, tuple)):
            return type(v)(Draw._s(x) for x in v)
        return v * SS

    def text(self, xy, s, font, fill):
        self.d.text(self._s(xy), s, font=font, fill=fill)

    def textlength(self, s, font):
        return self.d.textlength(s, font=font) / SS

    def line(self, xy, fill, width=STROKE):
        self.d.line(self._s(xy), fill=fill, width=width * SS)

    def polygon(self, pts, fill):
        self.d.polygon([self._s(p) for p in pts], fill=fill)

    def ellipse(self, xy, fill=None, outline=None, width=ACCENT):
        self.d.ellipse(self._s(xy), fill=fill, outline=outline, width=width * SS)

    def rectangle(self, xy, outline, width=ACCENT):
        self.d.rectangle(self._s(xy), outline=outline, width=width * SS)

    def rounded_rectangle(self, xy, radius, fill=None, outline=None, width=STROKE):
        self.d.rounded_rectangle(self._s(xy), radius=radius * SS, fill=fill, outline=outline, width=width * SS)


def wrap(d, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        raw, words, i = para.split(), [], 0
        while i < len(raw):
            w = raw[i]
            while (w.endswith("odst.") or (len(w) == 1 and w.lower() in "vkszouai")) and i + 1 < len(raw):
                i += 1
                w = w + " " + raw[i]
            words.append(w)
            i += 1
        cur = ""
        for w in words:
            test = (cur + " " + w).strip()
            if d.textlength(test, font=fnt) <= width:
                cur = test
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def text_block(d, xy, text, fnt, width, fill=TEXT, spacing=1.35):
    x, y = xy
    for line in wrap(d, text, fnt, width):
        d.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.logical * spacing)
    return y


def new(title):
    im = Image.new("RGB", (W * SS, H * SS), BG)
    d = Draw(im)
    d.text((70, 50), title, font=font(TITLE, True), fill=TEXT)
    d.line((70, 118, W - 70, 118), fill=LINE, width=STROKE)
    return im, d


def footer(d, text):
    d.text((70, H - 60), text, font=font(NOTE), fill=MUTED)


def arrow(d, x1, y1, x2, y2, color=BLUE, w=ARROW):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    s = 18
    d.line((x1, y1, x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)), fill=color, width=w)
    p1 = (x2 - s * math.cos(a - 0.45), y2 - s * math.sin(a - 0.45))
    p2 = (x2 - s * math.cos(a + 0.45), y2 - s * math.sin(a + 0.45))
    d.polygon([(x2, y2), p1, p2], fill=color)


def box(d, x, y, w, h, fill=PANEL, outline=LINE, r=18, width=None):
    width = STROKE if outline in (LINE,) else ACCENT
    d.rounded_rectangle((x, y, x + w, y + h), radius=r, fill=fill, outline=outline, width=width)


def save(im, name):
    im = im.resize((W, H), Image.LANCZOS)
    im.save(os.path.join(OUT, name), "PNG")
    print("ulozeno", name)


# Ukázka: dva rámečky se šipkou. Nahraď vlastními funkcemi obrázků.
def ukazka():
    im, d = new("Titulek obrázku")
    box(d, 70, 200, 600, 200)
    d.text((95, 225), "Nadpis rámečku", font=font(HEAD, True), fill=TEXT)
    text_block(d, (95, 275), "Krátký text, který se zalomí do šířky rámečku.", font(BODY), 550, fill=MUTED)
    arrow(d, 690, 300, 820, 300)
    box(d, 840, 200, 600, 200, fill=BG, outline=BLUE)
    d.text((865, 225), "Zvýrazněný rámeček", font=font(HEAD, True), fill=TEXT)
    footer(d, "Podle … (zdroj).")
    save(im, "KOD-M1-01-schema-ukazka.png")


if __name__ == "__main__":
    for g in (ukazka,):
        g()
