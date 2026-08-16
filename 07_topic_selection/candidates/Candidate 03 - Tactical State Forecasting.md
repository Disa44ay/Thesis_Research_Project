---
type: candidate-topic
status: hypothesis-high-risk
created: 2026-08-10
updated: 2026-08-10
tags: [candidate, forecasting, tactical, trajectories, football]
depends_on:
  - "[[01_goals_constraints/constraints/Football Domain Scope]]"
  - "[[01_goals_constraints/constraints/Research Compute Budget]]"
  - "[[03_datasets/datasets/SoccerTrack v2]]"
supported_by:
  - "[[04_literature/sources/SOURCE - SoccerTrack v2 2025]]"
related:
  - "[[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]"
---
# Candidate 03: Tactical State Forecasting

## Working title
**Short Term Tactical State Forecasting in Football from Player Trajectories and Game Context**

## Candidate research question
Can a lightweight temporal or graph model forecast a coarse future tactical state or outcome from recent player trajectories and game context?

## Why it is attractive
1. Full-pitch trajectories naturally support tactical reasoning.
2. Structured trajectories can drastically reduce raw-video compute.
3. The result can integrate with a backend that visualizes current state, forecast state, and similar historical situations.
4. The problem could be more unique than standard event spotting if the target is well defined.

## Why it is currently high risk
The exact prediction target is not yet validated. "Tactical state" must become an objective label or derivable quantity such as zone progression, possession transition, attack outcome, or another measurable state.

## Kill conditions
Reject if the target requires more than the 100 to 150 annotation ceiling, if the label is subjective, or if no meaningful baseline and evaluation protocol can be defined quickly.

## Downgrade update 2026-08-12

This candidate is now lower priority because [[04_literature/sources/SOURCE - GenTac 2026]] and [[04_literature/sources/SOURCE - TacticGen 2026]] already occupy generic tactical forecasting and trajectory-generation territory. See [[07_topic_selection/downgraded/Generic Tactical Forecasting]].
