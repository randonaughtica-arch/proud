"""A tiny vector-ish drawing API for flags.

Flags are drawn at a high resolution with coordinates given as fractions of the
flag's width (x) and height (y), then downsampled to the final texture size.
Sizes such as radii and line thicknesses are fractions of the flag's height.
"""
import math

from PIL import Image, ImageDraw

W, H = 48, 32  # final texture size (3:2)
SS = 8  # supersampling factor


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


# 3x5 pixel font for the few flags that carry text.
FONT = {
    "A": ["###", "#.#", "###", "#.#", "#.#"], "B": ["##.", "#.#", "##.", "#.#", "##."],
    "C": ["###", "#..", "#..", "#..", "###"], "D": ["##.", "#.#", "#.#", "#.#", "##."],
    "E": ["###", "#..", "##.", "#..", "###"], "F": ["###", "#..", "##.", "#..", "#.."],
    "G": ["###", "#..", "#.#", "#.#", "###"], "H": ["#.#", "#.#", "###", "#.#", "#.#"],
    "I": ["###", ".#.", ".#.", ".#.", "###"], "J": ["..#", "..#", "..#", "#.#", "###"],
    "K": ["#.#", "#.#", "##.", "#.#", "#.#"], "L": ["#..", "#..", "#..", "#..", "###"],
    "M": ["#.#", "###", "###", "#.#", "#.#"], "N": ["##.", "#.#", "#.#", "#.#", "#.#"],
    "O": ["###", "#.#", "#.#", "#.#", "###"], "P": ["###", "#.#", "###", "#..", "#.."],
    "Q": ["###", "#.#", "#.#", "###", "..#"], "R": ["##.", "#.#", "##.", "#.#", "#.#"],
    "S": ["###", "#..", "###", "..#", "###"], "T": ["###", ".#.", ".#.", ".#.", ".#."],
    "U": ["#.#", "#.#", "#.#", "#.#", "###"], "V": ["#.#", "#.#", "#.#", "#.#", ".#."],
    "W": ["#.#", "#.#", "###", "###", "#.#"], "X": ["#.#", "#.#", ".#.", "#.#", "#.#"],
    "Y": ["#.#", "#.#", ".#.", ".#.", ".#."], "Z": ["###", "..#", ".#.", "#..", "###"],
    "0": ["###", "#.#", "#.#", "#.#", "###"], "1": [".#.", "##.", ".#.", ".#.", "###"],
    "2": ["###", "..#", "###", "#..", "###"], "3": ["###", "..#", "###", "..#", "###"],
    "4": ["#.#", "#.#", "###", "..#", "..#"], "5": ["###", "#..", "###", "..#", "###"],
    "6": ["###", "#..", "###", "#.#", "###"], "7": ["###", "..#", "..#", "..#", "..#"],
    "8": ["###", "#.#", "###", "#.#", "###"], "9": ["###", "#.#", "###", "..#", "###"],
    " ": ["...", "...", "...", "...", "..."], ".": ["...", "...", "...", "...", ".#."],
}


class Canvas:
    def __init__(self):
        self.w, self.h = W * SS, H * SS
        self.img = Image.new("RGBA", (self.w, self.h), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)

    # ---- coordinate helpers
    def X(self, f):
        return f * self.w

    def Y(self, f):
        return f * self.h

    def L(self, f):
        """A length given as a fraction of the flag height."""
        return f * self.h

    def pt(self, p):
        return (self.X(p[0]), self.Y(p[1]))

    @staticmethod
    def col(c):
        return hexrgb(c) if isinstance(c, str) else c

    # ---- fields
    def fill(self, c):
        self.d.rectangle([0, 0, self.w, self.h], fill=self.col(c))

    def rect(self, x0, y0, x1, y1, c):
        self.d.rectangle([self.X(x0), self.Y(y0), self.X(x1) - 1, self.Y(y1) - 1], fill=self.col(c))

    def hstripes(self, colors, weights=None, x0=0.0, y0=0.0, x1=1.0, y1=1.0):
        weights = weights or [1] * len(colors)
        total, acc = sum(weights), 0.0
        for c, wgt in zip(colors, weights):
            a = y0 + (y1 - y0) * acc / total
            acc += wgt
            b = y0 + (y1 - y0) * acc / total
            self.d.rectangle([self.X(x0), self.Y(a), self.X(x1) - 1, math.ceil(self.Y(b)) - 1], fill=self.col(c))

    def vstripes(self, colors, weights=None, x0=0.0, y0=0.0, x1=1.0, y1=1.0):
        weights = weights or [1] * len(colors)
        total, acc = sum(weights), 0.0
        for c, wgt in zip(colors, weights):
            a = x0 + (x1 - x0) * acc / total
            acc += wgt
            b = x0 + (x1 - x0) * acc / total
            self.d.rectangle([self.X(a), self.Y(y0), math.ceil(self.X(b)) - 1, self.Y(y1) - 1], fill=self.col(c))

    def poly(self, pts, c):
        self.d.polygon([self.pt(p) for p in pts], fill=self.col(c))

    def hoist_triangle(self, c, depth=0.5, y0=0.0, y1=1.0):
        self.poly([(0, y0), (depth, (y0 + y1) / 2), (0, y1)], c)

    def diagonal(self, c, t, rising=True):
        """A band from one corner to the opposite one; rising goes bottom-left to top-right."""
        a, b = ((0, 1), (1, 0)) if rising else ((0, 0), (1, 1))
        self.line(a, b, c, t)

    def line(self, a, b, c, t):
        self.d.line([self.pt(a), self.pt(b)], fill=self.col(c), width=max(1, round(self.L(t))))

    # ---- crosses
    def cross(self, c, t, cx=0.5, cy=0.5):
        half = self.L(t) / 2
        self.d.rectangle([self.X(cx) - half, 0, self.X(cx) + half, self.h], fill=self.col(c))
        self.d.rectangle([0, self.Y(cy) - half, self.w, self.Y(cy) + half], fill=self.col(c))

    def nordic(self, c, t, cx=0.375):
        self.cross(c, t, cx=cx)

    def nordic_bordered(self, outer, inner, t_outer, t_inner, cx=0.375):
        self.cross(outer, t_outer, cx=cx)
        self.cross(inner, t_inner, cx=cx)

    def saltire(self, c, t):
        width = max(1, round(self.L(t)))
        self.d.line([(0, 0), (self.w, self.h)], fill=self.col(c), width=width)
        self.d.line([(0, self.h), (self.w, 0)], fill=self.col(c), width=width)

    def union_jack(self, x0=0.0, y0=0.0, x1=1.0, y1=1.0):
        sub = Canvas()
        sub.fill("#012169")
        sub.saltire("#ffffff", 0.2)
        # counterchanged red saltire, offset clockwise
        w, h, t = sub.w, sub.h, max(1, round(sub.L(0.066)))
        r = sub.col("#c8102e")
        off = t / 2
        sub.d.line([(0, -off), (w / 2, h / 2 - off)], fill=r, width=t)
        sub.d.line([(w / 2, h / 2 + off), (w, h + off)], fill=r, width=t)
        sub.d.line([(w + off, 0), (w / 2 + off, h / 2)], fill=r, width=t)
        sub.d.line([(w / 2 - off, h / 2), (-off, h)], fill=r, width=t)
        sub.cross("#ffffff", 0.333)
        sub.cross("#c8102e", 0.2)
        self.paste(sub, x0, y0, x1, y1)

    def us_stripes_and_canton(self, stripes=13, canton_color="#0a3161"):
        self.hstripes(["#b31942", "#ffffff"] * (stripes // 2) + ["#b31942"])
        self.rect(0, 0, 0.4, 7 / 13, canton_color)
        self.star_grid(0, 0, 0.4, 7 / 13, 5, 6, "#ffffff", 0.03, offset_rows=True)

    def star_grid(self, x0, y0, x1, y1, rows, cols, c, r, offset_rows=False):
        for row in range(rows * 2 - 1 if offset_rows else rows):
            n = cols if not offset_rows or row % 2 == 0 else cols - 1
            for i in range(n):
                if offset_rows:
                    fx = (2 * i + 1 + (1 if row % 2 else 0)) / (2 * cols)
                else:
                    fx = (i + 0.5) / cols
                fy = (row + 0.5) / (rows * 2 - 1 if offset_rows else rows)
                self.star(x0 + (x1 - x0) * fx, y0 + (y1 - y0) * fy, r, c)

    # ---- shapes
    def disc(self, cx, cy, r, c):
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        self.d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=self.col(c))

    def ellipse(self, cx, cy, rx, ry, c):
        x, y = self.X(cx), self.Y(cy)
        self.d.ellipse([x - self.L(rx), y - self.L(ry), x + self.L(rx), y + self.L(ry)], fill=self.col(c))

    def ring(self, cx, cy, r, t, c):
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        self.d.ellipse([x - rr, y - rr, x + rr, y + rr], outline=self.col(c), width=max(1, round(self.L(t))))

    def star(self, cx, cy, r, c, points=5, rot=-90.0, inner=0.382):
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        pts = []
        for i in range(points * 2):
            ang = math.radians(rot + i * 180.0 / points)
            rad = rr if i % 2 == 0 else rr * inner
            pts.append((x + rad * math.cos(ang), y + rad * math.sin(ang)))
        self.d.polygon(pts, fill=self.col(c))

    def stars_circle(self, cx, cy, R, n, r, c, start=-90.0):
        for i in range(n):
            a = math.radians(start + 360.0 * i / n)
            self.star(cx + R * (self.h / self.w) * math.cos(a), cy + R * math.sin(a), r, c)

    def crescent(self, cx, cy, r, c, dx=0.3, dy=0.0, r2=0.8):
        """A crescent: a disc with an offset disc cut away (dx, dy in units of r; +dx opens to the fly)."""
        mask = Image.new("L", (self.w, self.h), 0)
        md = ImageDraw.Draw(mask)
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        md.ellipse([x - rr, y - rr, x + rr, y + rr], fill=255)
        ox, oy, r2r = x + rr * dx, y + rr * dy, rr * r2
        md.ellipse([ox - r2r, oy - r2r, ox + r2r, oy + r2r], fill=0)
        self.img.paste(Image.new("RGBA", (self.w, self.h), self.col(c)), (0, 0), mask)
        self.d = ImageDraw.Draw(self.img)

    def arc(self, cx, cy, r, t, start, end, c):
        """A thick arc; angles in degrees clockwise from the fly direction."""
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        self.d.arc([x - rr, y - rr, x + rr, y + rr], start, end, fill=self.col(c), width=max(1, round(self.L(t))))

    def pieslice(self, cx, cy, r, start, end, c):
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        self.d.pieslice([x - rr, y - rr, x + rr, y + rr], start, end, fill=self.col(c))

    def outline_poly(self, pts, c, t):
        self.d.polygon([self.pt(p) for p in pts], outline=self.col(c), width=max(1, round(self.L(t))))

    def sun(self, cx, cy, r, c, rays=12, ray_len=1.6, ray_w=0.35):
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        for i in range(rays):
            a = math.radians(360.0 * i / rays)
            b1, b2 = a - ray_w * math.pi / rays, a + ray_w * math.pi / rays
            self.d.polygon([(x + rr * 0.8 * math.cos(b1), y + rr * 0.8 * math.sin(b1)),
                            (x + rr * ray_len * math.cos(a), y + rr * ray_len * math.sin(a)),
                            (x + rr * 0.8 * math.cos(b2), y + rr * 0.8 * math.sin(b2))], fill=self.col(c))
        self.d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=self.col(c))

    def triskelion(self, cx, cy, r, c, t=0.06):
        """Three bent legs running clockwise around the centre (Isle of Man, Sicily)."""
        k = self.h / self.w
        for i in range(3):
            a = math.radians(-90 + i * 120)
            knee = (cx + r * 0.55 * math.cos(a) * k, cy + r * 0.55 * math.sin(a))
            b = a + math.radians(70)
            foot = (knee[0] + r * 0.5 * math.cos(b) * k, knee[1] + r * 0.5 * math.sin(b))
            toe = (foot[0] + r * 0.18 * math.cos(b + math.radians(90)) * k,
                   foot[1] + r * 0.18 * math.sin(b + math.radians(90)))
            self.line((cx, cy), knee, c, t)
            self.line(knee, foot, c, t)
            self.line(foot, toe, c, t * 0.8)
        self.disc(cx, cy, t * 0.8, c)

    def rose(self, cx, cy, r, c, center):
        k = self.h / self.w
        for i in range(5):
            a = math.radians(-90 + i * 72)
            self.disc(cx + r * 0.5 * math.cos(a) * k, cy + r * 0.5 * math.sin(a), r * 0.5, c)
        self.disc(cx, cy, r * 0.35, center)

    def wheel(self, cx, cy, r, c, spokes=24, t=0.02):
        self.ring(cx, cy, r, t, c)
        x, y, rr = self.X(cx), self.Y(cy), self.L(r)
        for i in range(spokes):
            a = math.radians(360.0 * i / spokes)
            self.d.line([(x, y), (x + rr * math.cos(a), y + rr * math.sin(a))], fill=self.col(c),
                        width=max(1, round(self.L(t * 0.6))))
        self.disc(cx, cy, r * 0.15, c)

    def shield(self, cx, cy, h, c, border=None):
        """A simple heater shield, used for simplified coats of arms."""
        x, y, hh = self.X(cx), self.Y(cy), self.L(h)
        ww = hh * 0.8
        pts = [(x - ww / 2, y - hh / 2), (x + ww / 2, y - hh / 2), (x + ww / 2, y + hh * 0.05),
               (x, y + hh / 2), (x - ww / 2, y + hh * 0.05)]
        if border:
            self.d.polygon(pts, fill=self.col(border))
            s = 0.8
            pts = [(x + (px - x) * s, y + (py - y) * s) for px, py in pts]
        self.d.polygon(pts, fill=self.col(c))

    def seal(self, cx, cy, r, ring="#f2c94c", inner="#ffffff", detail=None):
        """A simplified round seal: a coloured ring around a disc with a small device."""
        self.disc(cx, cy, r, ring)
        self.disc(cx, cy, r * 0.78, inner)
        if detail:
            self.disc(cx, cy, r * 0.4, detail)

    def text(self, s, cx, cy, c, size=0.16):
        """Centered text in the 3x5 font; size is the letter height as a fraction of flag height."""
        px = self.L(size) / 5
        total = len(s) * 4 - 1
        x0, y0 = self.X(cx) - total * px / 2, self.Y(cy) - 2.5 * px
        for i, ch in enumerate(s.upper()):
            for row, bits in enumerate(FONT.get(ch, FONT[" "])):
                for col, bit in enumerate(bits):
                    if bit == "#":
                        x, y = x0 + (i * 4 + col) * px, y0 + row * px
                        self.d.rectangle([x, y, x + px - 1, y + px - 1], fill=self.col(c))

    def bitmap(self, art, cx, cy, h, c, aspect=1.0):
        """Draws ASCII art ('#' filled) centered at (cx, cy) with height h (fraction of flag height)."""
        rows = [r for r in art.strip("\n").split("\n")]
        n_rows, n_cols = len(rows), max(len(r) for r in rows)
        cell_h = self.L(h) / n_rows
        cell_w = cell_h * aspect
        x0, y0 = self.X(cx) - n_cols * cell_w / 2, self.Y(cy) - n_rows * cell_h / 2
        for j, row in enumerate(rows):
            for i, ch in enumerate(row):
                if ch == "#":
                    self.d.rectangle([x0 + i * cell_w, y0 + j * cell_h,
                                      x0 + (i + 1) * cell_w - 1, y0 + (j + 1) * cell_h - 1], fill=self.col(c))

    # ---- compositing
    def paste(self, other, x0, y0, x1, y1):
        box = (round(self.X(x0)), round(self.Y(y0)), round(self.X(x1)), round(self.Y(y1)))
        piece = other.img.resize((box[2] - box[0], box[3] - box[1]), Image.LANCZOS)
        self.img.alpha_composite(piece, (box[0], box[1]))

    def cut(self, pts):
        """Makes the area inside the polygon transparent (swallowtails, pennants)."""
        mask = Image.new("L", (self.w, self.h), 0)
        ImageDraw.Draw(mask).polygon([self.pt(p) for p in pts], fill=255)
        clear = Image.new("RGBA", (self.w, self.h), (0, 0, 0, 0))
        self.img = Image.composite(clear, self.img, mask)
        self.d = ImageDraw.Draw(self.img)

    def keep(self, pts):
        """Makes everything outside the polygon transparent (non-rectangular flags)."""
        mask = Image.new("L", (self.w, self.h), 0)
        ImageDraw.Draw(mask).polygon([self.pt(p) for p in pts], fill=255)
        clear = Image.new("RGBA", (self.w, self.h), (0, 0, 0, 0))
        self.img = Image.composite(self.img, clear, mask)
        self.d = ImageDraw.Draw(self.img)

    def render(self):
        small = self.img.resize((W, H), Image.LANCZOS)
        # Snap alpha so cutout rendering gets crisp edges.
        px = small.load()
        for y in range(H):
            for x in range(W):
                r, g, b, a = px[x, y]
                px[x, y] = (r, g, b, 255 if a >= 128 else 0)
        return small
