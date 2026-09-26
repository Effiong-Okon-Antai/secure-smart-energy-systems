# SECAF v1.0 — Control Reference

## About This Reference

This page provides a quick overview of the security areas covered by SECAF v1.0.

Each assessment check has a unique reference ID. These IDs can be used when recording findings in the SECAF assessment template.

| Prefix | Assessment Area | What It Covers |
|---|---|---|
| AC | Authentication and Access Control | Passwords, user accounts, administrator access and MFA |
| NS | Network Security | Wi-Fi, routers, network separation, services and network access |
| RC | Remote Access and Cloud Security | Remote management, cloud accounts, permissions and cloud communication |
| FS | Firmware and Software Security | Updates, support status, firmware versions and outdated components |
| DP | Data Protection and Privacy | Data collection, storage, access and sharing |
| ML | Security Monitoring and Logging | Login records, alerts, configuration changes and unusual activity |
| PS | Physical Security and Local Access | Physical access to equipment, gateways, routers and interfaces |
| BR | Backup, Recovery and Incident Response | Configuration recovery, compromised accounts and incident handling |

---

## Using the Reference IDs

If a security issue is identified, the relevant checklist ID should be included in the assessment finding.

For example:

**AC-01** refers to the check asking whether default usernames and passwords have been changed.

A finding can therefore be recorded as:

**Finding ID:** F-01  
**Checklist Reference:** AC-01

This makes it easier to trace a finding back to the original security check.

For the complete list of assessment checks, see the [SECAF Cybersecurity Assessment Checklist](assessment-checklist.md).
