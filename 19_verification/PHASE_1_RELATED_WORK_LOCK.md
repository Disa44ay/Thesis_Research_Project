---
type: phase-lock
status: locked
created: 2026-08-14
updated: 2026-08-14
tags: [phase-1, related-work, locked]
related:
  - "[[../04_literature/RELATED_WORK_MATRIX]]"
  - "[[../15_ai_configuration/research_runs/PR 005 - Claude Final Evidence Lock]]"
  - "[[FULL_EVIDENCE_REVERIFICATION_2026-08-14]]"
---
# Phase 1 - Related Work Lock

The core literature argument is intentionally small and adversarial.

## Anchor papers
1. [[../04_literature/sources/SOURCE - FAANTRA 2025]] establishes football Ball Action Anticipation.
2. [[../04_literature/sources/SOURCE - SoccerNet Challenges 2026]] documents the current 30-second observation to 5-second future challenge and reviewed BAA methods.
3. [[../04_literature/sources/SOURCE - Ochin Game State Action Detection 2025]] establishes video plus explicit game-state graph fusion for observed-action detection.
4. [[../04_literature/sources/SOURCE - SoccerTrack v2 2025]] provides the synchronized public data substrate.

## Supporting novelty threats
- [[../04_literature/sources/SOURCE - Beyond Pixels 2025]]: longer-context game-state reasoning for observed-action denoising.
- [[../04_literature/sources/SOURCE - FOOTPASS 2025]]: multimodal multi-agent tactical context for spotting.
- [[../04_literature/sources/SOURCE - TacticAI 2024]]: geometry-based predictive tactical reasoning for corner kicks.
- [[../04_literature/sources/SOURCE - GenTac 2026]] and [[../04_literature/sources/SOURCE - TacticGen 2026]]: structured multi-agent tactical forecasting/generation.
- [[../04_literature/sources/SOURCE - Seq2Event 2022]] and [[../04_literature/sources/SOURCE - EventGPT ScoutGPT 2025-2026]]: future event prediction from event sequences.

## Locked conclusion
Game-state fusion, graphs, contextual football action understanding, and future football-event prediction all have prior art. The defensible unresolved question is whether synchronized explicit player-level game state provides complementary value for temporally localized Ball Action Anticipation in an unobserved future interval.
