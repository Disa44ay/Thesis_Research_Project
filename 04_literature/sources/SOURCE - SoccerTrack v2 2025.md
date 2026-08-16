---
type: source
status: verified
created: 2026-08-10
updated: 2026-08-10
tags: [source, dataset, soccertrack, tracking, gsr, bas]
url: https://github.com/AtomScott/SoccerTrack-v2
supports:
  - "[[03_datasets/datasets/SoccerTrack v2]]"
  - "[[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]"
  - "[[07_topic_selection/candidates/Candidate 02 - Tactical Spatiotemporal Retrieval]]"
  - "[[07_topic_selection/candidates/Candidate 03 - Tactical State Forecasting]]"
---
# Source: SoccerTrack v2, 2025

Primary public repository and linked technical report.

## Verified claims at 2026-08-10
1. The repository is public.
2. The dataset contains 10 full-length panoramic 4K matches.
3. It includes per-frame Game State Reconstruction annotations with 2D pitch coordinates, jersey-based player IDs, roles, and teams.
4. It includes Ball Action Spotting labels across 12 action classes.
5. Dataset licensing is CC BY 4.0 and code licensing is MIT according to the repository.
6. The repository links a Hugging Face dataset distribution.

## Compute warning
Full-length 4K video is still large. Candidate projects should test whether annotations, derived trajectories, downsampled clips, or selective video use can avoid unnecessary full-resolution processing.
