---
type: dataset-engineering
status: feasibility-plan
created: 2026-08-12
updated: 2026-08-12
tags: [dataset, gsr, preprocessing, colab, compute]
related:
  - "[[03_datasets/datasets/SoccerTrack v2]]"
  - "[[09_implementation/COMPUTE_AND_DATA_PIPELINE]]"
---
# SoccerTrack v2 GSR Practical Handling

## User-observed storage reality
Individual GSR annotation folders or large released GSR units are approximately 2.5 to 3 GB, making direct upload into chat unnecessary and impractical.

## Official-format facts carried forward
1. GSR is released at 25 fps.
2. It contains pitch-space player information and identity-related attributes.
3. The current official documentation warns that shipped GSR files use a SoccerNet-COCO-style structure and may differ from older simplified examples.
4. Second-half BAS-to-GSR alignment must be half-aware. Raw global positions cannot be naively interpreted as within-half time.
5. Track IDs may change across halves, while player identity fields can help reconnect identities when available.

## Processing strategy
Do not train from multi-gigabyte JSON repeatedly.

1. Stream one match or half at a time.
2. Keep only fields needed by the research question.
3. Downsample structured state from 25 fps to a lower rate such as 2 to 5 Hz for initial experiments.
4. Derive velocity and relation features once.
5. Save compact Parquet, NPZ, or tensor files.
6. Train models from compact features rather than raw JSON.

## Evidence status
The exact optimal sampling rate is an implementation hypothesis, not a verified fact.
