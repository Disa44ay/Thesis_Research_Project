---
type: decision
status: decided
date: 2026-09-14
related:
  - "[[../26_implementation_architecture/FOUR_NOTEBOOK_PIPELINE_DECISION]]"
  - "[[../26_implementation_architecture/COMMON_PY_ARCHITECTURE]]"
---

# Decision: Four-Notebook Pipeline Split

## Decision

Implement the pipeline as four separate Colab notebooks (N1 Acquire &
Validate, N2 Visual Features, N3 Game-State Features, N4 Fusion &
Baselines), sharing one standalone `common.py` module on Google Drive.

## Reasoning

Colab GPU sessions are a limited, session-scoped resource. Splitting
the CPU-only acquisition/validation stage from the GPU-bound
feature-extraction and training stages means GPU quota is only spent
where it is needed, and CPU-only work can be checkpointed and re-run
independently of GPU availability.

## Alternatives considered

- **Single monolithic notebook.** Rejected — see
  [[../26_implementation_architecture/FOUR_NOTEBOOK_PIPELINE_DECISION]]
  for the full comparison.
- **Per-model notebooks (one per B0-B5).** Rejected at this stage —
  duplicates shared feature-extraction work across models.

## Consequences

- `common.py` becomes the single point of change for shared logic; see
  [[../26_implementation_architecture/COMMON_PY_ARCHITECTURE]].
- N1 must complete and checkpoint before any GPU-session notebook (N2)
  starts, per the project's existing Colab-workflow convention.
