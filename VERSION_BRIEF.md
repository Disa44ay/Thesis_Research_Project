---
type: version-brief
status: active
public_release: "Release 02"
historical_basis: "historical v3 (2026-08-12)"
updated: 2026-08-16
tags: [release, history, git, obsidian]
related:
  - "[[README]]"
  - "[[RELEASE_HISTORY]]"
  - "[[ARCHITECTURE]]"
---
# Version Brief — Release 02

## Release identity

**Project:** Thesis Research Project  
**Public release:** Release 02 — Evidence-Driven Candidate Validation  
**Historical basis:** historical v3 (2026-08-12)  
**Previous public release:** Release 01

## Plain-language summary

Release 02 captures the evidence-driven narrowing of the thesis. Multiple AI assistants were used as scoped researchers, their outputs were corrected against primary sources, the SoccerTrack v2 BAS snapshot was directly inspected, and Candidate 01B emerged as the strongest direction: short-horizon Ball Action Anticipation using visual and explicit game-state information.

## Previous release summary

Release 01 established football as the active domain, preserved the old PCBAS path, and defined the candidate search and feasibility constraints.

## What changed

1. Recorded PR-001 through PR-004 with assistant roles, outputs, errors, and corrections.
2. Expanded the verified related-work set around FAANTRA, SoccerNet BAA, Ochin, TacticAI, GenTac, Seq2Event, EventGPT/ScoutGPT, TacticGen and SoccerRAG.
3. Directly audited the user-provided SoccerTrack BAS snapshot and recorded 23,663 events for that snapshot, including strong class imbalance and timestamp anomalies.
4. Established SoccerTrack v2 as the primary feasibility dataset.
5. Rejected repeated end-to-end 4K training in favor of one-time visual feature extraction and compact GSR processing.
6. Drafted a derived BAA benchmark and controlled visual/state/fusion baselines.
7. Narrowed Candidate 01 toward relation-aware multimodal BAA while retaining alternatives 02 and 03 as downgraded candidates.

## Why it changed

Broad discovery showed that generic football retrieval and generic tactical forecasting already had strong prior art. Direct data inspection showed that SoccerTrack v2 could support a future-action task without large manual labeling, while compute analysis showed the raw data had to be transformed once into compact representations.

## What we were trying to learn

The promising gap was not 'future football prediction' or 'video plus game state' in general. It was the more specific question of whether explicit synchronized game state helps prediction of unseen future ball actions.

## Current understanding

Candidate 01B was the leading topic, but its novelty was still provisional and benchmark counts/folds had not yet passed a final adversarial verification.

## Remaining uncertainty

Exact method novelty, canonical release alignment, rare-class handling, and final split policy still needed verification.

## Next direction

Run a final hostile review of the candidate and lock the benchmark only after re-checking the primary papers and SoccerTrack release details.

## Historical continuity

This release is a **complete repository snapshot**, not a patch. Earlier notes remain present when they still explain the research journey. The public release numbering groups the original v1-v5 history into meaningful Git milestones without erasing the original version lineage.

## Preservation notes

The AI research-run corrections, direct BAS statistics, rejected candidates, and compute decisions remain part of the research record even where later releases refine them.

For the original v1-v5 lineage, see the project's version-history and migration notes as well as [[RELEASE_HISTORY]].
