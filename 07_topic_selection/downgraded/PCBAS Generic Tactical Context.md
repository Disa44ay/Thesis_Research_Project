---
type: downgrade
status: downgraded
created: 2026-08-10
updated: 2026-08-10
tags: [downgraded, pcbas, tactical-context]
supported_by:
  - "[[04_literature/sources/SOURCE - FOOTPASS 2025]]"
  - "[[04_literature/sources/SOURCE - PCBAS Extensions 2026]]"
related:
  - "[[05_direction/PCBAS_STATE]]"
  - "[[06_research_gaps/Candidate Gap B - Tactical Priors]]"
---
# Downgraded: Generic Tactical Context for PCBAS

## Earlier hypothesis
Inject soccer tactical priors or player context into PCBAS because existing methods may use only flat player features.

## New evidence
FOOTPASS explicitly introduces player-centric action spotting in a tactical multi-agent context. A 2026 SoccerNet PCBAS system further uses GNN-based tactical context with per-player visual features and fuses contextualized logits into sequence modeling.

## Decision
Do not claim "tactical context for PCBAS" as a novel contribution.

PCBAS remains a possible domain only if a narrower, independently validated weakness survives, such as a specific robustness, identity, missing-detection, rare-class, or temporal-association problem.
