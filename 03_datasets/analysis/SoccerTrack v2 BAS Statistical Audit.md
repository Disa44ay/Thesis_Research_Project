---
type: dataset-audit
status: verified-from-user-files
created: 2026-08-12
updated: 2026-08-12
tags: [dataset, soccertrack-v2, bas, audit, class-imbalance]
dataset:
  - "[[03_datasets/datasets/SoccerTrack v2]]"
feeds:
  - "[[08_experiments/BENCHMARK_DESIGN_DRAFT]]"
  - "[[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]"
---
# SoccerTrack v2 BAS Statistical Audit

## Evidence source
Direct analysis of the 10 BAS JSON files uploaded by the user on 2026-08-12.

## Total actions
23,663 labeled actions across 10 matches.

## Class distribution
| Action | Count | Share |
|---|---:|---:|
| PASS | 10,276 | 43.43% |
| DRIVE | 9,106 | 38.48% |
| HIGH PASS | 1,276 | 5.39% |
| OUT | 867 | 3.66% |
| CROSS | 438 | 1.85% |
| THROW IN | 423 | 1.79% |
| BALL PLAYER BLOCK | 401 | 1.69% |
| PLAYER SUCCESSFUL TACKLE | 328 | 1.39% |
| SHOT | 302 | 1.28% |
| FREE KICK | 164 | 0.69% |
| GOAL | 47 | 0.20% |
| HEADER | 35 | 0.15% |

## Key findings
1. Raw sample count is strong for an undergraduate benchmark.
2. Class imbalance is severe. PASS and DRIVE dominate.
3. HEADER is the main evaluation danger with only 35 examples.
4. GOAL is also very rare with 47 examples.
5. Only 108 of 23,663 actions lack a `player_id`, approximately 0.46 percent.
6. A class policy must be defined before model experiments to avoid cherry-picking.

## Raw 30s-to-5s window simulation
Using the released event timelines and a 5-second stride produced approximately:

1. 12,090 candidate windows.
2. 9,282 windows with at least one action.
3. 7,447 windows with more than one action.
4. Maximum of 9 actions in a 5-second future window.
5. Mean of approximately 1.94 actions per candidate window.

These raw counts include timeline anomalies and must not be treated as final benchmark statistics until preprocessing rules are locked.

## Timeline anomaly
96 suspicious first-half `OUT` annotations occur after minute 50 across matches 117092, 132831, and 132877. Some first-half `gameTime` values extend implausibly far. This suggests a small annotation or timeline artifact requiring cleaning or half-aware alignment.

## Consequence
The benchmark should predict a set of future actions, not collapse the task into ordinary single-label next-action classification.
