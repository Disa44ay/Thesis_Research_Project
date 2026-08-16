---
type: constraint
status: active
created: 2026-08-10
updated: 2026-08-10
tags: [constraint, deployment, zero-cost, storage]
related:
  - "[[14_decisions/2026-08-10 - Research Compute Expanded Deployment Still Free]]"
  - "[[09_implementation/IMPLEMENTATION_STATUS]]"
---
# Constraint: Zero Cost Deployment

## Hard rule
The final deployed thesis demonstration must not require recurring paid infrastructure.

Reject deployment designs that require paid hosting, paid inference, paid databases, paid object storage, or a permanently paid GPU server.

## Default video-storage strategy
Do not make permanent raw-video storage a requirement.

Preferred flow:
1. accept a short clip or local sample,
2. process it temporarily,
3. generate model predictions and structured outputs,
4. delete or avoid persisting the raw video,
5. persist only lightweight metadata when necessary, such as timestamps, actions, identities, coordinates, confidence values, embeddings, or experiment records.

Research dataset storage and research compute are separate from public deployment.
