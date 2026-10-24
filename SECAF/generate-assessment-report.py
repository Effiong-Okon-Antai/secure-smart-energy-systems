
"""
SECAF v1.1 — Automated Assessment Report Generator

Reads simulated-assessment.json, calculates risk scores,
and generates a Markdown cybersecurity assessment report.

This demonstration uses fictional security scenarios.
"""

import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "simulated-assessment.json"
OUTPUT_FILE = BASE_DIR / "generated-assessment-report.md"
CALCULATOR_FILE = BASE_DIR / "risk-calculator.py"


def load_calculator():
    spec = importlib.util.spec_from_file_location(
        "secaf_calculator",
        CALCULATOR_FILE
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module.calculate_risk


def generate_report():
    calculate_risk = load_calculator()

    with INPUT_FILE.open("r", encoding="utf-8") as file:
        assessment = json.load(file)

    findings = assessment["findings"]

    if not findings:
        raise ValueError("Assessment must contain at least one finding.")

    risk_counts = {
        "Low": 0,
        "Medium": 0,
        "High": 0,
        "Critical": 0
    }

    lines = [
        "# SECAF Automated Cybersecurity Assessment Report",
        "",
        f"**Framework:** {assessment['framework']}",
        f"**Version:** {assessment['version']}",
        f"**Assessment:** {assessment['assessment_type']}",
        f"**Assessment Date:** {assessment['assessment_date']}",
        f"**Environment:** {assessment['environment']}",
        "",
        f"**Disclaimer:** {assessment['disclaimer']}",
        "",
            "## 1. Executive Summary",
        "",
        "### Assessment Background",
        "",
        "This cybersecurity assessment demonstrates the application "
        "of the Smart Energy Cybersecurity Assessment Framework "
        "(SECAF) to a simulated hybrid solar energy environment.",
        "",
        "The fictional environment includes a hybrid inverter, "
        "lithium battery storage, a Wi-Fi monitoring dongle, "
        "a wireless router, a cloud monitoring platform, "
        "and a mobile application.",
        "",
        "### Assessment Objectives",
        "",
        "The objectives of this assessment are to:",
        "",
        "- Identify hypothetical cybersecurity weaknesses "
        "affecting connected smart energy systems.",
        "- Evaluate potential security risks using structured "
        "likelihood and impact ratings.",
        "- Calculate and classify cybersecurity risks "
        "using the SECAF risk-scoring methodology.",
        "- Recommend appropriate security controls "
        "and risk mitigation measures.",
        "- Demonstrate automated cybersecurity assessment "
        "report generation.",
        "",
        "### Assessment Scope",
        "",
        f"The assessment covers {len(findings)} hypothetical "
        "security findings involving authentication, "
        "wireless network security, firmware management, "
        "access permissions, and network segmentation.",
        "",
        "### Risk Assessment Method",
        "",
        "Each finding is assigned a likelihood score "
        "and an impact score ranging from 1 to 5.",
        "",
        "**Risk Score = Likelihood × Impact**",
        "",
        "The resulting score is classified as Low, Medium, "
        "High, or Critical according to SECAF thresholds.",
        "",
        "### Important Limitation",
        "",
        "This is a simulated assessment. No real inverter, "
        "customer system, or manufacturer infrastructure "
        "was tested. All findings and ratings are illustrative.",
        "",
        "## 2. Risk Assessment Results",
        "",
        "| ID | Finding | Likelihood | Impact | Score | Risk Level |",
        "|---|---|---:|---:|---:|---|"
    ]

    results = []
    seen_ids = set()

    for finding in findings:
        finding_id = finding["id"]

        if finding_id in seen_ids:
            raise ValueError(
                f"Duplicate finding ID: {finding_id}"
            )

        seen_ids.add(finding_id)

        score, level = calculate_risk(
            finding["likelihood"],
            finding["impact"]
        )

        if score != finding["expected_score"]:
            raise ValueError(
                f"Score mismatch for {finding_id}"
            )

        if level != finding["expected_level"]:
            raise ValueError(
                f"Risk level mismatch for {finding_id}"
            )

        risk_counts[level] += 1

        results.append({
            **finding,
            "calculated_score": score,
            "calculated_level": level
        })

        title = finding["title"].replace("|", "\\|")

        lines.append(
            f"| {finding_id} | {title} | "
            f"{finding['likelihood']} | "
            f"{finding['impact']} | "
            f"{score} | {level} |"
        )

    lines.extend([
        "",
        "## 3. Risk Distribution",
        "",
        f"- Critical: {risk_counts['Critical']}",
        f"- High: {risk_counts['High']}",
        f"- Medium: {risk_counts['Medium']}",
        f"- Low: {risk_counts['Low']}",
        "",
        "## 4. Detailed Findings",
        ""
    ])

    for result in results:

        security_scenarios = {
            "F-01": {
                "scenario": (
                    "The fictional smart inverter monitoring account "
                    "uses weak authentication controls."
                ),
                "impact": (
                    "Unauthorised access could expose monitoring "
                    "information or available account functions."
                ),
                "controls": [
                    "Use strong, unique passwords.",
                    "Enable multifactor authentication where supported.",
                    "Review account access and permissions.",
                    "Monitor suspicious login activity."
                ]
            },
            "F-02": {
                "scenario": (
                    "The fictional Wi-Fi monitoring device connects "
                    "through a wireless network with weak security settings."
                ),
                "impact": (
                    "An attacker within wireless range could attempt "
                    "unauthorised access to the local network."
                ),
                "controls": [
                    "Use WPA2-AES or WPA3 where supported.",
                    "Change default router credentials.",
                    "Disable insecure wireless authentication methods.",
                    "Keep router firmware updated."
                ]
            },
            "F-03": {
                "scenario": (
                    "The fictional inverter monitoring dongle "
                    "operates with outdated firmware."
                ),
                "impact": (
                    "Unpatched vulnerabilities could increase exposure "
                    "to unauthorised access or service disruption."
                ),
                "controls": [
                    "Check for vendor-supported firmware updates.",
                    "Verify firmware authenticity.",
                    "Restrict unnecessary network access.",
                    "Maintain a firmware inventory."
                ]
            },
            "F-04": {
                "scenario": (
                    "Multiple fictional monitoring users share "
                    "an account with excessive permissions."
                ),
                "impact": (
                    "Account misuse or compromise could expose "
                    "monitoring information or configuration functions."
                ),
                "controls": [
                    "Apply least-privilege access.",
                    "Use separate accounts where supported.",
                    "Review user permissions regularly.",
                    "Remove unnecessary access."
                ]
            },
            "F-05": {
                "scenario": (
                    "The fictional smart inverter monitoring device "
                    "shares a network with household computers "
                    "and other connected devices."
                ),
                "impact": (
                    "A compromised device could increase the exposure "
                    "of other systems connected to the same network."
                ),
                "controls": [
                    "Use a dedicated network segment where practical.",
                    "Restrict communication between network segments.",
                    "Allow only required network connections.",
                    "Monitor unusual network activity."
                ]
            }
        }

        details = security_scenarios.get(result["id"])

        lines.extend([
            f"### {result['id']} — {result['title']}",
            "",
            "#### Risk Assessment",
            "",
            f"**Likelihood:** {result['likelihood']}/5",
            f"**Impact:** {result['impact']}/5",
            f"**Risk Score:** {result['calculated_score']}",
            f"**Risk Level:** {result['calculated_level']}",
            ""
        ])

        if details:
            lines.extend([
                "#### Simulated Security Scenario",
                "",
                details["scenario"],
                "",
                "#### Potential Security Impact",
                "",
                details["impact"],
                "",
                "#### Recommended Security Controls",
                ""
            ])

            for control in details["controls"]:
                lines.append(f"- {control}")

            lines.append("")

        lines.extend([
            "#### Primary Recommended Action",
            "",
            result["recommendation"],
            ""
        ])

    highest = max(
        results,
        key=lambda item: item["calculated_score"]
    )

    lines.extend([
        "## 5. Highest-Priority Finding",
        "",
        f"**Finding:** {highest['id']} — {highest['title']}",
        f"**Risk Score:** {highest['calculated_score']}",
        f"**Risk Level:** {highest['calculated_level']}",
        "",
        "## 6. Assessment Limitations",
        "",
        "This report is based entirely on fictional scenarios.",
        "It does not represent a penetration test, live "
        "vulnerability assessment, or independent security audit.",
        "",
        "The risk ratings are illustrative assumptions.",
        "",
        "---",
        "",
        "Generated using SECAF v1.1.",
        "",
        f"**Generated (UTC):** "
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}",
        ""
    ])

    OUTPUT_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print("SECAF assessment report generated successfully.")
    print(f"Findings processed: {len(results)}")
    print(f"Highest risk: {highest['id']} ({highest['calculated_level']})")
    print(f"Report saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_report()
