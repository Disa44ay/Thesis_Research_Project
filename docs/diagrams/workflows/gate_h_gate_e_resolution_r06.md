---
type: diagram
status: active
purpose: "How Gate H and the Gate E extension were run and resolved, 2026-09-14 to 2026-09-17."
created: 2026-09-22
related_document: "[[../../25_gate_validation/GATE_STATUS_SUMMARY]]"
---

# Gate H / Gate E Resolution Timeline — Release 06

Rendered image: `../images/thesis/thesis_gate_h_gate_e_resolution_r06.png`
(created 2026-09-22, Release 06, from this file's mermaid source).

```mermaid
flowchart LR
    A["2026-09-14<br/>Protocol established<br/>(division of labor: Task A, Task B)"] --> B["Task A:<br/>gate_h_compute_feasibility_probe.py"]
    A --> C["Task B:<br/>gate_e_multi_match_offset_check.py"]

    B --> D["2026-09-15<br/>Gate H resolved<br/>~5.8 min/match, ~0.73 units/match,<br/>GPU ~0.34% utilization<br/>Tensorization bug fixed"]

    C --> E["2026-09-16/17<br/>Gate E extension resolved<br/>1s offset: 14/20 halves<br/>Absent: 6/20 halves<br/>Tail loss: 10/20 halves<br/>Unresolved: 1 half"]

    D --> F["Both cross-checked against<br/>Release 05 pilot numbers"]
    E --> F
    F --> G["Four-notebook pipeline<br/>architecture decided"]
```

## Reading this diagram

Task A and Task B ran in parallel per the established division of
labor. Both results were cross-checked against each other and against
the single-match Release 05 pilot before the pipeline architecture
decision was finalized.
