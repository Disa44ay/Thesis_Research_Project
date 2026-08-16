---
type: deployment-plan
status: planned-late-stage
created: 2026-08-14
updated: 2026-08-14
tags: [deployment, fastapi, zero-cost]
related:
  - "[[END_TO_END_DATA_SYSTEM_ARCHITECTURE]]"
  - "[[../01_goals_constraints/constraints/Zero Cost Deployment]]"
---
# Deployment Architecture

The deployment is a portfolio/system contribution, not the thesis novelty.

```mermaid
flowchart LR
    U[User selects short clip/sample] --> API[FastAPI]
    API --> PRE[Temporary preprocessing]
    PRE --> M[BAA inference model]
    M --> OUT[Action + future offset + confidence]
    OUT --> DB[Tiny structured store]
    OUT --> UI[Dashboard]
    PRE --> DEL[Delete temporary raw clip]
```

## Constraints
- zero recurring paid infrastructure
- short clips or precomputed demo samples
- raw uploads are temporary
- store structured predictions and experiment metadata, not large media
- model version recorded with each result
