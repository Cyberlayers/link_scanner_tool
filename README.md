# Link Scanner Tool

This **Python-based Link Scanner Tool** is designed for cybersecurity professionals and researchers to identify potentially suspicious URLs. It performs basic checks for malicious patterns, scans against the OpenPhish threat database, and validates SSL certificates for web security testing.

---

## 📦 Features
- **Suspicious URL Pattern Detection:** Detects suspicious patterns commonly used in phishing URLs (e.g., `@`, URL shorteners, special characters).
- **OpenPhish Threat Feed Lookup:** Compares URLs against the OpenPhish database for known phishing threats.
- **SSL Certificate Validation:** Checks if the URL uses a valid SSL certificate for secure HTTPS connections.

---

## 🚀 Installation and Setup (Kali Linux)
Ensure you have Python 3.x installed on your system.

### Option 1: Run Directly
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
pip install requests

### Option 2: Using a Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate
pip install requests

### How to Run the Tool
1. Run the script
python3 link_scanner.py
2. Enter a URL for Scanning: Example: https://example.com
3. Review the Results
The tool will scan the URL structure for suspicious patterns.
It will query the OpenPhish threat database.
It will validate the SSL certificate of the URL.

### How It Works
Pattern Matching: The tool scans URLs for suspicious symbols and patterns often seen in phishing attacks.
OpenPhish Check: Cross-checks the provided URL against the latest OpenPhish threat feed.
SSL Validation: Verifies if the URL is using a valid SSL certificate.


### License
This project is licensed under the MIT License. You are free to use, modify, and distribute this tool with proper attribution.

### Disclaimer
This tool is for educational and research purposes only. The author is not responsible for any misuse. Always obtain proper authorization before testing any third-party systems.

### Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to submit a pull request.
