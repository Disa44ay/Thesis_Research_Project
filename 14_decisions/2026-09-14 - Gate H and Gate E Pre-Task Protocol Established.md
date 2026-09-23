---
type: decision
status: decided
date: 2026-09-14
related:
  - "[[../25_gate_validation/GATE_H_COMPUTE_FEASIBILITY_RESULTS]]"
  - "[[../25_gate_validation/GATE_E_MULTI_MATCH_OFFSET_RESULTS]]"
  - "[[2026-09-14 - Four Notebook Pipeline Split]]"
---

# Decision: Gate H and Gate E Pre-Task Protocol Established

## Decision

Before starting the mandatory B0-B5 model matrix, run two explicit
pre-tasks: Gate H (measure real compute feasibility of the
acquisition/validation stage) and a Gate E extension (test the
Release-05 single-match RGB/GSR offset finding against the full
ten-match dataset). Document the protocol for both
(`claude/PROTOCOL_gate_h_and_multi_match_offset.md`) before running
either.

## Reasoning

The Release 05 feasibility pilot answered "can this work at all" on one
instance. It did not answer "what will this cost at full scale" or
"does this hold for every instance we will actually use." Starting the
model matrix without answering both questions risks discovering a
compute-budget problem or an alignment problem only after most of the
work is already committed.

## Alternatives considered

- **Skip straight to implementation and handle problems as they arise.**
  Rejected: the project's own quality-gate philosophy (carried from
  Release 04/05) treats this as the same mistake as skipping the
  feasibility pilot itself — deferring a knowable risk instead of
  measuring it.
- **Run only Gate H, assume the single-match offset generalizes.**
  Rejected: this is exactly the assumption
  [[../../Reusable_Research_OS/13_gate_extension_validation/MULTI_INSTANCE_GENERALIZATION_CHECK]]
  argues against.

## Consequences

- Division of labor: Task A (Gate H, via
  `claude/gate_h_compute_feasibility_probe.py`) and Task B (Gate E
  extension, via `claude/gate_e_multi_match_offset_check.py`) can run in
  parallel.
- Both results must be cross-checked against each other and against the
  Release 05 pilot's numbers before the model matrix starts.
- Neither script's result is treated as conclusive on its own for
  anything the protocol document explicitly says it cannot measure.
