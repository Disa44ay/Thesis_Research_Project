---
type: publication-positioning
status: draft
related:
  - "[[../21_proposal/PROPOSAL_REVISION_2026-08-14]]"
  - "[[../22_feasibility/FEASIBILITY_STUDY_REPORT]]"
---

# Research Positioning (Release 05)

## What the project can now honestly claim

- A working, timestamp-correct multimodal (RGB + GSR) short-horizon BAA
  pipeline was constructed and validated end-to-end on one
  representative SoccerTrack v2 match.
- A concrete, reproducible engineering finding: presentation-timestamp
  alignment is required between the released panoramic video and GSR;
  naive frame-index alignment silently misaligns the modalities by a
  fixed offset. This is a methodological contribution independent of
  the eventual fusion result, and is a candidate for its own short
  write-up or appendix regardless of RQ1/RQ2's outcome.
- A concrete derived benchmark exists (1,092 windows on one match) with
  known class-imbalance and multi-label characteristics, useful for
  describing the task even before full results.

## What the project cannot yet claim

- That explicit game state improves anticipation (RQ1) - untested.
- That relation-aware modeling adds value beyond flat fusion (RQ2) -
  untested.
- That any finding generalizes beyond one match - the ten-match
  extension has not run.
- Any accuracy, mAP, loss, or other model-performance number.

## Framing guidance

Present the feasibility outcome as what it is: proof that the
comparison is executable, not a preview of the result. The RGB/GSR
synchronization finding can be framed as a standalone contribution
("a common but under-documented pitfall in multimodal sports datasets
that combine independently-encoded video and structured-tracking
releases") separate from the fusion hypothesis, since it would remain
true and useful regardless of whether fusion ultimately helps.

## Target venue / format

UNKNOWN / NOT PROVIDED IN SOURCE MATERIAL. Final publication venue was
already recorded as NOT LOCKED as of the 2026-08-16 audit; nothing in
the material available for this release resolves it.

------------------------------------------------------------------------
