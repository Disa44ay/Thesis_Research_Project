---
type: research-gap
status: promising-but-unproven
created: 2026-08-12
updated: 2026-08-12
tags: [gap, baa, multimodal, game-state]
supported_by:
  - "[[04_literature/sources/SOURCE - FAANTRA 2025]]"
  - "[[04_literature/sources/SOURCE - SoccerNet Challenges 2026]]"
  - "[[04_literature/sources/SOURCE - Ochin Game State Action Detection 2025]]"
  - "[[04_literature/sources/SOURCE - GenTac 2026]]"
  - "[[04_literature/sources/SOURCE - TacticAI 2024]]"
  - "[[04_literature/sources/SOURCE - Seq2Event 2022]]"
  - "[[04_literature/sources/SOURCE - EventGPT ScoutGPT 2025-2026]]"
enabled_by:
  - "[[03_datasets/datasets/SoccerTrack v2]]"
leads_to:
  - "[[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]"
---
# Gap: Multimodal Game-State Fusion for BAA

## Exact boundary
The current systematic search has not identified a prior method that combines synchronized explicit full-pitch player game state with visual representations specifically to predict the class and temporal occurrence of unseen ball actions in a short future window.

## What is already known
1. [[04_literature/sources/SOURCE - FAANTRA 2025]] establishes Ball Action Anticipation from video.
2. [[04_literature/sources/SOURCE - SoccerNet Challenges 2026]] shows active BAA methods remain centered on visual or VLM-derived context. No reviewed BAA report identified in the official results was verified to use explicit synchronized per-player pitch coordinates or GSR trajectories.
3. [[04_literature/sources/SOURCE - Ochin Game State Action Detection 2025]] already fuses video and explicit game state for current-action detection.
4. [[04_literature/sources/SOURCE - GenTac 2026]], [[04_literature/sources/SOURCE - TacticAI 2024]], [[04_literature/sources/SOURCE - Seq2Event 2022]], and [[04_literature/sources/SOURCE - EventGPT ScoutGPT 2025-2026]] show that structured football state can predict future behavior in neighboring tasks.

## Safe novelty language
"No exact prior work was identified in the current search" is acceptable after final verification.

"First ever" is not yet justified.

## Kill condition
Reject or narrow further if a paper is found that performs synchronized visual plus explicit per-player game-state fusion for temporally localized future BAA under a substantially equivalent protocol.
