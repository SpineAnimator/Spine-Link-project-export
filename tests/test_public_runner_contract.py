from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "runner.yml"


class PublicRunnerContractTests(unittest.TestCase):
    def test_project_export_workflow_runs_only_on_public_ubuntu_24_04(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("self-hosted", source)
        self.assertGreaterEqual(source.count("runs-on: ubuntu-24.04"), 3)

    def test_public_runner_polls_the_export_queue_every_five_minutes(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("schedule:", source)
        self.assertIn("cron: '*/5 * * * *'", source)

    def test_licensed_export_job_is_delegated_to_public_runner(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("licensed-project-export:", source)
        self.assertIn("SOURCE_REPO_TOKEN", source)
        self.assertIn("ACCESS_TOKEN", source)
        self.assertIn("SPINE_LICENSE", source)
        self.assertIn("SPINE_LINUX_URL", source)
        self.assertIn("SPINE_LINK_LICENSED_EXPORT_WAITING_FOR_SECRETS", source)
        self.assertIn("scripts/spine-link-project-cloud-export.mjs", source)
        self.assertIn("SPINE_UPLOAD_ID", source)
        self.assertIn("timeout 180 xvfb-run", source)


if __name__ == "__main__":
    unittest.main()
