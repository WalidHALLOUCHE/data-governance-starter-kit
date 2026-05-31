# Architecture du projet Data Governance Starter Kit

## Vue d'ensemble

Ce projet démontre une approche complète de gouvernance data, incluant :
- Génération de données fictives brutes avec anomalies intentionnelles
- Référentiels métier centralisés
- Contrôle qualité automatisé avec détection d'anomalies
- Scoring de qualité pondéré
- Application Streamlit interactive
- Export pour Power BI

## Structure des dossiers

```
data-governance-starter-kit-powerbi-python/
│
├── app/
│   └── streamlit_app.py          # Application Streamlit interactive
│
├── data/
│   ├── raw/                      # Données brutes (générées)
│   │   ├── donnees_finance_raw.csv
│   │   ├── donnees_projets_raw.csv
│   │   └── donnees_kpi_raw.csv
│   │
│   ├── reference/                # Référentiels métier (données de référence)
│   │   ├── referentiel_entites.csv
│   │   ├── referentiel_projets.csv
│   │   ├── referentiel_business_lines.csv
│   │   └── referentiel_kpi.csv
│   │
│   └── processed/                # Données nettoyées et rapports
│       ├── donnees_finance_clean.csv
│       ├── rapport_anomalies.csv
│       ├── score_qualite_donnees.csv
│       ├── synthese_qualite_powerbi.csv
│       └── statistiques_anomalies.csv
│
├── docs/
│   ├── architecture_projet.md    # Ce fichier
│   ├── dictionnaire_donnees.md   # Dictionnaire de toutes les colonnes
│   ├── regles_qualite.md        # Règles de contrôle qualité
│   ├── gouvernance_data.md      # Méthodologie gouvernance
│   ├── guide_powerbi.md         # Comment construire les dashboards
│   └── README_POWERBI.md        # Déploiement Power BI
│
├── scripts/
│   ├── generate_demo_data.py           # Génération des données
│   ├── controle_qualite.py             # Détection des anomalies
│   ├── normalisation_referentiels.py   # Nettoyage des référentiels
│   └── generation_score_qualite.py     # Calcul des scores
│
├── tests/
│   └── test_controle_qualite.py        # Tests unitaires pytest
│
├── powerbi/
│   └── README_POWERBI.md               # Guide Power BI
│
├── screenshots/                         # Captures d'écran (à ajouter)
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Flux de traitement des données

```
1. Génération (generate_demo_data.py)
   ├── Référentiels (entités, projects, KPIs, business lines)
   └── Données brutes avec anomalies intentionnelles
        ├── donnees_finance_raw.csv (300+ lignes)
        ├── donnees_projets_raw.csv
        └── donnees_kpi_raw.csv

2. Normalisation (normalisation_referentiels.py)
   └── Nettoyage des codes et libellés

3. Contrôle qualité (controle_qualite.py)
   ├── Validation des données brutes
   ├── Détection des anomalies
   ├── Génération rapport_anomalies.csv
   └── Génération donnees_finance_clean.csv

4. Scoring (generation_score_qualite.py)
   ├── Calcul du score qualité global
   ├── Score qualité par source
   ├── Statistiques par type d'anomalie
   └── Génération fichiers synthèse

5. Visualisation (streamlit_app.py)
   └── Dashboard interactif local

6. Power BI (guide_powerbi.md)
   └── Utilisation des fichiers synthèse
```

## Fichiers de données

### Données d'entrée (data/raw/)

#### donnees_finance_raw.csv
- **Lignes** : ~305 (300 + doublons)
- **Anomalies** : ~30% volontairement injectées
- **Colonnes** :
  - periode (format YYYY-MM)
  - code_entite (référence)
  - code_projet (référence)
  - code_business_line (référence)
  - ca_eur, opex_eur, capex_eur, ebitda_eur
  - commentaire_source

#### donnees_projets_raw.csv
- **Lignes** : 15
- **Anomalies** : Entités manquantes, business lines inconnues, statuts invalides, dates incohérentes

#### donnees_kpi_raw.csv
- **Lignes** : 14 (12 + doublons)
- **Anomalies** : Formules/unités manquantes, KPIs critiques mal documentés

### Données de référence (data/reference/)

#### referentiel_entites.csv
- 5 entités fictives (France, Allemagne, Espagne, Italie, Maroc)
- Statuts : Actif

#### referentiel_business_lines.csv
- 4 business lines (Développement, Construction, Exploitation, Support)

#### referentiel_projets.csv
- 10 projets fictifs
- Dates cohérentes
- Statuts variés

#### referentiel_kpi.csv
- 8 KPIs financiers
- Niveaux de criticité

### Données de sortie (data/processed/)

#### donnees_finance_clean.csv
- Données brutes sans anomalies
- Prêtes pour analyse/Power BI

#### rapport_anomalies.csv
- **Colonnes** : id_anomalie, source, ligne, type_anomalie, gravité, description, ...
- **Types** : ENTITE_INCONNUE, PROJET_INCONNU, BUSINESS_LINE_INCONNUE, VALEUR_MANQUANTE, MONTANT_NEGATIF, EBITDA_INCOHERENT, DOUBLON, PERIODE_INVALIDE, STATUT_INVALIDE, DATE_INCOHERENTE, KPI_INCOMPLET
- **Gravités** : Critique, Majeure, Mineure

#### score_qualite_donnees.csv
- Score qualité global (0-100%)
- Taux validité
- Counts d'anomalies par gravité
- Pondération appliquée

#### synthese_qualite_powerbi.csv
- Score par source
- Utilisé par Power BI pour la synthèse

#### statistiques_anomalies.csv
- Analyse par type d'anomalie
- Breakdown par gravité

## Types d'anomalies détectées

| Type | Gravité | Description |
|------|---------|-------------|
| ENTITE_INCONNUE | Critique | Code entité non présent dans le référentiel |
| PROJET_INCONNU | Critique | Code projet non présent dans le référentiel |
| BUSINESS_LINE_INCONNUE | Critique | Code BL non présent dans le référentiel |
| VALEUR_MANQUANTE | Majeure | Champ obligatoire vide ou NULL |
| MONTANT_NEGATIF | Majeure | Montant financier < 0 |
| EBITDA_INCOHERENT | Majeure | EBITDA ≠ CA - OPEX |
| DOUBLON | Mineure | Enregistrement dupliqué |
| PERIODE_INVALIDE | Majeure | Format période invalide ou manquant |
| STATUT_INVALIDE | Majeure | Statut non autorisé |
| DATE_INCOHERENTE | Majeure | Date fin avant date début |
| KPI_INCOMPLET | Majeure | KPI sans formule, unité, ou documentation critique |

## Formule de scoring

```
Pondération par gravité :
- Critique = 5 points
- Majeure = 3 points
- Mineure = 1 point

Score qualité = MAX(0, 100 - (points_perdus / total_lignes) * 100)
```

## Commandes principales

```bash
# Installation
pip install -r requirements.txt

# Génération données
python scripts/generate_demo_data.py

# Normalisation
python scripts/normalisation_referentiels.py

# Contrôle qualité
python scripts/controle_qualite.py

# Scoring
python scripts/generation_score_qualite.py

# Application Streamlit
streamlit run app/streamlit_app.py

# Tests
pytest tests/
```

## Technologies utilisées

- **Python 3.10+**
- **Pandas** : Manipulation de données
- **NumPy** : Opérations numériques
- **Streamlit** : Interface web
- **Plotly** : Visualisations
- **Pytest** : Tests
- **Openpyxl** : Support Excel (optionnel)

## Bonnes pratiques implémentées

✅ Séparation raw/reference/processed
✅ Encodage UTF-8 et séparateur `;` uniformes
✅ Pathlib pour les chemins cross-platform
✅ Code PEP8 compliant
✅ Documentation inline pertinente
✅ Tests unitaires
✅ Gestion d'erreurs robuste
✅ Logging détaillé
✅ Répertition des anomalies
✅ Scoring pondéré

## Prochaines étapes

1. Exécuter les scripts dans l'ordre
2. Visualiser dans Streamlit
3. Importer les fichiers synthèse dans Power BI
4. Créer les mesures DAX recommandées
5. Adapter pour vos données réelles
