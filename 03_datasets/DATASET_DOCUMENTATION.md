---
type: dataset-documentation
status: single-match-verified
dataset: SoccerTrack v2
updated: 2026-09-10
related:
  - "[[DATASET_FINDINGS]]"
  - "[[../22_feasibility/FEASIBILITY_STUDY_REPORT]]"
---

# Dataset Documentation — SoccerTrack v2 (as verified)

This consolidates only what has been directly verified against the
actual distributed files, as opposed to what the dataset's documentation
claims. Earlier candidate-selection reasoning remains in
[[DATASET_FINDINGS]]; this file is the execution-facing counterpart.

## Access

Google Drive release (used because the Hugging Face route returned an
authorization error in the working environment at time of access).
Source reconciliation note: where the public landing page and the
actual distributed files disagree, this project follows the Reusable
Research OS's source-reconciliation rule and defers to the distributed
files.

## Inventory (verified)

- 22 video files, 20 GSR JSON files, 11 BAS directory entries (one is a
  non-data `.DS_Store`), 102 raw files.
- No MOT files present in this Drive mirror. Does not block the chosen
  BAA route, because player identity/team/role/boxes/pitch coordinates
  are already present in GSR.
- **10 matches with complete BAS + GSR coverage:** 117092, 117093,
  118575, 118576, 118577, 118578, 128057, 128058, 132831, 132877.

## GSR schema (verified on 117093)

COCO-like structure: `info`, `images`, `annotations`, `categories`.
Player annotations include `image_id`, `track_id`, `player_id`, role,
team, jersey number, image-space bounding boxes (`bbox_image`), pitch
coordinates (`bbox_pitch`, `bbox_pitch_raw`). 25 FPS. `image_id` uses a
zero-based local-frame rule: `local_frame = int(last_6_digits(image_id)) - 1`.

## BAS schema (verified on 117093)

Top-level keys: `match_id`, `fps`, `actions`. Each action includes a
`position` field that is **absolute match time**, not restarted at zero
for the second half - confirmed by min/max position inspection
(half 1: 680-2,694,000 ms; half 2: 2,700,760-5,506,280 ms).

## Per-match statistics (verified for match 117093 only)

| Field | Value |
|---|---|
| BAS events | 2,252 |
| Unique players | 41 |
| Raw classes | 12 |
| Most frequent classes | PASS (951), DRIVE (889), HIGH PASS (150) |
| Rarest classes | HEADER (3), GOAL (5) |
| First-half GSR frames | 67,650 (45:06 at 25 FPS) |
| Second-half GSR frames | 70,475 (46:59 at 25 FPS) |
| BAS-actor-to-GSR identity coverage | 100% (23/23 first half, 27/27 second half) |
| First-half canonical video | ~3.35 GB, 4096x1080, 25 FPS, 2706.002s, 67,625 decoded frames |
| RGB presentation-timeline offset vs. match time | +1.000s (see [[../22_feasibility/BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]]) |

**The above per-match statistics are verified for match 117093 only.**
They should not be assumed to hold for the other nine matches until
each is individually processed. In particular, class-imbalance ratios
and the RGB presentation offset are both candidates for per-match
variation, not confirmed constants.

## Known open items

- Canonical dataset revision is not pinned (a specific release/commit
  identifier for reproducibility has not been recorded in any provided
  source).
- Match 132831 has a documented correction issue requiring
  canonical-revision verification (carried forward from Release 03/04 -
  see [[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]]). **Now
  fully sourced:** two swapped calibration keypoints in the upstream
  repo produced ~1260.95px RMS error (vs. ~18.07px corrected); this
  match's GSR was generated from the faulty calibration and has not
  been regenerated. See
  [[../22_feasibility/MATCH_132831_CALIBRATION_DEFECT]]. Effectively
  **9 of 10 matches are currently usable for game-state work**, not 10.
- Rare-class handling policy (whether to use the 12-class raw view or
  the provisional 10-class BAA-compatible view excluding FREE KICK and
  GOAL) is not locked.

------------------------------------------------------------------------
