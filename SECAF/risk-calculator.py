# SECAF v1.0 Risk Calculator
# Smart Energy Cybersecurity Assessment Framework


def calculate_risk(likelihood, impact):
    """Calculate a SECAF risk score and risk level."""

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


print("SECAF v1.0 Risk Calculator")
print("--------------------------------")

try:
    likelihood = int(input("Enter Likelihood (1-5): "))
    impact = int(input("Enter Impact (1-5): "))

    if likelihood not in range(1, 6) or impact not in range(1, 6):
        print("Error: Likelihood and Impact must be between 1 and 5.")

    else:
        score, level = calculate_risk(likelihood, impact)

        print("\nAssessment Result")
        print("-----------------")
        print(f"Likelihood: {likelihood}")
        print(f"Impact: {impact}")
        print(f"Risk Score: {score}")
        print(f"Risk Level: {level}")

except ValueError:
    print("Error: Please enter numbers between 1 and 5.")
