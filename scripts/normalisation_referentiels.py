"""
Normalisation des référentiels.
Applique des transformations de nettoyage et harmonisation.
"""

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_REF = PROJECT_ROOT / "data" / "reference"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)


def normaliser_referentiels():
    """Normalise tous les référentiels."""
    print("\n" + "=" * 60)
    print("NORMALISATION DES RÉFÉRENTIELS")
    print("=" * 60 + "\n")
    
    fichiers = [
        "referentiel_entites.csv",
        "referentiel_business_lines.csv",
        "referentiel_projets.csv",
        "referentiel_kpi.csv",
    ]
    
    for fichier in fichiers:
        path = DATA_REF / fichier
        if path.exists():
            df = pd.read_csv(path, sep=";")
            
            # Normaliser les codes en majuscules
            for col in df.columns:
                if 'code' in col.lower():
                    df[col] = df[col].str.upper().str.strip()
            
            # Supprimer les espaces inutiles dans tous les champs texte
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].str.strip()
            
            # Sauvegarder
            df.to_csv(path, sep=";", encoding="utf-8", index=False)
            print(f"✓ {fichier}: normalisé ({len(df)} lignes)")
    
    print("\n" + "=" * 60)
    print("✓ NORMALISATION COMPLÉTÉE")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    normaliser_referentiels()
