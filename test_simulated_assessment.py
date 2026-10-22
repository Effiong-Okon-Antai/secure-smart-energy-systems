
# SECAF v1.1 Simulated Assessment Verification
# Smart Energy Cybersecurity Assessment Framework

import importlib.util
import unittest
from pathlib import Path


CALCULATOR_PATH = (
    Path(__file__).resolve().parent / "risk-calculator.py"
)

spec = importlib.util.spec_from_file_location(
    "secaf_calculator",
    CALCULATOR_PATH
)

calculator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculator)

calculate_risk = calculator.calculate_risk


# Expected findings from the simulated assessment document.
# These are hypothetical scenario ratings, not live measurements.
SIMULATED_FINDINGS = [
    ("F-01", "Weak authentication", 4, 4, 16, "High"),
    ("F-02", "Insecure Wi-Fi configuration", 3, 4, 12, "High"),
    ("F-03", "Outdated firmware", 3, 5, 15, "High"),
    ("F-04", "Excessive permissions", 3, 3, 9, "Medium"),
    ("F-05", "Inadequate network segmentation", 4, 5, 20, "Critical"),
]


class TestSimulatedAssessment(unittest.TestCase):

    def test_all_simulated_findings(self):
        for finding_id, name, likelihood, impact, score, level in SIMULATED_FINDINGS:
            with self.subTest(finding=finding_id):
                actual_score, actual_level = calculate_risk(
                    likelihood,
                    impact
                )

                self.assertEqual(
                    actual_score,
                    score,
                    f"Incorrect risk score for {finding_id}: {name}"
                )

                self.assertEqual(
                    actual_level,
                    level,
                    f"Incorrect risk level for {finding_id}: {name}"
                )

    def test_risk_category_distribution(self):
        categories = {
            "Low": 0,
            "Medium": 0,
            "High": 0,
            "Critical": 0,
        }

        for finding in SIMULATED_FINDINGS:
            likelihood = finding[2]
            impact = finding[3]

            _, level = calculate_risk(likelihood, impact)
            categories[level] += 1

        self.assertEqual(categories["Low"], 0)
        self.assertEqual(categories["Medium"], 1)
        self.assertEqual(categories["High"], 3)
        self.assertEqual(categories["Critical"], 1)

    def test_highest_priority_finding(self):
        highest = max(
            SIMULATED_FINDINGS,
            key=lambda finding: calculate_risk(
                finding[2],
                finding[3]
            )[0]
        )

        self.assertEqual(highest[0], "F-05")
        self.assertEqual(highest[4], 20)


if __name__ == "__main__":
    unittest.main()
