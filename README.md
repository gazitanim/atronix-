# CTF Automation Tool

## Overview
The **CTF Automation Tool** is a Python-based solution designed to streamline reconnaissance tasks commonly encountered in Capture-the-Flag (CTF) challenges. This tool automates:
- **Port Scanning**: Quickly identify open ports and services using `nmap`.
- **Directory Enumeration**: Detect hidden directories on web servers using `gobuster`.
- **Result Logging**: Saves all outputs for easy reference.

The tool is intended for ethical use in CTF environments or private lab setups.

---

## Features
- Automated **port scanning** with detailed service detection.
- Directory enumeration using wordlists for uncovering web server paths.
- User-friendly logging and output storage.
- Results saved in organized files for easy access.
- Built for use in isolated environments like Kali Linux.

---

## Installation

### Prerequisites
1. Python 3.x installed.
2. Required tools:
   - `nmap`
   - `gobuster`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CTF-Automation-Tool.git
   cd CTF-Automation-Tool
