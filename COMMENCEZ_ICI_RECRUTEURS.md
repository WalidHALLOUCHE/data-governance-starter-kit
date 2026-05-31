# 👀 COMMENCEZ ICI — Guide de Lecture pour Recruteurs

## ⏱️ Version Rapide (5 min)

1. **Lire ce fichier** (vous êtes ici ✓)
2. **Consulter** [`POUR_LES_RECRUTEURS.md`](POUR_LES_RECRUTEURS.md) — Explique les compétences en 30 sec
3. **Regarder** [`powerbi/Capture d'écran 2026-05-31 030922.png`](powerbi/Capture%20d'écran%202026-05-31%20030922.png) — Le dashboard en action

✅ Vous comprenez le projet en **5 minutes**.

---

## ⏱️ Version Standard (15 min)

Suivre la version rapide + :

4. **Ouvrir** [`README.md`](README.md) — Voir la section "À PROPOS DE CE PROJET"
5. **Explorer** [`docs/architecture_projet.md`](docs/architecture_projet.md) — Comprendre le design

✅ Vous maîtrisez le projet en **15 minutes**.

---

## ⏱️ Version Approfondie (1h)

Pour les recruteurs techniques qui veulent vraiment comprendre :

### Étape 1 : Contexte (5 min)
- [`POUR_LES_RECRUTEURS.md`](POUR_LES_RECRUTEURS.md) — Quelles compétences ce projet démontre

### Étape 2 : Code Python (20 min)
- [`docs/regles_qualite.md`](docs/regles_qualite.md) — Les 11 règles métier
- [`scripts/controle_qualite.py`](scripts/controle_qualite.py) — Logique de détection
- [`scripts/generation_score_qualite.py`](scripts/generation_score_qualite.py) — Scoring pondéré

### Étape 3 : Power BI (25 min)
- **Ouvrir le fichier** : `powerbi/Dashboard_Finance_Qualite_Donnees.pbix` dans Power BI Desktop
- **Voir les mesures DAX** : [`PowerBI_Finance_Qualite_Kit/powerbi/Mesures_DAX_Finance_Qualite.dax`](PowerBI_Finance_Qualite_Kit/powerbi/Mesures_DAX_Finance_Qualite.dax) (~30 mesures)
- **Explorer le design** : [`docs/guide_powerbi.md`](docs/guide_powerbi.md) (construction des 5 pages)

### Étape 4 : Production (10 min)
- [`CHECKLIST_PUSH.md`](CHECKLIST_PUSH.md) — Prêt pour production
- [`POWERBI_SUMMARY.md`](POWERBI_SUMMARY.md) — Structure finale

---

## 🎯 Qu'est-ce que Vous Cherchez ?

### "Je veux vérifier les compétences Python/Pandas"
→ Lire : `scripts/controle_qualite.py` (détection anomalies)  
→ Voir : `scripts/generation_score_qualite.py` (scoring)  
→ Tests : `tests/test_controle_qualite.py` (validation)

### "Je veux vérifier les compétences Power BI"
→ Ouvrir : `powerbi/Dashboard_Finance_Qualite_Donnees.pbix`  
→ Lire : `PowerBI_Finance_Qualite_Kit/powerbi/Mesures_DAX_Finance_Qualite.dax`  
→ Docs : `docs/guide_powerbi.md` (architecture du dashboard)

### "Je veux vérifier l'architecture & la mentalité produit"
→ Lire : `docs/architecture_projet.md`  
→ Voir : `.gitignore`, `requirements.txt` (production-ready)  
→ Parcourir : `scripts/` (modularité, séparation responsabilités)

### "Je veux vérifier la documentation & la rigueur"
→ Lire : Tous les fichiers dans `docs/`  
→ Consulter : `POUR_LES_RECRUTEURS.md` (contexte complet)  
→ Naviguer : Ce projet sur GitHub (structure, commit history)

---

## 📊 Chiffres Clés

| Métrique | Valeur |
|----------|--------|
| **Données brutes** | 305 lignes |
| **Anomalies injectées** | 122 (30%) |
| **Règles appliquées** | 11 types |
| **Mesures Power BI** | 30+ |
| **Pages dashboard** | 5 |
| **Documentation** | 6 guides |
| **Tests** | 5 cas testés |
| **Taille totale** | 1.1 MB |

---

## ❓ Questions Fréquentes

**Q: Est-ce réel ou une démo pédagogique ?**  
A: **Les deux**. C'est une démo, mais réaliste. Les données sont fictives (contrôlées), mais les règles et le pipeline sont production-ready.

**Q: Combien de temps a pris ce projet ?**  
A: ~4-5 jours (Python ETL + tests : 2j, Power BI : 2j, docs : 1j).

**Q: Est-ce qu'on peut vraiment l'utiliser en production ?**  
A: **Oui**, juste adapter les sources de données. Tout est modulaire et documenté.

**Q: Quelle est la plus grosse compétence démontrée ?**  
A: **L'architecture complète** — conception ETL + modèle data + dashboarding + documentation. Pas un seul domaine, mais le cycle entier.

---

## 🚀 Prochaines Étapes

### Pour Tester Vous-même

```bash
# 1. Cloner le repo
git clone [URL]
cd projet-data

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Générer les données
python scripts/generate_demo_data.py

# 4. Exécuter le contrôle qualité
python scripts/controle_qualite.py

# 5. Ouvrir le dashboard Power BI
# (Ouvrir powerbi/Dashboard_Finance_Qualite_Donnees.pbix)
```

### Pour Discuter avec le Candidat

- "Comment vous avez choisi la pondération Critique=5, Majeur=3, Mineur=1 ?"
- "Pourquoi 5 pages Power BI et pas 3 ou 10 ?"
- "Comment adapteriez-vous ce pipeline pour 10M lignes ?"
- "Montrez-moi la mesure DAX la plus compliquée que vous ayez écrite"

---

## 📞 Contact

**Tout le code est commenté et documenté.**  
**Pas de question = lire la doc correspondante.**

---

**Version recruteurs** — Créée le 31 mai 2026  
**Prêt pour vos questions** ✅
