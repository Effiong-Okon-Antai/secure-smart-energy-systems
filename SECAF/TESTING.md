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
| T-05 | 6 | 3 | Rejected | Invalid input | Passed |

The four risk classification tests returned the expected results. An additional range-validation test confirmed that values outside the permitted 1–5 range are rejected.

## What Was Tested

- reject Likelihood or Impact values outside the permitted 1–5 range.
  
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


---

## SECAF v1.1 Automated Unit Testing

**Validation date:** 22 October 2026

The SECAF risk calculator was tested using Python's built-in
`unittest` framework and GitHub Actions.

### Test Environment

- Python 3.11
- GitHub Actions hosted runner
- Python unittest framework
- Repository branch: `main`

### Test Coverage

| Test | Purpose | Result |
|---|---|---|
| Low Risk | Validate risk scores 1–4 | PASS |
| Medium Risk | Validate risk scores 5–9 | PASS |
| High Risk | Validate risk scores 10–16 | PASS |
| Critical Risk | Validate risk scores 17–25 | PASS |
| Invalid Low Values | Reject inputs below 1 | PASS |
| Invalid High Values | Reject inputs above 5 | PASS |
| Invalid Data Types | Reject unsupported input types | PASS |
| All Valid Combinations | Verify all 25 likelihood-impact combinations | PASS |

### Automated Test Results

```text
Ran 8 tests in 0.001s

OK
```

**Overall Result: 8 tests passed, 0 failures.**

### Verification Evidence

The automated tests were executed successfully using GitHub Actions.

[View Successful GitHub Actions Test Run](https://github.com/Effiong-Okon-Antai/secure-smart-energy-systems/actions/runs/39836018805)

### Reproducibility

To reproduce the unit tests locally, run the following command
from the repository root:

```bash
python -m unittest discover -s SECAF -p "test_*.py" -v
```

### Validation Scope and Limitations

These tests verify the implemented risk scoring function, including
risk classification thresholds and input validation.

They do not independently validate the suitability of the scoring
method for every real-world cybersecurity scenario.

Further testing is required for interactive input handling, Markdown
report generation, and application of the framework to realistic
smart-energy cybersecurity assessment scenarios.


---

## SECAF v1.1 Extended Automated Validation

**Validation date:** 22 October 2026

The SECAF v1.1 Python risk calculator and assessment report
generator were evaluated using automated unit and integration tests.

### Test Summary

| Test Category | Number of Tests | Result |
|---|---:|---|
| Risk calculation and classification | 8 | PASS |
| Assessment report generation and safety | 4 | PASS |
| **Total** | **12** | **PASS** |

### Risk Calculator Validation

The automated tests verify:

- Low, Medium, High and Critical risk classifications
- Risk score boundaries
- Invalid numerical inputs
- Unsupported input types
- All 25 valid likelihood-impact combinations

### Assessment Report Validation

The automated tests verify:

- Successful generation of a Markdown assessment report
- Correct recording of assessment information and risk scores
- Rejection of invalid likelihood values
- Rejection of unsafe Finding IDs
- Protection against overwriting existing assessment reports

### Test Execution

The tests run automatically using GitHub Actions.

Command:

    python -m unittest discover -s SECAF -p "test_*.py" -v

Expected verified output:

    Ran 12 tests

    OK

### GitHub Actions Evidence

Automated test execution history:

https://github.com/Effiong-Okon-Antai/secure-smart-energy-systems/actions/workflows/secaf-tests.yml

### Validation Limitations

The automated tests confirm the behaviour of the implemented
risk calculation and report-generation functions.

They do not independently validate the cybersecurity effectiveness
of the SECAF methodology or establish that the framework has been
deployed in a real smart-energy environment.

Further validation will involve applying the framework to
documented simulated smart-energy cybersecurity scenarios.
