---
type: benchmark-protocol
status: framework-locked-data-gated
created: 2026-08-14
updated: 2026-08-14
tags: [benchmark, baa, soccertrack-v2, cross-validation]
related:
  - "[[BENCHMARK_DESIGN_DRAFT]]"
  - "[[../03_datasets/datasets/SoccerTrack v2]]"
  - "[[../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]]"
  - "[[../20_system_architecture/DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]"
---
# Benchmark Protocol Lock

## Task
Provide up to 30 seconds of historical context and predict all ball actions occurring in the next 5 seconds. Each predicted event has a class, future temporal location, and confidence.

The model is not required to consume the full 30 seconds. Effective model context is a modeling decision, with 5 seconds as the initial compute-safe configuration.

## Output type
Variable-size set prediction, not next-action classification.

## Primary class policy
Use the 10 SN-BAA-compatible semantic classes by excluding Goal and Free Kick for primary methodological comparability. Also report the full 12-class SoccerTrack result where feasible. Header remains a known rare-class stability concern and must not be silently removed after results are observed.

## Split policy
- Whole-match grouping only.
- Five-fold grouped evaluation is the preferred final design if the usable match count remains sufficient after the data-quality gate.
- Exact match pairings are not frozen until canonical release validation and the documented 132831 issue are resolved.

## Evaluation windows
- 5-second future horizon.
- Fixed-stride validation/test windows generated independently of future annotations.
- No cross-half windows.
- Empty-window treatment remains a benchmark design choice to be checked against the official evaluator during implementation.

## Metrics
Use FAANTRA/SoccerNet-style mAP at temporal tolerances delta in {1,2,3,4,5,infinity}. For finite delta, correctness corresponds to a prediction falling within delta/2 seconds of the ground-truth time. Report mAPavg, per-class AP, fold mean, and fold dispersion.

## Leakage rules
1. No future video or GSR in the input.
2. No match appears in more than one partition within a fold.
3. Training-only statistics determine normalization and class weights.
4. Player identity is allowed for trajectory association, not as a learned semantic identity feature in the default model.
5. Window generation cannot depend on the existence of a future event.

## Gate
Exact usable event counts and fold identities remain provisional until [[../20_system_architecture/DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]] passes.
