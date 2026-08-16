---
type: current-state
status: active
tags: [current-state, thesis]
updated: 2026-08-10
---
# Current State

## Stage
Research exploration and validation. Topic not finally locked.

## Leading direction
Football Video Understanding → SoccerNet ecosystem → Player-Centric Ball Action Spotting, PCBAS.

## Candidate gap priority
1. Player-ID or tracking-drop recovery.
2. Tactical context or tactical priors.
3. Audio-visual continuity.
4. Shared lightweight backbone is currently high risk and rejected for the active constraints unless evidence changes.

## Critical unresolved decisions
Exact final dataset release or version, exact PCBAS benchmark definition, exact baseline to reproduce, exact publicly available multimodal inputs, validated research gap, final research question, and publication venue.

## Hard constraints still active
Public or free datasets only. No dependence on a personal GPU. Free Colab or Kaggle compute must be treated as a real constraint. Team of three. Roughly one month of practical execution. Prefer implementation-heavy work and an end-to-end deployable system. Publication is an opportunity, not a guarantee.

## Most important next action
Verify the PCBAS literature, official dataset or benchmark details, baseline availability, and candidate gaps from primary sources before topic lock.

## State update 2026-08-10

### Immediate goal
Produce 2 to 3 defensible football thesis candidate titles within two days, then continue validation before final topic lock.

### Search scope
Football is now the active domain boundary. Computer Vision is preferred because of instructor fit. Multimodality is a strong preference only when meaningful.

### Current top candidate families
1. [[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]
2. [[07_topic_selection/candidates/Candidate 02 - Tactical Spatiotemporal Retrieval]]
3. [[07_topic_selection/candidates/Candidate 03 - Tactical State Forecasting]]

### Important downgrades and rejections
1. [[07_topic_selection/rejections/Generic Football RAG]] is rejected as a generic thesis framing because SoccerRAG already covers multimodal natural-language soccer retrieval.
2. [[07_topic_selection/rejections/Exact 30 Second Future Prediction]] is rejected as the current forecasting target. Short-horizon or coarse-state prediction remains viable.
3. [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]] is downgraded because FOOTPASS and 2026 PCBAS work already use tactical or graph context.

### New operational constraints
Research compute may expand modestly through Colab, but [[01_goals_constraints/constraints/Zero Cost Deployment]] is a hard deployment rule. Dataset access, annotation, and effective team capacity are now explicit graph nodes.

### Topic status
No final topic is locked.

## State update 2026-08-12, 23:28 Asia/Dhaka

### Deadline
Title submission is due tomorrow. The project is now in a focused related-work, benchmark, novelty, and proposal sprint.

### Strongest candidate
[[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]

### Current gap
[[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]] plus [[06_research_gaps/Gap - Relation Aware Player Interactions for BAA]].

### Dataset
[[03_datasets/datasets/SoccerTrack v2]] is the current primary feasibility dataset. Direct BAS analysis is recorded in [[03_datasets/analysis/SoccerTrack v2 BAS Statistical Audit]].

### Benchmark
[[08_experiments/BENCHMARK_DESIGN_DRAFT]] uses 30 seconds observed and 5 seconds anticipated, with all future actions predicted as a set.

### Compute
[[09_implementation/COMPUTE_AND_DATA_PIPELINE]] keeps the topic feasible by converting raw 4K video and multi-gigabyte GSR into compact reusable features.

### Topic lock status
Not formally locked, but Candidate 01B is now a STRONG CANDIDATE rather than a broad hypothesis.
