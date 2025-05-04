# 🛡️ Ransomware Simulation and Detection Project

## 📚 Overview

This project was developed as part of the CSCE 5550 course (Spring 2025) to study and simulate ransomware attacks and implement a defense-in-depth strategy for detection and mitigation. The system is designed to work entirely within a secure virtual machine (VM) environment to avoid risk to the host machine.

The project simulates a real-world ransomware scenario, covering all stages—from encryption and infection to monitoring, detection, and mitigation. A custom ransomware tool is developed to encrypt a recursive directory, and a defense system is designed to detect and mitigate the threat using file system event monitoring and rule-based policy enforcement.

---

## 🏗️ Architecture

The project is divided into the following key components:

### 1. 🔍 Research
Initial survey of ransomware techniques, real-world attack vectors, and defense strategies.

### 2. 🔐 Action (Encryption/Decryption)
- Written in Python using the `cryptography` library (Fernet).
- Recursively encrypts all files in the `critical/` directory and its subfolders (`lab1/`, `lab2/`, `lab3/`).
- Decryption tool built to restore files after ransom payment.

### 3. 🧬 Infection Simulation
- Phishing simulation via malicious script disguised as a legitimate file.
- When executed, the script initiates the encryption routine.

### 4. 👁️ Monitoring
- Uses Python `watchdog` to monitor file system changes.
- Logs all file events (modifications, creations, deletions) to an SQLite database for later analysis.

### 5. ⚠️ Detection
- Analyzes logs against defined rules (e.g., high volume of file modifications in a short time).
- Flags and alerts on suspicious ransomware-like behavior.

### 6. 🧯 Mitigation
- Upon detection, the ransomware process is immediately terminated.
- Alerts are generated.
- Discusses backup, restoration, and additional fail-safes.

---

## ⚙️ Setup Instructions

### ✅ Requirements

- **Python 3.8+**
- `cryptography`
- `watchdog`
- `sqlite3` (built-in)
- `tkinter` (optional, for GUI wrapper)
- A Linux-based Virtual Machine (e.g., Ubuntu 20.04)

Install dependencies using:

```bash
pip install cryptography watchdog
# CompSec
