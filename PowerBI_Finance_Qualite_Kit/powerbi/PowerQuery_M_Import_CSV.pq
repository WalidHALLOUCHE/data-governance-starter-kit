/*
Power Query M - Import des fichiers CSV préparés.
Dans Power BI Desktop :
1. Accueil > Transformer les données
2. Gérer les paramètres > Nouveau paramètre : pDossierPowerBI
3. Valeur du paramètre = chemin du dossier "data" décompressé
4. Créer une requête vide par table et coller le code correspondant.
*/

/////////////////////////////////////////////
// Paramètre attendu
/////////////////////////////////////////////
// pDossierPowerBI = "C:\...\PowerBI_Finance_Qualite_Kit\data"

/////////////////////////////////////////////
// Table : donnees_finance_powerbi
/////////////////////////////////////////////
let
    Source = Csv.Document(
        File.Contents(pDossierPowerBI & "\donnees_finance_powerbi.csv"),
        [Delimiter=";", Columns=14, Encoding=65001, QuoteStyle=QuoteStyle.None]
    ),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(
        Headers,
        {
            {"periode", type text},
            {"code_entite", type text},
            {"code_projet", type text},
            {"code_business_line", type text},
            {"ca_eur", type number},
            {"opex_eur", type number},
            {"capex_eur", type number},
            {"ebitda_eur", type number},
            {"commentaire_source", type text},
            {"date_periode", type date},
            {"annee", Int64.Type},
            {"mois_num", Int64.Type},
            {"mois_annee", type text},
            {"cle_finance", type text}
        }
    )
in
    Types

/////////////////////////////////////////////
// Table : rapport_anomalies_powerbi
/////////////////////////////////////////////
let
    Source = Csv.Document(
        File.Contents(pDossierPowerBI & "\rapport_anomalies_powerbi.csv"),
        [Delimiter=";", Columns=18, Encoding=65001, QuoteStyle=QuoteStyle.None]
    ),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(
        Headers,
        {
            {"id_anomalie", type text},
            {"source", type text},
            {"ligne", Int64.Type},
            {"periode", type text},
            {"code_entite", type text},
            {"code_projet", type text},
            {"code_business_line", type text},
            {"code_kpi", type text},
            {"type_anomalie", type text},
            {"gravite", type text},
            {"description", type text},
            {"valeur_detectee", type text},
            {"correction_recommandee", type text},
            {"date_detection", type datetime},
            {"date_detection_date", type date},
            {"date_periode", type date},
            {"gravite_ordre", Int64.Type},
            {"cle_finance", type text}
        }
    )
in
    Types

/////////////////////////////////////////////
// Table : synthese_qualite_powerbi_ready
/////////////////////////////////////////////
let
    Source = Csv.Document(
        File.Contents(pDossierPowerBI & "\synthese_qualite_powerbi_ready.csv"),
        [Delimiter=";", Columns=8, Encoding=65001, QuoteStyle=QuoteStyle.None]
    ),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(
        Headers,
        {
            {"source", type text},
            {"total_lignes", Int64.Type},
            {"total_anomalies", Int64.Type},
            {"anomalies_critiques", Int64.Type},
            {"anomalies_majeures", Int64.Type},
            {"anomalies_mineures", Int64.Type},
            {"score_qualite", type number},
            {"score_qualite_ratio", Percentage.Type}
        }
    )
in
    Types

/////////////////////////////////////////////
// Table : score_qualite_global_powerbi
/////////////////////////////////////////////
let
    Source = Csv.Document(
        File.Contents(pDossierPowerBI & "\score_qualite_global_powerbi.csv"),
        [Delimiter=";", Columns=12, Encoding=65001, QuoteStyle=QuoteStyle.None]
    ),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(
        Headers,
        {
            {"total_lignes_controle", Int64.Type},
            {"lignes_valides", Int64.Type},
            {"lignes_invalides", Int64.Type},
            {"taux_validite", type number},
            {"total_anomalies", Int64.Type},
            {"anomalies_critiques", Int64.Type},
            {"anomalies_majeures", Int64.Type},
            {"anomalies_mineures", Int64.Type},
            {"taux_anomalies_pondere", type number},
            {"score_qualite_global", type number},
            {"taux_validite_ratio", Percentage.Type},
            {"score_qualite_global_ratio", Percentage.Type}
        }
    )
in
    Types

/////////////////////////////////////////////
// Table : statistiques_anomalies_powerbi
/////////////////////////////////////////////
let
    Source = Csv.Document(
        File.Contents(pDossierPowerBI & "\statistiques_anomalies_powerbi.csv"),
        [Delimiter=";", Columns=5, Encoding=65001, QuoteStyle=QuoteStyle.None]
    ),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(
        Headers,
        {
            {"type_anomalie", type text},
            {"nombre_anomalies", Int64.Type},
            {"anomalies_critiques", Int64.Type},
            {"anomalies_majeures", Int64.Type},
            {"anomalies_mineures", Int64.Type}
        }
    )
in
    Types