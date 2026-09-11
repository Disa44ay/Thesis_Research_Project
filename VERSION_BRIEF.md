---
type: version-brief
status: active
public_release: "Release 01"
historical_basis: "historical v1-v2 period, endpoint v2 (2026-08-10)"
updated: 2026-08-16
tags: [release, history, git, obsidian]
related:
  - "[[README]]"
  - "[[RELEASE_HISTORY]]"
  - "[[ARCHITECTURE]]"
---
# Version Brief — Release 01

## Release identity

**Project:** Thesis Research Project  
**Public release:** Release 01 — Foundation and Scope Formation  
**Historical basis:** historical v1-v2 period, endpoint v2 (2026-08-10)  
**Previous public release:** None

## Plain-language summary

The Thesis Project began as a broad computer-vision thesis search and was separated from the reusable research methodology on 2026-08-09. By the end of Release 01, football had become the active domain boundary, the old PCBAS direction was no longer accepted uncritically, and three newer candidate families were being investigated: game-state-aware action anticipation, tactical retrieval, and tactical state forecasting.

## Previous release summary

There is no previous public release. Historically, v1 preserved the original mixed-vault thesis state with PCBAS as the provisional leader. Historical v2 then converted that material into a graph-native thesis research space and is the endpoint of this release.

## What changed

1. Preserved the original PCBAS direction and candidate gaps A-D.
2. Locked football as the primary domain.
3. Recorded team capacity, annotation ceiling, dataset-access preferences, and zero-recurring-cost deployment as explicit constraints.
4. Changed multimodality from a requirement to a preference that must be justified.
5. Expanded candidate search toward Ball Action Anticipation, tactical retrieval, and tactical forecasting.
6. Downgraded generic PCBAS tactical-context novelty and rejected generic football RAG as insufficiently novel.
7. Added atomic decisions, constraints, source/dataset notes, and a graph-native knowledge map.

## Why it changed

The initial thesis direction was too dependent on unvalidated novelty assumptions. The team also needed a topic compatible with limited compute, public data, a short implementation window, and strong software-engineering value.

## What we were trying to learn

Which constraints actually control topic feasibility, and which apparently attractive directions become weak once existing literature and data access are considered.

## Current understanding

Football remained the best domain fit, but the exact thesis problem was still open. The project had moved from one provisional PCBAS idea into a structured candidate-comparison stage.

## Remaining uncertainty

No candidate had survived deep primary-source verification. Dataset access, exact benchmark design, and novelty boundaries were still unresolved.

## Next direction

Run adversarial literature search and dataset validation on the strongest football candidates, especially action anticipation using SoccerTrack/SoccerNet-related resources.

## Historical continuity

This release is a **complete repository snapshot**, not a patch. Earlier notes remain present when they still explain the research journey. The public release numbering groups the original v1-v5 history into meaningful Git milestones without erasing the original version lineage.

## Preservation notes

The earlier PCBAS gaps, rejected RAG direction, and all scope/constraint decisions remain because they explain why later BAA work was pursued.

For the original v1-v5 lineage, see the project's version-history and migration notes as well as [[RELEASE_HISTORY]].
