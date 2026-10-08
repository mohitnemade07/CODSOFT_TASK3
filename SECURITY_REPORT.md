# Security Audit Report

## Project: Python Web Application Security Audit

### 1. Objective

The objective of this security audit is to examine a Python Flask web application for common security weaknesses and coding flaws.

The assessment combines:

- Manual source-code review
- Static code analysis using Bandit
- Secure coding recommendations

The application used for this assessment is intentionally vulnerable and is intended for cybersecurity education and secure coding practice.

---

## 2. Tools Used

| Tool | Purpose |
|---|---|
| Python | Application development |
| Flask | Web application framework |
| SQLite | Database |
| Bandit | Static security analysis |
| Git & GitHub | Version control |

---

## 3. Methodology

The security review was performed using the following process:

1. Examined the application source code manually.
2. Identified potentially unsafe coding practices.
3. Ran Bandit against the vulnerable application.
4. Reviewed the reported security findings.
5. Classified the risks based on severity.
6. Recommended secure coding practices.
7. Planned a secure version of the application to address the identified weaknesses.

---

# 4. Static Analysis Results

Bandit identified four security findings in the application.

| ID | Finding | Severity | CWE |
|---|---|---|---|
| B105 | Hardcoded Secret | Low | CWE-259 |
| B608 | Possible SQL Injection | Medium | CWE-89 |
| B105 | Hardcoded Password | Low | CWE-259 |
| B201 | Flask Debug Mode Enabled | High | CWE-94 |

### Summary

- **High:** 1
- **Medium:** 1
- **Low:** 2
- **Total:** 4

---

# 5. Vulnerability Analysis

## 5.1 Hardcoded Secret

### Bandit Finding

**B105: hardcoded_password_string**

Location:

```text
vulnerable_app.py:7
# 13. Verification of Security Fixes

After applying the recommended secure coding practices, the updated application was analyzed using Bandit.

The secure version is:

```text
secure_app.py

