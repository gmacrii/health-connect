# 🧠 HealthConnect Analytics

Sistema di simulazione e analisi del rischio fisico basato su dati sintetici di allenamento. Il progetto utilizza un modello di Machine Learning (*Random Forest*) per classificare il livello di rischio degli atleti e fornire consigli pratici.

---

## 📌 Descrizione

**HealthConnect Analytics** genera un dataset simulato di sessioni sportive e utilizza un modello di classificazione per valutare il rischio fisico in base a:

- Battiti cardiaci
- Ore di sonno
- Carico di allenamento
- Giorni di riposo

Il sistema assegna un livello di rischio:

- 🟢 **BASSO**
- 🟡 **MEDIO**
- 🔴 **ALTO**

e fornisce raccomandazioni personalizzate.

---

## ⚙️ Tecnologie utilizzate

- Python 3
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

## 📊 Funzionalità principali

- ✅ Generazione dataset sintetico  
- ✅ Calcolo del punteggio di rischio  
- ✅ Classificazione con Random Forest  
- ✅ Valutazione del modello (accuratezza)  
- ✅ Visualizzazione matrice di confusione  
- ✅ Simulazione su nuovi atleti  
- ✅ Sistema di raccomandazioni  

---

## 🧪 Logica del rischio

Il punteggio viene calcolato secondo queste regole:

| Condizione                | Punti |
|-------------------------|------|
| Battiti > 170           | +2   |
| Sonno < 6 ore           | +2   |
| Carico > 400            | +1   |
| Nessun giorno di riposo | +1   |

### Classificazione

- **0–1 → BASSO**
- **2–3 → MEDIO**
- **4+ → ALTO**

---

## 🚀 Come eseguire il progetto

1. Clona il repository:
```bash
git clone https://github.com/tuo-username/healthconnect-analytics.git
cd healthconnect-analytics
````

2. Installa le dipendenze:

```bash
pip install numpy pandas matplotlib scikit-learn
```

3. Esegui lo script:

```bash
python main.py
```

---

## 📈 Output

Il programma mostrerà:

* Accuratezza del modello
* Matrice di confusione (grafica)
* Simulazione di rischio per atleti

### Esempio output

```
--- HEALTHCONNECT ANALYTICS ---
Sessioni analizzate: 300
Accuratezza Modello: 93.3%

SIMULATORE DI CARICO:
 > Marco : ALTO   -> RIPOSO OBBLIGATORIO.
 > Sofia : BASSO  -> OTTIMA CONDIZIONE. ALLENATI!
 > Luca  : MEDIO  -> RIDUCI INTENSITÀ DEL 30%.
```

---

## 🧑‍💻 Simulazione atleti

| Nome  | Battiti | Sonno | Carico | Riposo |
| ----- | ------- | ----- | ------ | ------ |
| Marco | 178     | 4.5   | 480    | 0      |
| Sofia | 130     | 8.0   | 200    | 2      |
| Luca  | 165     | 5.5   | 380    | 0      |

---

## 🧠 Modello utilizzato

* RandomForestClassifier
* 100 alberi decisionali
* Training/Test split: 80/20
* Stratificazione per classi

---

## 📌 Autori

- Macrì Giovanni
- Torretti Massimo
- Amati Giovanni
- Cara Samuele
- Gullotto Antonio

```
```
