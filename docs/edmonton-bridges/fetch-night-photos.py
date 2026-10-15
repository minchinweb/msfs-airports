"""Download the curated Wikimedia Commons night photos into reference/<site>/night/ with a SOURCES.md.
Run: python fetch-night-photos.py   (needs only the standard library). Images are 1800 px wide thumbnails."""
import json, os, re, time, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "msfs-airports-reference/1.0 (w_minchin@hotmail.com)"}
PICKS = {
 "R10-high-level": ["High Level Bridge at Night, purple.JPG", "High Level Bridge (15936015759).jpg", "High Level Bridge (16096297456).jpg",
                    "High Level Bridge (16121369032).jpg", "Edmonton High Level Bridge (32979070566).jpg", "High Level Bridge Late Evening.jpg",
                    "High Level Bridge - Valentine's 2017.jpg", "High Level Bridge (14383078920).jpg"],
 "R9-menzies": ["Dudley B. Menzies Bridge (16121360532).jpg", "Dudley R. Menzies Bridge Night Shot.jpg", "The Glowing Menzies - Flickr - Kurayba.jpg"],
 "R11-walterdale": ["Edmonton cityscape.jpg", "The new Walterdale Bridge (26863140898).jpg"],
 "R13-low-level": ["Low Level Bridge (331578242).jpg", "Low Level Bridge (331578329).jpg", "Edmonton Skyline Nightshot.jpg"],
 "F256-funicular": ["Funicular (26012308038).jpg", "Funicular (39175092924).jpg", "Funicular (39175098074).jpg", "Funicular (39886030591).jpg"],
 "P152-muttart": ["Muttart Conservatory Night.jpg"],
 "B255-hotel-macdonald": ["MacDonald Hotel at Night.jpg"],
}
LIGHT = {
 "R10-high-level": "Continuous LED strip along the top chord of the whole truss, cool blue-white by default (blue in the Jan 2017 frames, white-blue in 2017 Valentine's frame). The City says about 60,000 LEDs, colour-changeable, lit nightly since Canada Day 2014 (edmonton.ca 'Light the bridge'). The piers are washed from below by floodlights in the same colour, so the concrete glows (violet, blue, pink or orange in different frames: the colour is set per event, so model blue-white as the default). Other lighting seen: the LRT deck beside it has a white LED edge strip; streets and ramps below are orange sodium.",
 "R9-menzies": "A continuous cool white LED line runs along the outer edge of each guardway/handrail of the LRT deck (white with a blue tint in the long exposures). Tail lights of a train show red. Station platform and ramp lights beside it are white. Same piers floodlit as the High Level frames.",
 "R11-walterdale": "The two arches are outlined edge-on in white (cool white, HLB Lighting Design per the press kit). The deck and shared path are lit by tall street lamps in warm white-yellow (sodium or warm LED). No colour changes seen.",
 "R13-low-level": "2006 frames: the 1900 truss span is outlined in warm amber/orange (low-pressure-sodium look) along the top and bottom chords and the diagonals, with orange street lamps along the road. The Edmonton-Skyline-Nightshot frame (2009) shows the 1948 portals lit white with traffic trails and tall orange street lamps either side. Photos are 10-20 years old; the present lighting may differ.",
 "P152-muttart": "The ridge lines of the glass pyramids are traced with blue/violet LED strip (2009 night frame), the glass glows warm orange from inside, ground lights orange-red.",
 "B255-hotel-macdonald": "The stone facade is floodlit from below in warm white/amber; window rows are warm. Entrance and street level are lit warm white. The roof and copper details are picked out by the same floods.",
 "F256-funicular": "Funicular and promenade handrails carry evenly spaced vertical white LED bars set in the rail uprights (cool white), warm uplighting under the benches and stair treads. The glass elevator/funicular station glows white. Street lamps below on Grierson Hill are orange.",
}
def api(**k):
    k["format"] = "json"
    return json.load(urllib.request.urlopen(urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(k), headers=UA), timeout=60))
for site, names in PICKS.items():
    out = os.path.join(HERE, "reference", site, "night"); os.makedirs(out, exist_ok=True)
    rows = []
    for n in names:
        d = api(action="query", titles="File:" + n, prop="imageinfo", iiprop="url|extmetadata", iiurlwidth=1800,
                iiextmetadatafilter="LicenseShortName|DateTimeOriginal|Artist|LicenseUrl")
        p = next(iter(d["query"]["pages"].values())); i = p["imageinfo"][0]; m = i["extmetadata"]
        fn = re.sub(r"[^A-Za-z0-9._-]+", "-", n).strip("-")
        dest = os.path.join(out, fn)
        if not os.path.exists(dest):
            open(dest, "wb").write(urllib.request.urlopen(urllib.request.Request(i["thumburl"], headers=UA), timeout=120).read()); time.sleep(1)
        artist = re.sub(r"<[^>]+>", "", m.get("Artist", {}).get("value", "?")).strip()
        rows.append(f"| `{fn}` | {m.get('DateTimeOriginal', {}).get('value', '')[:19]} | {artist} | {m.get('LicenseShortName', {}).get('value')} | {i['descriptionurl']} |")
    open(os.path.join(out, "SOURCES.md"), "w", encoding="utf-8").write(
        "# Night photos\n\nWikimedia Commons, downloaded as 1800 px wide copies. Capture time is the EXIF local time as Commons reports it and may be wrong (camera clock or UTC). Lighting as read from the photos is under What the photos show.\n\n"
        "| File | Taken | Author | Licence | Page |\n| --- | --- | --- | --- | --- |\n" + "\n".join(rows) + "\n")
    print(site, len(rows))
