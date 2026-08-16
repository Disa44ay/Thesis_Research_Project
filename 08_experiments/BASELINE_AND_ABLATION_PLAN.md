---
type: experiment-plan
status: draft
created: 2026-08-12
updated: 2026-08-12
tags: [baselines, ablations, baa, multimodal]
related:
  - "[[08_experiments/BENCHMARK_DESIGN_DRAFT]]"
  - "[[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]"
---
# Baseline and Ablation Plan

## Core baselines
1. **Visual only:** frozen or pre-extracted visual features plus a lightweight temporal anticipation head.
2. **Game-state only:** player coordinates, team, role, velocity, and history through a lightweight temporal encoder.
3. **Simple fusion:** concatenate or late-fuse visual and structured embeddings.
4. **Proposed relation-aware fusion:** explicit player interaction encoder plus temporal game-state representation fused with visual features.

## Minimum ablations
1. Remove velocity.
2. Remove team information.
3. Remove explicit player relations.
4. Remove visual branch.
5. Remove game-state branch.

## Scientific purpose
The experiment must separate four questions:

1. Does video alone work?
2. Does game state alone carry future predictive signal?
3. Does adding game state help video?
4. Does relation-aware modeling help beyond simple fusion?
