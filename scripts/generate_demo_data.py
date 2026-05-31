"""
Génère les données fictives pour le starter kit de gouvernance data.
Ce script crée des données brutes avec anomalies intentionnelles pour tester
les contrôles qualité.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_REF = PROJECT_ROOT / "data" / "reference"

# Créer les dossiers s'ils n'existent pas
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_REF.mkdir(parents=True, exist_ok=True)


def create_referentiel_entites():
    """Crée le référentiel des entités."""
    data = {
        "code_entite": [
            "ENT_FR_001", "ENT_DE_001", "ENT_ES_001", "ENT_IT_001", "ENT_MA_001"
        ],
        "entite": [
            "Entité France", "Entité Allemagne", "Entité Espagne",
            "Entité Italie", "Entité Maroc"
        ],
        "pays": ["France", "Allemagne", "Espagne", "Italie", "Maroc"],
        "region": ["Europe", "Europe", "Europe", "Europe", "Afrique"],
        "statut_entite": ["Actif", "Actif", "Actif", "Actif", "Actif"],
    }
    df = pd.DataFrame(data)
    df.to_csv(DATA_REF / "referentiel_entites.csv", sep=";", encoding="utf-8",
              index=False)
    print(f"✓ Référentiel entités créé: {len(df)} lignes")
    return df


def create_referentiel_business_lines():
    """Crée le référentiel des business lines."""
    data = {
        "code_business_line": ["BL_DEV", "BL_CONST", "BL_EXP", "BL_SUP"],
        "business_line": [
            "Développement projets",
            "Construction",
            "Exploitation",
            "Fonctions support"
        ],
        "description": [
            "Pipeline et développement",
            "Construction et investissements CAPEX",
            "Exploitation et maintenance",
            "Finance, RH, IT et juridique"
        ],
    }
    df = pd.DataFrame(data)
    df.to_csv(DATA_REF / "referentiel_business_lines.csv", sep=";",
              encoding="utf-8", index=False)
    print(f"✓ Référentiel business lines créé: {len(df)} lignes")
    return df


def create_referentiel_projets():
    """Crée le référentiel des projets."""
    base_date = datetime(2023, 1, 1)
    data = {
        "code_projet": [
            "PRJ_001", "PRJ_002", "PRJ_003", "PRJ_004", "PRJ_005",
            "PRJ_006", "PRJ_007", "PRJ_008", "PRJ_009", "PRJ_010"
        ],
        "nom_projet": [
            "Projet solaire Nord", "Projet solaire Est", "Projet solaire Sud",
            "Projet éolien Ouest", "Projet hydro Central",
            "Projet PV Montagne", "Projet Énergie Verte", "Projet Smart Grid",
            "Projet Batterie Storage", "Projet Transition"
        ],
        "code_entite": [
            "ENT_FR_001", "ENT_DE_001", "ENT_ES_001", "ENT_IT_001", "ENT_MA_001",
            "ENT_FR_001", "ENT_DE_001", "ENT_ES_001", "ENT_IT_001", "ENT_MA_001"
        ],
        "code_business_line": [
            "BL_DEV", "BL_CONST", "BL_EXP", "BL_DEV", "BL_CONST",
            "BL_EXP", "BL_DEV", "BL_CONST", "BL_EXP", "BL_SUP"
        ],
        "statut_projet": [
            "Actif", "Actif", "En pause", "Actif", "Clos",
            "Actif", "Actif", "Planifié", "Actif", "Actif"
        ],
        "date_debut": [
            base_date + timedelta(days=i*30) for i in range(10)
        ],
        "date_fin_prevue": [
            base_date + timedelta(days=365 + i*30) for i in range(10)
        ],
    }
    df = pd.DataFrame(data)
    df.to_csv(DATA_REF / "referentiel_projets.csv", sep=";", encoding="utf-8",
              index=False)
    print(f"✓ Référentiel projets créé: {len(df)} lignes")
    return df


def create_referentiel_kpi():
    """Crée le référentiel des KPI."""
    data = {
        "code_kpi": [
            "KPI_CA", "KPI_OPEX", "KPI_CAPEX", "KPI_EBITDA",
            "KPI_MARGE_EBITDA", "KPI_ROI", "KPI_NPV", "KPI_IRR"
        ],
        "nom_kpi": [
            "Chiffre d'affaires", "OPEX", "CAPEX", "EBITDA",
            "Marge EBITDA", "ROI", "NPV", "Taux de retour interne"
        ],
        "domaine": [
            "Finance", "Finance", "Finance", "Finance",
            "Finance", "Finance", "Finance", "Finance"
        ],
        "formule": [
            "Somme du CA", "Somme des charges opérationnelles",
            "Somme des investissements", "CA - OPEX",
            "EBITDA / CA", "Profit / Investissement Initial",
            "Somme des cash flows actualisés", "Taux d'actualisation"
        ],
        "unite": ["EUR", "EUR", "EUR", "EUR", "%", "%", "EUR", "%"],
        "criticite": [
            "Haute", "Haute", "Haute", "Haute",
            "Moyenne", "Moyenne", "Moyenne", "Moyenne"
        ],
    }
    df = pd.DataFrame(data)
    df.to_csv(DATA_REF / "referentiel_kpi.csv", sep=";", encoding="utf-8",
              index=False)
    print(f"✓ Référentiel KPI créé: {len(df)} lignes")
    return df


def create_donnees_finance_raw():
    """Crée les données finance brutes avec anomalies intentionnelles."""
    np.random.seed(42)
    
    entites = ["ENT_FR_001", "ENT_DE_001", "ENT_ES_001", "ENT_IT_001", "ENT_MA_001"]
    projets = ["PRJ_001", "PRJ_002", "PRJ_003", "PRJ_004", "PRJ_005", "PRJ_006",
               "PRJ_007", "PRJ_008", "PRJ_009", "PRJ_010"]
    business_lines = ["BL_DEV", "BL_CONST", "BL_EXP", "BL_SUP"]
    periodes = []
    
    # Générer les périodes
    base_date = datetime(2023, 1, 1)
    for month in range(24):
        date = base_date + timedelta(days=month*30)
        periodes.append(date.strftime("%Y-%m"))
    
    # Générer les données
    data = []
    ligne_id = 1
    
    for _ in range(300):
        periode = np.random.choice(periodes)
        code_entite = np.random.choice(entites)
        code_projet = np.random.choice(projets)
        code_business_line = np.random.choice(business_lines)
        
        ca = np.random.uniform(100000, 5000000)
        opex = np.random.uniform(50000, ca * 0.6)
        capex = np.random.uniform(20000, 2000000)
        ebitda = ca - opex
        
        # Injecter des anomalies intentionnelles
        anomaly_type = np.random.choice(
            ["none", "entite_inconnue", "projet_inconnu", "bl_inconnu",
             "projet_vide", "ca_negatif", "opex_negatif", "capex_negatif",
             "ebitda_incoherent", "periode_vide", "periode_format", "valeur_manquante"],
            p=[0.7, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.07]
        )
        
        if anomaly_type == "entite_inconnue":
            code_entite = "ENT_XX_999"
        elif anomaly_type == "projet_inconnu":
            code_projet = "PRJ_999"
        elif anomaly_type == "bl_inconnu":
            code_business_line = "BL_UNKNOWN"
        elif anomaly_type == "projet_vide":
            code_projet = ""
        elif anomaly_type == "ca_negatif":
            ca = -np.random.uniform(100000, 500000)
        elif anomaly_type == "opex_negatif":
            opex = -np.random.uniform(50000, 200000)
        elif anomaly_type == "capex_negatif":
            capex = -np.random.uniform(20000, 100000)
        elif anomaly_type == "ebitda_incoherent":
            ebitda = np.random.uniform(10000000, 20000000)  # Très différent de ca-opex
        elif anomaly_type == "periode_vide":
            periode = ""
        elif anomaly_type == "periode_format":
            periode = "2023/01/01"  # Format invalide
        elif anomaly_type == "valeur_manquante":
            ca = np.nan if np.random.rand() > 0.5 else ca
        
        commentaire = "Source données test" if anomaly_type == "none" else f"Anomalie: {anomaly_type}"
        
        data.append({
            "periode": periode,
            "code_entite": code_entite,
            "code_projet": code_projet,
            "code_business_line": code_business_line,
            "ca_eur": ca,
            "opex_eur": opex,
            "capex_eur": capex,
            "ebitda_eur": ebitda,
            "commentaire_source": commentaire,
        })
        ligne_id += 1
    
    # Ajouter des doublons
    for i in range(5):
        data.append(data[i].copy())
    
    df = pd.DataFrame(data)
    df.to_csv(DATA_RAW / "donnees_finance_raw.csv", sep=";", encoding="utf-8",
              index=False)
    print(f"✓ Données finance brutes créées: {len(df)} lignes (avec anomalies)")
    return df


def create_donnees_projets_raw():
    """Crée les données projets brutes avec anomalies."""
    base_date = datetime(2023, 1, 1)
    
    data = []
    for i in range(15):
        code_projet = f"PRJX_{i+1:03d}"
        nom_projet = f"Projet énergie {i+1}"
        
        # Anomalies intentionnelles
        if i == 3:
            code_entite = ""  # Projet sans entité
        elif i == 5:
            code_entite = "ENT_UNKNOWN"  # Entité inconnue
        else:
            entites = ["ENT_FR_001", "ENT_DE_001", "ENT_ES_001", "ENT_IT_001", "ENT_MA_001"]
            code_entite = np.random.choice(entites)
        
        if i == 7:
            code_business_line = "BL_INVALID"  # Business line invalide
        else:
            bl = ["BL_DEV", "BL_CONST", "BL_EXP", "BL_SUP"]
            code_business_line = np.random.choice(bl)
        
        if i == 10:
            statut_projet = "Inexistant"  # Statut invalide
        else:
            statut_projet = np.random.choice(["Actif", "En pause", "Planifié", "Clos"])
        
        date_debut = base_date + timedelta(days=i*30)
        
        if i == 12:
            # Date de fin avant date de début
            date_fin_prevue = date_debut - timedelta(days=100)
        else:
            date_fin_prevue = date_debut + timedelta(days=365)
        
        data.append({
            "code_projet": code_projet,
            "nom_projet": nom_projet,
            "code_entite": code_entite,
            "code_business_line": code_business_line,
            "statut_projet": statut_projet,
            "date_debut": date_debut.strftime("%Y-%m-%d"),
            "date_fin_prevue": date_fin_prevue.strftime("%Y-%m-%d"),
        })
    
    df = pd.DataFrame(data)
    df.to_csv(DATA_RAW / "donnees_projets_raw.csv", sep=";", encoding="utf-8",
              index=False)
    print(f"✓ Données projets brutes créées: {len(df)} lignes (avec anomalies)")
    return df


def create_donnees_kpi_raw():
    """Crée les données KPI brutes avec anomalies."""
    data = []
    
    for i in range(12):
        code_kpi = f"KPI_{i+1:03d}"
        nom_kpi = f"Indicateur clé {i+1}"
        domaine = np.random.choice(["Finance", "Opérationnel", "RH", "IT"])
        
        if i == 2:
            formule = ""  # KPI sans formule
        else:
            formule = f"Calcul personnalisé {i+1}"
        
        if i == 4:
            unite = ""  # KPI sans unité
        else:
            unite = np.random.choice(["EUR", "%", "Nombre", "Jours"])
        
        if i == 6:
            criticite = "Critique"
            # KPI critique : pas très documenté
            description = ""
        else:
            criticite = np.random.choice(["Critique", "Majeure", "Mineure"])
            description = f"Description KPI {i+1}"
        
        data.append({
            "code_kpi": code_kpi,
            "nom_kpi": nom_kpi,
            "domaine": domaine,
            "formule": formule,
            "unite": unite,
            "criticite": criticite,
            "description": description,
        })
    
    # Ajouter des doublons
    data.append(data[0].copy())
    data.append(data[1].copy())
    
    df = pd.DataFrame(data)
    df.to_csv(DATA_RAW / "donnees_kpi_raw.csv", sep=";", encoding="utf-8",
              index=False)
    print(f"✓ Données KPI brutes créées: {len(df)} lignes (avec anomalies)")
    return df


def main():
    """Fonction principale."""
    print("\n" + "=" * 60)
    print("GÉNÉRATION DES DONNÉES FICTIVES DE DÉMONSTRATION")
    print("=" * 60 + "\n")
    
    create_referentiel_entites()
    create_referentiel_business_lines()
    create_referentiel_projets()
    create_referentiel_kpi()
    create_donnees_finance_raw()
    create_donnees_projets_raw()
    create_donnees_kpi_raw()
    
    print("\n" + "=" * 60)
    print("✓ GÉNÉRATION TERMINÉE")
    print("=" * 60)
    print("\nFichiers créés:")
    print("  - data/reference/referentiel_entites.csv")
    print("  - data/reference/referentiel_business_lines.csv")
    print("  - data/reference/referentiel_projets.csv")
    print("  - data/reference/referentiel_kpi.csv")
    print("  - data/raw/donnees_finance_raw.csv")
    print("  - data/raw/donnees_projets_raw.csv")
    print("  - data/raw/donnees_kpi_raw.csv")
    print("\nProchaine étape: python scripts/controle_qualite.py\n")


if __name__ == "__main__":
    main()
