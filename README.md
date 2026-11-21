# Public CI/CD execution endpoint

This repository contains only a minimal GitHub Actions runner wrapper.
All source code, libraries, decoders/decompilers, tests, fixtures, and orchestration
remain exclusively in the private `vladleopold/3Spine-core` repository.

The ephemeral GitHub-hosted runner checks out only the required private paths at
runtime. No source files are committed to this public repository and no source
archive or source-code artifact is uploaded here.

Required Actions secret: `SOURCE_REPO_TOKEN` with read-only access to
`vladleopold/3Spine-core`.

Dispatch payloads must contain task identifiers only, never source files,
credentials, PSD bytes, library contents, or private implementation details.
