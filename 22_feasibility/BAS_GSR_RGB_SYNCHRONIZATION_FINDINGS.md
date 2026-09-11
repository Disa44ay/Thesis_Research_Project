---
type: technical-finding
status: verified
severity: would-have-caused-silent-data-corruption
related:
  - "[[FEASIBILITY_STUDY_REPORT]]"
  - "Reusable_Research_OS (companion repository, cross-repo reference)"
---

# BAS/GSR/RGB Synchronization Findings

## The finding

The SoccerTrack v2 panoramic video for match 117093 has a presentation
timeline that begins **one second after** match time zero. FFprobe
reports 67,625 decoded video frames against 67,650 GSR frames for the
same half — a 25-frame difference. The RGB stream's first decoded frame
has presentation timestamp (PTS) 1.000s, not 0.000s, while GSR
represents the half starting from match time 0.00s.

## Why this matters

Before this was diagnosed, the natural implementation shortcut would
have been: "GSR frame N corresponds to RGB decoded frame N," since both
run at 25 FPS and both nominally cover the same 45-minute half. That
assumption is wrong by a fixed one-second (25-frame) offset. A direct
overlay test made the error visible: GSR player bounding boxes for
match time 30.0s, drawn on RGB decoded frame 750 (the "same index"
frame, true PTS 31.0s), are visibly displaced from the players in the
image. The same boxes drawn on RGB decoded frame 725 (true PTS ~30.0s)
align correctly.

Had this not been caught, every multimodal training sample would have
paired each GSR game-state frame with an RGB frame from roughly one
second in the future — a silent, systematic, undetectable-by-shape-check
form of data corruption, because tensor shapes and frame counts would
still have looked reasonable.

## The correct rule (verified)

Align RGB and GSR by **presentation/match timestamp**, never by raw
decoded frame index equality, even when both modalities claim the same
nominal frame rate. Concretely, for this dataset: sample RGB at the
nearest decoded frame to the target PTS, and sample GSR via the already
verified `local_ms -> local_frame` mapping. When both are resampled onto
a common timestamp grid (this study used 5 FPS, 30.0-59.8s), the
resulting timestamp matching error was ~1.07e-13 seconds — floating
point noise, i.e., true alignment.

## Reusable principle (generalization candidate)

This is exactly the kind of finding the Reusable Research OS's
multimodal validation protocol exists to catch. The general form:
**never assume two sources at the same nominal frame rate share a frame
index space; verify the two clocks (or timestamp origins) independently
before fusing, using a real visual/positional overlay test as ground
truth, not just matching frame counts.** A close frame count (67,625 vs
67,650, off by 0.04%) can still hide a systematic full-frame offset. See
`Reusable_Research_OS/12_execution_validation/MULTIMODAL_SYNCHRONIZATION_PRINCIPLE.md`
for the generalized, project-agnostic version of this rule.

## Status

Verified on one representative match (117093, first half) via direct
visual overlay and a controlled naive-index comparison. Not yet
confirmed to hold identically across all ten matches or across both
halves of matches with different raw source files — treat the one
second offset as verified-for-117093-first-half, not as an assumed
universal constant, until the ten-match extension is run.

------------------------------------------------------------------------
