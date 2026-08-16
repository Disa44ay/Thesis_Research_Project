---
type: constraint
status: active
created: 2026-08-10
updated: 2026-08-10
tags: [constraint, compute, colab]
supported_by:
  - "[[04_literature/sources/SOURCE - Google Colab Paid Services 2026]]"
related:
  - "[[14_decisions/2026-08-10 - Research Compute Expanded Deployment Still Free]]"
---
# Constraint: Research Compute Budget

## Research compute
The team may purchase a low-cost Google Colab paid plan if needed for model training. As of the 2026-08-10 verification checkpoint, Google's official Colab pricing page states that Colab Pro includes 100 compute units per month, with resource availability and usage limits still applying.

## Practical interpretation
Paid Colab expands the feasible search area, but it does not make large-scale raw-video training acceptable.

Prefer frozen or pretrained backbones, moderate fine-tuning, short clips, structured features, player trajectories, lightweight temporal models, selective video processing, or similarly bounded experiments.

## Re-verification rule
Pricing, available GPUs, and resource limits must be checked again before purchase or experiment planning because they can change.
