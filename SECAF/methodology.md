# SECAF v1.0 — Assessment Methodology

## How the Assessment Works

SECAF follows a simple process for reviewing cybersecurity risks in a connected energy system.

The assessment is divided into six stages.

---

## Stage 1 — Define the System

Before starting the assessment, identify what is actually being reviewed.

This may include:

- Solar or hybrid inverter
- Battery storage system
- Battery Management System (BMS)
- Wi-Fi or Ethernet connection
- Router or network equipment
- Monitoring gateway or communication module
- Mobile monitoring application
- Web portal
- Cloud monitoring platform

The assessor should record the equipment and services that are included in the assessment.

---

## Stage 2 — Understand the Connections

Identify how the different parts of the system communicate.

For example:

**Inverter → Wi-Fi/Router → Internet → Cloud Platform → Mobile App**

Also consider connections between the inverter, battery system, monitoring gateway and other devices.

The purpose of this stage is to understand which parts of the energy system depend on digital communication.

---

## Stage 3 — Complete the Security Checklist

Use the SECAF Cybersecurity Assessment Checklist to review the security controls that apply to the system.

The checklist covers:

1. Authentication and Access Control
2. Network Security
3. Remote Access and Cloud Security
4. Firmware and Software Security
5. Data Protection and Privacy
6. Security Monitoring and Logging
7. Physical Security and Local Access
8. Backup, Recovery and Incident Response

Each check should be recorded as:

- Yes
- No
- Partial
- N/A

Notes should be added where further explanation is needed.

---

## Stage 4 — Record Findings

A failed or partially implemented security control does not automatically have the same level of risk in every system.

Where an issue requires further attention, create a finding and record:

- Finding ID
- Checklist reference
- What was observed
- Available evidence
- Likelihood
- Impact
- Recommended action

Sensitive information such as passwords, private keys or authentication tokens should not be included in the assessment record.

---

## Stage 5 — Score the Risk

Use the SECAF Risk Scoring Method for each finding.

Assign:

**Likelihood: 1–5**

**Impact: 1–5**

Then calculate:

**Risk Score = Likelihood × Impact**

The result is classified as:

| Score | Risk Level |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

The score should be based on the actual system and available evidence rather than assumptions.

---

## Stage 6 — Recommend and Track Actions

For each finding, record a practical action that could reduce the identified risk.

Findings can then be tracked using:

- Open
- In Progress
- Resolved
- Accepted

Higher-risk findings can be reviewed first, while the system owner decides how each issue should be handled.

---

## Assessment Principle

SECAF is intended to support structured and repeatable cybersecurity reviews.

It does not guarantee that a connected energy system is secure, and it should not be used as a replacement for manufacturer guidance, professional security testing or established cybersecurity standards.

Assessments should only be carried out on systems that the assessor owns or has permission to review.
