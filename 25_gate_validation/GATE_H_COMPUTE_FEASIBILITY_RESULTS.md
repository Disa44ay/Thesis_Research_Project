---
type: gate-result
status: resolved
gate: "Gate H — Compute Feasibility"
resolved: 2026-09-15
related:
  - "[[../14_decisions/2026-09-14 - Gate H and Gate E Pre-Task Protocol Established]]"
  - "[[GATE_STATUS_SUMMARY]]"
  - "[[../../Reusable_Research_OS/13_gate_extension_validation/COMPUTE_FEASIBILITY_MEASUREMENT_PRINCIPLE]]"
---

# Gate H — Compute Feasibility Results

## Why this gate existed

Before committing the model matrix (B0-B5) to a fixed compute budget,
the project needed to know what the acquisition-and-validation stage
actually costs in wall-clock time, RAM, and GPU usage — measured, not
assumed. The working assumption going in was that this stage would be
meaningfully GPU-bound, since visual feature extraction downstream
would need a GPU session.

## Method

A dedicated probe script (`claude/gate_h_compute_feasibility_probe.py`)
ran a representative pass of the acquisition/validation stage and
recorded wall-clock time, RAM, and GPU utilization directly, rather
than estimating from stage descriptions.

## Result

- Average measured cost: approximately 5.8 minutes of wall-clock time
  per match.
- Normalized cost: approximately 0.73 compute units per match under the
  project's own unit definition.
- GPU utilization measured at approximately 0.34% of total runtime for
  this stage — the accelerator sat idle for nearly the entire run.

## What this changed

The stage is CPU-only feasible at near-zero compute cost. The original
assumption — that this stage would meaningfully consume GPU budget —
was wrong. Reserving paid accelerator time for this stage would have
been a waste; the compute budget for the project can be planned around
a CPU-only acquisition/validation pass.

## A defect found during measurement

While running the probe, a per-window tensorization bug was found: the
original implementation built tensors on a per-window basis, which was
both slower and less memory-efficient than necessary. It was fixed by
switching to a single streaming pass per half. This defect would not
have been found by reasoning about the pipeline in the abstract — it
only surfaced by running it and measuring.

## Status

Resolved 2026-09-15. This result is generalized, without
thesis-specific numbers, into the companion Reusable Research OS as
[[../../Reusable_Research_OS/13_gate_extension_validation/COMPUTE_FEASIBILITY_MEASUREMENT_PRINCIPLE]].

## Scope note

This file documents the Gate H measurement itself, which is
pre-implementation and in scope for Release 06. It does not include any
N1 notebook execution details, dataset inventory counts, or per-match
figures from the acquisition notebook's actual run — those belong to a
later release.
