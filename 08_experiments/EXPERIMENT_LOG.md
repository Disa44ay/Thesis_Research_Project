---
type: experiment-log
status: active
updated: 2026-09-10
---

# Experiment Log

This log records executed runs only. Planned-but-not-run work belongs in
[[../13_execution/ROADMAP]], not here.

## 2026-08-20 - Feasibility pipeline execution, match 117093

**What was run:** `SoccerTrack_v2_Feasibility_01.ipynb` (Colab), covering
dataset inventory, BAS/GSR schema validation, BAS-to-GSR temporal
mapping, 30s/5s benchmark construction, structured-tensor
materialization and leakage check, RGB video validation, RGB-GSR
synchronization test, and ResNet-18 visual-feature extraction probe.

**Environment:** Google Colab, CPU (visual feature extraction step
explicitly ran on CPU, not GPU).

**Inputs:** SoccerTrack v2 Google Drive release; match 117093 BAS file
(`117093_12_class_events.json`), two GSR halves, canonical first-half
panorama video (~3.35 GB, 4096x1080, 25 FPS).

**Outputs / measurements:**
- 2,252 BAS events, 41 unique players, 12 raw classes (severe
  imbalance: PASS 951, DRIVE 889, HIGH PASS 150 vs. HEADER 3, GOAL 5).
- 67,650 first-half / 70,475 second-half GSR frames at 25 FPS.
- 100% BAS-actor-to-GSR identity coverage (23/23, 27/27).
- 1,092 valid 30s/5s benchmark windows (535 / 557 by half); 233
  negative, 144 single-action, 715 multi-action; 2,197 target
  assignments, 0 duplicates.
- Leakage-free structured sample `117093_H1_0006` (750x22x2 position
  tensor, presence mask, role/team codes).
- RGB: 67,625 decoded frames vs. 67,650 GSR frames (25-frame gap);
  diagnosed as a 1.000s PTS offset, resolved via timestamp alignment
  (~1.07e-13s residual error after correction).
- Visual feature extraction: 150 synchronized RGB frames -> ResNet-18 ->
  finite (150, 512) feature matrix.

**Result:** GO, with strict scope control (see
[[../22_feasibility/FEASIBILITY_STUDY_REPORT]]).

**Not measured in this run:** wall-clock runtime, RAM/VRAM peak usage,
monetary cost, and any model accuracy/loss metric. These are explicitly
UNKNOWN / NOT PROVIDED IN SOURCE MATERIAL and should be captured in the
next execution pass alongside the ten-match extension.

**Discrepancies between teammate runs:** UNKNOWN / NOT PROVIDED IN
SOURCE MATERIAL - independent replication has not yet occurred (see
[[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]]).

## Planned next entries

- Independent teammate replication run on match 117093 (same protocol).
- Nine-match extension runs (one entry per match recommended, using the
  same six summary statistics as [[../22_feasibility/BAA_BENCHMARK_CONSTRUCTION]]).
- First B0/B1 baseline training run once the above are complete.

------------------------------------------------------------------------

# Experiment Log — Release 06 Addition

## Gate H — Compute Feasibility Probe

- **Date:** 2026-09-15
- **Script:** `claude/gate_h_compute_feasibility_probe.py`
- **What was measured:** wall-clock time, RAM, GPU utilization for a
  representative pass of the acquisition/validation stage.
- **Result:** ~5.8 min/match, ~0.73 compute units/match, GPU at ~0.34%
  utilization. See `25_gate_validation/GATE_H_COMPUTE_FEASIBILITY_RESULTS.md`.
- **Defect found during the run:** a per-window tensorization bug,
  fixed by switching to a single streaming pass per half.

## Gate E Extension — Multi-Match Offset Check

- **Date:** 2026-09-16/17
- **Script:** `claude/gate_e_multi_match_offset_check.py`
- **What was measured:** RGB/GSR presentation-timestamp offset via
  direct overlay, across all 10 matches / 20 halves.
- **Result:** 1-second offset confirmed in 14/20 halves, absent in
  6/20; new tail-loss defect (~10s missing video) found in 10/20
  halves; 1 half left unclassified. See
  `25_gate_validation/GATE_E_MULTI_MATCH_OFFSET_RESULTS.md`.

## Scope note

This is not a full experiment log entry for N1's dataset build or any
B0-B5 model run — those experiments have not been packaged into this
release. Only the two pre-implementation gate-validation scripts above
are in scope.
