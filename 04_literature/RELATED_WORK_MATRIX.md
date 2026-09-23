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

  -------------------------------------------------------------------------------------------------------------------------
  Work                               Task          Video      Full player   Future         Future timing     Main
                                                              geometry      discrete                         limitation
                                                                            action                           relative to
                                                                                                             Candidate 01B
  ---------------------------------- ------------- ---------- ------------- -------------- ----------------- --------------
  [[04_literature/sources/SOURCE -   BAA           Yes        No            Yes            Yes               no explicit
  FAANTRA 2025]]                                                                                             synchronized
                                                                                                             full-pitch
                                                                                                             game state

  [[04_literature/sources/SOURCE -   BAA challenge Yes        no reviewed   Yes            Yes               current
  SoccerNet Challenges 2026]]                                 method                                         methods
                                                              verified with                                  centered on
                                                              explicit GSR                                   visual or
                                                                                                             VLM-derived
                                                                                                             context

  [[04_literature/sources/SOURCE -   current       Yes        Yes           No             current action    detection, not
  Ochin Game State Action Detection  action                                                localization      anticipation
  2025]]                             detection                                                               

  [[04_literature/sources/SOURCE -   trajectory    No         Yes           neighboring    not               no visual BAA
  GenTac 2026]]                      and tactical                           event/tactic   SoccerNet-style   fusion
                                     forecasting                            output         BAA timing        

  [[04_literature/sources/SOURCE -   corner-kick   No         Yes           partial        No                set-piece
  TacticAI 2024]]                    tactical                               outcome                          only, no
                                     prediction                             prediction                       video, no
                                                                                                             open-play BAA

  [[04_literature/sources/SOURCE -   next-event    No         event         Yes            event-time        sparse event
  Seq2Event 2022]]                   prediction               coordinates                  prediction        stream, not
                                                              only                                           dense player
                                                                                                             state plus
                                                                                                             video

  [[04_literature/sources/SOURCE -   next-event    No         event-level   Yes            partial or        symbolic event
  EventGPT ScoutGPT 2025-2026]]      sequence                 spatial                      relative          stream, not
                                     prediction               context                                        full tracking
                                                                                                             plus video

  [[04_literature/sources/SOURCE -   tactical      No         Yes           not the same   No equivalent BAA large-scale
  TacticGen 2026]]                   trajectory                             BAA target     timing            trajectory
                                     generation                                                              generation,
                                                                                                             not
                                                                                                             public-data
                                                                                                             multimodal BAA

  [[04_literature/sources/SOURCE -   dataset       Yes        Yes           labels         timestamps        enables
  SoccerTrack v2 2025]]                                                     available      available         benchmark,
                                                                                                             does not
                                                                                                             itself solve
                                                                                                             anticipation
  -------------------------------------------------------------------------------------------------------------------------

Current literature logic

BAA exists → video-centered methods remain difficult → video plus game
state already helps current-action understanding → structured game state
predicts future football behavior in neighboring tasks → SoccerTrack v2
provides synchronized video, GSR, and BAS → the unresolved question is
whether explicit relation-aware game state improves temporally localized
future BAA.

Novelty discipline

Do not claim:

1.  First future football action prediction.
2.  First football GNN.
3.  First video plus game-state football model.
4.  First football tactical forecasting.

Potentially defensible after final verification:

“No exact prior work was identified in the current search that fuses
synchronized full-pitch player game state with visual features
specifically for temporally localized short-horizon Ball Action
Anticipation.”

2026-08-14 re-verification addendum

[[sources/SOURCE - Beyond Pixels 2025]] and newer FOOTPASS-related work
confirm that game-state-aware, relation-aware, and longer-context
football action understanding already has prior art in
detection/spotting. The remaining defensible bridge is explicit
game-state value for unobserved-future BAA. See
[[../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]].
