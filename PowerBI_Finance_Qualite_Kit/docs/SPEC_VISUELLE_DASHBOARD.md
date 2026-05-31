# Spécification visuelle du rapport Power BI

## Taille
Format recommandé : 16:9.

## Navigation
Créer une barre de navigation horizontale en haut :
- Executive Summary
- Qualité
- Anomalies
- Finance
- Audit

## Page 1 — Executive Summary

Disposition :
- Bandeau titre : `Dashboard Finance & Qualité des Données`
- Ligne KPI : 6 cartes
- Zone centrale gauche : graphique ligne CA / EBITDA
- Zone centrale droite : donut anomalies par gravité
- Bas gauche : top anomalies par type
- Bas droite : table qualité par source

## Page 2 — Qualité & Gouvernance

Disposition :
- 4 KPIs en haut : lignes contrôlées, lignes valides, lignes invalides, taux validité
- Jauge : Score qualité global
- Bar chart horizontal : anomalies par type
- Matrix : type anomalie × gravité
- Table source : source, total_lignes, total_anomalies, score_qualite_ratio

## Page 3 — Anomalies détaillées

Disposition :
- Slicers en haut : source, gravité, type_anomalie, période
- KPIs filtrés : total anomalies, critiques, majeures, mineures
- Graphique : top 10 anomalies
- Table détaillée pleine largeur

Tri recommandé de la table :
1. `gravite_ordre` croissant
2. `date_detection` décroissant

## Page 4 — Performance financière

Disposition :
- KPIs : CA, OPEX, CAPEX, EBITDA, Marge EBITDA
- Courbe : CA / EBITDA par `Calendrier[Mois Année]`
- Donut : CA par business line
- Bar chart : CA par entité
- Table : période, entité, projet, business line, CA, OPEX, CAPEX, EBITDA

## Page 5 — Audit technique

Disposition :
- Bloc 1 : données contrôlées
- Bloc 2 : statistiques anomalies
- Bloc 3 : source quality
- Bloc 4 : commentaire d’audit

Message d’audit proposé :
`Contrôle qualité réalisé sur les données financières de test. Le taux de validité est de 77,38 %, avec 122 anomalies détectées dont 21 critiques. Le rapport met en évidence les contrôles à prioriser avant publication métier.`