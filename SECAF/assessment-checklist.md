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
