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
│   ├── raw/            # dataset ORIGINALE scaricato da Kaggle (651k righe) - SOLO in locale, MAI su GitHub
│   ├── subset/         # sottoinsieme stratificato (10-20k righe, come richiesto dalle linee guida)
│   └── processed/      # subset dopo il feature engineering (pronto per i classificatori)
├── notebooks/          # notebook Colab/Jupyter, uno per fase (vedi notebooks/README.md)
├── src/
│   ├── make_subset.py  # crea il subset stratificato da data/raw -> data/subset
│   └── features.py     # funzioni di estrazione feature, riusabili da notebook e script
├── figures/            # grafici esportati (per le slide finali)
├── slides/              # le 10 slide di presentazione del progetto
├── requirements.txt
└── .gitignore
```

**Importante sul dataset**: il Malicious URL's Dataset ha 651.191 righe. Le linee guida del
progetto richiedono di usare un subset se il dataset supera 10.000-20.000 campioni. Per questo
`data/raw/` (il file completo) resta **solo sul computer di chi lo scarica**, non va mai caricato
su GitHub: si carica su GitHub solo `data/subset/malicious_urls_subset.csv` (circa 15.000 righe),
generato con `src/make_subset.py`, molto più leggero e sufficiente per tutto il progetto.

## Come iniziare (setup locale)

1. Clonare il repository:
   ```
   git clone <url-del-repo>
   cd malicious-url-detection
 
## Stato del progetto

- [ ] Analisi esplorativa dei dati (EDA)
- [ ] Feature engineering (vedi `src/features.py`)
- [ ] Split train/test
- [ ] Addestramento classificatori (Gaussiano, k-NN, SVM, MLP)
- [ ] Valutazione e confronto (cross-validation, confusion matrix)
- [ ] Slide finali + link GitHub
