# Malicious URL Detection — Progetto Machine Learning 2025/2026

Progetto per il corso di Machine Learning (Prof. Battista Biggio, Università di Cagliari).
Autori: Riccardo, Matteo.

## Obiettivo

Classificare un URL in una delle 4 classi: `benign`, `phishing`, `defacement`, `malware`,
a partire esclusivamente da feature calcolate sul testo dell'URL (nessuna richiesta di rete,
nessuna visita del sito).

Dataset: [Malicious URL's Dataset](https://www.kaggle.com/datasets/naveenbhadouria/malicious) (Kaggle, ~651k righe).

## Struttura del repository

```
malicious-url-detection/
├── data/
│   ├── raw/            # dataset originale scaricato da Kaggle (malicious_urls.csv) - NON versionato su git se >50MB
│   └── processed/      # dataset dopo il feature engineering (pronto per i classificatori)
├── notebooks/          # notebook Colab/Jupyter, uno per fase (vedi notebooks/README.md)
├── src/
│   └── features.py     # funzioni di estrazione feature, riusabili da notebook e script
├── figures/            # grafici esportati (per le slide finali)
├── slides/              # le 10 slide di presentazione del progetto
├── requirements.txt
└── .gitignore
```

## Come iniziare (setup locale)

1. Clonare il repository:
   ```
   git clone <url-del-repo>
   cd malicious-url-detection
   ```
2. Creare un ambiente virtuale e installare le dipendenze:
   ```
   python -m venv venv
   source venv/bin/activate   # su Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Scaricare il dataset da Kaggle e salvarlo in `data/raw/malicious_urls.csv`
   (serve un account Kaggle + API token, vedi https://www.kaggle.com/docs/api).

## Stato del progetto

- [ ] Analisi esplorativa dei dati (EDA)
- [ ] Feature engineering (vedi `src/features.py`)
- [ ] Split train/test
- [ ] Addestramento classificatori (Gaussiano, k-NN, SVM, MLP)
- [ ] Valutazione e confronto (cross-validation, confusion matrix)
- [ ] Slide finali + link GitHub
