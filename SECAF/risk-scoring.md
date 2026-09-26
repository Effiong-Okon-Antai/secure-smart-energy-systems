# SECAF v1.0 — Risk Scoring Method

## Purpose

The SECAF risk-scoring method provides a simple way to assess the importance of security issues identified during an assessment.

Not every security issue presents the same level of risk. A finding that is unlikely to occur and has little effect on the system should not be treated in the same way as a weakness that is easy to exploit and could seriously affect system access, monitoring or operation.

SECAF therefore considers two factors:

- **Likelihood** — how likely it is that the identified weakness could lead to a security problem.
- **Impact** — how serious the consequences could be if the problem occurred.

Each factor is given a score from **1 to 5**.

---

## Likelihood Rating

| Score | Rating | Description |
|---|---|---|
| 1 | Rare | Unlikely to occur under normal circumstances |
| 2 | Unlikely | Could occur, but there are significant barriers or existing controls |
| 3 | Possible | Could reasonably occur under certain conditions |
| 4 | Likely | There is a realistic chance of the issue being exploited or causing a security problem |
| 5 | Very Likely | The weakness is highly exposed or could be exploited with little difficulty |

---

## Impact Rating

| Score | Rating | Description |
|---|---|---|
| 1 | Minimal | Little or no significant effect on the system |
| 2 | Minor | Limited effect that can be corrected easily |
| 3 | Moderate | Could affect system access, data, monitoring or normal operation |
| 4 | Major | Could cause serious disruption, unauthorised access or significant data exposure |
| 5 | Severe | Could result in major loss of control, prolonged disruption or serious compromise of the connected energy system |

---

## Calculating the Risk Score

The risk score is calculated by multiplying the likelihood score by the impact score:

**Risk Score = Likelihood × Impact**

For example:

- Likelihood = 4
- Impact = 5
- Risk Score = 4 × 5 = **20**

---

## Risk Levels

| Risk Score | Risk Level |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

The risk rating helps decide which findings should receive attention first.

A higher score does not automatically mean that a system is unsafe. The score is intended to help organise findings and support decisions about which issues should be reviewed or addressed first.
