---
type: constraints
status: migrated
tags: [goals, constraints, thesis]
source: GOALS_AND_CONSTRAINTS.md
updated: 2026-08-10
---
# Thesis Goals and Hard Constraints

## Must-have constraints
1. Dataset must be free/publicly available.
2. Public datasets only.
3. Dataset should be multimodal whenever the chosen problem genuinely supports it.
4. There must be existing research and reproducible baselines.
5. Problem should be feasible for a 3-person undergraduate team.
6. Training must be feasible on free Colab/Kaggle resources.
7. Avoid dependence on a local GPU.
8. Prefer implementation-heavy work over mathematical novelty.
9. Thesis should produce an end-to-end deployable system.
10. Research should have a realistic path toward a Scopus-indexed venue.

## Desired balance
- Approximately 60% coding / implementation
- Approximately 40% research

Earlier preference was approximately 50/50 AI/ML and backend/application; this evolved toward **60% coding / 40% research**.

## Portfolio objectives
The final project should demonstrate:
- backend engineering,
- AI/ML,
- computer vision,
- multimodal processing,
- ETL/data pipelines,
- model inference,
- API design,
- deployment,
- experiment management.

## Publication objective
The team wants a realistic publication opportunity rather than a guaranteed publication.

Avoid:
- fake novelty,
- unsupported claims,
- research gaps invented by LLMs,
- competing directly with large labs on huge architectures,
- experiments that require expensive GPUs.

## Core strategy
Compete through:
- problem framing,
- multimodal integration,
- system engineering,
- efficient modeling,
- reproducibility,
- careful experiments,
- useful deployment.

Do not attempt to beat major research labs through raw model size.

## Constraint update 2026-08-10

### Domain
The active search is now restricted to football. See [[01_goals_constraints/constraints/Football Domain Scope]].

### Supervisor fit
Computer Vision is preferred because the thesis instructor specializes in CV. See [[01_goals_constraints/constraints/Computer Vision Preference]].

### Multimodality
Multimodality is a strong preference, not a hard requirement. It must be scientifically meaningful. See [[01_goals_constraints/constraints/Multimodality Preference]].

### Research compute
A modest paid Colab plan may be used if needed, but this does not justify large-scale raw-video training. See [[01_goals_constraints/constraints/Research Compute Budget]].

### Deployment
Recurring deployment cost must remain zero. Permanent raw-video storage should not be a core requirement. See [[01_goals_constraints/constraints/Zero Cost Deployment]].

### Dataset access
Direct public download is preferred. Request-based academic access is acceptable only with manageable delay and fallback. See [[01_goals_constraints/constraints/Dataset Access Policy]].

### Manual annotation
Manual annotation is allowed only as a small targeted layer, approximately 100 to 150 samples maximum. See [[01_goals_constraints/constraints/Annotation Budget]].

### Effective capacity
Plan around two continuously active team members. See [[01_goals_constraints/constraints/Team Capacity]].

### Immediate administrative deadline
Candidate titles are needed within two days. See [[01_goals_constraints/constraints/Title Deadline]].
