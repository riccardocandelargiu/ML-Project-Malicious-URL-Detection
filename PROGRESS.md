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
- [ ] Feature engineering (notebook 02_feature_engineering.ipynb)
- [ ] Split train/test + primo classificatore
- [ ] Valutazione e confronto
- [ ] Slide finali

## Aggiornamenti (in alto il più recente)

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
