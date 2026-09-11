---
type: known-defect
status: confirmed-sourced
affected_match: "132831"
source: "https://github.com/AtomScott/SoccerTrack-v2/tree/main/data_corrections"
related:
  - "[[FEASIBILITY_REPLICATION_STATUS]]"
  - "[[../03_datasets/DATASET_DOCUMENTATION]]"
  - "[[../21_proposal/CITATION_AND_SOURCE_AUDIT]]"
---

# Match 132831 — Confirmed Calibration Defect

## What is wrong

Two calibration keypoints for match 132831 were swapped in the
upstream SoccerTrack v2 repository. This is documented by the dataset
maintainers themselves at
`github.com/AtomScott/SoccerTrack-v2/tree/main/data_corrections`, not
discovered independently by this project.

## Measured severity

- Shipped (faulty) calibration: RMS error approximately **1260.95px**.
- Corrected calibration: RMS error approximately **18.07px**.

A ~70x error reduction between faulty and corrected calibration
confirms this is not a minor rounding issue — the faulty calibration is
effectively unusable for any pitch-coordinate-dependent task.

## Downstream consequence

Match 132831's GSR (Game State Reconstruction) labels were generated
**using the faulty calibration**. As of the correction note, the
distributed dataset copy this project has access to **has not yet had
its GSR regenerated** from the corrected calibration.

Since GSR pitch coordinates for this match were derived from a
calibration with ~70x the intended error, any BAS-to-GSR spatial
mapping, player-position tensor, or RGB-GSR alignment work for match
132831 specifically would inherit that error. Bounding-box/pixel-space
GSR fields may be less affected than pitch-coordinate fields, but this
project has not separately verified that distinction and should not
assume it without a specific check.

## Standing decision (carried through Release 03/04/05)

**Exclude/quarantine match 132831 from training, evaluation, and the
ten-match benchmark extension** until a corrected canonical GSR
revision is verified against the fixed calibration. This match is
correctly excluded from feasibility validation for this reason — it was
never a candidate for the representative-match pilot, and Release 04's
[[FEASIBILITY_REPLICATION_STATUS]] already noted this without detail;
this note supplies the detail that was previously only referenced.

## What would resolve this

Confirmation (from the SoccerTrack v2 maintainers, or by independently
verifying the shared/distributed copy) that GSR has been regenerated
using the corrected calibration, ideally accompanied by a new RMS-error
measurement showing agreement with the ~18.07px corrected figure. Until
then, treat match 132831 as **9 of 10 usable matches for game-state
work**, not 10 of 10 — this has downstream implications for evaluation
variance planning (see [[../13_execution/ROADMAP]] and
[[../23_experiment_framework/EXPERIMENT_PROTOCOL]]).

------------------------------------------------------------------------
