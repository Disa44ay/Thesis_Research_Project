---
type: project-state
status: active
updated: 2026-08-14
tags: [current-state, thesis, baa]
related:
  - "[[../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]]"
  - "[[../19_verification/PHASE_3_NOVELTY_LOCK]]"
  - "[[../08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]"
  - "[[../07_topic_selection/TOPIC_LOCK_STATUS]]"
---
# Current State

## Active direction
Football Ball Action Anticipation using synchronized visual and explicit player game-state information on SoccerTrack v2.

## Scientific center
The thesis no longer depends on claiming a novel GNN or novel video-plus-game-state fusion. The main research question is whether explicit player-level game state provides complementary value for predicting temporally localized ball actions in an unobserved future interval.

## Current phase
Phases 1-4 are evidence-locked:
- [[../19_verification/PHASE_1_RELATED_WORK_LOCK]]
- [[../08_experiments/BENCHMARK_PROTOCOL_LOCK]]
- [[../19_verification/PHASE_3_NOVELTY_LOCK]]
- [[../08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]

## Open gates
1. Pin and inspect the canonical SoccerTrack v2 revision.
2. Resolve or exclude match 132831 if the required GSR fields remain affected.
3. Validate BAS-to-GSR-to-video alignment with official loaders.
4. Recompute exact usable events and grouped folds before training.
5. Run a mini feasibility prototype before spending the paid compute budget.

Candidate 02 and Candidate 03 remain historical fallbacks, not active co-primary topics.
