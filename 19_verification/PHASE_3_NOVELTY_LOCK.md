---
type: phase-lock
status: locked
created: 2026-08-14
updated: 2026-08-14
tags: [phase-3, novelty, research-gap, locked]
related:
  - "[[PHASE_1_RELATED_WORK_LOCK]]"
  - "[[../06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[../07_topic_selection/TOPIC_LOCK_STATUS]]"
---
# Phase 3 - Novelty Lock

## Core research question
Does explicit player-level game-state information improve temporally localized short-horizon Ball Action Anticipation compared with visual-only anticipation?

## Secondary research question
Does relation-aware modeling of player interactions provide additional anticipation value beyond simple or flat game-state fusion when the underlying information is controlled?

## Defensible gap
Existing BAA methods predict future ball actions from visual observations and, in recent work, semantic tactical context derived from vision-language models. Separately, action-detection and spotting research shows that explicit positions, velocities, teams, and multi-player context can complement visual evidence when the target action is already observable. The reviewed literature does not establish whether synchronized explicit player game state provides complementary value for class-and-time prediction of ball actions in an unobserved future interval.

## Novelty hierarchy
1. **Core:** empirical test of explicit game state for future BAA.
2. **Supporting scientific:** controlled flat-state, flat-relations, and relation-aware comparisons.
3. **Supporting reproducibility:** derived SoccerTrack v2 BAA protocol.
4. **Engineering:** compute-efficient preprocessing and deployable inference system.

## Claims prohibited
- first video plus game-state football model
- first football future-event prediction model
- first graph model for football interactions
- first contextual BAA method
- SoccerNet leaderboard state of the art from SoccerTrack experiments
- professional-football generalization without testing
