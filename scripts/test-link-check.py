import subprocess
import unittest


class LinkCheckScopeTest(unittest.TestCase):
    def test_excludes_draft_content(self):
        result = subprocess.run(
            ["python3", "scripts/link-check.py"],
            capture_output=True,
            check=False,
            text=True,
        )

        self.assertNotIn("drafts/", result.stdout)


if __name__ == "__main__":
    unittest.main()
