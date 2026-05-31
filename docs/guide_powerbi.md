# Guide Power BI - Construction du dashboard

## Objectif

Ce guide explique comment construire un dashboard Power BI professionnel à partir des fichiers CSV générés par le starter kit.

---

## Étape 1 : Préparer les fichiers d'entrée

### Fichiers requis

Copier dans un dossier PowerBI les fichiers suivants depuis `data/processed/` :

```
📁 PowerBI/
├── donnees_finance_clean.csv       ← Données nettoyées
├── rapport_anomalies.csv          ← Détail des anomalies
├── synthese_qualite_powerbi.csv    ← Score qualité par source
└── statistiques_anomalies.csv      ← Statistiques par type
```

### Vérifier les formats

- ✅ Encodage UTF-8
- ✅ Séparateur `;` (point-virgule)
- ✅ Décimales avec `.`
- ✅ Dates au format YYYY-MM-DD

---

## Étape 2 : Import dans Power BI Desktop

### Créer un nouveau projet

1. Ouvrir **Power BI Desktop**
2. Cliquer **Obtenir les données** → **Texte/CSV**
3. Naviguer vers le dossier `PowerBI/`

### Charger les données

**Pour chaque fichier CSV** :

1. Sélectionner le fichier
2. Cliquer **Charger** (ou **Transformer les données** pour ajustements)
3. À la question du délimiteur → Sélectionner **Point-virgule (;)**

### Ordre de chargement recommandé

1. `donnees_finance_clean.csv` (principale)
2. `synthese_qualite_powerbi.csv`
3. `rapport_anomalies.csv`
4. `statistiques_anomalies.csv`

---

## Étape 3 : Modéliser les données (Data Model)

### Vue Modèle

Pour chaque table, vérifier/corriger les types :

#### Table `donnees_finance_clean`
| Colonne | Type | Notes |
|---------|------|-------|
| periode | Texte | → **Date** (format YYYY-MM) |
| code_entite | Texte | Garder texte |
| code_projet | Texte | Garder texte |
| code_business_line | Texte | Garder texte |
| ca_eur | Décimal | ✅ |
| opex_eur | Décimal | ✅ |
| capex_eur | Décimal | ✅ |
| ebitda_eur | Décimal | ✅ |

#### Table `synthese_qualite_powerbi`
| Colonne | Type |
|---------|------|
| source | Texte |
| total_lignes | Nombre entier |
| total_anomalies | Nombre entier |
| score_qualite | Décimal |

#### Table `rapport_anomalies`
| Colonne | Type |
|---------|------|
| id_anomalie | Texte |
| type_anomalie | Texte |
| gravite | Texte |
| date_detection | Date/Heure |

### Créer des relations

```
donnees_finance_clean ──┐
                        ├──→ synthese_qualite_powerbi
rapport_anomalies ──────┘
```

**Relations créer** :
- `donnees_finance_clean.code_entite` → `synthese_qualite_powerbi.source`
- `rapport_anomalies.type_anomalie` → `statistiques_anomalies.type_anomalie`

---

## Étape 4 : Créer les mesures DAX

### Mesures essentielles

Aller dans l'onglet **Modèle** → **Nouvelle mesure** pour chaque :

#### 1. Total anomalies détectées

```dax
Nombre Anomalies = COUNTA('rapport_anomalies'[id_anomalie])
```

#### 2. Anomalies par gravité

```dax
Anom Critiques = CALCULATE(
    COUNTA('rapport_anomalies'[id_anomalie]),
    'rapport_anomalies'[gravite] = "Critique"
)

Anom Majeures = CALCULATE(
    COUNTA('rapport_anomalies'[id_anomalie]),
    'rapport_anomalies'[gravite] = "Majeure"
)

Anom Mineures = CALCULATE(
    COUNTA('rapport_anomalies'[id_anomalie]),
    'rapport_anomalies'[gravite] = "Mineure"
)
```

#### 3. Score qualité global

```dax
Score Qualite Global = AVERAGE('synthese_qualite_powerbi'[score_qualite])
```

#### 4. Taux anomalies critiques

```dax
Taux Anom Critiques = 
    DIVIDE(
        [Anom Critiques],
        [Nombre Anomalies],
        0
    ) * 100
```

#### 5. Total lignes contrôlées

```dax
Total Lignes = COUNTA('donnees_finance_clean'[periode])
```

#### 6. Taux validité

```dax
Taux Validite = 
    DIVIDE(
        COUNTA('donnees_finance_clean'[periode]),
        [Total Lignes],
        0
    ) * 100
```

#### 7. Sommes financières

```dax
Total CA = SUM('donnees_finance_clean'[ca_eur])
Total OPEX = SUM('donnees_finance_clean'[opex_eur])
Total CAPEX = SUM('donnees_finance_clean'[capex_eur])
Total EBITDA = SUM('donnees_finance_clean'[ebitda_eur])
```

#### 8. EBITDA Margin %

```dax
Marge EBITDA = 
    DIVIDE(
        [Total EBITDA],
        [Total CA],
        0
    ) * 100
```

#### 9. Nombre sources contrôlées

```dax
Nombre Sources = COUNTA('synthese_qualite_powerbi'[source])
```

---

## Étape 5 : Construire les pages du rapport

### Page 1 : Vue qualité globale

**Objectif** : Vue d'ensemble de la qualité des données

#### Visuels

**Ligne 1 : KPIs principaux**
- Carte simple × 4 :
  - 📊 Total lignes contrôlées = `[Total Lignes]`
  - 📊 Total anomalies = `[Nombre Anomalies]`
  - 📊 Anomalies critiques = `[Anom Critiques]`
  - 📊 Score qualité = `[Score Qualite Global]` (format %)

**Ligne 2 : Graphiques**
- **Gauge (jauge)** : Score qualité global
  - Cible : 85% (vert), 70% (jaune), 0% (rouge)
  - Mesure : `[Score Qualite Global]`

- **Pie Chart** : Anomalies par gravité
  - Légende : `rapport_anomalies[gravite]`
  - Valeurs : `Nombre Anomalies` (filtrée par gravité)
  - Couleurs : Critique=rouge, Majeure=orange, Mineure=vert

**Ligne 3 : Tendances**
- **Line Chart** : Score qualité par source
  - Axe Y : `[Score Qualite Global]`
  - Axe X : `synthese_qualite_powerbi[source]`
  - Couleurs selon score : gradient rouge→vert

---

### Page 2 : Anomalies détaillées

**Objectif** : Explorer les anomalies individuelles

#### Visuels

**Ligne 1 : Filtres (Slicers)**
- Type d'anomalie (dropdown) → `rapport_anomalies[type_anomalie]`
- Gravité (buttons) → `rapport_anomalies[gravite]`
- Source (dropdown) → `rapport_anomalies[source]`

**Ligne 2 : KPIs filtrés**
- Cartes simples × 3 :
  - Anomalies sélectionnées = `[Nombre Anomalies]`
  - Critiques = `[Anom Critiques]`
  - Majeures = `[Anom Majeures]`

**Ligne 3 : Graphiques**
- **Bar Chart horizontal** : Top 10 anomalies par type
  - Axe Y : `rapport_anomalies[type_anomalie]`
  - Axe X : COUNT(id_anomalie)
  - Couleur : Gradient par gravité

- **Stacked Bar** : Anomalies par type et gravité
  - Axe X : `rapport_anomalies[type_anomalie]`
  - Y empilé : `rapport_anomalies[gravite]`

**Ligne 4 : Table détaillée**
- Tableau des anomalies (colonnes affichées) :
  - ✅ id_anomalie
  - ✅ source
  - ✅ type_anomalie
  - ✅ gravite
  - ✅ description
  - ✅ correction_recommandee
  - ✅ date_detection
- Tri par date (décroissant)
- Pagination : 50 lignes/page

---

### Page 3 : Données financières

**Objectif** : Vue métier des données nettoyées

#### Visuels

**Ligne 1 : KPIs financiers**
- Cartes × 4 :
  - 💶 Total CA = `[Total CA]` (format devise)
  - 💶 Total OPEX = `[Total OPEX]`
  - 💶 Total CAPEX = `[Total CAPEX]`
  - 📈 Marge EBITDA = `[Marge EBITDA]` (format %)

**Ligne 2 : Ventilations**
- **Pie Chart** : CA par entité
  - Légende : `donnees_finance_clean[code_entite]`
  - Valeurs : SUM(ca_eur)

- **Pie Chart** : CA par business line
  - Légende : `donnees_finance_clean[code_business_line]`
  - Valeurs : SUM(ca_eur)

**Ligne 3 : Tendances**
- **Line Chart** : CA et EBITDA par période
  - Axe X : `donnees_finance_clean[periode]` (date)
  - Axe Y : `[Total CA]` et `[Total EBITDA]` (dual axis)
  - Couleurs : CA=bleu, EBITDA=orange

**Ligne 4 : Détail**
- Table filtrée par période/entité/projet
  - Colonnes : periode, code_projet, ca_eur, opex_eur, ebitda_eur
  - Tri : période décroissante

---

### Page 4 : Références de vérification

**Objectif** : Audit et traçabilité des contrôles

#### Visuels

**Bloc 1 : Synthèse qualité par source**
- Table : `synthese_qualite_powerbi`
  - Colonnes :
    - source
    - total_lignes
    - total_anomalies
    - anomalies_critiques
    - score_qualite (format %)
  - Couleur fond : Gradient score (rouge < 70%, jaune < 85%, vert ≥ 85%)

**Bloc 2 : Statistiques anomalies**
- Table : `statistiques_anomalies`
  - Colonnes :
    - type_anomalie
    - nombre_anomalies
    - anomalies_critiques
    - anomalies_majeures
    - anomalies_mineures
  - Tri : nombre_anomalies décroissant

**Bloc 3 : Métadonnées**
- Texte statique :
  - "Données exportées le : [DATE]"
  - "Version données : [VERSION]"
  - "Contrôle qualité : VALIDE ✅"

---

## Étape 6 : Mise en forme et UX

### Thème visuel

1. **Couleurs standardisées** :
   - 🔴 Critique = #d62728 (rouge)
   - 🟠 Majeure = #ff7f0e (orange)
   - 🟢 Mineure = #2ca02c (vert)
   - Score = Gradient (rouge → vert)

2. **Polices** :
   - Titre : Segoe UI / Bold / 20pt
   - Sous-titre : Segoe UI / 14pt
   - Texte : Segoe UI / 11pt

3. **En-têtes et pieds de page** :
   - Logo ou nom du projet
   - Date dernier refresh
   - Filtres appliqués

### Navigation

- Boutons de navigation entre pages
- Breadcrumbs (chemin parcouru)
- Drill-through : Anomalies détaillées → Données source

---

## Étape 7 : Paramètres et alertes

### Paramètres (Parameters)

Créer des paramètres pour :

1. **Date de seuil**
   - Nom : `Seuil Score`
   - Valeurs : 70, 80, 85, 90, 95
   - Défaut : 85

2. **Source sélectionnée**
   - Nom : `Source Affichage`
   - Valeurs : données_finance_raw, données_projets_raw, données_kpi_raw
   - Défaut : données_finance_raw

### Alertes (Conditional Formatting)

- **Cartes KPIs** :
  - Score < 70% → Fond rouge
  - Score 70-84% → Fond orange
  - Score ≥ 85% → Fond vert

- **Table anomalies** :
  - Gravité "Critique" → Fond rouge clair
  - Gravité "Majeure" → Fond orange clair

---

## Étape 8 : Interactivité

### Slicers (Filtres)

Ajouter sur chaque page :

1. **Filtre période** (si données temporelles)
2. **Filtre entité**
3. **Filtre type anomalie** (pages anomalies)
4. **Filtre gravité**

### Synchronisation

- Activer **Sync slicers** entre pages
- Les sélections se propagent automatiquement

### Drill-through

Créer interactions drill-through :
- Cliquer sur type anomalie → Page détail anomalies
- Cliquer sur entité → Page données financières filtrées

---

## Étape 9 : Tableau de bord final

### Structure recommandée

```
📊 Dashboard Principal
├── 📄 Page 1 : Vue Qualité Globale
├── 📄 Page 2 : Anomalies Détaillées
├── 📄 Page 3 : Données Financières
├── 📄 Page 4 : Références & Audit
└── 📄 Page 5 : Mode Lecture (Exec Summary)
```

### Mode Lecture (Executive Summary)

Une page simplifiée pour C-suite :
- 4 KPIs principaux en gros
- 1 graphique tendance score qualité
- 1 indicateur "ALERTE" si score < 85%
- Message court d'impact

---

## Étape 10 : Publication

### Avant publication

- ✅ Vérifier tous les calculs DAX
- ✅ Tester tous les filtres
- ✅ Valider formats et mise en forme
- ✅ Relire textes et traductions
- ✅ Tester performances (pas de lag)

### Publication sur Power BI Service

1. **Fichier** → **Publier**
2. Sélectionner **Workspace**
3. Attendre la publication
4. Configurer **Paramètres de refresh** :
   - Quotidien si données mises à jour chaque jour
   - Hebdomadaire sinon

### Partage

- Assigner les lecteurs appropriés
- Activer les alertes (si nouvelles anomalies critiques)
- Activer commentaires/annotations

---

## Mesures DAX avancées (Optionnel)

### Anomalies critiques par période

```dax
Anom Critiques Period = 
    CALCULATE(
        COUNTA('rapport_anomalies'[id_anomalie]),
        'rapport_anomalies'[gravite] = "Critique",
        'rapport_anomalies'[date_detection] = MAX('donnees_finance_clean'[periode])
    )
```

### Variation score vs précédent

```dax
Var Score = 
    [Score Qualite Global] - 
    CALCULATE(
        [Score Qualite Global],
        DATEADD('donnees_finance_clean'[periode], -1, MONTH)
    )
```

### Taux anomalies par ligne

```dax
Taux Anom Per = 
    DIVIDE(
        [Nombre Anomalies],
        [Total Lignes],
        0
    ) * 100
```

---

## Troubleshooting

| Problème | Cause | Solution |
|----------|-------|----------|
| Données pas chargées | Mauvais encodage | Vérifier UTF-8 dans CSV |
| Séparateur invalide | Point-virgule non reconnu | Sélectionner `;` lors import |
| Graphiques vides | Mesure mal configurée | Vérifier DAX dans formule |
| Lenteur affichage | Trop de données | Ajouter filtre date ou chunker |
| Dates mal interprétées | Format non standard | Convertir en YYYY-MM-DD |
| Liens références absents | Relations mal créées | Recréer dans vue Modèle |

---

## Prochaines étapes

1. ✅ Publier tableau de bord
2. ✅ Configurer alertes automatiques
3. ✅ Planifier refresh quotidien
4. ✅ Former utilisateurs métier
5. 🔄 Ajouter modèles ML (prédiction anomalies)
6. 🔄 Intégrer données temps réel (streaming)
