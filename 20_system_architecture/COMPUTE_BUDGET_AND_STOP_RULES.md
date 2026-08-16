---
type: compute-plan
status: planned
created: 2026-08-14
updated: 2026-08-14
tags: [colab, compute-budget, stop-rules, feasibility]
related:
  - "[[VISUAL_FEATURE_EXTRACTION_PIPELINE]]"
  - "[[FEASIBILITY_PILOT_PLAN]]"
  - "[[../01_goals_constraints/constraints/Research Compute Budget]]"
---
# Compute Budget and Stop Rules

Colab resources and accelerator consumption are dynamic, so the project uses measurement-based gates instead of promising exact GPU-hours.

## Soft 100-unit envelope
- pilot visual extraction: <= 5 units
- remaining full visual extraction: <= 15 units
- debugging/core pipeline: <= 10 units
- B1-B5 core experiments: <= 40 units
- essential ablations: <= 15 units
- emergency reserve/re-runs: 15 units

CPU-only runtimes should handle JSON streaming, BAS processing, alignment, statistics, folds, and compact artifact construction wherever possible.

## Stop rules
1. Benchmark 10 minutes before full extraction.
2. Benchmark one full match before processing all matches.
3. Do not launch five-fold runs until B1-B5 work on one fold.
4. Do not spend accelerator units on optional ablations until RQ1 has an answer.
5. If a runtime is not using the accelerator, switch to standard CPU runtime.
6. If projected extraction exceeds budget, reduce frame rate/resolution/backbone before spending the rest.
