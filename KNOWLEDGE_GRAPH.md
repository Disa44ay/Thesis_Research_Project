---
type: moc
status: active
tags: [knowledge-graph, thesis, moc]
updated: 2026-08-10
---
# Thesis Knowledge Graph

## Governance and current state
[[00_project_governance/PROJECT_RULES]]
→ [[00_project_governance/CURRENT_STATE]]

## Research journey
[[00_context/USER_PROFILE]]
→ [[01_goals_constraints/GOALS_AND_CONSTRAINTS]]
→ [[02_journey/DOMAIN_EXPLORATION]]
→ [[03_datasets/DATASET_FINDINGS]]
→ [[04_literature/LITERATURE_FINDINGS]]
→ [[05_direction/PCBAS_STATE]]
→ [[06_research_gaps/RESEARCH_GAPS]]
→ [[07_topic_selection/TOPIC_LOCK_STATUS]]
→ [[08_experiments/EXPERIMENT_STATUS]]
→ [[09_implementation/IMPLEMENTATION_STATUS]]
→ [[10_writing/THESIS_AND_PAPER_STATUS]]
→ [[11_publication/PUBLICATION_STATUS]]
→ [[12_defense/DEFENSE_STATUS]]

## Football branch
[[05_direction/concepts/SoccerNet]]
→ [[05_direction/concepts/PCBAS]]
→ [[05_direction/baselines/FOOTPASS]]
→ [[05_direction/concepts/SoccerNet Tracking]]
→ [[06_research_gaps/Candidate Gap A - ID Drop Repair]]
→ [[06_research_gaps/Candidate Gap B - Tactical Priors]]
→ [[06_research_gaps/Candidate Gap D - Audio Visual Fusion]]

## Control and history
[[13_execution/ONE_MONTH_EXECUTION]]
→ [[14_decisions/DECISION_LOG]]
→ [[16_session_history/SESSION_LOG]]

## Current reasoning chain
Football interest → Football Video Understanding → SoccerNet ecosystem → PCBAS leading candidate.

No local GPU + one-month constraint → avoid heavy end-to-end raw-video training → prefer official pre-extracted features or structured tracking data when scientifically legitimate.

Publication goal → novelty claims require primary evidence.

Multimodal requirement → every claimed modality must be verified from public dataset access before topic lock.


## Graph update 2026-08-10

### Current constraint cluster
[[01_goals_constraints/constraints/Football Domain Scope]]
→ [[14_decisions/2026-08-10 - Football Scope Locked]]
→ [[07_topic_selection/TOPIC_LOCK_STATUS]]

[[01_goals_constraints/constraints/Computer Vision Preference]]
→ [[02_journey/DOMAIN_EXPLORATION]]

[[01_goals_constraints/constraints/Multimodality Preference]]
→ [[14_decisions/2026-08-10 - Multimodality Is Preference Not Requirement]]
→ [[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]

[[04_literature/sources/SOURCE - Google Colab Paid Services 2026]]
→ [[01_goals_constraints/constraints/Research Compute Budget]]
→ [[14_decisions/2026-08-10 - Research Compute Expanded Deployment Still Free]]
← [[01_goals_constraints/constraints/Zero Cost Deployment]]

[[01_goals_constraints/constraints/Dataset Access Policy]]
→ [[14_decisions/2026-08-10 - Dataset Access Preference]]

[[01_goals_constraints/constraints/Team Capacity]]
→ [[01_goals_constraints/constraints/Annotation Budget]]
→ [[14_decisions/2026-08-10 - Annotation Ceiling]]

[[01_goals_constraints/constraints/Title Deadline]]
→ [[14_decisions/2026-08-10 - Candidate Title Strategy]]
→ [[07_topic_selection/TOPIC_LOCK_STATUS]]

### Game-state and anticipation branch
[[04_literature/sources/SOURCE - SoccerNet GSR 2024]]
→ [[03_datasets/datasets/SoccerNet GSR]]
→ [[05_direction/concepts/Game State Reconstruction]]

[[04_literature/sources/SOURCE - FAANTRA 2025]]
→ [[03_datasets/datasets/SoccerNet Ball Action Anticipation]]
→ [[05_direction/concepts/Ball Action Anticipation]]
→ [[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]

[[04_literature/sources/SOURCE - SoccerTrack v2 2025]]
→ [[03_datasets/datasets/SoccerTrack v2]]
→ [[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]
→ [[07_topic_selection/candidates/Candidate 03 - Tactical State Forecasting]]

### Retrieval branch
[[04_literature/sources/SOURCE - SoccerRAG 2024]]
→ [[07_topic_selection/rejections/Generic Football RAG]]
→ [[05_direction/concepts/Tactical Retrieval]]
→ [[07_topic_selection/candidates/Candidate 02 - Tactical Spatiotemporal Retrieval]]

[[03_datasets/datasets/SoccerTrack v2]]
→ [[07_topic_selection/candidates/Candidate 02 - Tactical Spatiotemporal Retrieval]]

### PCBAS evidence correction branch
[[04_literature/sources/SOURCE - FOOTPASS 2025]]
→ [[05_direction/baselines/FOOTPASS]]
→ [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]]

[[04_literature/sources/SOURCE - PCBAS Extensions 2026]]
→ [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]]
→ [[06_research_gaps/Candidate Gap B - Tactical Priors]]

### Forecasting correction branch
[[04_literature/sources/SOURCE - FAANTRA 2025]]
→ [[07_topic_selection/rejections/Exact 30 Second Future Prediction]]
→ [[05_direction/concepts/Ball Action Anticipation]]

### Current candidate convergence
[[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]
→ [[07_topic_selection/TOPIC_LOCK_STATUS]]

[[07_topic_selection/candidates/Candidate 02 - Tactical Spatiotemporal Retrieval]]
→ [[07_topic_selection/TOPIC_LOCK_STATUS]]

[[07_topic_selection/candidates/Candidate 03 - Tactical State Forecasting]]
→ [[07_topic_selection/TOPIC_LOCK_STATUS]]

### Reasoning rule
Rejected, downgraded, and superseded nodes remain in the graph. They are evidence of the journey, not clutter to delete.
