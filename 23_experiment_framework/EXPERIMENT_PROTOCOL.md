---
type: experiment-protocol
status: ready-pending-ten-match-extension
related:
  - "[[../08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]"
  - "[[../22_feasibility/FEASIBILITY_STUDY_REPORT]]"
---

# Experiment Protocol (Release 05)

This is the execution-ready version of the comparison design implied by
the feasibility study (see
[[../22_feasibility/FEASIBILITY_STUDY_REPORT]] section 6), combined
with the locked B0-B5 model matrix from Release 03/04
([[../08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]).

## Minimum required comparisons

1. B1 visual-only vs. B0 statistical floor - sanity check that a
   temporal encoder beats a prior-only baseline.
2. B3 simple fusion vs. B1 visual-only - tests RQ1 (does explicit game
   state help at all).
3. B4 flat-relations vs. B3 simple fusion - isolates the value of
   explicit pairwise relation features.
4. B5 relation-aware fusion vs. B4 flat-relations - tests RQ2 (does
   relation-aware message passing add value beyond equivalent flat
   information).
5. B2 game-state-only, reported alongside but not required for the
   headline comparisons - characterizes how much signal exists without
   any visual input at all.

## Data protocol (locked from the feasibility study)

- Benchmark unit: 30s observation, 5s anticipation, 5s stride windows,
  constructed per [[../22_feasibility/BAA_BENCHMARK_CONSTRUCTION]].
- **Splits must be at the match level, never at the window level.**
  Overlapping windows share substantial temporal content; a window-level
  split would leak near-duplicate observations across train/val/test.
- Visual and structured branches must use identical preprocessing and
  identical observation windows across all compared models - no model
  gets a different visual backbone or sampling rate than another in the
  same comparison.
- RGB-GSR alignment must use the timestamp-based rule from
  [[../22_feasibility/BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]], applied
  identically to every match.

## Preconditions before this protocol may run at full scale

1. Independent teammate replication of the match-117093 pipeline
   (open - see [[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]]).
2. Extension of dataset inventory/benchmark construction to all ten
   matches (open).
3. Canonical dataset revision pinned (open).
4. Rare-class / loss-weighting policy locked (open).

## Interpretation rules (carried forward from the negative-result
contract)

- B5 <= B1 is a valid, reportable negative result about transfer from
  detection-style relational modeling to anticipation - not a failed
  experiment.
- Published visual BAA results from other datasets/domains are
  methodological references only, never directly comparable scores.
  The visual baseline (B1) must be retrained on this project's own
  SoccerTrack-derived benchmark.

------------------------------------------------------------------------
