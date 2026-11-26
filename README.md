# Public CI/CD execution endpoint

The current default-branch tree contains only this runner wrapper and this README.
Application source, libraries, decoders/decompilers, tests, fixtures, PSD files,
and orchestration belong exclusively in the private `vladleopold/3Spine-core`
repository and are checked out selectively at runtime.

The ephemeral GitHub-hosted runner checks out only the allow-listed private paths.
No source archive or source-code artifact is intentionally uploaded by this wrapper.

Required Actions secret: `SOURCE_REPO_TOKEN`, a fine-grained token with read-only
Contents access to `vladleopold/3Spine-core`.

Dispatch payloads must contain task identifiers only, never source files,
credentials, PSD bytes, library contents, or private implementation details.

Security note: this describes the current default-branch tree only. Older public
commits and historical Actions logs/artifacts are separate retention surfaces and
must be audited and purged through repository administration before claiming
historical cleanup is complete.
