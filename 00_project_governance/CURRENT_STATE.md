Current State

Primary title

Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation
in Football

Core research question

Does explicit synchronized player-level game state improve temporally
localized short-horizon Ball Action Anticipation relative to visual-only
anticipation?

Secondary research question

If game state helps, does relation-aware player modeling add value
beyond flat state and flat relational features receiving the same
underlying information?

Evidence boundary

The reviewed literature establishes video-based football BAA and
separately establishes game-state-assisted football action
detection/spotting. The current claim is narrower: the project will test
whether explicit synchronized player state adds predictive value to
unseen-future BAA.

Dataset

SoccerTrack v2 is the primary feasibility dataset, but the exact
experimental revision has not yet been pinned. The canonical revision
must pass schema, correction, and cross-modal alignment validation
before final counts or folds are frozen.

Benchmark direction

-   future horizon: 5 seconds,
-   variable-size multi-event prediction,
-   action class + future temporal location + confidence,
-   up to 30 seconds of available history in the broader benchmark
    design,
-   shorter effective context permitted for the initial model/pilot,
-   match-level grouped evaluation where the final usable match count
    permits,
-   BAA-style temporal mAP,
-   exact class/fold policy frozen only after canonical data validation.

Planned model comparison

1.  visual-only,
2.  game-state-only,
3.  simple fusion,
4.  flat relational features,
5.  relation-aware fusion.

Proposal

The original long proposal is preserved, but the current
instructor-facing artifact is the concise verified proposal described in
[[../21_proposal/PROPOSAL_REVISION_2026-08-14]] and supported by
[[../21_proposal/CITATION_AND_SOURCE_AUDIT]].

Immediate next action

Extend the executed single-match feasibility pilot to all ten available
SoccerTrack v2 matches, and arrange the independent teammate replication
run described in [[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]],
before beginning B0-B5 baseline implementation.

Critical status (updated at Release 05)

The feasibility pilot has been executed on representative match 117093.
Decision: **GO, with strict scope control** (see
[[../22_feasibility/FEASIBILITY_STUDY_REPORT]], dated 2026-08-20). This
supersedes the Release 04 status of "not yet run." The GO decision
covers pipeline construction only - it is not a claim that game-state
fusion improves anticipation. That remains the open research question.
Single-match validation has not yet been extended to the full ten-match
set, and no model has been trained or evaluated. See
[[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]] for exactly what is
and is not yet confirmed.

------------------------------------------------------------------------

## Release 06 note (2026-09-22)

This file is kept exactly as it stood at Release 05 and is not rewritten
in place, per this project's migration convention. It is now superseded
as the project's current-status reference: the root-level
[[../CURRENT_STATE]] (added at Release 06) carries the up-to-date
status, including the Gate H and Gate E extension resolutions recorded
in [[../25_gate_validation/GATE_STATUS_SUMMARY]]. Read this file for
the Release 05 snapshot of project state; read the root `CURRENT_STATE.md`
for the current one.
