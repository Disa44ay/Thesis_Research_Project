---
type: verification-audit
status: completed
created: 2026-08-14
updated: 2026-08-14
tags: [verification, corrections, evidence-audit, phase-gate]
related:
  - "[[PHASE_1_RELATED_WORK_LOCK]]"
  - "[[PHASE_3_NOVELTY_LOCK]]"
  - "[[../08_experiments/BENCHMARK_PROTOCOL_LOCK]]"
  - "[[../08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]"
  - "[[../03_datasets/analysis/SoccerTrack v2 BAS Statistical Audit]]"
---
# Full Evidence Reverification - 2026-08-14

This audit was performed before Phase 4 to re-check every conclusion that materially affects the title, research gap, dataset, benchmark, novelty, and feasibility.

## Verified and retained
1. Football Ball Action Anticipation is an established task.
2. The 2026 challenge uses 30 seconds of observation and a 5-second future window.
3. BAA is multi-event set prediction with class and temporal localization.
4. The five reviewed 2026 BAA technical reports do not document synchronized metric GSR/player-coordinate/player-graph inputs.
5. Video plus explicit game-state football action understanding already exists for detection/spotting.
6. Ochin et al. is detection, not anticipation.
7. SoccerTrack v2 is public and provides 10 full panoramic matches, GSR, and 12-class BAS.
8. Match-level evaluation and frozen visual features remain appropriate.

## Corrections
1. **30-second context:** official benchmark history is 30 seconds, but the model need not consume all 30 seconds. The original FAANTRA work often uses shorter effective context.
2. **mAP temporal tolerance:** finite mAP@delta uses a +/- delta/2 temporal window, not +/- delta.
3. **Method novelty:** relation-aware football modeling is not novel by itself. Beyond Pixels and FOOTPASS further weaken that claim.
4. **Primary novelty:** remains the empirical question of explicit game-state value for future BAA.
5. **Drive BAS snapshot:** the uploaded Drive-mirror schema differs from current documented/canonical release conventions.
6. **23,663 events:** verified only for the uploaded Drive snapshot, not certified as the canonical current revision.
7. **21,438 clean events:** withdrawn. It was a quarantine estimate that incorrectly treated unresolved timestamp records as invalid.
8. **Exact folds:** withdrawn until canonical release validation and match-level correction issues are resolved.
9. **5 Hz GSR:** implementation starting hypothesis, not an established optimum.
10. **100 Colab units:** likely feasible under feature pre-extraction and lightweight training, but not guaranteed.

## Data-quality risks
- The Drive snapshot contains 2,129 clock-only BAS records in three matches and 96 additional unusual prefixed records. These require alignment checks rather than automatic deletion.
- The current repository documents schema/timestamp caveats and recommends using the project loader for robust BAS-to-GSR timing.
- Match 132831 has a documented calibration correction issue. It is quarantined until the intended pitch-space inputs are confirmed or corrected.

## Final decision
Candidate 01 remains **GO**. Benchmark framework is **GO**, but exact counts/folds are data-gated. Method novelty is **moderate**, while the research-question novelty remains the strongest contribution.
