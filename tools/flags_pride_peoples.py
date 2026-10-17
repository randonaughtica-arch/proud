"""Pride, Indigenous peoples and other peoples' flags."""
from emblems import DHARI, YAZ, SPIRE, PINE
from registry import flag

W_ = "#ffffff"
K_ = "#000000"

# --------------------------------------------------------------------------- pride

RAINBOW = ["#e40303", "#ff8c00", "#ffed00", "#008026", "#24408e", "#732982"]


@flag("rainbow_pride", "Rainbow Pride", "pride")
def _(c):
    c.hstripes(RAINBOW)


@flag("gilbert_baker_pride", "Gilbert Baker Pride (1978)", "pride")
def _(c):
    c.hstripes(["#ff69b4", "#e40303", "#ff8c00", "#ffed00", "#008026", "#40e0d0", "#24408e", "#732982"])


@flag("philadelphia_pride", "Philadelphia Pride", "pride")
def _(c):
    c.hstripes(["#000000", "#784f17"] + RAINBOW)


@flag("progress_pride", "Progress Pride", "pride")
def _(c):
    c.hstripes(RAINBOW)
    slope = 0.5 / 0.2
    for color, depth in (("#000000", 0.48), ("#784f17", 0.41), ("#5bcefa", 0.34), ("#f5a9b8", 0.27), (W_, 0.2)):
        c.poly([(0, 0.5 - slope * depth), (depth, 0.5), (0, 0.5 + slope * depth)], color)


@flag("transgender", "Transgender", "pride")
def _(c):
    c.hstripes(["#5bcefa", "#f5a9b8", W_, "#f5a9b8", "#5bcefa"])


@flag("bisexual", "Bisexual", "pride")
def _(c):
    c.hstripes(["#d60270", "#9b4f96", "#0038a8"], [2, 1, 2])


@flag("pansexual", "Pansexual", "pride")
def _(c):
    c.hstripes(["#ff218c", "#ffd800", "#21b1ff"])


@flag("asexual", "Asexual", "pride")
def _(c):
    c.hstripes([K_, "#a3a3a3", W_, "#800080"])


@flag("aromantic", "Aromantic", "pride")
def _(c):
    c.hstripes(["#3da542", "#a7d379", W_, "#a9a9a9", K_])


@flag("aroace", "Aromantic Asexual", "pride")
def _(c):
    c.hstripes(["#e28c00", "#eccd00", W_, "#62aedc", "#203856"])


@flag("nonbinary", "Nonbinary", "pride")
def _(c):
    c.hstripes(["#fcf434", W_, "#9c59d1", "#2c2c2c"])


@flag("genderfluid", "Genderfluid", "pride")
def _(c):
    c.hstripes(["#ff76a4", W_, "#c011d7", K_, "#2f3cbe"])


@flag("genderqueer", "Genderqueer", "pride")
def _(c):
    c.hstripes(["#b57edc", W_, "#4a8123"])


@flag("agender", "Agender", "pride")
def _(c):
    c.hstripes([K_, "#bcc4c7", W_, "#b7f684", W_, "#bcc4c7", K_])


@flag("lesbian", "Lesbian", "pride")
def _(c):
    c.hstripes(["#d52d00", "#ff9a56", W_, "#d362a4", "#a30262"])


@flag("gay_men", "Gay Men", "pride")
def _(c):
    c.hstripes(["#078d70", "#26ceaa", "#98e8c1", W_, "#7bade2", "#5049cc", "#3d1a78"])


@flag("intersex", "Intersex", "pride")
def _(c):
    c.fill("#ffd800")
    c.ring(0.5, 0.5, 0.22, 0.07, "#7902aa")


@flag("demisexual", "Demisexual", "pride")
def _(c):
    c.hstripes([W_, "#6e0070", "#d2d2d2"], [5, 1, 5])
    c.hoist_triangle(K_, 0.33)


@flag("polysexual", "Polysexual", "pride")
def _(c):
    c.hstripes(["#f714ba", "#01d66a", "#1594f6"])


@flag("omnisexual", "Omnisexual", "pride")
def _(c):
    c.hstripes(["#fe9ace", "#ff53bf", "#200044", "#6760fe", "#8ea6ff"])


@flag("demigirl", "Demigirl", "pride")
def _(c):
    c.hstripes(["#7f7f7f", "#c4c4c4", "#fdadc8", W_, "#fdadc8", "#c4c4c4", "#7f7f7f"])


@flag("demiboy", "Demiboy", "pride")
def _(c):
    c.hstripes(["#7f7f7f", "#c4c4c4", "#9ad9eb", W_, "#9ad9eb", "#c4c4c4", "#7f7f7f"])


@flag("bigender", "Bigender", "pride")
def _(c):
    c.hstripes(["#c479a2", "#eda5cd", "#d6c7e8", W_, "#d6c7e8", "#9ac7e8", "#6d82d1"])


# --------------------------------------------------------------------------- indigenous peoples

@flag("aboriginal_australian", "Australian Aboriginal", "indigenous")
def _(c):
    c.hstripes([K_, "#cc0000"])
    c.disc(0.5, 0.5, 0.25, "#ffff00")


@flag("torres_strait_islander", "Torres Strait Islander", "indigenous")
def _(c):
    c.hstripes(["#00843d", K_, "#0050a0", K_, "#00843d"], [3, 0.5, 8, 0.5, 3])
    c.bitmap(DHARI, 0.5, 0.42, 0.28, W_, aspect=1.1)
    c.star(0.5, 0.66, 0.08, W_)


@flag("maori_tino_rangatiratanga", "Tino Rangatiratanga (Māori)", "indigenous")
def _(c):
    c.hstripes([K_, "#cc0000"])
    c.rect(0.3, 0.47, 1.0, 0.53, W_)
    c.arc(0.25, 0.42, 0.16, 0.06, 0, 300, W_)
    c.disc(0.25, 0.42, 0.06, W_)


@flag("sami", "Sámi", "indigenous")
def _(c):
    c.vstripes(["#d52b1e", "#078930", "#ffce00", "#0035ad"], [13, 2, 2, 18])
    cx = 0.4
    c.arc(cx, 0.5, 0.28, 0.07, 90, 270, "#0035ad")
    c.arc(cx, 0.5, 0.28, 0.07, 270, 450, "#d52b1e")


@flag("wiphala", "Wiphala (Andean peoples)", "indigenous")
def _(c):
    colors = ["#e4002b", "#ff8200", "#ffd100", W_, "#009a44", "#0072ce", "#6d2077"]
    for r in range(7):
        for col in range(7):
            c.rect(col / 7, r / 7, (col + 1) / 7, (r + 1) / 7, colors[(r + col + 4) % 7])


@flag("metis", "Métis", "indigenous")
def _(c):
    c.fill("#0076be")
    off = 0.13 * (2 / 3)
    c.ring(0.5 - off, 0.5, 0.13, 0.055, W_)
    c.ring(0.5 + off, 0.5, 0.13, 0.055, W_)


@flag("haudenosaunee", "Haudenosaunee (Hiawatha Belt)", "indigenous")
def _(c):
    c.fill("#4b2e83")
    c.rect(0.06, 0.48, 0.94, 0.52, W_)
    for x in (0.14, 0.31, 0.69, 0.86):
        c.rect(x - 0.06, 0.38, x + 0.06, 0.62, W_)
        c.rect(x - 0.035, 0.42, x + 0.035, 0.58, "#4b2e83")
    c.bitmap(PINE, 0.5, 0.5, 0.5, W_)


@flag("kanaky", "Kanaky (FLNKS)", "indigenous")
def _(c):
    c.hstripes(["#0047ab", "#e40014", "#009543"])
    c.disc(0.36, 0.5, 0.32, K_)
    c.disc(0.36, 0.5, 0.3, "#ffe000")
    c.bitmap(SPIRE, 0.36, 0.5, 0.48, K_)


@flag("garifuna", "Garifuna", "indigenous")
def _(c):
    c.hstripes(["#fcd116", W_, K_])


@flag("amazigh", "Amazigh (Berber)", "indigenous")
def _(c):
    c.hstripes(["#0072c6", "#3a9d23", "#fcd116"])
    c.bitmap(YAZ, 0.5, 0.5, 0.62, "#e4002b")


# --------------------------------------------------------------------------- peoples

@flag("romani", "Romani", "peoples")
def _(c):
    c.hstripes(["#3d6fb6", "#3f9e2f"])
    c.wheel(0.5, 0.5, 0.28, "#e2001a", spokes=16, t=0.05)


@flag("kurdistan", "Kurdistan", "peoples")
def _(c):
    c.hstripes(["#ed2024", W_, "#278e43"])
    c.sun(0.5, 0.5, 0.14, "#febd11", rays=21, ray_len=1.7)


@flag("sorbian", "Sorbian", "peoples")
def _(c):
    c.hstripes(["#0c4076", "#d52b1e", W_])


@flag("acadian", "Acadian", "peoples")
def _(c):
    c.vstripes(["#002395", W_, "#ed2939"])
    c.star(0.167, 0.3, 0.1, "#fcd116")


@flag("breton", "Breton (Gwenn-ha-Du)", "peoples")
def _(c):
    c.hstripes([K_, W_] * 4 + [K_])
    c.rect(0, 0, 0.42, 5 / 9, W_)
    for row in range(3):
        for col in range(3):
            x = 0.07 + col * 0.14 + (0.07 if row % 2 else 0)
            if x < 0.4:
                c.star(x, 0.1 + row * 0.17, 0.045, K_, points=3, rot=90)


@flag("pan_african", "Pan-African", "peoples")
def _(c):
    c.hstripes(["#e31b23", K_, "#00853f"])


@flag("crimean_tatar", "Crimean Tatar", "peoples")
def _(c):
    c.fill("#00a3dd")
    c.bitmap("""
#...#...#
#...#...#
#########
....#....
....#....
...###...
""", 0.2, 0.2, 0.22, "#fcd116")


@flag("circassian", "Circassian", "peoples")
def _(c):
    c.fill("#1d8f3b")
    for i, (x, y) in enumerate([(0.3, 0.12), (0.4, 0.1), (0.5, 0.09), (0.6, 0.1), (0.7, 0.12),
                                (0.33, 0.24), (0.43, 0.22), (0.57, 0.22), (0.67, 0.24),
                                (0.4, 0.34), (0.5, 0.33), (0.6, 0.34)]):
        c.star(x, y, 0.035, "#fcd116")
    c.line((0.35, 0.85), (0.65, 0.45), "#fcd116", 0.03)
    c.line((0.65, 0.85), (0.35, 0.45), "#fcd116", 0.03)
    c.line((0.5, 0.9), (0.5, 0.42), "#fcd116", 0.03)
