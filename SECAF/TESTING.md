# SECAF v1.0 Risk Calculator — Testing

## Purpose

The SECAF Risk Calculator was manually tested to confirm that the risk scoring function produces the expected risk levels.

The calculator uses:

**Risk Score = Likelihood × Impact**

with both Likelihood and Impact rated from 1 to 5.

## Test Results

| Test | Likelihood | Impact | Expected Score | Expected Level | Result |
|---|---:|---:|---:|---|---|
| T-01 | 5 | 5 | 25 | Critical | Passed |
| T-02 | 4 | 4 | 16 | High | Passed |
| T-03 | 3 | 3 | 9 | Medium | Passed |
| T-04 | 2 | 2 | 4 | Low | Passed |

All four manual tests returned the expected risk score and classification.

## What Was Tested

The tests confirmed that the calculator can:

- accept Likelihood and Impact values;
- calculate the risk score;
- classify the result as Low, Medium, High or Critical;
- display the assessment result; and
- generate a Markdown assessment report.

## Testing Limitations

These were basic functional tests of the SECAF v1.0 Risk Calculator.

They do not represent independent validation of SECAF, penetration testing of an energy system, or testing against a live inverter, battery system or cloud platform.

Further testing is required as the framework and calculator develop.
