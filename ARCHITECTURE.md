# Architecture

## Status at Release 02
The final research system had not been implemented. A candidate data/model architecture had emerged from the SoccerTrack v2 investigation.

```text
SoccerTrack video + GSR + BAS
→ one-time visual/state preprocessing
→ derived short-horizon BAA windows
→ visual-only / state-only / fusion candidates
→ future class + time prediction
```

This remains a **planned architecture** at this release.

Key notes:
1. [[08_experiments/BENCHMARK_DESIGN_DRAFT]]
2. [[08_experiments/BASELINE_AND_ABLATION_PLAN]]
3. [[09_implementation/COMPUTE_AND_DATA_PIPELINE]]
4. [[06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]
