---
type: proposal-draft
status: proposal-ready
created: 2026-08-14
updated: 2026-08-14
tags: [proposal, baa, soccertrack-v2, methodology]
related:
  - "[[PROPOSAL_ARTIFACT_INDEX]]"
  - "[[../07_topic_selection/PHASE_5_TITLE_PACKAGE]]"
  - "[[../19_verification/PHASE_3_NOVELTY_LOCK]]"
  - "[[../20_system_architecture/END_TO_END_DATA_SYSTEM_ARCHITECTURE]]"
  - "[[../20_system_architecture/FEASIBILITY_PILOT_PLAN]]"
---
# Academic Proposal Draft

## Title
**Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football**

## Abstract
This thesis investigates whether explicit synchronized player-level game state improves short-horizon Ball Action Anticipation. Existing BAA work is primarily visual, while separate football detection/spotting work shows that positions, velocities, teams, and player relations can complement visual evidence when the action is already observable. The study derives a reproducible BAA protocol from SoccerTrack v2 and compares visual-only, state-only, simple-fusion, flat-relations, and relation-aware models. Multi-gigabyte GSR is streamed once into compact tensors and 4K video is sampled once into frozen embeddings. A 10-minute feasibility pilot gates the full paid-compute workflow.

## Problem Statement
Given historical football context, predict all ball-related actions occurring in the following 5-second unobserved interval. Each output contains action class, future timestamp, and confidence. The benchmark may expose up to 30 seconds of history, while the initial compute-safe model uses a shorter recent context.

## Research Gap
Football BAA already exists. Video plus explicit game-state football action understanding also already exists for detection/spotting. The reviewed literature does not establish whether synchronized explicit player game state provides complementary value for temporally localized prediction of ball actions that have not yet occurred. The thesis tests that bridge directly.

## Research Questions
1. Does explicit player-level game state improve short-horizon BAA relative to visual-only anticipation?
2. Does relation-aware player modeling provide additional value beyond flat state and flat-relational features when the information content is controlled?

## Objectives
1. Pin and validate a reproducible SoccerTrack v2 release.
2. Derive and validate a BAA-style benchmark.
3. Build a compact streaming/feature-extraction pipeline.
4. Establish B0-B5 controlled baselines.
5. Run grouped match-level evaluation and per-class analysis.
6. Measure compute/storage/inference efficiency.
7. Build a zero-recurring-cost demonstration after the research pipeline is stable.

## Methodology
### Data
Use SoccerTrack v2 video, GSR, and BAS. Final event counts and match folds are regenerated only after the pinned release passes the correction/alignment gate.

### Benchmark
Predict all events in the next 5 seconds. Use the SN-BAA-compatible 10-class primary space for methodological comparability and fuller SoccerTrack reporting as a secondary analysis. Use match-level grouped evaluation, no cross-half windows, training-only normalization/class weights, and strict future-information exclusion.

### Models
- B0: statistical/no-event floor
- B1: visual-only
- B2: game-state-only
- B3: simple visual + state fusion
- B4: flat relational features without message passing
- B5: relation-aware fusion

### Primary comparisons
- B3 versus B1 answers the core modality-value question.
- B5 versus B4 isolates relation-aware reasoning from merely supplying relational features.

### Metrics
Use BAA-style mAP at finite temporal tolerances and infinity, mAPavg, per-class AP, fold variation, and efficiency measures. Avoid direct numerical SOTA claims against SoccerNet because SoccerTrack is a different dataset/domain.

## Large-Data Plan
GSR is streamed one half at a time, reduced to required state fields, downsampled initially to 5 Hz, and stored as compact per-half arrays. Panoramic video is sampled initially around 6.25 fps, passed through a frozen visual encoder once, and stored as FP16 embeddings. Training windows reference continuous arrays instead of duplicating overlapping clips.

## Validation and Double-Checking
Every event must map to a valid half/segment, GSR time/frame, and video time. Known correction issues are quarantined. Approximately 100 randomly sampled aligned events receive a manual video/GSR/BAS spot-check. Exclusions, corrections, alignment statistics, class counts, and fold manifests are preserved as artifacts.

## Feasibility Pilot
Run approximately 10 minutes of a clean match/half through the complete pipeline on free/low-cost Colab before full paid compute. The pilot must prove data access, GSR streaming, video feature extraction, BAS alignment, window generation, tiny-model training, checkpointing, prediction schema, and evaluator execution. Accuracy is not a pilot success criterion.

## Compute Strategy
Treat the expected 100 Colab compute units as a soft envelope. Reserve acceleration for one-time visual feature extraction and lightweight model training. CPU handles JSON parsing, alignment, statistics, and fold construction. Stop after 10 minutes and after one full match to measure actual cost before scaling.

## Expected Contributions
1. Evidence for or against the value of explicit game state for future BAA.
2. Controlled evidence on relational features versus relation-aware modeling.
3. Reproducible SoccerTrack-derived BAA construction and validation protocol.
4. Compute-efficient multimodal system and zero-cost demo architecture.

## Limitations
Small number of independent matches, university/full-pitch domain rather than professional broadcast, severe class imbalance, derived benchmark rather than official SoccerTrack BAA, and dynamic cloud compute availability. Claims remain bounded accordingly.

## Execution Order
1. canonical release and correction gate
2. 10-minute pilot
3. full compact feature extraction
4. B1-B3 one-fold smoke experiments
5. B4-B5 controlled study
6. grouped full evaluation
7. essential ablations and per-class analysis
8. writing, reproducibility release, and demo

The compiled LaTeX/PDF version is tracked by [[PROPOSAL_ARTIFACT_INDEX]].
