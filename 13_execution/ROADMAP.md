---
type: roadmap
status: active
updated: 2026-09-10
---

# Roadmap (as of Release 05)

## Done

- Football scope locked, candidate narrowed to explicit game-state
  fusion for short-horizon BAA (Releases 01-03).
- Safest primary title locked; raw-data-to-feature architecture,
  compute budget, and stop rules defined (Release 04).
- Feasibility pilot executed on representative match 117093: GO
  decision with strict scope control (Release 05).
- RGB/GSR one-second presentation-offset defect found and resolved via
  timestamp-based alignment (Release 05).
- First real 1,092-window BAA benchmark constructed for one match
  (Release 05).

## Not yet done (immediate)

- Independent teammate replication of the match-117093 pipeline run.
- Extension of the validated pipeline to the remaining matches
  (117092, 118575, 118576, 118577, 118578, 128057, 128058, 132877 -
  **8 matches**, not 9: 132831 is excluded/quarantined pending a
  corrected GSR revision, see
  [[../22_feasibility/MATCH_132831_CALIBRATION_DEFECT]]).
- Canonical dataset revision pinning.
- Rare-class / loss-weighting policy lock.
- Final visual backbone, resolution, and sampling-rate decisions.

## Not yet done (implementation phase)

- Implement B0 (statistical floor) through B5 (relation-aware fusion)
  per [[../08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]].
- Match-level train/validation/test split design across the full
  ten-match set.
- Run the ablation set: relation-aware vs flat-relations, no
  game-state, no visual input, remove velocity, remove team relation.
- Evaluate with BAA-style temporal mAP under grouped cross-validation
  where the final usable match count permits.

## Not yet done (writing and defense)

- Thesis writing beyond the concise verified proposal.
- Publication positioning beyond the Release 05 draft in
  [[../24_publication_positioning/RESEARCH_POSITIONING]].
- Defense preparation (status unchanged from Release 04 - see
  [[../12_defense/DEFENSE_STATUS]]).

## Explicit non-claims

No model has been trained. No fusion-performance result exists. The GO
decision covers pipeline buildability only.

------------------------------------------------------------------------

# Roadmap — Release 06 Addition

## Just closed (in scope for this release)

- Gate H (compute feasibility) — resolved 2026-09-15.
- Gate E extension (multi-match offset generalization) — resolved
  2026-09-16/17.
- Four-notebook pipeline architecture (N1-N4 + shared `common.py`) —
  decided 2026-09-14.
- Quarantine mechanism design (general pattern) — decided pre-N1.

## Next (explicitly out of scope for Release 06)

- N1 (Acquire & Validate) execution — per project memory, this notebook
  has already run (completed 2026-09-22), but its results are withheld
  from this release by deliberate scope decision, not because they are
  unknown.
- N2 (Visual Features, GPU session).
- N3 (Game-State Features).
- N4 (Fusion & Baselines) — the B0-B5 model matrix.
- N5 — reserved, not yet scoped in detail.
- Closing the tracking-sync gap recorded in
  `25_gate_validation/GATE_STATUS_SUMMARY.md` by pushing Gate H/Gate E
  documentation to the git remote so the automated daily check picks it
  up.

## Note on sequencing

The next public release for this project will cover N1 through N5 as a
single unit, consistent with the user's explicit instruction that
"N1-N5 will be in a separate release."
