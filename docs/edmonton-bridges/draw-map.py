"""Draw a simplified map of the Edmonton bridge lists.

Writes edmonton-bridges-map.png beside this script. Positions match
docs/edmonton-bridges/bridges.md and freeway-bridges.md. Centres are
approximate. Yellowhead interchanges that were named and then left off
the freeway list are estimated from the street grid.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).with_name("edmonton-bridges-map.png")

BG = (244, 241, 234)
PANEL = (255, 255, 255)
INK = (28, 28, 28)
MUTED = (90, 86, 80)
LINE = (118, 114, 108)
RIVER_COLOR = (47, 107, 168)
RIVER_DOT = (23, 78, 138)
FREEWAY_DOT = (140, 88, 22)
SKIP = (168, 52, 40)
FRAME = (196, 190, 180)
AIRPORT = (18, 18, 18)
HALO = (255, 255, 255)
INSET_FRAME = (168, 52, 40)

# Regional frame. North is up.
LON0, LON1 = -114.30, -113.02
LAT0, LAT1 = 53.16, 53.90

# Downtown valley and the Yellowhead interchanges beside City Centre.
IN_LON0, IN_LON1 = -113.70, -113.30
IN_LAT0, IN_LAT1 = 53.500, 53.595

AIRPORTS = [
    ("CYXD", "City Centre", 53.572, -113.520, "s"),
    ("CYED", "Namao", 53.669, -113.476, "e"),
    ("CYEG", "International", 53.310, -113.580, "e"),
    ("CZVL", "Villeneuve", 53.668, -113.854, "e"),
    ("CFB6", "Josephburg", 53.728, -113.087, "w"),
    ("CEZ3", "Cooking Lake", 53.428, -113.116, "nw"),
]

# code, name, lat, lon, estimated
RIVER = [
    ("R1", "Devon Bridge", 53.370, -113.752, False),
    ("R2", "Travis Jordan Memorial", 53.460, -113.615, False),
    ("R3", "Brett Ryan Memorial", 53.460, -113.615, False),
    ("R4", "Terwillegar Park Footbridge", 53.481, -113.598, False),
    ("R5", "Fort Edmonton Footbridge", 53.495, -113.590, False),
    ("R6", "Quesnell Bridge", 53.507, -113.567, False),
    ("R7", "Hawrelak Park Footbridge", 53.523, -113.547, False),
    ("R8", "Groat Bridge", 53.537, -113.539, False),
    ("R9", "Dudley B. Menzies", 53.531, -113.512, False),
    ("R10", "High Level Bridge", 53.531, -113.511, False),
    ("R11", "Walterdale Bridge", 53.529, -113.502, False),
    ("R12", "James MacDonald", 53.536, -113.488, False),
    ("R13", "Low Level Bridge", 53.538, -113.487, False),
    ("R14", "Tawatinâ Bridge", 53.5401, -113.4772, False),
    ("R15", "Dawson Bridge", 53.549, -113.467, False),
    ("R16", "Capilano Bridge", 53.556, -113.439, False),
    ("R17", "Capilano Footbridge", 53.563, -113.419, False),
    ("R18", "Ainsworth Dyer Footbridge", 53.554, -113.398, False),
    ("R19", "Rundle Park Footbridge", 53.563, -113.379, False),
    ("R20", "Beverly Bridge", 53.571, -113.373, False),
    ("R21", "Clover Bar Bridge", 53.572, -113.372, False),
    ("R22", "Clover Bar Railway", 53.573, -113.372, False),
    ("R23", "Henday northeast river", 53.608, -113.354, False),
    ("R24", "Beaver Hills Bridge", 53.628, -113.322, False),
    ("R25", "Highway 15, Fort Saskatchewan", 53.706, -113.235, False),
    ("R26", "CN west of Scotford", 53.761, -113.171, False),
]

FREEWAY = [
    ("Q94", "QE2 / 50 Ave and Black Gold", 53.261, -113.563, False),
    ("Q98", "QE2 / Leduc rail line", 53.380, -113.520, False),
    ("H27", "Henday / Calgary Trail", 53.437, -113.491, False),
    ("H28", "Blackmud Creek arches", 53.437, -113.496, False),
    ("H29", "Henday at 111 Street", 53.435, -113.514, False),
    ("H30", "Whitemud Creek arch", 53.448, -113.560, True),
    ("H33", "Henday / Wedgewood Creek", 53.471, -113.647, False),
    ("H36", "Henday / Whitemud west", 53.512, -113.659, False),
    ("H38", "Henday / Stony Plain Road", 53.540, -113.659, False),
    ("H39", "Henday / Yellowhead west", 53.574, -113.662, False),
    ("Y66", "Yellowhead / 178 Street", 53.572, -113.631, False),
    ("H41", "Henday / 137 Avenue", 53.601, -113.630, False),
    ("H43", "North Henday / Campbell Road", 53.633, -113.566, False),
    ("H47", "Manning / Henday", 53.631, -113.381, False),
    ("H50", "Henday / Yellowhead east", 53.568, -113.345, False),
    ("Y76", "Yellowhead at Broadmoor", 53.570, -113.333, False),
    ("Y78", "Yellowhead / Clover Bar Road", 53.570, -113.271, False),
    ("H54", "Highway 14 / Henday", 53.449, -113.336, False),
    ("H52", "Henday / Sherwood Park Fwy", 53.513, -113.344, False),
    ("S106", "SPF / 34 St and 67 St", 53.516, -113.408, False),
    ("W91", "Whitemud / 17 Street", 53.482, -113.364, False),
    ("W87", "Whitemud / Rainbow Valley", 53.483, -113.555, False),
    ("H45", "Henday / 97 Street", 53.6469, -113.4912, False),
    ("Q96", "QE2 / Airport Road", 53.3088, -113.5489, False),
]

# Short cross-road text drawn next to the code on the map.
CROSS = {
    "Q94": "50 Ave / Black Gold",
    "Q98": "Leduc rail",
    "H33": "Wedgewood Ck",
    "Y66": "178 St",
    "H41": "137 Ave",
    "H43": "Campbell Rd",
    "Y78": "Clover Bar Rd",
    "S106": "34 & 67 St",
    "W91": "17 St",
    "W87": "Rainbow Valley",
    "H45": "97 St",
    "Q96": "Airport Rd",
}

SKIPPED = [
    ("Y68", "Yellowhead / 156 Street", 53.578, -113.596, True),
    ("Y69", "Yellowhead / St. Albert Trail", 53.578, -113.548, True),
    ("Y70", "Yellowhead / 97 Street", 53.578, -113.489, True),
    ("Y71", "Yellowhead / 82 Street", 53.578, -113.462, True),
    ("Y72", "Yellowhead / Wayne Gretzky", 53.578, -113.450, True),
    ("Y73", "Yellowhead / 50 Street", 53.576, -113.405, True),
    ("Y74", "Yellowhead / Victoria Trail", 53.574, -113.388, True),
    ("Z124", "Mill Creek trestle", 53.512, -113.470, False),
    ("Y67", "Yellowhead / 170 Street", 53.5733, -113.6153, False),
    ("Y65", "Yellowhead / 184 Street", 53.5727, -113.6392, False),
    ("G117", "102 Avenue at Groat Road", 53.5430, -113.5403, False),
    ("Z125", "Wellington Bridge", 53.5431, -113.5481, False),
    ("G118", "Stony Plain Road at Groat", 53.5479, -113.5459, False),
    ("G119", "107 Avenue at Groat Road", 53.5510, -113.5498, False),
    ("C121", "Ada Boulevard", 53.5602, -113.4427, False),
    ("C122", "112 Avenue at Capilano", 53.5629, -113.4465, False),
    ("C123", "Grant Moellmann Bridge", 53.5754, -113.4530, False),
    ("H31", "Terwillegar Drive / Henday", 53.4442, -113.6002, False),
    ("W82", "Whitemud / 170 Street", 53.5122, -113.6153, False),
    ("W83", "Whitemud / 159 Street", 53.5119, -113.5967, False),
    ("W84", "Whitemud / 156 Street", 53.5121, -113.5904, False),
    ("W85", "Fox Drive, Campbell Bridge", 53.5032, -113.5610, False),
    ("W86", "Whitemud / 53 Avenue", 53.4904, -113.5720, False),
    ("W88", "Whitemud / Calgary Trail", 53.4804, -113.4938, False),
    ("W89", "Whitemud / 66 Street", 53.4852, -113.4427, False),
    ("W90", "Whitemud / 50 Street", 53.4873, -113.4182, False),
    ("H32", "Henday / 184 Street", 53.4666, -113.6311, False),
    ("H34", "Henday / Lessard Road", 53.4800, -113.6584, False),
    ("H35", "Henday / Callingwood Road", 53.4943, -113.6591, False),
    ("H37", "Henday / 87 Avenue", 53.5228, -113.6592, False),
    ("H40", "Henday / Ray Gibbon Drive", 53.5914, -113.6462, False),
    ("H42", "Henday / St. Albert Trail", 53.6169, -113.6004, False),
    ("H44", "Henday / 127 Street", 53.6390, -113.5453, False),
    ("H48", "Henday / 153 Avenue", 53.6173, -113.3593, False),
    ("H49", "Henday / 130 Avenue", 53.5873, -113.3453, False),
    ("H51", "Henday / Baseline Road", 53.5404, -113.3426, False),
    ("H55", "Henday / 17 Street", 53.4385, -113.3691, False),
    ("H56", "Henday / 50 Street", 53.4356, -113.4180, False),
    ("H57", "Henday / 91 Street", 53.4375, -113.4668, False),
    ("L113", "Highway 14 / Highway 21", 53.4468, -113.2461, False),
    ("Y79", "Highway 16 / Highway 21", 53.5702, -113.2461, False),
    ("Q97", "Highway 2 / Highway 19", 53.3379, -113.5489, False),
    ("Q100", "Highway 2 / Ellerslie Road", 53.4248, -113.4931, False),
    ("Q101", "Highway 2 / 23 Avenue", 53.4535, -113.4922, False),
    ("S105", "Sherwood Park Fwy / 50 Street", 53.5143, -113.4185, False),
    ("Z126", "50 Street rail overpass", 53.5181, -113.4184, False),
    ("H46", "Henday / 66 Street", 53.6465, -113.4390, False),
    ("H53", "Henday / Whitemud east", 53.4829, -113.3427, False),
    ("C120", "Capilano Drive / 106 Avenue", 53.5493, -113.4387, False),
    ("Y77", "Highway 16 / Sherwood Drive", 53.5703, -113.2954, False),
    ("Y80", "Highway 16 / Highway 824", 53.5700, -113.1479, False),
    ("Q99", "Highway 2 / 41 Avenue SW", 53.3963, -113.5122, False),
    ("A111", "Highway 16A / Winterburn Rd", 53.5412, -113.6887, False),
    ("Y64", "Highway 16 / Winterburn Road", 53.5703, -113.6891, False),
    ("Y63", "Highway 16 / Highway 60", 53.5699, -113.7633, False),
    ("A110", "Highway 16A / Highway 60", 53.5413, -113.7626, False),
    ("Y62", "Highway 16 / Highway 44", 53.5703, -113.8091, False),
    ("A109", "Highway 16A rail crossing", 53.5434, -113.8347, False),
    ("Y61", "Highway 16 / Century Road", 53.5698, -113.8854, False),
    ("Y60", "Highway 16 / Jennifer Heil Way", 53.5696, -113.9338, False),
    ("Y59", "Highway 16 / Highway 779", 53.5696, -114.0003, False),
    ("A108", "Highway 16A / Highway 779", 53.5413, -114.0019, False),
    ("Y58", "Highway 16 / Highway 43", 53.5702, -114.2214, False),
    ("Q102", "Highway 2 / Highway 37", 53.7159, -113.5533, False),
    ("M112", "Highway 15 / 99 Avenue", 53.7022, -113.2270, False),
    ("Q95", "Highway 2 / Highway 2A", 53.2648, -113.5638, False),
    ("Q93", "Highway 2 / Black Gold Drive", 53.2579, -113.5618, False),
    ("D115", "Highway 28 / Highway 28A", 53.8443, -113.3220, False),
    ("D114", "Highway 28 / 195 Avenue", 53.6579, -113.4986, False),
    ("S104", "SPF / 82 Ave and Argyll Rd", 53.5180, -113.4735, False),
    ("G116", "Groat Road / Hawrelak access", 53.5322, -113.5383, False),
    ("S107", "Sherwood Park Fwy / 17 Street", 53.5172, -113.3691, False),
    ("Y75", "Yellowhead / 17 Street", 53.5700, -113.3631, False),
    ("W81", "Whitemud / 178 Street", 53.5121, -113.6300, False),
    ("Q103", "Highway 2 / Highway 642", 53.8018, -113.6612, False),
    ("Q92", "Highway 2 / Township Rd 490", 53.1922, -113.5982, False),
]

YELLOWHEAD_ROW = {"Y68", "Y69", "Y70", "Y71", "Y72", "Y73", "Y74"}

LEFT_OFF = {code for code, *_rest in SKIPPED}
CATALOGUE = {row[0]: row for row in (*RIVER, *FREEWAY, *SKIPPED)}

# Numbers are unique across every bridge and increase along each road.
# Moving a bridge to another road, or between the include list and left off,
# changes the letter and keeps the number. A bridge on two roads keeps the
# number from the first road it was counted on: the river, then the Henday,
# then the other highways.
KEY_GROUPS = [
    ("River", ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13"]),
    ("River", ["R14", "R15", "R16", "R17", "R18", "R19", "R20", "R21", "R22", "R23", "R24", "R25", "R26"]),
    ("Henday", ["H27", "H28", "H29", "H30", "H31", "H32", "H33", "H34", "H35", "H36", "H37", "H38", "H39", "H40", "H41", "H42"]),
    ("Henday", ["H43", "H44", "H45", "H46", "H47", "H48", "H49", "H50", "H51", "H52", "H53", "H54", "H55", "H56", "H57"]),
    ("Yellowhead", ["Y58", "Y59", "Y60", "Y61", "Y62", "Y63", "Y64", "Y65", "Y66", "Y67", "Y68", "Y69"]),
    ("Yellowhead", ["Y70", "Y71", "Y72", "Y73", "Y74", "Y75", "Y76", "Y77", "Y78", "Y79", "Y80"]),
    ("Whitemud", ["W81", "W82", "W83", "W84", "W85", "W86", "W87", "W88", "W89", "W90", "W91"]),
    ("Highway 2", ["Q92", "Q93", "Q94", "Q95", "Q96", "Q97", "Q98", "Q99", "Q100", "Q101", "Q102", "Q103"]),
    ("SPF / 16A", ["S104", "S105", "S106", "S107", "A108", "A109", "A110", "A111", "M112", "L113"]),
    ("Groat / other", ["D114", "D115", "G116", "G117", "G118", "G119", "C120", "C121", "C122", "C123", "Z124", "Z125", "Z126"]),
]

def route(*items: str | tuple[float, float]) -> list[tuple[float, float]]:
    """Polyline through catalogue centres. A string is a bridge code."""
    lookup = {code: (lat, lon) for code, _name, lat, lon, _est in RIVER + FREEWAY + SKIPPED}
    points = []
    for item in items:
        point = lookup[item] if isinstance(item, str) else item
        if points and point == points[-1]:
            continue
        points.append(point)
    return points


# Upstream to downstream, one vertex per crossing. R3 shares R2's centre.
RIVER_LINE = route(
    "R1", "R2", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14",
    "R15", "R16", "R17", "R18", "R19", "R20", "R21", "R22", "R23", "R24", "R25", "R26",
)

# Each line is ordered along the road and uses the plotted bridge centres.
FREEWAYS = [
    ("Anthony Henday Dr", route(
        "H27", "H28", "H29", "H30", "H31", "R2", "H32", "H33", "H34", "H35", "H36", "H37", "H38",
        "H39", "H40", "H41", "H42", "H43", "H44", "H45", "H46", "H47", "H48", "R23", "H49",
        "H50", "H51", "H52", "H53", "H54", "H55", "H56", "H57", "H27",
    )),
    ("Yellowhead Tr", route(
        (53.570, -114.250),
        "Y58", "Y59", "Y60", "Y61", "Y62", "Y63", "Y64", "H39",
        "Y65", "Y66", "Y67", "Y68", "Y69", "Y70", "Y71", "Y72", "Y73", "Y74",
        "R20", "R21", "Y75", "H50", "Y76", "Y77", "Y78", "Y79", "Y80",
        (53.570, -113.120),
    )),
    ("Whitemud Dr", route(
        "H36", "W81", "W82", "W83", "W84", "R6", "W85", "W86", "W87", "W88", "W89", "W90", "W91", "H53",
    )),
    ("QE2", route("Q92", "Q93", "Q94", "Q95", "Q96", "Q97", "Q98", "Q99", "Q100", "H27", "Q101", "W88")),
    ("Sherwood Park Fwy", route("S104", "S105", "S106", "S107", "H52")),
    ("Hwy 14", route((53.428, -113.116), "L113", "H54")),
    ("Highway 16A", route("H38", "A111", "A110", "A109", "A108", (53.548, -114.120), "Y58")),
    ("Highway 21", route("L113", "Y79", (53.600, -113.246))),
    ("Highway 60", route("R1", "A110", "Y63")),
    # Highway 2 from the north becomes Ray Gibbon Drive, then St. Albert Trail, then Groat Road.
    ("Highway 2 / Groat", route(
        "G116", "R8", "G117", "G118", "G119", "Y69", "H42", "Q102", "Q103", (53.822, -113.651),
    )),
    ("Highway 642", route((53.802, -113.700), "Q103", (53.802, -113.620))),
    ("Township Road 490", route((53.192, -113.640), "Q92", (53.192, -113.550))),
    ("Highway 28A", route((53.770, -113.323), "D115")),
    ("Highway 28", route((53.834, -113.380), (53.840, -113.328), "D115", (53.872, -113.305))),
    ("Highway 28", route("H45", "D114", (53.675, -113.508))),
    # Capilano Drive becomes Wayne Gretzky Drive, then Manning Drive, then Highway 15.
    ("Capilano / Manning", route(
        "C120", "R16", "C121", "C122", "C123", "Y72", "H47", "R25", "M112", (53.728, -113.120),
    )),
]

# Road names on the regional map, anchored on the line: lat, lon, prefer.
ROAD_LABELS = [
    ("Anthony Henday Dr", 53.526, -113.668, "w"),
    ("Anthony Henday Dr", 53.648, -113.430, "n"),
    ("Yellowhead Tr", 53.574, -113.760, "n"),
    ("Whitemud Dr", 53.478, -113.460, "s"),
    ("QE2", 53.345, -113.552, "e"),
    ("Manning Dr", 53.668, -113.310, "nw"),
    ("Gretzky Dr", 53.598, -113.424, "s"),
    ("St. Albert Tr", 53.604, -113.582, "w"),
    ("Hwy 14", 53.438, -113.210, "n"),
    ("Highway 16", 53.578, -114.120, "n"),
    ("Highway 16A", 53.534, -113.980, "s"),
    ("Highway 60", 53.470, -113.770, "w"),
    ("Highway 21", 53.500, -113.230, "e"),
    ("Highway 2", 53.690, -113.545, "e"),
    ("Highway 642", 53.810, -113.690, "n"),
    ("Highway 28A", 53.800, -113.310, "e"),
    ("Highway 28", 53.838, -113.360, "s"),
    ("Groat Road", 53.528, -113.545, "w"),
    ("Capilano Drive", 53.552, -113.430, "e"),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "segoeuib.ttf" if bold else "segoeui.ttf"
    path = Path(r"C:\Windows\Fonts") / name
    if path.exists():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def box_size(lon0, lon1, lat0, lat1, height: int, pad: int) -> tuple[int, int]:
    cos = math.cos(math.radians((lat0 + lat1) / 2))
    inner_h = height - 2 * pad
    inner_w = inner_h * ((lon1 - lon0) * cos) / (lat1 - lat0)
    return int(round(inner_w + 2 * pad)), height


def make_projector(lon0, lon1, lat0, lat1, width, height, pad):
    cos = math.cos(math.radians((lat0 + lat1) / 2))
    avail_w = width - 2 * pad
    avail_h = height - 2 * pad
    span_x = (lon1 - lon0) * cos
    span_y = lat1 - lat0
    scale = min(avail_w / span_x, avail_h / span_y)
    used_w = span_x * scale
    used_h = span_y * scale
    x0 = pad + (avail_w - used_w) / 2
    y0 = pad + (avail_h - used_h) / 2

    def project(lat: float, lon: float) -> tuple[float, float]:
        x = x0 + (lon - lon0) * cos * scale
        y = y0 + (lat1 - lat) * scale
        return x, y

    return project, scale


def text_size(draw: ImageDraw.ImageDraw, text: str, face) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=face)
    return box[2] - box[0], box[3] - box[1]


class Labels:
    def __init__(self, bounds: tuple[int, int, int, int]):
        self.bounds = bounds
        self.boxes: list[tuple[float, float, float, float]] = []

    def reserve(self, box) -> None:
        self.boxes.append(box)

    def overlaps(self, box, gap: float = 3) -> bool:
        x0, y0, x1, y1 = box
        for a, b, c, d in self.boxes:
            if x0 < c + gap and x1 > a - gap and y0 < d + gap and y1 > b - gap:
                return True
        return False

    def inside(self, box) -> bool:
        x0, y0, x1, y1 = box
        a, b, c, d = self.bounds
        return x0 >= a and y0 >= b and x1 <= c and y1 <= d

    def place(self, draw, text, anchor, face, fill, prefer="e") -> bool:
        tw, th = text_size(draw, text, face)
        ax, ay = anchor
        order = [prefer, "e", "w", "n", "s", "ne", "nw", "se", "sw"]
        seen = []
        for key in order:
            if key not in seen:
                seen.append(key)
        for dist in (11, 18, 28, 40):
            options = {
                "e": (ax + dist, ay - th / 2),
                "w": (ax - dist - tw, ay - th / 2),
                "n": (ax - tw / 2, ay - dist - th),
                "s": (ax - tw / 2, ay + dist),
                "ne": (ax + dist * 0.8, ay - dist - th),
                "nw": (ax - dist * 0.8 - tw, ay - dist - th),
                "se": (ax + dist * 0.8, ay + dist * 0.6),
                "sw": (ax - dist * 0.8 - tw, ay + dist * 0.6),
            }
            for key in seen:
                x, y = options[key]
                box = (x, y, x + tw, y + th)
                if self.inside(box) and not self.overlaps(box):
                    draw.text((x, y), text, font=face, fill=fill, stroke_width=2, stroke_fill=HALO)
                    self.boxes.append(box)
                    return True
        return False


def polyline(draw, pts, fill, width):
    if len(pts) >= 2:
        draw.line(pts, fill=fill, width=width, joint="curve")


def in_inset(lat, lon) -> bool:
    return IN_LAT0 <= lat <= IN_LAT1 and IN_LON0 <= lon <= IN_LON1


def draw_scale(draw, origin, scale_px_per_deg_lat, face):
    """10 km bar. scale is pixels per degree of latitude."""
    px = 10 / 111.32 * scale_px_per_deg_lat
    x, y = origin
    draw.line([(x, y), (x + px, y)], fill=INK, width=3)
    draw.line([(x, y - 4), (x, y + 4)], fill=INK, width=2)
    draw.line([(x + px, y - 4), (x + px, y + 4)], fill=INK, width=2)
    draw.text((x, y + 6), "10 km", font=face, fill=INK)


def draw_north(draw, origin, face):
    x, y = origin
    draw.polygon([(x, y), (x - 6, y + 16), (x + 6, y + 16)], fill=INK)
    draw.text((x - 5, y + 18), "N", font=face, fill=INK)


def marker_box(x, y, r=8):
    return (x - r, y - r, x + r, y + r)


def draw_airport(draw, x, y):
    draw.rectangle([x - 5, y - 5, x + 5, y + 5], fill=AIRPORT)


def draw_dot(draw, x, y, fill, r=4):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=HALO)


def draw_cross(draw, x, y):
    draw.line([(x - 5, y - 5), (x + 5, y + 5)], fill=SKIP, width=2)
    draw.line([(x - 5, y + 5), (x + 5, y - 5)], fill=SKIP, width=2)


def joined_codes(codes: list[str]) -> str:
    ordered = sorted(codes, key=lambda code: (code[0], int(code[1:])))
    prefix = ordered[0][0]
    numbers = [int(code[1:]) for code in ordered]
    if len(ordered) >= 2 and all(code[0] == prefix for code in ordered):
        if numbers == list(range(numbers[0], numbers[-1] + 1)):
            return f"{ordered[0]}–{ordered[-1]}"
    return " ".join(ordered)


def label_for(codes: list[str]) -> str:
    ordered = sorted(codes, key=lambda code: (code[0], int(code[1:])))
    if len(ordered) == 1 and ordered[0] in CROSS:
        return f"{ordered[0]} {CROSS[ordered[0]]}"
    return joined_codes(ordered)


def stack_above(draw, labels: Labels, items, face, fill) -> None:
    """Put short labels above marks, stepping up a row when neighbours collide."""
    for x, y, text in sorted(items, key=lambda item: item[0]):
        tw, th = text_size(draw, text, face)
        placed = False
        for tier in range(8):
            ly = y - 16 - th - tier * (th + 5)
            lx = x - tw / 2
            box = (lx, ly, lx + tw, ly + th)
            if not labels.inside(box) or labels.overlaps(box, gap=2):
                continue
            draw.line([(x, y - 8), (x, ly + th)], fill=fill, width=1)
            draw.text((lx, ly), text, font=face, fill=fill, stroke_width=2, stroke_fill=HALO)
            labels.reserve(box)
            placed = True
            break
        if not placed:
            labels.place(draw, text, (x, y), face, fill, "n")


def group_nearby(items, min_px=14):
    """Greedy groups of (x, y, code) that sit on top of each other."""
    groups = []
    used = set()
    for i, item in enumerate(items):
        if i in used:
            continue
        group = [item]
        used.add(i)
        changed = True
        while changed:
            changed = False
            for j, other in enumerate(items):
                if j in used:
                    continue
                if any(math.hypot(other[0] - g[0], other[1] - g[1]) < min_px for g in group):
                    group.append(other)
                    used.add(j)
                    changed = True
        groups.append(group)
    return groups


def draw_panel(width, height, lon0, lon1, lat0, lat1, label_names: bool):
    pad = 36 if label_names else 32
    image = Image.new("RGB", (width, height), PANEL)
    draw = ImageDraw.Draw(image)
    project, scale = make_projector(lon0, lon1, lat0, lat1, width, height, pad)
    labels = Labels((6, 6, width - 6, height - 6))
    name_face = font(15 if label_names else 13, bold=True)
    code_face = font(12, bold=True)
    road_face = font(15 if label_names else 14)

    for _name, pts in FREEWAYS:
        polyline(draw, [project(lat, lon) for lat, lon in pts], LINE, 3 if label_names else 2)
    polyline(draw, [project(lat, lon) for lat, lon in RIVER_LINE], RIVER_COLOR, 5 if label_names else 4)

    if not label_names:
        ring = [project(lat, lon) for lat, lon in (
            (IN_LAT0, IN_LON0), (IN_LAT0, IN_LON1), (IN_LAT1, IN_LON1), (IN_LAT1, IN_LON0), (IN_LAT0, IN_LON0)
        )]
        draw.line(ring, fill=INSET_FRAME, width=2)
    else:
        # Keep the panel title clear of the crosses along the top.
        labels.reserve((0, 0, 230, 28))

    for code, _name, lat, lon, _est in FREEWAY:
        x, y = project(lat, lon)
        draw_dot(draw, x, y, FREEWAY_DOT, 4)
        labels.reserve(marker_box(x, y))
    for code, _name, lat, lon, _est in RIVER:
        x, y = project(lat, lon)
        draw_dot(draw, x, y, RIVER_DOT, 5)
        labels.reserve(marker_box(x, y))
    for code, _name, lat, lon, _est in SKIPPED:
        x, y = project(lat, lon)
        draw_cross(draw, x, y)
        labels.reserve(marker_box(x, y, 9))

    for code, name, lat, lon, prefer in AIRPORTS:
        x, y = project(lat, lon)
        draw_airport(draw, x, y)
        labels.reserve(marker_box(x, y, 8))
        text = code if not label_names else f"{code}  {name}"
        labels.place(draw, text, (x, y), name_face, INK, prefer)

    if not label_names:
        for text, lat, lon, prefer in ROAD_LABELS:
            x, y = project(lat, lon)
            labels.place(draw, text, (x, y), road_face, MUTED, prefer)
        for series in (RIVER, FREEWAY, SKIPPED):
            coded = []
            for code, _name, lat, lon, _est in series:
                if in_inset(lat, lon):
                    continue
                x, y = project(lat, lon)
                coded.append((x, y, code))
            for group in group_nearby(coded, 16):
                x = sum(p[0] for p in group) / len(group)
                y = sum(p[1] for p in group) / len(group)
                codes = [p[2] for p in group]
                text = label_for(codes)
                fill = SKIP if all(code in LEFT_OFF for code in codes) else INK
                labels.place(draw, text, (x, y), code_face, fill, "e")
    else:
        skips = []
        others = []
        for code, _name, lat, lon, _est in SKIPPED:
            if not in_inset(lat, lon):
                continue
            x, y = project(lat, lon)
            if code in YELLOWHEAD_ROW:
                skips.append((x, y, code))
            else:
                others.append((x, y, code, "s"))
        stack_above(draw, labels, skips, code_face, SKIP)
        for code, _name, lat, lon, _est in RIVER + FREEWAY:
            if not in_inset(lat, lon):
                continue
            x, y = project(lat, lon)
            prefer = "s" if code.startswith("R") or code in LEFT_OFF else "w" if lon < -113.55 else "e"
            others.append((x, y, code, prefer))
        for group in group_nearby([(x, y, code) for x, y, code, _prefer in others], 18):
            x = sum(p[0] for p in group) / len(group)
            y = sum(p[1] for p in group) / len(group)
            codes = [p[2] for p in group]
            text = label_for(codes)
            left = all(code in LEFT_OFF for code in codes)
            prefer = "s" if text.startswith("R") or left else "e" if x > width * 0.62 else "w"
            fill = SKIP if left else INK
            labels.place(draw, text, (x, y), code_face, fill, prefer)

    return image, draw, project, scale


def swatch_row(draw, x, y, face):
    draw.rectangle([x, y, x + 10, y + 10], fill=AIRPORT)
    draw.text((x + 16, y - 3), "Airport", font=face, fill=INK)
    draw.ellipse([x + 92, y, x + 102, y + 10], fill=RIVER_DOT)
    draw.text((x + 108, y - 3), "River list", font=face, fill=INK)
    draw.ellipse([x + 196, y, x + 206, y + 10], fill=FREEWAY_DOT)
    draw.text((x + 212, y - 3), "Freeway list", font=face, fill=INK)
    draw.line([(x + 320, y), (x + 330, y + 10)], fill=SKIP, width=2)
    draw.line([(x + 320, y + 10), (x + 330, y)], fill=SKIP, width=2)
    draw.text((x + 336, y - 3), "Named, then left off", font=face, fill=INK)
    draw.line([(x + 500, y + 5), (x + 528, y + 5)], fill=RIVER_COLOR, width=3)
    draw.text((x + 534, y - 3), "River", font=face, fill=INK)
    draw.line([(x + 590, y + 5), (x + 618, y + 5)], fill=LINE, width=3)
    draw.text((x + 624, y - 3), "Freeway", font=face, fill=INK)


def draw_key(draw, x, y, width, face, head):
    columns = [(title, [CATALOGUE[code] for code in codes], False) for title, codes in KEY_GROUPS]
    columns.append(("Airports", None, True))
    gap = 12
    col_w = (width - gap * (len(columns) - 1)) / len(columns)
    bottom = y
    for i, (title, rows, airports) in enumerate(columns):
        cx = x + i * (col_w + gap)
        yy = y
        draw.text((cx, yy), title, font=head, fill=INK)
        yy += 22
        if airports:
            for code, name, _lat, _lon, _prefer in AIRPORTS:
                draw.rectangle([cx, yy + 2, cx + 8, yy + 10], fill=AIRPORT)
                draw.text((cx + 14, yy - 2), f"{code}  {name}", font=face, fill=INK)
                yy += 17
            bottom = max(bottom, yy)
            continue
        for code, name, _lat, _lon, est in rows:
            mark = f"{code}  {name}" + ("  *" if est else "")
            fill = SKIP if code in LEFT_OFF else INK
            draw.text((cx, yy), mark, font=face, fill=fill)
            yy += 16
        bottom = max(bottom, yy)
    return bottom


def main():
    margin = 28
    title_h = 86
    ov_h = 1080
    ov_w, _ = box_size(LON0, LON1, LAT0, LAT1, ov_h, 32)
    in_h = 640
    in_w, _ = box_size(IN_LON0, IN_LON1, IN_LAT0, IN_LAT1, in_h, 36)
    gap = 22
    key_h = 310
    foot_h = 110
    width = margin + ov_w + gap + in_w + margin
    height = margin + title_h + ov_h + 36 + key_h + foot_h + margin

    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)
    title = font(26, bold=True)
    sub = font(15)
    head = font(16, bold=True)
    body = font(14)
    small = font(13)

    draw.text((margin, margin), "Edmonton airports, freeways, and bridges", font=title, fill=INK)
    draw.text(
        (margin, margin + 36),
        "Simplified sketch of the two scenery lists. North is up. Lines run through the listed centres, not surveyed centrelines.",
        font=sub,
        fill=MUTED,
    )

    overview, _od, _op, oscale = draw_panel(ov_w, ov_h, LON0, LON1, LAT0, LAT1, label_names=False)
    inset, _id, _ip, _is = draw_panel(in_w, in_h, IN_LON0, IN_LON1, IN_LAT0, IN_LAT1, label_names=True)

    ox = margin
    oy = margin + title_h
    image.paste(overview, (ox, oy))
    draw.rectangle([ox, oy, ox + ov_w, oy + ov_h], outline=FRAME)
    draw_north(draw, (ox + 18, oy + 16), font(14, bold=True))
    draw_scale(draw, (ox + 18, oy + ov_h - 36), oscale, small)

    ix = margin + ov_w + gap
    iy = oy
    image.paste(inset, (ix, iy))
    draw.rectangle([ix, iy, ix + in_w, iy + in_h], outline=INSET_FRAME, width=2)
    draw.text((ix + 12, iy + 8), "City Centre inset", font=head, fill=INK)

    swatch_row(draw, margin, oy + ov_h + 14, body)
    draw_key(draw, margin, oy + ov_h + 40, width - 2 * margin, body, head)

    foot = (
        "Squares are the six fields. Blue dots are the river list. Brown dots are the freeway list. "
        "Red crosses were named and then left off: Yellowhead interchanges, including the City Centre helicopter route, "
        "the Mill Creek trestle, Henday diamonds that are not brown dots, Whitemud and Terwillegar overpasses, "
        "and the Groat Road and Capilano Drive bridges north of the river. "
        "A star (*) is an estimated centre. Rabbit Hill Road on the Henday is still not plotted. "
        "Highway 16 west of the Henday, Highway 21, and the other new crosses are on this map and still left off the include list."
    )
    # Wrap the footnote into the full width.
    words = foot.split()
    line = ""
    fy = oy + ov_h + 40 + key_h + 8
    max_w = width - 2 * margin
    for word in words:
        trial = word if not line else line + " " + word
        if text_size(draw, trial, small)[0] <= max_w:
            line = trial
        else:
            draw.text((margin, fy), line, font=small, fill=MUTED)
            fy += 18
            line = word
    if line:
        draw.text((margin, fy), line, font=small, fill=MUTED)

    image.save(OUT, "PNG")
    print(f"wrote {OUT} ({image.size[0]}x{image.size[1]})")


if __name__ == "__main__":
    main()
