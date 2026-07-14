# Notebook del progetto

Un notebook per ogni fase, in ordine. Ogni notebook importa le funzioni da `src/features.py`
invece di riscrivere codice duplicato.

1. `01_eda.ipynb` — Analisi esplorativa: distribuzione delle 4 classi, esempi di URL per
   classe, prime ipotesi su quali pattern testuali le distinguono.
2. `02_feature_engineering.ipynb` — Applica `extract_features` a tutto il dataset,
   visualizza la distribuzione di ogni feature per classe (per verificare che sia
   davvero utile), salva il risultato in `data/processed/`.
3. `03_model_training.ipynb` — Split train/test, addestramento dei classificatori
   (Gaussiano, k-NN, SVM, MLP), grid search per gli iperparametri.
4. `04_evaluation.ipynb` — Confusion matrix, classification report, confronto finale
   tra modelli, grafici da esportare in `figures/` per le slide.
