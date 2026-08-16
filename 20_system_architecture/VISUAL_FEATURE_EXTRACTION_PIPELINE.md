---
type: implementation-plan
status: planned
created: 2026-08-14
updated: 2026-08-14
tags: [video, frozen-features, ffmpeg, compute]
related:
  - "[[END_TO_END_DATA_SYSTEM_ARCHITECTURE]]"
  - "[[COMPUTE_BUDGET_AND_STOP_RULES]]"
  - "[[../09_implementation/COMPUTE_AND_DATA_PIPELINE]]"
---
# Visual Feature Extraction Pipeline

## Principle
Raw panoramic 4K video is processed once. Normal model training uses compact frozen embeddings.

## Initial pipeline
1. Download/copy one match or half to temporary runtime storage.
2. Sample at approximately 6.25 fps as an evidence-backed starting rate.
3. Resize while preserving useful full-pitch spatial information.
4. Run a frozen pretrained visual encoder.
5. Store FP16 embeddings in a continuous per-half array with timestamps.
6. Delete the temporary raw runtime copy once verified.
7. Repeat for the next match.

## Why this fits the budget
For roughly 900 minutes, 6.25 fps corresponds to about 337,500 sampled timestamps. A 768-dimensional FP16 embedding matrix is about 0.5 GiB before metadata, far smaller than the source videos.

## Stop rule
Measure 10 minutes first. If extraction rate or compute-unit consumption projects beyond budget, reduce frame rate, input resolution, or backbone size before full extraction.
