---
type: moc
status: active
public_release: "Release 04"
updated: 2026-08-16
tags: [thesis, football, baa, git-ready, moc]
---
# Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football

## 1. Project Overview

This repository is the current execution-ready thesis state. The research question, proposal, raw-data-to-feature architecture, compute controls, and independent feasibility study are documented. The feasibility pilot and scientific experiments have not yet been run.

Start with [[VERSION_BRIEF]] for a plain-language explanation of what was known, what changed, and what remained uncertain at this release.

## 2. Features

1. Safest primary title and concise verified proposal.
2. Canonical dataset/version policy and cross-modal validation.
3. GSR streaming, frozen visual extraction, compute stop rules and pilot.
4. Independent teammate feasibility replication and self-contained handoff.
5. Planned zero-recurring-cost demo architecture.

## 3. Tech Stack

1. **Obsidian + Git** for research history, backlinks, diffs, and release management.
2. **Primary literature and official dataset documentation** for evidence control.
3. **SoccerTrack v2 / SoccerNet BAA literature** where present in this release.
4. **Python/PyTorch/Jupyter** for the planned data and model pipeline.
5. **FFmpeg and compact NumPy/NPZ/Parquet stores** in later execution stages.
6. **Google Colab/Kaggle** as constrained accelerator environments.
7. **FastAPI** only as a later engineering/demo component, not the research novelty.

## 4. Architecture

```text
Pinned SoccerTrack --> BAS Validator + GSR Streamer + Frozen Video Features --> Alignment --> Window Store --> B1-B5 --> Grouped Evaluation --> Demo
```

Implemented, planned, and experimental status are distinguished in [[ARCHITECTURE]] and the existing implementation/experiment notes.

## 5. Project Structure

The established numbered structure is preserved from context and constraints through literature, gaps, experiments, implementation, decisions, session history, verification, system architecture, and proposal material as those folders exist in this release.

Release 04 additionally includes `21_proposal/` for current and historical proposal artifacts and `22_feasibility/` for the planned replication handoff.

Core navigation: [[KNOWLEDGE_GRAPH]], [[00_project_governance/CURRENT_STATE]], [[22_feasibility/FEASIBILITY_HANDOFF_INDEX]], [[RELEASE_HISTORY]], [[GRAPH_AUDIT]].
