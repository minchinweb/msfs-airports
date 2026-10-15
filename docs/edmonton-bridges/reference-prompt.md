# Reference subagent prompt

Send this to one generalPurpose subagent at a time. Fill the braces. Do not start the next structure until that subagent has returned. Do not commit.

Voice and schema to match: `docs/edmonton-bridges/reference/R15-dawson/NOTES.md` and `docs/edmonton-bridges/reference/R11-walterdale/geometry.json`.

---

Gather modeling reference for {NAME} ({CODE}) in Edmonton. Repo: D:\Code\msfs-airports.

{ONE SENTENCE: what it is, the project centre, and the road or object it carries.}

{WHAT IT IS NOT. Name the neighbouring codes and centres. Do not copy their span lengths, widths, or pier notes into this folder. Present-day package only. Do not model a demolished span.}

Write only:

- docs/edmonton-bridges/reference/{FOLDER}/NOTES.md
- docs/edmonton-bridges/reference/{FOLDER}/SOURCES.md
- docs/edmonton-bridges/reference/{FOLDER}/geometry.json
- docs/edmonton-bridges/reference/{FOLDER}/photos/

Do not edit PRIORITY.md, bridges.md, freeway-bridges.md, lrt.md, STATUS.md, draw-map.py, bridge-geometry.json, lrt-tracks.json, or any existing reference folder.

## Read first

- The inventory row for {CODE} in bridges.md, freeway-bridges.md, or lrt.md, and the matching line in PRIORITY.md.
- The {CODE} object in docs/edmonton-bridges/bridge-geometry.json, or in lrt-tracks.json if it is track. {WAY IDS AND A LINE NUMBER, IF KNOWN.} Read the rest of the object. Compute horizontal WGS84 plan lengths. A clipped approach is not a climb to grade. A plan_length_m is not a structural length.
- docs/edmonton-bridges/reference/R15-dawson/NOTES.md and SOURCES.md for voice and photo rules.
- docs/edmonton-bridges/reference/R11-walterdale/geometry.json for the schema.

## NOTES.md

Short sentences. Cited numbers. Both figures when sources disagree. Do not average. Do not invent a height by adding or subtracting citations. Do not scale a photograph. OSM maxheight and width tags are mapper tags, not deck elevations, unless a published source states the same number.

Sections:

1. Opening: what it is, year, centre, which road, which way the lanes run, and what it is not.
2. Bridge: type, span count and lengths, total length, girder or arch or truss depth, pier count and type, clearance, sidewalks, and any widening or rehabilitation that changed the silhouette.
3. Approaches: each end separately, and each carriageway if they differ. Gradient, elevation change, and where each road meets grade. If unpublished, say so. OSM approach polylines are plan geometry only.
4. Deck: elevation above sea level and the datum; elevation above the river or the road underneath; thickness; width of each carriageway and of the whole crossing; lanes; sidewalk or path width and which side; crossfall; longitudinal grade.
5. Still missing.

Search City of Edmonton, Alberta Transportation, HistoricPlaces, engineering papers, Structurae, Wikipedia (cite its sources), and Edmonton City as Museum. Environment Canada gauge 05DF001 is at the Low Level Bridge and uses a local assumed datum. Do not convert a gauge reading into a geodetic deck elevation unless a source already does so.

## Photos

Open licence only (CC or public domain). Need the elevation, the piers or supports, the deck, and both approaches if open frames exist. Neighbouring structures may appear in the distance; say which structure is which. SOURCES.md table: file, what it shows, URL, licence. Not-open images are URL only under "Not downloaded". A 1920 px Wikimedia thumbnail is acceptable if you say so. Skip near-duplicates.

## geometry.json

code {CODE}, name {NAME}, centre {CENTRE AS [lat, lon]}, crs EPSG:4326, coordinate_order [lat, lon], geometry_source, geometry_retrieved {DATE}. plan_length_m is horizontal WGS84 along the nodes, one decimal. Decks, approaches, and paths that belong to this structure. Drop ways that are a different code, and say so in dropped_note. No invented elevations.

Numbers are unique across every prefix. Bridge codes already use 1–136. Do not invent a new code. The next free number is recorded in docs/edmonton-bridges/draw-map.py.

## Shell

Every Shell command must request required_permissions ["all"]. The default sandbox fails immediately with "Terminal unavailable".

## Return

Files written, photo count, span lengths and any heights with sources, how carriageways or neighbouring ways were split, and the still-missing list. Do not commit.
