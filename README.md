# Thesis Research Project — Release 06

## 1. Project Overview

Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation
in Football. The project studies whether synchronized player game-state
data (SoccerTrack v2 Game State Reconstruction) improves anticipation of
ball-related actions before they happen, compared to visual-only
models, under a common B0-B5 evaluation protocol.

Release 06: Pre-Implementation Gate Extension records the two
pre-tasks run between the Release 05 single-match feasibility pilot and
the start of the mandatory model matrix — measuring real compute cost
(Gate H) and testing the single-match alignment offset against the full
ten-match dataset (Gate E extension) — plus the four-notebook pipeline
architecture decision that followed from them.

Start with [[VERSION_BRIEF]] for the release history and
[[CURRENT_STATE]] for what is confirmed vs. still open.

## 2. What's new at Release 06

1. `25_gate_validation/` — Gate H and Gate E extension results, plus a
   combined status summary.
2. `26_implementation_architecture/` — the four-notebook pipeline
   decision, `common.py`'s architecture, and the general
   quarantine-mechanism design.
3. Four new decision records under `14_decisions/`.
4. Three new diagrams under `docs/diagrams/`.

## 3. Research Question

Whether an explicit description of match state (player positions,
velocities, team relations) improves short-horizon anticipation of
football actions, beyond what a visual-only model can infer, evaluated
via SoccerNet's Ball Action Anticipation formulation on SoccerTrack v2.

## 4. Architecture

```
Research Goal --> Dataset Selection (SoccerTrack v2) --> Mini Feasibility
Pilot (single match) --> Pre-Implementation Gate Extension (Gate H,
Gate E extension) --> Four-Notebook Pipeline (N1-N4) --> B0-B5 Model
Matrix --> Evaluation --> Publication
```

See [[ARCHITECTURE]] for the updated flow and
[[26_implementation_architecture/FOUR_NOTEBOOK_PIPELINE_DECISION]] for
the notebook split.

## 5. Project Structure

The established numbered folders are preserved. Key entry points for
this release:

1. `14_decisions/` — decision records, including four new Release 06
   entries.
2. `21_proposal/`, `22_feasibility/` — Release 05 proposal and
   feasibility content (unchanged).
3. `23_experiment_framework/`, `24_publication_positioning/` — unchanged.
4. `25_gate_validation/` — new at Release 06.
5. `26_implementation_architecture/` — new at Release 06.
6. `17_migration/`, `18_version_history/`, `16_session_history/` —
   provenance and chronological history.

See [[RELEASE_HISTORY]], `18_version_history/VERSION_HISTORY.md`, and
[[GRAPH_AUDIT]].

## 6. Scope boundary for this release

This release stops before the N1 (Acquire & Validate) notebook's own
execution. N1 has, per project memory, already run — but its results
are deliberately withheld from Release 06 and reserved for a future
release covering N1 through N5, per explicit project instruction.
