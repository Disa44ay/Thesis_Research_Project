---
type: benchmark-design
status: draft-needs-lock
created: 2026-08-12
updated: 2026-08-12
tags: [benchmark, baa, soccertrack-v2, evaluation]
depends_on:
  - "[[03_datasets/analysis/SoccerTrack v2 BAS Statistical Audit]]"
  - "[[03_datasets/analysis/SoccerTrack v2 GSR Practical Handling]]"
  - "[[05_direction/concepts/Ball Action Anticipation]]"
related:
  - "[[08_experiments/BASELINE_AND_ABLATION_PLAN]]"
---
# Benchmark Design Draft

## Task
Observe 30 seconds of football context and predict all BAS actions occurring in the following 5 seconds.

## Inputs
1. Visual feature sequence from the observed 30 seconds.
2. Synchronized structured player game state from the same 30 seconds.

## Targets
A set of future actions, each containing at minimum:

1. Action class.
2. Temporal occurrence inside the 5-second anticipation window.

## Split policy
Use match-level splits only. Randomly mixing windows from the same match across train and test is rejected because it creates leakage.

Tentative split for analysis: 6 train, 2 validation, 2 test. This is not locked until per-match class balance is analyzed.

## Window policy
Prefer a protocol close to established FAANTRA/SoccerNet BAA conventions rather than inventing a completely unrelated task.

## Class policy
Must be chosen before model evaluation.

1. PASS and DRIVE dominate.
2. HEADER has only 35 examples.
3. GOAL has only 47.
4. FREE KICK has 164.
5. Any exclusion threshold must be objective and documented before experiments.

## Evaluation
Primary metrics should remain compatible with BAA where feasible, including temporal-tolerance mAP and aggregate mAP.

Secondary analysis should include per-class AP and frequent-versus-rare action behavior.

## Leakage controls
1. Match-level split.
2. No future GSR frames in the observation input.
3. Half-aware timestamp conversion.
4. Explicit handling of overlapping windows.
5. Do not use raw persistent IDs in a way that lets the model memorize specific players across train and test.
