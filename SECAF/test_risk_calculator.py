
# SECAF v1.1 Automated Risk Calculator Tests
# Smart Energy Cybersecurity Assessment Framework

import unittest
import importlib.util
from pathlib import Path


# Load the calculator because its filename contains a hyphen.
calculator_path = Path(__file__).resolve().parent / "risk-calculator.py"

spec = importlib.util.spec_from_file_location(
    "secaf_risk_calculator",
    calculator_path
)

calculator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculator)

calculate_risk = calculator.calculate_risk


class TestSECAFRiskCalculator(unittest.TestCase):

    def test_low_risk(self):
        self.assertEqual(calculate_risk(1, 1), (1, "Low"))
        self.assertEqual(calculate_risk(2, 2), (4, "Low"))

    def test_medium_risk(self):
        self.assertEqual(calculate_risk(1, 5), (5, "Medium"))
        self.assertEqual(calculate_risk(3, 3), (9, "Medium"))

    def test_high_risk(self):
        self.assertEqual(calculate_risk(2, 5), (10, "High"))
        self.assertEqual(calculate_risk(4, 4), (16, "High"))

    def test_critical_risk(self):
        self.assertEqual(calculate_risk(5, 4), (20, "Critical"))
        self.assertEqual(calculate_risk(5, 5), (25, "Critical"))

    def test_invalid_low_values(self):
        with self.assertRaises(ValueError):
            calculate_risk(0, 3)

        with self.assertRaises(ValueError):
            calculate_risk(3, 0)

    def test_invalid_high_values(self):
        with self.assertRaises(ValueError):
            calculate_risk(6, 3)

        with self.assertRaises(ValueError):
            calculate_risk(3, 6)

    def test_invalid_data_types(self):
        with self.assertRaises(ValueError):
            calculate_risk("High", 3)

        with self.assertRaises(ValueError):
            calculate_risk(3, "Low")

        with self.assertRaises(ValueError):
            calculate_risk(2.5, 3)

    def test_all_valid_combinations(self):
        for likelihood in range(1, 6):
            for impact in range(1, 6):

                score, level = calculate_risk(likelihood, impact)

                self.assertEqual(score, likelihood * impact)

                if score <= 4:
                    expected_level = "Low"
                elif score <= 9:
                    expected_level = "Medium"
                elif score <= 16:
                    expected_level = "High"
                else:
                    expected_level = "Critical"

                self.assertEqual(level, expected_level)

    def test_likelihood_rating_definitions(self):
        expected = {
            1: "Rare",
            2: "Unlikely",
            3: "Possible",
            4: "Likely",
            5: "Almost Certain",
        }

        self.assertEqual(
            calculator.LIKELIHOOD_RATINGS,
            expected
        )

    def test_impact_rating_definitions(self):
        expected = {
            1: "Negligible",
            2: "Minor",
            3: "Moderate",
            4: "Major",
            5: "Critical",
        }

        self.assertEqual(
            calculator.IMPACT_RATINGS,
            expected
        )
        
if __name__ == "__main__":
    unittest.main()
