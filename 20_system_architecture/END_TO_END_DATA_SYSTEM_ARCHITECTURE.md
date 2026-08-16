---
type: system-architecture
status: planned
created: 2026-08-14
updated: 2026-08-14
tags: [architecture, data-pipeline, soccertrack-v2, reproducibility]
related:
  - "[[CANONICAL_DATASET_REVISION_POLICY]]"
  - "[[GSR_STREAMING_AND_COMPRESSION_PIPELINE]]"
  - "[[VISUAL_FEATURE_EXTRACTION_PIPELINE]]"
  - "[[DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]"
  - "[[../08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]"
---
# End-to-End Data and Research System Architecture

```mermaid
flowchart TD
    S[SoccerTrack v2 pinned release] --> M[Dataset manifest + hashes]
    M --> BAS[BAS events]
    M --> GSR[Large GSR JSON]
    M --> VID[4K panoramic video]
    BAS --> BV[BAS schema and time validator]
    GSR --> GS[Streaming parser + field selection + downsample]
    VID --> VS[FFmpeg sampling + frozen visual encoder]
    BV --> A[Cross-modal alignment validator]
    GS --> A
    VS --> A
    A --> W[Window manifest: past context -> next 5 s]
    W --> FS[Compact feature store]
    FS --> B1[Visual-only]
    FS --> B2[State-only]
    FS --> B3[Simple fusion]
    FS --> B4[Flat-relations]
    FS --> B5[Relation-aware fusion]
    B1 --> EV[Grouped evaluation]
    B2 --> EV
    B3 --> EV
    B4 --> EV
    B5 --> EV
    EV --> DEMO[Inference API / zero-cost demo]
```

## Core design rules
1. Raw 4K and giant JSON files are source material, not epoch-time training inputs.
2. Process one match/half at a time.
3. Save continuous compact arrays and a window index instead of duplicated clips.
4. Use CPU for schema validation, streaming, alignment, statistics, and window construction.
5. Use accelerator primarily for one-time visual feature extraction and lightweight model training.
6. Preserve every exclusion and correction in machine-readable audit files.
