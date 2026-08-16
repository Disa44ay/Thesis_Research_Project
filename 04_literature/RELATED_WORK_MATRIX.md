---
type: literature-matrix
status: active-draft
created: 2026-08-12
updated: 2026-08-12
tags: [literature, related-work, novelty]
related:
  - "[[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[06_research_gaps/Gap - Relation Aware Player Interactions for BAA]]"
---
# Related Work Matrix

| Work | Task | Video | Full player geometry | Future discrete action | Future timing | Main limitation relative to Candidate 01B |
|---|---|---|---|---|---|---|
| [[04_literature/sources/SOURCE - FAANTRA 2025]] | BAA | Yes | No | Yes | Yes | no explicit synchronized full-pitch game state |
| [[04_literature/sources/SOURCE - SoccerNet Challenges 2026]] | BAA challenge | Yes | no reviewed method verified with explicit GSR | Yes | Yes | current methods centered on visual or VLM-derived context |
| [[04_literature/sources/SOURCE - Ochin Game State Action Detection 2025]] | current action detection | Yes | Yes | No | current action localization | detection, not anticipation |
| [[04_literature/sources/SOURCE - GenTac 2026]] | trajectory and tactical forecasting | No | Yes | neighboring event/tactic output | not SoccerNet-style BAA timing | no visual BAA fusion |
| [[04_literature/sources/SOURCE - TacticAI 2024]] | corner-kick tactical prediction | No | Yes | partial outcome prediction | No | set-piece only, no video, no open-play BAA |
| [[04_literature/sources/SOURCE - Seq2Event 2022]] | next-event prediction | No | event coordinates only | Yes | event-time prediction | sparse event stream, not dense player state plus video |
| [[04_literature/sources/SOURCE - EventGPT ScoutGPT 2025-2026]] | next-event sequence prediction | No | event-level spatial context | Yes | partial or relative | symbolic event stream, not full tracking plus video |
| [[04_literature/sources/SOURCE - TacticGen 2026]] | tactical trajectory generation | No | Yes | not the same BAA target | No equivalent BAA timing | large-scale trajectory generation, not public-data multimodal BAA |
| [[04_literature/sources/SOURCE - SoccerTrack v2 2025]] | dataset | Yes | Yes | labels available | timestamps available | enables benchmark, does not itself solve anticipation |

## Current literature logic
BAA exists → video-centered methods remain difficult → video plus game state already helps current-action understanding → structured game state predicts future football behavior in neighboring tasks → SoccerTrack v2 provides synchronized video, GSR, and BAS → the unresolved question is whether explicit relation-aware game state improves temporally localized future BAA.

## Novelty discipline
Do not claim:

1. First future football action prediction.
2. First football GNN.
3. First video plus game-state football model.
4. First football tactical forecasting.

Potentially defensible after final verification:

"No exact prior work was identified in the current search that fuses synchronized full-pitch player game state with visual features specifically for temporally localized short-horizon Ball Action Anticipation."
