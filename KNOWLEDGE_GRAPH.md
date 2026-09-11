Knowledge Graph

Active research spine

    flowchart TD
        C[[01_goals_constraints/GOALS_AND_CONSTRAINTS]] --> F[[07_topic_selection/PHASE_5_TITLE_PACKAGE]]
        L[[19_verification/PHASE_1_RELATED_WORK_LOCK]] --> N[[19_verification/PHASE_3_NOVELTY_LOCK]]
        N --> F
        D[[03_datasets/datasets/SoccerTrack v2]] --> Q[[20_system_architecture/CANONICAL_DATASET_REVISION_POLICY]]
        Q --> A[[20_system_architecture/DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]
        A --> B[[08_experiments/BENCHMARK_PROTOCOL_LOCK]]
        B --> M[[08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]
        F --> M
        M --> S[[20_system_architecture/END_TO_END_DATA_SYSTEM_ARCHITECTURE]]
        S --> P[[20_system_architecture/FEASIBILITY_PILOT_PLAN]]
        P --> R[[21_proposal/PROPOSAL_ARTIFACT_INDEX]]
        P --> E[[22_feasibility/FEASIBILITY_STUDY_REPORT]]
        E --> BC[[22_feasibility/BAA_BENCHMARK_CONSTRUCTION]]
        E --> SY[[22_feasibility/BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]]
        E --> GO[[14_decisions/2026-08-20 - Feasibility Pilot GO Decision]]
        E --> RS[[22_feasibility/FEASIBILITY_REPLICATION_STATUS]]
        RS --> EP[[23_experiment_framework/EXPERIMENT_PROTOCOL]]
        EP --> M

Evidence spine

-   [[04_literature/sources/SOURCE - FAANTRA 2025]]
-   [[04_literature/sources/SOURCE - SoccerNet Challenges 2026]]
-   [[04_literature/sources/SOURCE - Ochin Game State Action Detection
    2025]]
-   [[04_literature/sources/SOURCE - Beyond Pixels 2025]]
-   [[04_literature/sources/SOURCE - FOOTPASS 2025]]
-   [[04_literature/sources/SOURCE - SoccerTrack v2 2025]]
-   [[15_ai_configuration/research_runs/PR 005 - Claude Final Evidence
    Lock]]
-   [[19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]]

Dataset and benchmark spine

-   [[03_datasets/analysis/SoccerTrack v2 BAS Statistical Audit]]
-   [[03_datasets/analysis/SoccerTrack v2 GSR Practical Handling]]
-   [[20_system_architecture/CANONICAL_DATASET_REVISION_POLICY]]
-   [[20_system_architecture/GSR_STREAMING_AND_COMPRESSION_PIPELINE]]
-   [[20_system_architecture/VISUAL_FEATURE_EXTRACTION_PIPELINE]]
-   [[20_system_architecture/DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]
-   [[08_experiments/BENCHMARK_PROTOCOL_LOCK]]

Experiment and execution spine

-   [[08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]
-   [[20_system_architecture/COMPUTE_BUDGET_AND_STOP_RULES]]
-   [[20_system_architecture/FEASIBILITY_PILOT_PLAN]]
-   [[20_system_architecture/DEPLOYMENT_ARCHITECTURE]]
-   [[13_execution/ONE_MONTH_EXECUTION]]

Historical branches preserved

-   [[05_direction/PCBAS_STATE]]
-   [[07_topic_selection/candidates/Candidate 02 - Tactical
    Spatiotemporal Retrieval]]
-   [[07_topic_selection/candidates/Candidate 03 - Tactical State
    Forecasting]]
-   [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]]
-   [[07_topic_selection/rejections/Generic Football RAG]]

Version provenance

See [[18_version_history/VERSION_HISTORY]],
[[16_session_history/SESSION_LOG]], and [[14_decisions/DECISION_LOG]].

Proposal draft: [[21_proposal/PROPOSAL_DRAFT]].

------------------------------------------------------------------------
