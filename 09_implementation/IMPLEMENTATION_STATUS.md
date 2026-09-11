Implementation Status

The final production architecture has not been locked because the
research question is still under validation.

Intended portfolio layer

The project should ultimately demonstrate an end-to-end deployable
system where appropriate, including data ingestion or ETL, model
inference, API design, experiment management, logging, deployment, and a
minimal dashboard if time permits.

Heavy raw-video end-to-end model training is currently outside the
preferred scope because of compute and timeline constraints.

Deployment constraint update 2026-08-10

The final system must support zero recurring deployment cost. See
[[01_goals_constraints/constraints/Zero Cost Deployment]].

Preferred architecture principle: process short video inputs transiently
or locally, persist lightweight derived outputs, and avoid making
permanent raw-video object storage a requirement.

Backend or system architecture remains a major portfolio objective, but
it must support a defensible research contribution rather than
substitute for one.

Update 2026-08-12

Implementation has not started. A compute-safe preprocessing
architecture is defined in
[[09_implementation/COMPUTE_AND_DATA_PIPELINE]].

Raw 4K end-to-end repeated training is rejected. Frozen visual feature
extraction plus compact structured game-state preprocessing is the
current feasibility plan.

Update 2026-08-20 (Release 05)

The compute-safe preprocessing architecture has been executed, not just
planned, on one match: frozen ResNet-18 visual features were extracted
on CPU at a common 5 FPS timestamp grid, producing a finite (150, 512)
feature matrix aligned to a (150, 22, 2) structured game-state tensor.
See [[../22_feasibility/FEASIBILITY_STUDY_REPORT]] section 3.7.
Production-scale implementation (all ten matches, cached feature store,
API/deployment layer) has not started - only the single-match
feasibility probe has run.

------------------------------------------------------------------------
