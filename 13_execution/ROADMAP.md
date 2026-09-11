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
