# Dictionnaire des données Power BI

## donnees_finance_powerbi

| Colonne | Type Power BI | Description |
|---|---|---|
| periode | Texte | Période d’origine au format YYYY-MM |
| date_periode | Date | Date normalisée au premier jour du mois |
| code_entite | Texte | Entité financière |
| code_projet | Texte | Projet |
| code_business_line | Texte | Business line |
| ca_eur | Décimal | Chiffre d’affaires en euros |
| opex_eur | Décimal | Charges opérationnelles |
| capex_eur | Décimal | Investissements |
| ebitda_eur | Décimal | EBITDA |
| commentaire_source | Texte | Commentaire de nettoyage/source |
| cle_finance | Texte | Clé technique période/entité/projet/business line |

## rapport_anomalies_powerbi

| Colonne | Type Power BI | Description |
|---|---|---|
| id_anomalie | Texte | Identifiant unique d’anomalie |
| source | Texte | Source contrôlée |
| ligne | Entier | Ligne concernée dans la source |
| periode | Texte | Période concernée |
| date_periode | Date | Période convertie en date |
| type_anomalie | Texte | Typologie de l’anomalie |
| gravite | Texte | Critique, Majeure ou Mineure |
| gravite_ordre | Entier | Ordre de tri : Critique=1, Majeure=2, Mineure=3 |
| description | Texte | Description de l’anomalie |
| correction_recommandee | Texte | Correction proposée |
| date_detection | Date/Heure | Date de détection |
| date_detection_date | Date | Date de détection sans heure |
| cle_finance | Texte | Clé technique alignée finance quand possible |

## score_qualite_global_powerbi

Table mono-ligne utilisée pour les KPIs globaux.

## synthese_qualite_powerbi_ready

Table de synthèse par source avec `score_qualite_ratio` prêt à formater en pourcentage.

## statistiques_anomalies_powerbi

Table agrégée par type d’anomalie.