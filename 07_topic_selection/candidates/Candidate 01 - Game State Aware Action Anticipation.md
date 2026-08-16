---
type: candidate-topic
status: hypothesis-top-tier
created: 2026-08-10
updated: 2026-08-10
tags: [candidate, anticipation, game-state, multimodal, football]
depends_on:
  - "[[01_goals_constraints/constraints/Football Domain Scope]]"
  - "[[01_goals_constraints/constraints/Research Compute Budget]]"
  - "[[01_goals_constraints/constraints/Zero Cost Deployment]]"
  - "[[03_datasets/datasets/SoccerNet Ball Action Anticipation]]"
  - "[[05_direction/concepts/Game State Reconstruction]]"
supported_by:
  - "[[04_literature/sources/SOURCE - FAANTRA 2025]]"
  - "[[04_literature/sources/SOURCE - SoccerTrack v2 2025]]"
related:
  - "[[07_topic_selection/candidates/Candidate 03 - Tactical State Forecasting]]"
---
# Candidate 01: Game State Aware Action Anticipation

## Working title
**Game State Aware Multimodal Action Anticipation in Football Using Visual and Spatiotemporal Player Context**

## Candidate research question
Can structured spatial player state and movement context improve short-horizon football action anticipation beyond visual evidence alone?

## Why it survived the first sweep
1. Football action anticipation is an established but recent task through the 2025 FAANTRA work.
2. Short horizons of five to ten seconds are already benchmarked, avoiding the unsupported ambition of exact thirty-second future prediction.
3. SoccerTrack v2 shows that detailed player trajectories, identities, roles, teams, and ball-action labels can exist together in a public dataset.
4. Game-state features create a meaningful second modality or representation rather than decorative multimodality.
5. The final system can expose predictions, player states, and tactical timelines through a lightweight backend without storing raw video permanently.

## Research contribution hypothesis
Fuse visual or video-derived context with structured game-state or trajectory context for anticipation, then evaluate whether the structured state improves timing, rare-action prediction, or robustness.

## Major unresolved risks
1. Direct prior work may already combine equivalent game-state features with action anticipation.
2. SoccerNet anticipation data and SoccerTrack v2 may not align directly enough for one clean benchmark.
3. A new cross-dataset setup could create domain-shift or evaluation-validity problems.
4. Compute must remain bounded.

## Kill conditions
Reject if recent literature already demonstrates the same fusion for the same task, if no defensible dataset alignment exists, or if evaluation would depend on large manual relabeling.

## Evolution update 2026-08-12

This original candidate is preserved as a historical node. It evolved into [[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]] after adversarial literature review showed that generic tactical context, football GNNs, video plus game-state action detection, and future event prediction already exist.
