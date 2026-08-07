#  Python Port Scanner v2.0

A fast, multithreaded TCP Port Scanner written in Python for network reconnaissance and cybersecurity learning.

---

##  Features

- Quick Scan (Top 30 Common Ports)
- Full Scan (1–65535)
- Custom Port Range
- Banner Grabbing
- Service Detection
- Multi-threaded Scanning
- Automatic Report Generation
- Clean Command-Line Interface

---

##  Project Structure

```
port-scanner/
├── port_scanner.py
├── scanner.py
├── banner.py
├── report.py
├── utils.py
├── requirements.txt
├── LICENSE
├── README.md
└── reports/
```

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/iamdonwisdom/port-scanner.git
```

### Go into the project

```bash
cd port-scanner
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the scanner:

```bash
python3 port_scanner.py
```

---

##  Scan Modes

- Quick Scan
- Full Scan
- Custom Port Range

---

##  Example Output

```
[OPEN] Port 22    SSH
[OPEN] Port 80    HTTP
[OPEN] Port 443   HTTPS

Report saved: reports/scan_20260807_113455.txt
```

---

##  Technologies Used

- Python 3
- Socket Programming
- ThreadPoolExecutor
- Banner Grabbing
- Network Reconnaissance

---

##  Disclaimer

This tool is for educational purposes and authorized security testing only. Do not scan systems without permission.

---

##  Author

**Ede Chidozie Philip**

GitHub: https://github.com/iamdonwisdom

---

##  Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
