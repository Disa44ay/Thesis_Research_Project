---
type: decision
status: rejected-compute-pattern
created: 2026-08-12
updated: 2026-08-12
tags: [decision, compute, video, rejection]
caused_by:
  - "[[01_goals_constraints/constraints/Research Compute Budget]]"
  - "[[03_datasets/analysis/SoccerTrack v2 GSR Practical Handling]]"
results_in:
  - "[[09_implementation/COMPUTE_AND_DATA_PIPELINE]]"
---
# 2026-08-12: Raw 4K End-to-End Training Rejected

Repeated end-to-end training on the complete 4K panoramic video corpus is rejected for the active compute budget.

The accepted strategy is one-time visual feature extraction with a frozen encoder and repeated training on compact precomputed embeddings plus compact game-state tensors.
