# Notebook del progetto

Un notebook per ogni fase, in ordine. Ogni notebook importa le funzioni da `src/features.py`
invece di riscrivere codice duplicato.
Usiamo questo tipo di file (.ipynb) che sta per Jupyter Notebook perchè più comodo:
funziona come un file JSON, quindi una struttura dati e può contenere delle celle che
possono essere testo normale o codice alternativamente. L'aspetto positivo è che
salva tutti i risultati come grafici o immagini generate.

1. `01_eda.ipynb` — Analisi esplorativa che viene fatta prima di costruire il modello:
   bisogna guardare i dati per capire cosa contengono e se sono adatti.
   Vediamo la distribuzione delle 4 classi, alcuni esempi di URL per
   classe, e delle prime ipotesi su quali pattern testuali le distinguono.
2. `02_feature_engineering.ipynb` — Applica `extract_features` a tutto il dataset,
   visualizza la distribuzione di ogni feature per classe (per verificare che sia
   davvero utile), salva il risultato in `data/processed/`.
3. `03_model_training.ipynb` — Split train/test, addestramento dei classificatori
   (Gaussiano, k-NN, SVM, MLP), grid search per gli iperparametri.
4. `04_evaluation.ipynb` — Confusion matrix, classification report, confronto finale
   tra modelli, grafici da esportare in `figures/` per le slide.
