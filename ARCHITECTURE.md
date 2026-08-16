# Architecture

## Status at Release 04
The system is **planned and proposal-ready**, with a detailed feasibility pilot. The pilot and full scientific experiments have **not yet been executed**.

## Raw data to research model

```text
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
```

## Feasibility gate

```text
match 117093, about 10 minutes
→ parse BAS
→ stream/downsample GSR
→ extract frozen video features
→ align
→ build 5s→5s windows
→ tiny-batch overfit
→ tiny fusion run
→ resource report
→ independent teammate comparison
→ GO / MODIFY / NO-GO
```

## Planned deployment

```text
short clip / sample
→ temporary preprocessing
→ trained model
→ structured future-action predictions
→ optional lightweight API/demo
```

Key notes:
1. [[20_system_architecture/END_TO_END_DATA_SYSTEM_ARCHITECTURE]]
2. [[20_system_architecture/DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]
3. [[20_system_architecture/COMPUTE_BUDGET_AND_STOP_RULES]]
4. [[20_system_architecture/FEASIBILITY_PILOT_PLAN]]
5. [[22_feasibility/FEASIBILITY_REPLICATION_STATUS]]
