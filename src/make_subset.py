"""
make_subset.py

The project guidelines explicitly require using a subset if the dataset
exceeds 10,000-20,000 samples. The Malicious URL's Dataset has 651,191, so it
must be reduced BEFORE any other stage (EDA, feature engineering, training).
From here on, the whole project works ONLY on the subset, never on the
original file.

The sampling is stratified (stratify=df["type"]): a portion is drawn from
EACH class in proportion to its original frequency, instead of drawing rows
at random from the whole dataset. Without this, by pure bad luck of random
sampling we could end up with very few (or zero) examples of the rarest class
(malware, about 5% of the total) in our subset.

Usage (locally or in Google Colab):
    python make_subset.py

Requires: pandas, scikit-learn
"""

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split


# Paths computed from the location of THIS file (src/make_subset.py), not from
# the folder you launch it from: this works both in PyCharm and from a terminal.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "malicious_urls.csv"
SUBSET_PATH = PROJECT_ROOT / "data" / "subset" / "malicious_urls_subset.csv"
TARGET_SIZE = 15000

# initial alternative, changed to the syntax above to avoid errors when
# running the code on different machines.
# RAW_PATH = "data/raw/malicious_urls.csv"          # file downloaded from Kaggle
# SUBSET_PATH = "data/subset/malicious_urls_subset.csv"
# TARGET_SIZE = 15000                                # within the required 10,000-20,000 range

def main():
    df = pd.read_csv(RAW_PATH)
    print("Original dataset:", len(df), "rows")
    print(df["type"].value_counts())

    # --- Deduplication: remove repeated URLs BEFORE sampling ---
    # Prevents the same URL from ending up in both training and test (data
    # leakage), which would artificially inflate the models' performance.
    before = len(df)
    df = df.drop_duplicates(subset="url").reset_index(drop=True)
    print(f"\nDuplicates removed: {before - len(df)} (unique rows: {len(df)})")

    subset, _ = train_test_split(
        df,
        train_size=TARGET_SIZE,
        stratify=df["type"],       # keeps the original proportions among the 4 classes
        random_state=42,           # fixes the seed: the subset is reproducible by anyone who reruns the script
    )

    print("\nSubset created:", len(subset), "rows")
    print(subset["type"].value_counts())
    print((subset["type"].value_counts(normalize=True) * 100).round(1))

    subset.to_csv(SUBSET_PATH, index=False)
    print(f"\nSaved to {SUBSET_PATH}")


if __name__ == "__main__":
    main()