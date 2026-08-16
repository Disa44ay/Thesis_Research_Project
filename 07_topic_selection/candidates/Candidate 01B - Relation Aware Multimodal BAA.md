---
type: candidate-topic
status: strongest-current-candidate
created: 2026-08-12
updated: 2026-08-12
tags: [candidate, baa, multimodal, game-state, relation-aware]
evolved_from:
  - "[[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]"
depends_on:
  - "[[03_datasets/datasets/SoccerTrack v2]]"
  - "[[03_datasets/analysis/SoccerTrack v2 BAS Statistical Audit]]"
  - "[[08_experiments/BENCHMARK_DESIGN_DRAFT]]"
supported_by:
  - "[[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[06_research_gaps/Gap - Relation Aware Player Interactions for BAA]]"
  - "[[04_literature/sources/SOURCE - FAANTRA 2025]]"
  - "[[04_literature/sources/SOURCE - Ochin Game State Action Detection 2025]]"
---
# Candidate 01B: Relation-Aware Multimodal BAA

## Current preferred working title
**Relation-Aware Multimodal Game-State Fusion for Short-Horizon Ball Action Anticipation in Football**

## Exact research question
Does synchronized player-level game state improve temporally localized short-horizon Ball Action Anticipation when fused with visual evidence, and does explicit relation-aware player interaction modeling outperform simple multimodal fusion?

## Benchmark target
Past 30 seconds of context → predict all ball actions occurring in the following 5 seconds.

## Proposed inputs
1. Frozen or pre-extracted visual features from full-pitch video.
2. Player pitch coordinates.
3. Player identities for alignment, not memorization.
4. Team information.
5. Role.
6. Velocity derived from tracking history.
7. Relative spatial relations.

## Proposed outputs
1. Future ball-action class.
2. Temporal occurrence within the 5-second anticipation window.

## Minimum scientific comparison
1. Visual-only baseline.
2. Game-state-only baseline.
3. Simple multimodal fusion.
4. Relation-aware multimodal fusion.
5. Ablations for velocity, team information, relations, visual branch, and game-state branch.

## Why it is stronger than the earlier Candidate 01
The earlier formulation was too broad and could be interpreted as generic tactical context. This version narrows the contribution to explicit synchronized geometry, future action anticipation, controlled fusion baselines, and relation-aware interactions.

## Current verdict
STRONG CANDIDATE, pending final related-work matrix and benchmark policy lock.
