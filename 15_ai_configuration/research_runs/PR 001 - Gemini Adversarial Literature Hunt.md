---
type: ai-research-run
run_id: PR-001
helper: Gemini Pro
status: completed-with-corrections
created: 2026-08-12
updated: 2026-08-12
tags: [ai-run, gemini, novelty, baa]
influenced:
  - "[[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[07_topic_selection/candidates/Candidate 01B - Relation Aware Multimodal BAA]]"
---
# PR 001: Gemini Adversarial Literature Hunt

## Goal
Try to disprove novelty of explicit player-level game-state augmented Ball Action Anticipation.

## Prompt scope
The prompt required a 2020-2026 adversarial search across BAA, tracking-conditioned anticipation, future event prediction, trajectory forecasting, TacticAI, FAANTRA, FOOTPASS, SoccerTrack v2, SoccerNet GSR, and GenTac. It explicitly required primary-source evidence labels, a direct-threat table, SoccerTrack v2 feasibility, leakage analysis, compute feasibility, and a final kill-or-survive verdict.

## Main useful findings
1. The broad idea "use player coordinates to predict future football actions" is not novel.
2. FAANTRA defines the BAA task.
3. TacticAI, event-sequence models, and tactical forecasting papers reduce conceptual novelty.
4. SoccerTrack v2 appears unusually well aligned for a derived BAA task.
5. A narrower multimodal fusion question remained promising.

## Important errors later corrected
1. GenTac arXiv metadata was wrong in the raw report. Correct identifier is arXiv:2604.11786.
2. TacticAI authorship and DOI metadata were wrong. Correct DOI is 10.1038/s41467-024-45965-x.
3. The report overclaimed that all 2026 BAA teams used only video. The safer statement concerns reviewed methods in the official challenge report.
4. It overstated some SoccerTrack v2 actor-label details before the released schema was checked directly.

## Status
Useful discovery run. Not safe as a verbatim literature source.
