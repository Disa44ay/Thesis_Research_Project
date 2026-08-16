---
type: research-landscape
status: migrated
tags: [domains, history]
source: DOMAIN_EXPLORATION.md
updated: 2026-08-10
---
# Domain Exploration Findings

## Initial priority domains

### 1. Football Video Understanding
Description:
Automated understanding of broadcast soccer videos, including action spotting, player-centric actions, tracking, tactical analysis, replay grounding, anticipation, and multimodal video understanding.

Research activity:
Very high.

Industry relevance:
Very high, especially sports analytics, scouting, broadcasting, and tactical analysis.

Major ecosystem:
- SoccerNet
- SoccerNet-v2
- SoccerNet Tracking
- SoccerNet challenge tasks
- Player-Centric Ball Action Spotting

Main problem:
Raw end-to-end video processing is compute-heavy.

Important workaround:
Use organizer-provided pre-extracted features/tracking information whenever legitimate for the experiment.

### 2. Satellite Vision / Remote Sensing
Description:
Computer vision over satellite imagery for classification, segmentation, detection, and change detection.

Research activity:
Very high.

Public datasets discussed:
- LEVIR-CD
- WHU-CD
- xBD
- SpaceNet
- SpaceNet 7
- EuroSAT
- SEN12MS

Compute:
Generally manageable using patch-based training.

Publication potential:
High.

### 3. General Computer Vision — Document AI
Document AI was considered because it strongly matches backend deployment.

Datasets discussed:
- SROIE
- FUNSD
- CORD
- DocVQA
- PubLayNet
- RVL-CDIP
- XFUND

Typical models:
- LayoutLM/LayoutLMv3
- Donut
- TrOCR
- lightweight detectors

Compute:
Generally low-to-medium with parameter-efficient methods.

## Strategic conclusion
The initial broad ranking favored:
1. Document AI
2. Satellite Vision
3. Football Video Understanding

However, the user's strong football interest caused deeper investigation of the SoccerNet ecosystem.

The current project direction therefore shifted toward football rather than blindly following the easiest domain.

## Search narrowing 2026-08-10
The active search is now intentionally restricted to football rather than continuing cross-domain comparison.

The search remains broader than PCBAS. Current areas of interest include tactical analysis, short-horizon forecasting or anticipation, intelligent football-video retrieval, Game State Reconstruction, player trajectories, and other football CV tasks that survive the project's constraints.

Camera style is not a restriction. Broadcast video, fixed or panoramic cameras, tactical views, top-down representations, and tracking-based datasets are acceptable when public, feasible, and scientifically useful.

Relevant active SoccerNet task families were verified from official challenge material. See [[04_literature/sources/SOURCE - SoccerNet Challenges 2026]].
