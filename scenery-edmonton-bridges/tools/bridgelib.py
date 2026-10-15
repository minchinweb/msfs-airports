"""Shared helpers for the Edmonton bridge models.

Uses the CYXD generator's Mesh class and palette (airport-cyxd/tools/gen_buildings.py) so the bridges keep the same flat-colour
look as the hangars, and extends the palette with the swatches the bridges need (appended after the 32 CYXD ones, so the CYXD
indices stay the same).

Model frame while building: x = east, y = up (0 = the site datum, see SITE altitude), z = north.  Mesh.mirror_x() is applied once
at the end because the sim places model +X to the west.  Every model is placed with heading 0.

Files written per model chunk (a glTF with 16-bit indices holds at most 65,535 vertices, so large bridges are split into chunks
that are placed at the same point):
  scenery-edmonton-bridges/PackageSources/modelLib/<name>/<name>.{gltf,bin,xml}
  scenery-edmonton-bridges/PackageSources/modelLib/texture/bridge_palette.png(.xml)
"""
import json, math, struct, sys, uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "airport-cyxd" / "tools"))
import gen_buildings as gb  # noqa: E402
from gen_buildings import Mesh, PALETTE  # noqa: E402

MODELLIB = ROOT / "scenery-edmonton-bridges" / "PackageSources" / "modelLib"
NS = uuid.UUID("5d0c6c7e-0c1d-4a53-9b6e-0c7d00000002")

# CYXD swatches, re-exported
WALL, ROOF, METAL, DARK, BRICK, TRIM, RED, WHITE, GREY, SALMON, BLUE, YELLOW, GLASS, DGREY, CREAM, NAVY, PANEL, PBLUE, SLATE, DOORG = range(20)
GREEN, MUSTARD, STEEL, TAN, BRONZE, RWHITE, TEAL, YELLOWR, BRICKD, MAUVE, PEACH, LROOF = range(20, 32)

# bridge swatches (index 32 on)
_NEW = [
    ("BLACKST", (46, 42, 42)),      # High Level: dark brown-grey steel
    ("RUST", (116, 62, 42)),        # weathered rust-brown steel (Low Level, Dawson)
    ("SEAGREEN", (146, 190, 168)),  # pale sea-green steel (Low Level south-bound truss)
    ("CONC", (178, 176, 170)),      # new light concrete
    ("CONCD", (128, 126, 120)),     # weathered / shaded concrete
    ("ASPHALT", (52, 54, 58)),
    ("BALLAST", (112, 106, 98)),
    ("RAILRED", (146, 44, 38)),     # red-painted barrier rail
    ("COPPER", (104, 164, 146)),    # oxidised copper roofs
    ("SAND", (200, 174, 134)),      # sandstone / pale brick
    ("BLUEWALK", (52, 108, 170)),   # Menzies hung walkway
    ("WHITEST", (238, 240, 240)),   # Walterdale ribs
    ("RAILSTEEL", (150, 152, 156)),
    ("TIMBER", (122, 88, 58)),
    ("GRASS", (86, 118, 72)),
    ("GLASSLT", (150, 196, 204)),   # conservatory glass
    ("LAMP", (70, 74, 80)),
    ("ORANGE", (214, 120, 40)),
    ("BURGUNDY", (112, 36, 40)),
    ("DKGREEN", (44, 76, 56)),
    ("DAWSONBLUE", (96, 128, 156)),  # Dawson truss steel-blue
    ("PIERBEIGE", (190, 182, 166)),
]
for _i, (_n, _rgb) in enumerate(_NEW):
    globals()[_n] = len(PALETTE)
    PALETTE.append(_rgb)


# local frame -------------------------------------------------------------------------------------
class Frame:
    """Local east/north metres around a lat/lon origin (WGS84 series)."""

    def __init__(self, lat0, lon0):
        p = math.radians(lat0)
        self.lat0, self.lon0 = lat0, lon0
        self.ky = 111132.92 - 559.82 * math.cos(2 * p) + 1.175 * math.cos(4 * p)
        self.kx = 111412.84 * math.cos(p) - 93.5 * math.cos(3 * p) + 0.118 * math.cos(5 * p)

    def en(self, lat, lon):
        return ((lon - self.lon0) * self.kx, (lat - self.lat0) * self.ky)

    def ll(self, e, n):
        return (self.lat0 + n / self.ky, self.lon0 + e / self.kx)

    def axis(self, latlon_pts):
        return Axis([self.en(la, lo) for la, lo in latlon_pts])


class Axis:
    """Polyline in east/north metres parametrised by arc length s; t is the lateral offset, positive to the LEFT of travel."""

    def __init__(self, pts):
        self.p = [tuple(p) for p in pts]
        self.cum = [0.0]
        for a, b in zip(self.p[:-1], self.p[1:]):
            self.cum.append(self.cum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
        self.L = self.cum[-1]

    def at(self, s):
        """(e, n, de, dn): point and unit direction at arc length s (extrapolated along the end segments)."""
        c = self.cum
        i = 0
        while i < len(c) - 2 and s > c[i + 1]:
            i += 1
        a, b = self.p[i], self.p[i + 1]
        ln = (c[i + 1] - c[i]) or 1.0
        de, dn = (b[0] - a[0]) / ln, (b[1] - a[1]) / ln
        u = s - c[i]
        return (a[0] + de * u, a[1] + dn * u, de, dn)

    def en(self, s, t=0.0):
        e, n, de, dn = self.at(s)
        return (e - dn * t, n + de * t)

    def p3(self, s, t, y):
        e, n = self.en(s, t)
        return (e, y, n)

    def heading(self, s=None):
        e, n, de, dn = self.at(self.L / 2 if s is None else s)
        return math.degrees(math.atan2(de, dn)) % 360

    def stations(self, s0, s1, step):
        """Sample stations from s0 to s1: every polyline vertex in between plus a regular step."""
        pts = {round(s0, 6), round(s1, 6)}
        for c in self.cum:
            if s0 < c < s1:
                pts.add(round(c, 6))
        if step:
            k = int(math.ceil((s1 - s0) / step))
            for i in range(1, k):
                pts.add(round(s0 + (s1 - s0) * i / k, 6))
        return sorted(pts)


def profile(points):
    """Piecewise-linear f(s) through (s, y) points (clamped at the ends)."""
    pts = sorted(points)

    def f(s):
        if s <= pts[0][0]:
            return pts[0][1]
        for (a, ya), (b, yb) in zip(pts[:-1], pts[1:]):
            if s <= b:
                return ya + (yb - ya) * (s - a) / ((b - a) or 1.0)
        return pts[-1][1]
    return f


def _fn(v):
    return v if callable(v) else (lambda s, v=v: v)


# solids ------------------------------------------------------------------------------------------
def _unit(v):
    ln = math.sqrt(sum(x * x for x in v)) or 1.0
    return tuple(x / ln for x in v)


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def beam(m, p0, p1, w, h, sw, ref=(0.0, 1.0, 0.0)):
    """Rectangular bar from p0 to p1 (x, y, z).  `w` runs along the part of `ref` that is square to the bar, `h` square to both."""
    a = _unit(tuple(p1[i] - p0[i] for i in range(3)))
    r = tuple(ref[i] - _dot(ref, a) * a[i] for i in range(3))
    if _dot(r, r) < 1e-6:
        r = (1.0, 0.0, 0.0) if abs(a[0]) < 0.9 else (0.0, 0.0, 1.0)
        r = tuple(r[i] - _dot(r, a) * a[i] for i in range(3))
    wd = _unit(r)
    hd = _unit(_cross(a, wd))
    c = [(p0[i] + p1[i]) / 2 for i in range(3)]

    def P(p, sw_, sh_):
        return tuple(p[i] + wd[i] * sw_ * w / 2 + hd[i] * sh_ * h / 2 for i in range(3))
    q0 = [P(p0, -1, -1), P(p0, 1, -1), P(p0, 1, 1), P(p0, -1, 1)]
    q1 = [P(p1, -1, -1), P(p1, 1, -1), P(p1, 1, 1), P(p1, -1, 1)]
    m.poly(q0, sw, c)
    m.poly(q1, sw, c)
    for i in range(4):
        j = (i + 1) % 4
        m.poly([q0[i], q0[j], q1[j], q1[i]], sw, c)


def ribbon(m, ax, s0, s1, t0, t1, y0, y1, sw, step=None, caps=True, sw_top=None, sw_side=None, sw_bot=None):
    """Slab along the axis from s0 to s1, lateral extent t0..t1 (t0 < t1), vertical extent y0..y1 (numbers or functions of s)."""
    f0, f1 = _fn(y0), _fn(y1)
    ss = ax.stations(s0, s1, step)
    sw_top = sw if sw_top is None else sw_top
    sw_side = sw if sw_side is None else sw_side
    sw_bot = sw if sw_bot is None else sw_bot
    for a, b in zip(ss[:-1], ss[1:]):
        def V(s, t, f):
            return ax.p3(s, t, f(s))
        c = ax.p3((a + b) / 2, (t0 + t1) / 2, (f0((a + b) / 2) + f1((a + b) / 2)) / 2)
        m.poly([V(a, t0, f1), V(b, t0, f1), V(b, t1, f1), V(a, t1, f1)], sw_top, c)
        m.poly([V(a, t0, f0), V(b, t0, f0), V(b, t1, f0), V(a, t1, f0)], sw_bot, c)
        m.poly([V(a, t1, f0), V(b, t1, f0), V(b, t1, f1), V(a, t1, f1)], sw_side, c)
        m.poly([V(a, t0, f0), V(b, t0, f0), V(b, t0, f1), V(a, t0, f1)], sw_side, c)
    if caps:
        for s in (s0, s1):
            c = ax.p3((s0 + s1) / 2, (t0 + t1) / 2, (f0((s0 + s1) / 2) + f1((s0 + s1) / 2)) / 2)
            m.poly([ax.p3(s, t0, f0(s)), ax.p3(s, t1, f0(s)), ax.p3(s, t1, f1(s)), ax.p3(s, t0, f1(s))], sw_side, c)


def prism(m, pts, y0, y1, sw, sw_top=None):
    """Convex polygon (list of (x, z)) extruded from y0 to y1."""
    n = len(pts)
    cx = sum(p[0] for p in pts) / n
    cz = sum(p[1] for p in pts) / n
    c = (cx, (y0 + y1) / 2, cz)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        m.poly([(a[0], y0, a[1]), (b[0], y0, b[1]), (b[0], y1, b[1]), (a[0], y1, a[1])], sw, c)
    m.poly([(p[0], y1, p[1]) for p in pts], sw if sw_top is None else sw_top, c)
    m.poly([(p[0], y0, p[1]) for p in pts], sw, c)


def frustum(m, bot, top, y0, y1, sw, sw_top=None):
    """Convex polygon `bot` at y0 joined to polygon `top` at y1 (same vertex count)."""
    n = len(bot)
    c = (sum(p[0] for p in bot) / n, (y0 + y1) / 2, sum(p[1] for p in bot) / n)
    for i in range(n):
        j = (i + 1) % n
        m.poly([(bot[i][0], y0, bot[i][1]), (bot[j][0], y0, bot[j][1]), (top[j][0], y1, top[j][1]), (top[i][0], y1, top[i][1])], sw, c)
    m.poly([(p[0], y1, p[1]) for p in top], sw if sw_top is None else sw_top, c)
    m.poly([(p[0], y0, p[1]) for p in bot], sw, c)


def circle(cx, cz, r, n=14, rot=0.0):
    return [(cx + r * math.cos(rot + 2 * math.pi * i / n), cz + r * math.sin(rot + 2 * math.pi * i / n)) for i in range(n)]


def cyl(m, cx, cz, r0, r1, y0, y1, sw, n=14):
    frustum(m, circle(cx, cz, r0, n), circle(cx, cz, r1, n), y0, y1, sw)


def nose_plan(ax, s, t, half_s, half_t, nose, ends=(True, True)):
    """Pier plan on the axis frame: a rectangle `half_s` x `half_t` about (s, t) with a pointed nose of length `nose` on the +t and/or -t ends."""
    pts = []
    L, R = ends[0], ends[1]
    pts.append(ax.en(s - half_s, t - half_t))
    if R:
        pts.append(ax.en(s, t - half_t - nose))
    pts.append(ax.en(s + half_s, t - half_t))
    pts.append(ax.en(s + half_s, t + half_t))
    if L:
        pts.append(ax.en(s, t + half_t + nose))
    pts.append(ax.en(s - half_s, t + half_t))
    return pts


def scale_poly(pts, k, about=None):
    cx = sum(p[0] for p in pts) / len(pts) if about is None else about[0]
    cz = sum(p[1] for p in pts) / len(pts) if about is None else about[1]
    return [(cx + (x - cx) * k, cz + (z - cz) * k) for x, z in pts]


# truss -------------------------------------------------------------------------------------------
def truss_plane(m, ax, t, s0, s1, ytop, ybot, npan, kind="pratt", chord=(0.7, 0.9), web=(0.35, 0.5), sw=None, sw_web=None,
                top_fn=None, sub=False, skip_ends=False, counters=True):
    """One plane of a truss at lateral offset t between stations s0 and s1.

    ytop / ybot: chord centre heights (numbers); top_fn(i/npan) overrides ytop with a polygonal top chord (camelback / Pennsylvania).
    kind: "pratt" (diagonals fall toward mid-span), "warren" (alternating diagonals), "howe" (diagonals rise toward mid-span).
    sub: Baltimore-style sub-struts in the lower half of every panel.
    """
    sw = sw if sw is not None else DARK
    sw_web = sw_web if sw_web is not None else sw
    lat = (-ax.at((s0 + s1) / 2)[3], 0.0, ax.at((s0 + s1) / 2)[2])
    dp = (s1 - s0) / npan
    S = [s0 + i * dp for i in range(npan + 1)]
    ft, fb = _fn(ytop), _fn(ybot)
    yt = [(top_fn(i / npan) if top_fn else ft(S[i])) for i in range(npan + 1)]
    yb = [fb(S[i]) for i in range(npan + 1)]
    P = lambda s, y: ax.p3(s, t, y)
    cw, ch = chord
    ww, wh = web
    for i in range(npan):  # chords per panel (kinks allowed)
        beam(m, P(S[i], yt[i]), P(S[i + 1], yt[i + 1]), cw, ch, sw, lat)
        beam(m, P(S[i], yb[i]), P(S[i + 1], yb[i + 1]), cw, ch, sw, lat)
    mid = npan / 2.0
    for i in range(npan + 1):
        if skip_ends and i in (0, npan):
            continue
        beam(m, P(S[i], yt[i]), P(S[i], yb[i]), ww, wh, sw_web, lat)
    for i in range(npan):
        T0, T1, B0, B1 = (S[i], yt[i]), (S[i + 1], yt[i + 1]), (S[i], yb[i]), (S[i + 1], yb[i + 1])
        if kind == "warren":
            a, b = (T0, B1) if i % 2 == 0 else (B0, T1)
        elif kind == "pratt":
            if i + 0.5 < mid:
                a, b = T0, B1
            elif i + 0.5 > mid:
                a, b = B0, T1
            else:  # centre panel: an X
                a, b = T0, B1
                if counters:
                    beam(m, P(*B0), P(*T1), ww, wh, sw_web, lat)
        else:  # howe
            a, b = (B0, T1) if i + 0.5 < mid else (T0, B1)
        beam(m, P(*a), P(*b), ww, wh, sw_web, lat)
        if sub and kind == "pratt" and i + 0.5 != mid:
            # Baltimore sub-strut: a short post from the lower chord to the middle of the diagonal, and a sub-diagonal back to the node
            smid = (a[0] + b[0]) / 2
            ymid = (a[1] + b[1]) / 2
            ylow = (B0[1] + B1[1]) / 2
            beam(m, P(smid, ylow), P(smid, ymid), ww * 0.8, wh * 0.8, sw_web, lat)
            lowend = B0 if (a == B0 or b == B0) else B1
            beam(m, P(smid, ymid), P(*lowend), ww * 0.7, wh * 0.7, sw_web, lat)
    return S


def floor_beams(m, ax, stations, t0, t1, y, w, h, sw):
    """Cross-beams spanning laterally at each station."""
    for s in stations:
        beam(m, ax.p3(s, t0, y), ax.p3(s, t1, y), w, h, sw)


def x_brace(m, ax, s0, s1, t0, t1, y, w, h, sw):
    """Plan X bracing between two lateral lines over one panel."""
    beam(m, ax.p3(s0, t0, y), ax.p3(s1, t1, y), w, h, sw, (0, 1, 0))
    beam(m, ax.p3(s0, t1, y), ax.p3(s1, t0, y), w, h, sw, (0, 1, 0))


def railing(m, ax, s0, s1, t, y, h=1.1, post_step=3.0, sw_post=None, sw_rail=None, step=None, rails=2, post_w=0.12):
    """Posts and rails along the axis at lateral offset t, sitting on y."""
    sw_post = sw_post if sw_post is not None else DARK
    sw_rail = sw_rail if sw_rail is not None else sw_post
    yf = _fn(y)
    k = max(1, int(round((s1 - s0) / post_step)))
    for i in range(k + 1):
        s = s0 + (s1 - s0) * i / k
        beam(m, ax.p3(s, t, yf(s)), ax.p3(s, t, yf(s) + h), post_w, post_w, sw_post)
    for j in range(rails):
        hh = h * (1.0 if j == 0 else (j / rails * 0.9))
        ribbon(m, ax, s0, s1, t - 0.05, t + 0.05, lambda s, hh=hh: yf(s) + hh - 0.05, lambda s, hh=hh: yf(s) + hh + 0.05, sw_rail,
               step=step, caps=True)


def lamp(m, e, n, y, h, arm, dx, dz, sw=None, head=0.5):
    """Street lamp: round-ish pole, an arm reaching `arm` m toward (dx, dz) and a head."""
    sw = sw if sw is not None else LAMP
    ln = math.hypot(dx, dz) or 1.0
    dx, dz = dx / ln, dz / ln
    beam(m, (e, y, n), (e, y + h, n), 0.22, 0.22, sw)
    beam(m, (e, y + h, n), (e + dx * arm, y + h + 0.5, n + dz * arm), 0.12, 0.12, sw)
    beam(m, (e + dx * (arm - 0.6), y + h + 0.45, n + dz * (arm - 0.6)), (e + dx * (arm + 0.5), y + h + 0.5, n + dz * (arm + 0.5)), 0.38, 0.2, GREY)


def through_truss_span(m, ax, s0, s1, tt, ybot, npan, h_fn, kind="pratt", sub=False, sw=None, sw_web=None, chord=(0.7, 0.8),
                       web=(0.35, 0.45), portal_clear=5.4, bracing=True):
    """Two truss planes at lateral +-tt with the deck between them at the bottom chord: top struts, plan bracing, portals, floor beams.

    h_fn(f) gives the top-chord height above the bottom chord at fraction f of the span (a flat or polygonal top chord).
    """
    sw = sw if sw is not None else DARK
    sw_web = sw_web if sw_web is not None else sw
    S = None
    for t in (-tt, tt):
        S = truss_plane(m, ax, t, s0, s1, ybot, ybot, npan, kind=kind, chord=chord, web=web, sw=sw, sw_web=sw_web,
                        top_fn=lambda f: ybot + h_fn(f), sub=sub)
    n = len(S) - 1
    for i, s in enumerate(S):
        y = ybot + h_fn(i / n)
        beam(m, ax.p3(s, -tt, y), ax.p3(s, tt, y), 0.35, 0.45, sw_web)                         # top strut
        beam(m, ax.p3(s, -tt, ybot), ax.p3(s, tt, ybot), 0.4, 0.9, sw_web)                      # floor beam
        if bracing and 0 < i < n and i % 2 == 0:
            beam(m, ax.p3(s, -tt, y - 1.6), ax.p3(s, tt, y - 1.6), 0.2, 0.2, sw_web)
    if bracing:
        for i in range(n):
            ya = ybot + h_fn(i / n)
            x_brace(m, ax, S[i], S[i + 1], -tt, tt, ya, 0.2, 0.2, sw_web)
    for s, f in ((S[0], 0.0), (S[-1], 1.0)):  # portals
        y = ybot + h_fn(f)
        pt = ybot + portal_clear
        beam(m, ax.p3(s, -tt, pt), ax.p3(s, tt, pt), 0.4, 0.6, sw_web)
    return S


# saving ------------------------------------------------------------------------------------------
class BMesh(Mesh):
    """Mesh that remembers where each polygon starts so it can be split into model chunks."""

    def __init__(self):
        super().__init__(textured=False)
        self.pstart = []

    def poly(self, pts, sw, centre):
        self.pstart.append((len(self.pos), len(self.tri_mat)))
        super().poly(pts, sw, centre)

    def add_to(self, other):
        """Copy this mesh into `other` (keeps polygon boundaries)."""
        for (v0, t0), nxt in zip(self.pstart, self.pstart[1:] + [(len(self.pos), len(self.tri_mat))]):
            other.pstart.append((len(other.pos), len(other.tri_mat)))
            base = len(other.pos)
            other.pos += self.pos[v0:nxt[0]]
            other.nrm += self.nrm[v0:nxt[0]]
            other.uv += self.uv[v0:nxt[0]]
            other.idx += [i - v0 + base for i in self.idx[3 * t0:3 * nxt[1]]]
            other.tri_mat += self.tri_mat[t0:nxt[1]]

    def chunks(self, limit=60000):
        out, cur = [], None
        marks = self.pstart + [(len(self.pos), len(self.tri_mat))]
        for (v0, t0), (v1, t1) in zip(marks[:-1], marks[1:]):
            if cur is None or len(cur["pos"]) + (v1 - v0) > limit:
                cur = {"pos": [], "nrm": [], "uv": [], "idx": []}
                out.append(cur)
            base = len(cur["pos"])
            cur["pos"] += self.pos[v0:v1]
            cur["nrm"] += self.nrm[v0:v1]
            cur["uv"] += self.uv[v0:v1]
            cur["idx"] += [i - v0 + base for i in self.idx[3 * t0:3 * t1]]
        return out


def write_palette():
    gb.write_palette(MODELLIB / "texture" / "bridge_palette.png")


def save_chunks(m, name, prune=True):
    """Mirror once, write the chunks as <name>_1, <name>_2 ... and return [(model name, guid)]."""
    m.mirror_x()
    folder_names = []
    parts = m.chunks()
    for k, ch in enumerate(parts, 1):
        nm = name if len(parts) == 1 else "%s_%d" % (name, k)
        folder = MODELLIB / nm
        folder.mkdir(parents=True, exist_ok=True)
        n = len(ch["pos"])
        assert n < 65535, n
        pos = b"".join(struct.pack("<3f", *p) for p in ch["pos"])
        nrm = b"".join(struct.pack("<3f", *p) for p in ch["nrm"])
        uv = b"".join(struct.pack("<2f", *p) for p in ch["uv"])
        ib = b"".join(struct.pack("<H", i) for i in ch["idx"])
        pad = (-len(ib)) % 4
        blob = pos + nrm + uv + ib + b"\x00" * pad
        mn = [min(p[i] for p in ch["pos"]) for i in range(3)]
        mx = [max(p[i] for p in ch["pos"]) for i in range(3)]
        views = [{"buffer": 0, "byteOffset": 0, "byteLength": len(pos)},
                 {"buffer": 0, "byteOffset": len(pos), "byteLength": len(nrm)},
                 {"buffer": 0, "byteOffset": len(pos) + len(nrm), "byteLength": len(uv)},
                 {"buffer": 0, "byteOffset": len(pos) + len(nrm) + len(uv), "byteLength": len(ib)}]
        accs = [{"bufferView": 0, "componentType": 5126, "count": n, "type": "VEC3", "min": mn, "max": mx},
                {"bufferView": 1, "componentType": 5126, "count": n, "type": "VEC3"},
                {"bufferView": 2, "componentType": 5126, "count": n, "type": "VEC2"},
                {"bufferView": 3, "componentType": 5123, "count": len(ch["idx"]), "type": "SCALAR"}]
        g = {
            "asset": {"version": "2.0", "generator": "scenery-edmonton-bridges/tools/bridgelib.py",
                      "extensions": {"ASOBO_normal_map_convention": {"tangent_space_convention": "DirectX"}}},
            "extensionsUsed": ["ASOBO_normal_map_convention"],
            "scene": 0, "scenes": [{"nodes": [0]}],
            "nodes": [{"mesh": 0, "name": nm}],
            "meshes": [{"name": nm, "primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2}, "indices": 3, "mode": 4, "material": 0}]}],
            "materials": [{"name": "bridge_palette", "pbrMetallicRoughness": {
                "baseColorTexture": {"index": 0}, "metallicFactor": 0.0, "roughnessFactor": 0.9}}],
            "textures": [{"sampler": 0, "source": 0}],
            "samplers": [{"magFilter": 9728, "minFilter": 9728}],
            "images": [{"uri": "bridge_palette.png"}],
            "accessors": accs, "bufferViews": views, "buffers": [{"uri": f"{nm}.bin", "byteLength": len(blob)}],
        }
        (folder / f"{nm}.bin").write_bytes(blob)
        (folder / f"{nm}.gltf").write_text(json.dumps(g, indent=1))
        guid = "{" + str(uuid.uuid5(NS, nm)).upper() + "}"
        (folder / f"{nm}.xml").write_text(
            f'<?xml version="1.0" encoding="utf-8"?>\n<ModelInfo guid="{guid}" version="1.1">\n'
            f'\t<LODS>\n\t\t<LOD minSize="0" ModelFile="{nm}.gltf"/>\n\t</LODS>\n</ModelInfo>\n')
        folder_names.append((nm, guid))
    return folder_names


# preview -----------------------------------------------------------------------------------------
def preview(m, out, az=210.0, el=22.0, width=1800, height=900, span=None, centre=None, water=True, y_water=0.0, zoom=1.0, light=(0.4, 0.8, 0.45)):
    """Orthographic painter's-algorithm render of an UNMIRRORED mesh (x east, y up, z north) to a PNG.  az = compass bearing the
    camera stands at (looking back at the centre); el = degrees above the horizon."""
    import numpy as np
    from PIL import Image, ImageDraw
    P = np.array(m.pos, float)
    N = np.array(m.nrm, float)
    U = np.array([u[0] for u in m.uv], float)
    I = np.array(m.idx, int).reshape(-1, 3)
    col = np.array(PALETTE, float)
    a, e_ = math.radians(az), math.radians(el)
    f = (-math.sin(a), -math.cos(a))          # horizontal view direction (east, north)
    r = (f[1], -f[0])                         # screen right
    cam = np.array([math.sin(a) * math.cos(e_), math.sin(e_), math.cos(a) * math.cos(e_)])
    cen = np.array(centre if centre else ((P.min(0) + P.max(0)) / 2))

    def proj(Q):
        d = (Q[:, 0] - cen[0]) * f[0] + (Q[:, 2] - cen[2]) * f[1]
        x = (Q[:, 0] - cen[0]) * r[0] + (Q[:, 2] - cen[2]) * r[1]
        y = (Q[:, 1] - cen[1]) * math.cos(e_) - d * math.sin(e_)
        w = d * math.cos(e_) + (Q[:, 1] - cen[1]) * math.sin(e_)
        return x, y, w
    x, y, w = proj(P)
    sp = span or max(x.max() - x.min(), (y.max() - y.min()) * width / height) * 1.06
    sc = width / sp * zoom
    cy = (y.max() + y.min()) / 2
    X = width / 2 + x * sc
    Y = height / 2 - (y - cy) * sc
    img = Image.new("RGB", (width, height), (196, 214, 232))
    dr = ImageDraw.Draw(img)
    if water:
        ext = max(abs(P[:, 0] - cen[0]).max(), abs(P[:, 2] - cen[2]).max()) * 1.6
        corners = np.array([[cen[0] - ext, y_water, cen[2] - ext], [cen[0] + ext, y_water, cen[2] - ext],
                            [cen[0] + ext, y_water, cen[2] + ext], [cen[0] - ext, y_water, cen[2] + ext]])
        cx_, cy_, _ = proj(corners)
        dr.polygon([(width / 2 + a_ * sc, height / 2 - (b_ - cy) * sc) for a_, b_ in zip(cx_, cy_)], fill=(122, 148, 160))
    tri_n = N[I[:, 0]]
    facing = (tri_n @ cam) > 0
    L = np.array(light) / np.linalg.norm(light)
    shade = 0.55 + 0.45 * np.clip(tri_n @ L, 0, 1)
    depth = w[I].mean(1)
    order = np.argsort(-depth)
    for t in order:
        if not facing[t]:
            continue
        i0, i1, i2 = I[t]
        c = col[int(U[i0] * len(PALETTE))] * shade[t]
        dr.polygon([(X[i0], Y[i0]), (X[i1], Y[i1]), (X[i2], Y[i2])], fill=tuple(int(max(0, min(255, v))) for v in c))
    img.save(out)
    return out


# site data helpers ---------------------------------------------------------------------------------
def find_way(folder, osm_id):
    """Nodes [(lat, lon), ...] of an OSM way in docs/edmonton-bridges/reference/<folder>/geometry.json."""
    g = json.load(open(ROOT / "docs/edmonton-bridges/reference" / folder / "geometry.json", encoding="utf-8"))
    stack = [g]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            if o.get("osm_way") == osm_id and "nodes" in o:
                return [tuple(p) for p in o["nodes"]]
            stack += list(o.values())
        elif isinstance(o, list):
            stack += o
    raise KeyError(osm_id)


def ground_profile(folder, part_way, datum):
    """f(chainage) = bare-earth height above `datum` along an OSM way, from the 25 m profiles.csv (2018 LiDAR)."""
    import csv
    pts = []
    for r in csv.DictReader(open(ROOT / "docs/edmonton-bridges/reference" / folder / "elevation/profiles.csv")):
        if str(r["osm_way"]) == str(part_way):
            pts.append((float(r["chainage_m"]), float(r["dtm_m"]) - datum))
    return profile(pts)


def deck_profile(folder, part_way, datum):
    """Same for the first-return surface (deck top incl. rails)."""
    import csv
    pts = []
    for r in csv.DictReader(open(ROOT / "docs/edmonton-bridges/reference" / folder / "elevation/profiles.csv")):
        if str(r["osm_way"]) == str(part_way):
            pts.append((float(r["chainage_m"]), float(r["dsm_m"]) - datum))
    return profile(pts)


def mid_axis(fr, nodes_a, nodes_b, n=40):
    """Axis midway between two roughly parallel ways (b is reversed if it runs the other way)."""
    A, B = Axis([fr.en(*p) for p in nodes_a]), Axis([fr.en(*p) for p in nodes_b])
    a0, a1, b0, b1 = A.p[0], A.p[-1], B.p[0], B.p[-1]
    rev = (math.hypot(a0[0] - b0[0], a0[1] - b0[1]) + math.hypot(a1[0] - b1[0], a1[1] - b1[1]) >
           math.hypot(a0[0] - b1[0], a0[1] - b1[1]) + math.hypot(a1[0] - b0[0], a1[1] - b0[1]))
    pts = []
    for i in range(n + 1):
        f = i / n
        pa = A.at(A.L * f)[:2]
        pb = B.at(B.L * (1 - f if rev else f))[:2]
        pts.append(((pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2))
    return Axis(pts)


def project(ax, e, n, samples=400):
    """(s, t) of a point relative to a polyline axis (nearest sample)."""
    best = None
    for i in range(samples + 1):
        s = ax.L * i / samples
        pe, pn, de, dn = ax.at(s)
        d = math.hypot(e - pe, n - pn)
        if best is None or d < best[0]:
            best = (d, s, (e - pe) * -dn + (n - pn) * de)
    return best[1], best[2]


def run_info(site, way):
    """(from, to chainage of the raised structure run, rise median) of an OSM way, from docs/edmonton-bridges/data/measurements.json."""
    d = json.load(open(ROOT / "docs/edmonton-bridges/data/measurements.json", encoding="utf-8"))
    for ln in d[site]["lines"]:
        if ln.get("osm_way") == way and "structure_run" in ln:
            r = ln["structure_run"]
            return r["from_chainage_m"], r["to_chainage_m"], r
    raise KeyError((site, way))


def deck_fit(folder, way, datum, s0, s1, lift=-0.2):
    """Straight deck line y(s) fitted to the first-return profile inside s0..s1 (DSM includes traffic, so `lift` trims it)."""
    import csv
    pts = [(float(r["chainage_m"]), float(r["dsm_m"]) - datum) for r in csv.DictReader(open(ROOT / "docs/edmonton-bridges/reference" / folder / "elevation/profiles.csv"))
           if str(r["osm_way"]) == str(way) and s0 - 1 <= float(r["chainage_m"]) <= s1 + 1]
    if len(pts) < 2:
        y = sum(p[1] for p in pts) / max(1, len(pts))
        return lambda s: y + lift
    n = len(pts)
    ms, my = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    den = sum((p[0] - ms) ** 2 for p in pts) or 1.0
    k = sum((p[0] - ms) * (p[1] - my) for p in pts) / den
    return lambda s: my + k * (s - ms) + lift


def slab_bridge(m, ax, s0, s1, w, y_fn, depth=1.6, parapet_h=0.95, parapet_sw=None, rail_sw=None, deck_sw=None, side_sw=None,
                piers=(), pier_w=2.4, abut_depth=9.0, post_sw=None, lamps=()):
    """Girder / slab road bridge on abutments (and optional piers): deck, parapets with a top rail, abutment walls, column piers."""
    deck_sw = ASPHALT if deck_sw is None else deck_sw
    side_sw = CONC if side_sw is None else side_sw
    parapet_sw = CONC if parapet_sw is None else parapet_sw
    ribbon(m, ax, s0, s1, -w / 2, w / 2, lambda s: y_fn(s) - depth, y_fn, side_sw, step=15.0, sw_top=deck_sw, sw_bot=CONCD)
    for sg in (-1, 1):
        t = sg * (w / 2 - 0.2)
        ribbon(m, ax, s0, s1, t - 0.2, t + 0.2, y_fn, lambda s: y_fn(s) + parapet_h, parapet_sw, step=15.0)
        if rail_sw is not None:
            ribbon(m, ax, s0, s1, t - 0.06, t + 0.06, lambda s: y_fn(s) + parapet_h, lambda s: y_fn(s) + parapet_h + 0.35, rail_sw, step=15.0)
    for s, sg in ((s0, -1), (s1, 1)):
        ribbon(m, ax, s - (1.6 if sg < 0 else 0.0), s + (0.0 if sg < 0 else 1.6), -w / 2 - 0.6, w / 2 + 0.6, y_fn(s) - depth - abut_depth, y_fn(s) - depth + 0.2, CONC)
    for s in piers:
        e, n = ax.en(s, 0.0)
        cyl(m, e, n, pier_w / 2, pier_w / 2, y_fn(s) - depth - abut_depth, y_fn(s) - depth, CONCD, n=14)
    for s, side in lamps:
        e, n = ax.en(s, side * (w / 2 + 0.3))
        de, dn = -ax.at(s)[3], ax.at(s)[2]
        lamp(m, e, n, y_fn(s), 9.5, 2.0, -side * de, -side * dn)


def triangulate(pts):
    """Ear clipping of a simple 2D polygon: list of (i, j, k) index triples."""
    idx = list(range(len(pts)))
    if sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in idx) < 0:
        idx.reverse()

    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

    def inside(p, a, b, c):
        return cross(a, b, p) >= 0 and cross(b, c, p) >= 0 and cross(c, a, p) >= 0
    tris = []
    while len(idx) > 3:
        for k in range(len(idx)):
            i0, i1, i2 = idx[k - 1], idx[k], idx[(k + 1) % len(idx)]
            a, b, c = pts[i0], pts[i1], pts[i2]
            if cross(a, b, c) <= 1e-9:
                continue
            if any(inside(pts[j], a, b, c) for j in idx if j not in (i0, i1, i2)):
                continue
            tris.append((i0, i1, i2))
            del idx[k]
            break
        else:
            break
    if len(idx) == 3:
        tris.append(tuple(idx))
    return tris


def wheel(m, ax, s_c, y_c, r, t0, t1, sw, n=16):
    """Disc with its axle along the lateral direction: a paddle wheel."""
    rim = [(s_c + r * math.cos(2 * math.pi * i / n), y_c + r * math.sin(2 * math.pi * i / n)) for i in range(n)]
    c = ax.p3(s_c, (t0 + t1) / 2, y_c)
    for i in range(n):
        a, b = rim[i], rim[(i + 1) % n]
        m.poly([ax.p3(a[0], t0, a[1]), ax.p3(b[0], t0, b[1]), ax.p3(b[0], t1, b[1]), ax.p3(a[0], t1, a[1])], sw, c)
    for t in (t0, t1):
        m.poly([ax.p3(p[0], t, p[1]) for p in rim], sw, c)


def pca_axis(pts, toward=None):
    """Principal direction of `pts` (east/north metres): (cx, cy, (de, dn), min, max) along it; `toward` picks the sign."""
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    syy = sum((p[1] - my) ** 2 for p in pts)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    th = 0.5 * math.atan2(2 * sxy, sxx - syy)
    d = (math.cos(th), math.sin(th))
    if toward and d[0] * toward[0] + d[1] * toward[1] < 0:
        d = (-d[0], -d[1])
    ext = [(p[0] - mx) * d[0] + (p[1] - my) * d[1] for p in pts]
    return mx, my, d, min(ext), max(ext)
