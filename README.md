# CTF Automation Tool

## Overview
The **CTF Automation Tool** is a Python-based solution designed to automate reconnaissance tasks commonly required in Capture-the-Flag (CTF) challenges. This tool:
- Performs **port scanning** to detect open ports and services.
- Conducts **directory enumeration** to identify hidden web paths.
- Logs results in organized files for easy access.

The tool is intended for use in **isolated virtual environments**, such as Kali Linux or any system supporting Python.

---

## Features
- Automated **port scanning** with detailed service detection.
- Directory enumeration using local wordlists for hidden paths.
- Organized output storage for both scans and logs.
- Runs independently in virtual environments without requiring `apt`.

---

## Installation

### Prerequisites
1. Python 3.x installed on your system.
2. The following tools available **locally or as binaries**:
   - `nmap` (for port scanning): Download [nmap binaries](https://nmap.org/download.html).
   - `gobuster` (for directory enumeration): Download [gobuster binaries](https://github.com/OJ/gobuster/releases).

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.co
