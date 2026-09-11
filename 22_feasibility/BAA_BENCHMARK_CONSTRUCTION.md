---
type: benchmark-record
status: executed-single-match
match: "117093"
related:
  - "[[FEASIBILITY_STUDY_REPORT]]"
  - "[[../08_experiments/BENCHMARK_PROTOCOL_LOCK]]"
---

# BAA Benchmark Construction — Match 117093 (Executed)

## Windowing protocol (as executed)

- Observation window: 30 seconds
- Anticipation horizon: 5 seconds
- Stride: 5 seconds
- Windows only generated when the full observation and future interval
  remain inside the same half (no cross-period windows)

## Result

| Metric | Value |
|---|---|
| Total valid reference times (windows) | 1,092 |
| First half | 535 |
| Second half | 557 |
| Negative windows (0 future actions) | 233 (21.34%) |
| Single-action windows | 144 (13.19%) |
| Multi-action windows (2+) | 715 (65.48%) |
| Total compatible target assignments | 2,197 |
| Duplicate target assignments | 0 |
| Eligible actions not covered | 33 (all too early in a half for full 30s context) |
| Native GSR frames per observation | 750 |

A provisional 10-class compatibility view excluding FREE KICK and GOAL
was also generated for analysis. **This is not a locked thesis class
policy** — it exists to support early analysis only.

## What this confirms

- The task is genuinely multi-label and cannot be reduced to
  single-positive-action classification; nearly two-thirds of windows
  have 2+ future actions.
- A meaningful fraction (~21%) of windows are true negatives (no action
  in the next 5 seconds) and must be retained, not filtered out, or the
  benchmark would misrepresent real match dynamics.
- No target duplication occurred across the 2,197 assignments — each
  BAA-compatible action is attached to exactly one reference window.

## What this does not yet confirm

- Whether these proportions (21% negative / 13% single / 65% multi) hold
  across the other nine matches. Class balance and window-density
  patterns may vary by match, tempo, or scoreline.
- Final class policy (12-class raw vs. 10-class compatibility view vs.
  some other grouping).
- Fold/split design beyond "must be match-level, never window-level"
  (window-level splits would leak near-duplicate overlapping
  observations across train/val/test).

## Next step

Repeat this exact windowing protocol identically on the eight other
currently-usable matches (117092, 118575, 118576, 118577, 118578,
128057, 128058, 132877), record the same six summary statistics per
match, and check whether the negative/single/multi-action proportions
are stable enough to support a single global class-weighting policy or
require a per-match-aware strategy. **Match 132831 is excluded from
this step** pending a corrected GSR revision (see
[[BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]] for the unrelated timestamp
issue and [[FEASIBILITY_REPLICATION_STATUS]] /
`MATCH_132831_CALIBRATION_DEFECT.md` for this match's specific
calibration defect).

------------------------------------------------------------------------
