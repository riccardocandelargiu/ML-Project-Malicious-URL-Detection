# Diario di lavoro

Aggiornare questa pagina ogni volta che vengono svolte task o dopo ogni lavoro, anche con
poche righe. 
**Formato: data e ora - autore: cosa è stato fatto.**
L'ideale sarebbe controllare questo file anche ogni volta che si inizia a lavorare per
leggere gli aggiornamenti del collega.

Legenda:
❗ per segnalare dei promemoria, da cancellare una volta risolti.
❓ per segnalare domande poste al collega, da cancellare da chi risponde.

## Cose da fare (checklist rapida, vedi fasi nel README.md per attività più precise)

- [x] Creare struttura repository
- [x] Scaricare dataset e creare subset (15.000 righe)
- [x] EDA sul subset (notebook 01_eda.ipynb)
- [x] Feature engineering (notebook 02_feature_engineering.ipynb)
- [x] Split train/test + primo classificatore
- [x] Valutazione e confronto
- [ ] Slide finali

## Aggiornamenti (in alto il più recente)

**18/07/2026 17:26 - Matteo**: Model selection completa
- Aggiunta la grid search sugli iperparametri anche all'MLP (hidden_layer_sizes e alpha) nel notebook 03: ora TUTTI i modelli ottimizzabili (kNN, SVM, MLP) usano GridSearchCV a 5 fold, come richiesto dal prof nella mail (model selection + variazione iperparametri).
- Risultati finali (balanced acc / macro-F1): MLP ~0.85/~0.87 (migliore), kNN 0.80/0.817, SVM (RBF) 0.78/0.809, Gaussiano 0.583/0.503.
- Matrice di confusione MLP (recall): benign ~97%, defacement ~95%, malware ~84%, phishing ~69% (confuso soprattutto col benign). Conferma la previsione dell'EDA.
- Scritte le conclusioni finali nei notebook 01, 02 e 03.
- Parte tecnica del progetto COMPLETA. Prossimo passo: 10 slide.

**15/07/2026 19:25 - Matteo**: Completato lo step Model Training (notebook 03_model_training.ipynb). Pipeline come nel lab04: split stratificato 80/20 → scaling con MinMaxScaler (stimato solo sul training) → ottimizzazione iperparametri con GridSearchCV a 5 fold → addestramento e valutazione. Modelli: classificatore Gaussiano scritto da zero (come lab03), kNN, SVM (RBF), MLP. Metriche adatte allo sbilanciamento (balanced accuracy, macro-F1). Risultati: MLP migliore (macro-F1 0.873 / bal.acc 0.852), poi kNN (0.817), SVM (0.809), Gaussiano molto sotto (0.503 — l'assunzione gaussiana è violata dalle feature di conteggio/binarie). La matrice di confusione conferma l'EDA: malware ben riconosciuto (recall ~83%), phishing la classe più difficile e confusa col benign (106 casi). Conclusione onesta: l'MLP vince ma guadagna solo ~5-6 punti di F1 sul kNN, che resta un baseline forte e semplice. Salvati data/processed/model_results.csv e le figure (model_comparison.png, confusion_matrix_best.png). Con questo il punto 3 delle direttive (modello + motivazione) è completo; restano le 10 slide.

**15/07/2026 19:25 - Matteo**: Completato lo step Feature Engineering (notebook 02_feature_engineering.ipynb): applicate le 25 feature di features.py al subset, controllo qualità (nessun NaN/infinito/feature costante), validazione del potere discriminante (boxplot per classe, barplot feature binarie, heatmap correlazioni — salvati in figures/), salvato data/processed/features.csv. Osservazioni: has_ip e digit_ratio isolano bene il malware; entropy_url/url_length separano phishing (bassi) da defacement (alti); suspicious_word_count e le feature parole/TLD poco utili; blocco "dimensione" molto ridondante. ❗ IMPORTANTE Riccardo: ho aggiunto la deduplicazione in make_subset.py (drop_duplicates su 'url') PRIMA del campionamento, per evitare data leakage → rimossi 10.072 duplicati e subset rigenerato. Fai git pull e riparti dal nuovo malicious_urls_subset.csv (ho già rieseguito 01_eda sul nuovo subset). Reso anche più robusto il parsing in features.py ("//" → "://").

**14/07/2026 19:45 - Matteo**:
RISPOSTA DOMANDA: Lasciamo perdere le issue e lavoriamo utilizzando i punti definiti nel README e aggiornamenti qui sul PROGRESS.

**14/07/2026 18:30 - Riccardo**:
Creato e implementato il notebook 01_eda che analizza il dataset per verificare che i dati siano ottimali prima
di creare le feature che saranno in seguito classificate.
Và solamente analizzato l'output per annotare gli accorgimenti da definire in un eventuale report o presentazione (❗ promemoria da fare).
I grafici generati dal notebook 01.eda non sono stati salvati su figures per qualche motivo, devo rivederlo, me ne occupo io (❗ promemoria da fare)

**14/07/2026 15:00 - Riccardo**: 
Creata struttura repository e generato subset stratificato
da 15.000 righe (proporzioni originali mantenute tra le 4 classi), quindi considero svolta la fase 0.
Creato il README.md aggiornato con tutte le cose da fare (lavoriamo sui nostri IDE personali
e il lavoro svolto lo inseriamo dentro la cartella notebooks, creando sotto-cartelle dedicate ad ogni fase)
DOMANDA: Usiamo le issue come supporto (come per ISDE) per definire meglio le tasks?
