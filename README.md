# 📊 Tableau de Bord Gouvernance Data & Performance Financière

**Projet personnel** — Pilotage financier intégrant le contrôle qualité des données

**Description** : Dashboard Power BI de gouvernance data et performance financière couvrant le pilotage financier, la qualité des données, la détection d'anomalies, les indicateurs clés (DAX) et l'aide à la décision fiabilisée.

## 🎯 Objectif & Portée

**Fiabiliser la prise de décision financière** en garantissant la qualité des données et en détectant les anomalies en temps réel.

- **Pilotage financier** : KPIs, chiffres d'affaires, marges, performance par période
- **Gouvernance data** : Validation règles métier, scoring qualité, taux de validité
- **Détection d'anomalies** : 11 règles de contrôle, classification par gravité
- **Aide à la décision** : Dashboards interactifs et rapports d'audit

---

## � Contexte Métier

Dans un environnement financier, la **qualité des données** conditionne la fiabilité du reporting et la pertinence des décisions stratégiques.

Ce projet démontre :
- ✅ **Modélisation de données** cohérente (entités, périodes, montants)
- ✅ **Contrôle qualité automatisé** avec 11 règles métier (validation, détection d'anomalies)
- ✅ **Gouvernance data** par scoring qualité et suivi des taux de validité
- ✅ **Pilotage financier** via KPIs fiabilisés (CA, EBITDA, marges)
- ✅ **Documentation des anomalies** pour audit et correction

---

## �🚀 Démarrage Rapide

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

## 📊 Dashboard Power BI - Gouvernance Data & Performance Financière

**Fichier** : `powerbi/Dashboard_Finance_Qualite_Donnees.pbix`

![Dashboard Power BI](powerbi/Capture%20d'écran%202026-05-31%20030922.png)

### Tableaux & Indicateurs
- **KPIs Financiers** : Chiffre d'affaires, EBITDA, marges, variations périodiques
- **Indicateurs de Qualité** : Taux de validité, score qualité global, répartition anomalies
- **Détection d'Anomalies** : Tableau filtrable par type, gravité, source
- **Mesures DAX** : 30+ formules pour calculs financiers et indicateurs qualité

---

## 📈 Application Interactive - Visualisation Données

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

## 📊 Indicateurs Clés - Résultats de Qualité

| Métrique | Valeur |
|----------|--------|
| Lignes traitées | **305** |
| Anomalies détectées | **122** (21 critiques, 64 majeures, 37 mineures) |
| Lignes valides | **236** (77.38% taux de validité) |
| Règles de contrôle | **11** règles métier |

---

## 🔍 Règles de Contrôle Qualité (11 Critères)

Entités invalides · Montants négatifs · EBITDA incohérents · Doublons · Dates invalides · Valeurs manquantes · Statuts invalides · KPI incomplets · Projets inconnus · Business lines inconnues

---

## 💡 Compétences Démontrées

### Power BI & Analytics
- ✅ **Modélisation sémantique** : Tables, relations, schéma en étoile
- ✅ **Langage DAX** : 30+ mesures (CALCULATE, SWITCH, DATEADD, agrégations)
- ✅ **Visualisations** : KPI cards, tables matrice, graphiques interactifs
- ✅ **Thématisation** : Palettes professionnelles, cohérence visuelle

### Données & Gouvernance
- ✅ **Qualité data** : Définition et implémentation de règles métier
- ✅ **Détection anomalies** : Classification par type et gravité
- ✅ **Scoring qualité** : Algorithme pondéré de fiabilité
- ✅ **Audit trail** : Traçabilité des anomalies détectées

### Développement & Intégration
- ✅ **Pipeline ETL** : Extraction, transformation, chargement
- ✅ **Python** : Pandas, validation données, scoring
- ✅ **Dashboards interactifs** : Power BI + Streamlit

---

## 💻 Technologies

Python 3.10+ · Pandas · Power BI (DAX, Power Query) · Streamlit

---

## 📌 À Propos

Ce projet démontre une **approche complète de gouvernance data** : de la modélisation au contrôle qualité, en passant par la présentation des indicateurs financiers. 

**Aligné avec les besoins** d'un **Chef de projet Data / Référent déploiement IA** en termes de :
- Rigueur méthodologique (11 règles, documentation anomalies)
- Maîtrise outils BI (Power BI, DAX, modélisation)
- Pilotage par la donnée (KPIs, scoring, tableaux de bord)
- Gouvernance et fiabilisation du reporting

✅ **Production-ready** — Code fonctionnel, dashboards interactifs, documenté
