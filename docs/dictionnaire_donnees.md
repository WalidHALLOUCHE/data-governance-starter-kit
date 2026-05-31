# Dictionnaire des données

## donnees_finance_raw.csv

| Colonne | Type | Format | Description | Exemple | Domaine |
|---------|------|--------|-------------|---------|---------|
| periode | Texte | YYYY-MM | Période de la donnée (année-mois) | 2023-01 | Date |
| code_entite | Texte | ENT_XX_### | Code unique de l'entité | ENT_FR_001 | Référence |
| code_projet | Texte | PRJ_### | Code unique du projet | PRJ_001 | Référence |
| code_business_line | Texte | BL_XXX | Code de la business line | BL_DEV | Référence |
| ca_eur | Décimal | Montant (EUR) | Chiffre d'affaires en euros | 1500000.50 | Finance |
| opex_eur | Décimal | Montant (EUR) | Charges opérationnelles en euros | 750000.00 | Finance |
| capex_eur | Décimal | Montant (EUR) | Investissements CAPEX en euros | 200000.00 | Finance |
| ebitda_eur | Décimal | Montant (EUR) | EBITDA = CA - OPEX en euros | 750000.50 | Finance |
| commentaire_source | Texte | Libre | Commentaire/source de la donnée | Source données test | Metadata |

**Règles** :
- periode est obligatoire et au format YYYY-MM
- code_entite, code_projet, code_business_line doivent exister dans les référentiels
- ca_eur, opex_eur, capex_eur ≥ 0
- ebitda_eur = ca_eur - opex_eur
- Pas de doublon par (periode, code_entite, code_projet, code_business_line)

---

## donnees_projets_raw.csv

| Colonne | Type | Format | Description | Exemple |
|---------|------|--------|-------------|---------|
| code_projet | Texte | PRJ_### | Identifiant unique du projet | PRJ_001 |
| nom_projet | Texte | Libre | Libellé complet du projet | Projet solaire Nord |
| code_entite | Texte | ENT_XX_### | Code entité propriétaire du projet | ENT_FR_001 |
| code_business_line | Texte | BL_XXX | Code de la business line | BL_DEV |
| statut_projet | Texte | Contrôlé | Statut du projet (Actif, En pause, Planifié, Clos) | Actif |
| date_debut | Date | YYYY-MM-DD | Date de début du projet | 2023-01-15 |
| date_fin_prevue | Date | YYYY-MM-DD | Date de fin prévue | 2024-01-15 |

**Règles** :
- code_projet est obligatoire et unique
- code_entite et code_business_line doivent exister dans les référentiels
- statut_projet ∈ [Actif, En pause, Planifié, Clos]
- date_fin_prevue ≥ date_debut

---

## donnees_kpi_raw.csv

| Colonne | Type | Format | Description | Exemple |
|---------|------|--------|-------------|---------|
| code_kpi | Texte | KPI_### | Identifiant unique du KPI | KPI_001 |
| nom_kpi | Texte | Libre | Libellé du KPI | Chiffre d'affaires |
| domaine | Texte | Contrôlé | Domaine (Finance, Opérationnel, RH, IT) | Finance |
| formule | Texte | Libre | Formule de calcul du KPI | Somme du CA |
| unite | Texte | Contrôlée | Unité (EUR, %, Nombre, Jours) | EUR |
| criticite | Texte | Contrôlée | Niveau (Critique, Majeure, Mineure) | Critique |
| description | Texte | Libre | Description détaillée | Description du KPI |

**Règles** :
- code_kpi est obligatoire et unique
- formule et unite sont obligatoires
- Si criticite = Critique, description est obligatoire
- Pas de doublon sur code_kpi

---

## referentiel_entites.csv

| Colonne | Type | Format | Description | Exemple |
|---------|------|--------|-------------|---------|
| code_entite | Texte | ENT_XX_### | Code unique de l'entité | ENT_FR_001 |
| entite | Texte | Libre | Libellé complet | Entité France |
| pays | Texte | Libre | Pays d'implantation | France |
| region | Texte | Libre | Région géographique | Europe |
| statut_entite | Texte | Actif/Inactif | Statut de l'entité | Actif |

---

## referentiel_business_lines.csv

| Colonne | Type | Format | Description | Exemple |
|---------|------|--------|-------------|---------|
| code_business_line | Texte | BL_XXX | Code de la business line | BL_DEV |
| business_line | Texte | Libre | Libellé court | Développement projets |
| description | Texte | Libre | Description détaillée | Pipeline et développement |

---

## referentiel_projets.csv

| Colonne | Type | Format | Description | Exemple |
|---------|------|--------|-------------|---------|
| code_projet | Texte | PRJ_### | Code unique du projet | PRJ_001 |
| nom_projet | Texte | Libre | Libellé du projet | Projet solaire Nord |
| code_entite | Texte | ENT_XX_### | Code entité | ENT_FR_001 |
| code_business_line | Texte | BL_XXX | Code business line | BL_DEV |
| statut_projet | Texte | Contrôlé | Statut (Actif, Clos, etc.) | Actif |
| date_debut | Date | YYYY-MM-DD | Démarrage | 2023-01-01 |
| date_fin_prevue | Date | YYYY-MM-DD | Fin prévue | 2024-01-01 |

---

## referentiel_kpi.csv

| Colonne | Type | Format | Description | Exemple |
|---------|------|--------|-------------|---------|
| code_kpi | Texte | KPI_XXX | Code du KPI | KPI_CA |
| nom_kpi | Texte | Libre | Libellé du KPI | Chiffre d'affaires |
| domaine | Texte | Libre | Domaine métier | Finance |
| formule | Texte | Libre | Formule de calcul | Somme du CA |
| unite | Texte | EUR, %, etc. | Unité de mesure | EUR |
| criticite | Texte | Haute, Moyenne | Niveau de criticité | Haute |

---

## rapport_anomalies.csv

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| id_anomalie | Texte | Identifiant unique | ANOM_000001 |
| source | Texte | Fichier source | donnees_finance_raw |
| ligne | Entier | Numéro de ligne (base 1 + header) | 42 |
| periode | Texte | Période concernée | 2023-01 |
| code_entite | Texte | Entité concernée | ENT_FR_001 |
| code_projet | Texte | Projet concerné | PRJ_001 |
| code_business_line | Texte | Business line concernée | BL_DEV |
| type_anomalie | Texte | Type détecté | ENTITE_INCONNUE |
| gravite | Texte | Critique/Majeure/Mineure | Critique |
| description | Texte | Description de l'anomalie | Entité inconnue: ENT_XX_999 |
| valeur_detectee | Texte | Valeur problématique | ENT_XX_999 |
| correction_recommandee | Texte | Action recommandée | Vérifier contre référentiel |
| date_detection | DateTime | Quand l'anomalie a été détectée | 2024-05-30 10:30:15 |

---

## score_qualite_donnees.csv

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| total_lignes_controle | Entier | Nombre total de lignes contrôlées | 305 |
| lignes_valides | Entier | Nombre de lignes sans anomalie | 212 |
| lignes_invalides | Entier | Nombre de lignes avec anomalies | 93 |
| taux_validite | Décimal | Pourcentage lignes valides | 69.51 |
| total_anomalies | Entier | Total anomalies détectées | 127 |
| anomalies_critiques | Entier | Anomalies critiques | 28 |
| anomalies_majeures | Entier | Anomalies majeures | 65 |
| anomalies_mineures | Entier | Anomalies mineures | 34 |
| taux_anomalies_pondere | Décimal | Score anomalies pondérées (%) | 45.25 |
| score_qualite_global | Décimal | Score global (0-100%) | 54.75 |

---

## synthese_qualite_powerbi.csv

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| source | Texte | Fichier source | donnees_finance_raw |
| total_lignes | Entier | Lignes contrôlées | 305 |
| total_anomalies | Entier | Anomalies détectées | 86 |
| anomalies_critiques | Entier | Critiques | 20 |
| anomalies_majeures | Entier | Majeures | 48 |
| anomalies_mineures | Entier | Mineures | 18 |
| score_qualite | Décimal | Score (0-100%) | 62.48 |

---

## statistiques_anomalies.csv

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| type_anomalie | Texte | Type d'anomalie | ENTITE_INCONNUE |
| nombre_anomalies | Entier | Total du type | 12 |
| anomalies_critiques | Entier | Critiques | 8 |
| anomalies_majeures | Entier | Majeures | 3 |
| anomalies_mineures | Entier | Mineures | 1 |

---

## Conventions et standards

### Encodage
- **UTF-8** pour tous les fichiers CSV
- **Séparateur** : point-virgule (`;`)
- **Décimales** : point (`.`)
- **Format dates** : YYYY-MM-DD ou YYYY-MM

### Codes métier
- **Entités** : ENT_XX_### (2 lettres pays + 3 chiffres)
- **Projets** : PRJ_### (3 chiffres)
- **Business lines** : BL_XXX (2-3 lettres)
- **KPIs** : KPI_XXX (3 lettres)

### Qualité minimale
- Pas de NULL mélangés avec vides
- Pas de doublons
- Pas de montants négatifs
- Dates cohérentes
- Codes valides et présents dans référentiels

### Traçabilité
- Chaque anomalie reçoit un ID unique
- Chaque anomalie est datée
- Chaque anomalie est sourcée
- Chaque anomalie reçoit une correction recommandée
