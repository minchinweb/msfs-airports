# Y68 Yellowhead / 156 Street: street-level photos (Mapillary)

Gathered 2026-11-23 from the Mapillary graph API, `images` endpoint, two bounding boxes (-113.5935, 53.5745, -113.5870, 53.5800) and (-113.5935, 53.5795, -113.5870, 53.5830). Together they cover the mapped deck and approaches plus about 150 m. The query returned 336 images before duplicates were removed (315 unique). All 315 were non-panoramic with a thumbnail. Four were kept: the four nearest the structure's mapped deck and approaches, at least 30 m apart from each other. Each thumbnail is the API's `thumb_1024_url`, not scaled.

## Licence

The query asked for the fields id, captured_at, computed_geometry, is_pano, creator, and thumb_1024_url. It did not ask for a licence field, so none was returned. The licence is unconfirmed. Mapillary's default is CC BY-SA 4.0, and that is recorded here as unconfirmed, not as the licence of these images. Creator usernames are kept for attribution.

## Images

Distance is from each camera point to the nearest mapped node of the deck or approach ways in `geometry.json`, in metres. It is a plan distance, not a survey. Times are UTC.

| File | Captured (UTC) | Creator | Distance to structure (m) | Mapillary page | What it shows |
| --- | --- | --- | --- | --- | --- |
| `mly-168062425247961.jpg` | 2018-07-11 18:21 | lvl5 | 0.7, on the deck | https://www.mapillary.com/app/?pKey=168062425247961 | Multi-lane roadway with a concrete parapet and metal railing on the right, lamp posts, and a traffic queue. The camera is on the 156 Street deck. No pier, deck soffit, or Yellowhead roadway is visible. Shows the deck edge. |
| `mly-148722357268545.jpg` | 2018-07-11 18:14 | lvl5 | 1.1, at the junction | https://www.mapillary.com/app/?pKey=148722357268545 | Signalised junction with a "156 ST" sign on the signal mast and a "West Yellowhead Trail" sign. Shows the approach and junction, not the deck. |
| `mly-473088773762755.jpg` | 2018-07-11 18:21 | lvl5 | 1.6, on the approach | https://www.mapillary.com/app/?pKey=473088773762755 | Two-lane road with a white car ahead and an overhead sign gantry, a "Yellowhead Trail West" sign, and a "156 Street" sign. Approach only. |
| `mly-243773217516633.jpg` | 2018-07-11 18:14 | lvl5 | 2.9, on the approach | https://www.mapillary.com/app/?pKey=243773217516633 | Two-lane road with trucks, a 60 km/h sign, a light pole, and an industrial yard on the right. Approach only. |

Which images show the structure: the first (168062) is on the deck and shows its edge. The other three show the approaches and junction only. None shows the structure's supports, its soffit, or the Yellowhead roadway beneath it.

The other 311 images from the query were not downloaded.
