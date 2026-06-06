import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

with open("/Users/babs/Documents/emails.txt", "r") as file:
    emails = file.readlines()

for email in emails:
    email = email.strip()
    if "@" in email:
        try:
            _, domain = email.split("@")
            webmail_url = f"https://webmail.{domain}"
            response = requests.get(webmail_url, headers=headers, timeout=5)

            if response.status_code == 200:
                print(f"{webmail_url} -  Website reachable")
            else:
                print(f"{webmail_url} - Error: {response.status_code}")
        except requests.RequestException:
            print(f"{webmail_url} -  Website unreachable")

