---
type: dataset
status: verified-core-facts
created: 2026-08-10
updated: 2026-08-10
tags: [dataset, soccernet, gsr, broadcast-video]
supported_by:
  - "[[04_literature/sources/SOURCE - SoccerNet GSR 2024]]"
related:
  - "[[05_direction/concepts/Game State Reconstruction]]"
---
# Dataset: SoccerNet Game State Reconstruction

## Verified core facts
SoccerNet-GSR was introduced in 2024 for Game State Reconstruction from football broadcast video.

The primary paper reports 200 video sequences of 30 seconds with detailed pitch, camera, and athlete annotations.

## Why it matters
The short-sequence format is potentially much more feasible than training over hundreds of complete matches while retaining genuine computer-vision complexity.

## Open checks before topic lock
1. current access procedure,
2. exact storage footprint,
3. practical Colab preprocessing cost,
4. which annotations can be used without leakage for a proposed downstream task.
