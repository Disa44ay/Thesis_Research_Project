---
type: project-state
status: feasibility-ready
updated: 2026-08-16
tags: [current-state, thesis, baa, feasibility-ready]
related:
  - "[[../07_topic_selection/PHASE_5_TITLE_PACKAGE]]"
  - "[[../19_verification/PHASE_3_NOVELTY_LOCK]]"
  - "[[../20_system_architecture/END_TO_END_DATA_SYSTEM_ARCHITECTURE]]"
  - "[[../21_proposal/PROPOSAL_REVISION_2026-08-14]]"
  - "[[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]]"
---
# Current State

## Primary title

**Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football**

## Core research question

Does explicit synchronized player-level game state improve temporally localized short-horizon Ball Action Anticipation relative to visual-only anticipation?

## Secondary research question

If game state helps, does relation-aware player modeling add value beyond flat state and flat relational features receiving the same underlying information?

## Evidence boundary

The reviewed literature establishes video-based football BAA and separately establishes game-state-assisted football action detection/spotting. The current claim is narrower: the project will test whether explicit synchronized player state adds predictive value to unseen-future BAA.

## Dataset

SoccerTrack v2 is the primary feasibility dataset, but the exact experimental revision has **not yet been pinned**. The canonical revision must pass schema, correction, and cross-modal alignment validation before final counts or folds are frozen.

## Benchmark direction

- future horizon: 5 seconds,
- variable-size multi-event prediction,
- action class + future temporal location + confidence,
- up to 30 seconds of available history in the broader benchmark design,
- shorter effective context permitted for the initial model/pilot,
- match-level grouped evaluation where the final usable match count permits,
- BAA-style temporal mAP,
- exact class/fold policy frozen only after canonical data validation.

## Planned model comparison

1. visual-only,
2. game-state-only,
3. simple fusion,
4. flat relational features,
5. relation-aware fusion.

## Proposal

The original long proposal is preserved, but the current instructor-facing artifact is the concise verified proposal described in [[../21_proposal/PROPOSAL_REVISION_2026-08-14]] and supported by [[../21_proposal/CITATION_AND_SOURCE_AUDIT]].

## Immediate next action

Run the independently reproducible feasibility pilot described in [[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]].

## Critical status

**The feasibility pilot has not run. No scientific model result exists.**
