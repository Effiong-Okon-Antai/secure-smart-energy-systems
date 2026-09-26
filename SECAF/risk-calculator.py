# SECAF v1.0 Risk Calculator
# Smart Energy Cybersecurity Assessment Framework


def calculate_risk(likelihood, impact):
    """Calculate the SECAF risk score and risk level."""

    risk_score = likelihood * impact

    if risk_score <= 4:
        risk_level = "Low"
    elif risk_score <= 9:
        risk_level = "Medium"
    elif risk_score <= 16:
        risk_level = "High"
    else:
        risk_level = "Critical"

    return risk_score, risk_level


print("\nSECAF v1.0 Risk Calculator")
print("-----------------------------------")

finding_id = input("Enter Finding ID (example F-01): ").strip()
checklist_id = input("Enter Checklist Reference (example AC-01): ").strip()
finding = input("Briefly describe the finding: ").strip()
recommendation = input("Enter recommended action: ").strip()

try:
    likelihood = int(input("Enter Likelihood (1-5): "))
    impact = int(input("Enter Impact (1-5): "))

    if likelihood not in range(1, 6) or impact not in range(1, 6):
        print("\nError: Likelihood and Impact must be between 1 and 5.")

    else:
        score, level = calculate_risk(likelihood, impact)

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

Generated using the SECAF v1.0 Risk Calculator.
"""

        filename = f"{finding_id.lower()}-assessment.md"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)

        print(f"\nAssessment report saved as: {filename}")

except ValueError:
    print("\nError: Please enter numbers between 1 and 5 for Likelihood and Impact.")
