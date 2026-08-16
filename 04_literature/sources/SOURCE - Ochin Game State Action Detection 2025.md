---
type: source
status: verified-primary
created: 2026-08-12
updated: 2026-08-12
tags: [source, action-detection, game-state, gnn, video]
supports:
  - "[[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[06_research_gaps/Gap - Relation Aware Player Interactions for BAA]]"
related:
  - "[[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]"
---
# SOURCE: Ochin et al. 2025

## Paper
**Game State and Spatio-Temporal Action Detection in Soccer Using Graph Neural Networks and 3D Convolutional Networks**

Primary identifier: arXiv:2502.15462. ICPRAM 2025 paper DOI 10.5220/0013161100003905.

## Verified relevance
1. Uses video plus explicit football game state.
2. Structured state includes player positions, velocities, team information, and temporal player track information.
3. Uses GNN context with a 3D CNN visual branch.
4. Solves spatio-temporal **action detection**, not future action anticipation.
5. Therefore it kills any claim that video plus game-state fusion for football action understanding is new.
6. It does not by itself kill the narrower future-anticipation research question.

## Threat level
HIGH architectural threat, MEDIUM exact-task threat.
