# 📊 Data Governance Starter Kit

**Projet personnel** — Gouvernance data avec Python + Power BI

- 🐍 **Python ETL** : Génération données, détection anomalies, scoring qualité
- 📊 **Power BI Dashboard** : 5 pages, 30 mesures DAX, 588M€ de données  
- 📸 **Dashboards en action** : Voir ci-dessous

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

**Contient:**
- Executive Summary (KPIs clés)
- Qualité & Gouvernance (scores, validité)
- Anomalies Détaillées (table filtrable)
- Performance Financière (CA/EBITDA par période)
- Audit Technique (tables brutes)

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

- **305** lignes brutes
- **122** anomalies détectées (21 critiques, 64 majeures, 37 mineures)
- **236** lignes valides
- **588M€** CA | **398.88M€** EBITDA
- **77.38%** taux validité

---

## 🔍 11 Règles de Qualité

Entités/Projets invalides · Montants négatifs · EBITDA incohérents · Doublons · Dates invalides · Valeurs manquantes

---

## 💻 Technologies

Python 3.10+ · Pandas · Power BI (DAX) · Streamlit

---

**Prêt pour production ✅**
