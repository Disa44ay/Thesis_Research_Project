---
type: implementation-plan
status: planned
created: 2026-08-14
updated: 2026-08-14
tags: [gsr, json, streaming, compression]
related:
  - "[[END_TO_END_DATA_SYSTEM_ARCHITECTURE]]"
  - "[[DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]"
  - "[[../03_datasets/analysis/SoccerTrack v2 GSR Practical Handling]]"
---
# GSR Streaming and Compression Pipeline

## Problem
Dense 25-fps GSR JSON files are too large to repeatedly parse during training and can be multi-gigabyte per half.

## Pipeline
1. Stream records with an incremental JSON parser or the official loader. Never rely on full-file `json.load` for the large halves.
2. Keep only fields needed for anticipation: timestamp/frame, x, y, role, team relation, trajectory IDs for continuity, and masks.
3. Derive velocity from historical positions after alignment.
4. Start with 5 Hz temporal sampling as an implementation hypothesis, not an optimality claim.
5. Convert variable annotations to fixed/padded player tensors plus validity masks.
6. Save per-half compact NPZ/Parquet artifacts.
7. Keep IDs only in metadata unless an explicit identity experiment is later approved.

## Storage pattern
Continuous state arrays are stored once. Training windows hold offsets into those arrays instead of copying overlapping states.

## Relation construction
Pairwise relative position, distance, relative velocity, and same-team/opponent indicators can be computed at training time or from compact neighbor indexes. Full dense edge tensors do not need to be permanently stored.
