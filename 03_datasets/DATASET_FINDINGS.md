---
type: dataset-landscape
status: migrated
tags: [datasets, public-data]
source: DATASET_FINDINGS.md
updated: 2026-08-10
---
# Dataset Findings

## Dataset requirements
The selected dataset should ideally be:
- public,
- free,
- downloadable,
- documented,
- benchmarked,
- sufficiently annotated,
- supported by existing code,
- feasible on Colab/Kaggle,
- multimodal or naturally capable of multimodal fusion.

## Dataset candidates found

| Dataset | Domain | Main task | Compute | Current relevance |
|---|---|---|---|---|
| SoccerNet-v2 | Football | Action spotting/replay grounding | Low with pre-extracted features | Very high |
| SoccerNet PCBAS | Football | Player-centric ball action spotting | Medium if structured features are used | Very high |
| SoccerNet Tracking | Football | MOT | High if training tracker from raw video | High |
| SROIE | Document AI | Receipt extraction | Low | High |
| FUNSD | Document AI | Form understanding | Low | High |
| CORD | Document AI | Receipt understanding | Low | High |
| DocVQA | Document AI | VQA | Medium/high depending on model | High |
| LEVIR-CD | Remote sensing | Change detection | Low/medium | Very high |
| WHU-CD | Remote sensing | Change detection | Low/medium | High |
| xBD | Remote sensing | Disaster damage assessment | Medium | High |
| SpaceNet | Remote sensing | Building/object extraction | Medium/high | High |
| EuroSAT | Remote sensing | Land-use classification | Low | High |
| SEN12MS | Remote sensing | Multispectral classification | Medium | High |

## Current strongest football dataset direction
SoccerNet PCBAS / related SoccerNet player-centric data.

Why:
- directly matches the user's football interest,
- modern task,
- strong benchmark ecosystem,
- public benchmark infrastructure,
- structured tracking/features can reduce compute,
- natural opportunity for backend + AI system building.

## Multimodality consideration
The football direction can combine:
- video-derived features,
- player bounding boxes,
- player identity/tracking information,
- spatial coordinates,
- action logits,
- temporal context,
- potentially audio/commentary.

However, the exact availability and license of each modality must be verified from the official dataset release before claiming a multimodal experiment.

## Critical warning
Earlier AI-generated dataset rankings included claims such as exact dataset sizes, storage requirements, and challenge details. These must be rechecked against official dataset documentation before being used in a thesis.

## Dataset update 2026-08-10

### New dataset candidates
#### [[03_datasets/datasets/SoccerNet GSR]]
Verified from the 2024 primary paper. It contains 200 short 30-second sequences and rich game-state annotations, making it strategically interesting under limited compute.

#### [[03_datasets/datasets/SoccerTrack v2]]
Verified from the public repository and technical report. It provides 10 full-length panoramic 4K matches with per-frame game-state annotations and 12 ball-action classes under CC BY 4.0.

#### [[03_datasets/datasets/SoccerNet Ball Action Anticipation]]
Verified as the dataset introduced with FAANTRA for future ball-action prediction.

### Access policy update
Directly downloadable datasets are preferred. Free request-based academic access remains acceptable with a fallback. See [[01_goals_constraints/constraints/Dataset Access Policy]].

### Compute warning
A public dataset is not automatically feasible. Full-match 4K video can still be too expensive. Prefer structured annotations, selective clips, downsampled data, or frozen features when scientifically legitimate.

## Dataset update 2026-08-12: SoccerTrack v2 direct audit

The user confirmed direct access to the complete SoccerTrack v2 release and supplied the 10 BAS JSON files for analysis.

[[03_datasets/analysis/SoccerTrack v2 BAS Statistical Audit]] found 23,663 actions with severe long-tail imbalance but enough total annotations to keep the derived BAA benchmark viable.

The GSR release is too large to move through chat directly. [[03_datasets/analysis/SoccerTrack v2 GSR Practical Handling]] defines a streaming and downsampling plan.
