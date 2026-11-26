from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "runner.yml"


class PublicRunnerContractTests(unittest.TestCase):
    def test_project_export_workflow_runs_only_on_public_ubuntu_24_04(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("self-hosted", source)
        self.assertGreaterEqual(source.count("runs-on: ubuntu-24.04"), 3)

    def test_reusable_runner_probe_checks_out_its_own_public_repository(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        probe = source.split("  runner-probe:", 1)[1].split("  execute-source-contracts:", 1)[0]
        self.assertIn("repository: SpineAnimator/Spine-Link-project-export", probe)
        self.assertIn("ref: main", probe)

    def test_public_runner_checks_storage_write_scope_without_printing_token(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("SPINE_LINK_STORAGE_WRITE_PERMISSION_MISSING", source)
        self.assertIn("repos/vladleopold/spine", source)
        self.assertIn(".permissions.push", source)
        self.assertIn('GH_TOKEN="$STORAGE_GITHUB_TOKEN"', source)
        self.assertNotIn('GH_TOKEN="$SOURCE_REPO_TOKEN"', source)

    def test_public_runner_polls_the_export_queue_every_five_minutes(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("schedule:", source)
        self.assertIn("cron: '*/5 * * * *'", source)

    def test_licensed_export_job_is_delegated_to_public_runner(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("licensed-project-export:", source)
        self.assertIn("SOURCE_REPO_TOKEN", source)
        self.assertIn("STORAGE_GITHUB_TOKEN", source)
        self.assertNotIn("secrets.ACCESS_TOKEN", source)
        self.assertIn("SPINE_LICENSE", source)
        self.assertIn("SPINE_LINUX_URL", source)
        self.assertIn("SPINE_LINK_LICENSED_EXPORT_WAITING_FOR_SECRETS", source)
        self.assertIn("scripts/spine-link-project-cloud-export.mjs", source)
        self.assertIn("SPINE_UPLOAD_ID", source)
        self.assertIn("timeout 180 xvfb-run", source)
        self.assertNotIn(".github/workflows/spine-link-project-export.yml", source)

    def test_last7_reusable_audit_checks_private_source_from_public_runner(self):
        source = (ROOT / ".github" / "workflows" / "last7-real-preview.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_call:", source)
        self.assertIn("source-repository:", source)
        self.assertIn("source-ref:", source)
        self.assertIn("secrets.SOURCE_REPO_TOKEN", source)
        self.assertIn("runs-on: ubuntu-24.04", source)
        self.assertEqual(source.count("repository: ${{ inputs.source-repository }}"), 2)

    def test_reusable_workflow_uses_caller_token_for_private_source_and_optional_license_secrets(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        call = source.split("workflow_call:", 1)[1].split("  pull_request:", 1)[0]
        self.assertNotIn("SOURCE_REPO_TOKEN:", call)
        self.assertIn("github.repository == 'vladleopold/3Spine-core' && github.token", source)
        for secret in ("STORAGE_GITHUB_TOKEN", "SPINE_LICENSE", "SPINE_LINUX_URL"):
            self.assertRegex(call, rf"(?s){secret}:\s*required: false")
        self.assertRegex(call, r"(?s)upload_id:.*?type: string")




if __name__ == "__main__":
    unittest.main()
