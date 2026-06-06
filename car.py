#!/usr/bin/env python3
"""
mudah_scrape_simple.py

Simple scraper to extract a WhatsApp / phone number from a Mudah.my listing page
(using requests + BeautifulSoup). Intended for learning and personal use only.
Do NOT use this to harvest personal contact data without permission.

Usage:
    python mudah_scrape_simple.py "https://www.mudah.my/your-listing-url.htm"

Requirements:
    pip install requests beautifulsoup4 lxml pyperclip
"""

import argparse
import re
import sys
from typing import Optional

import requests
from bs4 import BeautifulSoup

# Try to import pyperclip for clipboard copying; if not available, we'll still print the number.
try:
    import pyperclip
    HAS_CLIP = True
except Exception:
    HAS_CLIP = False


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0 Safari/537.36"
    )
}

# 1) WhatsApp link patterns (wa.me or api.whatsapp.com)
WHATSAPP_LINK_RE = re.compile(r"(?:https?://)?(?:api\.whatsapp\.com/send|wa\.me)[^\s\"'<>]*", re.IGNORECASE)

# 2) Phone-like pattern: look for sequences that look like phone numbers.
# This is conservative: we capture groups with digits, maybe leading +, spaces, hyphens, parentheses.
PHONE_LIKE_RE = re.compile(
    r"(?:(?:\+?\d{1,3})[ \-]?)?(?:\(?\d{2,4}\)?[ \-]?)?\d{3,4}[ \-]?\d{3,4}"
)

# Normalise to an international-style digits-only string (keep leading + if present)
def normalise_phone(raw: str) -> str:
    raw = raw.strip()
    # If the raw contains 'phone=' query (from whatsapp API), grab digits after phone=
    m = re.search(r"phone=([+\d]+)", raw)
    if m:
        candidate = m.group(1)
    else:
        candidate = raw

    # remove common surrounding text
    candidate = candidate.strip().strip("()[]{}")

    # keep leading plus if any, then digits only
    plus = "+" if candidate.startswith("+") else ""
    digits = re.sub(r"\D", "", candidate)
    return plus + digits if digits else ""


def fetch_html(url: str, timeout: int = 15) -> str:
    r = requests.get(url, headers=HEADERS, timeout=timeout)
    r.raise_for_status()
    return r.text


def find_whatsapp_from_links(soup: BeautifulSoup) -> Optional[str]:
    # search all anchors for wa.me or api.whatsapp.com
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "wa.me" in href or "api.whatsapp.com" in href or "whatsapp" in href.lower():
            # try to extract phone=... first
            m = re.search(r"phone=([+\d]+)", href)
            if m:
                return normalise_phone(m.group(1))
            # wa.me/<number>
            m2 = re.search(r"wa\.me/([+\d]+)", href)
            if m2:
                return normalise_phone(m2.group(1))
            # otherwise, return the href for fallback normalisation
            return normalise_phone(href)
    return None


def find_phone_in_text(soup: BeautifulSoup) -> Optional[str]:
    # Get visible text only
    text = soup.get_text(separator=" ", strip=True)
    # Search for phone-like patterns
    matches = PHONE_LIKE_RE.findall(text)
    if not matches:
        return None
    # Heuristic: prefer longer digit sequences (likely a full phone)
    best = ""
    for m in matches:
        cand = normalise_phone(m)
        # accept only if we have at least 7 digits (avoid false positives)
        if len(re.sub(r"\D", "", cand)) >= 7 and len(cand) > len(best):
            best = cand
    return best if best else None


def extract_phone_from_html(url: str) -> Optional[str]:
    html = fetch_html(url)
    soup = BeautifulSoup(html, "lxml")

    # Strategy 1: WhatsApp links
    found = find_whatsapp_from_links(soup)
    if found:
        return found

    # Strategy 2: search the page text for phone-like patterns
    found = find_phone_in_text(soup)
    if found:
        return found

    # Strategy 3: search specific likely containers (class/id names that contain contact/phone)
    selectors = [
        "[class*='phone']", "[class*='contact']", "[class*='mobile']",
        "[id*='phone']", "[id*='contact']"
    ]
    for sel in selectors:
        for el in soup.select(sel):
            txt = el.get_text(" ", strip=True)
            m = PHONE_LIKE_RE.search(txt)
            if m:
                cand = normalise_phone(m.group(0))
                if len(re.sub(r"\D", "", cand)) >= 7:
                    return cand

    return None


def main():
    p = argparse.ArgumentParser(description="Extract WhatsApp/phone number from a Mudah.my listing (simple HTML scrape)")
    p.add_argument("url", help="Listing URL (e.g. https://www.mudah.my/...)")
    p.add_argument("--no-copy", action="store_true", help="Do not copy result to clipboard even if pyperclip is available")
    args = p.parse_args()

    try:
        phone = extract_phone_from_html(args.url)
    except requests.HTTPError as e:
        print(f"HTTP error while fetching page: {e}", file=sys.stderr)
        sys.exit(2)
    except requests.RequestException as e:
        print(f"Network error: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(3)

    if not phone:
        print("No phone number found in static HTML. The number may be generated by JavaScript; try the Selenium approach.", file=sys.stderr)
        sys.exit(1)

    # copy to clipboard if possible
    if HAS_CLIP and not args.no_copy:
        try:
            pyperclip.copy(phone)
            clipped = True
        except Exception:
            clipped = False
    else:
        clipped = False

    print(phone)
    if clipped:
        print("(Copied to clipboard.)", file=sys.stderr)


if __name__ == "__main__":
    main()
