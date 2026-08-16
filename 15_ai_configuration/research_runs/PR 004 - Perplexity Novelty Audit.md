---
type: ai-research-run
run_id: PR-004
helper: Perplexity Free
mode: Search
status: completed-with-reasoning-correction
created: 2026-08-12
updated: 2026-08-12
tags: [ai-run, perplexity, novelty-audit]
influenced:
  - "[[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[03_datasets/datasets/SoccerTrack v2]]"
---
# PR 004: Perplexity Novelty Audit

## Goal
Run an independent adversarial audit of the exact novelty boundary and SoccerTrack v2 suitability.

## Strong findings
1. Ochin 2025 is the closest architecture-level threat because it already fuses video with explicit player game state.
2. FAANTRA is the closest task-level threat because it already defines future Ball Action Anticipation.
3. GenTac, TacticGen, TacticAI, Seq2Event, and EventGPT reduce broader conceptual novelty but do not exactly match the proposed input-output setup.
4. SoccerTrack v2 contains the infrastructure needed for a synchronized video, GSR, and BAS derived benchmark.

## Reasoning correction
Perplexity labeled the exact novelty statement CONTRADICTED while also stating that no paper exactly matched the full setup. This conflated "video plus game state for football action prediction" with "video plus game state for future BAA."

The corrected status is **LIKELY BUT NOT PROVEN** until the final related-work sweep is complete.

## Additional corrections
1. SoccerTrack v2 dataset licensing is not UNKNOWN. The official repository provides dataset licensing under CC BY 4.0.
2. A two-dataset SoccerTrack v2 plus SoccerNet BAA main experiment is not required and could introduce unnecessary domain mismatch.
3. Off-screen broadcast-player reasoning is a conditional fallback story, not the clean primary story for panoramic SoccerTrack v2.
