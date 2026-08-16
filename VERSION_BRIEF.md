---
type: version-brief
status: active
public_release: "Release 04"
historical_basis: "historical v5 plus verified post-v5 work through 2026-08-16"
updated: 2026-08-16
tags: [release, history, git, obsidian]
related:
  - "[[README]]"
  - "[[RELEASE_HISTORY]]"
  - "[[ARCHITECTURE]]"
---
# Version Brief — Release 04

## Release identity

**Project:** Thesis Research Project  
**Public release:** Release 04 — Execution-Ready Proposal and Feasibility  
**Historical basis:** historical v5 plus verified post-v5 work through 2026-08-16  
**Previous public release:** Release 03

## Plain-language summary

Release 04 is the current execution-ready thesis snapshot. The research question, evidence boundary, system architecture, compute strategy, proposal, and feasibility study are documented well enough to begin the pilot. The key status remains important: the feasibility study is planned and independently reproducible, but it has not yet been executed, and no scientific model result exists yet.

## Previous release summary

Release 03 scientifically locked the question, narrowed the novelty claim, documented dataset hazards, and defined the controlled B0-B5 experiment matrix.

## What changed

1. Selected the safest primary title: Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football.
2. Added an end-to-end raw-data-to-feature-store architecture.
3. Added canonical dataset revision and cross-modal validation policies.
4. Added GSR streaming/downsampling and one-time frozen visual feature extraction plans.
5. Added compute budget, stop rules, and a 10-minute pilot before paid scaling.
6. Added zero-recurring-cost deployment architecture as an engineering objective.
7. Generated a detailed long-form proposal, then preserved it as superseded when it proved too disorganized for proposal use.
8. Generated a concise verified proposal and a separate citation/source audit.
9. Generated a three-page teammate brief.
10. Expanded the pilot into a self-contained AI/teammate context handoff and step-by-step feasibility guide.
11. Added independent teammate replication: the same pinned pilot should produce matching event counts, tensor shapes, windows, and validation outputs before the pipeline is considered structurally validated.
12. Added release-reconstruction metadata and a reproducible vault validator.

## Why it changed

The project had reached the point where scientific plausibility was no longer enough. The team needed proof that multi-gigabyte GSR JSON, panoramic video, alignment, compact features, model training, and Colab cost could be handled in practice. The proposal also needed to become shorter and easier for an instructor to evaluate without losing the detailed evidence trail.

## What we were trying to learn

A good thesis proposal should present the argument, not the entire laboratory notebook. Feasibility should be measured on a small complete pipeline, and replication should compare structural outputs before scientific results are trusted.

## Current understanding

The current goal is to determine whether explicit player-level game state helps predict future ball actions beyond visual evidence, then test whether relation-aware reasoning adds anything beyond equivalent flat relational features. The execution plan is compute-aware and data-quality-gated.

## Remaining uncertainty

The canonical experimental dataset revision is not pinned yet. The pilot has not run. Exact final event counts, folds, inclusion of match 132831, sample rates, backbone choice, compute cost, and model performance remain unknown.

## Next direction

Run the same match-117093 approximately 10-minute feasibility pilot independently, validate BAS/GSR/video alignment and compact feature generation, overfit a tiny batch, measure resources, compare teammate outputs, then issue a GO/MODIFY/NO-GO decision before full-scale experiments.

## Historical continuity

This release is a **complete repository snapshot**, not a patch. Earlier notes remain present when they still explain the research journey. The public release numbering groups the original v1-v5 history into meaningful Git milestones without erasing the original version lineage.

## Preservation notes

Release 04 keeps the old PCBAS history, candidate alternatives, PR-001 through PR-005, dataset anomalies, withdrawn counts/folds, the superseded long proposal, and all later corrections. Plans are not rewritten as completed experiments.

For the original v1-v5 lineage, see the project's version-history and migration notes as well as [[RELEASE_HISTORY]].
