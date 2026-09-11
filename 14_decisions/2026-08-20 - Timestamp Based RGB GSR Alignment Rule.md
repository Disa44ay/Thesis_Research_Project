2026-08-20 - Timestamp Based RGB GSR Alignment Rule

Decision

Align RGB video and GSR game-state data by presentation/match timestamp.
Never assume equal raw decoded frame index means equal match time, even
when both sources report the same nominal frame rate.

Reasoning

FFprobe measurement on match 117093's canonical first-half panorama
showed 67,625 decoded frames against GSR's 67,650 frames for the same
half. Diagnosis found the RGB stream's presentation timestamps begin at
PTS 1.000s while GSR represents the half from match time 0.00s - a
one-second presentation offset. A direct overlay test (GSR boxes for
match time 30.0s drawn on RGB decoded frame 750, the naive equal-index
frame, true PTS 31.0s) showed visible displacement; the same boxes on
RGB decoded frame 725 (true PTS ~30.0s) aligned correctly.

Alternatives considered

Assuming equal frame indices (rejected - empirically produces
misaligned player boxes). Discarding the video and using only GSR
(rejected - would remove the visual-only baseline and the RGB branch of
the fusion comparison entirely, undermining RQ1).

Consequences

All future RGB feature extraction must resample by timestamp against a
common grid, as done in the 5 FPS, 150-timestep extraction described in
[[../22_feasibility/FEASIBILITY_STUDY_REPORT]]. This rule is proposed
for generalization into the Reusable Research OS as a project-agnostic
multimodal synchronization principle - see
[[../22_feasibility/BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]].

------------------------------------------------------------------------
