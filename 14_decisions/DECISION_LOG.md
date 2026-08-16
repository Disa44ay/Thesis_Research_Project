---
type: decision-log
status: migrated
tags: [decisions, history]
source: DECISION_LOG.md
updated: 2026-08-10
---
# Thesis Decision Log

## Decision 1 — Backend + AI balance
Chosen:
- approximately 60% coding
- approximately 40% research

Reason:
The team wants to transition toward AI while leveraging existing backend strength.

## Decision 2 — Compute
Constraint:
No local GPU.

Allowed:
- university-access Colab
- Kaggle
- free cloud GPU/TPU resources where available.

Implication:
Avoid end-to-end heavy video/VLM training.

## Decision 3 — Dataset policy
Chosen:
Public/free datasets only.

No private data.

## Decision 4 — Publication target
Chosen:
Realistic Scopus-indexed publication potential.

Q2 is an aspiration, not a guarantee.

## Decision 5 — Research depth
Chosen:
Medium research depth.

Comfortable with:
- deep learning papers,
- attention,
- Transformers,
- loss functions,
- evaluation.

Avoid:
- heavy theoretical derivations.

## Decision 6 — Domain preference
Preferred:
Football Video Understanding.

Secondary:
Satellite Vision / Remote Sensing.

General:
Computer Vision / Multimodal AI.

## Decision 7 — Current leading direction
Chosen provisionally:
**SoccerNet → Player-Centric Ball Action Spotting (PCBAS).**

Reason:
Best intersection of:
- football interest,
- modern CV research,
- public benchmark ecosystem,
- backend opportunity,
- structured-feature compute feasibility,
- portfolio value.

## Decision 8 — Standard Action Spotting
Not preferred as final research direction.

Reason:
Compute is excellent, but the task is mature and novelty is harder.

## Decision 9 — Ball Action Anticipation
Interesting but risky.

Reason:
prediction is difficult and scores may be low; practical demonstration is harder.

## Decision 10 — Soccer VQA
Interesting but compute/scope risk is higher.

## Decision 11 — Heavy end-to-end vision architecture
Rejected for current timeline/compute.

## Decision 12 — Current candidate gaps
Priority:
1. Player-ID/tracking-drop recovery
2. Tactical context/priors
3. Audio-visual continuity

These remain hypotheses until literature validation.

## Critical unresolved decisions
- exact final dataset release/version,
- exact PCBAS benchmark definition,
- exact baseline to reproduce,
- exact multimodal inputs available publicly,
- validated research gap,
- final research question,
- publication venue.

## Current project status
**Research exploration / validation stage. Topic is not finally locked.**

## Decision 13 — Football-only search scope
Chosen: keep active topic search within football. See [[14_decisions/2026-08-10 - Football Scope Locked]].

## Decision 14 — Multimodality is preferred, not mandatory
Chosen: meaningful multimodal work receives preference, but stronger unimodal football CV research may win. See [[14_decisions/2026-08-10 - Multimodality Is Preference Not Requirement]].

## Decision 15 — Research compute may expand modestly
Chosen: modest paid Colab compute may be used if necessary. This does not remove the large-video feasibility constraint. See [[14_decisions/2026-08-10 - Research Compute Expanded Deployment Still Free]].

## Decision 16 — Deployment recurring cost must be zero
Chosen: do not depend on paid hosting, inference, databases, object storage, or persistent GPU services. Raw video should not require permanent server-side storage. See [[01_goals_constraints/constraints/Zero Cost Deployment]].

## Decision 17 — Dataset access preference
Chosen: direct free download preferred, free request-based academic access acceptable with timing safety and fallback. See [[14_decisions/2026-08-10 - Dataset Access Preference]].

## Decision 18 — Annotation ceiling
Chosen: approximately 100 to 150 manual annotations maximum. See [[14_decisions/2026-08-10 - Annotation Ceiling]].

## Decision 19 — Effective execution capacity
Plan around two continuously active members even though the formal team has three. See [[01_goals_constraints/constraints/Team Capacity]].

## Decision 20 — Candidate title strategy
The instructor allows multiple candidate titles. Prepare a small evidence-backed set within two days rather than force an early final lock. See [[14_decisions/2026-08-10 - Candidate Title Strategy]].

## Decision 21 — Generic football RAG rejected
Generic natural-language RAG over football data is not sufficiently novel after verification of SoccerRAG. See [[07_topic_selection/rejections/Generic Football RAG]].

## Decision 22 — Exact thirty-second gameplay prediction rejected as current framing
Use short-horizon or coarse future targets instead. See [[07_topic_selection/rejections/Exact 30 Second Future Prediction]].

## Decision 23 — Broad PCBAS tactical-context gap downgraded
Recent verified work already uses tactical and graph context. See [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]].

## Decisions added 2026-08-12
1. [[14_decisions/2026-08-12 - Candidate 01 Narrowed to Relation Aware Multimodal BAA]]
2. [[14_decisions/2026-08-12 - SoccerTrack v2 Primary Feasibility Dataset]]
3. [[14_decisions/2026-08-12 - BAA Benchmark Protocol 30s to 5s]]
4. [[14_decisions/2026-08-12 - Raw 4K End to End Training Rejected]]
5. [[14_decisions/2026-08-12 - External AI Helper Strategy]]
6. [[14_decisions/2026-08-12 - Strategic Related Work and Proposal Sprint]]

## 2026-08-14 - Candidate 01 survives full re-verification
Core novelty is now the empirical value of explicit player game state for future BAA. Relation-aware modeling is a controlled method study, not the main invention. Exact dataset counts and folds remain gated on canonical release/alignment validation. See [[../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]].
