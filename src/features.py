"""
features.py

Extraction of lexical/statistical features from a URL, for the Malicious URL
classification project (benign / phishing / defacement / malware).

All features are computed ONLY from the URL string: no network requests, no
whois/DNS lookups. This keeps the system fast and usable even "offline"
(e.g. email filter, browser).

The features are organized into 4 categories, each motivated by a hypothesis
about why it should help distinguish the classes. Every category must be
checked with EDA (Exploratory Data Analysis) on the real dataset before taking
it for granted: some hypotheses may turn out to be less useful than others,
and this is normal (and should be discussed in the final slides).

Typical usage:
    import pandas as pd
    from src.features import extract_features

    df = pd.read_csv("data/raw/malicious_urls.csv")   # columns: url, type
    feature_rows = df["url"].apply(extract_features)
    features_df = pd.DataFrame(list(feature_rows))
    df_final = pd.concat([df, features_df], axis=1)
    df_final.to_csv("data/processed/urls_with_features.csv", index=False)
"""

import re
import math
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Reference lists (to be reviewed/extended after EDA on the real dataset)
# ---------------------------------------------------------------------------

# Typical phishing words: they mimic security/urgency actions to push the user
# into clicking (hypothesis: much more frequent in phishing than in benign)
SUSPICIOUS_WORDS = [
    "login", "signin", "verify", "secure", "account", "update", "confirm",
    "banking", "bank", "password", "pay", "free", "bonus", "gift",
]

# Brands commonly impersonated in phishing (hypothesis: present in the URL but
# NOT in the brand's real domain -> strong impersonation signal)
BRAND_NAMES = [
    "paypal", "amazon", "apple", "microsoft", "google", "facebook",
    "netflix", "instagram", "whatsapp", "ebay",
]

# Executable/compressed file extensions: typical of URLs pointing to direct
# malware downloads
EXECUTABLE_EXTENSIONS = [".exe", ".apk", ".scr", ".bat", ".msi", ".zip", ".rar", ".jar"]

# Well-known URL-shortening services: a "short" URL hides the real
# destination, a technique used both legitimately (marketing) and maliciously
SHORTENER_DOMAINS = ["bit.ly", "tinyurl.com", "goo.gl", "t.co", "is.gd", "ow.ly"]

# TLDs (Top-Level Domains, e.g. .com/.ru/.tk) historically associated with
# free or poorly controlled domains, often preferred by attackers because
# cheap/anonymous (hypothesis to be verified empirically on the dataset!)
SUSPICIOUS_TLDS = [".tk", ".ml", ".ga", ".cf", ".xyz", ".top", ".gq"]


def shannon_entropy(s: str) -> float:
    """Shannon entropy of a string: how 'random'/unpredictable it is.

    A randomly generated domain (e.g. from a DGA - Domain Generation
    Algorithm, used by malware to generate command-and-control domains) has
    high entropy. A domain with real words (e.g. "unica.it") has lower, more
    regular entropy.
    """
    if not s:
        return 0.0
    probs = [s.count(c) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in probs)


def has_ip_address(url: str) -> int:
    """1 if the host is a raw IP address instead of a domain name.

    Hypothesis: legitimate sites almost always buy a domain; a URL pointing
    directly to an IP is a strong hint of 'throwaway' malware/phishing.
    """
    return int(bool(re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", url)))


def extract_features(url: str) -> dict:
    """Compute all features for a single URL. Returns a dictionary
    {feature_name: value}, ready to be turned into columns of a pandas
    DataFrame.
    """
    url_str = str(url).strip()
    url_lower = url_str.lower()

    # urlparse needs the scheme (http/https) to correctly interpret host/path;
    # many rows in the dataset have no "http://" in front, so we add it
    # temporarily just for parsing.
    parse_target = url_str if "://" in url_str else "http://" + url_str
    parsed = urlparse(parse_target)
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""

    features = {
        # --- 1. Length features -------------------------------------------
        # Hypothesis: malicious URLs tend to be longer (to hide redirects,
        # parameters, or to imitate a legitimate domain with extra text)
        "url_length": len(url_str),
        "hostname_length": len(hostname),
        "path_length": len(path),
        "query_length": len(query),

        # --- 2. Count features (lexical) ----------------------------------
        "num_dots": url_str.count("."),
        "num_hyphens": url_str.count("-"),
        "num_underscores": url_str.count("_"),
        "num_slashes": url_str.count("/"),
        "num_digits": sum(c.isdigit() for c in url_str),
        "num_special_chars": sum(not c.isalnum() for c in url_str),
        "num_params": query.count("&") + (1 if query else 0),
        "num_subdomains": max(hostname.count(".") - 1, 0),

        # --- 3. Binary features (host/structure) --------------------------
        "has_ip": has_ip_address(url_str),
        "has_https": int(url_lower.startswith("https")),
        "has_at_symbol": int("@" in url_str),
        "has_double_slash_redirect": int("//" in path),
        "has_port": int(bool(parsed.port)),
        "is_shortened": int(any(s in url_lower for s in SHORTENER_DOMAINS)),
        "has_suspicious_tld": int(any(url_lower.endswith(t) or t + "/" in url_lower for t in SUSPICIOUS_TLDS)),
        "has_executable_extension": int(any(url_lower.endswith(ext) for ext in EXECUTABLE_EXTENSIONS)),

        # --- 4. Content/keyword features ----------------------------------
        "suspicious_word_count": sum(w in url_lower for w in SUSPICIOUS_WORDS),
        "brand_name_count": sum(b in url_lower for b in BRAND_NAMES),

        # --- 5. Statistical features --------------------------------------
        "entropy_url": round(shannon_entropy(url_str), 3),
        "entropy_hostname": round(shannon_entropy(hostname), 3),
        "digit_ratio": round(sum(c.isdigit() for c in url_str) / len(url_str), 3) if url_str else 0.0,
    }
    return features


if __name__ == "__main__":
    # Small manual self-test (does not replace EDA on the real dataset)
    examples = [
        "www.unica.it/corsi/machine-learning",
        "http://banking-secure-login.verify-account.tk/update",
        "192.168.1.4.free-download-crack.ru/setup.exe",
    ]
    for u in examples:
        print(u, "->", extract_features(u))