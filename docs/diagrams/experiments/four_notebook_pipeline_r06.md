---
type: diagram
status: active
purpose: "Four-notebook pipeline architecture and the shared common.py module."
created: 2026-09-22
related_document: "[[../../26_implementation_architecture/FOUR_NOTEBOOK_PIPELINE_DECISION]]"
---

# Four-Notebook Pipeline — Release 06

Rendered image: `../images/thesis/thesis_four_notebook_pipeline_r06.png`
(created 2026-09-22, Release 06, from this file's mermaid source).

```mermaid
flowchart TB
    subgraph Drive["Google Drive: MyDrive/Thesis_Project/code/"]
        C[common.py<br/>paths, alignment check,<br/>quarantine mechanism]
    end

    subgraph N1["N1: Acquire and Validate (CPU-only)"]
        N1a[Pull dataset] --> N1b[Alignment / quarantine checks] --> N1c[Build window index]
    end

    subgraph N2["N2: Visual Features (GPU)"]
        N2a[Load validated windows] --> N2b[ResNet-18 extraction]
    end

    subgraph N3["N3: Game-State Features"]
        N3a[Load GSR data] --> N3b[Build game-state feature representation]
    end

    subgraph N4["N4: Fusion and Baselines"]
        N4a[Combine visual + game-state features] --> N4b[Train / evaluate B0-B5]
    end

    C -.imported by.-> N1
    C -.imported by.-> N2
    C -.imported by.-> N3
    C -.imported by.-> N4

    N1c --> N2a
    N1c --> N3a
    N2b --> N4a
    N3b --> N4a
```

## Reading this diagram

`common.py` is imported by all four notebooks rather than duplicated.
N1 is CPU-only per the Gate H result and must complete and checkpoint
before N2's GPU session starts, per the project's existing Colab
workflow convention.
