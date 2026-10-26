
"""
SECAF v1.1 — Automated Simulated Assessment Verification

Reads findings from simulated-assessment.json and checks
their risk scores using the SECAF risk calculator.

All scenarios are hypothetical.
"""

import importlib.util
import json
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

CALCULATOR_PATH = BASE_DIR / "SECAF" / "risk-calculator.py"
ASSESSMENT_PATH = BASE_DIR / "SECAF" / "simulated-assessment.json"

# Import the existing SECAF risk calculator.
spec = importlib.util.spec_from_file_location(
    "secaf_calculator",
    CALCULATOR_PATH
)

calculator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculator)

calculate_risk = calculator.calculate_risk


class TestSimulatedAssessment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with ASSESSMENT_PATH.open(
            "r",
            encoding="utf-8"
        ) as file:
            cls.assessment = json.load(file)

        cls.findings = cls.assessment["findings"]

    def test_assessment_contains_five_findings(self):
        self.assertEqual(len(self.findings), 5)

    def test_unique_finding_ids(self):
        finding_ids = [
            finding["id"]
            for finding in self.findings
        ]

        self.assertEqual(
            len(finding_ids),
            len(set(finding_ids))
        )

    def test_all_risk_scores_and_levels(self):
        for finding in self.findings:
            with self.subTest(finding=finding["id"]):
                score, level = calculate_risk(
                    finding["likelihood"],
                    finding["impact"]
                )

                self.assertEqual(
                    score,
                    finding["expected_score"]
                )

                self.assertEqual(
                    level,
                    finding["expected_level"]
                )

    def test_risk_category_distribution(self):
        distribution = {
            "Low": 0,
            "Medium": 0,
            "High": 0,
            "Critical": 0
        }

        for finding in self.findings:
            _, level = calculate_risk(
                finding["likelihood"],
                finding["impact"]
            )

            distribution[level] += 1

        self.assertEqual(
            distribution,
            {
                "Low": 0,
                "Medium": 1,
                "High": 3,
                "Critical": 1
            }
        )

    def test_highest_priority_finding(self):
        highest = max(
            self.findings,
            key=lambda finding: calculate_risk(
                finding["likelihood"],
                finding["impact"]
            )[0]
        )

        self.assertEqual(highest["id"], "F-05")
        self.assertEqual(highest["expected_score"], 20)

    def test_required_assessment_fields(self):
        required_fields = [
            "id",
            "title",
            "likelihood",
            "impact",
            "expected_score",
            "expected_level",
            "recommendation"
        ]

        for finding in self.findings:
            with self.subTest(finding=finding.get("id")):
                for field in required_fields:
                    self.assertIn(field, finding)

    def test_assessment_is_identified_as_simulated(self):
        self.assertIn(
            "Simulated",
            self.assessment["assessment_type"]
        )

        self.assertIn(
            "Hypothetical",
            self.assessment["disclaimer"]
        )


if __name__ == "__main__":
    unittest.main()
