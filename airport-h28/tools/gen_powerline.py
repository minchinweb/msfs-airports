"""Generate the H28 power lines (own pole and wire models, orange marker balls) and the port pole lights, and place them
in H28.xml between BEGIN/END markers. Run gen_port.py first (it owns the palette), then:
    python -I airport-h28/tools/gen_powerline.py
Routing (docs/h28/powerline-routing-2025.png, drawn by docs/h28/powerline_map.py from the user's review of the Esri
frame, the Sep 2025 Street View streetview-2025-09-*, the CLUI 2014 photo and the mindtrip aerial), two separate systems:
- US line, two wires on cross-arms: a pole in the trees west of the road just south of the border, over the road (one
  ball over its middle) to the transformer pole in the US parking 33 m east of the west fence and 70 ft (21 m) south of
  the centreline (FAA remark: P-line 31 ft high, 70 ft right of the centreline, red balls), east (three balls) to a pole
  by the windsock, then due south across the US fields (US_SOUTH poles, about 77 m apart).
- Canadian line, four wires stacked on one side of short poles (a low-voltage rack): from a pole north of the CBSA
  garages south behind (east of) all the port buildings to a dead-end pole just north of the Canadian pocket, guyed
  south to an anchor just inside the pocket's north fence. It does not run up the highway; its feed is not seen.
- Road lights at the border: one on the east shoulder just north of the border (red beacon), with a single wire to the
  transformer pole, and two on the west shoulder either side of the border, joined by a single wire and fed from the
  US line's west pole (that drop is assumed).
Wires hang from the cross-arm ends at 9.5 m (31 ft) with a small sag; the poles are built to that height, so wires and
cross-arms line up (the library pole was about twice as tall as the old 9.4 m wires).
Lights: night-only MSFS 2024 street lights with lens flare, so they show from a distance and lead pilots to the runway:
four 8 m plaza lights by each port's inspection lane, and 10 m highway lights along the road, one of them at the border
by the runway's west end. Each port's lamps (and the road lights on its side of the border) are one model, as wide as the
plaza: the sim culls a lone lamp post, and its lights with it, about 1 NM out (it drops models by their size on screen).
A merged model is placed at one altitude, so each lamp is raised or lowered by the ground height at its post relative to
the model's origin (USGS 3DEP 1 m LiDAR, which covers both sides of the border here; cached in ground.json), and its
pole runs on below ground to hide the difference between that and the sim's terrain."""
import json
import math
import urllib.request
import re
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_field as gf  # noqa: E402
import gen_port as gp  # noqa: E402

LAT, LON = gp.LAT, gp.LON
HEIGHT, ARM = 9.5, 1.0  # wire attachment height and half cross-arm (metres)
ROAD = -112.78826  # east shoulder of the highway
ROAD_C = -112.78840  # road centre (checked on a DevMode top-down shot, see gen_port.py)
SOUTH = gf.CL - 70 * 0.3048 / LAT  # 70 ft right of the 07 centreline
DROP = 8.6  # height of the single light-feed wires (below the cross-arm, above the transformer can)
RACK = (8.4, 7.9, 7.4, 6.9)  # Canadian line: wire heights on the rack
TX, SOCK = "transformer pole, US parking", "pole by the windsock, the line turns south"
WEST = "US line west pole, in the trees west of the road"
US_SPACING, US_SOUTH = 77.0, 10  # from the review: poles 78 m and 147 m south of the windsock pole; ten poles south
# (title, lat, lon, kind): kind is plain, tx (transformer), rack or rack_end (Canadian, the last one guyed)
US_POLES = ([(WEST, SOUTH, ROAD_C - 40 / LON, "plain"), (TX, SOUTH, gf.WF + 33 / LON, "tx"),
             (SOCK, SOUTH, gf.WF + 137 / LON, "plain")]
            + [(f"US line pole {k} south of the windsock", SOUTH - US_SPACING * k / LAT, gf.WF + 137 / LON, "plain")
               for k in range(1, US_SOUTH + 1)])
# The CBSA model reaches 43.6 m east of the west fence (its north garage; the radio mast is at about 31 m), so the line
# runs 48 m east, behind all of it. North of the border, in metres: north end past the north garage (175.7), dead end
# 7 m north of the pocket fence with the guy anchored 1 m inside it.
CA_EAST = gf.WF + 48 / LON
CA_POLES = [("Canadian line north end, past the CBSA garages", gf.BORDER + 185 / LAT, CA_EAST, "rack"),
            ("Canadian line pole behind the CBSA office", gf.BORDER + 135 / LAT, CA_EAST, "rack"),
            ("Canadian line pole behind the CBSA sheds", gf.BORDER + 88 / LAT, CA_EAST, "rack"),
            ("Canadian line dead-end pole north of the pocket (guyed south)", gf.POCKET_N + 7 / LAT, CA_EAST, "rack_end")]
GUY = 6.0  # m from the dead-end pole to its anchor
FLARE = 60000.0  # cd, the flare-only light on each lamp (the downward light alone shows no flare from the side)
SINK = 4.0  # m of lamp pole below ground (covers the sim terrain differing from the LiDAR)
GROUND = Path(__file__).resolve().parent / "ground.json"
# balls at these fractions along a span: one over the middle of the road, three between the transformer and windsock poles
BALL_SPANS = {(WEST, TX): [(ROAD_C - US_POLES[0][2]) / (US_POLES[1][2] - US_POLES[0][2])], (TX, SOCK): [0.25, 0.5, 0.75]}
BEGIN = "<!-- BEGIN power line and pole lights (generated by airport-h28/tools/gen_powerline.py) -->"
END = "<!-- END power line and pole lights -->"


def tube(m, x, pts, w=0.02):
    """Thin wire as two crossed ribbons, each double-sided."""
    for (ya, za), (yb, zb) in zip(pts, pts[1:]):
        for quad in ([(x - w, ya, za), (x + w, ya, za), (x + w, yb, zb), (x - w, yb, zb)],
                     [(x, ya - w, za), (x, ya + w, za), (x, yb + w, zb), (x, yb - w, zb)]):
            m.poly(quad, gp.DARK)
            m.poly(quad[::-1], gp.DARK)


def ball(m, cx, cy, cz, r=0.3, n=8):
    ring = lambda k: (r * math.sin(math.pi * k / n), r * math.cos(math.pi * k / n))  # noqa: E731
    for k in range(n):
        (r0, y0), (r1, y1) = ring(k), ring(k + 1)
        for i in range(n):
            a0, a1 = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n
            p = lambda rr, y, a: (cx + rr * math.cos(a), cy + y, cz + rr * math.sin(a))  # noqa: E731
            m.poly([p(r0, y0, a0), p(r1, y1, a0), p(r1, y1, a1), p(r0, y0, a1)], gp.ORANGE)
            m.poly([p(r0, y0, a1), p(r1, y1, a1), p(r1, y1, a0), p(r0, y0, a0)], gp.ORANGE)


def span(length, balls=(), dh=0.0, wires=((-ARM, HEIGHT), (ARM, HEIGHT))):
    """Wires (x, height) from z = 0 to z = length along +Z, sagging about 1 m per 100 m; the far end is dh higher (the
    ground there, from the LiDAR). Balls hang on the first wire with x > 0, at the given fractions along the span."""
    m = gp.Mesh()
    sag = 0.6 + 0.004 * length
    n = 12
    y = lambda h, t: h + dh * t - 4 * sag * t * (1 - t)  # noqa: E731
    for x, h in wires:
        tube(m, x, [(y(h, t / n), length * t / n) for t in range(n + 1)])
    bx, bh = next(w for w in wires if w[0] > 0) if balls else (0, 0)
    for t in balls:
        ball(m, bx, y(bh, t) - 0.3, length * t)
    return m


def octo(m, r0, r1, y0, y1, sw, n=8):
    """Tapered 8-sided post (outward faces, open top)."""
    for i in range(n):
        a0, a1 = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n
        m.poly([(r0 * math.cos(a0), y0, r0 * math.sin(a0)), (r0 * math.cos(a1), y0, r0 * math.sin(a1)),
                (r1 * math.cos(a1), y1, r1 * math.sin(a1)), (r1 * math.cos(a0), y1, r1 * math.sin(a0))][::-1], sw)
    m.poly([(r1 * math.cos(2 * math.pi * i / n), y1, r1 * math.sin(2 * math.pi * i / n)) for i in range(n)][::-1], sw)


def pole(transformer):
    """Wooden pole 10.2 m, cross-arm along X at 9.3 m, insulators up to the wire height."""
    m = gp.Mesh()
    octo(m, 0.15, 0.11, 0.0, 10.2, gp.BROWN)
    m.box(-ARM - 0.15, ARM + 0.15, 9.25, 9.37, -0.05, 0.07, gp.BROWN, bottom=True)
    for x in (-ARM, ARM):
        m.box(x - 0.04, x + 0.04, 9.37, HEIGHT, -0.04, 0.04, gp.GREY)
    m.box(-0.04, 0.04, 10.2, 10.35, -0.04, 0.04, gp.GREY)  # top insulator
    if transformer:
        m.box(-0.28, 0.28, 7.4, 8.4, 0.15, 0.7, gp.GREY, bottom=True)
    return m


def rack_pole(guyed):
    """Short wooden pole with four spool insulators stacked on its +X side (a low-voltage rack); the dead-end pole has a
    guy wire along +Z to a ground anchor GUY metres away."""
    m = gp.Mesh()
    octo(m, 0.14, 0.11, 0.0, 9.2, gp.BROWN)
    m.box(0.11, 0.16, RACK[-1] - 0.3, RACK[0] + 0.3, -0.05, 0.05, gp.STEEL)  # rack bracket
    for h in RACK:
        m.box(0.16, 0.3, h - 0.07, h + 0.07, -0.07, 0.07, gp.GREY)
    if guyed:
        tube(m, 0.0, [(RACK[0] + 0.4, 0.12), (0.25, GUY)], 0.015)
        m.box(-0.05, 0.05, 0.0, 0.3, GUY - 0.05, GUY + 0.05, gp.STEEL)  # anchor rod
    return m


def lamp(height, arm, intensity, cone, beacon=False):
    """Steel pole with an arm along +Z, a lamp head with a glowing lens and a night-only street light under it."""
    m = gp.Mesh()
    m.box(-0.1, 0.1, -SINK, height, -0.1, 0.1, gp.STEEL, top=False)
    m.box(-0.06, 0.06, height - 0.12, height, -0.06, arm, gp.STEEL)  # arm
    m.box(-0.25, 0.25, height - 0.32, height - 0.1, arm - 0.4, arm + 0.1, gp.GREY, bottom=True)  # lamp head
    m.poly([(-0.2, height - 0.33, arm + 0.05), (-0.2, height - 0.33, arm - 0.35), (0.2, height - 0.33, arm - 0.35),
            (0.2, height - 0.33, arm + 0.05)], gp.GLOW, True)
    m.lights.append((0.0, height - 0.4, arm - 0.15, intensity, cone, False))
    m.lights.append((0.0, height - 0.45, arm - 0.15, FLARE, 360.0, True))  # all-round flare, seen from the air
    if beacon:  # flashing red obstruction light on top of the pole
        m.box(-0.15, 0.15, height, height + 0.35, -0.15, 0.15, gp.REDR)
        m.lights.append((0.0, height + 0.45, 0.0, *gp.BEACON))
    return m


# Highway lights (2025 Street View: tall arm lights along AB-62/MT-213 at both ports). At the border: one on the east
# shoulder just north of it, by the runway's west end, carrying the red beacon, and two on the west shoulder either side
# of it (Street View g, h; CLUI 2014). (title, lat, lon, arm heading)
EAST_SH, WEST_SH = ROAD + 1 / LON, ROAD_C - 8 / LON
BEACON_LIGHT = "road light at the border, east shoulder, by the runway's west end"
L_EAST = (BEACON_LIGHT, gf.BORDER + 6 / LAT, EAST_SH, 270.0)
L_WEST_N = ("road light at the border, west shoulder, north", gf.BORDER + 10 / LAT, WEST_SH, 90.0)
L_WEST_S = ("road light at the border, west shoulder, south", gf.BORDER - 14 / LAT, WEST_SH, 90.0)
ROAD_LIGHTS = [L_EAST, L_WEST_N, L_WEST_S,
               ("road light, CBSA approach", 48.99905, EAST_SH, 270.0), ("road light, CBSA lane", 48.99985, EAST_SH, 270.0),
               ("road light, US side", 48.99795, EAST_SH, 270.0), ("road light, US side", 48.99740, EAST_SH, 270.0),
               ("road light, CBP approach", 48.99690, EAST_SH, 270.0)]
# single wires (from, to) between a pole or light and the next, all at DROP
FEEDS = [(L_EAST, (TX,) + US_POLES[1][1:3]), (L_WEST_S, L_WEST_N), ((WEST,) + US_POLES[0][1:3], L_WEST_S)]


def ground(lat, lon, cache={}):
    """Ground elevation (m) from the USGS Elevation Point Query Service, cached in ground.json."""
    if not cache:
        cache.update(json.loads(GROUND.read_text(encoding="utf-8")) if GROUND.exists() else {})
    key = f"{lat:.6f},{lon:.6f}"
    if key not in cache:
        url = f"https://epqs.nationalmap.gov/v1/json?x={lon:.6f}&y={lat:.6f}&units=Meters&wkid=4326"
        for attempt in range(5):  # the service often times out (HTTP 504); try again
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    cache[key] = round(float(json.load(r)["value"]), 2)
                break
            except OSError:
                if attempt == 4:
                    raise
                time.sleep(3)
        GROUND.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return cache[key]


def merge(dst, src, ox, oz, hd, oy=0.0):
    """Add src (a gp.Mesh in its own frame) to dst, turned to heading hd (clockwise from north) and moved to (ox east,
    oy up, oz north) metres."""
    c, s = math.cos(math.radians(hd)), math.sin(math.radians(hd))

    def rot(x, z):
        return x * c + z * s, -x * s + z * c

    base = len(dst.pos)
    for (x, y, z), (nx, ny, nz) in zip(src.pos, src.nrm):
        rx, rz = rot(x, z)
        dst.pos.append((ox + rx, oy + y, oz + rz))
        rnx, rnz = rot(nx, nz)
        dst.nrm.append((rnx, ny, rnz))
    dst.uv += src.uv
    dst.idx += [i + base for i in src.idx]
    dst.glow += src.glow
    for x, y, z, *rest in src.lights:
        rx, rz = rot(x, z)
        dst.lights.append((ox + rx, oy + y, oz + rz, *rest))


def bearing(a, b):
    de, dn = (b[2] - a[2]) * LON, (b[1] - a[1]) * LAT
    return math.hypot(de, dn), math.degrees(math.atan2(de, dn)) % 360


def line(poles, ml, models, tag, wires):
    out = []
    for k, (a, b) in enumerate(zip(poles, poles[1:])):
        length, hd = bearing(a, b)
        name = f"h28_wire_{tag}{k + 1}"
        dh = ground(b[1], b[2]) - ground(a[1], a[2])
        g = span(length, BALL_SPANS.get((a[0], b[0]), ()), dh, wires).save(ml / name, name)
        out.append(gf.obj(f"wires, {a[0]} to {b[0]} ({length:.0f} m)", g, a[1], a[2], hd))
    for k, p in enumerate(poles):
        hd = bearing(poles[max(k - 1, 0)], poles[min(k + 1, len(poles) - 1)])[1]
        out.append(gf.obj(p[0], models[p[3]], p[1], p[2], hd))
    return out


def main():
    ml = gp.MODELLIB
    olds = [ml / o for o in ("h28_wire_balls", "h28_wire_plain", "h28_pole_light", "h28_road_light")]  # earlier models
    for old in olds + sorted(ml.glob("h28_wire_*")):  # and every span, since their count changes with the routing
        for f in old.glob("*"):
            f.unlink()
        if old.exists():
            old.rmdir()
    models = {"plain": pole(False).save(ml / "h28_pole", "h28_pole"),
              "tx": pole(True).save(ml / "h28_pole_transformer", "h28_pole_transformer"),
              "rack": rack_pole(False).save(ml / "h28_pole_rack", "h28_pole_rack"),
              "rack_end": rack_pole(True).save(ml / "h28_pole_rack_guyed", "h28_pole_rack_guyed")}
    out = [f"\t{BEGIN}\n"]
    out += line(US_POLES, ml, models, "us", ((-ARM, HEIGHT), (ARM, HEIGHT)))
    out += line(CA_POLES, ml, models, "ca", tuple((0.3, h) for h in RACK))
    for k, (a, b) in enumerate(FEEDS):
        length, hd = bearing(a, b)
        name = f"h28_wire_feed{k + 1}"
        g = span(length, (), ground(b[1], b[2]) - ground(a[1], a[2]), ((0.0, DROP),)).save(ml / name, name)
        out.append(gf.obj(f"single wire, {a[0]} to {b[0]} ({length:.0f} m)", g, a[1], a[2], hd))
    # lamps: (lat, lon, heading, road light?). Pole lights: four by each port's inspection lane (CBP: under its canopy east of the building; CBSA: either side of
    # the drive-through bay, 8 m out from the north and south faces), arms pointing in over the lane
    lamps = []
    for key, title, lat, lon, w, d, h, kind, wall, roof in gp.FOOTPRINTS:
        if kind == "canopy":
            cx, dz, sxs = lon + gp.DX + (w / 2 + 14) / LON, d / 2 + 5, (-9, 9)
        elif kind == "drive":
            cx, dz = lon + gp.DX + sum(gp.BAY) / 2 / LON, d / 2 + 8
            half = (gp.BAY[1] - gp.BAY[0]) / 2 + 2.5
            sxs = (-half, half)
        else:
            continue
        for sx, sz, hd in ((sxs[0], -dz, 0), (sxs[1], -dz, 0), (sxs[0], dz, 180), (sxs[1], dz, 180)):
            lamps.append((lat + sz / LAT, cx + sx / LON, hd, False))
    lamps += [(lat, lon, hd, title) for title, lat, lon, hd in ROAD_LIGHTS]
    pole_lamp, road_lamp = lamp(8.0, 1.0, 8000, 165.0), lamp(10.0, 2.5, 12000, 165.0)
    beacon_lamp = lamp(10.0, 2.5, 12000, 165.0, True)
    for tag, title, key, north in (("ca", "CBSA plaza and road lights", "cbsa_main", True),
                                   ("us", "CBP plaza and road lights", "cbp_main", False)):
        olat, olon = next((f[2], f[3] + gp.DX) for f in gp.FOOTPRINTS if f[0] == key)
        oy = ground(olat, olon)
        m = gp.Mesh()
        for lat, lon, hd, road in lamps:
            if (lat > gf.BORDER) == north:
                dy = ground(lat, lon) - oy
                print(f"  {tag} lamp {lat:.5f},{lon:.5f}: {dy:+.2f} m")
                merge(m, (beacon_lamp if road == BEACON_LIGHT else road_lamp) if road else pole_lamp, (lon - olon) * LON, (lat - olat) * LAT, hd, dy)
        name = f"h28_lights_{tag}"
        out.append(gf.obj(f"{title} ({sum(1 for l in m.lights if not l[5] and len(l) == 6)} lamps, one model)", m.save(ml / name, name), olat, olon))
    out.append(f"\t{END}\n")
    block = "".join(out)
    s = gp.H28.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in s else "\n"
    s = s.replace("\r\n", "\n")
    if BEGIN in s:
        s = re.sub(r"\t" + re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n", lambda _m: block, s, flags=re.S)
    else:
        i = s.index("\t<Airport displayName")
        s = s[:i] + block + s[i:]
    gp.H28.write_text(s.replace("\n", nl), encoding="utf-8", newline="")
    print(len(out) - 2, "placements")


if __name__ == "__main__":
    main()
