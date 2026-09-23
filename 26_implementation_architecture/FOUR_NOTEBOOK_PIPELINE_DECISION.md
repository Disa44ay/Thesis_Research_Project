---
type: architecture-decision
status: decided
decided: 2026-09-14
related:
  - "[[COMMON_PY_ARCHITECTURE]]"
  - "[[../14_decisions/2026-09-14 - Four Notebook Pipeline Split]]"
---

# Four-Notebook Pipeline Decision

## Decision

The implementation is split into four Colab notebooks, each with a
single responsibility, sharing one standalone module:

1. **N1 — Acquire & Validate.** Pull the dataset, run alignment and
   quarantine checks, build the window index. CPU-only (per Gate H).
2. **N2 — Visual Features.** GPU session. Extract per-frame visual
   features (ResNet-18) from the validated windows.
3. **N3 — Game-State Features.** Build the game-state-only feature
   representation from GSR data.
4. **N4 — Fusion & Baselines.** Combine visual and game-state features,
   train and evaluate the B0-B5 model matrix.

All four notebooks import a single shared module, `common.py`, kept on
Google Drive at `MyDrive/Thesis_Project/code/common.py`, rather than
duplicating logic across notebooks.

## Why this split

- Colab sessions are not persistent and GPU quota is limited; separating
  the CPU-only acquisition/validation stage (N1) from the GPU-bound
  feature-extraction and training stages (N2-N4) means the expensive
  GPU quota is only spent on stages that actually need it — a decision
  Gate H's measured result (GPU at ~0.34% utilization for the
  acquisition stage) directly supports.
- A single shared `common.py` avoids the failure mode where a bug fix
  (such as the tensorization fix found during Gate H) has to be
  re-applied in multiple copy-pasted notebook cells.
- Checkpointing CPU work before starting a GPU session (an existing
  project convention, see `ways-of-working.md`) is only practical if the
  CPU-only stage is cleanly separated into its own notebook.

## Alternatives considered

- **A single monolithic notebook.** Rejected: mixes CPU-only and
  GPU-bound work in one session, wasting GPU quota on stages that do not
  need it, and makes checkpointing before a GPU session harder.
- **One notebook per model (B0-B5).** Rejected at this stage: the
  feature-extraction stages (N2, N3) are shared across all six models
  in the matrix; duplicating them per model would multiply GPU cost for
  no benefit.

## Consequences

- Any change to shared logic (alignment, quarantine rules, dataset
  paths) is made once, in `common.py`, and picked up by all four
  notebooks on next import.
- N1 must fully complete and checkpoint its output before N2 starts a
  GPU session, per the existing project convention.

## Scope note

This file records the pipeline-split decision itself, made 2026-09-14,
before N1 was executed. It does not include N1's actual run results.
