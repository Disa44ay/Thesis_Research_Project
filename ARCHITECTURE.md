---
type: architecture
status: active
updated: 2026-09-22
note: "This file is a full rewrite for Release 06, describing the current architecture directly rather than as a diff against Release 05."
related:
  - "[[README]]"
  - "[[VERSION_BRIEF]]"
  - "[[26_implementation_architecture/FOUR_NOTEBOOK_PIPELINE_DECISION]]"
---

# Architecture — Release 06 Update

## Updated flow

```
Research Goal --> Dataset Selection (SoccerTrack v2) --> Mini Feasibility
Pilot (single match) --> Pre-Implementation Gate Extension
(Gate H compute measurement, Gate E multi-match offset check)
--> Four-Notebook Pipeline (N1 Acquire & Validate, N2 Visual Features,
N3 Game-State Features, N4 Fusion & Baselines) --> B0-B5 Model Matrix
--> Evaluation --> Publication
```

## The gate-extension stage, applied to this project

- **Gate H (compute feasibility):** measured ~5.8 min/match,
  ~0.73 compute units/match, GPU at ~0.34% utilization for the
  acquisition/validation stage. Result: CPU-only feasible. See
  `25_gate_validation/GATE_H_COMPUTE_FEASIBILITY_RESULTS.md`.
- **Gate E extension (multi-match offset):** the Release 05 single-match
  1-second offset held in 14/20 halves, was absent in 6/20; a new
  tail-loss defect was found in 10/20 halves; one half unresolved. See
  `25_gate_validation/GATE_E_MULTI_MATCH_OFFSET_RESULTS.md`.

## Pipeline architecture

Four Colab notebooks share a single `common.py` module on Google Drive:

- **N1 — Acquire & Validate** (CPU-only, per Gate H): dataset pull,
  alignment/quarantine checks, window index.
- **N2 — Visual Features** (GPU): ResNet-18 feature extraction.
- **N3 — Game-State Features**: GSR-derived feature representation.
- **N4 — Fusion & Baselines**: B0-B5 model training and evaluation.

See `26_implementation_architecture/FOUR_NOTEBOOK_PIPELINE_DECISION.md`
and `26_implementation_architecture/COMMON_PY_ARCHITECTURE.md` for the
full reasoning.

## Quarantine mechanism

`common.py` defines a general, reasoned exclusion mechanism for dataset
instances that fail alignment or other validation checks. See
`26_implementation_architecture/QUARANTINE_MECHANISM_DESIGN.md` for the
design; this release does not specify which instances are quarantined
under it, since those decisions are made as each notebook actually
runs.

## Unchanged

The proposal content (`21_proposal/`), the single-match feasibility
evidence (`22_feasibility/`), the experiment framework
(`23_experiment_framework/`), and the publication positioning
(`24_publication_positioning/`) are unchanged from Release 05.

## Scope boundary

This architecture update describes the pipeline as designed, before N1
executed. It does not describe N1's actual output.
