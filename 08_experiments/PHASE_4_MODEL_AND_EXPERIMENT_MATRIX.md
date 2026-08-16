---
type: experiment-plan
status: architecture-locked
created: 2026-08-14
updated: 2026-08-14
tags: [phase-4, model, baselines, ablations]
related:
  - "[[BENCHMARK_PROTOCOL_LOCK]]"
  - "[[BASELINE_AND_ABLATION_PLAN]]"
  - "[[../19_verification/PHASE_3_NOVELTY_LOCK]]"
  - "[[../09_implementation/COMPUTE_AND_DATA_PIPELINE]]"
---
# Phase 4 - Model and Experiment Matrix

## Design principle
The scientific contribution comes from controlled comparisons. The model should remain lightweight.

## Initial effective context
5 seconds of recent visual and game-state history, while the benchmark can expose up to 30 seconds. Longer context is optional ablation work.

## Visual branch
Sample low-rate video, extract frozen pretrained features once, and train only a lightweight temporal encoder during normal experiments.

## Game-state branch
Use player x/y position, derived velocity, role, masks, and team relationships. Player IDs support trajectory continuity but are not semantic learned inputs.

## Core models
- **B0 Statistical floor:** class/no-event priors.
- **B1 Visual-only:** visual temporal encoder + query decoder.
- **B2 Game-state-only:** flat/pooled player state + temporal encoder + query decoder.
- **B3 Simple fusion:** visual + flat state.
- **B4 Flat-relations:** visual + explicit pairwise relation features without graph message passing.
- **B5 Relation-aware fusion:** visual + relation-aware player encoder + temporal encoder.

## What comparisons mean
- B3 > B1 supports value of explicit game state for BAA.
- B4 > B3 supports value of explicit relation features.
- B5 > B4 supports value of relational message passing beyond the same information.
- B5 <= B1 can still be a valid negative result about transfer from detection to anticipation.

## Required ablations
1. relation-aware vs flat-relations
2. no game state
3. no visual input
4. remove velocity if time permits
5. remove team relation if time permits

## Decoder
Use a fixed set of event queries, Hungarian matching, actionness/no-event prediction, class prediction, and normalized future timestamp regression. Determine the number of queries from training-fold event statistics only.

## Scope exclusions
No backbone zoo, no tracking reconstruction, no camera-calibration research, no end-to-end 4K fine-tuning, no cross-dataset transfer requirement, and no unnecessary fusion-block novelty.
