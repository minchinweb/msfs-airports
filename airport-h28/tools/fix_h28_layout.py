"""One-off edit of H28.xml (2026-10-27): striped-grass runway 37 m wide and a striped-grass parking apron (no material
polygons), parking and taxi layout inside the parking area, bigger cones with red cones inboard at both ends, pole turned 90 deg.
    python -I airport-h28/tools/fix_h28_layout.py
Run gen_cones.py's model step first (the model GUIDs below must match its output). Not idempotent for the apron/taxi part
beyond replacing what it finds, so re-running is safe."""
import re
from pathlib import Path

H28 = Path(__file__).resolve().parents[1] / "PackageSources/Scenery/airport-h28/H28.xml"
LAT, LON = 111200.0, 73030.0
W, E = -112.78474, -112.76620
S, N = 48.998514, 48.998847
PS, PE = 48.997813, -112.78282
GRASS = "{322DE917-E25D-4AD8-BFBB-4D5F4D259413}"
WHITE = "{304661D0-CDE0-5537-8896-1F036B3F1086}"
RED = "{88E97374-C8C7-57CA-A6AE-880D40F11E0D}"
SCALE = 3.0
END_MARK = 202.0
LENGTH = (E - W) * LON


def fence(m):
    return W + m / LON


s = H28.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in s else "\n"
s = s.replace("\r\n", "\n")

# 1. drop the material polygons
s = re.sub(r"\t<Polygon version=\"0\.\d\.0\" displayName=\"(?:Runway|Taxi) Grass[^\n]*\n.*?\t</Polygon>\n", "", s, flags=re.S)

# 2. runway 37 m wide (the mowed strip), striped surface already set
s = re.sub(r'(<Runway [^>]*?) width="[0-9.]+"', r'\1 width="20.00000000000000"', s, count=1)

# 3. pole turned 90 degrees
s = re.sub(r'(<!-- wooden power pole[^\n]*-->\n\t<SceneryObject [^>]*?) heading="[-0-9.]+"', r'\1 heading="90.000000"', s, count=1)

# 4. cones: remove all and re-add
s = re.sub(r"\t<!-- (?:white|red) cone[^\n]*-->\n\t<SceneryObject[^\n]*>\n[^\n]*\n\t</SceneryObject>\n", "", s)


def cone(kind, side, m, lat, lon, guid):
    return (f"\t<!-- {kind} cone, {side} edge, {m:.0f} m from the west fence -->\n"
            f'\t<SceneryObject lat="{lat:.8f}" lon="{lon:.8f}" alt="0.10000000000000" pitch="0.000000" bank="0.000000" '
            f'heading="0.000000" imageComplexity="VERY_SPARSE" altitudeIsAgl="TRUE" snapToGround="TRUE" snapToNormal="FALSE">\n'
            f'\t\t<LibraryObject name="{guid}" scale="{SCALE:.6f}"/>\n\t</SceneryObject>\n')


east_mark = LENGTH - END_MARK
marks = (END_MARK, east_mark)
# cones come in pairs: the same stations on both edges
stations = [62, 95, 127] + [m for m in range(int(END_MARK) + 61, int(east_mark) - 25, 61)]
south = north = stations
inset = 1.5 / LAT
out = ""
for m in stations:
    out += cone("white", "S", m, S, fence(m), WHITE) + cone("white", "N", m, N, fence(m), WHITE)
for m in marks:
    out += cone("white", "S", m, S, fence(m), WHITE) + cone("red", "S", m, S + inset, fence(m), RED)
    out += cone("white", "N", m, N, fence(m), WHITE) + cone("red", "N", m, N - inset, fence(m), RED)
i = s.index("\t<Airport displayName")
s = s[:i] + out + s[i:]

# 5. taxi points, parking, taxi paths inside the parking area (south of the border, 140 m x 78 m)
X = fence(72)
dx = 30 / LON
rowN, rowS, mid = 48.99835, 48.99805, 48.99820
pts = (
    f'\t\t<TaxiwayPoint displayName="Runway entry" parentGroupID="2" index="0" type="NORMAL" orientation="FORWARD" lat="48.99868000000000" lon="{X:.14f}"/>\n'
    f'\t\t<TaxiwayPoint displayName="Apron" parentGroupID="2" groupIndex="1" index="1" type="NORMAL" orientation="FORWARD" lat="{mid:.14f}" lon="{X:.14f}"/>\n')
spots = [(rowN, X - dx), (rowN, X + dx), (rowS, X - dx), (rowS, X + dx)]
park = ""
for k, (la, lo) in enumerate(spots):
    hd = 0.0 if la == rowS else 180.0
    gi = f' groupIndex="{k}"' if k else ""
    park += (f'\t\t<TaxiwayParking parentGroupID="4"{gi} index="{k + 2}" type="RAMP_GA_SMALL" lat="{la:.14f}" lon="{lo:.14f}" '
             f'heading="{hd:.6f}" radius="8.000000" name="PARKING" number="{k + 1}" suffix="NONE" numberMarking="FALSE" '
             f'has3DMesh="TRUE" drawDirt="FALSE" passengerAccessType="RAMP" numberBiasX="0.000000" numberBiasZ="0.000000" numberHeading="0.000000"/>\n')
tail = ('surface="%s" centerLine="FALSE" start="%d" end="%d" width="8.000000" weightLimit="0" name="0" drawSurface="FALSE" '
        'drawDetail="FALSE" groundMerging="TRUE" excludeVegetationAround="TRUE" excludeVegetationInside="TRUE"/>\n')
paths = '\t\t<TaxiwayPath parentGroupID="3" type="TAXI" ' + tail % (GRASS, 0, 1)
for k in range(4):
    paths += f'\t\t<TaxiwayPath parentGroupID="3" groupIndex="{k + 1}" type="PARKING" ' + tail % (GRASS, 1, k + 2)
a = s.index('\t\t<TaxiwayPoint displayName="Runway entry"')
b = s.index("\t\t<TaxiName")
c = s.index("\t\t<Runway ")
s = s[:a] + pts + park + s[b:s.index("\t\t<TaxiwayPath", b)] + paths + s[c:]

# 6. striped-grass apron over the parking area
apron = ('\t\t<Aprons>\n'
         f'\t\t\t<Apron parentGroupID="1" surface="{GRASS}" drawSurface="TRUE" drawDetail="FALSE" localUV="TRUE" stretchUV="FALSE" '
         'flipUV="FALSE" priority="1" tiling="25.000000" heading="0.000000" falloff="0.100000" opacity="255" groundMerging="TRUE" '
         'excludeVegetationAround="TRUE" excludeVegetationInside="TRUE" isRectangle="TRUE">\n'
         + "".join(f'\t\t\t\t<Vertex lat="{la:.8f}" lon="{lo:.8f}"/>\n' for la, lo in [(S, W), (S, PE), (PS, PE), (PS, W)])
         + '\t\t\t</Apron>\n'
         # the mowed strip around the 20 m runway, same striped surface
         + f'\t\t\t<Apron parentGroupID="1" groupIndex="1" surface="{GRASS}" drawSurface="TRUE" drawDetail="FALSE" localUV="TRUE" '
         'stretchUV="FALSE" flipUV="FALSE" priority="1" tiling="25.000000" heading="1.570796" falloff="0.100000" opacity="255" '
         'groundMerging="TRUE" excludeVegetationAround="TRUE" excludeVegetationInside="TRUE" isRectangle="TRUE">\n'
         + "".join(f'\t\t\t\t<Vertex lat="{la:.8f}" lon="{lo:.8f}"/>\n' for la, lo in [(S, W), (S, E), (N, E), (N, W)])
         + '\t\t\t</Apron>\n\t\t</Aprons>\n')
s = re.sub(r"\t\t<Aprons/>\n|\t\t<Aprons>.*?</Aprons>\n", lambda m: apron, s, count=1, flags=re.S)

# 7. fence: wooden posts only, down both sides of the runway (FAA: 4 ft fences 44 ft each side of the centreline)
s = re.sub(r"\t<VectorPlacement .*?</VectorPlacement>\n", "", s, flags=re.S)
POST = "{2F9D8F36-A130-499C-A035-C81641B91980}"
CL = 48.99868
off = 13.4 / LAT
fences = ""
for name, la in (("north", CL + off), ("south", CL - off)):
    fences += (f'\t<VectorPlacement displayName="runway fence, {name} side (wooden posts)" profile="{POST}" snapToVertices="FALSE" '
               'spacing="6.0" heading="0.000000" scale="1.000000" scaleDelta="0.000000" rotation="Follow edge" '
               'avoidDiscontinuity="TRUE" castShadow="TRUE">\n'
               f'\t\t<Model modelGUID="{POST}" probability="1"/>\n'
               f'\t\t<Vertex lat="{la:.8f}" lon="{W:.8f}"/>\n\t\t<Vertex lat="{la:.8f}" lon="{E:.8f}"/>\n\t</VectorPlacement>\n')
i = s.index("\t<Airport displayName")
s = s[:i] + fences + s[i:]

H28.write_text(s.replace("\n", nl), encoding="utf-8", newline="")
print(len(south), "S,", len(north), "N,", "east mark at %.0f m" % east_mark)
