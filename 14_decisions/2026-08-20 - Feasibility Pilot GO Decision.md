2026-08-20 - Feasibility Pilot GO Decision

Decision

GO, with strict scope control, on the multimodal BAA pipeline, based on
representative match 117093.

Reasoning

All major execution risks named at Release 04 - data access, annotation
schemas, actor identity coverage, period timing, anticipation-window
construction, leakage control, structured-state materialization, real
video decoding, RGB-GSR synchronization, and visual feature extraction -
were tested and passed on one representative full-match case. See
[[../22_feasibility/FEASIBILITY_STUDY_REPORT]].

Explicitly not decided

This decision does not claim that game-state fusion improves
anticipation. RQ1 and RQ2 remain untested. It also does not certify the
pipeline for the full ten-match dataset; only one match has been
validated in this depth.

Alternatives considered

NO-GO was not selected because no blocking defect was found. MODIFY was
considered for the RGB/GSR alignment issue but was resolved via a
timestamp-based fix rather than a scope reduction, so a plain GO was
issued instead of a conditional MODIFY.

Consequences

Implementation of B0-B5 baselines may begin once the ten-match extension
and independent teammate replication (see
[[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]]) are complete.

See also

[[2026-08-20 - Timestamp Based RGB GSR Alignment Rule]]

------------------------------------------------------------------------
