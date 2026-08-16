---
type: session-log
status: active
tags: [session, history]
updated: 2026-08-14
---
# Session Log

## 2026-08-09. Knowledge-base architecture clarified
The project owner decided to maintain two separate Obsidian knowledge vaults.

The reusable vault contains the generic research system and AI pipeline.

This project vault contains only the active research journey, from topic finding and literature review to publishing and defending the thesis in front of the panel.

Non-negotiable rule: do not lose existing knowledge. The vault should remain updated through the latest confirmed chat state so the research history can survive loss of account access.

During this migration, topic-specific material was kept here and generic workflow material was moved into the reusable system vault. Mixed original notes were split by function, not deleted.

## 2026-08-10. Football candidate-title discovery session

### Session objective
Narrow the active thesis search toward a defensible football research topic and candidate title.

### Confirmed project preferences and constraints
1. Stay inside football.
2. Prefer Computer Vision because the instructor specializes in CV.
3. Multimodality is preferred but not mandatory and must be meaningful.
4. Moderate paid Colab research compute may be considered.
5. Large-scale raw-video training remains out of scope.
6. Final deployment must have zero recurring cost.
7. Avoid permanent server-side raw-video storage where possible.
8. Directly downloadable public datasets are preferred, with request-based free academic access acceptable only when timing risk is manageable.
9. Manual annotation is capped around 100 to 150 samples.
10. Plan execution around two continuously active team members.
11. Candidate titles are needed within two days, and the instructor permits multiple candidates.

### User-interest branches
Strong interest was expressed in tactical analysis, future-gameplay prediction, and intelligent search or retrieval inside football video. The search remains open to other football topics that better satisfy the constraints.

### Research findings verified during the session
1. SoccerNet Game State Reconstruction provides a short-sequence football CV benchmark with rich player and pitch state.
2. FAANTRA establishes short-horizon football ball-action anticipation using five-second and ten-second windows.
3. SoccerTrack v2 provides public full-pitch panoramic matches with game-state and ball-action labels.
4. SoccerRAG already covers generic multimodal natural-language soccer information retrieval.
5. FOOTPASS and 2026 PCBAS work already use tactical or graph-based player context, weakening the earlier generic tactical-prior gap.

### Current candidate families
1. [[07_topic_selection/candidates/Candidate 01 - Game State Aware Action Anticipation]]
2. [[07_topic_selection/candidates/Candidate 02 - Tactical Spatiotemporal Retrieval]]
3. [[07_topic_selection/candidates/Candidate 03 - Tactical State Forecasting]]

### Preserved rejected or downgraded branches
1. [[07_topic_selection/rejections/Generic Football RAG]]
2. [[07_topic_selection/rejections/Exact 30 Second Future Prediction]]
3. [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]]

### Next session
Attack Candidate 01 first. Search recent literature for equivalent game-state-aware anticipation, verify dataset alignment and baseline reproducibility, then either kill, narrow, or promote it. After that, perform the same process for Candidates 02 and 03 and prepare 2 to 3 instructor-facing titles.

## Session 2026-08-12, Candidate 01 validation sprint

### External AI research
1. [[15_ai_configuration/research_runs/PR 001 - Gemini Adversarial Literature Hunt]] completed with metadata and reasoning corrections.
2. [[15_ai_configuration/research_runs/PR 002 - Claude Deep Verification]] partially completed before Claude Free quota exhaustion.
3. [[15_ai_configuration/research_runs/PR 003 - Gemini Targeted Verification]] completed with several factual corrections.
4. [[15_ai_configuration/research_runs/PR 004 - Perplexity Novelty Audit]] completed in free Search mode and required a novelty-reasoning correction.

### Dataset work
The user supplied the official SoccerTrack v2 Google Drive folder and uploaded all 10 BAS JSON files. Direct audit produced 23,663 total actions and exposed severe long-tail imbalance plus a small timeline anomaly cluster.

### Candidate evolution
The original game-state anticipation idea was narrowed to [[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]. Generic tactical forecasting was downgraded.

### Compute decision
The project remains feasible only with one-time feature extraction and compact structured preprocessing. End-to-end repeated 4K video training is rejected.

### Immediate next work
Related works, limitations, novelty boundary, benchmark design, title lock, full proposal, hostile review.

## 2026-08-14 - Scientific lock
Claude PR-005 returned KEEP BUT NARROW. Independent re-verification confirmed Candidate 01 but corrected context-window wording, mAP tolerance interpretation, method novelty, SoccerTrack release provenance, provisional BAS cleaning, and fold assignment. Architecture/experiment ladder B0-B5 was locked.
