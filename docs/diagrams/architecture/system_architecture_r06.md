---
type: diagram
status: active
purpose: "System architecture as of Release 06 — the pre-implementation state, before N1 execution."
created: 2026-09-22
related_document: "[[../../ARCHITECTURE]]"
---

# System Architecture — Release 06

Rendered image: `../images/thesis/thesis_system_architecture_r06.png`
(created 2026-09-22, Release 06, from this file's mermaid source).

```mermaid
flowchart TD
    A[SoccerTrack v2<br/>10 matches, RGB + GSR + BAS] --> B[Mini Feasibility Pilot<br/>single match, Release 05]
    B --> C[Pre-Implementation Gate Extension]
    C --> D[Gate H<br/>compute feasibility]
    C --> E[Gate E extension<br/>multi-match offset check]
    D --> F[common.py<br/>shared module, Google Drive]
    E --> F
    F --> G[N1: Acquire and Validate<br/>CPU-only]
    G --> H[N2: Visual Features<br/>GPU, ResNet-18]
    G --> I[N3: Game-State Features]
    H --> J[N4: Fusion and Baselines<br/>B0-B5 model matrix]
    I --> J
    J --> K[Evaluation]
    K --> L[Publication]

    style G fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style H fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style I fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style J fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style K fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style L fill:#eee,stroke:#999,stroke-dasharray: 5 5
```

## Reading this diagram

Solid boxes (A through F) are complete and documented in this release.
Dashed boxes (G through L) represent the pipeline as designed and
decided, not yet executed within this release's scope — N1 has, per
project memory, actually run, but its results are deliberately excluded
from Release 06 and belong to a future release.
