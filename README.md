# Python Web Application Security Audit

A cybersecurity project demonstrating manual source-code review and
static security analysis of an intentionally vulnerable Python Flask
application using Bandit.

## Objective

The objective of this project is to identify common security weaknesses
and coding flaws in a Python web application, recommend secure coding
practices, implement security fixes, and verify the improvements using
static code analysis.

## Technologies Used

- Python
- Flask
- SQLite
- Bandit
- Git & GitHub

## Security Assessment

The initial vulnerable application was analyzed using Bandit:

```bash
py -m bandit vulnerable_app.py