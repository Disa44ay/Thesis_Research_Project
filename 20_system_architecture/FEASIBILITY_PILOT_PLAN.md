---
type: feasibility-plan
status: next-action
created: 2026-08-14
updated: 2026-08-14
tags: [pilot, colab, proof-of-feasibility]
related:
  - "[[COMPUTE_BUDGET_AND_STOP_RULES]]"
  - "[[DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]"
  - "[[../21_proposal/PROPOSAL_ARTIFACT_INDEX]]"
---
# Mini Feasibility Pilot Plan

## Purpose
Prove the complete raw-data-to-prediction pipeline on a small slice before consuming the paid accelerator budget. This is a feasibility proof, not a scientific result.

## Suggested slice
Use approximately the first 10 minutes of a relatively clean match/half, preferably match 117093 after confirming the pinned canonical revision. Avoid 132831 during the pilot.

## Structured-data proof
- stream 10 minutes of GSR
- sample to 5 Hz starting configuration
- build fixed/padded player tensors and masks
- derive velocities
- save `pilot_state.npz`

## Video proof
- sample matching video at about 6.25 fps
- extract frozen visual features
- save `pilot_visual.npy`

## Label/window proof
- validate BAS alignment
- create context -> next 5-second windows
- save compact event/window tables

## Tiny training proof
Train a simple flat-state + visual fusion model long enough to verify:
- finite/decreasing loss
- checkpoint save/load
- action-class output
- timestamp output
- evaluation code execution

Accuracy is not a decision criterion at this stage.

## Required pilot artifacts
- pilot_manifest.json
- pilot_state.npz
- pilot_visual.npy
- pilot_events.parquet
- pilot_windows.parquet
- model_checkpoint.pt
- training_log.csv
- resource_usage.json
- sample_predictions.json

## Go/no-go criteria
Proceed to paid full-scale work only if download, streaming, alignment, feature extraction, compact storage, training, and prediction all pass and measured resource use projects within the budget.
