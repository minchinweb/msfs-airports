"""Generate the H28 cone models (flat-colour palette, like CYXD's gen_buildings.py) into
airport-h28/PackageSources/modelLib/:
  h28_cone_white/   white cone with a black top (the strip's edge cones)
  h28_cone_red/     all-red cone (placed next to a white one at the red-white pairs)
  texture/h28_palette.png(.xml)
Then swaps the library cone in H28.xml for the white model and adds a red cone beside the white cones at 202 m and 266 m.
    python -I airport-h28/tools/gen_cones.py
Prints the two model GUIDs. Safe to re-run (it replaces earlier red cones and the old GUIDs)."""
import json
import math
import re
import struct
import uuid
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODELLIB = ROOT / "airport-h28/PackageSources/modelLib"
H28 = ROOT / "airport-h28/PackageSources/Scenery/airport-h28/H28.xml"
NS = uuid.UUID("5d0c6c7e-0c1d-4a53-9b6e-0c7d00000028")
LIB_CONE = "{332F3033-B7B6-7FDD-1CAB-6E972A9235B8}"
PALETTE = [(236, 234, 230), (196, 40, 36), (24, 24, 26)]  # white, red, black
WHITE, RED, BLACK = range(3)
SW = 16
SIDES = 16


def write_palette(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    w, h = SW * len(PALETTE), SW
    raw = b"".join(b"\x00" + b"".join(bytes(PALETTE[x // SW]) for x in range(w)) for _ in range(h))

    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) \
        + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.write_bytes(png)
    path.with_name(path.name + ".xml").write_text(
        '<BitmapConfiguration>\n\t<BitmapSlot>MTL_BITMAP_DECAL0</BitmapSlot>\n</BitmapConfiguration>\n')


class Mesh:
    def __init__(self):
        self.pos, self.nrm, self.uv, self.idx = [], [], [], []

    def uvof(self, sw):
        return ((sw + 0.5) / len(PALETTE), 0.5)

    def band(self, r0, y0, r1, y1, sw):
        """Cone-frustum side (counter-clockwise seen from outside), outward normals."""
        slope = (r0 - r1) / (y1 - y0) if y1 != y0 else 0.0
        base = len(self.pos)
        for i in range(SIDES + 1):
            a = 2 * math.pi * i / SIDES
            c, s = math.cos(a), math.sin(a)
            n = (c, slope, s)
            ln = math.sqrt(sum(v * v for v in n))
            n = tuple(v / ln for v in n)
            for r, y in ((r0, y0), (r1, y1)):
                self.pos.append((r * c, y, r * s))
                self.nrm.append(n)
                self.uv.append(self.uvof(sw))
        for i in range(SIDES):
            a, b, c2, d = base + 2 * i, base + 2 * i + 1, base + 2 * i + 2, base + 2 * i + 3
            self.idx += [a, c2, b, b, c2, d]

    def cap(self, r, y, sw):
        base = len(self.pos)
        self.pos.append((0, y, 0))
        self.nrm.append((0, 1, 0))
        self.uv.append(self.uvof(sw))
        for i in range(SIDES + 1):
            a = 2 * math.pi * i / SIDES
            self.pos.append((r * math.cos(a), y, r * math.sin(a)))
            self.nrm.append((0, 1, 0))
            self.uv.append(self.uvof(sw))
        for i in range(SIDES):
            self.idx += [base, base + 2 + i, base + 1 + i]

    def save(self, folder, name):
        folder.mkdir(parents=True, exist_ok=True)
        pos = b"".join(struct.pack("<3f", *p) for p in self.pos)
        nrm = b"".join(struct.pack("<3f", *p) for p in self.nrm)
        uv = b"".join(struct.pack("<2f", *p) for p in self.uv)
        ib = b"".join(struct.pack("<H", i) for i in self.idx)
        blob = pos + nrm + uv + ib
        if len(blob) % 4:
            blob += b"\x00" * (4 - len(blob) % 4)
        n = len(self.pos)
        mn = [min(p[i] for p in self.pos) for i in range(3)]
        mx = [max(p[i] for p in self.pos) for i in range(3)]
        g = {
            "asset": {"version": "2.0", "generator": "airport-h28/tools/gen_cones.py",
                      "extensions": {"ASOBO_normal_map_convention": {"tangent_space_convention": "DirectX"}}},
            "extensionsUsed": ["ASOBO_normal_map_convention"],
            "scene": 0, "scenes": [{"nodes": [0]}],
            "nodes": [{"mesh": 0, "name": name}],
            "meshes": [{"name": name, "primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2},
                                                      "indices": 3, "mode": 4, "material": 0}]}],
            "materials": [{"name": "h28_flat", "pbrMetallicRoughness": {
                "baseColorTexture": {"index": 0}, "metallicFactor": 0.0, "roughnessFactor": 0.9}}],
            "textures": [{"sampler": 0, "source": 0}],
            "samplers": [{"magFilter": 9728, "minFilter": 9728}],
            "images": [{"uri": "h28_palette.png"}],
            "accessors": [
                {"bufferView": 0, "componentType": 5126, "count": n, "type": "VEC3", "min": mn, "max": mx},
                {"bufferView": 1, "componentType": 5126, "count": n, "type": "VEC3"},
                {"bufferView": 2, "componentType": 5126, "count": n, "type": "VEC2"},
                {"bufferView": 3, "componentType": 5123, "count": len(self.idx), "type": "SCALAR"}],
            "bufferViews": [
                {"buffer": 0, "byteOffset": 0, "byteLength": len(pos)},
                {"buffer": 0, "byteOffset": len(pos), "byteLength": len(nrm)},
                {"buffer": 0, "byteOffset": len(pos) + len(nrm), "byteLength": len(uv)},
                {"buffer": 0, "byteOffset": len(pos) + len(nrm) + len(uv), "byteLength": len(ib)}],
            "buffers": [{"uri": f"{name}.bin", "byteLength": len(blob)}],
        }
        (folder / f"{name}.bin").write_bytes(blob)
        (folder / f"{name}.gltf").write_text(json.dumps(g, indent=1))
        guid = "{" + str(uuid.uuid5(NS, name)).upper() + "}"
        (folder / f"{name}.xml").write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n'
            f'<ModelInfo guid="{guid}" version="1.1">\n\t<LODS>\n\t\t<LOD minSize="0" ModelFile="{name}.gltf"/>\n\t</LODS>\n</ModelInfo>\n')
        return guid


H, R0, R1 = 0.45, 0.20, 0.05  # cone height, base radius, top radius (metres)
TOP = 0.10  # black-top band height


def lerp_r(y):
    return R0 + (R1 - R0) * y / H


def white_cone():
    m = Mesh()
    m.band(R0, 0.0, lerp_r(H - TOP), H - TOP, WHITE)
    m.band(lerp_r(H - TOP), H - TOP, R1, H, BLACK)
    m.cap(R1, H, BLACK)
    return m


def red_cone():
    m = Mesh()
    m.band(R0, 0.0, R1, H, RED)
    m.cap(R1, H, RED)
    return m


def main():
    write_palette(MODELLIB / "texture" / "h28_palette.png")
    white = white_cone().save(MODELLIB / "h28_cone_white", "h28_cone_white")
    red = red_cone().save(MODELLIB / "h28_cone_red", "h28_cone_red")
    print("white", white, "red", red)

    s = H28.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in s else "\n"
    s = s.replace("\r\n", "\n")
    # forget earlier red cones, then re-point the white ones
    s = re.sub(r"\t<!-- red cone[^\n]*-->\n\t<SceneryObject[^\n]*>\n[^\n]*\n\t</SceneryObject>\n", "", s)
    s = s.replace(LIB_CONE, white)
    for old in re.findall(r'<LibraryObject name="(\{[0-9A-F-]{36}\})" scale="1.000000"/>', s):
        pass
    # red cone 1.5 m east of each white cone at 202 m and 266 m
    add = {}
    for m in re.finditer(r"(\t<!-- white cone, ([SN]) edge, (202|266) m from the west fence -->\n"
                         r"\t<SceneryObject lat=\"([-0-9.]+)\" lon=\"([-0-9.]+)\"[^>]*>)", s):
        side, dist, lat, lon = m.group(2), m.group(3), float(m.group(4)), float(m.group(5))
        lon2 = lon + 1.5 / 73030.0
        add[m.start()] = (
            f'\t<!-- red cone, {side} edge, {dist} m from the west fence (next to the white cone) -->\n'
            f'\t<SceneryObject lat="{lat:.8f}" lon="{lon2:.8f}" alt="0.00000000000000" pitch="0.000000" bank="0.000000" '
            f'heading="0.000000" imageComplexity="VERY_SPARSE" altitudeIsAgl="TRUE" snapToGround="TRUE" snapToNormal="FALSE">\n'
            f'\t\t<LibraryObject name="{red}" scale="1.000000"/>\n\t</SceneryObject>\n')
    for pos in sorted(add, reverse=True):
        s = s[:pos] + add[pos] + s[pos:]
    H28.write_text(s.replace("\n", nl), encoding="utf-8", newline="")
    print(len(add), "red cones placed")


if __name__ == "__main__":
    main()
