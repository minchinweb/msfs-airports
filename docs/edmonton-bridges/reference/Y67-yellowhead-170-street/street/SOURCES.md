# Y67 Yellowhead / 170 Street: street-level photos (Mapillary)

Gathered 2026-11-23 from the Mapillary graph API, `images` endpoint, bounding box -113.61777, 53.57058, -113.61271, 53.57530 (the mapped deck and approaches, plus about 150 m). The query returned 146 images. Panoramas and images without a thumbnail were skipped. Four were kept, at least 30 m apart from each other, nearest the structure first. Each thumbnail is the API's `thumb_1024_url`, not scaled.

## Licence

The query asked for the fields id, captured_at, computed_geometry, is_pano, creator, and thumb_1024_url. It did not ask for a licence field, and none was returned. The licence is unconfirmed. Mapillary's default is CC BY-SA 4.0, and that is recorded here as unconfirmed, not as the licence of these images. Creator usernames are kept for attribution.

## Images

Distance is from each camera point to the nearest mapped piece of the structure in `geometry.json` (deck or approach), in metres. It is a plan distance, not a survey.

| File | Captured (UTC) | Creator | Distance to structure (m) | Mapillary page | What it shows |
| --- | --- | --- | --- | --- | --- |
| `mly-611131474017633.jpg` | 2021-07-28 13:40 | rps333 | 3.8, on the east deck | https://www.mapillary.com/app/?pKey=611131474017633 | Signalised junction with a truck and concrete barriers, and a flat landscape beyond. The camera is at the east deck, but the frame shows the junction, not the deck. Shows approaches, not the structure. |
| `mly-301991668220262.jpg` | 2018-07-10 23:46 | lvl5 | 1.4, on the west deck | https://www.mapillary.com/app/?pKey=301991668220262 | Multi-lane road with a concrete barrier on the right, lamp posts, and a traffic queue. The camera is on the west deck, but no deck edge, rail, or pier is identifiable in the frame. Shows the roadway, not the structure. |
| `mly-607864951031785.jpg` | 2021-07-28 13:40 | rps333 | 1.5, on the south approach | https://www.mapillary.com/app/?pKey=607864951031785 | Ramp or merge with truck signs, barriers, and lane channelizers. Approach only. |
| `mly-323409399174384.jpg` | 2018-07-10 23:46 | lvl5 | 1.2, on the north approach | https://www.mapillary.com/app/?pKey=323409399174384 | Road with trucks ahead and a concrete barrier. Approach only. |

Which images show the structure: none clearly shows the deck, its edges, or its supports. Two (611 and 301) are taken on or beside the deck, but the frames show the roadway. Two (607 and 323) are on the approaches. None shows the Yellowhead roadway underneath.

The other 142 images from the query were not downloaded. Four were enough for the rule above.
