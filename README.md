# 📊 Data Governance Starter Kit

**Projet personnel** — Solution de gouvernance data pour les équipes finance

Permet de **gouverner la qualité des données financières** : détection anomalies, validation règles métier, scoring qualité temps réel.

- 🐍 **Python ETL** : Génération données, détection anomalies (11 règles), scoring qualité
- 📊 **Power BI Dashboard** : 30+ mesures DAX, KPIs financiers, anomalies détaillées
- 📈 **Streamlit App** : Visualisation interactive des données et anomalies

---

## 🚀 Démarrage Rapide

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Générer les données
python scripts/generate_demo_data.py
python scripts/controle_qualite.py
python scripts/generation_score_qualite.py

# 3. Lancer Streamlit
streamlit run app/streamlit_app.py
```

---

## 📊 Power BI Dashboard

**Fichier** : `powerbi/Dashboard_Finance_Qualite_Donnees.pbix`

![Dashboard Power BI](powerbi/Capture%20d'écran%202026-05-31%20030922.png)

**Tableaux & Mesures** : KPIs financiers (CA, EBITDA), taux validité, anomalies par type/gravité, scoring qualité

---

## 📈 Dashboard Streamlit

![Streamlit Dashboard](screenshots/Capture%20d'écran%202026-05-31%20033400.png)

![Streamlit Anomalies](screenshots/Capture%20d'écran%202026-05-31%20033416.png)

![Streamlit Statistiques](screenshots/Capture%20d'écran%202026-05-31%20033452.png)

---

## 📁 Structure

```
├── scripts/                   # Code Python
│   ├── generate_demo_data.py
│   ├── controle_qualite.py
│   └── generation_score_qualite.py
│
├── data/processed/            # Données nettoyées
│   ├── rapport_anomalies.csv
│   └── donnees_finance_clean.csv
│
├── powerbi/                   # Power BI
│   └── Dashboard_Finance_Qualite_Donnees.pbix
│
└── screenshots/               # Captures d'écran
```

---

## 📊 Métriques

- **305** lignes traitées
- **122** anomalies détectées (21 critiques, 64 majeures, 37 mineures)
- **236** lignes valides après nettoyage
- **77.38%** taux de validité

---

## 🔍 11 Règles de Qualité

Entités/Projets invalides · Montants négatifs · EBITDA incohérents · Doublons · Dates invalides · Valeurs manquantes

---

## 💻 Technologies

Python 3.10+ · Pandas · Power BI (DAX) · Streamlit

---

**Prêt pour production ✅**
