# 🛡️ Dependency Security & License Audit Tool (DevSecOps)

A lightweight DevSecOps utility to audit Python project dependencies for known CVE vulnerabilities and flag risky open-source licenses before code deployment.

## 🚀 Key Features
- **Vulnerability Scanning:** Queries Advisory Databases for known security flaws (CVEs).
- **License Compliance Check:** Identifies permissive vs. copyleft or restricted licenses.
- **Fail-Fast Mechanism:** Returns non-zero exit codes for integration into CI/CD pipelines.

## 🛠️ Stack & Tools
- **Language:** Python 3
- **Environment:** Linux / POSIX Bash
- **Security Logic:** Parsing requirements and vulnerability pattern analysis.

## 💻 Usage
```bash
python dep_checker.py --file requirements.txt
