---
type: version-brief
status: active
public_release: "Release 03"
historical_basis: "historical v4 (2026-08-14)"
updated: 2026-08-16
tags: [release, history, git, obsidian]
related:
  - "[[README]]"
  - "[[RELEASE_HISTORY]]"
  - "[[ARCHITECTURE]]"
---
# Version Brief — Release 03

## Release identity

**Project:** Thesis Research Project  
**Public release:** Release 03 — Scientific Lock and Re-verification  
**Historical basis:** historical v4 (2026-08-14)  
**Previous public release:** Release 02

## Plain-language summary

Release 03 is the scientific-lock stage. The project survived a final adversarial review, but several claims were narrowed or withdrawn. The thesis became centered on one defensible empirical question: whether explicit player game state adds predictive value to short-horizon Ball Action Anticipation, not whether graph reasoning or video-plus-state fusion is novel by itself.

## Previous release summary

Release 02 made Candidate 01B the leading direction using direct dataset evidence and multi-agent literature review, but several assumptions remained provisional.

## What changed

1. Added PR-005, a focused Claude evidence-lock review.
2. Re-verified FAANTRA, SoccerNet 2026 BAA, Ochin, SoccerTrack v2 and additional prior art from primary sources.
3. Added Beyond Pixels as a novelty threat and downgraded relation/GNN method novelty.
4. Locked the core research gap around explicit game-state value for unseen-future BAA.
5. Corrected the interpretation of the 30-second observation context and BAA temporal mAP tolerances.
6. Withdrew the provisional 21,438 'clean events' estimate.
7. Withdrew exact fold pairings until canonical release and alignment validation.
8. Documented canonical-source/schema differences, second-half alignment caveats, and the match 132831 correction issue.
9. Defined the controlled B0-B5 experiment matrix, including a flat-relations control.

## Why it changed

The candidate had to survive the strongest prior work rather than rely on optimistic novelty language. Re-verification also showed that the Drive BAS snapshot and current documented release should not be silently treated as identical.

## What we were trying to learn

The research question remains useful even if the GNN adds no gain, because the study can separately test information value, relational features, and message passing. Dataset provenance is part of the scientific method, not merely preprocessing.

## Current understanding

The topic is defensible with narrow claims. The benchmark framework is scientifically usable, but exact event counts and match folds remain gated on a pinned canonical SoccerTrack revision.

## Remaining uncertainty

No feasibility run or model experiment had yet been executed. Exact data revision, final folds, visual backbone, sample rates, and compute consumption remained unresolved.

## Next direction

Translate the scientific lock into a resource-budgeted system architecture and run a small end-to-end feasibility pilot before full experiments.

## Historical continuity

This release is a **complete repository snapshot**, not a patch. Earlier notes remain present when they still explain the research journey. The public release numbering groups the original v1-v5 history into meaningful Git milestones without erasing the original version lineage.

## Preservation notes

Earlier candidate names and provisional benchmark notes remain linked as historical states. Withdrawn estimates and corrections are explicitly retained rather than erased.

For the original v1-v5 lineage, see the project's version-history and migration notes as well as [[RELEASE_HISTORY]].
