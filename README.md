# Data Governance Starter Kit — Référentiel & qualité des données

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

## 🎯 Objectif du projet

**Data Governance Starter Kit** est un projet de démonstration complet et professionnel montrant comment mettre en place une gouvernance data robuste en entreprise.

Ce starter kit simule un **environnement réaliste** avec :
- 📊 Données brutes fictives avec anomalies volontairement injectées
- 📋 Référentiels métier centralisés
- ✅ Contrôles qualité automatisés (11 règles appliquées)
- 📈 Scoring de qualité pondéré
- 🎨 Dashboard interactif Streamlit
- 📑 Synthèses pour Power BI
- 📚 Documentation complète en français

**Ce projet démontre** :
- Gouvernance et référentiels données
- Détection et suivi des anomalies
- Qualité et fiabilisation des données
- Préparation des données pour BI/IA
- Architecture data scalable
- Bonnes pratiques Python/Pandas

---

## � À PROPOS DE CE PROJET

### 🎓 Projet Personnel

Ce projet a été conçu et développé **en intégralité** comme un **projet personnel** pour démontrer :

#### 🔧 Compétences Techniques Couvertes

| Domaine | Compétences Démontrées |
|---------|------------------------|
| **Python Data** | Pandas, NumPy, validation données, ETL |
| **Data Quality** | Règles métier, détection anomalies, scoring pondéré |
| **Architecture** | Modèle en couches, séparation responsabilités, scalabilité |
| **BI/Analytics** | Power BI (DAX, Power Query, thème custom), Streamlit |
| **Soft Skills** | Documentation, API métier, spécifications visuelles |

#### 💡 Objectif Professionnel

Ce projet **simule un cas réel d'entreprise** avec :
- ✅ **Données réalistes** : 305+ lignes avec ~30% d'anomalies intentionnelles
- ✅ **11 règles métier** : Détecter entités invalides, montants négatifs, EBITDA incohérents, etc.
- ✅ **Scoring pondéré** : Critère (5 pts) > Majeure (3 pts) > Mineure (1 pt)
- ✅ **Dashboard complet** : 5 pages d'analyse + 30 mesures DAX
- ✅ **Documentation professionnelle** : Guides, dictionnaire, architecture

#### 🎯 Ce que cela démontre

Un recruteur y verra :
- 👨‍💻 **Capacité à concevoir une architecture data** complète (source → nettoyage → analyse)
- 📊 **Maîtrise de Power BI** en production (DAX avancé, thème custom, modèle relationnel)
- 🐍 **Expertise Python/Pandas** pour l'ETL et la qualité des données
- 📚 **Rigueur documentaire** (documentation 6 guides + code commenté)
- 🧪 **Bonnes pratiques** (tests, modularité, réutilisabilité)
- 🚀 **Mentalité produit** : Livrable prêt pour production, pas juste un prototype

---

## �📁 Structure du projet

```
data-governance-starter-kit-powerbi-python/
│
├── app/
│   └── streamlit_app.py               # Dashboard interactif
│
├── data/
│   ├── raw/                           # Données brutes (générées)
│   │   ├── donnees_finance_raw.csv    # 305 lignes avec anomalies
│   │   ├── donnees_projets_raw.csv    # Projets avec anomalies
│   │   └── donnees_kpi_raw.csv        # KPIs avec anomalies
│   ├── reference/                     # Référentiels métier
│   │   ├── referentiel_entites.csv
│   │   ├── referentiel_projets.csv
│   │   ├── referentiel_business_lines.csv
│   │   └── referentiel_kpi.csv
│   └── processed/                     # Données nettoyées & rapports
│       ├── donnees_finance_clean.csv
│       ├── rapport_anomalies.csv
│       ├── score_qualite_donnees.csv
│       └── synthese_qualite_powerbi.csv
│
├── docs/
│   ├── architecture_projet.md         # Architecture complète
│   ├── dictionnaire_donnees.md        # Dictionnaire colonnes
│   ├── regles_qualite.md             # 11 règles de contrôle
│   ├── gouvernance_data.md           # Méthodologie gouvernance
│   ├── guide_powerbi.md              # Construction dashboard
│   └── README_POWERBI.md             # Déploiement Power BI
│
├── scripts/
│   ├── generate_demo_data.py         # Génération données + anomalies
│   ├── controle_qualite.py           # Détection anomalies
│   ├── normalisation_referentiels.py # Nettoyage référentiels
│   └── generation_score_qualite.py   # Calcul scores
│
├── tests/
│   └── test_controle_qualite.py      # Tests pytest
│
├── powerbi/
│   └── README_POWERBI.md             # Instructions Power BI
│
├── .gitignore
├── requirements.txt
└── README.md                          # Ce fichier
```

---

## 🚀 Démarrage rapide

### Prérequis

- Python 3.10+
- Pip

### Installation

```bash
# 1. Cloner le repository
git clone https://github.com/votre-username/data-governance-starter-kit-powerbi-python.git
cd data-governance-starter-kit-powerbi-python

# 2. Créer un environnement virtuel
python -m venv venv
source venv/Scripts/activate  # Windows
# OU
source venv/bin/activate      # Linux/Mac

# 3. Installer les dépendances
pip install -r requirements.txt
```

### Exécution

```bash
# 1. Générer les données fictives de démonstration
python scripts/generate_demo_data.py

# 2. Exécuter le contrôle qualité (détection anomalies)
python scripts/controle_qualite.py

# 3. Calculer les scores qualité
python scripts/generation_score_qualite.py

# 4. Lancer le dashboard Streamlit
streamlit run app/streamlit_app.py
```

L'application s'ouvre automatiquement à `http://localhost:8501`

---

## 📊 Fonctionnalités principales

### 1️⃣ Génération des données

```bash
python scripts/generate_demo_data.py
```

**Génère automatiquement** :
- 5 entités fictives (France, Allemagne, Espagne, Italie, Maroc)
- 4 business lines (Développement, Construction, Exploitation, Support)
- 10 projets fictifs
- 305+ lignes de données finance avec **~30% d'anomalies intentionnelles**

**Anomalies volontaires injectées** :
- Entités/projets/business lines inconnues
- Montants négatifs
- EBITDA incohérents
- Doublons
- Périodes invalides
- Valeurs manquantes

### 2️⃣ Contrôle qualité automatisé

```bash
python scripts/controle_qualite.py
```

**Détecte 11 types d'anomalies** :

| Type | Gravité | Description |
|------|---------|-------------|
| ENTITE_INCONNUE | 🔴 Critique | Code entité non validé |
| PROJET_INCONNU | 🔴 Critique | Code projet non validé |
| BUSINESS_LINE_INCONNUE | 🔴 Critique | Code BL non validé |
| VALEUR_MANQUANTE | 🟠 Majeure | Champ obligatoire vide |
| MONTANT_NEGATIF | 🟠 Majeure | CA/OPEX/CAPEX < 0 |
| EBITDA_INCOHERENT | 🟠 Majeure | EBITDA ≠ CA - OPEX |
| DOUBLON | 🟢 Mineure | Enregistrement dupliqué |
| PERIODE_INVALIDE | 🟠 Majeure | Format YYYY-MM invalide |
| STATUT_INVALIDE | 🟠 Majeure | Statut non autorisé |
| DATE_INCOHERENTE | 🟠 Majeure | Fin avant début |
| KPI_INCOMPLET | 🟠 Majeure | KPI sans formule/unité |

**Génère** :
- `rapport_anomalies.csv` : Détail de chaque anomalie avec ID unique
- `donnees_finance_clean.csv` : Données nettoyées
- Résumé console

### 3️⃣ Scoring qualité pondéré

```bash
python scripts/generation_score_qualite.py
```

**Calcule** :
- Score qualité global (0-100%)
- Score qualité par source
- Statistiques anomalies par type
- Taux validité

**Pondération** :
```
Critique = 5 points
Majeure = 3 points
Mineure = 1 point
Score = MAX(0, 100 - (points_perdus / total_lignes) * 100)
```

**Exemple** : Si 100 lignes avec 1 Critique (5 pts) + 2 Majeures (6 pts) = 11 pts
→ Score = 100 - 11 = **89%**

### 4️⃣ Dashboard Streamlit interactif

```bash
streamlit run app/streamlit_app.py
```

**Affiche** :
- 📈 KPIs : lignes contrôlées, anomalies totales, critiques, score qualité
- 📊 Graphiques interactifs Plotly :
  - Anomalies par type (bar chart)
  - Anomalies par gravité (pie chart)
  - Anomalies par source
  - Score qualité par source
- 🔍 Tableau anomalies filtrable et interactive
- 🎚️ Filtres dynamiques : source, gravité, type

### 5️⃣ Dashboard Power BI — Fichier Complet 🏆

**🎯 Fichier Principal** : [`powerbi/Dashboard_Finance_Qualite_Donnees.pbix`](powerbi/)

**✅ Produit Professionnel Complet** — Construit entièrement par ce projet Python, prêt pour une utilisation en production.

Téléchargez et ouvrez dans [Power BI Desktop](https://powerbi.microsoft.com) (gratuit).

#### 📊 Architecture Power BI

**Modèle de Données** :
- 5 tables intégrées (données nettoyées par Python)
- Relations configurées automatiquement
- Calendrier intelligent avec années/mois/trimestres
- Clés de jointure optimisées

**Mesures DAX** (~30 mesures) :
- Mesures de volume (lignes, sources, entités, projets)
- Mesures d'anomalies (critiques, majeures, mineures)
- Mesures de qualité (scores, taux validité)
- Mesures financières (CA, OPEX, CAPEX, EBITDA)
- Mesures temporelles (variation MoM, titres dynamiques)

**Thème Custom** (Fichier JSON) :
- Palette violet-rose professionnel
- Cohérence visuelle sur 5 pages
- Couleurs par gravité d'anomalie (rouge, orange, vert)

#### 📈 Pages d'Analyse (5 Pages)

| Page | Cibles | Visuels |
|------|--------|---------|
| **1. Executive Summary** | C-Level | KPIs clés, CA/EBITDA trends, donut gravités, top anomalies |
| **2. Qualité & Gouvernance** | Data Officer | Jauge score, bar anomalies, matrix source×gravité |
| **3. Anomalies Détaillées** | Analyst | Slicers avancés, table interactive, filtering |
| **4. Performance Financière** | CFO | CA/EBITDA par période/entité/BL/projet, trends |
| **5. Audit Technique** | DQA | Tables brutes, statistiques, traçabilité |

#### 📊 Volumétrie Réelle

- **CA total** : 588M€ 
- **EBITDA total** : 398.88M€ (marge : 67.86%)
- **Lignes contrôlées** : 236 lignes propres
- **Anomalies** : 122 détectées (21 critiques, 64 majeures, 37 mineures)
- **Taux validité** : 77.38%
- **Couverture** : Jan 2023 → Nov 2024 (22 périodes)

#### 🛠️ Compétences Power BI Démontrées

- ✅ **DAX avancé** : CALCULATE, SWITCH, DIVIDE avec gestion nulle, ADDCOLUMNS
- ✅ **Power Query (M)** : Import dynamique CSV, transformation de type, gestion encodage
- ✅ **Modèle relationnel** : Schéma en étoile, relations 1:N, pas de boucles
- ✅ **Formatage personnalisé** : Devise €, pourcentages, thème global
- ✅ **Visualisations avancées** : KPI cards, bar, line, donut, matrix, table interactive
- ✅ **UX/Design** : Navigation fluide, slicers contextuels, drill-through possible

#### 📚 Documentation du Dashboard

Pour **reconstruire depuis zéro** (si Power BI Desktop) :
1. Voir [`PowerBI_Finance_Qualite_Kit/README_IMPORT_RAPIDE.md`](PowerBI_Finance_Qualite_Kit/README_IMPORT_RAPIDE.md) — 11 étapes simples
2. Voir [`docs/guide_powerbi.md`](docs/guide_powerbi.md) — Guide de construction complet (avec screenshots)
3. Voir [`PowerBI_Finance_Qualite_Kit/docs/SPEC_VISUELLE_DASHBOARD.md`](PowerBI_Finance_Qualite_Kit/docs/SPEC_VISUELLE_DASHBOARD.md) — Spécifications des 5 pages

---

## 📚 Documentation

### Pour démarrer
- 📖 [Architecture du projet](docs/architecture_projet.md) : Vue d'ensemble

### Pour comprendre les données
- 📖 [Dictionnaire des données](docs/dictionnaire_donnees.md) : Toutes les colonnes documentées
- 📖 [Règles de qualité](docs/regles_qualite.md) : 11 règles détaillées

### Pour la gouvernance
- 📖 [Gouvernance data](docs/gouvernance_data.md) : Méthodologie et bonnes pratiques

### Pour Power BI
- 📖 [Guide Power BI](docs/guide_powerbi.md) : Construire les dashboards (5 pages recommandées)
- 📖 [Déploiement Power BI](powerbi/README_POWERBI.md) : Instructions d'intégration

---

## 🔬 Tests

```bash
# Exécuter les tests pytest
pytest tests/ -v

# Ou lancer test spécifique
pytest tests/test_controle_qualite.py::test_entite_inconnue_detectee -v
```

**Tests inclus** :
- ✅ Détection entité inconnue
- ✅ Détection montant négatif
- ✅ Détection EBITDA incohérent
- ✅ Colonnes rapport anomalies
- ✅ Unicité IDs anomalies
- ✅ Validité gravités

---

## 💾 Données et confidententialité

### ⚠️ Données 100% fictives

Ce projet utilise **exclusivement des données fictives** :

- ✅ Aucune donnée réelle d'entreprise
- ✅ Aucun nom d'entreprise réelle
- ✅ Aucune donnée personnelle
- ✅ Aucun logo ou identifiant réelle
- ✅ Aucune donnée confidentielle
- ✅ Toutes les données sont générées automatiquement

**Adaptation à vos données réelles** :
1. Remplacer les fichiers CSV raw par vos propres données
2. Adapter les référentiels dans `data/reference/`
3. Ajuster les règles qualité dans `controle_qualite.py`
4. Re-exécuter les scripts

---

## 🛠️ Technologies utilisées

| Technologie | Version | Rôle |
|-------------|---------|------|
| **Python** | 3.10+ | Langage principal |
| **Pandas** | 2.1.4 | Manipulation données |
| **NumPy** | 1.26.3 | Calculs numériques |
| **Streamlit** | 1.28.1 | Dashboard web |
| **Plotly** | 5.18.0 | Visualisations interactives |
| **pytest** | 7.4.3 | Tests unitaires |
| **Openpyxl** | 3.11.0 | Support Excel (optionnel) |

---

## 📊 Cas d'usage

### Cas 1️⃣ : Préparation Power BI

1. Lancer les scripts (`generate_demo_data.py` → `controle_qualite.py` → `generation_score_qualite.py`)
2. Exporter fichiers de `data/processed/` vers Power BI
3. Importer dans Power BI Desktop
4. Construire pages selon [guide_powerbi.md](docs/guide_powerbi.md)
5. Publier sur Power BI Service

### Cas 2️⃣ : Modèle Machine Learning

1. Charger `donnees_finance_clean.csv`
2. Vérifier score qualité ≥ 85%
3. Consulter `rapport_anomalies.csv` pour data drift
4. Créer features à partir données propres
5. Entraîner modèle ML
6. Valider prédictions vs anomalies historiques

### Cas 3️⃣ : Audit et conformité

1. Consulter `rapport_anomalies.csv`
2. Tracer corrections appliquées
3. Valider score qualité > seuil
4. Générer certificat qualité données
5. Archiver traces pour audit

### Cas 4️⃣ : Montée en charge

1. Adapter scripts pour volume réel (millions lignes)
2. Implémenter processing par batch (Airflow/Prefect)
3. Ajouter monitoring temps réel (streaming)
4. Déployer en production (Azure/AWS/GCP)

---

## 🎓 Compétences démontrées

Ce projet montre expertise dans :

✅ **Gouvernance data**
- Référentiels métier centralisés
- Traçabilité complète
- Responsabilités clairement définies

✅ **Qualité des données**
- 11 règles contrôle automatisées
- Pondération anomalies
- Scoring robuste

✅ **Python/Pandas**
- Code PEP8 compliant
- Gestion d'erreurs
- Performances optimisées
- Tests unitaires

✅ **Business Intelligence**
- Préparation Power BI
- DAX et mesures calculées
- Dashboards interactifs
- Storytelling data

✅ **Documentationdonnées**
- Dictionnaire complet
- Règles métier
- Architecture claire
- Bonnes pratiques

---

## 🔄 Workflow complet

```
1. GÉNÉRATION (generate_demo_data.py)
   ↓
   ├─ Référentiels (entités, projets, KPI, BL)
   └─ Données brutes RAW (+ anomalies intentionnelles)
   
2. NORMALISATION (normalisation_referentiels.py)
   ↓
   └─ Référentiels nettoyés
   
3. CONTRÔLE QUALITÉ (controle_qualite.py)
   ↓
   ├─ Validation 11 règles
   ├─ Génération rapport_anomalies.csv
   └─ Génération donnees_finance_clean.csv
   
4. SCORING (generation_score_qualite.py)
   ↓
   ├─ Score qualité global (0-100%)
   ├─ Score par source
   └─ Statistiques par type anomalie
   
5. VISUALISATION (streamlit_app.py)
   ↓
   └─ Dashboard interactif local
   
6. POWER BI (guide_powerbi.md)
   ↓
   ├─ Import fichiers synthèse
   ├─ Création mesures DAX
   ├─ Construction 5 pages
   └─ Publication Power BI Service
```

---

## 📋 Commandes principales

```bash
# Initialisation
python scripts/generate_demo_data.py              # Générer données

# Processus
python scripts/normalisation_referentiels.py      # Normaliser
python scripts/controle_qualite.py                # Contrôle qualité
python scripts/generation_score_qualite.py        # Calculer scores

# Application
streamlit run app/streamlit_app.py                # Lancer dashboard

# Tests
pytest tests/ -v                                  # Exécuter tests
pytest tests/ --cov=scripts                       # Couverture code
```

---

## 🤝 Contribution

Ce projet est un starter kit. Pour adapter à vos besoins :

1. **Modifier les données** : Remplacer CSV raw par vos propres données
2. **Adapter les référentiels** : Ajouter vos codes métier
3. **Ajouter règles qualité** : Étendre `controle_qualite.py`
4. **Personnaliser dashboard** : Modifier `streamlit_app.py`
5. **Étendre Power BI** : Ajouter pages selon votre contexte

---

## 📞 Support

### Documentation
- 📖 Voir dossier `docs/` pour documentation complète
- 📖 Voir `powerbi/` pour instructions Power BI

### Troubleshooting
- Python ne trouve pas Pandas → Vérifier l'environnement virtuel
- Streamlit n'affiche rien → Vérifier fichiers CSV générés
- Power BI erreur séparateur → Utiliser `;` (point-virgule)

### Questions
- Consulter [architecture_projet.md](docs/architecture_projet.md) pour vue d'ensemble
- Consulter [dictionnaire_donnees.md](docs/dictionnaire_donnees.md) pour colonnes
- Consulter [regles_qualite.md](docs/regles_qualite.md) pour anomalies

---

## 📄 License

MIT License - Libre d'utilisation

---

## 👤 Auteur

**Walid HALLOUCHE**  
Data Analyst / BI Analyst Power BI

---

## 🎯 Conclusion

Ce starter kit démontre une **approche professionnelle et scalable** de la gouvernance data.

**Prochaines étapes** :
1. ✅ Exécuter les scripts et voir les résultats
2. ✅ Explorer le dashboard Streamlit
3. ✅ Construire le tableau Power BI
4. ✅ Adapter à vos propres données
5. 🔄 Déployer en production

**Bon travail !** 🚀
