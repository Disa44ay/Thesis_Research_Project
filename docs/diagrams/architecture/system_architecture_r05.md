---
purpose: Executed multimodal pipeline architecture at Release 05
created: 2026-09-10
version: Release 05
related: "[[../../../ARCHITECTURE]]"
---

# System Architecture — Release 05 (executed portion highlighted)

```mermaid
flowchart TD
    D[SoccerTrack v2 Google Drive release] --> BAS[BAS actions - validated]
    D --> GSR[GSR player state - validated]
    D --> RGB[Panoramic RGB video - validated]

    BAS --> ALIGN[Timestamp-based BAS to GSR mapping - VERIFIED]
    GSR --> ALIGN
    RGB --> SYNC[Timestamp-based RGB to GSR sync - VERIFIED, 1.000s offset resolved]
    GSR --> SYNC

    ALIGN --> WIN[30s to 5s window benchmark - 1,092 windows executed on match 117093]
    SYNC --> FEAT[Frozen ResNet-18 visual features, 150x512 - executed]

    WIN --> STORE[Compact structured + visual feature store]
    FEAT --> STORE

    STORE --> MODELS[B0 through B5 model matrix - NOT YET RUN]
    MODELS --> EVAL[Grouped match-level evaluation - NOT YET RUN]
```

Everything above the "NOT YET RUN" boundary has been executed and
verified on one representative match. Nothing below it has started.
