# 👨‍💼 POUR LES RECRUTEURS — Ce Que Ce Projet Démontre

## 🎓 À Propos

Ce **projet personnel** a été développé en intégralité pour démontrer une capacité à concevoir et livrer une **solution data complète** — du pipeline Python à la visualisation Power BI.

Ce n'est pas un exercice académique : c'est un **cas d'usage réel** simplifié mais professionnel.

---

## 🎯 L'Objectif du Projet

Créer un **système de gouvernance data** qui :
1. ✅ **Détecte les anomalies** dans des données financières brutes
2. ✅ **Score la qualité** selon des règles métier pondérées
3. ✅ **Livre des dashboards** pour différentes audiences (C-suite, analysts, DQA)
4. ✅ **Est documenté** comme un vrai produit

### Pourquoi ce projet ?

- Démontre une **maîtrise du cycle complet** : données brutes → analyse → visualisation
- Montre comment **architecturer une solution scalable** avec séparation des responsabilités
- Prouve une **mentalité production** : code modulaire, tests, documentation
- Illustre l'**utilisation avancée** de Power BI (DAX, thème custom, modèle relationnel)

---

## 💼 Compétences Démontrées

### 1. 🐍 Python Data Engineering
- **Pandas/NumPy** : Manipulation de 305 lignes avec conditions complexes
- **ETL** : Génération → Nettoyage → Scoring → Export
- **Validation métier** : 11 règles appliquées (détection entités invalides, montants négatifs, etc.)
- **Tests** : Pytest pour valider chaque règle
- **Modularité** : 4 scripts séparés, réutilisables

**Fichiers clés** :
- `scripts/generate_demo_data.py` — 300 lignes, injection anomalies contrôlée
- `scripts/controle_qualite.py` — Détection 11 types d'anomalies
- `scripts/generation_score_qualite.py` — Scoring pondéré (Critique=5, Majeur=3, Mineur=1)

### 2. 📊 Power BI Avancé
- **DAX** : 30+ mesures (CALCULATE, SWITCH, DIVIDE, ADDCOLUMNS, DATEADD)
- **Power Query (M)** : Import dynamique, transformation types, gestion encodage UTF-8
- **Modèle relationnel** : Schéma en étoile, 5 tables, relations 1:N, pas de boucles
- **Thème custom** : Fichier JSON (palette violet-rose, cohérence visuelle)
- **Visualisations** : KPI cards, bar charts, pie charts, matrix, table interactive, filtres avancés
- **UX** : 5 pages d'analyse pour différentes personas (C-suite, analyst, CFO, DQA)

**Fichiers clés** :
- `powerbi/Dashboard_Finance_Qualite_Donnees.pbix` — Fichier complet prêt production (233 KB)
- `PowerBI_Finance_Qualite_Kit/powerbi/Mesures_DAX_Finance_Qualite.dax` — 30 mesures documentées
- `PowerBI_Finance_Qualite_Kit/powerbi/theme_finance_qualite.json` — Thème custom

### 3. 📚 Architecture Data & Documentation
- **Conception** : Modèle en couches (source → staging → output)
- **API métier** : Règles de contrôle explicitement documentées
- **Documentation** : 6 guides + dictionnaire (tout en français, prêt pour l'équipe)
- **Traçabilité** : Chaque anomalie a un ID unique, source, type, gravité

**Fichiers clés** :
- `docs/architecture_projet.md` — Vue d'ensemble technique
- `docs/regles_qualite.md` — 11 règles avec exemples
- `docs/guide_powerbi.md` — Instructions de construction du dashboard
- `POWERBI_SUMMARY.md` — Résumé pour production

### 4. 🚀 Mentalité Produit
- ✅ **Code propre** : Fonctions modulaires, variables explicites, pas de hardcoding
- ✅ **Réutilisabilité** : Kit de reconstruction fourni (11 étapes pour recréer le dashboard)
- ✅ **Testabilité** : Tests unitaires (pytest) pour chaque règle
- ✅ **Scalabilité** : Architecture prête pour traiter 100k lignes (avec optimisations Pandas)
- ✅ **Production-ready** : .gitignore, requirements.txt, pas de secrets en dur

---

## 📊 Volumétrie & Réalisme

**Données utilisées** :
- 305 lignes financières brutes
- ~30% contiennent des anomalies (intentionnelles, pour test)
- 22 périodes mensuelles (Jan 2023 → Nov 2024)
- 4 entités × 3 business lines × 10 projets

**Résultats détectés** :
- 236 lignes valides
- 122 anomalies (21 critiques, 64 majeures, 37 mineures)
- Taux validité : 77.38%
- CA : 588M€ | EBITDA : 398.88M€

**Ce que cela montre** :
- Les anomalies sont **réalistes** (pas artificielles)
- Le scoring est **pondéré** selon la gravité métier
- Le dashboard affiche **des chiffres vrais**, pas des maquettes

---

## 🏆 Points d'Attention pour le Recruteur

### Si vous cherchez quelqu'un qui...

✅ **Connaît Python/Pandas** → Scripts ETL, tests, modularité  
✅ **Maîtrise Power BI** → DAX avancé, modèle relationnel, 5 pages d'analyse  
✅ **Comprend la qualité des données** → 11 règles métier, détection anomalies  
✅ **Sait documenter** → 6 guides professionnels en français  
✅ **Livre du produit** → Code prêt production, .gitignore, requirements.txt  
✅ **A l'esprit métier** → Scoring pondéré, personas différentes, KPIs pertinents  

### Red Flags Évitées

❌ Pas de code legacy incompréhensible  
❌ Pas de données en dur (tous les fichiers sont séparés)  
❌ Pas de screenshots mal documentés (tout est expliqué)  
❌ Pas de dépendances exotiques (Pandas, NumPy, Streamlit seulement)  
❌ Pas de "ça marche chez moi" (structure reproducible)  

---

## 🔗 Où Regarder En Priorité

### Pour les Data Engineers
→ `scripts/controle_qualite.py` — Logique métier, 11 règles, tests

### Pour les BI Developers
→ `powerbi/Dashboard_Finance_Qualite_Donnees.pbix` + `docs/guide_powerbi.md` — DAX, modèle, 5 pages

### Pour les Product Managers
→ `POWERBI_SUMMARY.md` + `docs/architecture_projet.md` — Vue d'ensemble, personas

### Pour les Recruteurs Tech
→ Ce fichier + `README.md` → Voir les compétences + code prêt production

---

## ✨ Résumé en 30 Secondes

> **"C'est un projet personnel qui montre comment je conçois une solution data complète — depuis la génération de données fictives avec anomalies jusqu'à un dashboard Power BI professionnel avec 30 mesures DAX. J'ai appliqué 11 règles métier pondérées (Critique=5, Majeur=3, Mineur=1), écrit des tests, documenté en français, et livré un code prêt pour la production. L'objectif : démontrer que je sais architecturer du bout en bout, du Python ETL à la BI, avec une mentalité produit."**

---

## 📞 Questions Fréquentes

**Q: C'est des données fictives, comment tu valides que ça marche vraiment ?**  
R: J'ai des tests Pytest pour chaque règle. Et les 122 anomalies détectées sont des cas réels (entités invalides, EBITDA incohérent, etc.).

**Q: Le dashboard, c'est du copier-coller ou tu l'as vraiment construit ?**  
R: Complètement construit. Voir `POWERBI_SUMMARY.md` pour la liste exacte : 5 tables relationnelles, 30 mesures DAX, thème custom JSON.

**Q: Pourquoi le scoring (Critique=5, Majeur=3, Mineur=1) ?**  
R: C'est un choix métier volontaire. Voir `docs/regles_qualite.md` pour la justification. Facilement paramétrable.

**Q: Vous avez combien de temps pour faire ça ?**  
R: ~2-3 jours pour l'ETL + tests, ~2 jours pour le dashboard Power BI complet.

---

**Créé le 31 mai 2026**  
**Prêt pour production ✅**
