
# SECAF v1.1 Risk Calculator
# Smart Energy Cybersecurity Assessment Framework

from pathlib import Path
import re
# SECAF v1.2 Risk Assessment Rating Definitions

LIKELIHOOD_RATINGS = {
    1: "Rare",
    2: "Unlikely",
    3: "Possible",
    4: "Likely",
    5: "Almost Certain",
}

IMPACT_RATINGS = {
    1: "Negligible",
    2: "Minor",
    3: "Moderate",
    4: "Major",
    5: "Critical",
}


def calculate_risk(likelihood, impact):
    """Calculate a risk score and classify it."""

    if (
        type(likelihood) is not int
        or type(impact) is not int
        or not 1 <= likelihood <= 5
        or not 1 <= impact <= 5
    ):
        raise ValueError(
            "Likelihood and impact must be integers between 1 and 5."
        )

    score = likelihood * impact

    if score <= 4:
        level = "Low"
    elif score <= 9:
        level = "Medium"
    elif score <= 16:
        level = "High"
    else:
        level = "Critical"

    return score, level


def main():
    print("\nSECAF v1.1 Risk Calculator")
    print("-----------------------------------")

    finding_id = input("Enter Finding ID (example F-01): ").strip()
    checklist_id = input(
        "Enter Checklist Reference (example AC-01): "
    ).strip()
    finding = input("Briefly describe the finding: ").strip()
    recommendation = input("Enter recommended action: ").strip()

    if not re.fullmatch(r"[A-Za-z0-9_-]{1,40}", finding_id):
        print(
            "\nError: Finding ID must contain only letters, "
            "numbers, hyphens or underscores (maximum 40 characters)."
        )
        return

    try:
        likelihood = int(input("Enter Likelihood (1-5): "))
        impact = int(input("Enter Impact (1-5): "))

        score, level = calculate_risk(likelihood, impact)

    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\nSECAF Assessment Result")
    print("-----------------------------------")
    print(f"Finding ID: {finding_id}")
    print(f"Checklist Reference: {checklist_id}")
    print(f"Finding: {finding}")
    print(f"Likelihood: {likelihood}")
    print(f"Impact: {impact}")
    print(f"Risk Score: {score}")
    print(f"Risk Level: {level}")
    print(f"Recommended Action: {recommendation}")

    report = f"""# SECAF Assessment Finding

## Finding Information

**Finding ID:** {finding_id}

**Checklist Reference:** {checklist_id}

**Finding:**

{finding}

## Risk Assessment

**Likelihood:** {likelihood}/5

**Impact:** {impact}/5

**Risk Score:** {score}

**Risk Level:** {level}

## Recommended Action

{recommendation}

---

Generated using the SECAF v1.1 Risk Calculator.
"""

    filename = f"{finding_id.lower()}-assessment.md"
    report_path = Path(filename)

    try:
        with report_path.open("x", encoding="utf-8") as file:
            file.write(report)
    except FileExistsError:
        print(
            f"\nError: {filename} already exists. "
            "Use a different Finding ID to avoid overwriting it."
        )
        return
    except OSError as error:
        print(f"\nError saving report: {error}")
        return

    print(f"\nAssessment report saved as: {filename}")


if __name__ == "__main__":
    main()
