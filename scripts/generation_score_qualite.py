"""
Génération du score qualité des données.
Calcule les métriques et génère les fichiers de synthèse.
"""

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)


class GenerateurScoreQualite:
    """Classe pour générer les scores de qualité."""
    
    def __init__(self):
        self.rapport_anomalies = None
        self.donnees_finance_clean = None
        self.donnees_finance_raw = None
        self.load_data()
    
    def load_data(self):
        """Charge les données nécessaires."""
        self.rapport_anomalies = pd.read_csv(
            DATA_PROCESSED / "rapport_anomalies.csv", sep=";"
        )
        self.donnees_finance_clean = pd.read_csv(
            DATA_PROCESSED / "donnees_finance_clean.csv", sep=";"
        )
        self.donnees_finance_raw = pd.read_csv(
            DATA_RAW / "donnees_finance_raw.csv", sep=";"
        )
        print("✓ Données chargées")
    
    def calculer_score_qualite(self):
        """Calcule le score qualité global."""
        total_lignes = len(self.donnees_finance_raw)
        lignes_valides = len(self.donnees_finance_clean)
        
        # Calcul des points perdus par gravité (pondération)
        df_anom = self.rapport_anomalies
        
        points_perdu_critique = len(df_anom[df_anom['gravite'] == 'Critique']) * 5
        points_perdu_majeure = len(df_anom[df_anom['gravite'] == 'Majeure']) * 3
        points_perdu_mineure = len(df_anom[df_anom['gravite'] == 'Mineure']) * 1
        
        total_points_perdu = points_perdu_critique + points_perdu_majeure + points_perdu_mineure
        
        # Formule: score = max(0, 100 - taux_anomalies_pondere)
        score_qualite_global = max(0, 100 - (total_points_perdu / total_lignes) * 100)
        
        return {
            'total_lignes_controle': total_lignes,
            'lignes_valides': lignes_valides,
            'lignes_invalides': total_lignes - lignes_valides,
            'taux_validite': (lignes_valides / total_lignes * 100) if total_lignes > 0 else 0,
            'total_anomalies': len(df_anom),
            'anomalies_critiques': len(df_anom[df_anom['gravite'] == 'Critique']),
            'anomalies_majeures': len(df_anom[df_anom['gravite'] == 'Majeure']),
            'anomalies_mineures': len(df_anom[df_anom['gravite'] == 'Mineure']),
            'taux_anomalies_pondere': (total_points_perdu / total_lignes * 100) if total_lignes > 0 else 0,
            'score_qualite_global': score_qualite_global,
        }
    
    def calculer_score_par_source(self):
        """Calcule le score qualité par source de données."""
        df_anom = self.rapport_anomalies
        
        sources = df_anom['source'].unique()
        scores = []
        
        for source in sources:
            df_source = df_anom[df_anom['source'] == source]
            
            # Déterminer le nombre total de lignes pour cette source
            if 'finance' in source:
                total = len(self.donnees_finance_raw)
            elif 'projets' in source:
                total = len(pd.read_csv(DATA_RAW / "donnees_projets_raw.csv", sep=";"))
            elif 'kpi' in source:
                total = len(pd.read_csv(DATA_RAW / "donnees_kpi_raw.csv", sep=";"))
            else:
                total = 1
            
            # Calcul du score
            points_perdu = (
                len(df_source[df_source['gravite'] == 'Critique']) * 5 +
                len(df_source[df_source['gravite'] == 'Majeure']) * 3 +
                len(df_source[df_source['gravite'] == 'Mineure']) * 1
            )
            
            score = max(0, 100 - (points_perdu / total * 100))
            
            scores.append({
                'source': source,
                'total_lignes': total,
                'total_anomalies': len(df_source),
                'anomalies_critiques': len(df_source[df_source['gravite'] == 'Critique']),
                'anomalies_majeures': len(df_source[df_source['gravite'] == 'Majeure']),
                'anomalies_mineures': len(df_source[df_source['gravite'] == 'Mineure']),
                'score_qualite': score,
            })
        
        return pd.DataFrame(scores)
    
    def calculer_score_par_type_anomalie(self):
        """Calcule le nombre d'anomalies par type."""
        df_anom = self.rapport_anomalies
        
        types = df_anom['type_anomalie'].unique()
        stats = []
        
        for anomaly_type in types:
            df_type = df_anom[df_anom['type_anomalie'] == anomaly_type]
            stats.append({
                'type_anomalie': anomaly_type,
                'nombre_anomalies': len(df_type),
                'anomalies_critiques': len(df_type[df_type['gravite'] == 'Critique']),
                'anomalies_majeures': len(df_type[df_type['gravite'] == 'Majeure']),
                'anomalies_mineures': len(df_type[df_type['gravite'] == 'Mineure']),
            })
        
        return pd.DataFrame(stats)
    
    def generer_fichiers(self):
        """Génère tous les fichiers de sortie."""
        print("\n" + "=" * 60)
        print("GÉNÉRATION DES SCORES QUALITÉ")
        print("=" * 60 + "\n")
        
        # Score qualité global
        score_global = self.calculer_score_qualite()
        
        # Fichier score_qualite_donnees.csv
        df_score_global = pd.DataFrame([score_global])
        df_score_global.to_csv(DATA_PROCESSED / "score_qualite_donnees.csv", sep=";",
                              encoding="utf-8", index=False)
        
        print("Score qualité global:")
        print(f"  - Score: {score_global['score_qualite_global']:.2f}%")
        print(f"  - Lignes contrôlées: {score_global['total_lignes_controle']}")
        print(f"  - Lignes valides: {score_global['lignes_valides']}")
        print(f"  - Total anomalies: {score_global['total_anomalies']}")
        print(f"    - Critiques: {score_global['anomalies_critiques']}")
        print(f"    - Majeures: {score_global['anomalies_majeures']}")
        print(f"    - Mineures: {score_global['anomalies_mineures']}")
        
        # Fichier synthese_qualite_powerbi.csv
        df_score_source = self.calculer_score_par_source()
        df_score_source.to_csv(DATA_PROCESSED / "synthese_qualite_powerbi.csv", sep=";",
                              encoding="utf-8", index=False)
        
        print("\nScore qualité par source:")
        for _, row in df_score_source.iterrows():
            print(f"  - {row['source']}: {row['score_qualite']:.2f}% ({row['total_anomalies']} anomalies)")
        
        # Fichier statistiques par type d'anomalie
        df_type_anomalie = self.calculer_score_par_type_anomalie()
        df_type_anomalie.to_csv(DATA_PROCESSED / "statistiques_anomalies.csv", sep=";",
                               encoding="utf-8", index=False)
        
        print("\nAnomalies par type:")
        for _, row in df_type_anomalie.iterrows():
            print(f"  - {row['type_anomalie']}: {row['nombre_anomalies']}")
        
        print("\n" + "=" * 60)
        print("✓ FICHIERS GÉNÉRÉS")
        print("=" * 60)
        print("\nFichiers créés dans data/processed/:")
        print("  - score_qualite_donnees.csv")
        print("  - synthese_qualite_powerbi.csv")
        print("  - statistiques_anomalies.csv")
        print("\nProchaine étape: streamlit run app/streamlit_app.py\n")


def main():
    """Fonction principale."""
    generateur = GenerateurScoreQualite()
    generateur.generer_fichiers()


if __name__ == "__main__":
    main()
