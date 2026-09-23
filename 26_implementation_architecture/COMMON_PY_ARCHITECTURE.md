---
type: architecture
status: active
updated: 2026-09-22
related:
  - "[[FOUR_NOTEBOOK_PIPELINE_DECISION]]"
  - "[[QUARANTINE_MECHANISM_DESIGN]]"
---

# common.py Architecture

## Purpose

A single standalone Python module, stored on Google Drive at
`MyDrive/Thesis_Project/code/common.py`, imported by all four pipeline
notebooks (N1-N4). It holds logic that must behave identically
regardless of which notebook calls it: dataset paths, alignment
checks, the quarantine mechanism, and shared data-loading utilities.

## What belongs in common.py

- Dataset path resolution and file-existence checks.
- The RGB/GSR alignment check used by Gate E (and its extension).
- The quarantine mechanism (see [[QUARANTINE_MECHANISM_DESIGN]]) —
  a general, reusable exclusion pattern, not any one match's specific
  entry.
- Shared metadata-diff and validation helpers.

## What does not belong in common.py

- Model definitions and training loops (these live in N4).
- Feature-extraction code specific to one modality (visual extraction
  in N2, game-state extraction in N3) unless a helper is genuinely
  shared by both.
- Any notebook-specific plotting or exploratory cell.

## Why a standalone Drive module rather than a package

Colab sessions mount Google Drive directly; a standalone `.py` file on
Drive can be imported by any notebook without a packaging or
installation step, and a single edit to it is immediately visible to
every notebook on next import — no version drift between per-notebook
copies.

## Versioning discipline

Each change to `common.py` is expected to bump an internal version
marker and be traceable to a specific fix or decision (the project's
existing convention, evidenced by the fix history the module has
already accumulated through its pre-N1 development). This release does
not restate that fix history in numeric detail; see the scope note
below.

## Scope note

This file describes the module's architecture and role in the pipeline
as decided pre-N1. It does not include the specific version number,
hash, or line-by-line fix history `common.py` had accumulated by the
time N1 actually ran — that belongs to a later release.
