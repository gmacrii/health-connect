import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

np.random.seed(7)
n = 300

battiti = np.random.normal(145, 20, n).clip(60, 200)
sonno = np.random.normal(7.0, 1.2, n).clip(3, 10)
carico = np.random.normal(300, 80, n).clip(50, 600)
riposo = np.random.randint(0, 7, n)

punteggio = ((battiti > 170).astype(int) * 2 +
             (sonno < 6).astype(int) * 2 +
             (carico > 400).astype(int) * 1 +
             (riposo == 0).astype(int) * 1)

def calcola_classe(p):
    if p <= 1: return 'BASSO'
    elif p <= 3: return 'MEDIO'
    else: return 'ALTO'

rischio = np.array([calcola_classe(p) for p in punteggio])

df = pd.DataFrame({
    'battiti': battiti, 
    'sonno': sonno, 
    'carico': carico, 
    'riposo': riposo, 
    'rischio': rischio
})

ordine_classi = ['BASSO', 'MEDIO', 'ALTO']
mappa_numerica = {'BASSO': 0, 'MEDIO': 1, 'ALTO': 2}
mappa_inversa = {0: 'BASSO', 1: 'MEDIO', 2: 'ALTO'}

X = df[['battiti', 'sonno', 'carico', 'riposo']]
y = df['rischio'].map(mappa_numerica)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

modello = RandomForestClassifier(n_estimators=100, random_state=42)
modello.fit(X_train, y_train)

y_pred = modello.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"--- HEALTHCONNECT ANALYTICS ---")
print(f"Sessioni analizzate: {len(df)}")
print(f"Accuratezza Modello: {acc*100:.1f}%\n")

cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(5, 4))
cax = ax.imshow(cm, cmap='YlGnBu')

ax.set_xticks([0, 1, 2])
ax.set_yticks([0, 1, 2])
ax.set_xticklabels(ordine_classi)
ax.set_yticklabels(ordine_classi)
ax.set_xlabel('Predizione')
ax.set_ylabel('Reale')
ax.set_title('Matrice di Confusione', fontweight='bold')

for i in range(3):
    for j in range(3):
        ax.text(j, i, str(cm[i, j]), ha='center', va='center', 
                color='white' if cm[i, j] > cm.max()/2 else 'black', fontweight='bold')

plt.tight_layout()
plt.show()

atleti_input = pd.DataFrame([
    [178, 4.5, 480, 0],
    [130, 8.0, 200, 2],
    [165, 5.5, 380, 0]
], columns=['battiti', 'sonno', 'carico', 'riposo'])

consigli = {
    'ALTO': 'RIPOSO OBBLIGATORIO.',
    'MEDIO': 'RIDUCI INTENSITÀ DEL 30%.',
    'BASSO': 'OTTIMA CONDIZIONE. ALLENATI!'
}

nomi = ['Marco', 'Sofia', 'Luca']
predizioni_num = modello.predict(atleti_input)

print("SIMULATORE DI CARICO:")
for nome, p_num in zip(nomi, predizioni_num):
    classe = mappa_inversa[p_num]
    print(f" > {nome:6}: {classe:6} -> {consigli[classe]}")