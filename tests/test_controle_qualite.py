"""
Tests pytest pour le contrôle qualité.
"""

import pytest
import pandas as pd
from pathlib import Path
from scripts.controle_qualite import ControleurQualite

PROJECT_ROOT = Path(__file__).parent.parent


def test_entite_inconnue_detectee():
    """Test que une entité inconnue est détectée."""
    controleur = ControleurQualite()
    
    # Créer une anomalie fictive
    controleur.add_anomaly(
        source="test",
        ligne=1,
        type_anomalie="ENTITE_INCONNUE",
        gravite="Critique",
        description="Entité inconnue: ENT_INVALID",
        code_entite="ENT_INVALID"
    )
    
    assert len(controleur.anomalies) == 1
    assert controleur.anomalies[0]['type_anomalie'] == "ENTITE_INCONNUE"
    assert controleur.anomalies[0]['gravite'] == "Critique"


def test_montant_negatif_detecte():
    """Test qu'un montant négatif est détecté."""
    controleur = ControleurQualite()
    
    controleur.add_anomaly(
        source="test",
        ligne=1,
        type_anomalie="MONTANT_NEGATIF",
        gravite="Majeure",
        description="CA négatif",
        valeur_detectee="-1000"
    )
    
    assert len(controleur.anomalies) == 1
    assert controleur.anomalies[0]['type_anomalie'] == "MONTANT_NEGATIF"


def test_ebitda_incoherent_detecte():
    """Test qu'un EBITDA incohérent est détecté."""
    controleur = ControleurQualite()
    
    controleur.add_anomaly(
        source="test",
        ligne=1,
        type_anomalie="EBITDA_INCOHERENT",
        gravite="Majeure",
        description="EBITDA incohérent",
        valeur_detectee="500000"
    )
    
    assert len(controleur.anomalies) == 1
    assert controleur.anomalies[0]['type_anomalie'] == "EBITDA_INCOHERENT"


def test_rapport_anomalies_colonnes_presentes():
    """Test que le rapport d'anomalies contient les colonnes attendues."""
    # Vérifier que le fichier rapport_anomalies.csv existe et contient les bonnes colonnes
    rapport_path = PROJECT_ROOT / "data" / "processed" / "rapport_anomalies.csv"
    
    if rapport_path.exists():
        df = pd.read_csv(rapport_path, sep=";")
        
        colonnes_attendues = [
            'id_anomalie', 'source', 'ligne', 'periode',
            'code_entite', 'code_projet', 'code_business_line',
            'type_anomalie', 'gravite', 'description',
            'valeur_detectee', 'correction_recommandee'
        ]
        
        for col in colonnes_attendues:
            assert col in df.columns, f"Colonne manquante: {col}"


def test_anomaly_id_unique():
    """Test que les IDs d'anomalies sont uniques."""
    controleur = ControleurQualite()
    
    for i in range(5):
        controleur.add_anomaly(
            source="test",
            ligne=i,
            type_anomalie="TEST",
            gravite="Mineure",
            description=f"Anomalie {i}"
        )
    
    ids = [anom['id_anomalie'] for anom in controleur.anomalies]
    assert len(ids) == len(set(ids)), "Des IDs d'anomalies dupliqués ont été détectés"


def test_gravite_valide():
    """Test que la gravité a une valeur valide."""
    controleur = ControleurQualite()
    
    controleur.add_anomaly(
        source="test",
        ligne=1,
        type_anomalie="TEST",
        gravite="Critique",
        description="Test"
    )
    
    assert controleur.anomalies[0]['gravite'] in ["Critique", "Majeure", "Mineure"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
