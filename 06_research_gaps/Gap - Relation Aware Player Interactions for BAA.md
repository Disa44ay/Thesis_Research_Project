---
type: research-gap
status: candidate-method-gap
created: 2026-08-12
updated: 2026-08-12
tags: [gap, relation-aware, graph, player-interactions, baa]
supported_by:
  - "[[04_literature/sources/SOURCE - Ochin Game State Action Detection 2025]]"
  - "[[04_literature/sources/SOURCE - TacticAI 2024]]"
related:
  - "[[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]"
---
# Gap: Relation-Aware Player Interactions for BAA

## Motivation
Simple visual-feature plus coordinate-feature concatenation may be too incremental because multimodal fusion and football GNNs already exist in neighboring tasks.

## Candidate method contribution
Model explicit player relations before multimodal fusion, potentially including:

1. Relative displacement.
2. Pairwise distance.
3. Relative velocity.
4. Same-team versus opposition relation.
5. Local player density.
6. Attacker-defender proximity.
7. Spatial neighborhood graph.
8. Ball proximity if reliable ball state is available.

## Research question
Does relation-aware game-state encoding improve future action class and temporal localization beyond visual-only, game-state-only, and simple-fusion baselines?

## Risk
Graph neural networks themselves are not novel in football. The novelty must come from the BAA task, exact relation design, controlled comparison, and evidence that relations add predictive value beyond simple fusion.
