---
type: decision
status: decided
date: 2026-09-15
related:
  - "[[../25_gate_validation/GATE_H_COMPUTE_FEASIBILITY_RESULTS]]"
---

# Decision: Gate H Resolved — CPU-Only Feasible

## Decision

Treat the acquisition/validation stage (N1) as CPU-only for planning
purposes. Do not reserve GPU session time for it.

## Reasoning

`claude/gate_h_compute_feasibility_probe.py` measured approximately 5.8
minutes of wall-clock time per match, approximately 0.73 compute units
per match, and GPU utilization at approximately 0.34% of runtime — the
accelerator was idle for nearly the entire measured run. The original
assumption that this stage would be meaningfully GPU-bound was wrong.

## Alternatives considered

- **Run N1 in the same GPU session as N2.** Rejected: the measured
  result shows this would waste GPU quota on a stage that does not use
  it, directly informing the four-notebook split decision.

## Consequences

- N1 is planned and checkpointed as a CPU-only notebook.
- A per-window tensorization bug found during this measurement was
  fixed (switched to a single streaming pass per half) — a concrete
  example of why the measurement, not the plan, was the deciding
  evidence.
- This result is generalized into
  [[../../Reusable_Research_OS/13_gate_extension_validation/COMPUTE_FEASIBILITY_MEASUREMENT_PRINCIPLE]].
