Architecture

Status at Release 05

The feasibility pilot has been executed on one representative match
(117093): GO, with strict scope control. Full scientific experiments
(B0-B5 training and evaluation) have not yet been executed. See
[[22_feasibility/FEASIBILITY_STUDY_REPORT]].

Status at Release 04 (historical, superseded above)

The system was planned and proposal-ready, with a detailed feasibility
pilot design. The pilot and full scientific experiments had not yet
been executed as of Release 04.

Raw data to research model

    Pinned SoccerTrack v2 revision
            |
      +-----+-----+
      |     |     |
     BAS   GSR   4K video
      |     |     |
    validate stream sample/frozen encode
      |     |     |
      +-----+-----+
            |
     cross-modal alignment
            |
     compact event/state/visual stores
            |
     context -> next 5 s windows
            |
     B1 / B2 / B3 / B4 / B5
            |
     grouped evaluation + per-class analysis

Feasibility gate (as executed, Release 05)

    match 117093, full-match validation (larger scope than the
    originally planned ~10 minute pilot - see
    [[22_feasibility/FEASIBILITY_REPLICATION_STATUS]])
    → parse BAS (2,252 events, 41 players, verified)
    → validate GSR schema and identity coverage (100%)
    → verify BAS-to-GSR timestamp mapping (zero-frame boundary error)
    → build 30s→5s windows (1,092 windows, 535/557 by half)
    → materialize structured tensor + leakage check (PASS)
    → decode RGB, diagnose frame-count mismatch, verify timestamp
      alignment rule (PTS offset = 1.000s)
    → extract frozen visual features at common 5 FPS grid ((150, 512))
    → GO, with strict scope control

    (tiny fusion run, resource report, and independent teammate
    comparison remain open - see [[13_execution/ROADMAP]])

Planned deployment

    short clip / sample
    → temporary preprocessing
    → trained model
    → structured future-action predictions
    → optional lightweight API/demo

Key notes: 1.
[[20_system_architecture/END_TO_END_DATA_SYSTEM_ARCHITECTURE]] 2.
[[20_system_architecture/DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]] 3.
[[20_system_architecture/COMPUTE_BUDGET_AND_STOP_RULES]] 4.
[[20_system_architecture/FEASIBILITY_PILOT_PLAN]] 5.
[[22_feasibility/FEASIBILITY_REPLICATION_STATUS]]

------------------------------------------------------------------------
