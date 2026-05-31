# Gouvernance des données - Méthodologie

## Contexte

La gouvernance data est l'ensemble des processus, politiques et technologies permettant de gérer les données comme un actif critique de l'entreprise. Ce document décrit la méthodologie appliquée dans ce starter kit.

---

## Principes fondamentaux

### 1. Unicité de la vérité (Single Source of Truth)

- **Référentiels centralisés** : Entités, projets, KPIs, business lines
- **Données brutes immuables** : Archivées telles que reçues
- **Données nettoyées traçables** : Avec historique anomalies
- **Un seul export Power BI** : Synthèse qualité validée

### 2. Qualité avant utilisation

Les données ne peuvent être utilisées pour la prise de décision que si :
- ✅ Elles ont passé les contrôles qualité
- ✅ Anomalies critiques = 0
- ✅ Score qualité ≥ 85%
- ✅ Traçabilité assurée

### 3. Traçabilité complète

Chaque donnée doit pouvoir être tracée :
- Source d'origine
- Transformations appliquées
- Anomalies détectées
- Corrections effectuées
- Date/utilisateur intervention

### 4. Responsabilité métier

- **Propriétaire données** : Responsable de la qualité à la source
- **Propriétaire référentiel** : Valide contenu et mises à jour
- **Contrôleur qualité** : Exécute vérifications automatisées
- **Utilisateur final** : Consomme données certifiées

---

## Architecture de gouvernance

```
┌─────────────────────────────────────────────────────────────┐
│ SOURCES MÉTIER (ERP, Outils projet, Fichiers Excel)       │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  ZONE RAW (Brute)   │ ← Immuable, en tant que reçue
        ├──────────────────────┤
        │ • donnees_*.csv     │
        │ • Métadonnées source│
        │ • Hash/Checksum     │
        └──────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  RÉFÉRENTIELS       │ ← Source unique de vérité
        ├──────────────────────┤
        │ • Entités           │
        │ • Projets           │
        │ • KPIs              │
        │ • Business lines    │
        └──────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  CONTRÔLE QUALITÉ   │ ← Détection anomalies
        ├──────────────────────┤
        │ • Validations ref.  │
        │ • Règles métier     │
        │ • Détection doublons│
        │ • Cohérences        │
        └──────────────────────┘
                   │
        ┌──────────┴───────────┐
        ▼                      ▼
    ✅ VALIDES           ❌ ANOMALIES
    ┌──────────────┐   ┌──────────────────┐
    │Données clean │   │Rapport anomalies │
    │ & processed  │   │ & corrections    │
    └──────┬───────┘   └────────┬─────────┘
           │                    │
           ▼                    ▼
    ┌──────────────┐   ┌──────────────────┐
    │ SYNTHÈSES    │   │ ASSIGNATION MÉTIER
    │ POWER BI     │   │ Priorité/Action  │
    └──────┬───────┘   └────────┬─────────┘
           │                    │
           ▼                    ▼
    ┌──────────────────────────────────┐
    │ DASHBOARDS DÉCISIONNELS (BI)     │
    │ MODÈLES IA/ML                    │
    │ RAPPORTS EXÉCUTIFS               │
    └──────────────────────────────────┘
```

---

## Composants de la gouvernance

### 1. RÉFÉRENTIELS MÉTIER

**Objectif** : Garantir l'unicité et la cohérence des codes/catégories

#### Référentiel entités
- Liste des entités légales/opérationnelles
- Code, libellé, localisation, statut
- **Propriétaire** : Directeur Administratif & Financier
- **Fréquence mise à jour** : Trimestrielle

#### Référentiel projets
- Portfolio complet des projets actifs
- Code, nom, entité, business line, dates
- **Propriétaire** : Chef de projet ou PMO
- **Fréquence mise à jour** : Mensuelle

#### Référentiel business lines
- Classification de l'activité (ex: Dev, Construction, Exploitation)
- Code, libellé, description
- **Propriétaire** : Directeur général/Stratégie
- **Fréquence mise à jour** : Annuelle

#### Référentiel KPIs
- Indicateurs clés du pilotage
- Code, formule, unité, criticité
- **Propriétaire** : Contrôle de gestion ou Analytics
- **Fréquence mise à jour** : Semestrielle

### 2. DICTIONNAIRE DE DONNÉES

**Objectif** : Documenter toutes les colonnes et règles métier

- Chaque fichier CSV documenté
- Types de données, formats, domaines
- Règles de validation associées
- Exemples corrects/incorrects
- Responsable

**Avantage** : Onboarding nouveau analytique, prévention erreurs

### 3. RÈGLES QUALITÉ

**Objectif** : Détecter automatiquement les anomalies

11 règles implémentées :
- Validité références (entité, projet, BL, KPI)
- Montants positifs
- Cohérence financière (EBITDA)
- Formats dates/périodes
- Absence doublons
- Statuts valides
- Documentation KPIs

**Pondération** : Critique (5 pts) > Majeure (3 pts) > Mineure (1 pt)

### 4. CONTRÔLES AUTOMATISÉS

**Exécution** : Scripts Python lancés à fréquence définie

```
Data RAW + Référentiels
    ↓
Script controle_qualite.py
    ├─ Validation métier
    ├─ Génération rapport anomalies
    └─ Données propres
    ↓
Script generation_score_qualite.py
    ├─ Score qualité global
    ├─ Score par source
    └─ Statistiques par type
    ↓
Synthèse Power BI
    ├─ Tableau anomalies
    ├─ Indicateurs qualité
    └─ Tendances
```

### 5. ESCALADE ANOMALIES

| Gravité | Qui | Délai | Action |
|---------|-----|-------|--------|
| 🔴 Critique | Propriétaire données | 24h | Corriger source |
| 🟠 Majeure | Manager métier | 1 semaine | Analyser + corriger |
| 🟢 Mineure | Équipe data | 1 mois | Ajouter contrôle |

### 6. MONITORING CONTINU

**Dashboard Power BI** :
- Score qualité en tendance
- Top 10 anomalies par type
- Heatmap sources vs gravité
- Courbe anomalies/temps

**Alertes** :
- 🔴 Score < 80% → Alerte immédiate
- 🟠 Anomalies critiques > 5% → Alerte quotidienne
- 🟢 Tendance + mauvaise → Alerte hebdomadaire

---

## Cas d'usage

### Cas 1 : Préparation Power BI

```
1. Charger donnees_finance_clean.csv
2. Linker à synthese_qualite_powerbi.csv
3. Créer mesures DAX :
   - Total anomalies
   - Score qualité
   - Taux validité
4. Créer pages :
   - Vue qualité globale
   - Anomalies par source
   - Suivi KPIs
5. Paramétrer alertes si score < 90%
```

### Cas 2 : Modèle Machine Learning

```
1. Charger donnees_finance_clean.csv
2. Vérifier score qualité ≥ 85%
3. Charger rapport_anomalies.csv
4. Filtrer anomalies par type pertinent
5. Créer features à partir données propres
6. Entraîner modèle
7. Valider prédictions vs anomalies historiques
```

### Cas 3 : Audit/Conformité

```
1. Vérifier traçabilité complète
2. Consulter rapport_anomalies.csv
3. Vérifier corrections appliquées
4. Valider score qualité > threshold
5. Générer certificat qualité données
```

---

## Matrice des responsabilités

| Rôle | Données brutes | Référentiels | Contrôles | Correction | Utilisation |
|------|---|---|---|---|---|
| **Producteur données** | 📝 Produit | ❌ - | ❌ - | ⚠️ Aide | ❌ - |
| **Propriétaire métier** | ⚠️ Valide | 📝 Maîtrise | ❌ - | 📝 Corrige | 📝 Utilise |
| **Data Steward** | ⚠️ Reçoit | ⚠️ Suit | 📝 Exécute | ⚠️ Suit | ❌ - |
| **Analyste data** | 📖 Lit | 📖 Consulte | ⚠️ Valide | ⚠️ Aide | 📖 Consomme |
| **CIO/DSI** | ❌ - | ⚠️ Gouverne | ⚠️ Supervise | ⚠️ Escalade | ❌ - |

**Légende** : 📝 Propriétaire | ⚠️ Contributeur | 📖 Consommateur | ❌ Non concerné

---

## Bonnes pratiques

### ✅ À faire

- ✅ Documenter AVANT les données
- ✅ Tester dès que possible
- ✅ Automatiser les contrôles
- ✅ Tracer les anomalies
- ✅ Escalader rapidement
- ✅ Communiquer les problèmes
- ✅ Valider avec métier
- ✅ Archiver immutable

### ❌ À éviter

- ❌ Nettoyer sans tracer
- ❌ Ignorer anomalies
- ❌ Données sans référentiel
- ❌ Contrôles manuels
- ❌ Pas de documentation
- ❌ Données multiples sources
- ❌ Corriger après utilisation
- ❌ Décisions sur données doutes

---

## Évolution du modèle

### Phase 1 (Actuellement)
✅ Référentiels statiques
✅ Contrôles en batch
✅ Rapports statiques

### Phase 2 (Futur court terme)
🔄 Contrôles temps réel (streaming)
🔄 Alertes automatiques Slack
🔄 Historique versioning référentiels

### Phase 3 (Futur moyen terme)
🔄 Machine Learning anomalies
🔄 Prédiction qualité données
🔄 Auto-correction suggestions

### Phase 4 (Futur long terme)
🔄 Gouvernance collaborative (web)
🔄 Cataloge données complet
🔄 Lineage visualisé

---

## Ressources additionnelles

### Standards externes

- **ISO 8601** : Formats dates/temps
- **ISO 20022** : Codification codes pays
- **GDPR** : Confidentialité données (si données réelles)
- **ISO 27001** : Sécurité information

### Outils recommandés

- **Apache Airflow** : Orchestration contrôles
- **dbt** : Transformation données
- **Great Expectations** : Validation données avancée
- **Collibra** : Governance plateforme

### Formation

- Tous les utilisateurs → Guide utilisation
- Data Stewards → Gestion référentiels
- Analystes → Détection anomalies
- Métier → Escalade impacts
