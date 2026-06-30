# VulnProbe 🔍

A Python-based network vulnerability scanner that detects open ports, identifies running services and versions, checks them against real CVE databases, and generates a professional HTML vulnerability report.

## Features
- ✅ **Stage 1**: Port scanning with service detection
- ✅ **Stage 2**: Nmap integration for exact software version detection
- ✅ **Stage 3**: Live CVE lookup via the NVD (National Vulnerability Database) API
- ✅ **Stage 4**: Auto-generated HTML vulnerability report

## How It Works
1. Scans a target's open ports using Python sockets
2. Identifies the service running on each open port
3. Uses Nmap to detect the exact software name and version
4. Queries the official NVD database for known CVEs matching that software/version
5. Generates a styled HTML report summarizing all findings, color-coded by severity

## Usage
```bash
python scanner.py
```
You'll be prompted for:
- Target IP or hostname
- Start port
- End port

## Sample Output
VulnProbe - Network Vulnerability Scanner
Target   : scanme.nmap.org (45.33.32.156)
Ports    : 1 to 100
[OPEN] Port    22 --> ssh             | OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13
No known CVEs found.
[OPEN] Port    80 --> http            | Apache httpd 2.4.7
[VULNERABLE] CVE-2021-44224 - HIGH - A crafted URI sent to httpd...
Scan complete. 2 open port(s) found.
[+] Report saved as: VulnProbe_Report_scanme_nmap_org.html

## Tech Stack
- Python 3.13
- `socket` (built-in) — port scanning
- `python-nmap` — service/version detection
- `requests` — NVD API integration
- Nmap 7.99

## Disclaimer
This tool is for educational purposes and authorized security testing only. Only scan systems you own or have explicit permission to test. `scanme.nmap.org` is a legal public test server provided by the Nmap project.

## Author
**Adithya** | CSE (Cybersecurity Specialization) | IIIT Kottayam
[GitHub](https://github.com/Adithya9x)
