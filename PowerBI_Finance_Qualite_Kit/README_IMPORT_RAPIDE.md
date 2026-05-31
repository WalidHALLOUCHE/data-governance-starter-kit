# Étapes rapides dans Power BI Desktop

1. Télécharger et décompresser le ZIP.
2. Ouvrir Power BI Desktop.
3. Cliquer sur `Obtenir les données` > `Texte/CSV`.
4. Importer les 5 fichiers du dossier `data/`.
5. Vérifier le séparateur : `;`.
6. Vérifier les types :
   - `date_periode` = Date
   - montants = Nombre décimal
   - scores ratio = Pourcentage
7. Créer la table `Calendrier` avec le fichier `powerbi/Table_Calendrier_DAX.dax`.
8. Créer les relations indiquées dans `docs/README_CREATION_POWERBI.md`.
9. Créer une table vide `Mesures`, puis coller les mesures du fichier `powerbi/Mesures_DAX_Finance_Qualite.dax`.
10. Importer le thème :
    - Affichage > Thèmes > Parcourir les thèmes
    - Choisir `powerbi/theme_finance_qualite.json`
11. Construire les 5 pages avec `docs/SPEC_VISUELLE_DASHBOARD.md`.

Important :
Le fichier `.pbix` ne peut pas être généré directement ici sans Power BI Desktop, mais ce kit contient tout ce qu’il faut pour reconstruire le dashboard proprement en quelques minutes.