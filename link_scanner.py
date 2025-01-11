import requests
from urllib.parse import urlparse

# Basic suspicious URL patterns for detection
SUSPICIOUS_PATTERNS = ['@', 'xn--', 'tinyurl', 'bit.ly', 'shorturl', '://']

# OpenPhish Feed URL
OPENPHISH_FEED = "https://openphish.com/feed.txt"

# Function to check URL structure for suspicious patterns
def check_suspicious_patterns(url):
    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in url:
            return True
    return False

# Function to check URL against OpenPhish database
def check_openphish(url):
    try:
        response = requests.get(OPENPHISH_FEED)
        if response.status_code == 200:
            if url in response.text:
                return True
    except requests.RequestException:
        print("Error connecting to OpenPhish database.")
    return False

# Function to check SSL certificate (basic implementation)
def check_ssl_certificate(url):
    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith('https'):
            return True
        else:
            return False
    except requests.RequestException:
        return False

# Main function
def scan_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    print(f"Scanning URL: {url}")

    # Check for suspicious patterns
    if check_suspicious_patterns(url):
        print("[!] Warning: URL contains suspicious patterns!")

    # Check OpenPhish database
    if check_openphish(url):
        print("[!] Alert: URL flagged as phishing in OpenPhish database!")
    else:
        print("[+] URL not flagged in OpenPhish database.")

    # Check SSL Certificate
    if check_ssl_certificate(url):
        print("[+] SSL Certificate Valid.")
    else:
        print("[!] Warning: SSL Certificate missing or invalid.")

    print("\nScan Complete!")

# Run the scanner
if __name__ == "__main__":
    target_url = input("Enter the URL to scan: ")
    scan_url(target_url)
