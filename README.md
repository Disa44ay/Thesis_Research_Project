---
type: moc
status: active
public_release: "Release 03"
updated: 2026-08-16
tags: [thesis, football, baa, git-ready, moc]
---
# Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football

## 1. Project Overview

This repository captures the scientifically re-verified thesis state. The defensible core question is whether explicit player game state adds predictive value to unseen-future Ball Action Anticipation. Dataset counts/folds remain gated on canonical release validation.

Start with [[VERSION_BRIEF]] for a plain-language explanation of what was known, what changed, and what remained uncertain at this release.

## 2. Features

1. PR-005 and full primary-source re-verification.
2. Narrow novelty lock and additional prior-art threats.
3. Canonical release/alignment risks and withdrawn premature counts/folds.
4. Controlled B0-B5 experiment matrix.

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
Pinned Dataset Gate --> Controlled B1-B5 Models --> Match-level Evaluation --> Scientific Interpretation
```

Implemented, planned, and experimental status are distinguished in [[ARCHITECTURE]] and the existing implementation/experiment notes.

## 5. Project Structure

The established numbered structure is preserved from context and constraints through literature, gaps, experiments, implementation, decisions, session history, verification, system architecture, and proposal material as those folders exist in this release.

Core navigation: [[KNOWLEDGE_GRAPH]], [[00_project_governance/CURRENT_STATE]], [[RELEASE_HISTORY]], [[GRAPH_AUDIT]].
