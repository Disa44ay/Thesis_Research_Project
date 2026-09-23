Public Release Mapping

The repositories preserve the original historical v1-v5 snapshots, but
the Git-facing public history is grouped into synchronized semantic
releases.

  -----------------------------------------------------------------------
  Public release          Historical basis        Milestone
  ----------------------- ----------------------- -----------------------
  Release 01              v1-v2 period            Foundation and Scope
                                                  Formation

  Release 02              v3                      Evidence-Driven
                                                  Candidate Validation

  Release 03              v4                      Scientific Lock and
                                                  Re-verification

  Release 04              v5 plus verified        Execution-Ready
                          post-v5 work through    Proposal and
                          2026-08-16              Feasibility

  Release 05              Release 04 plus the     Feasibility Executed
                          executed feasibility    and Experiment-Ready
                          pilot, 2026-08-16 to
                          2026-08-20

  Release 06              Release 05 plus the     Pre-Implementation
                          Gate H / Gate E         Gate Extension
                          extension pre-tasks
                          and four-notebook
                          pipeline architecture
                          decision, 2026-09-14
                          to 2026-09-17
  -----------------------------------------------------------------------

The public grouping does not erase the original version history.
Historical v1-v5 remain provenance checkpoints, while the public
releases are milestone labels for GitHub and synchronized project
communication.

See [[VERSION_BRIEF]] for the state represented by this snapshot.

## Release 06 scope note

Release 06 stops before N1's execution, per explicit project
instruction. N1 has run per project memory (completed 2026-09-22), but
its results, along with all of N2-N5, are reserved for a future,
separate release. Release 06 covers `25_gate_validation/` (Gate H and
Gate E extension results) and `26_implementation_architecture/` (the
four-notebook pipeline decision, `common.py`'s architecture, and the
general quarantine-mechanism design).
