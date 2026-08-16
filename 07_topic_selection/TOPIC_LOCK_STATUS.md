---
type: topic-status
status: keep-and-advance
updated: 2026-08-14
tags: [topic-selection, baa, soccertrack-v2]
related:
  - "[[candidates/Candidate 01 - Game State Aware Action Anticipation]]"
  - "[[candidates/Candidate 01B - Relation Aware Multimodal BAA]]"
  - "[[../19_verification/PHASE_3_NOVELTY_LOCK]]"
  - "[[../00_project_governance/CURRENT_STATE]]"
---
# Topic Lock Status

## Decision
**KEEP AND ADVANCE Candidate 01**, with narrowed novelty.

## Current research framing
Evaluate whether explicit synchronized player-level game state provides complementary predictive value for short-horizon Ball Action Anticipation, and whether relation-aware player modeling adds value beyond flat structured fusion.

## Why it survives
1. BAA exists, so the task is grounded.
2. Game-state fusion exists for detection/spotting, so the information source is grounded.
3. The reviewed literature does not establish the same explicit game-state fusion question for an unobserved future BAA interval.
4. SoccerTrack v2 supplies the necessary synchronized modalities.
5. A negative result remains scientifically interpretable.

## What is no longer claimed
GNNs, player graphs, multimodal football action understanding, tactical context, and future football-event prediction are not treated as first-time inventions.

Final instructor-facing title selection is deferred to Phase 5 and will be recorded in the next release.
