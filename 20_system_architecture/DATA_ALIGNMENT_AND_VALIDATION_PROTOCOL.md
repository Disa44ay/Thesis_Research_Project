---
type: validation-protocol
status: mandatory
created: 2026-08-14
updated: 2026-08-14
tags: [alignment, validation, bas, gsr, video]
related:
  - "[[CANONICAL_DATASET_REVISION_POLICY]]"
  - "[[END_TO_END_DATA_SYSTEM_ARCHITECTURE]]"
  - "[[../08_experiments/BENCHMARK_PROTOCOL_LOCK]]"
  - "[[../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]]"
---
# Data Alignment and Validation Protocol

## Event gate
A BAS event is usable only after:
1. schema is accepted by the pinned loader,
2. half/segment is known,
3. event time maps to an existing GSR time/frame,
4. corresponding video time exists,
5. no documented correction makes the required state unreliable.

Failed records are quarantined with reason codes, not silently deleted.

## Known special case
Match 132831 has a documented calibration correction issue in the repository. It remains quarantined until the specific pitch-space GSR fields required by this thesis are verified as corrected or scientifically safe. If unresolved, exclude the match and redesign grouped folds.

## Manual spot-check
Review approximately 100 randomly sampled aligned events across matches/classes where possible. Inspect event label/time, a short video segment, and GSR/minimap position. This is quality assurance, not new annotation.

## Required audit outputs
- alignment_report.json
- exclusions.json
- per-match event counts
- per-class event counts
- missing-state/frame statistics
- usable durations
- final fold manifest

Only after this protocol passes are exact benchmark counts and folds frozen.
