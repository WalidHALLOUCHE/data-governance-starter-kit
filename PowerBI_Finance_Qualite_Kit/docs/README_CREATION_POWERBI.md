# Dashboard Power BI — Finance & Qualité des données

## Ce qui a été préparé

Ce kit contient des fichiers CSV prêts pour Power BI, les mesures DAX, un thème JSON et un guide de construction du rapport.

## Fichiers Power BI prêts à importer

Dossier `data/` :

| Fichier | Rôle |
|---|---|
| `donnees_finance_powerbi.csv` | Table principale des données financières nettoyées |
| `rapport_anomalies_powerbi.csv` | Détail ligne par ligne des anomalies |
| `synthese_qualite_powerbi_ready.csv` | Qualité par source |
| `score_qualite_global_powerbi.csv` | Score global et taux de validité |
| `statistiques_anomalies_powerbi.csv` | Agrégats par type d’anomalie |

## Volumétrie réelle détectée

| Indicateur | Valeur |
|---|---:|
| Lignes financières propres | 236 |
| Anomalies détectées | 122 |
| Anomalies critiques | 21 |
| Anomalies majeures | 64 |
| Anomalies mineures | 37 |
| CA total | 587,795,124.94 € |
| EBITDA total | 398,881,290.83 € |
| Marge EBITDA | 67.86% |
| Période min | 2023-01 |
| Période max | 2024-11 |
| Taux de validité global | 77.38% |
| Score qualité global source | 0.00% |

## Modèle recommandé

Créer les relations suivantes :

1. `Calendrier[Date]` → `donnees_finance_powerbi[date_periode]`
2. `Calendrier[Date]` → `rapport_anomalies_powerbi[date_periode]`
3. `synthese_qualite_powerbi_ready[source]` → `rapport_anomalies_powerbi[source]`
4. `statistiques_anomalies_powerbi[type_anomalie]` → `rapport_anomalies_powerbi[type_anomalie]`

## Correction importante du modèle

Ne pas créer la relation `donnees_finance_clean[code_entite]` → `synthese_qualite_powerbi[source]`.

Pourquoi : `code_entite` contient des valeurs de type `ENT_IT_001`, alors que `source` contient des valeurs de type `donnees_finance_raw`. La relation produirait un modèle incohérent et des visuels faux.

## Pages à construire

### Page 1 — Executive Summary

KPIs :
- Total CA
- Total EBITDA
- Marge EBITDA
- Total anomalies
- Anomalies critiques
- Taux validité
- Score qualité global
- Statut qualité

Visuels :
- Courbe CA / EBITDA par mois
- Donut anomalies par gravité
- Bar chart top anomalies par type
- Table des sources qualité

### Page 2 — Qualité & Gouvernance

KPIs :
- Lignes contrôlées
- Lignes valides
- Lignes invalides
- Taux validité
- Score qualité global

Visuels :
- Jauge score qualité
- Bar chart anomalies par type
- Matrix source × gravité
- Table synthèse qualité par source

### Page 3 — Anomalies détaillées

Slicers :
- Source
- Gravité
- Type anomalie
- Période
- Entité

Visuels :
- Top 10 types d’anomalies
- Anomalies par gravité
- Table détaillée : id, source, ligne, période, entité, type, gravité, description, correction recommandée

### Page 4 — Performance financière

KPIs :
- CA total
- OPEX total
- CAPEX total
- EBITDA total
- Marge EBITDA
- Résultat après CAPEX

Visuels :
- CA et EBITDA par période
- CA par entité
- CA par business line
- Table financière par projet

### Page 5 — Audit technique

Visuels :
- Table `score_qualite_global_powerbi`
- Table `statistiques_anomalies_powerbi`
- Table `synthese_qualite_powerbi_ready`
- Texte d’audit : date de détection des anomalies, nombre de lignes contrôlées, statut qualité

## Formatage conseillé

- CA, OPEX, CAPEX, EBITDA : format devise `€`
- Marges et taux : format pourcentage
- Score qualité : format pourcentage
- Gravité :
  - Critique : rouge
  - Majeure : orange
  - Mineure : vert