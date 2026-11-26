"""B276 The Church of Jesus Christ of Latter-day Saints, 9010 85 Street NW (Strathearn), across 85 Street from Holyrood Gardens (B262).

Plan: OpenStreetMap way 322965284, the whole building (31 nodes, no parts or heights).  Its walls run square to one another at 30.6 deg
off the compass, so the model works in a building frame: u along bearing 59.4 (toward 85 Street), v along bearing 329.4; the face at
-v (bearing 149) looks over the curved front lot to Connors Road.

Masses and heights: the 2018 City LiDAR, DSM minus the grade (DTM median under the footprint, 665.45 m), read on a 2 m grid in the
building frame, so they are measured, not assumed:
  - the one-storey wings fill the whole outline: 3 m on the DSM, modelled 3.3 m to the top of the fascia;
  - the cultural hall, u -24.5..5, v -4.5..17: 7 m (8 m along its north edge), modelled 7.2 m;
  - the chapel, u -18.5..-3, v -18.8..-4.5, with its front bay (the OSM bump, u -15.4..-3.7) out to v -25: 7 to 8 m, modelled 7.8 m;
  - the spire, a free-standing brick shaft in the corner between the entrance and the east wing (DSM peak 14.8 m at u 3.5, v -16.5),
    modelled 15.0 m with a needle to 18.6 m.  The needle length is scaled from the shaft in the owner's 2024 photo and the 2018 frame
    (0.2 to 0.26 of the shaft), so it is an estimate.
Form and colours: the owner's photos (2024 front, 2026 night, 2020 wing, 2026 courtyard) and Mapillary 348860486834010 (2018): buff
brick throughout; the chapel's front is beige panels between white pilasters with brick piers at the corners and a brown fascia; the
spire is three brick fins with stepped tops; a flat entrance canopy with two downlights in front of glazed doors; the low wings have
window bands between brick piers under a deep fascia; the lettering panel ("The Church of Jesus Christ of Latter-day Saints") at the
east end of the front stands a little higher.  Window counts and positions are not surveyed.
Night (owner's photo 2026-10-28): the spire and the chapel face are lit from the ground, the canopy has two downlights, and the lobby
is lit.  The courtyard photo shows wall packs on the wings; their number and places here are assumed.  Not yet seen in the sim.

Site: car parks from the architect's 2015 site plan (reference only; geometry.json parking_plan_2015) and the 2019 aerial: the north
lot off the lane, the west lot, and two rows along the curved front drive (the inner row where the 2019 aerial and the 2024 photo show
cars; the outer row from the stall lines in the 2024 photo).  Trees: the 2018 DSM crowns on the church parcel, the species from the
plan's symbols and the photos, as stock MSFS 2024 trees (GUIDs from fs24-asobo-modellib-vegetation's bglindex.bout, as CYXD Hangar 19).
The parcel (OSM way 594346540) clears the sim's own trees and buildings, so only the placed trees stand there.
Datum (y = 0): 665.11 m, the lowest 2018 DTM cell under the footprint; grade is y = 0.34 (665.45 m).
"""
import math

from bridgelib import *

CODE, TITLE = "B276", "Latter-day Saints church, 85 Street"
F = "B276-lds-church-85-street"
LAT0, LON0 = 53.525858, -113.458448       # OSM outline centre (PRIORITY.md)
DATUM = 665.11
G = 0.34                                   # grade above the datum
LOW, HALL, CHAPEL = G + 3.3, G + 7.2, G + 7.8
SPIRE, NEEDLE = G + 15.0, G + 18.6
TH = math.radians(30.6)                    # building u axis, counter-clockwise from east

# stock MSFS 2024 trees, by species (fs24-asobo-modellib-vegetation bglindex.bout, read 2026-11-24; sizes not checked in the sim)
PINUS = ("{F05B3BD0-1C1E-4865-A904-45F9DF37EBDF}", "{60E021B9-9D85-4C59-B106-EC430025816A}", "{8F8A023D-380F-4CB3-8ED8-25D1595AF998}",
         "{48EF1351-F046-406D-BF0E-94524662991D}")
POPULUS = ("{5269E5F0-4CB5-4E81-828A-61169D850DF4}", "{70080A01-E271-45DC-9F70-3488BA9DDA6C}")
BETULA = ("{191FAD7E-E94C-40A3-ADC0-902A5A1F3CB7}", "{81D19B30-F45D-47CB-9787-2BEF376C64CA}", "{4A576EEF-CFA0-47DB-91F9-526718AE5950}",
          "{2C5B485B-06A8-4E8E-B86D-23711DB64A8D}")
CUPRESSUS = ("{D49B152B-463B-4654-A7B0-9AEA48A27215}",)
# Each stock tree's own size in m (bglindex.bout record, tag 0x21, a float; read 2026-11-25).  Placed at scale 1 they stood 2 to 5 times
# their crowns in the sim (the cypress about 60 m, as its 62.5 here), so the field is taken as the model's height and each tree is
# scaled to its 2018 crown.
SIZE = {PINUS[0]: 41.5, PINUS[1]: 19.9, PINUS[2]: 34.0, PINUS[3]: 30.6, POPULUS[0]: 26.2, POPULUS[1]: 25.4,
        BETULA[0]: 28.5, BETULA[1]: 28.9, BETULA[2]: 18.4, BETULA[3]: 30.4, CUPRESSUS[0]: 62.5}
# 2018 DSM crowns on the parcel: (lat, lon, crown height m above the DTM, species).  Spruces (pine stand-ins): the row on the north lot's
# north edge and the trees by 85 Street (the plan's starbursts there; the tall spruces right of the wing in the 2024 photo), the big pair
# west of the chapel and the blue spruces in front of it (2024 photo).  Columnar: the tree at the chapel's east corner (two columnar
# trees in the 2018 frame, one dark columnar tree in the 2024 photo).  The rest are broadleaf (the plan's circles; birch, or poplar for
# the tallest).  The shrub island in the north lot (3.5 m) and the plan's shrub beds are left out.
TREES = [
    (53.5266462, -113.4583700, 13.2, BETULA[0]), (53.5266757, -113.4580972, 9.9, PINUS[0]), (53.5266791, -113.4579711, 9.5, PINUS[1]),
    (53.5267104, -113.4577950, 10.7, PINUS[2]), (53.5264618, -113.4583895, 16.3, POPULUS[0]), (53.5262034, -113.4587713, 9.1, PINUS[3]),
    (53.5262511, -113.4582359, 9.4, BETULA[1]), (53.5260091, -113.4594888, 10.7, BETULA[2]), (53.5262814, -113.4578517, 9.5, BETULA[3]),
    (53.5261420, -113.4584209, 10.1, BETULA[0]), (53.5262299, -113.4578738, 9.8, BETULA[1]), (53.5258869, -113.4595873, 8.9, BETULA[2]),
    (53.5261627, -113.4579839, 12.4, POPULUS[1]), (53.5261651, -113.4578094, 19.1, PINUS[0]), (53.5258265, -113.4594452, 8.1, BETULA[3]),
    (53.5261014, -113.4577934, 18.2, PINUS[1]), (53.5257766, -113.4594042, 10.0, PINUS[2]), (53.5257809, -113.4593265, 9.1, BETULA[0]),
    (53.5258070, -113.4591798, 18.2, PINUS[3]), (53.5257504, -113.4593911, 10.1, BETULA[1]), (53.5260323, -113.4578068, 17.6, PINUS[0]),
    (53.5257913, -113.4591080, 17.1, PINUS[1]), (53.5256872, -113.4589439, 10.5, PINUS[2]), (53.5256229, -113.4582886, 13.6, CUPRESSUS[0]),
    (53.5255627, -113.4584662, 12.6, PINUS[3]), (53.5254294, -113.4588946, 6.0, BETULA[2]), (53.5253864, -113.4587613, 6.7, BETULA[3]),
]
# Front drive, inner stall row: centre line through the cars on the 2019 aerial (east, north m from LAT0 / LON0), west end along the
# plan's inner kerb.  The outer row is 12.5 m further out (a 7 m aisle between), as far east as the plan's outer kerb allows.
CURVE = [(-14.0, -44.0), (-3.0, -44.5), (7.3, -42.7), (16.7, -40.0), (22.0, -37.3), (26.0, -34.0), (30.0, -30.7), (33.3, -27.3),
         (36.0, -24.7), (38.7, -19.3), (41.3, -16.0)]
OUTER_TO = 5                                 # outer row along CURVE[:OUTER_TO + 1]


def to_xz(u, v):
    """Building frame -> site frame (x east, z north)."""
    c, s = math.cos(TH), math.sin(TH)
    return (u * c - v * s, u * s + v * c)


def to_uv(x, z):
    c, s = math.cos(TH), math.sin(TH)
    return (x * c + z * s, -x * s + z * c)


# the chapel's front bay, (u, v): back east, front east, front west, back west.  The OSM bump (outline nodes 23 to 26: (-2.59, -18.84),
# (-3.67, -24.86), (-15.44, -24.99), (-16.40, -18.84)) narrows toward the front; this is it squared at the front (v -25.0, the face) and
# set 3 to 8 cm outside it, back to the chapel's front wall at v -18.8.
BAY = [(-2.52, -18.8), (-3.72, -25.0), (-15.48, -25.0), (-16.44, -18.8)]


def bay_u(a, b, v):
    """u on the line a -> b at v."""
    return a[0] + (b[0] - a[0]) * (v - a[1]) / (b[1] - a[1])


def out_of(a, b):
    """Outward unit normal (u, v) of a bay edge a -> b (edges run clockwise in u, v, as the front from west to east)."""
    du, dv = b[0] - a[0], b[1] - a[1]
    ln = math.hypot(du, dv)
    return (dv / ln, -du / ln)


def solid(m, uv, y0, y1, sw, sw_top=None):
    """Simple polygon in the building frame (u, v), concave allowed, extruded from y0 to y1: walls face out edge by edge, the top is
    ear-clipped."""
    pts = [to_xz(u, v) for u, v in uv]
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(pts, pts[1:] + pts[:1]))
    sgn = 1.0 if area > 0 else -1.0                       # counter-clockwise: outward normal of edge a->b is (dz, -dx)
    for a, b in zip(pts, pts[1:] + pts[:1]):
        dx, dz = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dz) or 1.0
        c = ((a[0] + b[0]) / 2 - sgn * dz / ln, (y0 + y1) / 2, (a[1] + b[1]) / 2 + sgn * dx / ln)
        m.poly([(a[0], y0, a[1]), (b[0], y0, b[1]), (b[0], y1, b[1]), (a[0], y1, a[1])], sw, c)
    for i, j, k in triangulate(pts):
        tri = [pts[i], pts[j], pts[k]]
        cx, cz = sum(p[0] for p in tri) / 3, sum(p[1] for p in tri) / 3
        m.poly([(p[0], y1, p[1]) for p in tri], sw if sw_top is None else sw_top, (cx, y1 - 1.0, cz))


def ubox(m, u0, u1, v0, v1, y0, y1, sw, sw_top=None):
    solid(m, [(u0, v0), (u1, v0), (u1, v1), (u0, v1)], y0, y1, sw, sw_top)


def face_quad(m, a, b, y0, y1, out, off, sw):
    """Flat quad on a wall from (u, v) a to b, y0..y1, `off` m proud of it along the outward unit normal `out` (u, v)."""
    pa = to_xz(a[0] + out[0] * off, a[1] + out[1] * off)
    pb = to_xz(b[0] + out[0] * off, b[1] + out[1] * off)
    cin = to_xz((a[0] + b[0]) / 2 - out[0], (a[1] + b[1]) / 2 - out[1])
    m.poly([(pa[0], y0, pa[1]), (pb[0], y0, pb[1]), (pb[0], y1, pb[1]), (pa[0], y1, pa[1])], sw, (cin[0], (y0 + y1) / 2, cin[1]))


def light(m, u, v, y, cd, cone, rot=DOWN):
    x, z = to_xz(u, v)
    m.lights.append((x, y, z, cd, cone, False, rot))


def wall_pack(m, a, out, y):
    """Small dark fixture on a wall at (u, v) a, lens lit at night, with a downward street light."""
    u, v = a[0] + out[0] * 0.2, a[1] + out[1] * 0.2
    pu, pv = -out[1], out[0]
    c = (u, v)
    q = [(c[0] - pu * 0.2 - out[0] * 0.2, c[1] - pv * 0.2 - out[1] * 0.2), (c[0] + pu * 0.2 - out[0] * 0.2, c[1] + pv * 0.2 - out[1] * 0.2),
         (c[0] + pu * 0.2 + out[0] * 0.2, c[1] + pv * 0.2 + out[1] * 0.2), (c[0] - pu * 0.2 + out[0] * 0.2, c[1] - pv * 0.2 + out[1] * 0.2)]
    solid(m, q, y, y + 0.3, DGREY)
    m.mat = "glow_lamp"
    face_quad(m, q[2], q[3], y - 0.02, y + 0.12, out, 0.01, GREY)
    m.mat = None
    light(m, c[0] + out[0] * 0.3, c[1] + out[1] * 0.3, y - 0.1, 1500.0, 120.0)


def window_band(m, a, b, out, lit_every=2, w=2.4, h=1.4, sill=0.9, pitch=3.6, end=1.5):
    """Windows along the wall a -> b of a low wing, each between brick piers that stand 0.25 m proud (the 2020 photo), with a white
    panel under it; every `lit_every`-th window is lit at night."""
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    if L < w + 2 * end:
        return
    du, dv = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    n = int((L - 2 * end - w) // pitch) + 1
    s0 = (L - (n - 1) * pitch - w) / 2
    for i in range(n):
        s = s0 + i * pitch
        p0, p1 = (a[0] + du * s, a[1] + dv * s), (a[0] + du * (s + w), a[1] + dv * (s + w))
        face_quad(m, p0, p1, G + 0.3, G + sill, out, 0.05, WHITE)
        m.mat = "glow" if i % lit_every == 0 else None
        face_quad(m, p0, p1, G + sill, G + sill + h, out, 0.05, GLASS)
        m.mat = None
        q0 = (a[0] + du * (s + w), a[1] + dv * (s + w))
        q1 = (a[0] + du * (s + w + 0.6), a[1] + dv * (s + w + 0.6))
        if i < n - 1:
            solid(m, [q0, q1, (q1[0] + out[0] * 0.25, q1[1] + out[1] * 0.25), (q0[0] + out[0] * 0.25, q0[1] + out[1] * 0.25)],
                  -0.5, LOW - 0.45, BUFF)


def bands(fr, pts, half, title):
    """Car-park quads along a centre line (east, north m), about 11 m long, `half` m each side."""
    out = []
    for k in range(0, len(pts) - 1, 2):
        seg = pts[k:k + 3]
        a, b = seg[0], seg[-1]
        dx, dz = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dz)
        nx, nz = -dz / ln * half, dx / ln * half
        q = [(a[0] + nx, a[1] + nz), (b[0] + nx, b[1] + nz), (b[0] - nx, b[1] - nz), (a[0] - nx, a[1] - nz)]
        out.append(("%s %s %d" % (CODE, title, k // 2 + 1), [fr.ll(x, z) for x, z in q]))
    return out


def offset(pts, d):
    """Polyline moved d m to the right of travel (away from the building for CURVE, which runs west to east round the south side)."""
    res = []
    for i, p in enumerate(pts):
        a, b = pts[max(i - 1, 0)], pts[min(i + 1, len(pts) - 1)]
        dx, dz = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dz)
        res.append((p[0] + dz / ln * d, p[1] - dx / ln * d))
    return res


def build():
    fr = Frame(LAT0, LON0)
    outline = [fr.en(*p) for p in find_way(F, 322965284)][:-1]
    fp = [to_uv(*p) for p in outline]
    m = BMesh()

    # one-storey wings: the whole outline, buff brick, pale membrane roof, deep brown fascia (photos)
    solid(m, fp, -2.0, LOW, BUFF, sw_top=LROOF)
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(fp, fp[1:] + fp[:1]))
    sgn = 1.0 if area > 0 else -1.0
    edges = []
    for a, b in zip(fp, fp[1:] + fp[:1]):
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        out = (sgn * (b[1] - a[1]) / L, -sgn * (b[0] - a[0]) / L)
        edges.append((a, b, out, L))

    def in_box(a, b, u0, u1, v0, v1):
        mu, mv = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        return u0 - 0.3 <= mu <= u1 + 0.3 and v0 - 0.3 <= mv <= v1 + 0.3
    for a, b, out, L in edges:
        if in_box(a, b, -16.5, -3.6, -25.2, -18.7):        # the chapel's front bay
            continue
        if in_box(a, b, -2.7, 3.7, -18.9, -18.7):          # the entrance glazing
            continue
        if L >= 6.0:
            window_band(m, a, b, out)
    for a, b, out, L in edges:                              # the low roof's fascia, except round the bay (inside the chapel there)
        if not in_box(a, b, -16.5, -2.5, -25.2, -18.7):
            face_quad(m, a, b, LOW - 0.45, LOW, out, 0.12, BRONZE)

    # lettering panel at the east end of the front: 0.5 m higher, two lines of bronze letters (a strip each) on its -v face
    ubox(m, 23.5, 34.8, -17.2, -12.0, -1.0, LOW + 0.5, BUFF, sw_top=LROOF)
    face_quad(m, (23.5, -17.2), (34.8, -17.2), LOW, LOW + 0.5, (0.0, -1.0), 0.12, BRONZE)
    for y in (G + 2.35, G + 1.85):
        face_quad(m, (25.0, -17.2), (33.3, -17.2), y, y + 0.28, (0.0, -1.0), 0.04, BRONZE)

    # cultural hall: buff brick block, flat roof, a brown fascia; clerestory band on its south face above the low roof
    ubox(m, -24.5, 5.0, -4.5, 17.0, 0.0, HALL, BUFF, sw_top=LROOF)
    for a, b, out in (((-24.5, 17.0), (5.0, 17.0), (0, 1)), ((5.0, -4.5), (-24.5, -4.5), (0, -1)), ((-24.5, -4.5), (-24.5, 17.0), (-1, 0)),
                      ((5.0, 17.0), (5.0, -4.5), (1, 0))):
        face_quad(m, a, b, HALL - 0.5, HALL, out, 0.1, BRONZE)
    m.mat = "glow"
    face_quad(m, (-2.5, -4.5), (4.2, -4.5), LOW + 1.0, LOW + 2.2, (0, -1), 0.04, GLASS)
    m.mat = None

    # chapel: main block and front bay, buff brick; the bay's front is beige panels between white pilasters, brick piers at the corners
    ubox(m, -18.5, -3.0, -18.8, -4.5, 0.0, CHAPEL, BUFF, sw_top=LROOF)
    # the bay follows the OSM bump, which narrows toward the front (its sides splay out to the chapel), and stops at the chapel's front
    # wall.  A rectangle here let the low roof's splayed walls and fascia show through its sides and front, ran 0.8 m into the chapel,
    # and the canopy ran into it.  It is set a few cm outside the bump so the low roof's walls there stay hidden.
    solid(m, BAY, -2.0, CHAPEL, BUFF, sw_top=LROOF)
    m.mat = "glow_wash"
    face_quad(m, (-14.2, -25.0), (-4.9, -25.0), G, CHAPEL - 0.6, (0, -1), 0.05, CREAM)
    for k in range(6):
        uu = -14.2 + k * (9.3 / 5)
        face_quad(m, (uu - 0.12, -25.0), (uu + 0.12, -25.0), G, CHAPEL - 0.6, (0, -1), 0.09, WHITE)
    m.mat = None
    bay_e, bay_w = (BAY[1], BAY[0]), (BAY[3], BAY[2])       # front to back on the east side, back to front on the west
    for a, b, out in ((BAY[2], BAY[1], (0, -1)), (*bay_e, out_of(*bay_e)), (*bay_w, out_of(*bay_w)),
                      ((-18.5, -4.5), (-3.0, -4.5), (0, 1)), ((-3.0, -18.8), (-3.0, -4.5), (1, 0)), ((-18.5, -18.8), (-18.5, -4.5), (-1, 0)),
                      ((-18.5, -18.8), BAY[3], (0, -1))):
        face_quad(m, a, b, CHAPEL - 0.6, CHAPEL, out, 0.1, BRONZE)
    # tall narrow windows on the bay's east side (Mapillary 2018) and a clerestory row on the main block's east wall above the low roof
    m.mat = "glow"
    for vv in (-23.6, -20.6):
        face_quad(m, (bay_u(BAY[1], BAY[0], vv), vv), (bay_u(BAY[1], BAY[0], vv + 0.9), vv + 0.9), G + 1.0, CHAPEL - 1.2,
                  out_of(*bay_e), 0.04, GLASS)
    for vv in (-16.5, -13.0, -9.5, -6.0):
        face_quad(m, (-3.0, vv), (-3.0, vv + 1.2), LOW + 0.8, CHAPEL - 1.0, (1, 0), 0.04, GLASS)
    m.mat = None

    # entrance: glazed doors and side lights under a flat canopy with a lit soffit and two downlights (night photo, "9010 - 85 ST.")
    m.mat = "glow"
    face_quad(m, (-2.2, -18.8), (3.2, -18.8), G, G + 2.6, (0, -1), 0.05, GLASS)
    m.mat = None
    face_quad(m, (-2.2, -18.8), (3.2, -18.8), G + 2.6, G + 2.75, (0, -1), 0.06, WHITE)
    face_quad(m, (-0.2, -18.8), (1.2, -18.8), G + 2.15, G + 2.45, (0, -1), 0.08, DARK)     # address board
    # the canopy's west edge runs along the bay's splayed east wall, 3 cm off it (it ran 0.3 m into the bay as a rectangle)
    cy0, cy1 = G + 3.0, G + 3.45
    cw0, cw1 = bay_u(BAY[1], BAY[0], -21.8) + 0.03, bay_u(BAY[1], BAY[0], -18.8) + 0.03
    solid(m, [(cw0, -21.8), (3.6, -21.8), (3.6, -18.8), (cw1, -18.8)], cy0, cy1, WHITE, sw_top=LROOF)
    face_quad(m, (cw0, -21.8), (3.6, -21.8), cy0, cy1, (0, -1), 0.04, BRONZE)
    m.mat = "glow"
    pts = [to_xz(u, v) for u, v in ((bay_u(BAY[1], BAY[0], -21.6) + 0.2, -21.6), (3.4, -21.6), (3.4, -18.9),
                                    (bay_u(BAY[1], BAY[0], -18.9) + 0.2, -18.9))]
    m.poly([(x, cy0 - 0.02, z) for x, z in pts], WHITE, (pts[0][0], cy0 + 1.0, pts[0][1]))
    m.mat = "glow_lamp"
    for uu in (-1.0, 2.0):
        pts = [to_xz(u, v) for u, v in ((uu - 0.2, -20.5), (uu + 0.2, -20.5), (uu + 0.2, -20.1), (uu - 0.2, -20.1))]
        m.poly([(x, cy0 - 0.04, z) for x, z in pts], WHITE, (pts[0][0], cy0 + 1.0, pts[0][1]))
        light(m, uu, -20.3, cy0 - 0.1, 2500.0, 130.0)
    m.mat = None
    for uu in (bay_u(BAY[1], BAY[0], -21.6) + 0.3, 3.4):                      # canopy posts, the west one clear of the bay
        ubox(m, uu - 0.1, uu + 0.1, -21.7, -21.5, G, cy0, WHITE)

    # spire: a brick shaft of three fins with stepped tops (photos), floodlit at night, a steel needle on the middle fin
    m.mat = "glow_flood"
    ubox(m, 3.9, 6.1, -16.6, -15.3, -2.0, SPIRE - 1.2, BUFF, sw_top=BUFF)    # back of the shaft
    for u0, u1, top in ((3.9, 4.55, SPIRE - 0.7), (4.7, 5.3, SPIRE), (5.45, 6.1, SPIRE - 0.35)):
        ubox(m, u0, u1, -17.9, -16.5, -2.0, top, BUFF, sw_top=BUFF)
    m.mat = None
    ubox(m, 4.92, 5.08, -17.28, -17.12, SPIRE, NEEDLE, WHITE)
    for uu in (4.2, 5.8):                                                      # uplights at the foot of the spire
        light(m, uu, -18.6, G + 0.2, 3000.0, 25.0, UP)
    for uu in (-12.5, -9.5, -6.5):                                             # uplights washing the chapel face
        light(m, uu, -26.2, G + 0.2, 1500.0, 40.0, UP)

    # wall packs (courtyard photo): on the west, north and east faces and the front of the east wing, over the lots and walks
    for a, out in (((-31.5, 0.0), (-1, 0)), ((-31.5, 14.0), (-1, 0)), ((-14.0, 23.7), (0, 1)), ((0.0, 23.7), (0, 1)),
                   ((34.8, -4.0), (1, 0)), ((34.8, 8.0), (1, 0)), ((12.0, -15.2), (0, -1)), ((20.0, -15.2), (0, -1)),
                   ((14.5, 0.7), (0, -1)), ((-25.0, -18.5), (0, -1))):
        wall_pack(m, a, out, LOW - 0.9)

    # car parks
    pp = json_plan()
    car_parks = []
    for lot in pp["parking_lots_2015_proposed"]:
        if lot["id"] == "east_curve_lot":                  # drawn about 5 m too far out on the plan: use the rows below
            continue
        ring = [fr.en(*p) for p in lot["polygon"]]
        if lot["id"] == "north_strip_row_16":              # only its west end is paved on the 2019 aerial (lawn and trees east of it)
            ring = [(x if x < 10.0 else 10.0, z) for x, z in ring]
        car_parks.append(("%s %s" % (CODE, lot["id"].replace("_", " ")), [fr.ll(x, z) for x, z in ring]))
    car_parks += bands(fr, CURVE, 2.75, "front drive inner row")
    car_parks += bands(fr, offset(CURVE[:OUTER_TO + 1], 12.5), 2.75, "front drive outer row")

    objects = [("%s tree (stock MSFS tree; 2018 crown %.0f m)" % (CODE, h), la, lo, float((k * 137) % 360), guid, round(h / SIZE[guid], 3))
               for k, (la, lo, h, guid) in enumerate(TREES)]
    parcel = find_way(F, 594346540)[:-1]
    extra = [("exclude", "%s %s parcel (sim trees and buildings)" % (CODE, TITLE), DATUM, parcel)]

    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_b276_lds_church", m)], frame=fr,
                axis=Axis([to_xz(-31.5, 0.0), to_xz(34.8, 0.0)]), car_parks=car_parks, objects=objects, terrain_extra=extra,
                views=[("a", 160.0, 14.0), ("b", 60.0, 20.0), ("c", 300.0, 40.0)], preview=dict(water=False))


def json_plan():
    import json
    return json.load(open(ROOT / "docs/edmonton-bridges/reference" / F / "geometry.json", encoding="utf-8"))["parking_plan_2015"]
