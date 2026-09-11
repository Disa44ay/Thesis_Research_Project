---
type: implementation-status
status: not-started
tags: [implementation, system]
updated: 2026-08-10
---
# Implementation Status

The final production architecture has not been locked because the research question is still under validation.

## Intended portfolio layer
The project should ultimately demonstrate an end-to-end deployable system where appropriate, including data ingestion or ETL, model inference, API design, experiment management, logging, deployment, and a minimal dashboard if time permits.

Heavy raw-video end-to-end model training is currently outside the preferred scope because of compute and timeline constraints.

## Deployment constraint update 2026-08-10
The final system must support zero recurring deployment cost. See [[01_goals_constraints/constraints/Zero Cost Deployment]].

Preferred architecture principle: process short video inputs transiently or locally, persist lightweight derived outputs, and avoid making permanent raw-video object storage a requirement.

Backend or system architecture remains a major portfolio objective, but it must support a defensible research contribution rather than substitute for one.
