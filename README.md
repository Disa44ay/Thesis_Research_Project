---
type: moc
status: active
public_release: "Release 01"
updated: 2026-08-16
tags: [thesis, football, baa, git-ready, moc]
---
# Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football

## 1. Project Overview

This repository preserves the football thesis search at the end of the foundation period. Football is the active domain, the original PCBAS direction is preserved, and newer candidate families are being evaluated under explicit compute, data, annotation, and deployment constraints.

Start with [[VERSION_BRIEF]] for a plain-language explanation of what was known, what changed, and what remained uncertain at this release.

## 2. Features

1. Preserved PCBAS history and candidate gaps A-D.
2. Football scope and feasibility constraints.
3. Candidate families around anticipation, tactical retrieval, and forecasting.
4. Atomic decision and research-history graph.

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
Constraints + Literature + Dataset Search --> Candidate Comparison --> Decisions --> Next Verification
```

Implemented, planned, and experimental status are distinguished in [[ARCHITECTURE]] and the existing implementation/experiment notes.

## 5. Project Structure

The established numbered structure is preserved from context and constraints through literature, gaps, experiments, implementation, decisions, session history, verification, system architecture, and proposal material as those folders exist in this release.

Core navigation: [[KNOWLEDGE_GRAPH]], [[00_project_governance/CURRENT_STATE]], [[RELEASE_HISTORY]], [[GRAPH_AUDIT]].
