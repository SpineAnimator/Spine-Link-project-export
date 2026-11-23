# Public CI/CD execution endpoint

This repository contains only a minimal GitHub Actions runner wrapper.
All private source code, libraries, tests, fixtures, and orchestration remain in their
respective private source repositories. Public workflows contain orchestration only.

The ephemeral GitHub-hosted runner checks out only the required private paths at
runtime. No source files are committed to this public repository and no source
archive or source-code artifact is uploaded here.

Required Actions secret: `SOURCE_REPO_TOKEN` with read-only access to
`SpineAnimator/spine-animator-private` for the SAPS acceptance workflow (and any other source repository explicitly configured by a workflow).

Dispatch payloads must contain task identifiers only, never source files,
credentials, PSD bytes, library contents, or private implementation details.


## SAPS v7.54 public Ubuntu acceptance

The workflow `.github/workflows/saps-v754-public-ubuntu.yml` runs the SAPS acceptance matrix on GitHub-hosted `ubuntu-24.04` runners. Four independent jobs validate PSD parsing/rasterization, v7.54 export semantics, AI source-readiness contracts, and Spine 4.3 package invariants; a fifth job joins their results.

The runner repository intentionally contains **no private source code or customer PSDs**. Each job checks out the requested ref from `SpineAnimator/spine-animator-private` at runtime using the repository Actions secret `SOURCE_REPO_TOKEN`, which must have read-only access to that private repository. The token is never printed and checkout credentials are not persisted.

- Push to branch `task/saps-v754-public-ubuntu-acceptance` runs the acceptance workflow.
- Manual runs can select a private branch, tag or commit SHA using `workflow_dispatch`.
- The default source ref is `feature/saps-v754-parallel-integration-20261123`.
- If `SOURCE_REPO_TOKEN` is missing or lacks access, the jobs stop with a clear configuration error.
- This is source-level Linux validation; it does not certify Photoshop pixel parity, a native Spine Editor GUI import, or visual AI approval.
