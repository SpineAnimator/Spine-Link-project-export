# Spine-Link project export — public runner

This repository is the dedicated public GitHub Actions execution host for the Spine-Link licensed project export task. The canonical source/orchestration remains in `vladleopold/3Spine-core`; the required runner scripts and tests are mirrored here so the job does not need private-core checkout.

## Runner
- GitHub-hosted `ubuntu-latest`
- Workflow: `.github/workflows/runner.yml`
- Triggers: workflow_dispatch, repository_dispatch, and 5-minute queue polling
- Serial licensed-editor execution via concurrency group

## Required repository secret
- `ACCESS_TOKEN`: read/write access to public storage repository `vladleopold/spine` (queue polling and result upload).
- `SPINE_LICENSE` and `SPINE_LINUX_URL`: licensed Spine Editor 4.3.26 activation and Linux distribution.

The runner-probe job independently confirms that GitHub allocates a Linux runner. The export job cannot process queued user projects until the above credentials are configured in this repository's Actions secrets.
