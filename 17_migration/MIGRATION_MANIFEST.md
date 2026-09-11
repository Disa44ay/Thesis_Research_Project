Migration Manifest

Preserved in this project vault

User profile, goals and constraints, domain exploration, dataset
findings, literature findings, PCBAS state, SoccerNet concepts, FOOTPASS
note, candidate research gaps, one-month execution plan, and decision
history.

The richer standalone versions of the supplied thesis notes were used
where available. The original Obsidian concept notes were retained for
graph continuity.

Mixed notes split

RESEARCH_STRATEGY.md, AI_WORKFLOW.md, and REUSABLE_PROMPTS.md contained
reusable system logic mixed with this thesis’s concrete constraints.

Generic logic moved to the Reusable Research OS.

The thesis-specific profile, domain priorities, execution limits, and
AI-role history were preserved in
[[15_ai_configuration/APPLIED_AI_RESEARCH_CONFIGURATION]].

Future lifecycle notes added

Topic lock, experiment status, implementation status, thesis and paper
status, publication status, defense status, current state, and session
history were added so the vault can track the entire journey instead of
stopping at research-gap discovery.

The combined migration package retains an unchanged source snapshot for
auditability.

Release 04 -> Release 05 migration (2026-09-10)

Previous state: Release 04 was execution-ready but the feasibility pilot
had not run.

New state: the pilot executed on match 117093 with a GO decision. This
migration:

1.  Rewrote [[../VERSION_BRIEF]], [[../README]], [[../ARCHITECTURE]],
    [[../RELEASE_HISTORY]], [[../00_project_governance/CURRENT_STATE]]
    to reflect the executed pilot. Superseded Release 04 wording is kept
    as clearly labeled historical text within those same files, not
    deleted.
2.  Added new files rather than overwriting old evidence:
    [[../22_feasibility/FEASIBILITY_STUDY_REPORT]],
    [[../22_feasibility/BAA_BENCHMARK_CONSTRUCTION]],
    [[../22_feasibility/BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]],
    [[../22_feasibility/ERROR_LOG]],
    [[../14_decisions/2026-08-20 - Feasibility Pilot GO Decision]],
    [[../14_decisions/2026-08-20 - Timestamp Based RGB GSR Alignment Rule]],
    [[../13_execution/ROADMAP]], [[../08_experiments/EXPERIMENT_LOG]],
    [[../03_datasets/DATASET_DOCUMENTATION]],
    [[../23_experiment_framework/EXPERIMENT_PROTOCOL]],
    [[../24_publication_positioning/RESEARCH_POSITIONING]].
3.  Updated (appended to, not replaced) [[../22_feasibility/FEASIBILITY_REPLICATION_STATUS]],
    [[../14_decisions/DECISION_LOG]], [[../16_session_history/SESSION_LOG]],
    [[../18_version_history/VERSION_HISTORY]],
    [[../08_experiments/EXPERIMENT_STATUS]],
    [[../09_implementation/IMPLEMENTATION_STATUS]].
4.  Left untouched: all Release 01-04 candidate, literature, decision,
    verification, and proposal material, including the superseded long
    proposal.

Reason: the feasibility pilot's execution is the single largest factual
change since Release 04 and needed to be reflected everywhere the
"not yet executed" status was previously recorded, while preserving that
Release 04 accurately described its own point in time.

Compatibility: no folder was renamed or removed. Three new numbered
folders were added (23_experiment_framework/, 24_publication_positioning/)
following the next available numbers after 22_feasibility/, avoiding the
numbering collision present in the earlier draft Release 05A package
(which had proposed 20_feasibility_validation/ and
21_architecture_update/, colliding with the existing 20_system_architecture/
and 21_proposal/). Feasibility-validation content was placed inside the
existing 22_feasibility/ folder instead.

------------------------------------------------------------------------
