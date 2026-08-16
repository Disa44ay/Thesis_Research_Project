---
type: decision
status: active
created: 2026-08-10
updated: 2026-08-10
tags: [decision, compute, deployment]
depends_on:
  - "[[01_goals_constraints/constraints/Research Compute Budget]]"
  - "[[01_goals_constraints/constraints/Zero Cost Deployment]]"
supported_by:
  - "[[04_literature/sources/SOURCE - Google Colab Paid Services 2026]]"
---
# Decision: Expand Research Compute, Keep Deployment Free

## Decision
Allow modest paid Colab research compute if needed, while keeping recurring deployment cost at zero.

## Reason
A small research-compute purchase can expand feasible model training, but ongoing paid hosting or video storage is outside the team's budget.

## Practical consequence
Moderate fine-tuning is allowed. Large-scale end-to-end raw-video training remains out of scope. The deployed system should avoid permanent raw-video storage and persist lightweight outputs where possible.
