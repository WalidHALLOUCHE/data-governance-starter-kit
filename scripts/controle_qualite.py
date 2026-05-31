"""
Contrôle qualité des données.
Détecte les anomalies, génère un rapport et produit des données nettoyées.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_REF = PROJECT_ROOT / "data" / "reference"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)


class ControleurQualite:
    """Classe pour contrôler la qualité des données."""
    
    def __init__(self):
        self.anomalies = []
        self.anomaly_id = 1
        self.referentiels = {}
        self.load_referentiels()
    
    def load_referentiels(self):
        """Charge les référentiels."""
        self.referentiels['entites'] = pd.read_csv(
            DATA_REF / "referentiel_entites.csv", sep=";", dtype=str
        )
        self.referentiels['projets'] = pd.read_csv(
            DATA_REF / "referentiel_projets.csv", sep=";"
        )
        self.referentiels['business_lines'] = pd.read_csv(
            DATA_REF / "referentiel_business_lines.csv", sep=";", dtype=str
        )
        self.referentiels['kpi'] = pd.read_csv(
            DATA_REF / "referentiel_kpi.csv", sep=";", dtype=str
        )
        print("✓ Référentiels chargés")
    
    def add_anomaly(self, source, ligne, type_anomalie, gravite, description,
                   code_entite="", code_projet="", code_business_line="",
                   code_kpi="", periode="", valeur_detectee="", correction=""):
        """Ajoute une anomalie au rapport."""
        self.anomalies.append({
            "id_anomalie": f"ANOM_{self.anomaly_id:06d}",
            "source": source,
            "ligne": ligne,
            "periode": periode,
            "code_entite": code_entite,
            "code_projet": code_projet,
            "code_business_line": code_business_line,
            "code_kpi": code_kpi,
            "type_anomalie": type_anomalie,
            "gravite": gravite,
            "description": description,
            "valeur_detectee": valeur_detectee,
            "correction_recommandee": correction,
            "date_detection": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        self.anomaly_id += 1
    
    def control_donnees_finance(self):
        """Contrôle les données finance."""
        print("\nContrôle des données finance...")
        df = pd.read_csv(DATA_RAW / "donnees_finance_raw.csv", sep=";")
        
        valid_entites = set(self.referentiels['entites']['code_entite'].values)
        valid_projets = set(self.referentiels['projets']['code_projet'].values)
        valid_bl = set(self.referentiels['business_lines']['code_business_line'].values)
        
        lignes_valides = []
        
        for idx, row in df.iterrows():
            ligne = idx + 2  # +2 pour account pour header et base 1
            has_anomaly = False
            
            # Vérifier la période
            if pd.isna(row['periode']) or row['periode'] == "":
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "PERIODE_INVALIDE", "Majeure",
                    "Période manquante", periode="", correction="Remplir la période"
                )
                has_anomaly = True
            elif not self._is_valid_periode(row['periode']):
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "PERIODE_INVALIDE", "Majeure",
                    f"Format période invalide: {row['periode']}",
                    periode=row['periode'], correction="Format attendu: YYYY-MM"
                )
                has_anomaly = True
            
            # Vérifier l'entité
            if row['code_entite'] not in valid_entites:
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "ENTITE_INCONNUE", "Critique",
                    f"Entité inconnue: {row['code_entite']}",
                    code_entite=row['code_entite'], periode=row['periode'],
                    correction="Vérifier contre le référentiel entités"
                )
                has_anomaly = True
            
            # Vérifier le projet
            if pd.isna(row['code_projet']) or row['code_projet'] == "":
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "VALEUR_MANQUANTE", "Majeure",
                    "Projet manquant",
                    code_entite=row['code_entite'], periode=row['periode'],
                    correction="Remplir le code projet"
                )
                has_anomaly = True
            elif row['code_projet'] not in valid_projets:
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "PROJET_INCONNU", "Critique",
                    f"Projet inconnu: {row['code_projet']}",
                    code_projet=row['code_projet'], code_entite=row['code_entite'],
                    periode=row['periode'], correction="Vérifier contre le référentiel projets"
                )
                has_anomaly = True
            
            # Vérifier la business line
            if row['code_business_line'] not in valid_bl:
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "BUSINESS_LINE_INCONNUE", "Critique",
                    f"Business line inconnue: {row['code_business_line']}",
                    code_business_line=row['code_business_line'],
                    code_entite=row['code_entite'], periode=row['periode'],
                    correction="Vérifier contre le référentiel business lines"
                )
                has_anomaly = True
            
            # Vérifier les montants
            if pd.notna(row['ca_eur']) and row['ca_eur'] < 0:
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "MONTANT_NEGATIF", "Majeure",
                    f"CA négatif: {row['ca_eur']}",
                    code_entite=row['code_entite'], periode=row['periode'],
                    valeur_detectee=str(row['ca_eur']), correction="CA doit être >= 0"
                )
                has_anomaly = True
            
            if pd.notna(row['opex_eur']) and row['opex_eur'] < 0:
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "MONTANT_NEGATIF", "Majeure",
                    f"OPEX négatif: {row['opex_eur']}",
                    code_entite=row['code_entite'], periode=row['periode'],
                    valeur_detectee=str(row['opex_eur']), correction="OPEX doit être >= 0"
                )
                has_anomaly = True
            
            if pd.notna(row['capex_eur']) and row['capex_eur'] < 0:
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "MONTANT_NEGATIF", "Majeure",
                    f"CAPEX négatif: {row['capex_eur']}",
                    code_entite=row['code_entite'], periode=row['periode'],
                    valeur_detectee=str(row['capex_eur']), correction="CAPEX doit être >= 0"
                )
                has_anomaly = True
            
            # Vérifier cohérence EBITDA
            if (pd.notna(row['ca_eur']) and pd.notna(row['opex_eur']) and
                pd.notna(row['ebitda_eur'])):
                ebitda_calcule = row['ca_eur'] - row['opex_eur']
                if abs(row['ebitda_eur'] - ebitda_calcule) > 1:  # Tolérance 1 EUR
                    self.add_anomaly(
                        "donnees_finance_raw", ligne, "EBITDA_INCOHERENT", "Majeure",
                        f"EBITDA incohérent: {row['ebitda_eur']} vs CA-OPEX={ebitda_calcule}",
                        code_entite=row['code_entite'], periode=row['periode'],
                        valeur_detectee=str(row['ebitda_eur']),
                        correction=f"EBITDA devrait être {ebitda_calcule}"
                    )
                    has_anomaly = True
            
            # Vérifier valeurs manquantes
            if pd.isna(row['ca_eur']):
                self.add_anomaly(
                    "donnees_finance_raw", ligne, "VALEUR_MANQUANTE", "Mineure",
                    "CA manquant",
                    code_entite=row['code_entite'], periode=row['periode'],
                    correction="Remplir la valeur de CA"
                )
                has_anomaly = True
            
            if not has_anomaly:
                lignes_valides.append(row)
        
        # Vérifier les doublons
        df_dedup = df.drop_duplicates(
            subset=['periode', 'code_entite', 'code_projet', 'code_business_line'],
            keep=False
        )
        
        if len(df) - len(df_dedup) > 0:
            print(f"  - {len(df) - len(df_dedup)} doublons détectés")
            for idx, row in df[df.duplicated(
                subset=['periode', 'code_entite', 'code_projet', 'code_business_line'],
                keep=False
            )].iterrows():
                self.add_anomaly(
                    "donnees_finance_raw", idx + 2, "DOUBLON", "Mineure",
                    "Enregistrement dupliqué",
                    code_entite=row['code_entite'], periode=row['periode'],
                    correction="Supprimer l'un des doublons"
                )
        
        df_clean = pd.DataFrame(lignes_valides)
        print(f"  Lignes valides: {len(df_clean)}/{len(df)}")
        return df_clean
    
    def control_donnees_projets(self):
        """Contrôle les données projets."""
        print("\nContrôle des données projets...")
        df = pd.read_csv(DATA_RAW / "donnees_projets_raw.csv", sep=";")
        
        valid_entites = set(self.referentiels['entites']['code_entite'].values)
        valid_projets = set(self.referentiels['projets']['code_projet'].values)
        valid_bl = set(self.referentiels['business_lines']['code_business_line'].values)
        valid_statuts = ["Actif", "En pause", "Planifié", "Clos"]
        
        for idx, row in df.iterrows():
            ligne = idx + 2
            
            if row['code_entite'] == "" or pd.isna(row['code_entite']):
                self.add_anomaly(
                    "donnees_projets_raw", ligne, "VALEUR_MANQUANTE", "Critique",
                    "Entité manquante pour le projet",
                    code_projet=row['code_projet'],
                    correction="Remplir le code entité"
                )
            elif row['code_entite'] not in valid_entites:
                self.add_anomaly(
                    "donnees_projets_raw", ligne, "ENTITE_INCONNUE", "Critique",
                    f"Entité inconnue: {row['code_entite']}",
                    code_entite=row['code_entite'], code_projet=row['code_projet'],
                    correction="Vérifier contre le référentiel entités"
                )
            
            if row['code_business_line'] not in valid_bl:
                self.add_anomaly(
                    "donnees_projets_raw", ligne, "BUSINESS_LINE_INCONNUE", "Critique",
                    f"Business line inconnue: {row['code_business_line']}",
                    code_business_line=row['code_business_line'],
                    code_projet=row['code_projet'],
                    correction="Vérifier contre le référentiel business lines"
                )
            
            if row['statut_projet'] not in valid_statuts:
                self.add_anomaly(
                    "donnees_projets_raw", ligne, "STATUT_INVALIDE", "Majeure",
                    f"Statut invalide: {row['statut_projet']}",
                    code_projet=row['code_projet'],
                    correction=f"Statut doit être parmi: {', '.join(valid_statuts)}"
                )
            
            # Vérifier la cohérence des dates
            try:
                debut = pd.to_datetime(row['date_debut'])
                fin = pd.to_datetime(row['date_fin_prevue'])
                if fin < debut:
                    self.add_anomaly(
                        "donnees_projets_raw", ligne, "DATE_INCOHERENTE", "Majeure",
                        f"Date fin avant date début",
                        code_projet=row['code_projet'],
                        valeur_detectee=f"{row['date_debut']} to {row['date_fin_prevue']}",
                        correction="Date fin doit être après date début"
                    )
            except Exception:
                pass
    
    def control_donnees_kpi(self):
        """Contrôle les données KPI."""
        print("\nContrôle des données KPI...")
        df = pd.read_csv(DATA_RAW / "donnees_kpi_raw.csv", sep=";")
        
        for idx, row in df.iterrows():
            ligne = idx + 2
            
            if row['formule'] == "" or pd.isna(row['formule']):
                self.add_anomaly(
                    "donnees_kpi_raw", ligne, "KPI_INCOMPLET", "Majeure",
                    "KPI sans formule",
                    code_kpi=row['code_kpi'],
                    correction="Remplir la formule du KPI"
                )
            
            if row['unite'] == "" or pd.isna(row['unite']):
                self.add_anomaly(
                    "donnees_kpi_raw", ligne, "KPI_INCOMPLET", "Majeure",
                    "KPI sans unité",
                    code_kpi=row['code_kpi'],
                    correction="Remplir l'unité du KPI"
                )
            
            if (row['criticite'] == "Critique" and
                (row['description'] == "" or pd.isna(row['description']))):
                self.add_anomaly(
                    "donnees_kpi_raw", ligne, "KPI_INCOMPLET", "Critique",
                    "KPI critique sans description",
                    code_kpi=row['code_kpi'],
                    correction="Documenter les KPI critiques"
                )
        
        # Vérifier les doublons
        doublons = df[df.duplicated(subset=['code_kpi'], keep=False)]
        if len(doublons) > 0:
            print(f"  - {len(doublons)} doublons KPI détectés")
            for idx, row in doublons.iterrows():
                self.add_anomaly(
                    "donnees_kpi_raw", idx + 2, "DOUBLON", "Mineure",
                    "KPI dupliqué",
                    code_kpi=row['code_kpi'],
                    correction="Supprimer l'un des doublons"
                )
    
    def _is_valid_periode(self, periode):
        """Vérifie si la période est au bon format."""
        if pd.isna(periode) or periode == "":
            return False
        try:
            # Format attendu: YYYY-MM
            if len(str(periode)) == 7 and str(periode)[4] == "-":
                pd.to_datetime(str(periode), format="%Y-%m")
                return True
            return False
        except Exception:
            return False
    
    def generer_rapports(self, df_clean):
        """Génère les rapports."""
        print("\nGénération des rapports...")
        
        # Rapport anomalies
        df_anomalies = pd.DataFrame(self.anomalies)
        df_anomalies.to_csv(DATA_PROCESSED / "rapport_anomalies.csv", sep=";",
                          encoding="utf-8", index=False)
        print(f"✓ Rapport anomalies: {len(df_anomalies)} anomalies détectées")
        
        # Données finance nettoyées
        df_clean.to_csv(DATA_PROCESSED / "donnees_finance_clean.csv", sep=";",
                       encoding="utf-8", index=False)
        print(f"✓ Données finance nettoyées: {len(df_clean)} lignes valides")
        
        # Résumé
        self._print_resume(df_anomalies)
    
    def _print_resume(self, df_anomalies):
        """Affiche un résumé."""
        print("\n" + "=" * 60)
        print("RÉSUMÉ CONTRÔLE QUALITÉ")
        print("=" * 60)
        
        total_anomalies = len(df_anomalies)
        anomalies_critiques = len(df_anomalies[df_anomalies['gravite'] == 'Critique'])
        anomalies_majeures = len(df_anomalies[df_anomalies['gravite'] == 'Majeure'])
        anomalies_mineures = len(df_anomalies[df_anomalies['gravite'] == 'Mineure'])
        
        print(f"\nTotal anomalies: {total_anomalies}")
        print(f"  - Critiques: {anomalies_critiques}")
        print(f"  - Majeures: {anomalies_majeures}")
        print(f"  - Mineures: {anomalies_mineures}")
        
        if total_anomalies > 0:
            print(f"\nPar source:")
            for source in df_anomalies['source'].unique():
                count = len(df_anomalies[df_anomalies['source'] == source])
                print(f"  - {source}: {count}")
            
            print(f"\nPar type:")
            for anomaly_type in df_anomalies['type_anomalie'].unique():
                count = len(df_anomalies[df_anomalies['type_anomalie'] == anomaly_type])
                print(f"  - {anomaly_type}: {count}")
        
        print("\n" + "=" * 60 + "\n")


def main():
    """Fonction principale."""
    controleur = ControleurQualite()
    df_clean = controleur.control_donnees_finance()
    controleur.control_donnees_projets()
    controleur.control_donnees_kpi()
    controleur.generer_rapports(df_clean)
    
    print("Prochaine étape: python scripts/generation_score_qualite.py\n")


if __name__ == "__main__":
    main()
