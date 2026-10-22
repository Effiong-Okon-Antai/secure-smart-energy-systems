#  Securing Smart Energy Systems (Inverters, Batteries & Solar)


[![SECAF Automated Tests](https://github.com/Effiong-Okon-Antai/secure-smart-energy-systems/actions/workflows/secaf-tests.yml/badge.svg)](https://github.com/Effiong-Okon-Antai/secure-smart-energy-systems/actions/workflows/secaf-tests.yml)

### SECAF Automated Validation

The Smart Energy Cybersecurity Assessment Framework (SECAF)
includes automated Python tests executed through GitHub Actions.

The test suite covers:

- Risk calculation and classification
- Input validation and risk scoring boundaries
- Markdown assessment report generation
- Report filename validation and overwrite protection
- Verification of five hypothetical smart inverter security findings

**Test suite:** 15 automated tests, subject to the latest workflow results.

**Testing documentation:** [SECAF Testing](SECAF/TESTING.md)

**Simulated assessment:** [Smart Inverter Cybersecurity Assessment](SECAF/simulated-smart-inverter-assessment.md)

These tests verify implemented software behaviour and illustrative
risk calculations. They do not constitute independent cybersecurity
certification or testing of real smart-energy equipment.

##  Project Overview
Modern energy systems such as solar inverters, lithium battery storage, and hybrid power solutions are no longer isolated hardware systems. They are increasingly integrated with mobile applications, cloud-based platforms, and remote monitoring tools.

This project explores the cybersecurity risks associated with these connected energy systems and provides practical recommendations for securing them in real-world deployments.

---

##  System Architecture 

![Smart Energy System Architecture](architecture-diagram.png)

---

##  Key Components

- **Inverter Systems** (WiFi-enabled / app-controlled)
- **Battery Management Systems (BMS)**
- **Cloud Monitoring Platforms**
- **Mobile Applications (Android/iOS)**
- **Home/Enterprise Network Infrastructure**

---

##  Threat Model

### 1. Unauthorized Access
- Default credentials
- Weak authentication mechanisms

### 2. Network-Based Attacks
- Open or poorly secured WiFi networks
- Device discovery via network scanning

### 3. Remote Exploitation
- Misconfigured remote access
- API vulnerabilities in cloud platforms

### 4. Data Exposure
- Energy usage patterns
- System performance data leakage

---

##  Practical Scenario

A residential solar inverter connected to a home WiFi network without proper segmentation or password security may be exposed.

An attacker could:
- Gain unauthorized access  
- Monitor system activity  
- Modify configuration settings  
- Disrupt power delivery  

---

##  Security Recommendations

### Device-Level Security
- Change default credentials immediately
- Enable strong authentication where available

### Network Security
- Use WPA2/WPA3 secured networks
- Segment IoT devices (separate VLAN or guest network)

### System Hardening
- Disable unnecessary remote access
- Keep firmware updated

### Monitoring & Awareness
- Monitor unusual activity
- Limit external access to trusted endpoints only

---

##  Future Improvements

- Integration with intrusion detection systems (IDS)
- Development of a lightweight monitoring script
- Simulation of attack scenarios
- Risk scoring model for smart energy deployments

---

##  Why This Matters

As smart energy systems become part of critical infrastructure, their security becomes essential. The intersection of cybersecurity and energy systems represents a growing field where vulnerabilities can have real-world consequences.

---

##  Author

**Effiong Okon Antai**  
Cybersecurity & Smart Energy Systems  
MSc Cybersecurity – Nottingham Trent University  
