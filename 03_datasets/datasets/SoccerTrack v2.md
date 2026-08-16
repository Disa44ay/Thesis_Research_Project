---
type: dataset
status: verified-core-facts
created: 2026-08-10
updated: 2026-08-10
tags: [dataset, soccertrack, panoramic, tracking, gsr, bas]
supported_by:
  - "[[04_literature/sources/SOURCE - SoccerTrack v2 2025]]"
related:
  - "[[05_direction/concepts/Game State Reconstruction]]"
  - "[[05_direction/concepts/Ball Action Anticipation]]"
  - "[[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]"
  - "[[07_topic_selection/candidates/Candidate 02 - Tactical Spatiotemporal Retrieval]]"
  - "[[07_topic_selection/candidates/Candidate 03 - Tactical State Forecasting]]"
---
# Dataset: SoccerTrack v2

## Verified core facts
Public football dataset with 10 full-length panoramic 4K matches, per-frame pitch coordinates and player identity or role or team information, and 12 ball-action classes.

Dataset license is CC BY 4.0 according to the public repository.

## Why it is attractive
It combines complete-pitch spatial state with action annotations and therefore supports tactical and temporal research without requiring every research idea to infer player geometry from broadcast footage first.

## Main risk
Raw 4K full-match processing may still exceed the practical project budget. The project should prefer structured annotations, trajectories, selective clips, or downsampled visual processing unless a candidate specifically requires raw frames.

## Direct access and file verification, 2026-08-12

### User-verified full dataset access
Google Drive folder supplied and confirmed by the user:

https://drive.google.com/drive/folders/1N2Qx2qkFgRtpbHitl2Vh6sLVYGgqkWwn

The folder contains the release components including BAS, raw data, videos, GSR, and MOT.

### Direct BAS verification
The user uploaded the complete 10-match BAS JSON set. See [[03_datasets/analysis/SoccerTrack v2 BAS Statistical Audit]].

### Practical GSR note
The released GSR units are multi-gigabyte files. See [[03_datasets/analysis/SoccerTrack v2 GSR Practical Handling]].

### Current thesis role
SoccerTrack v2 is the primary feasibility dataset for [[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]. It enables a derived 30-second observation to 5-second future BAA benchmark without large-scale manual relabeling.
