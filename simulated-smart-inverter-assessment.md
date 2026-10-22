
# SECAF v1.1 — Simulated Smart Inverter Cybersecurity Assessment

**Framework:** Smart Energy Cybersecurity Assessment Framework (SECAF)  
**Assessment Type:** Simulated cybersecurity risk assessment  
**Assessment Date:** 22 October 2026  
**Assessment Status:** Illustrative scenario — not a live security test

## 1. Assessment Overview

This assessment demonstrates the application of SECAF v1.1
to a fictional smart energy installation.

The simulated environment includes a hybrid solar inverter,
lithium battery storage, a Wi-Fi monitoring dongle,
a local wireless network, and a cloud-connected
mobile monitoring application.

The purpose is to identify potential cybersecurity risks,
assign likelihood and impact scores, and recommend
appropriate security controls.

No real customer systems, manufacturer infrastructure,
or operational energy equipment were tested.

## 2. Simulated System Architecture

The fictional system consists of:

1. A 6 kW hybrid solar inverter
2. A connected lithium battery storage system
3. A Wi-Fi monitoring dongle
4. A local wireless router
5. An internet-connected monitoring platform
6. A mobile application used for remote monitoring

Illustrative communication path:

Smart Inverter
    |
Wi-Fi Monitoring Dongle
    |
Local Wireless Router
    |
Internet / Cloud Monitoring Platform
    |
Mobile Monitoring Application

The architecture is hypothetical and does not represent
a verified implementation of any particular manufacturer's
product.

## 3. Assessment Methodology

The assessment follows the SECAF methodology:

1. Identify connected system components.
2. Identify potential threats and vulnerabilities.
3. Estimate the likelihood of each scenario.
4. Estimate its potential impact.
5. Calculate risk using likelihood multiplied by impact.
6. Classify risk according to SECAF thresholds.
7. Recommend security controls.
8. Document findings and residual uncertainties.

### Risk Classification

| Risk Score | Risk Level |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

Likelihood and impact are each rated from 1 to 5.

The numerical ratings in this assessment are illustrative
assumptions, not measurements from real-world testing.

## 4. Simulated Security Findings

### Finding F-01 — Weak Monitoring Account Authentication

**Scenario:**

The fictional monitoring application uses a weak password
and does not enforce multifactor authentication.

**Potential Threat:**

An unauthorised person could gain access to monitoring
information or available account functions.

**Likelihood:** 4/5  
**Impact:** 4/5

**Risk Score:** 16  
**Risk Level:** High

**Recommended Controls:**

- Use strong, unique account passwords.
- Enable multifactor authentication where supported.
- Restrict account sharing.
- Review active sessions and account permissions.
- Monitor for suspicious login activity.

### Finding F-02 — Insecure Wi-Fi Configuration

**Scenario:**

The monitoring dongle connects through a wireless network
using outdated or weak security settings.

**Potential Threat:**

An attacker within wireless range could attempt
unauthorised network access.

**Likelihood:** 3/5  
**Impact:** 4/5

**Risk Score:** 12  
**Risk Level:** High

**Recommended Controls:**

- Use WPA2-AES or WPA3 where supported.
- Disable insecure wireless authentication methods.
- Change default router credentials.
- Separate energy monitoring devices from guest networks.
- Keep network equipment updated.

### Finding F-03 — Outdated Monitoring Device Firmware

**Scenario:**

The fictional monitoring dongle runs outdated firmware.

**Potential Threat:**

Known vulnerabilities could remain unpatched,
increasing exposure to unauthorised access
or service disruption.

**Likelihood:** 3/5  
**Impact:** 5/5

**Risk Score:** 15  
**Risk Level:** High

**Recommended Controls:**

- Check for vendor-supported firmware updates.
- Verify firmware authenticity.
- Follow documented update procedures.
- Restrict unnecessary network access.
- Maintain a device and firmware inventory.

### Finding F-04 — Excessive Monitoring Account Permissions

**Scenario:**

Multiple users share an account with more permissions
than they require.

**Potential Threat:**

Account misuse or compromise could expose
monitoring data or configuration functions.

**Likelihood:** 3/5  
**Impact:** 3/5

**Risk Score:** 9  
**Risk Level:** Medium

**Recommended Controls:**

- Use separate accounts where supported.
- Apply least-privilege access.
- Review account permissions regularly.
- Remove access when no longer required.
- Enable audit logging where available.

### Finding F-05 — Inadequate Network Segmentation

**Scenario:**

The inverter monitoring dongle shares the same network
as personal computers and other household devices.

**Potential Threat:**

A compromised device could increase the exposure
of other connected systems.

**Likelihood:** 4/5  
**Impact:** 5/5

**Risk Score:** 20  
**Risk Level:** Critical

**Recommended Controls:**

- Place energy monitoring devices on a dedicated
  network segment where practical.
- Restrict communication between network segments.
- Permit only required outbound connections.
- Review firewall and router settings.
- Monitor unusual network activity.

## 5. Risk Assessment Summary

| Finding | Risk Scenario | Likelihood | Impact | Score | Level |
|---|---|---:|---:|---:|---|
| F-01 | Weak authentication | 4 | 4 | 16 | High |
| F-02 | Insecure Wi-Fi configuration | 3 | 4 | 12 | High |
| F-03 | Outdated firmware | 3 | 5 | 15 | High |
| F-04 | Excessive permissions | 3 | 3 | 9 | Medium |
| F-05 | Inadequate network segmentation | 4 | 5 | 20 | Critical |

### Summary

- Critical risks: 1
- High risks: 3
- Medium risks: 1
- Low risks: 0
- Total simulated findings: 5

## 6. Risk Prioritisation

The fictional network segmentation weakness (F-05)
has the highest assigned risk score.

It should therefore receive priority in this
illustrative remediation plan.

The remaining High risks should be addressed
according to the system owner's operational
requirements and applicable security policies.

## 7. Assessment Limitations

This is a scenario-based demonstration.

The assessment does not include:

- Live penetration testing
- Firmware reverse engineering
- Vulnerability scanning of real equipment
- Verification of manufacturer security controls
- Testing of a production monitoring application
- Measurements of actual attack likelihood
- Validation of the assigned risk scores against incidents

The findings demonstrate how SECAF can structure
risk assessment decisions. They are not evidence
that any real PRAG or third-party product contains
the described weaknesses.

## 8. Future Validation

Future work may include:

1. Developing an isolated smart-energy IoT test environment.
2. Using authorised test devices or simulated components.
3. Comparing SECAF assessments against established
   cybersecurity guidance.
4. Evaluating the consistency of risk ratings.
5. Extending automated assessment report generation.

## 9. Conclusion

This simulated assessment demonstrates the application
of SECAF v1.1 to a fictional connected smart-energy system.

Five hypothetical security scenarios were documented
using structured likelihood, impact, risk scoring,
and recommended controls.

The assessment illustrates the framework's intended
workflow but does not establish its effectiveness
against real-world attacks or vulnerabilities.

---

**Project:** Secure Smart Energy Systems  
**Framework:** SECAF v1.1  
**Author:** Effiong Okon Antai  
**Repository:** https://github.com/Effiong-Okon-Antai/secure-smart-energy-systems
