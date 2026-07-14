# Malicious URL Detection — Progetto Machine Learning

Progetto per il corso di Machine Learning.
Autori: Riccardo Candelargiu, Matteo Mura.

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
├── slides/             # le 10 slide di presentazione del progetto
├── requirements.txt
├── PROGRESS.md         # contentente tutti gli aggiornamenti lavorativi quotidiani
├── README.md
└── .gitignore
```

**Importante sul dataset**: il Malicious URL's Dataset ha 651.191 righe. Le linee guida del
progetto richiedono di usare un subset se il dataset supera 10.000-20.000 campioni. Per questo
`data/raw/` (il file completo) resta **solo sul computer di chi lo scarica**, non va mai caricato
su GitHub: si carica su GitHub solo `data/subset/malicious_urls_subset.csv` (circa 15.000 righe),
generato con `src/make_subset.py`, molto più leggero e sufficiente per tutto il progetto.

⚠ **Aggiornare PROGRESS.md dopo ogni modifica importante.**


## ROADMAP (da valutare modifica in caso classificazione con un solo modello)

**Fase 0 — Creazione del subset:** solo Python/pandas (sezione 12 della guida), nessun concetto teorico specifico, ma è un passaggio obbligatorio prima di tutto il resto.

**Fase 1 — EDA (Exploratory Data Analysis):** guardate quanti esempi ci sono per classe, alcuni URL di esempio per classe, distribuzioni di lunghezza/caratteri. Strumenti: pandas, matplotlib (grafici a barre/istogrammi).

**Fase 2 — Feature engineering:** applicate features.py a tutto il subset. Concettualmente è l'applicazione pratica del concetto di "feature/feature space" visto nell'introduzione del corso (sezione 2 della guida).

**Fase 3 — Visualizzazione con PCA (e volendo t-SNE):** sezione 8 della guida. Una volta che avete le 28 feature numeriche, usate PCA per proiettarle in 2D e vedere visivamente quanto le 4 classi si separano — ottimo sia per capire se le feature funzionano, sia come grafico per le slide finali.

**Fase 4 — Split train/test:** hold-out stratificato (sezione 6), dividendo il subset (non il dataset intero) in training e test set, mantenendo le proporzioni tra le 4 classi.

**Fase 5 — Classificatori "classici" come baseline:** il classificatore Gaussiano (sezione 3) e/o k-NN (sezione 4), implementati anche a mano (come nel laboratorio) per dimostrare di aver capito la teoria, non solo di saper chiamare una libreria.

**Fase 6 — SVM:** sezione 5, con scikit-learn (SVC), come classificatore discriminativo intermedio.

**Fase 7 — Rete neurale (MLP):** sezione 9, per il confronto esplicito "modello classico vs rete neurale" richiesto dalle linee guida del progetto.

**Fase 8 — Hyperparameter tuning:** sezione 6, GridSearchCV con cross-validation per scegliere k (k-NN), C e gamma (SVM), numero di neuroni (MLP).

**Fase 9 — Valutazione:** sezione 6, confusion matrix e classification report per classe (fondamentale, visto che le classi sono sbilanciate anche nel subset).

**Fase 10 — Extra per il 30L (facoltativo ma consigliato):** un accenno al modulo di adversarial machine learning (sezione 9): quanto sarebbe facile per un attaccante modificare leggermente un URL malevolo per ingannare il vostro classificatore? Anche solo una discussione qualitativa nelle slide finali, collegata alla ricerca del Prof, dà un ottimo valore aggiunto.

**Fase 11 — Slide finali:** le 10 slide richieste, con link GitHub nella prima.

 
## Stato del progetto iniziale

- [ ] Analisi esplorativa dei dati (EDA)
- [ ] Feature engineering (vedi `src/features.py`)
- [ ] Split train/test
- [ ] Addestramento classificatori (Gaussiano, k-NN, SVM, MLP)
- [ ] Valutazione e confronto (cross-validation, confusion matrix)
- [ ] Slide finali
