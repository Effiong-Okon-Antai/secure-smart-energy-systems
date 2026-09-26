# SECAF v1.0 — Cybersecurity Assessment Checklist

## About This Checklist

This checklist is designed to help assess the basic cybersecurity controls around a connected smart energy system.

It can be used to review an installation that includes equipment such as an inverter, battery system, network connection, monitoring device, mobile application or cloud monitoring platform.

For each check, record one of the following:

- **Yes** — the security control is in place
- **No** — the security control is not in place
- **Partial** — the control is only partly implemented
- **N/A** — the check does not apply to the system being assessed

Any issue identified during the assessment should be recorded for further review and, where necessary, included in the SECAF risk assessment.

---

## 1. Authentication and Access Control

| ID | Security Check | Result | Notes |
|---|---|---|---|
| AC-01 | Have default usernames and passwords been changed? |  |  |
| AC-02 | Are strong, unique passwords used for system accounts? |  |  |
| AC-03 | Is multi-factor authentication enabled where supported? |  |  |
| AC-04 | Are administrator accounts limited to people who need them? |  |  |
| AC-05 | Are unused or old user accounts removed or disabled? |  |  |
| AC-06 | Are different users given appropriate levels of access? |  |  |

---

## 2. Network Security

| ID | Security Check | Result | Notes |
|---|---|---|---|
| NS-01 | Is the energy system connected to a secured Wi-Fi or wired network? |  |  |
| NS-02 | Is WPA2 or WPA3 used where the system connects through Wi-Fi? |  |  |
| NS-03 | Has the router's default administrator password been changed? |  |  |
| NS-04 | Are energy and IoT devices separated from other important devices where possible? |  |  |
| NS-05 | Are unnecessary network services and ports disabled or restricted? |  |  |
| NS-06 | Is remote network access restricted to authorised users only? |  |  |
| NS-07 | Are connected energy devices regularly reviewed to identify unknown or unexpected devices? |  |  |

---

## 3. Remote Access and Cloud Security

Many connected energy systems allow users or installers to monitor and manage equipment through mobile apps, web portals or cloud platforms. These features are useful, but access should be properly controlled.

| ID | Security Check | Result | Notes |
|---|---|---|---|
| RC-01 | Is remote access enabled only when it is needed? |  |  |
| RC-02 | Is remote access limited to authorised users? |  |  |
| RC-03 | Are strong, unique passwords used for cloud and remote-access accounts? |  |  |
| RC-04 | Is multi-factor authentication enabled where the platform supports it? |  |  |
| RC-05 | Are former installers, employees or other users removed when they no longer require access? |  |  |
| RC-06 | Is communication with the cloud or remote platform encrypted, where this can be verified? |  |  |
| RC-07 | Are account permissions reviewed to make sure users only have the access they need? |  |  |
| RC-08 | Are security or login notifications enabled where the platform provides them? |  |  |

---

## 4. Firmware and Software Security

Connected inverters, battery systems, gateways and monitoring devices may depend on firmware or software to operate and communicate. Keeping these components updated can help reduce known security risks.

| ID | Security Check | Result | Notes |
|---|---|---|---|
| FS-01 | Is the current firmware or software version known and recorded? |  |  |
| FS-02 | Is the equipment still supported by the manufacturer or supplier? |  |  |
| FS-03 | Are firmware and software updates obtained from trusted or official sources? |  |  |
| FS-04 | Are available security updates reviewed and applied when appropriate? |  |  |
| FS-05 | Is there a process for checking whether important security updates are available? |  |  |
| FS-06 | Are outdated or unsupported components identified for review or replacement? |  |  |
| FS-07 | Are important system settings or configurations recorded before major updates where possible? |  |  |

---

## 5. Data Protection and Privacy

Connected energy systems can collect and transmit information about system performance, energy production, battery status, device information and user accounts. Some systems may also send this information to mobile apps or cloud platforms.

It is important to understand what information is being collected, where it is stored and who can access it.

| ID | Security Check | Result | Notes |
|---|---|---|---|
| DP-01 | Is it clear what system and user data is being collected? |  |  |
| DP-02 | Is it known where the collected data is stored or processed? |  |  |
| DP-03 | Is access to system and user data limited to authorised users? |  |  |
| DP-04 | Is sensitive data protected when transmitted between devices, apps and cloud services, where this can be verified? |  |  |
| DP-05 | Are users aware when system information is shared with a manufacturer, installer or cloud service? |  |  |
| DP-06 | Are unnecessary data-sharing features disabled where possible? |  |  |
| DP-07 | Is there a way to remove or revoke access when a user, installer or service provider no longer needs the data? |  |  |

---

## 6. Security Monitoring and Logging

Security monitoring can help identify unusual access, unexpected configuration changes or other activity that may require investigation.

The monitoring features available will depend on the inverter, battery system, mobile app or cloud platform being assessed.

| ID | Security Check | Result | Notes |
|---|---|---|---|
| ML-01 | Does the system keep records of user logins or access, where supported? |  |  |
| ML-02 | Can failed or unusual login attempts be identified? |  |  |
| ML-03 | Are important configuration changes recorded, where supported? |  |  |
| ML-04 | Are security or system alerts enabled where available? |  |  |
| ML-05 | Is there a process for reviewing important alerts or unusual activity? |  |  |
| ML-06 | Are monitoring records protected from unauthorised access where possible? |  |  |
| ML-07 | Is there a clear process for investigating unusual activity when it is detected? |  |  |

---

## 7. Physical Security and Local Access

Cybersecurity is not limited to online access. Someone with physical access to an inverter, communication gateway, router or other connected equipment may also be able to access settings, network connections or system controls.

Physical access should therefore be considered as part of the overall security assessment.

| ID | Security Check | Result | Notes |
|---|---|---|---|
| PS-01 | Is important energy and communication equipment located in a reasonably secure area? |  |  |
| PS-02 | Is physical access to configuration or communication interfaces limited to authorised people? |  |  |
| PS-03 | Are routers, gateways and communication modules protected from unnecessary public access? |  |  |
| PS-04 | Are unused physical communication ports or interfaces restricted where possible? |  |  |
| PS-05 | Is there a process for controlling installer or maintenance access to the equipment? |  |  |
| PS-06 | Are signs of unauthorised physical access or changes to equipment checked during maintenance? |  |  |

---

## 8. Backup, Recovery and Incident Response

Security is not only about preventing problems. It is also important to know how the system can be recovered if an account is compromised, a configuration is changed incorrectly, a device fails or another security incident occurs.

The available backup and recovery options will depend on the equipment and platform being assessed.

| ID | Security Check | Result | Notes |
|---|---|---|---|
| BR-01 | Are important system settings or configurations backed up where supported? |  |  |
| BR-02 | Is there a known process for restoring the system after a failure or incorrect configuration? |  |  |
| BR-03 | Is there a process for responding if a user or administrator account is compromised? |  |  |
| BR-04 | Can remote access be disabled or restricted quickly if a security problem is identified? |  |  |
| BR-05 | Are important contact details for the installer, supplier or manufacturer available when technical support is required? |  |  |
| BR-06 | Is there a process for recording and reviewing security incidents? |  |  |
| BR-07 | After an incident, are passwords, access permissions and affected configurations reviewed where necessary? |  |  |
