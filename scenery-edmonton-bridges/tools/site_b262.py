"""B262 Holyrood Gardens tower ("The Beacon Apartments at East Junction"), 9009 85 Street NW, on the 85 Street / Connors Road circle.

Plan: OpenStreetMap.  Way 1221215089 is the tower part, a 30.7 x 30.0 m square on 85 Street (tagged 26 levels, height 86); way
1209666933 is the whole building, which adds the low wing at the back (east), 16.3 x 21.5 m.  City permits: building 1 is 26 storeys
(2023 revision); DC2 caps building type E at 86.0 m and its floor plate above 22.0 m at 750 m2.  The 2018 LiDAR predates the tower.
Ground: 2018 DTM inside the footprint 664.56 to 665.12 m (median 664.86).

The form is from the developer's rendering (DER + Associates, 13 Nov 2018, on SkyriseCities): a slender shaft in three vertical masses,
grey panel masses each side of a taller white-framed pale-glass centre whose frame stands proud of the roof with a yellow panel in it,
blue vertical stripes in the joints, stacked corner balconies with white slabs and glass rails, small yellow accent panels, a two-storey
podium, and a six-storey white wing.  The rendering may not match what was built (the storey count changed in 2023).  ASSUMED, no
drawings: the shaft core inset (1.5 m street side, 3.5 m back), the split of the masses, the mass heights (86.0 / 82 / 79.5 m above
grade: only the 86 m top is sourced), floor heights (4.5 m ground, 3.05 m above), podium 2 storeys, wing 6 storeys (OSM
building:levels 6 on the outline; building 2 in the permits is also 6 storeys, but it is a separate building), balcony positions.
Datum (y = 0): 664.56 m, the lowest 2018 DTM cell inside the footprint; grade is taken as y = 0.3.
"""
from bridgelib import *

CODE, TITLE = "B262", "Holyrood Gardens tower"
F = "B262-holyrood-gardens"
DATUM = 664.56
G = 0.3                        # grade above the datum
L1, FH = 4.5, 3.05             # ground storey, typical storey
NFL = 26
POD = G + L1 + FH + 0.3        # podium roof (two storeys)
TOP_C, TOP_S, TOP_N = G + 86.0, G + 82.0, G + 79.5
WING = G + L1 + 5 * FH + 1.0   # six storeys and a parapet
BAL = 1.5                      # balcony depth = shaft inset on the street side


def floor_y(k):
    """Floor level of storey k (1 = ground)."""
    return G if k == 1 else G + L1 + (k - 2) * FH


def box(m, x0, x1, z0, z1, y0, y1, sw, sw_top=None):
    prism(m, [(x0, z0), (x1, z0), (x1, z1), (x0, z1)], y0, y1, sw, sw_top)


def ring_bands(m, x0, x1, z0, z1, y0, y1, sw, off=0.05, faces="wens"):
    """Thin skin quads on the faces of an axis-aligned block (window bands, slab edges), `off` proud of the wall."""
    cx, cz, cy = (x0 + x1) / 2, (z0 + z1) / 2, (y0 + y1) / 2
    X0, X1, Z0, Z1 = x0 - off, x1 + off, z0 - off, z1 + off
    if "w" in faces:
        m.poly([(X0, y0, z0), (X0, y0, z1), (X0, y1, z1), (X0, y1, z0)], sw, (cx, cy, cz))
    if "e" in faces:
        m.poly([(X1, y0, z0), (X1, y0, z1), (X1, y1, z1), (X1, y1, z0)], sw, (cx, cy, cz))
    if "s" in faces:
        m.poly([(x0, y0, Z0), (x1, y0, Z0), (x1, y1, Z0), (x0, y1, Z0)], sw, (cx, cy, cz))
    if "n" in faces:
        m.poly([(x0, y0, Z1), (x1, y0, Z1), (x1, y1, Z1), (x0, y1, Z1)], sw, (cx, cy, cz))


def balcony(m, x0, x1, z0, z1, y, open_sides):
    """Slab x0..x1 / z0..z1 at floor level y, glass rails on the open sides ('w', 'e', 's', 'n')."""
    box(m, x0, x1, z0, z1, y - 0.25, y, WHITEST)
    t, h = 0.06, 1.1
    if "w" in open_sides:
        box(m, x0, x0 + t, z0, z1, y, y + h, GLASSLT)
    if "e" in open_sides:
        box(m, x1 - t, x1, z0, z1, y, y + h, GLASSLT)
    if "s" in open_sides:
        box(m, x0, x1, z0, z0 + t, y, y + h, GLASSLT)
    if "n" in open_sides:
        box(m, x0, x1, z1 - t, z1, y, y + h, GLASSLT)


def parapet(m, x0, x1, z0, z1, y0, top, sw, sides="wens", t=0.3, off=0.1, rise=0.4):
    """Parapet round the roof of the block x0..x1 / z0..z1 whose roof is at `top`: edge walls `t` thick, `off` proud of the faces, from
    y0 to `rise` above the roof, on the given sides.  No face lies in the roof plane (the solid caps this replaces had their tops in
    it and z-fought with the roof from above in the sim)."""
    y1 = top + rise
    zw0 = z0 - off if "s" in sides else z0
    zw1 = z1 + off if "n" in sides else z1
    if "w" in sides:
        box(m, x0 - off, x0 + t, zw0, zw1, y0, y1, sw)
    if "e" in sides:
        box(m, x1 - t, x1 + off, zw0, zw1, y0, y1, sw)
    xs0 = x0 + t if "w" in sides else x0
    xs1 = x1 - t if "e" in sides else x1
    if "s" in sides:
        box(m, xs0, xs1, z0 - off, z0 + t, y0, y1, sw)
    if "n" in sides:
        box(m, xs0, xs1, z1 - t, z1 + off, y0, y1, sw)


def build():
    whole = find_way(F, 1209666933)
    tower = find_way(F, 1221215089)
    lat0 = sum(p[0] for p in whole[:-1]) / (len(whole) - 1)
    lon0 = sum(p[1] for p in whole[:-1]) / (len(whole) - 1)
    fr = Frame(lat0, lon0)
    te = [fr.en(*p) for p in tower]
    we = [fr.en(*p) for p in whole]
    # the OSM ways are drawn square to the compass (edges at 0 / 90 deg within 0.1 deg), so work in axis-aligned boxes
    tx0, tx1 = min(p[0] for p in te), max(p[0] for p in te)
    tz0, tz1 = min(p[1] for p in te), max(p[1] for p in te)
    wx1 = max(p[0] for p in we)
    wz0 = min(p[1] for p in we if p[0] > tx1 + 1.0)
    wz1 = max(p[1] for p in we if p[0] > tx1 + 1.0)
    g = (tx0, tx1, tz0, tz1, wx1, wz0, wz1)
    # Lower LODs keep the tower in view from the downtown approaches, 5 nm and more.  MSFS 2024 holds a model back until it fills a
    # share of the screen set by its vertex count: the full model (about 11,000 vertices) needs about 4 %, about 1 nm out, which is
    # where it popped in.  LOD 1 (no balcony rails) needs about 2 %.  LOD 2 is under 1,000 vertices, which has no floor.
    lods = [(2.0, model(*g, lod=1)), (0.0, model(*g, lod=2))]
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=DATUM, parts=[("br_b262_holyrood_gardens", model(*g), lods, 4.0)],
                frame=fr, axis=Axis([(tx0, 0.0), (wx1, 0.0)]),
                views=[("a", 225.0, 12.0), ("b", 60.0, 18.0), ("c", 300.0, 45.0)])


def model(tx0, tx1, tz0, tz1, wx1, wz0, wz1, lod=0):
    """The building at LOD 0 (full), 1 (balcony slabs without their glass rails, which are most of the vertices) or 2 (far: the
    masses, the crown frame, the stripes and parapets; no balconies, window bands or accent panels)."""
    far = lod >= 2
    m = BMesh()
    # podium: the tower square, two storeys, storefront / townhouse bands
    box(m, tx0, tx1, tz0, tz1, -2.0, POD, METAL, sw_top=LROOF)
    if not far:
        ring_bands(m, tx0, tx1, tz0, tz1, G + 0.6, G + L1 - 0.8, SLATE)
        ring_bands(m, tx0, tx1, tz0, tz1, G + L1 + 0.7, G + L1 + 2.4, SLATE)
        for zz in (tz0 + 4.0, tz0 + 13.0, tz0 + 22.0):        # brick townhouse bays on the street face
            box(m, tx0 - 0.3, tx0 + 0.2, zz, zz + 4.0, G, POD - 0.4, BRICK)

    # shaft core: 1.5 m in from the street, south and north faces (balconies reach the OSM line), 3.5 m in at the back
    cx0, cx1, cz0, cz1 = tx0 + BAL, tx1 - 3.5, tz0 + BAL, tz1 - BAL
    zs, zn = cz0 + 8.7, cz0 + 19.2                        # joints: south grey mass | white centre | north mass
    # the rendering's south mass is grey panel for its lower two-thirds and white-framed pale glass above (from storey 18, assumed)
    split_s = floor_y(18)
    masses = [("s", cz0, zs, TOP_S, split_s), ("c", zs, zn, TOP_C - 4.0, POD), ("n", zn, cz1, TOP_N, TOP_N)]
    for key, z0, z1, top, split in masses:
        if split > POD:
            box(m, cx0, cx1, z0, z1, POD - 0.3, split, METAL, sw_top=ROOF)
        if split < top:
            box(m, cx0, cx1, z0, z1, max(split, POD - 0.3), top, GLASSLT, sw_top=ROOF)
        faces = "we" + ("s" if key == "s" else "") + ("n" if key == "n" else "")
        for k in range(3, NFL + 1):
            y = floor_y(k)
            if far or y + 2.2 > top:
                break
            if y >= split - 0.1:
                ring_bands(m, cx0, cx1, z0, z1, y - 0.25, y + 0.35, WHITEST, faces=faces)     # white slab edges on the glass
            else:
                ring_bands(m, cx0, cx1, z0, z1, y + 0.7, y + 2.5, SLATE, faces=faces)       # window bands on the grey panels
        # white frame on the glass centre: corner pilasters, and the crown frame standing 4 m proud of its roof, open to the
        # west and east, with the yellow panel set back in it
        if key == "c":
            for zz in (z0, z1 - 1.2):
                box(m, cx0 - 0.15, cx1 + 0.15, zz, zz + 1.2, POD, TOP_C, WHITEST)
            for x0, x1 in ((cx0 - 0.15, cx0 + 1.2), (cx1 - 1.2, cx1 + 0.15)):        # lintels over the open west and east faces,
                box(m, x0, x1, z0 + 1.2, z1 - 1.2, TOP_C - 0.8, TOP_C, WHITEST)         # between the pilasters (no shared top)
            box(m, cx0 + 3.0, cx0 + 3.3, z0 + 2.5, z1 - 2.5, TOP_C - 4.0, TOP_C - 0.8, YELLOW)
            box(m, cx1 - 3.3, cx1 - 3.0, z0 + 2.5, z1 - 2.5, TOP_C - 4.0, TOP_C - 0.8, YELLOW)
            box(m, cx0 + 6.0, cx1 - 6.0, z0 + 1.5, z1 - 1.5, TOP_C - 4.0, TOP_C - 1.5, METAL, sw_top=ROOF)   # plant room
        else:
            # parapet cap on the exposed faces, 0.4 m above the roof; the face against the white centre is left out (the south mass is
            # level with the centre's roof, the north mass below it)
            parapet(m, cx0, cx1, z0, z1, top - 1.6, top, WHITEST if key == "n" else METAL, sides=faces)
    # blue stripes in the two joints, street and back faces
    for zz in (zs, zn):
        for x0, x1 in ((cx0 - 0.25, cx0 + 0.3), (cx1 - 0.3, cx1 + 0.25)):
            box(m, x0, x1, zz - 0.6, zz + 0.6, POD, TOP_S - 2.0, BLUE)

    # balconies, storeys 3 to 25: wrapped round the four corners of the shaft, plus a stack on the street face of the centre
    bal = balcony if lod == 0 else (lambda m_, x0, x1, z0, z1, y_, _sides: box(m_, x0, x1, z0, z1, y_ - 0.25, y_, WHITEST))
    for k in range(3, NFL if not far else 3):
        y = floor_y(k)
        bal(m, tx0, cx0, tz0, cz0 + 7.0, y, "ws")              # south-west corner
        bal(m, cx0, cx0 + 8.0, tz0, cz0, y, "s")
        bal(m, tx0, cx0, cz1 - 6.0, tz1, y, "wn")              # north-west corner
        bal(m, cx0, cx0 + 7.0, cz1, tz1, y, "n")
        bal(m, cx1 - 8.0, cx1, tz0, cz0, y, "s")               # back corners (south-east, north-east)
        bal(m, cx1 - 7.0, cx1, cz1, tz1, y, "n")
        bal(m, tx0, cx0, zs + 2.2, zn - 2.2, y, "w")           # centre stack, street face
        # yellow accent panels: every second storey, on the corner panels next to the south-west and north-east balconies
        if k % 2:
            box(m, cx0 + 8.3, cx0 + 9.9, cz0 - 0.12, cz0, y + 0.6, y + 2.4, YELLOW)
            box(m, cx1 + 0.0, cx1 + 0.12, cz1 - 9.5, cz1 - 7.9, y + 0.6, y + 2.4, YELLOW)

    # the six-storey wing at the back (east): white, a grey band and a blue stripe, window bands, yellow balcony panels
    box(m, tx1, wx1, wz0, wz1, -2.0, WING, WHITEST, sw_top=ROOF)
    box(m, tx1, wx1 + 0.08, wz0 - 0.08, wz1 + 0.08, G, G + L1 - 0.5, METAL)          # proud of the east face too, not in its plane
    if not far:
        for k in range(2, 7):
            y = floor_y(k)
            ring_bands(m, tx1, wx1, wz0, wz1, y + 0.7, y + 2.4, SLATE, faces="ens")
    box(m, tx1 + 7.4, tx1 + 8.6, wz0 - 0.25, wz0 + 0.3, G, WING - 1.0, BLUE)         # up to the parapet, clear of the roof
    if not far:
        for k in (3, 5):
            y = floor_y(k)
            box(m, wx1 - 4.6, wx1 - 1.0, wz0 - 0.25, wz0 + 0.3, y + 0.5, y + 2.5, YELLOW)
    parapet(m, tx1, wx1, wz0, wz1, WING - 1.0, WING, METAL)
    return m
