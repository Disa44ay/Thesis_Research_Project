Feasibility Replication Status

Status (updated at Release 05)

**EXECUTED on one representative match. NOT YET INDEPENDENTLY
REPLICATED. NOT YET EXTENDED to the remaining nine matches (of which
one, 132831, is currently excluded/quarantined - see
[[MATCH_132831_CALIBRATION_DEFECT]] - leaving 8 matches actually
available for the extension until that match's GSR is corrected).**

A full feasibility result, GO decision, and dataset/schema/alignment
validation now exist — see [[FEASIBILITY_STUDY_REPORT]] (dated
2026-08-20). What still does not exist: a second teammate's independent
run of the same pipeline to confirm structural agreement, any run on
the other nine matches, or any trained/evaluated model.

**Scope note — the executed run differs from the originally planned
mini-pilot below.** The plan as written at Release 04 called for a
short ~10-minute, 5-seconds-observed to next-5-seconds segment purely
to validate pipeline mechanics. What was actually executed instead
processed the benchmark construction over a full match half using the
project's real 30-second observation / 5-second anticipation window
definition (see [[BAA_BENCHMARK_CONSTRUCTION]]), plus a separate 30-
second RGB/GSR visual-synchronization probe. This is a **larger and more
representative** validation than originally planned, not a smaller one,
but it means the "first ~10 minutes, 5s->5s" pilot described below was
superseded rather than run as originally specified. This scope
difference is recorded here rather than silently reconciled, per the
project's no-invention rule.

Originally planned common pilot (superseded in scope by the executed
run above; retained for historical record)

Unless the pinned canonical revision reveals a new issue:

-   match: 117093
-   segment: first valid approximately 10 minutes of one half
-   modalities: BAS + matching GSR + matching panoramic video
-   pilot task: 5 seconds observed → next 5 seconds
-   purpose: pipeline validation, not scientific accuracy.

Match 132831 is not the default pilot because the project history
records a documented correction issue requiring canonical-revision
verification (see [[MATCH_132831_CALIBRATION_DEFECT]] for the full,
sourced detail: swapped calibration keypoints, ~1260.95px shipped RMS
error vs. ~18.07px corrected, GSR not yet regenerated from the fix).

Independent teammate replication (still open)

Two teammates may run the same pipeline independently on match 117093.
This has not yet happened. It remains a precondition for treating the
pipeline as structurally validated project-wide, not just
single-run-validated.

The pipeline is structurally validated only when the runs agree on, or
can reproducibly explain differences in:

1.  retained BAS events,
2.  state tensor shapes,
3.  visual feature shapes,
4.  generated window count,
5.  alignment validator outputs,
6.  class/time target construction.

Hardware-dependent timing may differ.

Required stages

    pin source/revision
    → parse BAS
    → stream/downsample GSR
    → extract frozen visual features
    → align modalities
    → build windows
    → overfit a tiny batch
    → run tiny fusion model
    → measure resource usage
    → compare teammate structural outputs
    → GO / MODIFY / NO-GO

Handoff files

1.  [[CONTEXT_HANDOFF]] contains enough context for another teammate or
    AI assistant to understand and critique the pilot.
2.  Feasibility Study Guide gives the step-by-step execution plan.
3.  [[../20_system_architecture/FEASIBILITY_PILOT_PLAN]] preserves the
    earlier vault-native feasibility design.

------------------------------------------------------------------------
