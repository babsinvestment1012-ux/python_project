import requests
import re
import json
import time
import argparse
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import random
import string
import base64

class WebVulnerabilityScanner:
    def __init__(self, target_url, report_file="vulnerability_report.json"):
        self.target_url = target_url
        self.session = requests.Session()
        self.report = {
            "target": target_url,
            "scan_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "vulnerabilities": []
        }
        self.report_file = report_file
        self.discovered_urls = set([target_url])
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def discover_urls(self, max_urls=50):
        """Discover additional URLs on the target website"""
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(self.target_url, href)

                if urlparse(full_url).netloc == urlparse(self.target_url).netloc:
                    self.discovered_urls.add(full_url)

                    if len(self.discovered_urls) >= max_urls:
                        break

        except Exception as e:
            print(f"Error discovering URLs: {e}")

        return list(self.discovered_urls)

    def check_sql_injection(self, url):
        """Check for SQL Injection vulnerabilities"""
        sql_payloads = [
            "' OR '1'='1",
            "' OR 1=1--",
            "'; DROP TABLE users--",
            "' UNION SELECT NULL--",
            "' OR 'x'='x",
            "1' OR '1'='1' /*",
            "admin'--",
            "' OR 1=1#"
        ]

        error_indicators = [
            "SQL syntax",
            "mysql_fetch",
            "ORA-[0-9]{5}",
            "Microsoft OLE DB Provider",
            "ODBC SQL Server Driver",
            "SQLite/JDBCDriver",
            "PostgreSQL query failed",
            "Warning: pg_",
            "valid MySQL result",
            "Npgsql\\.",
            "PdoException",
            "XPathException"
        ]

        try:
            response = self.session.get(url)

            parsed_url = urlparse(url)
            query_params = parsed_url.query.split('&')

            for param in query_params:
                if '=' in param:
                    key, value = param.split('=', 1)

                    for payload in sql_payloads:
                        test_url = url.replace(f"{key}={value}", f"{key}={payload}")

                        try:
                            test_response = self.session.get(test_url)

                            for error in error_indicators:
                                if re.search(error, test_response.text, re.IGNORECASE):
                                    self.report_vulnerability(
                                        "SQL Injection",
                                        test_url,
                                        f"Possible SQL Injection vulnerability detected with payload: {payload}",
                                        "High"
                                    )
                                    break

                        except Exception:
                            continue

            forms = self.get_forms(url)
            for form in forms:
                form_details = self.get_form_details(form)

                for payload in sql_payloads:
                    data = {}
                    for input_tag in form_details["inputs"]:
                        if input_tag["type"] == "text" or input_tag["type"] == "search":
                            data[input_tag["name"]] = payload
                        elif input_tag["type"] == "submit":
                            data[input_tag["name"]] = input_tag["value"]

                    try:
                        if form_details["method"] == "post":
                            response = self.session.post(form_details["action"], data=data)
                        else:
                            response = self.session.get(form_details["action"], params=data)

                        for error in error_indicators:
                            if re.search(error, response.text, re.IGNORECASE):
                                self.report_vulnerability(
                                    "SQL Injection",
                                    form_details["action"],
                                    f"Possible SQL Injection vulnerability detected in form with payload: {payload}",
                                    "High"
                                )
                                break

                    except Exception:
                        continue

        except Exception as e:
            print(f"Error checking SQL Injection: {e}")

    def check_xss(self, url):
        """Check for Cross-Site Scripting (XSS) vulnerabilities"""
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "javascript:alert('XSS')",
            "<img src=x onerror=alert('XSS')>",
            "';alert('XSS');//",
            "<svg onload=alert('XSS')>",
            "'\"><script>alert('XSS')</script>",
            "<iframe src=javascript:alert('XSS')>",
            "<body onload=alert('XSS')>"
        ]

        try:
            parsed_url = urlparse(url)
            query_params = parsed_url.query.split('&')

            for param in query_params:
                if '=' in param:
                    key, value = param.split('=', 1)

                    for payload in xss_payloads:
                        test_url = url.replace(f"{key}={value}", f"{key}={payload}")

                        try:
                            test_response = self.session.get(test_url)

                            if payload in test_response.text:
                                self.report_vulnerability(
                                    "Cross-Site Scripting (XSS)",
                                    test_url,
                                    f"Possible XSS vulnerability detected with payload: {payload}",
                                    "Medium"
                                )
                                break

                        except Exception:
                            continue

            forms = self.get_forms(url)
            for form in forms:
                form_details = self.get_form_details(form)

                for payload in xss_payloads:
                    data = {}
                    for input_tag in form_details["inputs"]:
                        if input_tag["type"] == "text" or input_tag["type"] == "search":
                            data[input_tag["name"]] = payload
                        elif input_tag["type"] == "submit":
                            data[input_tag["name"]] = input_tag["value"]

                    try:
                        if form_details["method"] == "post":
                            response = self.session.post(form_details["action"], data=data)
                        else:
                            response = self.session.get(form_details["action"], params=data)

                        if payload in response.text:
                            self.report_vulnerability(
                                "Cross-Site Scripting (XSS)",
                                form_details["action"],
                                f"Possible XSS vulnerability detected in form with payload: {payload}",
                                "Medium"
                            )
                            break

                    except Exception:
                        continue

        except Exception as e:
            print(f"Error checking XSS: {e}")

    def check_csrf(self, url):
        """Check for Cross-Site Request Forgery (CSRF) vulnerabilities"""
        try:
            forms = self.get_forms(url)

            for form in forms:
                form_details = self.get_form_details(form)

                action_lower = form_details["action"].lower()
                method_lower = form_details["method"].lower()

                if ("post" in method_lower or "put" in method_lower or "delete" in method_lower) and \
                   any(keyword in action_lower for keyword in ["update", "delete", "change", "add", "create", "modify"]):

                    csrf_found = False
                    for input_tag in form_details["inputs"]:
                        input_name = input_tag["name"].lower()
                        if any(token in input_name for token in ["csrf", "token", "nonce", "_token", "authenticity"]):
                            csrf_found = True
                            break

                    if not csrf_found:
                        self.report_vulnerability(
                            "Cross-Site Request Forgery (CSRF)",
                            form_details["action"],
                            "Form appears to perform state-changing operation without CSRF protection",
                            "Medium"
                        )

        except Exception as e:
            print(f"Error checking CSRF: {e}")

    def check_ssrf(self, url):
        """Check for Server-Side Request Forgery (SSRF) vulnerabilities"""
        ssrf_payloads = [
            "http://127.0.0.1",
            "http://localhost",
            "http://169.254.169.254",  # AWS metadata endpoint
            "file:///etc/passwd",
            "ftp://example.com",
            "dict://127.0.0.1:11211/",
            "gopher://127.0.0.1:80/"
        ]

        try:
            parsed_url = urlparse(url)
            query_params = parsed_url.query.split('&')

            for param in query_params:
                if '=' in param:
                    key, value = param.split('=', 1)

                    # Check for parameters that might be URLs
                    param_lower = key.lower()
                    if any(keyword in param_lower for keyword in ["url", "redirect", "link", "file", "path", "doc", "page"]):
                        for payload in ssrf_payloads:
                            test_url = f"{url}?{key}={payload}"
                            try:
                                response = self.session.get(test_url, timeout=5)
                                if response.status_code == 200:
                                    self.report_vulnerability(
                                        "Server-Side Request Forgery (SSRF)",
                                        test_url,
                                        f"Possible SSRF vulnerability detected with payload: {payload}",
                                        "High"
                                    )
                            except Exception:
                                pass

        except Exception as e:
            print(f"Error checking SSRF: {e}")

    def get_forms(self, url):
        """Extract all forms from a URL"""
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find_all('form')
        except Exception as e:
            print(f"Error getting forms: {e}")
            return []

    def get_form_details(self, form):
        """Extract details from a form element"""
        details = {
            "action": form.attrs.get("action", "").lower(),
            "method": form.attrs.get("method", "get").lower(),
            "inputs": []
        }

        for input_tag in form.find_all("input"):
            details["inputs"].append({
                "type": input_tag.attrs.get("type", "text"),
                "name": input_tag.attrs.get("name", ""),
                "value": input_tag.attrs.get("value", "")
            })

        return details

    def report_vulnerability(self, vuln_type, url, description, severity):
        """Add a vulnerability to the report"""
        vulnerability = {
            "type": vuln_type,
            "url": url,
            "description": description,
            "severity": severity,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.report["vulnerabilities"].append(vulnerability)
        print(f"[{severity}] {vuln_type} found at {url}")
        print(f"  Description: {description}")

    def save_report(self):
        """Save the vulnerability report to a JSON file"""
        with open(self.report_file, 'w') as f:
            json.dump(self.report, f, indent=4)
        print(f"\nReport saved to {self.report_file}")

    def run(self):
        """Run all vulnerability checks"""
        print(f"\n[*] Starting scan on: {self.target_url}")
        print("[*] Discovering URLs...")
        urls = self.discover_urls()
        print(f"[*] Found {len(urls)} URLs to scan\n")

        for url in urls:
            print(f"[*] Scanning: {url}")
            self.check_sql_injection(url)
            self.check_xss(url)
            self.check_csrf(url)
            self.check_ssrf(url)

        print(f"\n[*] Scan complete. Found {len(self.report['vulnerabilities'])} vulnerabilities.")
        self.save_report()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")
    parser.add_argument("-u", "--url", required=True, help="Target URL to scan")
    parser.add_argument("-o", "--output", default="vulnerability_report.json", help="Output report file")
    args = parser.parse_args()

    target = args.url
    if not target.startswith("http"):
        target = "https://" + target

    scanner = WebVulnerabilityScanner(target, args.output)
    scanner.run()