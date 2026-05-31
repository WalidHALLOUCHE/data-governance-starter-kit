# Gouvernance Data & Performance Financière

**Projet personnel** — Solution de gouvernance data et pilotage financier

**Description** : Solution complète de gouvernance data combinant un pipeline Python, contrôle qualité, scoring, détection d'anomalies, Power BI et Streamlit pour fiabiliser le reporting financier.

---

## Objectif du Projet

**Fiabiliser la prise de décision financière** en garantissant la qualité des données et en détectant les anomalies en temps réel.

Ce projet permet de :

✓ **Pipeline ETL Python** : Extraction, transformation, chargement des données financières  
✓ **11 règles de contrôle qualité** : Validation automatisée (entités, montants, cohérence, dates, doublons, valeurs manquantes)  
✓ **Scoring de validité** : Évaluation pondérée de la qualité globale des données  
✓ **Détection de 122 anomalies** : Classification par type et gravité (critique, majeure, mineure)  
✓ **Dashboard Power BI** : 30+ mesures DAX pour pilotage KPIs et gouvernance data  
✓ **Application Streamlit** : Visualisation interactive et exploration des anomalies  

**Résultat** : Taux de validité de **77,38%** pour 305 lignes traitées, avec traçabilité complète des anomalies.

---

## Démarrage Rapide

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

## Dashboard Power BI

**Fichier** : `powerbi/Dashboard_Finance_Qualite_Donnees.pbix`

![Dashboard Power BI](powerbi/Capture%20d'écran%202026-05-31%20030922.png)

### Tableaux & Indicateurs

- **KPIs Financiers** : Chiffre d'affaires, EBITDA, marges, variations périodiques
- **Indicateurs de Qualité** : Taux de validité, score qualité global, répartition anomalies
- **Détection d'Anomalies** : Tableau filtrable par type, gravité, source
- **Mesures DAX** : 30+ formules pour calculs financiers et indicateurs qualité

---

## Application Interactive - Streamlit

![Streamlit Dashboard](screenshots/Capture%20d'écran%202026-05-31%20033400.png)

![Streamlit Anomalies](screenshots/Capture%20d'écran%202026-05-31%20033416.png)

![Streamlit Statistiques](screenshots/Capture%20d'écran%202026-05-31%20033452.png)

---

## Structure du Projet

```
├── scripts/                   # Code Python (ETL & Contrôle qualité)
│   ├── generate_demo_data.py
│   ├── controle_qualite.py
│   └── generation_score_qualite.py
│
├── data/processed/            # Données nettoyées
│   ├── rapport_anomalies.csv
│   └── donnees_finance_clean.csv
│
├── powerbi/                   # Fichier Power BI
│   └── Dashboard_Finance_Qualite_Donnees.pbix
│
└── screenshots/               # Captures d'écran
```

---

## Résultats & Métriques

| Métrique | Valeur |
|----------|--------|
| Lignes traitées | **305** |
| Anomalies détectées | **122** (21 critiques, 64 majeures, 37 mineures) |
| Lignes valides | **236** |
| Taux de validité | **77,38%** |
| Règles de contrôle | **11** |

---

## Règles de Contrôle Qualité

1. Entités invalides
2. Montants négatifs
3. EBITDA incohérents
4. Doublons
5. Dates invalides
6. Valeurs manquantes
7. Statuts invalides
8. KPI incomplets
9. Projets inconnus
10. Business lines inconnues
11. Périodes invalides

---

## Compétences Démontrées

### Power BI & Business Intelligence

- Modélisation sémantique (tables, relations, schéma en étoile)
- Langage DAX : 30+ mesures (CALCULATE, SWITCH, DATEADD, agrégations)
- Visualisations interactives (KPI cards, matrices, graphiques)
- Thématisation et cohérence visuelle

### Gouvernance Data & Qualité

- Définition et implémentation de règles métier
- Détection d'anomalies avec classification
- Scoring de qualité et algorithme pondéré
- Audit trail et traçabilité complète

### Développement & Intégration

- Pipeline ETL (Python, Pandas)
- Transformation de données et nettoyage
- Dashboards interactifs (Power BI + Streamlit)
- Analyse financière et KPIs

---

## Technologies Utilisées

Python 3.10+ | Pandas | Power BI | DAX | Power Query | Streamlit

---

## Évolutions Futures

Ce projet peut évoluer vers des cas d'usage IA comme :
- Priorisation automatique des anomalies par score de criticité
- Recommandations d'amélioration qualité basées sur historique
- Aide à l'analyse métier et détection de patterns

---

## À Propos

Ce projet démontre une approche complète de gouvernance data, du contrôle qualité à la présentation des indicateurs financiers. Il combine modélisation robuste, automatisation des règles métier et visualisations d'aide à la décision.

**Domaines couverts** : Power BI, DAX, gouvernance data, ETL Python, qualité de données, pilotage financier.

✅ **Prêt pour production** — Code fonctionnel, documenté et testable.
