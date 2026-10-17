"""National flags. Coats of arms and seals are simplified to fit a 48x32 texture."""
import emblems as E
from registry import flag

W_, K_ = "#ffffff", "#000000"


def h(fid, name, colors, weights=None):
    flag(fid, name, "countries")(lambda c: c.hstripes(colors, weights))


def v(fid, name, colors, weights=None):
    flag(fid, name, "countries")(lambda c: c.vstripes(colors, weights))


def country(fid, name):
    return flag(fid, name, "countries")


def diagonal_split(c, top_left, bottom_right):
    c.fill(bottom_right)
    c.poly([(0, 0), (1, 0), (0, 1)], top_left)


def diagonal_band(c, color, t, border=None, bt=0.0, rising=True):
    if border:
        c.diagonal(border, t + bt, rising)
    c.diagonal(color, t, rising)


def blue_ensign(c, field="#012169"):
    c.fill(field)
    c.union_jack(0, 0, 0.5, 0.5)


def emblem(c, cx=0.5, cy=0.5, size=0.3, fill="#c8a046", border="#7a5a1a"):
    c.shield(cx, cy, size, fill, border)


# --------------------------------------------------------------------------- simple stripes
h("armenia", "Armenia", ["#d90012", "#0033a0", "#f2a800"])
h("austria", "Austria", ["#c8102e", W_, "#c8102e"])
h("bulgaria", "Bulgaria", [W_, "#00966e", "#d62612"])
h("estonia", "Estonia", ["#0072ce", K_, W_])
h("gabon", "Gabon", ["#009e60", "#fcd116", "#3a75c4"])
h("germany", "Germany", [K_, "#dd0000", "#ffce00"])
h("hungary", "Hungary", ["#cd2a3e", W_, "#436f4d"])
h("indonesia", "Indonesia", ["#ff0000", W_])
h("latvia", "Latvia", ["#9e3039", W_, "#9e3039"], [2, 1, 2])
h("lithuania", "Lithuania", ["#fdb913", "#006a44", "#c1272d"])
h("luxembourg", "Luxembourg", ["#ef3340", W_, "#00a3e0"])
h("mauritius", "Mauritius", ["#ea2839", "#1a206d", "#ffd500", "#00a551"])
h("monaco", "Monaco", ["#ce1126", W_])
h("netherlands", "Netherlands", ["#ae1c28", W_, "#21468b"])
h("poland", "Poland", [W_, "#dc143c"])
h("russia", "Russia", [W_, "#0039a6", "#d52b1e"])
h("sierra_leone", "Sierra Leone", ["#1eb53a", W_, "#0072c6"])
h("thailand", "Thailand", ["#a51931", W_, "#2d2a4a", W_, "#a51931"], [1, 1, 2, 1, 1])
h("ukraine", "Ukraine", ["#0057b7", "#ffd700"])
h("yemen", "Yemen", ["#ce1126", W_, K_])
h("bolivia", "Bolivia", ["#d52b1e", "#f9e300", "#007934"])
h("colombia", "Colombia", ["#fcd116", "#003893", "#ce1126"], [2, 1, 1])
h("botswana", "Botswana", ["#75aadb", W_, K_, W_, "#75aadb"], [9, 1, 4, 1, 9])
h("gambia", "The Gambia", ["#ce1126", W_, "#0c1c8c", W_, "#3a7728"], [6, 1, 4, 1, 6])

v("belgium", "Belgium", [K_, "#fdda24", "#ef3340"])
v("chad", "Chad", ["#002664", "#fecb00", "#c60c30"])
v("cote_divoire", "Côte d'Ivoire", ["#f77f00", W_, "#009e60"])
v("france", "France", ["#002654", W_, "#ce1126"])
v("guinea", "Guinea", ["#ce1126", "#fcd116", "#009460"])
v("ireland", "Ireland", ["#169b62", W_, "#ff883e"])
v("italy", "Italy", ["#009246", W_, "#ce2b37"])
v("mali", "Mali", ["#14b53a", "#fcd116", "#ce1126"])
v("nigeria", "Nigeria", ["#008751", W_, "#008751"])
v("peru", "Peru", ["#d91023", W_, "#d91023"])
v("romania", "Romania", ["#002b7f", "#fcd116", "#ce1126"])


# --------------------------------------------------------------------------- A
@country("afghanistan", "Afghanistan")
def _(c):
    c.vstripes([K_, "#be0000", "#009900"])
    c.ring(0.5, 0.5, 0.2, 0.04, W_)
    c.bitmap(E.TEMPLE, 0.5, 0.5, 0.18, W_)


@country("albania", "Albania")
def _(c):
    c.fill("#e41e20")
    c.bitmap(E.DOUBLE_EAGLE, 0.5, 0.5, 0.75, K_)


@country("algeria", "Algeria")
def _(c):
    c.vstripes(["#006233", W_])
    c.crescent(0.48, 0.5, 0.32, "#d21034", dx=0.3, r2=0.8)
    c.star(0.56, 0.5, 0.13, "#d21034", rot=-90)


@country("andorra", "Andorra")
def _(c):
    c.vstripes(["#10069f", "#fedf00", "#d50032"], [8, 9, 8])
    emblem(c, size=0.32)


@country("angola", "Angola")
def _(c):
    c.hstripes(["#cc092f", K_])
    c.arc(0.5, 0.5, 0.2, 0.06, 120, 400, "#ffcb00")
    c.star(0.47, 0.42, 0.08, "#ffcb00")


@country("antigua_and_barbuda", "Antigua and Barbuda")
def _(c):
    c.fill(K_)
    c.sun(0.5, 0.42, 0.12, "#fcd116", rays=16, ray_len=1.7)
    c.rect(0, 0.45, 1, 0.65, "#0072c6")
    c.rect(0, 0.65, 1, 1, W_)
    c.poly([(0, 0), (0.5, 1), (0, 1)], "#ce1126")
    c.poly([(1, 0), (1, 1), (0.5, 1)], "#ce1126")


@country("argentina", "Argentina")
def _(c):
    c.hstripes(["#74acdf", W_, "#74acdf"])
    c.sun(0.5, 0.5, 0.08, "#f6b40e", rays=16, ray_len=1.8)


@country("australia", "Australia")
def _(c):
    blue_ensign(c)
    c.star(0.25, 0.75, 0.14, W_, points=7)
    for x, y, r in ((0.75, 0.17, 0.065), (0.63, 0.45, 0.065), (0.86, 0.39, 0.065), (0.75, 0.83, 0.07)):
        c.star(x, y, r, W_, points=7)
    c.star(0.8, 0.55, 0.04, W_)


@country("azerbaijan", "Azerbaijan")
def _(c):
    c.hstripes(["#00b5e2", "#ef3340", "#509e2f"])
    c.crescent(0.47, 0.5, 0.12, W_, dx=0.28, r2=0.82)
    c.star(0.54, 0.5, 0.06, W_, points=8)


# --------------------------------------------------------------------------- B
@country("bahamas", "The Bahamas")
def _(c):
    c.hstripes(["#00778b", "#ffc72c", "#00778b"])
    c.hoist_triangle(K_, 0.4)


@country("bahrain", "Bahrain")
def _(c):
    c.fill("#ce1126")
    pts = [(0, 0), (0.25, 0)]
    for i in range(5):
        pts += [(0.37, (i + 0.5) / 5), (0.25, (i + 1) / 5)]
    pts.append((0, 1))
    c.poly(pts, W_)


@country("bangladesh", "Bangladesh")
def _(c):
    c.fill("#006a4e")
    c.disc(0.45, 0.5, 0.3, "#f42a41")


@country("barbados", "Barbados")
def _(c):
    c.vstripes(["#00267f", "#ffc726", "#00267f"])
    c.bitmap(E.TRIDENT, 0.5, 0.5, 0.55, K_)


@country("belarus", "Belarus")
def _(c):
    c.hstripes(["#c8313e", "#4aa657"], [2, 1])
    c.rect(0, 0, 0.11, 1, W_)
    for i in range(6):
        c.poly([(0.055, i / 6), (0.1, i / 6 + 1 / 12), (0.055, (i + 1) / 6), (0.01, i / 6 + 1 / 12)], "#c8313e")


@country("belize", "Belize")
def _(c):
    c.hstripes(["#d90f19", "#003f87", "#d90f19"], [1, 8, 1])
    c.disc(0.5, 0.5, 0.33, W_)
    c.ring(0.5, 0.5, 0.3, 0.05, "#2a7a2a")
    emblem(c, size=0.25, fill="#5a8fd0", border="#d4a017")


@country("benin", "Benin")
def _(c):
    c.hstripes(["#fcd116", "#e8112d"])
    c.rect(0, 0, 0.4, 1, "#008751")


@country("bhutan", "Bhutan")
def _(c):
    diagonal_split(c, "#ffd520", "#ff4e12")
    c.bitmap(E.DRAGON, 0.5, 0.5, 0.6, W_)


@country("bosnia_and_herzegovina", "Bosnia and Herzegovina")
def _(c):
    c.fill("#002395")
    c.poly([(0.27, 0), (0.73, 0), (0.73, 1)], "#fecb00")
    for i in range(7):
        t = (i + 0.5) / 7
        c.star(0.2 + 0.46 * t, 0.02 + 0.96 * t, 0.055, W_)


@country("brazil", "Brazil")
def _(c):
    c.fill("#009c3b")
    c.poly([(0.08, 0.5), (0.5, 0.1), (0.92, 0.5), (0.5, 0.9)], "#ffdf00")
    c.disc(0.5, 0.5, 0.26, "#002776")
    c.arc(0.42, 0.75, 0.35, 0.04, 220, 320, W_)
    for x, y in ((0.45, 0.6), (0.52, 0.65), (0.56, 0.58), (0.5, 0.57), (0.47, 0.68)):
        c.disc(x, y, 0.015, W_)


@country("brunei", "Brunei")
def _(c):
    c.fill("#f7e017")
    c.diagonal(W_, 0.2, rising=False)
    c.line((0, 0.15), (1, 1.15), K_, 0.13)
    c.crescent(0.5, 0.55, 0.15, "#cf1126", dx=0.0, dy=-0.4, r2=0.85)
    c.rect(0.48, 0.25, 0.52, 0.6, "#cf1126")


@country("burkina_faso", "Burkina Faso")
def _(c):
    c.hstripes(["#ef2b2d", "#009e49"])
    c.star(0.5, 0.5, 0.15, "#fcd116")


@country("burundi", "Burundi")
def _(c):
    c.fill("#1eb53a")
    c.poly([(0, 0), (1, 0), (0.5, 0.5)], "#ce1126")
    c.poly([(0, 1), (1, 1), (0.5, 0.5)], "#ce1126")
    c.saltire(W_, 0.14)
    c.disc(0.5, 0.5, 0.28, W_)
    for x, y in ((0.5, 0.38), (0.43, 0.6), (0.57, 0.6)):
        c.star(x, y, 0.07, "#1eb53a", points=6)
        c.star(x, y, 0.055, "#ce1126", points=6)


# --------------------------------------------------------------------------- C
@country("cabo_verde", "Cabo Verde")
def _(c):
    c.hstripes(["#003893", W_, "#cf2027", W_, "#003893"], [6, 1, 1, 1, 3])
    c.stars_circle(0.375, 0.625, 0.25, 10, 0.04, "#f7d116")


@country("cambodia", "Cambodia")
def _(c):
    c.hstripes(["#032ea1", "#e00025", "#032ea1"], [1, 2, 1])
    c.bitmap(E.TEMPLE, 0.5, 0.5, 0.4, W_)


@country("cameroon", "Cameroon")
def _(c):
    c.vstripes(["#007a5e", "#ce1126", "#fcd116"])
    c.star(0.5, 0.5, 0.12, "#fcd116")


@country("canada", "Canada")
def _(c):
    c.vstripes(["#d80621", W_, "#d80621"], [1, 2, 1])
    c.bitmap(E.MAPLE, 0.5, 0.52, 0.66, "#d80621")


@country("central_african_republic", "Central African Republic")
def _(c):
    c.hstripes(["#003082", W_, "#289728", "#ffce00"])
    c.rect(0.4375, 0, 0.5625, 1, "#d21034")
    c.star(0.13, 0.125, 0.09, "#ffce00")


@country("chile", "Chile")
def _(c):
    c.hstripes([W_, "#d52b1e"])
    c.rect(0, 0, 1 / 3, 0.5, "#0039a6")
    c.star(1 / 6, 0.25, 0.12, W_)


@country("china", "China")
def _(c):
    c.fill("#ee1c25")
    c.star(0.167, 0.25, 0.15, "#ffff00")
    for x, y, rot in ((0.333, 0.1, -60), (0.4, 0.2, -80), (0.4, 0.35, -100), (0.333, 0.45, -120)):
        c.star(x, y, 0.05, "#ffff00", rot=rot)


@country("comoros", "Comoros")
def _(c):
    c.hstripes(["#ffd100", W_, "#ef3340", "#003da5"])
    c.hoist_triangle("#009639", 0.4)
    c.crescent(0.13, 0.5, 0.17, W_, dx=0.35, r2=0.85)
    for i in range(4):
        c.star(0.2, 0.32 + i * 0.12, 0.03, W_)


@country("congo_dr", "DR Congo")
def _(c):
    c.fill("#007fff")
    diagonal_band(c, "#ce1021", 0.16, "#f7d618", 0.08)
    c.star(0.17, 0.22, 0.13, "#f7d618")


@country("congo_republic", "Republic of the Congo")
def _(c):
    diagonal_split(c, "#009543", "#dc241f")
    c.diagonal("#fbde4a", 0.4)


@country("costa_rica", "Costa Rica")
def _(c):
    c.hstripes(["#002b7f", W_, "#ce1126", W_, "#002b7f"], [1, 1, 2, 1, 1])


@country("croatia", "Croatia")
def _(c):
    c.hstripes(["#ff0000", W_, "#171796"])
    for row in range(5):
        for col in range(5):
            x0, y0 = 0.42 + col * 0.032, 0.32 + row * 0.07
            c.rect(x0, y0, x0 + 0.032, y0 + 0.07, "#ff0000" if (row + col) % 2 == 0 else W_)


@country("cuba", "Cuba")
def _(c):
    c.hstripes(["#002a8f", W_] * 2 + ["#002a8f"])
    c.hoist_triangle("#cf142b", 0.43)
    c.star(0.14, 0.5, 0.12, W_)


@country("cyprus", "Cyprus")
def _(c):
    c.fill(W_)
    c.poly([(0.25, 0.4), (0.45, 0.33), (0.62, 0.3), (0.78, 0.22), (0.7, 0.36), (0.55, 0.47), (0.35, 0.5)],
           "#d57800")
    c.arc(0.42, 0.55, 0.2, 0.035, 100, 170, "#4e5b31")
    c.arc(0.58, 0.55, 0.2, 0.035, 10, 80, "#4e5b31")


@country("czechia", "Czechia")
def _(c):
    c.hstripes([W_, "#d7141a"])
    c.hoist_triangle("#11457e", 0.5)


# --------------------------------------------------------------------------- D-F
@country("denmark", "Denmark")
def _(c):
    c.fill("#c8102e")
    c.nordic(W_, 0.14, cx=0.36)


@country("djibouti", "Djibouti")
def _(c):
    c.hstripes(["#6ab2e7", "#12ad2b"])
    c.hoist_triangle(W_, 0.42)
    c.star(0.15, 0.5, 0.1, "#d7141a")


@country("dominica", "Dominica")
def _(c):
    c.fill("#006b3f")
    for color, t in (("#fcd116", 0.18), (K_, 0.12), (W_, 0.06)):
        c.cross(color, t)
    c.disc(0.5, 0.5, 0.25, "#d41c30")
    c.stars_circle(0.5, 0.5, 0.2, 10, 0.03, "#009e49")
    c.ellipse(0.5, 0.5, 0.05, 0.1, "#9461c9")


@country("dominican_republic", "Dominican Republic")
def _(c):
    c.fill(W_)
    c.rect(0, 0, 0.5, 0.5, "#002d62")
    c.rect(0.5, 0, 1, 0.5, "#ce1126")
    c.rect(0, 0.5, 0.5, 1, "#ce1126")
    c.rect(0.5, 0.5, 1, 1, "#002d62")
    c.cross(W_, 0.18)
    c.shield(0.5, 0.5, 0.15, "#002d62", "#2e7d32")


@country("ecuador", "Ecuador")
def _(c):
    c.hstripes(["#ffdd00", "#034ea2", "#ed1c24"], [2, 1, 1])
    c.bitmap(E.EAGLE, 0.5, 0.42, 0.3, "#5a3d1a")
    c.disc(0.5, 0.52, 0.08, "#4aa3df")


@country("egypt", "Egypt")
def _(c):
    c.hstripes(["#ce1126", W_, K_])
    c.bitmap(E.EAGLE, 0.5, 0.5, 0.28, "#c09300")


@country("el_salvador", "El Salvador")
def _(c):
    c.hstripes(["#0f47af", W_, "#0f47af"])
    c.poly([(0.5, 0.38), (0.56, 0.6), (0.44, 0.6)], "#2e7d32")
    c.ring(0.5, 0.5, 0.12, 0.025, "#c8a046")


@country("equatorial_guinea", "Equatorial Guinea")
def _(c):
    c.hstripes(["#3e9a00", W_, "#e32118"])
    c.hoist_triangle("#0073ce", 0.25)
    c.shield(0.55, 0.5, 0.2, "#c0c0c0", "#3e9a00")


@country("eritrea", "Eritrea")
def _(c):
    c.fill("#12ad2b")
    c.poly([(0, 1), (1, 0.5), (1, 1)], "#4189dd")
    c.poly([(0, 0), (1, 0.5), (0, 1)], "#ea0437")
    c.ring(0.22, 0.5, 0.17, 0.035, "#ffc726")
    c.rect(0.215, 0.38, 0.225, 0.64, "#ffc726")


@country("eswatini", "Eswatini")
def _(c):
    c.hstripes(["#3e5eb9", "#ffd900", "#b10c0c", "#ffd900", "#3e5eb9"], [3, 1, 8, 1, 3])
    c.ellipse(0.5, 0.5, 0.3, 0.13, K_)
    c.pieslice(0.5, 0.5, 0.13, 270, 450, W_)
    c.line((0.12, 0.5), (0.88, 0.5), "#ffd900", 0.02)


@country("ethiopia", "Ethiopia")
def _(c):
    c.hstripes(["#078930", "#fcdd09", "#da121a"])
    c.disc(0.5, 0.5, 0.27, "#0f47af")
    c.star(0.5, 0.5, 0.2, "#fcdd09", inner=0.5)
    c.star(0.5, 0.5, 0.11, "#0f47af", inner=0.5)


@country("fiji", "Fiji")
def _(c):
    blue_ensign(c, "#68bfe5")
    c.shield(0.75, 0.5, 0.42, W_, "#ce1126")
    c.cross("#ce1126", 0.04, cx=0.75, cy=0.5)


@country("finland", "Finland")
def _(c):
    c.fill(W_)
    c.nordic("#002f6c", 0.27, cx=0.36)


# --------------------------------------------------------------------------- G-H
@country("georgia", "Georgia")
def _(c):
    c.fill(W_)
    c.cross("#ff0000", 0.2)
    for x, y in ((0.22, 0.22), (0.78, 0.22), (0.22, 0.78), (0.78, 0.78)):
        c.rect(x - 0.015, y - 0.1, x + 0.015, y + 0.1, "#ff0000")
        c.rect(x - 0.065, y - 0.03, x + 0.065, y + 0.03, "#ff0000")


@country("ghana", "Ghana")
def _(c):
    c.hstripes(["#ce1126", "#fcd116", "#006b3f"])
    c.star(0.5, 0.5, 0.16, K_)


@country("greece", "Greece")
def _(c):
    c.hstripes(["#0d5eaf", W_] * 4 + ["#0d5eaf"])
    side = 5 / 9
    c.rect(0, 0, side * 2 / 3, side, "#0d5eaf")
    c.rect(side / 3 - 0.04, 0, side / 3 + 0.04, side, W_)
    c.rect(0, side / 2 - 1 / 18, side * 2 / 3, side / 2 + 1 / 18, W_)


@country("grenada", "Grenada")
def _(c):
    c.fill("#ce1126")
    x0, y0, x1, y1 = 0.083, 0.125, 0.917, 0.875
    c.rect(x0, y0, x1, y1, "#007a5e")
    c.poly([(x0, y0), (x1, y0), (0.5, 0.5)], "#fcd116")
    c.poly([(x0, y1), (x1, y1), (0.5, 0.5)], "#fcd116")
    c.disc(0.5, 0.5, 0.13, "#ce1126")
    c.star(0.5, 0.5, 0.09, "#fcd116")
    for x in (0.25, 0.5, 0.75):
        c.star(x, 0.0625, 0.045, "#fcd116")
        c.star(x, 0.9375, 0.045, "#fcd116")
    c.ellipse(0.2, 0.5, 0.05, 0.08, "#fcd116")


@country("guatemala", "Guatemala")
def _(c):
    c.vstripes(["#4997d0", W_, "#4997d0"])
    c.ring(0.5, 0.5, 0.15, 0.03, "#5a8a2a")
    c.bitmap(E.BIRD, 0.5, 0.45, 0.12, "#2e7d32")


@country("guinea_bissau", "Guinea-Bissau")
def _(c):
    c.hstripes(["#fcd116", "#009e49"])
    c.rect(0, 0, 1 / 3, 1, "#ce1126")
    c.star(1 / 6, 0.5, 0.13, K_)


@country("guyana", "Guyana")
def _(c):
    c.fill("#009e49")
    c.poly([(0, 0), (1, 0.5), (0, 1)], W_)
    c.poly([(0, 0.04), (0.94, 0.5), (0, 0.96)], "#fcd116")
    c.poly([(0, 0), (0.5, 0.5), (0, 1)], K_)
    c.poly([(0, 0.05), (0.45, 0.5), (0, 0.95)], "#ce1126")


@country("haiti", "Haiti")
def _(c):
    c.hstripes(["#00209f", "#d21034"])
    c.rect(0.36, 0.33, 0.64, 0.67, W_)
    c.bitmap(E.PALMETTO, 0.5, 0.5, 0.28, "#016a16")


@country("honduras", "Honduras")
def _(c):
    c.hstripes(["#18c3df", W_, "#18c3df"])
    for x, y in ((0.5, 0.5), (0.4, 0.42), (0.6, 0.42), (0.4, 0.58), (0.6, 0.58)):
        c.star(x, y, 0.05, "#18c3df")


# --------------------------------------------------------------------------- I-K
@country("iceland", "Iceland")
def _(c):
    c.fill("#02529c")
    c.nordic_bordered(W_, "#dc1e35", 0.22, 0.11, cx=0.36)


@country("india", "India")
def _(c):
    c.hstripes(["#ff9933", W_, "#138808"])
    c.wheel(0.5, 0.5, 0.14, "#000080", spokes=24, t=0.025)


@country("iran", "Iran")
def _(c):
    c.hstripes(["#239f40", W_, "#da0000"])
    c.bitmap(E.TRIDENT, 0.5, 0.5, 0.28, "#da0000")


@country("iraq", "Iraq")
def _(c):
    c.hstripes(["#ce1126", W_, K_])
    for x in (0.3, 0.4, 0.5, 0.6, 0.7):
        c.rect(x - 0.02, 0.4, x + 0.02, 0.6, "#007a3d")
    c.rect(0.28, 0.56, 0.72, 0.6, "#007a3d")


@country("israel", "Israel")
def _(c):
    c.fill(W_)
    c.rect(0, 0.1, 1, 0.25, "#0038b8")
    c.rect(0, 0.75, 1, 0.9, "#0038b8")
    r = 0.17
    k = 2 / 3
    c.outline_poly([(0.5, 0.5 - r), (0.5 + r * 0.866 * k, 0.5 + r / 2), (0.5 - r * 0.866 * k, 0.5 + r / 2)],
                   "#0038b8", 0.035)
    c.outline_poly([(0.5, 0.5 + r), (0.5 + r * 0.866 * k, 0.5 - r / 2), (0.5 - r * 0.866 * k, 0.5 - r / 2)],
                   "#0038b8", 0.035)


@country("jamaica", "Jamaica")
def _(c):
    c.fill(K_)
    c.poly([(0, 0), (1, 0), (0.5, 0.5)], "#009b3a")
    c.poly([(0, 1), (1, 1), (0.5, 0.5)], "#009b3a")
    c.saltire("#fed100", 0.16)


@country("japan", "Japan")
def _(c):
    c.fill(W_)
    c.disc(0.5, 0.5, 0.3, "#bc002d")


@country("jordan", "Jordan")
def _(c):
    c.hstripes([K_, W_, "#007a3d"])
    c.hoist_triangle("#ce1126", 0.5)
    c.star(0.17, 0.5, 0.08, W_, points=7)


@country("kazakhstan", "Kazakhstan")
def _(c):
    c.fill("#00afca")
    c.sun(0.55, 0.42, 0.13, "#fec50c", rays=32, ray_len=1.5)
    c.bitmap(E.BIRD, 0.55, 0.68, 0.16, "#fec50c")
    for i in range(8):
        c.rect(0.04, i / 8 + 0.02, 0.08, i / 8 + 0.1, "#fec50c")


@country("kenya", "Kenya")
def _(c):
    c.hstripes([K_, W_, "#bb0000", W_, "#006600"], [6, 1, 6, 1, 6])
    c.line((0.4, 0.8), (0.6, 0.2), W_, 0.03)
    c.line((0.6, 0.8), (0.4, 0.2), W_, 0.03)
    c.ellipse(0.5, 0.5, 0.11, 0.3, "#bb0000")
    c.ellipse(0.5, 0.25, 0.06, 0.07, K_)
    c.ellipse(0.5, 0.75, 0.06, 0.07, K_)
    c.ellipse(0.5, 0.5, 0.03, 0.12, W_)


@country("kiribati", "Kiribati")
def _(c):
    c.fill("#ce1126")
    c.sun(0.5, 0.55, 0.12, "#fcd116", rays=17, ray_len=1.9)
    c.bitmap(E.BIRD, 0.5, 0.25, 0.14, "#fcd116")
    c.hstripes(["#003f87", W_, "#003f87", W_, "#003f87", W_], y0=0.55)


@country("kosovo", "Kosovo")
def _(c):
    c.fill("#244aa5")
    c.poly([(0.36, 0.45), (0.45, 0.33), (0.6, 0.35), (0.66, 0.5), (0.58, 0.75), (0.45, 0.72)], "#d0a650")
    for i in range(6):
        c.star(0.3 + i * 0.08, 0.22 - 0.04 * (1 - abs(i - 2.5) / 2.5), 0.04, W_)


@country("kuwait", "Kuwait")
def _(c):
    c.hstripes(["#007a3d", W_, "#ce1126"])
    c.poly([(0, 0), (0.25, 1 / 3), (0.25, 2 / 3), (0, 1)], K_)


@country("kyrgyzstan", "Kyrgyzstan")
def _(c):
    c.fill("#e8112d")
    c.sun(0.5, 0.5, 0.2, "#ffef00", rays=40, ray_len=1.5, ray_w=0.6)
    c.disc(0.5, 0.5, 0.12, "#e8112d")
    c.ring(0.5, 0.5, 0.12, 0.025, "#ffef00")
    c.arc(0.5, 0.62, 0.12, 0.02, 200, 340, "#ffef00")


# --------------------------------------------------------------------------- L-M
@country("laos", "Laos")
def _(c):
    c.hstripes(["#ce1126", "#002868", "#ce1126"], [1, 2, 1])
    c.disc(0.5, 0.5, 0.2, W_)


@country("lebanon", "Lebanon")
def _(c):
    c.hstripes(["#ee161f", W_, "#ee161f"], [1, 2, 1])
    c.bitmap(E.CEDAR, 0.5, 0.5, 0.46, "#00a651")


@country("lesotho", "Lesotho")
def _(c):
    c.hstripes(["#00209f", W_, "#009543"], [3, 4, 3])
    c.bitmap(E.HAT, 0.5, 0.48, 0.3, K_)


@country("liberia", "Liberia")
def _(c):
    c.hstripes(["#bf0a30", W_] * 5 + ["#bf0a30"])
    c.rect(0, 0, 5 / 11 * 2 / 3, 5 / 11, "#002868")
    c.star(5 / 11 / 3, 2.5 / 11, 0.13, W_)


@country("libya", "Libya")
def _(c):
    c.hstripes(["#e70013", K_, "#239e46"], [1, 2, 1])
    c.crescent(0.48, 0.5, 0.13, W_, dx=0.3, r2=0.8)
    c.star(0.56, 0.5, 0.06, W_)


@country("liechtenstein", "Liechtenstein")
def _(c):
    c.hstripes(["#002b7f", "#ce1126"])
    c.bitmap(E.CROWN, 0.25, 0.25, 0.2, "#ffd83d")


@country("madagascar", "Madagascar")
def _(c):
    c.hstripes(["#fc3d32", "#007e3a"])
    c.rect(0, 0, 1 / 3, 1, W_)


@country("malawi", "Malawi")
def _(c):
    c.hstripes([K_, "#ce1126", "#339e35"])
    c.sun(0.5, 0.33, 0.1, "#ce1126", rays=31, ray_len=1.6)
    c.rect(0, 1 / 3, 1, 2 / 3, "#ce1126")


@country("malaysia", "Malaysia")
def _(c):
    c.hstripes(["#cc0001", W_] * 7)
    c.rect(0, 0, 0.5, 8 / 14, "#010066")
    c.crescent(0.2, 0.29, 0.2, "#ffcc00", dx=0.3, r2=0.8)
    c.star(0.33, 0.29, 0.13, "#ffcc00", points=14, inner=0.45)


@country("maldives", "Maldives")
def _(c):
    c.fill("#d21034")
    c.rect(0.25, 0.25, 0.75, 0.75, "#007e3a")
    c.crescent(0.52, 0.5, 0.17, W_, dx=0.35, r2=0.82)


@country("malta", "Malta")
def _(c):
    c.vstripes([W_, "#cf142b"])
    c.rect(0.08, 0.1, 0.12, 0.26, "#8a8a8a")
    c.rect(0.04, 0.16, 0.16, 0.2, "#8a8a8a")


@country("marshall_islands", "Marshall Islands")
def _(c):
    c.fill("#003893")
    c.poly([(0, 1), (1, 0), (1, 0.1), (0, 1.0)], "#dd7500")
    c.poly([(0, 1), (1, 0.1), (1, 0.2)], W_)
    c.star(0.2, 0.25, 0.14, W_, points=24, inner=0.5)


@country("mauritania", "Mauritania")
def _(c):
    c.hstripes(["#d01c1f", "#00a95c", "#d01c1f"], [1, 6, 1])
    c.crescent(0.5, 0.48, 0.22, "#ffd700", dx=0.0, dy=-0.35, r2=0.85)
    c.star(0.5, 0.35, 0.08, "#ffd700")


@country("mexico", "Mexico")
def _(c):
    c.vstripes(["#006847", W_, "#ce1126"])
    c.bitmap(E.EAGLE, 0.5, 0.47, 0.3, "#7a4a1d")
    c.arc(0.5, 0.5, 0.16, 0.03, 30, 150, "#3c8a2e")


@country("micronesia", "Micronesia")
def _(c):
    c.fill("#75b2dd")
    for x, y in ((0.5, 0.25), (0.5, 0.75), (0.33, 0.5), (0.67, 0.5)):
        c.star(x, y, 0.09, W_)


@country("moldova", "Moldova")
def _(c):
    c.vstripes(["#0046ae", "#ffd200", "#cc092f"])
    c.bitmap(E.EAGLE, 0.5, 0.5, 0.4, "#b07e3e")


@country("mongolia", "Mongolia")
def _(c):
    c.vstripes(["#c4272f", "#015197", "#c4272f"])
    c.disc(1 / 6, 0.32, 0.05, "#f9cf02")
    c.crescent(1 / 6, 0.4, 0.06, "#f9cf02", dx=0.0, dy=-0.5, r2=0.8)
    c.rect(1 / 6 - 0.05, 0.47, 1 / 6 + 0.05, 0.5, "#f9cf02")
    c.disc(1 / 6, 0.62, 0.07, "#f9cf02")
    c.rect(0.07, 0.45, 0.09, 0.82, "#f9cf02")
    c.rect(0.243, 0.45, 0.263, 0.82, "#f9cf02")


@country("montenegro", "Montenegro")
def _(c):
    c.fill("#d3ae3b")
    c.rect(0.04, 0.06, 0.96, 0.94, "#c40308")
    c.bitmap(E.DOUBLE_EAGLE, 0.5, 0.5, 0.6, "#d3ae3b")


@country("morocco", "Morocco")
def _(c):
    c.fill("#c1272d")
    r, k = 0.27, 2 / 3
    pts = []
    for i in range(5):
        import math
        a = math.radians(-90 + i * 144)
        pts.append((0.5 + r * math.cos(a) * k, 0.5 + r * math.sin(a)))
    c.outline_poly(pts, "#006233", 0.04)


@country("mozambique", "Mozambique")
def _(c):
    c.hstripes(["#007168", W_, K_, W_, "#fce100"], [6, 1, 6, 1, 6])
    c.hoist_triangle("#d21034", 0.45)
    c.star(0.15, 0.5, 0.18, "#fce100")
    c.rect(0.11, 0.48, 0.19, 0.56, W_)


@country("myanmar", "Myanmar")
def _(c):
    c.hstripes(["#fecb00", "#34b233", "#ea2839"])
    c.star(0.5, 0.55, 0.36, W_)


# --------------------------------------------------------------------------- N-P
@country("namibia", "Namibia")
def _(c):
    diagonal_split(c, "#003580", "#009543")
    diagonal_band(c, "#d21034", 0.22, W_, 0.08)
    c.sun(0.18, 0.25, 0.07, "#ffce00", rays=12, ray_len=1.8)


@country("nauru", "Nauru")
def _(c):
    c.fill("#002b7f")
    c.rect(0, 0.46, 1, 0.54, "#ffc61e")
    c.star(0.25, 0.72, 0.12, W_, points=12, inner=0.55)


@country("nepal", "Nepal")
def _(c):
    outer = [(0.12, 0.0), (0.66, 0.48), (0.36, 0.48), (0.66, 1.0), (0.12, 1.0)]
    c.poly(outer, "#003893")
    c.poly([(0.15, 0.06), (0.57, 0.44), (0.29, 0.44), (0.58, 0.95), (0.15, 0.95)], "#dc143c")
    c.crescent(0.27, 0.27, 0.08, W_, dx=0.0, dy=-0.4, r2=0.8)
    c.sun(0.27, 0.72, 0.06, W_, rays=12, ray_len=1.5)
    c.keep(outer)


@country("new_zealand", "New Zealand")
def _(c):
    blue_ensign(c)
    for x, y, r in ((0.75, 0.2, 0.07), (0.63, 0.46, 0.065), (0.85, 0.4, 0.06), (0.75, 0.8, 0.075)):
        c.star(x, y, r + 0.02, W_)
        c.star(x, y, r, "#c8102e")


@country("nicaragua", "Nicaragua")
def _(c):
    c.hstripes(["#0067c6", W_, "#0067c6"])
    c.poly([(0.5, 0.38), (0.57, 0.6), (0.43, 0.6)], "#4aa3df")
    c.ring(0.5, 0.52, 0.11, 0.02, "#c8a046")


@country("niger", "Niger")
def _(c):
    c.hstripes(["#e05206", W_, "#0db02b"])
    c.disc(0.5, 0.5, 0.12, "#e05206")


@country("north_korea", "North Korea")
def _(c):
    c.hstripes(["#024fa2", W_, "#ed1c27", W_, "#024fa2"], [6, 1, 18, 1, 6])
    c.disc(0.36, 0.5, 0.25, W_)
    c.star(0.36, 0.5, 0.23, "#ed1c27")


@country("north_macedonia", "North Macedonia")
def _(c):
    c.fill("#d20000")
    for i in range(8):
        import math
        a = math.radians(i * 45 + 22.5)
        b = math.radians(i * 45 - 22.5 + 45)
        c.poly([(0.5, 0.5), (0.5 + 1.2 * math.cos(a - 0.15), 0.5 + 1.8 * math.sin(a - 0.15)),
                (0.5 + 1.2 * math.cos(a + 0.15), 0.5 + 1.8 * math.sin(a + 0.15))], "#ffe600")
    c.disc(0.5, 0.5, 0.17, "#d20000")
    c.disc(0.5, 0.5, 0.14, "#ffe600")


@country("norway", "Norway")
def _(c):
    c.fill("#ba0c2f")
    c.nordic_bordered(W_, "#00205b", 0.25, 0.125, cx=0.36)


@country("oman", "Oman")
def _(c):
    c.hstripes([W_, "#db161b", "#008000"])
    c.rect(0, 0, 0.32, 1, "#db161b")
    c.bitmap(E.KEYS, 0.12, 0.18, 0.22, W_)


@country("pakistan", "Pakistan")
def _(c):
    c.fill("#01411c")
    c.rect(0, 0, 0.25, 1, W_)
    c.crescent(0.64, 0.52, 0.27, W_, dx=0.25, dy=-0.25, r2=0.82)
    c.star(0.72, 0.38, 0.09, W_, rot=-60)


@country("palau", "Palau")
def _(c):
    c.fill("#4aadd6")
    c.disc(0.45, 0.5, 0.3, "#ffde00")


@country("palestine", "Palestine")
def _(c):
    c.hstripes([K_, W_, "#007a3d"])
    c.hoist_triangle("#ce1126", 0.33)


@country("panama", "Panama")
def _(c):
    c.fill(W_)
    c.rect(0.5, 0, 1, 0.5, "#da121a")
    c.rect(0, 0.5, 0.5, 1, "#072357")
    c.star(0.25, 0.25, 0.1, "#072357")
    c.star(0.75, 0.75, 0.1, "#da121a")


@country("papua_new_guinea", "Papua New Guinea")
def _(c):
    c.fill(K_)
    c.poly([(0, 0), (1, 0), (1, 1)], "#ce1126")
    for x, y in ((0.25, 0.42), (0.18, 0.6), (0.32, 0.58), (0.25, 0.82), (0.28, 0.68)):
        c.star(x, y, 0.04, W_)
    c.bitmap(E.BIRD, 0.7, 0.3, 0.22, "#fcd116")


@country("paraguay", "Paraguay")
def _(c):
    c.hstripes(["#d52b1e", W_, "#0038a8"])
    c.ring(0.5, 0.5, 0.11, 0.025, "#2e7d32")
    c.star(0.5, 0.5, 0.05, "#fcd116")


@country("philippines", "Philippines")
def _(c):
    c.hstripes(["#0038a8", "#ce1126"])
    c.hoist_triangle(W_, 0.43)
    c.sun(0.15, 0.5, 0.07, "#fcd116", rays=8, ray_len=1.9)
    for x, y in ((0.04, 0.12), (0.04, 0.88), (0.37, 0.5)):
        c.star(x, y, 0.045, "#fcd116")


@country("portugal", "Portugal")
def _(c):
    c.vstripes(["#006600", "#ff0000"], [2, 3])
    c.ring(0.4, 0.5, 0.2, 0.04, "#ffe000")
    c.shield(0.4, 0.5, 0.26, W_, "#ff0000")
    c.disc(0.4, 0.5, 0.04, "#003399")


# --------------------------------------------------------------------------- Q-S
@country("qatar", "Qatar")
def _(c):
    c.fill("#8d1b3d")
    pts = [(0, 0), (0.25, 0)]
    for i in range(9):
        pts += [(0.36, (i + 0.5) / 9), (0.25, (i + 1) / 9)]
    pts.append((0, 1))
    c.poly(pts, W_)


@country("rwanda", "Rwanda")
def _(c):
    c.hstripes(["#00a1de", "#fad201", "#20603d"], [2, 1, 1])
    c.sun(0.83, 0.25, 0.07, "#e5be01", rays=24, ray_len=1.8)


@country("saint_kitts_and_nevis", "Saint Kitts and Nevis")
def _(c):
    diagonal_split(c, "#009e49", "#ce1126")
    diagonal_band(c, K_, 0.28, "#fcd116", 0.12)
    c.star(0.38, 0.63, 0.07, W_)
    c.star(0.62, 0.37, 0.07, W_)


@country("saint_lucia", "Saint Lucia")
def _(c):
    c.fill("#66ccff")
    c.poly([(0.5, 0.12), (0.7, 0.88), (0.3, 0.88)], W_)
    c.poly([(0.5, 0.18), (0.66, 0.88), (0.34, 0.88)], K_)
    c.poly([(0.5, 0.5), (0.68, 0.88), (0.32, 0.88)], "#fcd116")


@country("saint_vincent", "Saint Vincent and the Grenadines")
def _(c):
    c.vstripes(["#002674", "#fcd116", "#009e60"], [1, 2, 1])
    for x, y in ((0.42, 0.4), (0.58, 0.4), (0.5, 0.62)):
        c.poly([(x, y - 0.12), (x + 0.05, y), (x, y + 0.12), (x - 0.05, y)], "#009e60")


@country("samoa", "Samoa")
def _(c):
    c.fill("#ce1126")
    c.rect(0, 0, 0.5, 0.5, "#002b7f")
    for x, y, r in ((0.25, 0.1, 0.05), (0.17, 0.25, 0.05), (0.33, 0.22, 0.05), (0.25, 0.4, 0.055),
                    (0.29, 0.3, 0.03)):
        c.star(x, y, r, W_)


@country("san_marino", "San Marino")
def _(c):
    c.hstripes([W_, "#5eb6e4"])
    c.shield(0.5, 0.5, 0.35, "#5eb6e4", "#c8a046")
    c.bitmap(E.CASTLE, 0.5, 0.48, 0.16, W_)


@country("sao_tome_and_principe", "São Tomé and Príncipe")
def _(c):
    c.hstripes(["#12ad2b", "#ffce00", "#12ad2b"], [2, 3, 2])
    c.hoist_triangle("#d21034", 0.25)
    c.star(0.5, 0.5, 0.1, K_)
    c.star(0.75, 0.5, 0.1, K_)


@country("saudi_arabia", "Saudi Arabia")
def _(c):
    c.fill("#006c35")
    for x in (0.25, 0.32, 0.4, 0.47, 0.55, 0.62, 0.7):
        c.rect(x, 0.25, x + 0.035, 0.42, W_)
    c.rect(0.22, 0.42, 0.78, 0.46, W_)
    c.rect(0.25, 0.62, 0.75, 0.66, W_)
    c.rect(0.25, 0.6, 0.29, 0.68, W_)


@country("senegal", "Senegal")
def _(c):
    c.vstripes(["#00853f", "#fdef42", "#e31b23"])
    c.star(0.5, 0.5, 0.12, "#00853f")


@country("serbia", "Serbia")
def _(c):
    c.hstripes(["#c6363c", "#0c4076", W_])
    c.shield(0.35, 0.47, 0.42, "#c6363c", "#edb92e")
    c.bitmap(E.DOUBLE_EAGLE, 0.35, 0.45, 0.3, W_)


@country("seychelles", "Seychelles")
def _(c):
    c.poly([(0, 1), (0, 0), (1 / 3, 0)], "#003f87")
    c.poly([(0, 1), (1 / 3, 0), (2 / 3, 0)], "#fcd856")
    c.poly([(0, 1), (2 / 3, 0), (1, 0), (1, 1 / 3)], "#d62828")
    c.poly([(0, 1), (1, 1 / 3), (1, 2 / 3)], W_)
    c.poly([(0, 1), (1, 2 / 3), (1, 1)], "#007a3d")


@country("singapore", "Singapore")
def _(c):
    c.hstripes(["#ef3340", W_])
    c.crescent(0.17, 0.25, 0.17, W_, dx=0.33, r2=0.85)
    for i in range(5):
        import math
        a = math.radians(-90 + i * 72)
        c.star(0.27 + 0.065 * math.cos(a) * 2 / 3, 0.25 + 0.085 * math.sin(a), 0.035, W_)


@country("slovakia", "Slovakia")
def _(c):
    c.hstripes([W_, "#0b4ea2", "#ee1c25"])
    c.shield(0.33, 0.5, 0.5, "#ee1c25", W_)
    c.rect(0.325, 0.33, 0.345, 0.6, W_)
    c.rect(0.3, 0.38, 0.37, 0.41, W_)
    c.rect(0.29, 0.46, 0.38, 0.49, W_)
    c.disc(0.335, 0.64, 0.06, "#0b4ea2")


@country("slovenia", "Slovenia")
def _(c):
    c.hstripes([W_, "#005da4", "#ed1c24"])
    c.shield(0.27, 0.33, 0.3, "#005da4", "#ed1c24")
    c.poly([(0.22, 0.4), (0.27, 0.3), (0.32, 0.4)], W_)
    for x in (0.25, 0.27, 0.29):
        c.star(x, 0.24, 0.02, "#ffdd00", points=6)


@country("solomon_islands", "Solomon Islands")
def _(c):
    diagonal_split(c, "#0051ba", "#215b33")
    c.diagonal("#fcd116", 0.07)
    for x, y in ((0.1, 0.12), (0.3, 0.12), (0.2, 0.25), (0.1, 0.38), (0.3, 0.38)):
        c.star(x, y, 0.05, W_)


@country("somalia", "Somalia")
def _(c):
    c.fill("#4189dd")
    c.star(0.5, 0.5, 0.2, W_)


@country("south_africa", "South Africa")
def _(c):
    c.hstripes(["#e03c31", "#001489"])
    for color, t in ((W_, 0.333), ("#007749", 0.2)):
        c.line((0, 0), (0.36, 0.5), color, t)
        c.line((0, 1), (0.36, 0.5), color, t)
        c.rect(0.33, 0.5 - t / 2, 1, 0.5 + t / 2, color)
    c.poly([(0, 0.15), (0.28, 0.5), (0, 0.85)], "#ffb81c")
    c.poly([(0, 0.24), (0.21, 0.5), (0, 0.76)], K_)


@country("south_korea", "South Korea")
def _(c):
    c.fill(W_)
    c.disc(0.5, 0.5, 0.25, "#cd2e3a")
    c.pieslice(0.5, 0.5, 0.25, 0, 180, "#0047a0")
    c.disc(0.5 - 0.125 * 2 / 3, 0.5, 0.125, "#0047a0")
    c.disc(0.5 + 0.125 * 2 / 3, 0.5, 0.125, "#cd2e3a")
    for x, y in ((0.2, 0.22), (0.8, 0.22), (0.2, 0.78), (0.8, 0.78)):
        for i in range(3):
            c.rect(x - 0.05, y - 0.08 + i * 0.06, x + 0.05, y - 0.05 + i * 0.06, K_)


@country("south_sudan", "South Sudan")
def _(c):
    c.hstripes([K_, W_, "#da121a", W_, "#078930"], [6, 1, 6, 1, 6])
    c.hoist_triangle("#0f47af", 0.4)
    c.star(0.13, 0.5, 0.12, "#fcdd09")


@country("spain", "Spain")
def _(c):
    c.hstripes(["#aa151b", "#f1bf00", "#aa151b"], [1, 2, 1])
    c.shield(0.3, 0.5, 0.3, "#aa151b", "#c8a046")
    c.bitmap(E.CROWN, 0.3, 0.3, 0.08, "#c8a046")


@country("sri_lanka", "Sri Lanka")
def _(c):
    c.fill("#ffbe29")
    c.rect(0.04, 0.06, 0.16, 0.94, "#00534e")
    c.rect(0.16, 0.06, 0.28, 0.94, "#eb7400")
    c.rect(0.31, 0.06, 0.96, 0.94, "#8d153a")
    c.bitmap(E.LION, 0.63, 0.5, 0.6, "#ffbe29")


@country("sudan", "Sudan")
def _(c):
    c.hstripes(["#d21034", W_, K_])
    c.hoist_triangle("#007229", 0.33)


@country("suriname", "Suriname")
def _(c):
    c.hstripes(["#377e3f", W_, "#b40a2d", W_, "#377e3f"], [2, 1, 4, 1, 2])
    c.star(0.5, 0.5, 0.17, "#ecc81d")


@country("sweden", "Sweden")
def _(c):
    c.fill("#006aa7")
    c.nordic("#fecc02", 0.2, cx=0.375)


@country("switzerland", "Switzerland")
def _(c):
    s = 2 / 3
    c.rect(0, 0, s, 1, "#da291c")
    c.rect(s / 2 - s * 3 / 32, 0.1875, s / 2 + s * 3 / 32, 0.8125, W_)
    c.rect(s * 6 / 32, 0.5 - 3 / 32, s * 26 / 32, 0.5 + 3 / 32, W_)


@country("syria", "Syria")
def _(c):
    c.hstripes(["#007a3d", W_, K_])
    for x in (0.3, 0.5, 0.7):
        c.star(x, 0.5, 0.1, "#ce1126")


# --------------------------------------------------------------------------- T-Z
@country("taiwan", "Taiwan")
def _(c):
    c.fill("#fe0000")
    c.rect(0, 0, 0.5, 0.5, "#000095")
    c.sun(0.25, 0.25, 0.09, W_, rays=12, ray_len=1.8)
    c.disc(0.25, 0.25, 0.08, "#000095")
    c.disc(0.25, 0.25, 0.065, W_)


@country("tajikistan", "Tajikistan")
def _(c):
    c.hstripes(["#cc0000", W_, "#006600"], [2, 3, 2])
    c.bitmap(E.CROWN, 0.5, 0.52, 0.12, "#f8c300")
    for i in range(7):
        import math
        a = math.radians(200 + i * 140 / 6)
        c.star(0.5 + 0.2 * math.cos(a) * 2 / 3, 0.53 + 0.2 * math.sin(a), 0.03, "#f8c300")


@country("tanzania", "Tanzania")
def _(c):
    diagonal_split(c, "#1eb53a", "#00a3dd")
    diagonal_band(c, K_, 0.28, "#fcd116", 0.12)


@country("timor_leste", "Timor-Leste")
def _(c):
    c.fill("#dc241f")
    c.hoist_triangle("#ffc726", 0.5)
    c.hoist_triangle(K_, 0.33)
    c.star(0.11, 0.5, 0.11, W_, rot=-60)


@country("togo", "Togo")
def _(c):
    c.hstripes(["#006a4e", "#ffce00"] * 2 + ["#006a4e"])
    c.rect(0, 0, 0.4, 0.6, "#d21034")
    c.star(0.2, 0.3, 0.17, W_)


@country("tonga", "Tonga")
def _(c):
    c.fill("#c10000")
    c.rect(0, 0, 0.42, 0.5, W_)
    c.rect(0.18, 0.08, 0.24, 0.42, "#c10000")
    c.rect(0.1, 0.22, 0.32, 0.29, "#c10000")


@country("trinidad_and_tobago", "Trinidad and Tobago")
def _(c):
    c.fill("#ce1126")
    c.diagonal(W_, 0.45, rising=False)
    c.diagonal(K_, 0.33, rising=False)


@country("tunisia", "Tunisia")
def _(c):
    c.fill("#e70013")
    c.disc(0.5, 0.5, 0.25, W_)
    c.crescent(0.5, 0.5, 0.19, "#e70013", dx=0.25, r2=0.8)
    c.star(0.54, 0.5, 0.09, "#e70013")


@country("turkey", "Türkiye")
def _(c):
    c.fill("#e30a17")
    c.crescent(0.36, 0.5, 0.25, W_, dx=0.25, r2=0.8)
    c.star(0.5, 0.5, 0.1, W_, rot=180)


@country("turkmenistan", "Turkmenistan")
def _(c):
    c.fill("#00843d")
    c.rect(0.14, 0, 0.3, 1, "#d22630")
    for i in range(5):
        c.ellipse(0.22, 0.12 + i * 0.19, 0.04, 0.06, "#fcd116")
    c.crescent(0.43, 0.22, 0.1, W_, dx=0.3, r2=0.8)
    for i in range(5):
        c.star(0.48 + (i % 2) * 0.04, 0.1 + i * 0.05, 0.022, W_)


@country("tuvalu", "Tuvalu")
def _(c):
    blue_ensign(c, "#009fca")
    for x, y in ((0.6, 0.85), (0.6, 0.65), (0.7, 0.75), (0.75, 0.55), (0.82, 0.8), (0.85, 0.4), (0.9, 0.6),
                 (0.92, 0.2), (0.7, 0.3)):
        c.star(x, y, 0.045, "#ffce00")


@country("uganda", "Uganda")
def _(c):
    c.hstripes([K_, "#fcdc04", "#d90000"] * 2)
    c.disc(0.5, 0.5, 0.22, W_)
    c.bitmap(E.PELICAN, 0.5, 0.5, 0.3, "#5a5a5a")


@country("united_arab_emirates", "United Arab Emirates")
def _(c):
    c.hstripes(["#00732f", W_, K_])
    c.rect(0, 0, 0.25, 1, "#ff0000")


@country("united_kingdom", "United Kingdom")
def _(c):
    c.union_jack()


@country("united_states", "United States")
def _(c):
    c.us_stripes_and_canton()


@country("uruguay", "Uruguay")
def _(c):
    c.hstripes([W_, "#0038a8"] * 4 + [W_])
    c.rect(0, 0, 5 / 9 * 2 / 3, 5 / 9, W_)
    c.sun(5 / 9 / 3, 5 / 18, 0.1, "#fcd116", rays=16, ray_len=1.8)


@country("uzbekistan", "Uzbekistan")
def _(c):
    c.hstripes(["#0099b5", "#ce1126", W_, "#ce1126", "#1eb53a"], [10, 1, 10, 1, 10])
    c.crescent(0.12, 0.16, 0.11, W_, dx=0.33, r2=0.82)
    for row, n in ((0, 3), (1, 4), (2, 5)):
        for i in range(n):
            c.star(0.36 - i * 0.06, 0.07 + row * 0.09, 0.025, W_)


@country("vanuatu", "Vanuatu")
def _(c):
    c.hstripes(["#d21034", "#009543"])
    for color, t in (("#fdce12", 0.24), (K_, 0.16)):
        c.line((0, 0), (0.4, 0.5), color, t)
        c.line((0, 1), (0.4, 0.5), color, t)
        c.rect(0.38, 0.5 - t / 2, 1, 0.5 + t / 2, color)
    c.poly([(0, 0.1), (0.33, 0.5), (0, 0.9)], K_)
    c.arc(0.14, 0.5, 0.12, 0.04, 60, 330, "#fdce12")


@country("vatican_city", "Vatican City")
def _(c):
    s = 2 / 3
    c.rect(0, 0, s / 2, 1, "#ffe000")
    c.rect(s / 2, 0, s, 1, W_)
    c.bitmap(E.KEYS, s * 0.75, 0.55, 0.38, "#c8a046")
    c.bitmap(E.CROWN, s * 0.75, 0.22, 0.12, "#c8a046")


@country("venezuela", "Venezuela")
def _(c):
    c.hstripes(["#ffcc00", "#00247d", "#cf142b"])
    for i in range(8):
        import math
        a = math.radians(200 + i * 140 / 7)
        c.star(0.5 + 0.28 * math.cos(a) * 2 / 3, 0.66 + 0.28 * math.sin(a), 0.035, W_)


@country("vietnam", "Vietnam")
def _(c):
    c.fill("#da251d")
    c.star(0.5, 0.5, 0.3, "#ffff00")


@country("zambia", "Zambia")
def _(c):
    c.fill("#198a00")
    c.vstripes(["#de2010", K_, "#ef7d00"], x0=0.67, y0=0.38)
    c.bitmap(E.EAGLE, 0.83, 0.2, 0.22, "#ef7d00")


@country("zimbabwe", "Zimbabwe")
def _(c):
    c.hstripes(["#319208", "#ffd200", "#de2010", K_, "#de2010", "#ffd200", "#319208"])
    c.poly([(0, 0), (0.45, 0.5), (0, 1)], K_)
    c.poly([(0, 0.04), (0.42, 0.5), (0, 0.96)], W_)
    c.star(0.12, 0.5, 0.13, "#de2010")
    c.bitmap(E.BIRD, 0.13, 0.5, 0.1, "#ffd200")


# --------------------------------------------------------------------------- unions
@country("european_union", "European Union")
def _(c):
    c.fill("#003399")
    c.stars_circle(0.5, 0.5, 0.33, 12, 0.055, "#ffcc00")
