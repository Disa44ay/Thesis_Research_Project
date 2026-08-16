---
type: data-policy
status: mandatory
created: 2026-08-14
updated: 2026-08-14
tags: [dataset-version, provenance, soccertrack-v2]
related:
  - "[[END_TO_END_DATA_SYSTEM_ARCHITECTURE]]"
  - "[[DATA_ALIGNMENT_AND_VALIDATION_PROTOCOL]]"
  - "[[../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]]"
---
# Canonical Dataset Revision Policy

## Why this exists
The uploaded Google Drive BAS snapshot and the current documented SoccerTrack v2 schema are not identical. The official repository now points to a public Hugging Face dataset and also distributes data through Google Drive. Experiments must therefore pin the exact release rather than relying on the dataset name alone.

## Required manifest
Record:
- source URL/provider
- revision/commit or download date
- match IDs
- BAS/GSR/video file names
- file hashes when practical
- known correction status
- excluded matches/halves

## Rule
Do not mix annotations from one revision with video/GSR from another revision without an explicit compatibility check.

The historical Drive snapshot with 23,663 BAS events remains valuable as research provenance, but final benchmark statistics must be regenerated from the pinned experimental release.
