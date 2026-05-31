# Règles de contrôle qualité des données

## Objectif

Ce document définit l'ensemble des règles de contrôle qualité appliquées automatiquement par le module `controle_qualite.py`. Chaque règle est associée à un type d'anomalie, un niveau de gravité et une action de correction recommandée.

---

## Règles sur les référentiels

### RQ-001 : Validité de l'entité

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-001 |
| **Type anomalie** | ENTITE_INCONNUE |
| **Gravité** | 🔴 Critique |
| **Description** | Le code_entite doit exister dans referentiel_entites.csv |
| **Formule** | code_entite ∈ referentiel_entites.code_entite |
| **Exemple correct** | ENT_FR_001 (existe) |
| **Exemple incorrect** | ENT_XX_999 (n'existe pas) |
| **Correction** | Vérifier le code entité dans le référentiel |
| **Impact** | Les lignes n'est impossible à associer au bon domaine |

---

### RQ-002 : Validité du projet

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-002 |
| **Type anomalie** | PROJET_INCONNU |
| **Gravité** | 🔴 Critique |
| **Description** | Le code_projet doit exister dans referentiel_projets.csv |
| **Formule** | code_projet ∈ referentiel_projets.code_projet |
| **Exemple correct** | PRJ_001 (existe) |
| **Exemple incorrect** | PRJ_999 (n'existe pas) |
| **Correction** | Vérifier le code projet dans le référentiel |
| **Impact** | Impossible de linker les données aux projets métier |

---

### RQ-003 : Validité de la business line

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-003 |
| **Type anomalie** | BUSINESS_LINE_INCONNUE |
| **Gravité** | 🔴 Critique |
| **Description** | Le code_business_line doit exister dans referentiel_business_lines.csv |
| **Formule** | code_business_line ∈ referentiel_business_lines.code_business_line |
| **Exemple correct** | BL_DEV (existe) |
| **Exemple incorrect** | BL_UNKNOWN (n'existe pas) |
| **Correction** | Vérifier le code business line dans le référentiel |
| **Impact** | Impossible de classifier les données par domaine métier |

---

## Règles sur les données financières

### RQ-004 : Montants non négatifs

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-004 |
| **Type anomalie** | MONTANT_NEGATIF |
| **Gravité** | 🟠 Majeure |
| **Description** | CA, OPEX et CAPEX doivent être ≥ 0 |
| **Formule** | ca_eur ≥ 0 AND opex_eur ≥ 0 AND capex_eur ≥ 0 |
| **Exemple correct** | CA=1000, OPEX=500, CAPEX=200 |
| **Exemple incorrect** | CA=-1000 ou OPEX=-500 |
| **Correction** | Vérifier l'origine de la donnée, appliquer valeur absolue si erreur de saisie |
| **Impact** | Fausse les calculs d'EBITDA et marges |

---

### RQ-005 : Cohérence EBITDA

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-005 |
| **Type anomalie** | EBITDA_INCOHERENT |
| **Gravité** | 🟠 Majeure |
| **Description** | EBITDA doit égaler CA - OPEX (tolérance 1 EUR) |
| **Formule** | \|ebitda_eur - (ca_eur - opex_eur)\| ≤ 1 |
| **Exemple correct** | CA=1000, OPEX=400, EBITDA=600 |
| **Exemple incorrect** | CA=1000, OPEX=400, EBITDA=800 |
| **Correction** | Recalculer EBITDA = CA - OPEX |
| **Impact** | Biais tous les indicateurs de rentabilité |

---

## Règles sur les périodes

### RQ-006 : Format et présence de la période

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-006 |
| **Type anomalie** | PERIODE_INVALIDE |
| **Gravité** | 🟠 Majeure |
| **Description** | Période obligatoire, format YYYY-MM valide |
| **Formule** | periode IS NOT NULL AND periode MATCHES 'YYYY-MM' |
| **Exemple correct** | 2023-01, 2024-12 |
| **Exemple incorrect** | 2023/01, 01-2023, vide |
| **Correction** | Remplir la période et normaliser au format YYYY-MM |
| **Impact** | Impossible de sérier les données dans le temps |

---

## Règles sur les valeurs manquantes

### RQ-007 : Champs obligatoires

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-007 |
| **Type anomalie** | VALEUR_MANQUANTE |
| **Gravité** | 🟠 Majeure (ou 🔴 Critique si clé) |
| **Description** | Certains champs ne peuvent pas être vides |
| **Formule** | periode IS NOT NULL AND code_entite IS NOT NULL AND code_projet IS NOT NULL |
| **Exemple correct** | Tous les champs remplis |
| **Exemple incorrect** | code_projet = "" ou NULL |
| **Correction** | Remplir le champ avec la valeur correcte |
| **Impact** | Perte de traçabilité et d'intégrité des données |

---

## Règles sur les doublons

### RQ-008 : Absence de doublons

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-008 |
| **Type anomalie** | DOUBLON |
| **Gravité** | 🟢 Mineure |
| **Description** | Pas d'enregistrements en doublon sur (periode, entité, projet, BL) |
| **Formule** | COUNT(DISTINCT(periode, code_entite, code_projet, code_business_line)) = COUNT(*) |
| **Exemple correct** | Chaque combinaison unique 1 fois |
| **Exemple incorrect** | Même ligne 2 fois |
| **Correction** | Supprimer l'un des doublons (keeper = 1er) |
| **Impact** | Double-comptage des montants, statistiques biaisées |

---

## Règles sur les statuts

### RQ-009 : Validité des statuts

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-009 |
| **Type anomalie** | STATUT_INVALIDE |
| **Gravité** | 🟠 Majeure |
| **Description** | Statut projet doit être parmi [Actif, En pause, Planifié, Clos] |
| **Formule** | statut_projet IN ('Actif', 'En pause', 'Planifié', 'Clos') |
| **Exemple correct** | Actif, En pause, Planifié, Clos |
| **Exemple incorrect** | Inexistant, En cours, Archive |
| **Correction** | Normaliser vers statut autorisé |
| **Impact** | Mauvaise classification des projets actifs |

---

## Règles sur les dates

### RQ-010 : Cohérence des dates

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-010 |
| **Type anomalie** | DATE_INCOHERENTE |
| **Gravité** | 🟠 Majeure |
| **Description** | Date fin prévue ≥ date début |
| **Formule** | date_fin_prevue ≥ date_debut |
| **Exemple correct** | Début=2023-01-01, Fin=2024-01-01 |
| **Exemple incorrect** | Début=2024-01-01, Fin=2023-01-01 |
| **Correction** | Inverser ou corriger les dates |
| **Impact** | Durées négatives, timeline invalide |

---

## Règles sur les KPI

### RQ-011 : Documentation des KPI

| Paramètre | Valeur |
|-----------|--------|
| **Code règle** | RQ-011 |
| **Type anomalie** | KPI_INCOMPLET |
| **Gravité** | 🟠 Majeure (🔴 Critique si KPI.criticite=Critique) |
| **Description** | KPI doit avoir formule, unité, et si criticite=Critique alors description |
| **Formule** | formule IS NOT NULL AND unite IS NOT NULL AND (criticite != 'Critique' OR description IS NOT NULL) |
| **Exemple correct** | KPI_CA avec formule=Somme, unite=EUR, criticite=Critique, description=... |
| **Exemple incorrect** | KPI sans formule, ou KPI critique sans description |
| **Correction** | Documenter le KPI complètement |
| **Impact** | Impossibilité de reproduire les calculs, manque de traçabilité |

---

## Pondération des anomalies

### Calcul du score qualité

```
Points perdus par gravité :
- 🔴 Critique = 5 points
- 🟠 Majeure = 3 points
- 🟢 Mineure = 1 point

Total points perdus = ∑(anomalies.gravité.points)

Score qualité = MAX(0, 100 - (points_perdus / total_lignes) * 100)
```

### Exemple de calcul

```
Données de test:
- Total lignes: 100
- Anomalies: 1 Critique (5 pts) + 2 Majeures (6 pts) + 3 Mineures (3 pts) = 14 pts

Points perdus: 5 + (2 × 3) + (3 × 1) = 14 points

Score: 100 - (14 / 100) × 100 = 100 - 14 = 86%
```

---

## Processus de correction

### Priorité de traitement

1. **🔴 Critiques** → À corriger avant tout (bloquent exploitation)
2. **🟠 Majeures** → À corriger rapidement (faussent analyses)
3. **🟢 Mineures** → À corriger en continu (optimisation)

### Actions recommandées par type

| Type anomalie | Cause probable | Correction |
|---------------|----------------|-----------|
| ENTITE_INCONNUE | Typo/erreur saisie | Consulter métier |
| PROJET_INCONNU | Donnée anciennes/nouvelles | Mettre à jour référentiel |
| BUSINESS_LINE_INCONNUE | Changement organisationnel | Valider avec métier |
| MONTANT_NEGATIF | Erreur calcul/saisie | Recalculer/corriger |
| EBITDA_INCOHERENT | Formule incorrecte | Auditer formule source |
| DOUBLON | ETL mal configuré | Dédupliquer |
| PERIODE_INVALIDE | Format incorrect | Normaliser |
| DATE_INCOHERENTE | Erreur saisie | Corriger dates |

---

## Monitoring continu

### Métriques à surveiller

- **Score qualité global** : Doit rester > 90%
- **Anomalies critiques** : Doit rester < 1% des lignes
- **Tendance anomalies** : À tracker dans Power BI
- **Latence détection** : À automatiser quotidiennement

### Gouvernance

- Anomalies critiques = assignées à propriétaire métier
- Majeures = revue hebdomadaire
- Mineures = revue mensuelle
- Tableau de bord Power BI alimenté quotidiennement
