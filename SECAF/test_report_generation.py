
# SECAF v1.1 Report Generation Tests
# Smart Energy Cybersecurity Assessment Framework

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CALCULATOR = Path(__file__).resolve().parent / "risk-calculator.py"


class TestSECAFReportGeneration(unittest.TestCase):

    def run_calculator(self, inputs, working_directory):
        """Run the interactive calculator with simulated input."""

        return subprocess.run(
            [sys.executable, str(CALCULATOR)],
            input="\n".join(inputs) + "\n",
            text=True,
            capture_output=True,
            cwd=working_directory,
            timeout=10,
            check=False,
        )

    def test_report_created_successfully(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.run_calculator(
                [
                    "F-01",
                    "AC-01",
                    "Insecure remote monitoring access",
                    "Enable strong authentication",
                    "4",
                    "5",
                ],
                temp_dir,
            )

            report_path = Path(temp_dir) / "f-01-assessment.md"

            self.assertEqual(result.returncode, 0)
            self.assertTrue(report_path.is_file())

            report = report_path.read_text(encoding="utf-8")

            self.assertIn("Finding ID:** F-01", report)
            self.assertIn("Checklist Reference:** AC-01", report)
            self.assertIn("Insecure remote monitoring access", report)
            self.assertIn("Risk Score:** 20", report)
            self.assertIn("Risk Level:** Critical", report)
            self.assertIn("Enable strong authentication", report)
            self.assertIn("**Likelihood:** 4/5 (Likely)", report)
            self.assertIn("**Impact:** 5/5 (Critical)", report)

    def test_invalid_risk_does_not_create_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.run_calculator(
                [
                    "F-02",
                    "AC-02",
                    "Invalid likelihood test",
                    "Review assessment",
                    "6",
                    "3",
                ],
                temp_dir,
            )

            self.assertEqual(result.returncode, 0)
            self.assertIn("Error:", result.stdout)
            self.assertFalse(
                (Path(temp_dir) / "f-02-assessment.md").exists()
            )

    def test_invalid_finding_id_does_not_create_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.run_calculator(
                [
                    "../invalid",
                    "AC-03",
                    "Invalid filename test",
                    "Review finding ID",
                ],
                temp_dir,
            )

            self.assertEqual(result.returncode, 0)
            self.assertIn("Error:", result.stdout)
            self.assertEqual(
                list(Path(temp_dir).glob("*-assessment.md")),
                [],
            )

    def test_existing_report_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "f-04-assessment.md"
            report_path.write_text(
                "Existing assessment",
                encoding="utf-8",
            )

            result = self.run_calculator(
                [
                    "F-04",
                    "AC-04",
                    "Duplicate finding",
                    "Review existing report",
                    "3",
                    "3",
                ],
                temp_dir,
            )

            self.assertEqual(result.returncode, 0)
            self.assertIn("already exists", result.stdout)
            self.assertEqual(
                report_path.read_text(encoding="utf-8"),
                "Existing assessment",
            )


if __name__ == "__main__":
    unittest.main()
