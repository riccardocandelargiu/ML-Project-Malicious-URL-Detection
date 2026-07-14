"""
features.py

Estrazione di feature lessicali/statistiche da un URL, per il progetto di
classificazione Malicious URL (benign / phishing / defacement / malware).

Tutte le feature sono calcolate SOLO a partire dalla stringa dell'URL:
nessuna richiesta di rete, nessun accesso a whois/DNS. Questo rende il
sistema veloce e utilizzabile anche "offline" (es. filtro email, browser).

Le feature sono organizzate in 4 categorie, ciascuna motivata da un'ipotesi
sul perché dovrebbe aiutare a distinguere le classi. Ogni categoria va
verificata con l'EDA (Exploratory Data Analysis) sul dataset reale prima di
darla per assodata: alcune ipotesi potrebbero rivelarsi meno utili di altre,
e questo è normale (e va discusso nelle slide finali).

Uso tipico:
    import pandas as pd
    from src.features import extract_features

    df = pd.read_csv("data/raw/malicious_urls.csv")   # colonne: url, type
    feature_rows = df["url"].apply(extract_features)
    features_df = pd.DataFrame(list(feature_rows))
    df_final = pd.concat([df, features_df], axis=1)
    df_final.to_csv("data/processed/urls_with_features.csv", index=False)
"""

import re
import math
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Liste di riferimento (da rivedere/estendere dopo l'EDA sul dataset reale)
# ---------------------------------------------------------------------------

# Parole tipiche di phishing: imitano azioni di sicurezza/urgenza per indurre
# l'utente a cliccare (ipotesi: molto più frequenti in phishing che in benign)
SUSPICIOUS_WORDS = [
    "login", "signin", "verify", "secure", "account", "update", "confirm",
    "banking", "bank", "password", "pay", "free", "bonus", "gift",
]

# Marchi comunemente impersonati nel phishing (ipotesi: presenti nell'URL ma
# NON nel dominio reale del brand -> segnale forte di impersonificazione)
BRAND_NAMES = [
    "paypal", "amazon", "apple", "microsoft", "google", "facebook",
    "netflix", "instagram", "whatsapp", "ebay",
]

# Estensioni di file eseguibili/compressi: tipiche di URL che puntano a
# download diretti di malware
EXECUTABLE_EXTENSIONS = [".exe", ".apk", ".scr", ".bat", ".msi", ".zip", ".rar", ".jar"]

# Servizi noti di URL-shortening: un URL "corto" nasconde la destinazione
# reale, tecnica usata sia in phishing legittimo (marketing) sia malevolo
SHORTENER_DOMAINS = ["bit.ly", "tinyurl.com", "goo.gl", "t.co", "is.gd", "ow.ly"]

# TLD (Top-Level Domain, es. .com/.ru/.tk) storicamente associati a domini
# gratuiti o poco controllati, spesso preferiti da attaccanti perché a
# basso costo/anonimi (ipotesi da verificare empiricamente sul dataset!)
SUSPICIOUS_TLDS = [".tk", ".ml", ".ga", ".cf", ".xyz", ".top", ".gq"]


def shannon_entropy(s: str) -> float:
    """Entropia di Shannon di una stringa: quanto è 'casuale'/imprevedibile.

    Un dominio generato casualmente (es. da un algoritmo DGA - Domain
    Generation Algorithm, usato da malware per generare domini di comando e
    controllo) ha entropia alta. Un dominio con parole reali (es. "unica.it")
    ha entropia più bassa e più regolare.
    """
    if not s:
        return 0.0
    probs = [s.count(c) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in probs)


def has_ip_address(url: str) -> int:
    """1 se l'host è un indirizzo IP grezzo invece di un nome a dominio.

    Ipotesi: i siti legittimi comprano quasi sempre un dominio; un URL che
    punta direttamente a un IP è un forte indizio di malware/phishing
    'usa e getta'.
    """
    return int(bool(re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", url)))


def extract_features(url: str) -> dict:
    """Calcola tutte le feature per un singolo URL. Ritorna un dizionario
    {nome_feature: valore}, pronto per essere convertito in colonne di un
    DataFrame pandas.
    """
    url_str = str(url).strip()
    url_lower = url_str.lower()

    # urlparse ha bisogno dello schema (http/https) per interpretare bene
    # host/path; molte righe del dataset non hanno "http://" davanti, quindi
    # lo aggiungiamo temporaneamente solo per il parsing.
    parse_target = url_str if "//" in url_str else "http://" + url_str
    parsed = urlparse(parse_target)
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""

    features = {
        # --- 1. Feature di lunghezza --------------------------------------
        # Ipotesi: URL malevoli tendono ad essere più lunghi (per nascondere
        # redirect, parametri, o imitare un dominio legittimo con testo extra)
        "url_length": len(url_str),
        "hostname_length": len(hostname),
        "path_length": len(path),
        "query_length": len(query),

        # --- 2. Feature di conteggio (lessicali) --------------------------
        "num_dots": url_str.count("."),
        "num_hyphens": url_str.count("-"),
        "num_underscores": url_str.count("_"),
        "num_slashes": url_str.count("/"),
        "num_digits": sum(c.isdigit() for c in url_str),
        "num_special_chars": sum(not c.isalnum() for c in url_str),
        "num_params": query.count("&") + (1 if query else 0),
        "num_subdomains": max(hostname.count(".") - 1, 0),

        # --- 3. Feature binarie (host/struttura) --------------------------
        "has_ip": has_ip_address(url_str),
        "has_https": int(url_lower.startswith("https")),
        "has_at_symbol": int("@" in url_str),
        "has_double_slash_redirect": int("//" in path),
        "has_port": int(bool(parsed.port)),
        "is_shortened": int(any(s in url_lower for s in SHORTENER_DOMAINS)),
        "has_suspicious_tld": int(any(url_lower.endswith(t) or t + "/" in url_lower for t in SUSPICIOUS_TLDS)),
        "has_executable_extension": int(any(url_lower.endswith(ext) for ext in EXECUTABLE_EXTENSIONS)),

        # --- 4. Feature di contenuto/parole chiave ------------------------
        "suspicious_word_count": sum(w in url_lower for w in SUSPICIOUS_WORDS),
        "brand_name_count": sum(b in url_lower for b in BRAND_NAMES),

        # --- 5. Feature statistiche ----------------------------------------
        "entropy_url": round(shannon_entropy(url_str), 3),
        "entropy_hostname": round(shannon_entropy(hostname), 3),
        "digit_ratio": round(sum(c.isdigit() for c in url_str) / len(url_str), 3) if url_str else 0.0,
    }
    return features


if __name__ == "__main__":
    # Piccolo self-test manuale (non sostituisce l'EDA sul dataset reale)
    esempi = [
        "www.unica.it/corsi/machine-learning",
        "http://banking-secure-login.verify-account.tk/update",
        "192.168.1.4.free-download-crack.ru/setup.exe",
    ]
    for u in esempi:
        print(u, "->", extract_features(u))
