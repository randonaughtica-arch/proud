"""State, province, constituent-country and regional flags. Seals and arms are simplified."""
import math

import emblems as E
from registry import flag

W_, K_ = "#ffffff", "#000000"
US_BLUE, US_RED, GOLD = "#002868", "#bf0a30", "#f2c94c"


def seal_flag(cat, fid, name, field=US_BLUE, ring=GOLD, inner=W_, detail="#3b6e3b", r=0.3, text=None,
              text_color=GOLD, text_y=0.85, cy=0.47):
    def draw(c):
        c.fill(field)
        c.seal(0.5, cy, r, ring, inner, detail)
        if text:
            c.text(text, 0.5, text_y, text_color, size=0.15)
    flag(fid, name, cat)(draw)


def us(fid, name):
    return flag(fid, name, "us_states")


def ensign(c, field="#012169"):
    c.fill(field)
    c.union_jack(0, 0, 0.5, 0.5)


def disc_badge(c, color, cx=0.75, cy=0.5, r=0.28):
    c.disc(cx, cy, r, color)


def southern_cross(c, x, color=W_, scale=1.0):
    for dx, y, r in ((0, 0.17, 0.06), (-0.08, 0.45, 0.055), (0.08, 0.38, 0.05), (0, 0.8, 0.065),
                     (0.045, 0.56, 0.035)):
        c.star(x + dx * scale, y, r * scale, color, points=7 if r > 0.04 else 5)


# =========================================================================== US states
@us("alabama", "Alabama")
def _(c):
    c.fill(W_)
    c.saltire("#b22234", 0.2)


@us("alaska", "Alaska")
def _(c):
    c.fill("#0f204b")
    for x, y in ((0.1, 0.72), (0.2, 0.75), (0.3, 0.68), (0.4, 0.62), (0.42, 0.78), (0.55, 0.8), (0.56, 0.62)):
        c.star(x, y, 0.045, "#ffb612")
    c.star(0.82, 0.2, 0.08, "#ffb612")


@us("arizona", "Arizona")
def _(c):
    c.fill(US_BLUE)
    for i in range(13):
        a0 = math.radians(180 + i * 180 / 13)
        a1 = math.radians(180 + (i + 1) * 180 / 13)
        c.poly([(0.5, 0.5), (0.5 + 2 * math.cos(a0), 0.5 + 2 * math.sin(a0)),
                (0.5 + 2 * math.cos(a1), 0.5 + 2 * math.sin(a1))], "#fed700" if i % 2 == 0 else US_RED)
    c.rect(0, 0.5, 1, 1, US_BLUE)
    c.star(0.5, 0.5, 0.2, "#ce5c17")


@us("arkansas", "Arkansas")
def _(c):
    c.fill(US_RED)
    c.poly([(0.5, 0.06), (0.86, 0.5), (0.5, 0.94), (0.14, 0.5)], US_BLUE)
    c.poly([(0.5, 0.16), (0.78, 0.5), (0.5, 0.84), (0.22, 0.5)], W_)
    c.text("ARKANSAS", 0.5, 0.5, US_BLUE, size=0.1)
    c.star(0.5, 0.33, 0.05, US_BLUE)
    for x in (0.42, 0.5, 0.58):
        c.star(x, 0.66, 0.04, US_BLUE)


@us("california", "California")
def _(c):
    c.fill(W_)
    c.rect(0, 0.85, 1, 1, "#b22234")
    c.rect(0.25, 0.72, 0.75, 0.75, "#5a8a2a")
    c.bitmap(E.BEAR, 0.5, 0.55, 0.35, "#6b4423")
    c.star(0.12, 0.17, 0.09, "#b22234")


@us("colorado", "Colorado")
def _(c):
    c.hstripes([US_BLUE, W_, US_BLUE])
    c.arc(0.42, 0.5, 0.3, 0.14, 40, 320, US_RED)
    c.disc(0.42, 0.5, 0.15, "#ffd700")


@us("connecticut", "Connecticut")
def _(c):
    c.fill("#0f204b")
    c.shield(0.5, 0.45, 0.5, W_, "#c8a046")
    for y in (0.32, 0.45, 0.58):
        c.disc(0.5, y, 0.045, "#6a2c91")


@us("delaware", "Delaware")
def _(c):
    c.fill("#0060a8")
    c.poly([(0.5, 0.15), (0.75, 0.5), (0.5, 0.85), (0.25, 0.5)], "#e6c793")
    c.seal(0.5, 0.5, 0.15, "#5a7d3a", "#e6c793", "#3b6e9b")


@us("florida", "Florida")
def _(c):
    c.fill(W_)
    c.saltire(US_RED, 0.16)
    c.seal(0.5, 0.5, 0.17, "#c8a046", "#7bb7e0", "#3b8a3b")


@us("georgia_us", "Georgia (US)")
def _(c):
    c.hstripes(["#b22234", W_, "#b22234"])
    c.rect(0, 0, 0.36, 2 / 3, "#002868")
    c.stars_circle(0.18, 0.33, 0.24, 13, 0.025, W_)
    c.seal(0.18, 0.33, 0.12, GOLD, GOLD, W_)


@us("hawaii", "Hawaii")
def _(c):
    c.hstripes([W_, "#c8102e", "#00247d"] * 2 + [W_, "#c8102e"])
    c.union_jack(0, 0, 0.5, 0.5)


seal_flag("us_states", "idaho", "Idaho", text="IDAHO", text_color=GOLD)
seal_flag("us_states", "illinois", "Illinois", field=W_, ring="#7a8a5a", inner=W_, detail="#4a3a2a",
          text="ILLINOIS", text_color="#002868")


@us("indiana", "Indiana")
def _(c):
    c.fill(US_BLUE)
    c.stars_circle(0.5, 0.5, 0.36, 13, 0.035, GOLD)
    c.stars_circle(0.5, 0.55, 0.2, 5, 0.03, GOLD, start=-140)
    c.star(0.5, 0.12, 0.06, GOLD)
    c.bitmap(E.TORCH, 0.5, 0.55, 0.45, GOLD)


@us("iowa", "Iowa")
def _(c):
    c.vstripes([US_BLUE, W_, US_RED])
    c.bitmap(E.EAGLE, 0.5, 0.4, 0.35, "#1f4a8a")
    c.text("IOWA", 0.5, 0.73, US_RED, size=0.13)


@us("kansas", "Kansas")
def _(c):
    c.fill("#00369c")
    c.seal(0.5, 0.45, 0.24, "#c8a046", "#7bb7e0", "#3b6e3b")
    c.disc(0.5, 0.15, 0.06, "#ffcc00")
    c.text("KANSAS", 0.5, 0.85, "#ffcc00", size=0.15)


seal_flag("us_states", "kentucky", "Kentucky", field="#002868", ring=GOLD, inner=W_, detail="#2a3a7a")


@us("louisiana", "Louisiana")
def _(c):
    c.fill(US_BLUE)
    c.bitmap(E.PELICAN, 0.5, 0.48, 0.55, W_)
    c.rect(0.25, 0.82, 0.75, 0.9, W_)


@us("maine", "Maine")
def _(c):
    c.fill(US_BLUE)
    c.shield(0.5, 0.48, 0.5, "#7bb7e0", "#c8a046")
    c.bitmap(E.PINE, 0.5, 0.48, 0.32, "#2e6b2e")
    c.star(0.5, 0.12, 0.06, GOLD)


@us("maryland", "Maryland")
def _(c):
    def calvert(x0, y0):
        c.vstripes(["#e8c84a", K_] * 3, x0=x0, y0=y0, x1=x0 + 0.5, y1=y0 + 0.5)
        c.line((x0, y0), (x0 + 0.5, y0 + 0.5), "#e8c84a", 0.05)

    def crossland(x0, y0):
        c.rect(x0, y0, x0 + 0.25, y0 + 0.25, W_)
        c.rect(x0 + 0.25, y0, x0 + 0.5, y0 + 0.25, US_RED)
        c.rect(x0, y0 + 0.25, x0 + 0.25, y0 + 0.5, US_RED)
        c.rect(x0 + 0.25, y0 + 0.25, x0 + 0.5, y0 + 0.5, W_)
        c.rect(x0 + 0.23, y0 + 0.06, x0 + 0.27, y0 + 0.44, K_)
        c.rect(x0 + 0.1, y0 + 0.22, x0 + 0.4, y0 + 0.28, K_)

    calvert(0, 0)
    crossland(0.5, 0)
    crossland(0, 0.5)
    calvert(0.5, 0.5)


@us("massachusetts", "Massachusetts")
def _(c):
    c.fill(W_)
    c.shield(0.5, 0.5, 0.6, "#0f4d92", "#c8a046")
    c.star(0.42, 0.38, 0.08, W_)


@us("michigan", "Michigan")
def _(c):
    c.fill(US_BLUE)
    c.shield(0.5, 0.5, 0.5, "#7bb7e0", "#c8a046")
    c.bitmap(E.EAGLE, 0.5, 0.2, 0.2, "#c8a046")


@us("minnesota", "Minnesota")
def _(c):
    c.fill("#52c9e8")
    c.poly([(0, 0), (0.33, 0), (0.37, 0.38), (0.31, 0.55), (0.36, 1), (0, 1)], "#002d5d")
    c.star(0.16, 0.5, 0.17, W_, points=8, inner=0.45)


@us("mississippi", "Mississippi")
def _(c):
    c.vstripes(["#bf0a30", "#ffd700", "#002868", "#ffd700", "#bf0a30"], [2, 0.3, 7, 0.3, 2])
    c.stars_circle(0.5, 0.5, 0.32, 20, 0.03, W_, start=-72)
    c.star(0.5, 0.15, 0.05, "#ffd700")
    c.disc(0.5, 0.5, 0.13, W_)
    c.disc(0.5, 0.5, 0.05, "#ffd700")


@us("missouri", "Missouri")
def _(c):
    c.hstripes([US_RED, W_, US_BLUE])
    c.ring(0.5, 0.5, 0.2, 0.04, US_BLUE)
    c.seal(0.5, 0.5, 0.14, "#c8a046", W_, "#6b4423")


seal_flag("us_states", "montana", "Montana", text="MONTANA", text_y=0.12, cy=0.55)
seal_flag("us_states", "nebraska", "Nebraska", ring=GOLD, inner=GOLD, detail=US_BLUE)


@us("nevada", "Nevada")
def _(c):
    c.fill("#003da5")
    c.star(0.17, 0.2, 0.1, W_)
    c.text("NEVADA", 0.17, 0.42, "#ffd700", size=0.09)
    c.arc(0.17, 0.25, 0.2, 0.03, 30, 150, "#ffd700")


seal_flag("us_states", "new_hampshire", "New Hampshire", detail="#8a5a2a")


@us("new_jersey", "New Jersey")
def _(c):
    c.fill("#e6c793")
    c.shield(0.5, 0.5, 0.45, "#1f4a8a", "#c8a046")


@us("new_mexico", "New Mexico")
def _(c):
    c.fill("#ffd700")
    red = "#bf0a30"
    c.disc(0.5, 0.5, 0.11, red)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        for k in (-1.5, -0.5, 0.5, 1.5):
            if dx:
                y = 0.5 + k * 0.05
                c.rect(0.5 + dx * 0.1 if dx > 0 else 0.5 - 0.27, y - 0.012,
                       0.5 + 0.27 if dx > 0 else 0.5 - 0.1, y + 0.012, red)
            else:
                x = 0.5 + k * 0.033
                c.rect(x - 0.009, 0.5 + 0.16 if dy > 0 else 0.5 - 0.4,
                       x + 0.009, 0.5 + 0.4 if dy > 0 else 0.5 - 0.16, red)
    c.disc(0.5, 0.5, 0.07, "#ffd700")


@us("new_york", "New York")
def _(c):
    c.fill(US_BLUE)
    c.shield(0.5, 0.5, 0.45, "#7bb7e0", "#c8a046")
    c.disc(0.5, 0.42, 0.06, GOLD)
    c.ellipse(0.32, 0.55, 0.04, 0.16, "#c8a046")
    c.ellipse(0.68, 0.55, 0.04, 0.16, "#c8a046")


@us("north_carolina", "North Carolina")
def _(c):
    c.hstripes([US_RED, W_])
    c.rect(0, 0, 1 / 3, 1, US_BLUE)
    c.star(1 / 6, 0.5, 0.1, W_)
    c.text("N", 0.09, 0.5, GOLD, size=0.14)
    c.text("C", 0.24, 0.5, GOLD, size=0.14)


@us("north_dakota", "North Dakota")
def _(c):
    c.fill("#1c3f94")
    c.bitmap(E.EAGLE, 0.5, 0.52, 0.55, "#4a3a2a")
    c.stars_circle(0.5, 0.35, 0.18, 7, 0.025, GOLD, start=200)


@us("ohio", "Ohio")
def _(c):
    c.hstripes([US_RED, W_, US_RED, W_, US_RED])
    c.poly([(0, 0), (0.52, 0.5), (0, 1)], US_BLUE)
    c.ring(0.2, 0.5, 0.15, 0.06, W_)
    c.disc(0.2, 0.5, 0.08, US_RED)
    for i in range(13):
        a = math.radians(-60 + i * 120 / 12)
        if abs(i - 6) > 1:
            c.star(0.2 + 0.32 * math.cos(a) * 2 / 3, 0.5 + 0.32 * math.sin(a), 0.03, W_)
    c.cut([(1.01, -0.01), (0.77, 0.5), (1.01, 1.01)])


@us("oklahoma", "Oklahoma")
def _(c):
    c.fill("#2a6ebb")
    c.ellipse(0.5, 0.45, 0.32, 0.22, "#c8a46c")
    c.star(0.42, 0.42, 0.04, "#6b4423", points=4)
    c.star(0.58, 0.42, 0.04, "#6b4423", points=4)
    c.line((0.3, 0.48), (0.7, 0.48), "#6b4423", 0.02)
    c.text("OKLAHOMA", 0.5, 0.82, W_, size=0.12)


@us("oregon", "Oregon")
def _(c):
    c.fill("#002a86")
    c.text("OREGON", 0.5, 0.17, "#ffd700", size=0.13)
    c.seal(0.5, 0.52, 0.2, "#ffd700", "#002a86", "#ffd700")
    c.text("1859", 0.5, 0.86, "#ffd700", size=0.13)


@us("pennsylvania", "Pennsylvania")
def _(c):
    c.fill("#002868")
    c.shield(0.5, 0.5, 0.45, "#7bb7e0", "#c8a046")
    c.ellipse(0.3, 0.55, 0.06, 0.13, K_)
    c.ellipse(0.7, 0.55, 0.06, 0.13, K_)


@us("rhode_island", "Rhode Island")
def _(c):
    c.fill(W_)
    c.stars_circle(0.5, 0.48, 0.35, 13, 0.035, "#f6bd38")
    c.bitmap(E.ANCHOR, 0.5, 0.45, 0.42, "#f6bd38")
    c.rect(0.38, 0.75, 0.62, 0.83, "#003593")
    c.text("HOPE", 0.5, 0.79, "#f6bd38", size=0.06)


@us("south_carolina", "South Carolina")
def _(c):
    c.fill("#003f87")
    c.bitmap(E.PALMETTO, 0.5, 0.52, 0.6, W_)
    c.crescent(0.17, 0.2, 0.09, W_, dx=0.0, dy=-0.25, r2=0.85)


@us("south_dakota", "South Dakota")
def _(c):
    c.fill("#0f5aa0")
    c.sun(0.5, 0.48, 0.24, "#f2c94c", rays=24, ray_len=1.3, ray_w=0.6)
    c.seal(0.5, 0.48, 0.2, W_, "#7bb7e0", "#3b6e3b")


@us("tennessee", "Tennessee")
def _(c):
    c.fill(US_RED)
    c.rect(0.91, 0, 1, 1, W_)
    c.rect(0.93, 0, 1, 1, US_BLUE)
    c.disc(0.47, 0.5, 0.28, W_)
    c.disc(0.47, 0.5, 0.25, US_BLUE)
    for x, y in ((0.47, 0.37), (0.39, 0.58), (0.55, 0.58)):
        c.star(x, y, 0.07, W_)


@us("texas", "Texas")
def _(c):
    c.hstripes([W_, US_RED])
    c.rect(0, 0, 1 / 3, 1, US_BLUE)
    c.star(1 / 6, 0.5, 0.15, W_)


@us("utah", "Utah")
def _(c):
    c.hstripes([W_, "#1d2b4e", "#b22234"], [1, 1.3, 0.7])
    for x in (0.1, 0.3, 0.5, 0.7, 0.9):
        c.poly([(x - 0.12, 0.34), (x, 0.24), (x + 0.12, 0.34)], W_)
    c.poly([(0.5, 0.3), (0.58, 0.4), (0.58, 0.6), (0.5, 0.7), (0.42, 0.6), (0.42, 0.4)], "#1d2b4e")
    c.ellipse(0.5, 0.5, 0.08, 0.1, "#f2a900")


@us("vermont", "Vermont")
def _(c):
    c.fill(US_BLUE)
    c.shield(0.5, 0.5, 0.5, "#7bb7e0", "#c8a046")
    c.rect(0.4, 0.55, 0.6, 0.68, "#4a8a3a")
    c.bitmap(E.PINE, 0.5, 0.42, 0.25, "#2e6b2e")


seal_flag("us_states", "virginia", "Virginia", field="#002868", ring=W_, inner="#7bb7e0", detail="#6b4423")
seal_flag("us_states", "washington", "Washington", field="#00573f", ring=GOLD, inner=W_, detail="#5a5a5a")


@us("west_virginia", "West Virginia")
def _(c):
    c.fill("#002868")
    c.rect(0.04, 0.06, 0.96, 0.94, W_)
    c.seal(0.5, 0.45, 0.22, "#3b6e3b", W_, "#7a5a3a")
    c.rect(0.3, 0.75, 0.7, 0.82, "#b22234")


@us("wisconsin", "Wisconsin")
def _(c):
    c.fill("#002868")
    c.text("WISCONSIN", 0.5, 0.13, W_, size=0.1)
    c.shield(0.5, 0.5, 0.42, "#c8a046", W_)
    c.text("1848", 0.5, 0.86, W_, size=0.1)


@us("wyoming", "Wyoming")
def _(c):
    c.fill(US_RED)
    c.rect(0.05, 0.075, 0.95, 0.925, W_)
    c.rect(0.08, 0.12, 0.92, 0.88, US_BLUE)
    c.bitmap(E.BISON, 0.5, 0.5, 0.48, W_)
    c.disc(0.42, 0.5, 0.08, US_BLUE)


@us("district_of_columbia", "District of Columbia")
def _(c):
    c.fill(W_)
    c.rect(0, 0.42, 1, 0.6, "#e91436")
    c.rect(0, 0.72, 1, 0.9, "#e91436")
    for x in (0.25, 0.5, 0.75):
        c.star(x, 0.22, 0.1, "#e91436")


@us("puerto_rico", "Puerto Rico")
def _(c):
    c.hstripes(["#ed0000", W_] * 2 + ["#ed0000"])
    c.hoist_triangle("#0050f0", 0.43)
    c.star(0.15, 0.5, 0.12, W_)


@us("guam", "Guam")
def _(c):
    c.fill("#c62139")
    c.rect(0.03, 0.045, 0.97, 0.955, "#00297b")
    c.ellipse(0.5, 0.5, 0.17, 0.27, "#c62139")
    c.ellipse(0.5, 0.5, 0.15, 0.25, "#7bb7e0")
    c.rect(0.4, 0.6, 0.6, 0.72, "#e6c793")


@us("us_virgin_islands", "US Virgin Islands")
def _(c):
    c.fill(W_)
    c.bitmap(E.EAGLE, 0.5, 0.5, 0.55, "#f2c94c")
    c.shield(0.5, 0.52, 0.18, "#002868", "#bf0a30")
    c.text("V", 0.3, 0.5, "#162e5c", size=0.15)
    c.text("I", 0.7, 0.5, "#162e5c", size=0.15)


@us("american_samoa", "American Samoa")
def _(c):
    c.fill("#002b7f")
    c.poly([(1, 0), (0, 0.5), (1, 1)], "#bf0a30")
    c.poly([(1, 0.07), (0.12, 0.5), (1, 0.93)], W_)
    c.bitmap(E.EAGLE, 0.7, 0.5, 0.4, "#6b4423")


@us("northern_mariana_islands", "Northern Mariana Islands")
def _(c):
    c.fill("#0071bc")
    c.ring(0.5, 0.5, 0.33, 0.06, "#4a8a3a")
    c.rect(0.46, 0.5, 0.54, 0.8, "#a0a0a0")
    c.ellipse(0.5, 0.48, 0.1, 0.05, "#a0a0a0")
    c.star(0.5, 0.42, 0.17, W_)


# =========================================================================== Canada
def ca(fid, name):
    return flag(fid, name, "canada")


@ca("ontario", "Ontario")
def _(c):
    ensign(c, "#d80621")
    c.shield(0.75, 0.5, 0.45, "#2e7d32", W_)
    c.rect(0.66, 0.31, 0.84, 0.4, "#d80621")
    c.bitmap(E.MAPLE, 0.75, 0.55, 0.15, "#f2c94c")


@ca("quebec", "Quebec")
def _(c):
    c.fill("#003da5")
    c.cross(W_, 0.2)
    for x, y in ((0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)):
        c.bitmap(E.FLEUR, x, y, 0.3, W_)


@ca("british_columbia", "British Columbia")
def _(c):
    c.hstripes(["#003da5", W_] * 4, y0=0.55)
    c.union_jack(0, 0, 1, 0.42)
    c.pieslice(0.5, 0.62, 0.22, 180, 360, "#f2c94c")
    c.rect(0, 0.42, 1, 0.45, "#f2c94c")


@ca("alberta", "Alberta")
def _(c):
    c.fill("#002395")
    c.shield(0.5, 0.5, 0.55, "#7bb7e0", "#c8a046")
    c.rect(0.39, 0.3, 0.61, 0.38, W_)
    c.rect(0.4, 0.55, 0.6, 0.68, "#4a8a3a")


@ca("saskatchewan", "Saskatchewan")
def _(c):
    c.hstripes(["#006a4e", "#fcd116"])
    c.shield(0.18, 0.25, 0.3, "#2e7d32", "#c8a046")
    c.bitmap(E.LILY, 0.8, 0.5, 0.45, "#e65c00")


@ca("manitoba", "Manitoba")
def _(c):
    ensign(c, "#d80621")
    c.shield(0.75, 0.5, 0.45, "#2e7d32", W_)
    c.bitmap(E.BISON, 0.75, 0.55, 0.15, "#6b4423")


@ca("new_brunswick", "New Brunswick")
def _(c):
    c.fill("#f2c94c")
    c.rect(0, 0, 1, 0.33, "#d80621")
    c.bitmap(E.LION_PASSANT, 0.5, 0.17, 0.22, "#f2c94c")
    c.hstripes(["#003da5", W_] * 2, y0=0.8)
    c.bitmap(E.SHIP, 0.5, 0.6, 0.32, K_)


@ca("nova_scotia", "Nova Scotia")
def _(c):
    c.fill(W_)
    c.saltire("#005eb8", 0.2)
    c.shield(0.5, 0.5, 0.3, "#f2c94c", W_)
    c.bitmap(E.LION, 0.5, 0.5, 0.2, "#d80621")


@ca("prince_edward_island", "Prince Edward Island")
def _(c):
    c.fill(W_)
    c.rect(0, 0, 1, 0.33, "#d80621")
    c.bitmap(E.LION_PASSANT, 0.45, 0.17, 0.22, "#f2c94c")
    c.bitmap(E.PINE, 0.6, 0.6, 0.35, "#2e7d32")
    for x in (0.2, 0.3, 0.4):
        c.bitmap(E.PINE, x, 0.67, 0.2, "#2e7d32")
    c.rect(0, 0.88, 1, 0.92, "#4a8a3a")
    for i in range(8):
        c.rect(0.94, i / 8, 1, i / 8 + 1 / 16, "#d80621")


@ca("newfoundland_and_labrador", "Newfoundland and Labrador")
def _(c):
    c.fill(W_)
    c.poly([(0, 0), (0.4, 0), (0, 0.45)], "#002395")
    c.poly([(0, 1), (0.4, 1), (0, 0.55)], "#002395")
    c.poly([(0.45, 0.5), (0.55, 0.1), (0.75, 0.5), (0.55, 0.9)], "#d80621")
    c.poly([(0.75, 0.5), (0.95, 0.35), (0.85, 0.5), (0.95, 0.65)], "#f2c94c")


@ca("yukon", "Yukon")
def _(c):
    c.vstripes(["#006a4e", W_, "#002395"], [1, 1.5, 1])
    c.shield(0.5, 0.5, 0.42, "#7bb7e0", "#d80621")
    c.ring(0.5, 0.5, 0.28, 0.03, "#7a4a9a")


@ca("northwest_territories", "Northwest Territories")
def _(c):
    c.vstripes(["#0b5bb3", W_, "#0b5bb3"], [1, 2, 1])
    c.shield(0.5, 0.5, 0.45, "#2e7d32", W_)
    c.rect(0.39, 0.26, 0.61, 0.38, "#0b5bb3")


@ca("nunavut", "Nunavut")
def _(c):
    c.vstripes(["#e0b100", W_])
    c.bitmap(E.INUKSHUK, 0.47, 0.55, 0.6, "#e2232a")
    c.star(0.8, 0.2, 0.09, "#0f3a9a")


# =========================================================================== Australia
def au(fid, name):
    return flag(fid, name, "australia")


@au("new_south_wales", "New South Wales")
def _(c):
    ensign(c)
    disc_badge(c, W_)
    c.rect(0.73, 0.24, 0.77, 0.76, "#c8102e")
    c.rect(0.58, 0.47, 0.92, 0.53, "#c8102e")
    c.bitmap(E.LION_PASSANT, 0.75, 0.5, 0.1, "#f2c94c")


@au("victoria", "Victoria")
def _(c):
    ensign(c)
    southern_cross(c, 0.75)
    c.bitmap(E.CROWN, 0.75, 0.06, 0.08, W_)


@au("queensland", "Queensland")
def _(c):
    ensign(c)
    disc_badge(c, "#7bb7e0")
    c.rect(0.73, 0.32, 0.77, 0.68, "#002868")
    c.rect(0.66, 0.47, 0.84, 0.53, "#002868")
    c.bitmap(E.CROWN, 0.75, 0.5, 0.1, "#f2c94c")


@au("south_australia", "South Australia")
def _(c):
    ensign(c)
    disc_badge(c, "#ffd200")
    c.bitmap(E.BIRD, 0.75, 0.5, 0.2, K_)


@au("western_australia", "Western Australia")
def _(c):
    ensign(c)
    disc_badge(c, "#ffd200")
    c.bitmap(E.SWAN, 0.75, 0.5, 0.25, K_)


@au("tasmania", "Tasmania")
def _(c):
    ensign(c)
    disc_badge(c, W_)
    c.bitmap(E.LION_PASSANT, 0.75, 0.5, 0.2, "#c8102e")


@au("northern_territory", "Northern Territory")
def _(c):
    c.fill("#c65d1e")
    c.rect(0, 0, 1 / 3, 1, K_)
    southern_cross(c, 1 / 6)
    c.star(0.66, 0.5, 0.25, W_, points=7, inner=0.6)
    c.disc(0.66, 0.5, 0.08, K_)
    c.star(0.66, 0.5, 0.05, W_, points=7)


@au("australian_capital_territory", "Australian Capital Territory")
def _(c):
    c.fill("#ffd200")
    c.rect(0, 0, 1 / 3, 1, "#002868")
    southern_cross(c, 1 / 6)
    c.shield(0.66, 0.55, 0.45, "#002868", W_)
    c.bitmap(E.CASTLE, 0.66, 0.5, 0.15, W_)


# =========================================================================== UK
def uk(fid, name):
    return flag(fid, name, "uk")


@uk("england", "England")
def _(c):
    c.fill(W_)
    c.cross("#ce1124", 0.2)


@uk("scotland", "Scotland")
def _(c):
    c.fill("#005eb8")
    c.saltire(W_, 0.2)


@uk("wales", "Wales")
def _(c):
    c.hstripes([W_, "#00b140"])
    c.bitmap(E.DRAGON, 0.5, 0.5, 0.72, "#d30731")


@uk("saint_patricks_saltire", "Saint Patrick's Saltire")
def _(c):
    c.fill(W_)
    c.saltire("#c8102e", 0.15)


@uk("cornwall", "Cornwall")
def _(c):
    c.fill(K_)
    c.cross(W_, 0.2)


@uk("isle_of_man", "Isle of Man")
def _(c):
    c.fill("#cf142b")
    c.triskelion(0.5, 0.5, 0.42, W_, t=0.09)


@uk("jersey", "Jersey")
def _(c):
    c.fill(W_)
    c.saltire("#df112d", 0.14)
    c.shield(0.5, 0.25, 0.25, "#df112d", "#f2c94c")


@uk("guernsey", "Guernsey")
def _(c):
    c.fill(W_)
    c.cross("#e8112d", 0.2)
    c.cross("#f9dd16", 0.07)


@uk("yorkshire", "Yorkshire")
def _(c):
    c.fill("#0072c6")
    c.rose(0.5, 0.5, 0.25, W_, "#f2c94c")


@uk("northumberland", "Northumberland")
def _(c):
    c.vstripes(["#c8102e", "#fcd116"] * 4)


@uk("shetland", "Shetland")
def _(c):
    c.fill("#0065bd")
    c.nordic(W_, 0.2, cx=0.36)


@uk("orkney", "Orkney")
def _(c):
    c.fill("#d6001c")
    c.nordic_bordered("#fcd116", "#003da5", 0.2, 0.1, cx=0.36)


# =========================================================================== Germany
def de(fid, name):
    return flag(fid, name, "germany")


def de_tricolor_arms(c, shield_color, mark_color):
    c.hstripes([K_, "#dd0000", "#ffce00"])
    c.shield(0.5, 0.5, 0.45, shield_color, W_)
    return mark_color


flag("baden_wurttemberg", "Baden-Württemberg", "germany")(lambda c: c.hstripes([K_, "#ffcc00"]))


@de("bavaria", "Bavaria")
def _(c):
    c.fill(W_)
    n_cols, n_rows = 7, 5
    for row in range(n_rows + 1):
        for col in range(n_cols + 1):
            if (row + col) % 2 == 0:
                x = col / n_cols - (0.5 / n_cols if row % 2 else 0)
                y = row / n_rows
                c.poly([(x, y - 0.5 / n_rows), (x + 0.5 / n_cols, y), (x, y + 0.5 / n_rows),
                        (x - 0.5 / n_cols, y)], "#0098d4")


@de("berlin", "Berlin")
def _(c):
    c.hstripes(["#e2001a", W_, "#e2001a"], [1, 3, 1])
    c.bitmap(E.BEAR, 0.5, 0.5, 0.35, K_)


@de("brandenburg", "Brandenburg")
def _(c):
    c.hstripes(["#e2001a", W_])
    c.shield(0.5, 0.5, 0.45, W_, "#e2001a")
    c.bitmap(E.EAGLE, 0.5, 0.48, 0.3, "#e2001a")


@de("bremen", "Bremen")
def _(c):
    c.hstripes(["#e2001a", W_] * 4)
    for row in range(8):
        for col in range(2):
            if (row + col) % 2 == 1:
                c.rect(col * 0.06, row / 8, (col + 1) * 0.06, (row + 1) / 8, "#e2001a")
            else:
                c.rect(col * 0.06, row / 8, (col + 1) * 0.06, (row + 1) / 8, W_)


@de("hamburg", "Hamburg")
def _(c):
    c.fill("#e2001a")
    c.bitmap(E.CASTLE, 0.5, 0.5, 0.45, W_)


flag("hesse", "Hesse", "germany")(lambda c: c.hstripes(["#e2001a", W_]))


@de("lower_saxony", "Lower Saxony")
def _(c):
    de_tricolor_arms(c, "#e2001a", W_)
    c.bitmap(E.HORSE, 0.5, 0.5, 0.25, W_)


flag("mecklenburg_vorpommern", "Mecklenburg-Vorpommern", "germany")(
    lambda c: c.hstripes(["#0060ad", W_, "#ffcc00", W_, "#e2001a"], [4, 1, 2, 1, 4]))
flag("north_rhine_westphalia", "North Rhine-Westphalia", "germany")(
    lambda c: c.hstripes(["#009639", W_, "#e2001a"]))


@de("rhineland_palatinate", "Rhineland-Palatinate")
def _(c):
    c.hstripes([K_, "#dd0000", "#ffce00"])
    c.shield(0.2, 0.3, 0.4, K_, "#ffce00")


@de("saarland", "Saarland")
def _(c):
    de_tricolor_arms(c, "#0060ad", W_)
    c.bitmap(E.LION, 0.5, 0.5, 0.25, W_)


flag("saxony", "Saxony", "germany")(lambda c: c.hstripes([W_, "#009a3d"]))


@de("saxony_anhalt", "Saxony-Anhalt")
def _(c):
    c.hstripes(["#ffcc00", K_])
    c.shield(0.5, 0.5, 0.45, "#ffcc00", K_)
    c.bitmap(E.CROWN, 0.5, 0.48, 0.12, "#009a3d")


flag("schleswig_holstein", "Schleswig-Holstein", "germany")(
    lambda c: c.hstripes(["#003c8f", W_, "#e2001a"]))
flag("thuringia", "Thuringia", "germany")(lambda c: c.hstripes([W_, "#e2001a"]))


# =========================================================================== Spain
def es(fid, name):
    return flag(fid, name, "spain")


def senyera(c):
    c.hstripes(["#fcdd09", "#da121a"] * 4 + ["#fcdd09"])


es("catalonia", "Catalonia")(senyera)


@es("basque_country", "Basque Country")
def _(c):
    c.fill("#d52b1e")
    c.saltire("#009b48", 0.14)
    c.cross(W_, 0.14)


@es("galicia", "Galicia")
def _(c):
    c.fill(W_)
    c.diagonal("#0099cc", 0.25, rising=False)


flag("andalusia", "Andalusia", "spain")(lambda c: c.hstripes(["#007a3d", W_, "#007a3d"]))


@es("valencia", "Valencian Community")
def _(c):
    senyera(c)
    c.rect(0, 0, 0.25, 1, "#0073ce")
    c.bitmap(E.CROWN, 0.125, 0.2, 0.15, "#fcdd09")


flag("canary_islands", "Canary Islands", "spain")(lambda c: c.vstripes([W_, "#0768a9", "#fecd00"]))


@es("aragon", "Aragon")
def _(c):
    senyera(c)
    c.shield(0.3, 0.5, 0.45, "#0073ce", "#da121a")


@es("asturias", "Asturias")
def _(c):
    c.fill("#0066ff")
    c.rect(0.47, 0.15, 0.53, 0.85, "#fcdd09")
    c.rect(0.38, 0.3, 0.62, 0.36, "#fcdd09")


@es("navarre", "Navarre")
def _(c):
    c.fill("#d52b1e")
    c.ring(0.5, 0.5, 0.24, 0.05, "#fcdd09")
    c.line((0.34, 0.26), (0.66, 0.74), "#fcdd09", 0.04)
    c.line((0.34, 0.74), (0.66, 0.26), "#fcdd09", 0.04)


@es("balearic_islands", "Balearic Islands")
def _(c):
    senyera(c)
    c.rect(0, 0, 0.42, 5 / 9, "#6c3082")
    c.bitmap(E.CASTLE, 0.21, 0.28, 0.25, W_)


@es("madrid", "Community of Madrid")
def _(c):
    c.fill("#c8102e")
    for x, y in ((0.36, 0.38), (0.5, 0.38), (0.64, 0.38), (0.29, 0.62), (0.43, 0.62), (0.57, 0.62),
                 (0.71, 0.62)):
        c.star(x, y, 0.08, W_)


@es("extremadura", "Extremadura")
def _(c):
    c.hstripes(["#00a650", W_, K_])


@es("castile_la_mancha", "Castilla-La Mancha")
def _(c):
    c.vstripes(["#a50034", W_])
    c.bitmap(E.CASTLE, 0.25, 0.5, 0.4, "#fcdd09")


@es("castile_and_leon", "Castile and León")
def _(c):
    c.fill(W_)
    c.rect(0, 0, 0.5, 0.5, "#c8102e")
    c.rect(0.5, 0.5, 1, 1, "#c8102e")
    c.bitmap(E.CASTLE, 0.25, 0.25, 0.3, "#fcdd09")
    c.bitmap(E.CASTLE, 0.75, 0.75, 0.3, "#fcdd09")
    c.bitmap(E.LION, 0.75, 0.25, 0.35, "#6a2c91")
    c.bitmap(E.LION, 0.25, 0.75, 0.35, "#6a2c91")


@es("cantabria", "Cantabria")
def _(c):
    c.hstripes([W_, "#c8102e"])


@es("la_rioja", "La Rioja")
def _(c):
    c.hstripes(["#c8102e", W_, "#009a3d", "#fcdd09"])


@es("murcia", "Region of Murcia")
def _(c):
    c.fill("#b3002d")
    for x, y in ((0.12, 0.15), (0.12, 0.45), (0.12, 0.75), (0.27, 0.3)):
        c.bitmap(E.CASTLE, x, y, 0.13, "#fcdd09")
    for x, y in ((0.85, 0.2), (0.85, 0.5), (0.85, 0.8), (0.72, 0.35), (0.72, 0.65), (0.6, 0.5), (0.27, 0.65)):
        c.bitmap(E.CROWN, x, y, 0.1, "#fcdd09")


# =========================================================================== other regions
def rg(fid, name):
    return flag(fid, name, "regions")


@rg("greenland", "Greenland")
def _(c):
    c.hstripes([W_, "#d00c33"])
    cx = 7 / 18
    c.pieslice(cx, 0.5, 0.33, 180, 360, "#d00c33")
    c.pieslice(cx, 0.5, 0.33, 0, 180, W_)


@rg("faroe_islands", "Faroe Islands")
def _(c):
    c.fill(W_)
    c.nordic_bordered("#0065bd", "#ef303e", 0.25, 0.125, cx=0.36)


@rg("aland", "Åland")
def _(c):
    c.fill("#0064ae")
    c.nordic_bordered("#ffd300", "#da0e15", 0.25, 0.125, cx=0.36)


@rg("sardinia", "Sardinia")
def _(c):
    c.fill(W_)
    c.cross("#d20f19", 0.15)
    for x, y in ((0.22, 0.22), (0.78, 0.22), (0.22, 0.78), (0.78, 0.78)):
        c.disc(x, y, 0.11, K_)
        c.rect(x - 0.08, y - 0.06, x + 0.08, y - 0.03, W_)


@rg("sicily", "Sicily")
def _(c):
    c.fill("#fcdd09")
    c.poly([(0, 0), (1, 0), (0, 1)], "#da121a")
    c.triskelion(0.5, 0.5, 0.38, "#f2b6a0", t=0.07)
    c.disc(0.5, 0.5, 0.1, "#f2b6a0")


@rg("flanders", "Flanders")
def _(c):
    c.fill("#fff200")
    c.bitmap(E.LION, 0.5, 0.5, 0.75, K_)


@rg("wallonia", "Wallonia")
def _(c):
    c.fill("#fff200")
    c.bitmap(E.BIRD, 0.5, 0.5, 0.4, "#da121a")


@rg("normandy", "Normandy")
def _(c):
    c.fill("#e30a17")
    c.bitmap(E.LION_PASSANT, 0.5, 0.3, 0.25, "#fcdd09")
    c.bitmap(E.LION_PASSANT, 0.5, 0.7, 0.25, "#fcdd09")


@rg("scania", "Scania")
def _(c):
    c.fill("#d40b0b")
    c.nordic("#fdd700", 0.2, cx=0.36)


@rg("bohemia", "Bohemia")
def _(c):
    c.hstripes([W_, "#d7141a"])


@rg("upper_silesia", "Upper Silesia")
def _(c):
    c.hstripes(["#fcd116", "#0047ab"])


@rg("venice", "Venice")
def _(c):
    c.fill("#a50021")
    c.bitmap(E.LION, 0.45, 0.45, 0.6, "#fcd116")
    for i in range(6):
        c.cut([(1.01, i / 6), (0.86, (i + 0.5) / 6), (1.01, (i + 1) / 6)])


@rg("occitania", "Occitania")
def _(c):
    c.fill("#d52b1e")
    c.rect(0.47, 0.25, 0.53, 0.75, "#fcdd09")
    c.rect(0.4, 0.46, 0.6, 0.54, "#fcdd09")
    for x, y in ((0.47, 0.25), (0.53, 0.25), (0.47, 0.75), (0.53, 0.75), (0.4, 0.46), (0.4, 0.54),
                 (0.6, 0.46), (0.6, 0.54)):
        c.disc(x, y, 0.025, "#fcdd09")


@rg("tatarstan", "Tatarstan")
def _(c):
    c.hstripes(["#00a651", W_, "#ed1c24"], [7, 1, 7])


@rg("bashkortostan", "Bashkortostan")
def _(c):
    c.hstripes(["#0072bc", W_, "#00a651"])
    c.disc(0.5, 0.5, 0.15, "#fcdd09")
    c.bitmap(E.LILY, 0.5, 0.5, 0.2, "#fcdd09")


@rg("sao_paulo", "São Paulo")
def _(c):
    c.hstripes([K_, W_] * 6 + [K_])
    c.rect(0, 0, 0.5, 7 / 13, "#de2b1f")
    c.disc(0.25, 0.27, 0.15, W_)
    c.poly([(0.2, 0.22), (0.3, 0.22), (0.28, 0.33), (0.22, 0.33)], "#162e8a")
