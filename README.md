Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football

1. Project Overview

This repository is the current thesis state at Release 05. The
feasibility pilot has been executed on one representative match (GO
decision, strict scope control); the ten-match extension, independent
teammate replication, and all scientific experiments (B0-B5) have not
yet been run.

Start with [[VERSION_BRIEF]] for a plain-language explanation of what
was known, what changed, and what remained uncertain at this release,
and [[22_feasibility/FEASIBILITY_STUDY_REPORT]] for the executed pilot
itself.

2. Features

1.  Safest primary title and concise verified proposal.
2.  Canonical dataset/version policy and cross-modal validation.
3.  GSR streaming, frozen visual extraction, compute stop rules and
    pilot.
4.  Independent teammate feasibility replication and self-contained
    handoff.
5.  Planned zero-recurring-cost demo architecture.

3. Tech Stack

1.  Obsidian + Git for research history, backlinks, diffs, and release
    management.
2.  Primary literature and official dataset documentation for evidence
    control.
3.  SoccerTrack v2 / SoccerNet BAA literature where present in this
    release.
4.  Python/PyTorch/Jupyter for the planned data and model pipeline.
5.  FFmpeg and compact NumPy/NPZ/Parquet stores in later execution
    stages.
6.  Google Colab/Kaggle as constrained accelerator environments.
7.  FastAPI only as a later engineering/demo component, not the research
    novelty.

4. Architecture

    Pinned SoccerTrack --> BAS Validator + GSR Streamer + Frozen Video Features --> Alignment --> Window Store --> B1-B5 --> Grouped Evaluation --> Demo

Implemented, planned, and experimental status are distinguished in
[ARCHITECTURE] and the existing implementation/experiment notes.

5. Project Structure

The established numbered structure is preserved from context and
constraints through literature, gaps, experiments, implementation,
decisions, session history, verification, system architecture, and
proposal material as those folders exist in this release.

Release 04 additionally includes 21_proposal/ for current and historical
proposal artifacts and 22_feasibility/ for the feasibility record
(now executed - see below).

Release 05 additionally includes 23_experiment_framework/ for the
execution-ready experiment protocol and 24_publication_positioning/
for early publication framing, plus new required release-management
files: 13_execution/ROADMAP.md, 08_experiments/EXPERIMENT_LOG.md,
22_feasibility/ERROR_LOG.md, and 03_datasets/DATASET_DOCUMENTATION.md.
22_feasibility/archive/ holds a superseded feasibility-report PDF
(same content, earlier working title), kept for provenance rather than
deleted.

Core navigation: [[KNOWLEDGE_GRAPH]],
[[00_project_governance/CURRENT_STATE]],
[[22_feasibility/FEASIBILITY_STUDY_REPORT]],
[[22_feasibility/FEASIBILITY_HANDOFF_INDEX]], [[13_execution/ROADMAP]],
[[RELEASE_HISTORY]], [[GRAPH_AUDIT]].

------------------------------------------------------------------------
