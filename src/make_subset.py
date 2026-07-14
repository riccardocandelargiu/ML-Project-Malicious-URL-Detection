"""
make_subset.py

Le linee guida del progetto richiedono esplicitamente di usare un sottoinsieme
(subset) se il dataset supera 10.000-20.000 campioni. Il Malicious URL's
Dataset ne ha 651.191: va quindi ridotto PRIMA di qualunque altra fase
(EDA, feature engineering, training). Da qui in poi tutto il progetto lavora
SOLO sul subset, mai sul file originale.

Il campionamento è stratificato (stratify=df["type"]): significa che si
estrae una porzione da OGNI classe in proporzione alla sua frequenza
originale, invece di estrarre righe a caso da tutto il dataset. Senza questo
accorgimento rischieremmo, per pura sfortuna del campionamento casuale, di
finire con pochissimi (o zero) esempi della classe più rara (malware, il 5%
circa del totale) nel nostro subset.

Uso (in locale o in Google Colab):
    python make_subset.py

Richiede: pandas, scikit-learn
"""

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split


# Percorsi calcolati a partire dalla posizione di QUESTO file (src/make_subset.py),
# non dalla cartella da cui lo lanci: funziona sia da PyCharm sia da terminale.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "malicious_urls.csv"
SUBSET_PATH = PROJECT_ROOT / "data" / "subset" / "malicious_urls_subset.csv"
TARGET_SIZE = 15000

# alternativa iniziale, modificato con la sintassi di sopra per evitare errori
# quando si esegue codice in dispositivi diversi.
# RAW_PATH = "data/raw/malicious_urls.csv"          # file scaricato da Kaggle
# SUBSET_PATH = "data/subset/malicious_urls_subset.csv"
# TARGET_SIZE = 15000                                # dentro il range 10.000-20.000 richiesto

def main():
    df = pd.read_csv(RAW_PATH)
    print("Dataset originale:", len(df), "righe")
    print(df["type"].value_counts())

    subset, _ = train_test_split(
        df,
        train_size=TARGET_SIZE,
        stratify=df["type"],       # mantiene le proporzioni originali tra le 4 classi
        random_state=42,           # fissa il seed: il subset è riproducibile da chiunque rilanci lo script
    )

    print("\nSubset creato:", len(subset), "righe")
    print(subset["type"].value_counts())
    print((subset["type"].value_counts(normalize=True) * 100).round(1))

    subset.to_csv(SUBSET_PATH, index=False)
    print(f"\nSalvato in {SUBSET_PATH}")


if __name__ == "__main__":
    main()
