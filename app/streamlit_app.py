"""
Application Streamlit pour la gouvernance data.
Dashboard interactif pour visualiser la qualité des données.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Configuration Streamlit
st.set_page_config(
    page_title="Data Governance Starter Kit",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemins
PROJECT_ROOT = Path(__file__).parent.parent
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"


@st.cache_data
def load_data():
    """Charge les données."""
    try:
        anomalies_df = pd.read_csv(DATA_PROCESSED / "rapport_anomalies.csv", sep=";")
        score_global_df = pd.read_csv(DATA_PROCESSED / "score_qualite_donnees.csv", sep=";")
        synthese_df = pd.read_csv(DATA_PROCESSED / "synthese_qualite_powerbi.csv", sep=";")
        stats_anomalies = pd.read_csv(DATA_PROCESSED / "statistiques_anomalies.csv", sep=";")
        return anomalies_df, score_global_df, synthese_df, stats_anomalies
    except FileNotFoundError:
        return None, None, None, None


# Titre principal
st.markdown("# 📊 Data Governance Starter Kit")
st.markdown("### Référentiel & qualité des données")

# Charger les données
anomalies_df, score_global_df, synthese_df, stats_anomalies = load_data()

if anomalies_df is None:
    st.error("❌ Les fichiers de données n'ont pas été trouvés.")
    st.info("Veuillez exécuter les scripts:")
    st.code("""python scripts/generate_demo_data.py
python scripts/controle_qualite.py
python scripts/generation_score_qualite.py""")
    st.stop()

# ============================================================================
# BARRE LATÉRALE - FILTRES
# ============================================================================
st.sidebar.markdown("## 🔧 Filtres")

filter_source = st.sidebar.multiselect(
    "Source",
    options=sorted(anomalies_df['source'].unique()),
    default=sorted(anomalies_df['source'].unique())
)

filter_gravite = st.sidebar.multiselect(
    "Gravité",
    options=["Critique", "Majeure", "Mineure"],
    default=["Critique", "Majeure", "Mineure"]
)

filter_type = st.sidebar.multiselect(
    "Type d'anomalie",
    options=sorted(anomalies_df['type_anomalie'].unique()),
    default=sorted(anomalies_df['type_anomalie'].unique())
)

# Appliquer les filtres
anomalies_filtered = anomalies_df[
    (anomalies_df['source'].isin(filter_source)) &
    (anomalies_df['gravite'].isin(filter_gravite)) &
    (anomalies_df['type_anomalie'].isin(filter_type))
]

# ============================================================================
# SECTION KPI - INDICATEURS CLÉS
# ============================================================================
st.markdown("## 📈 Indicateurs clés")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_lignes = int(score_global_df['total_lignes_controle'].values[0])
    st.metric("Total lignes contrôlées", f"{total_lignes:,}")

with col2:
    total_anom = len(anomalies_df)
    st.metric("Total anomalies", f"{total_anom:,}")

with col3:
    anom_critiques = len(anomalies_df[anomalies_df['gravite'] == 'Critique'])
    st.metric("Anomalies critiques", f"{anom_critiques:,}")

with col4:
    score = float(score_global_df['score_qualite_global'].values[0])
    st.metric("Score qualité global", f"{score:.2f}%")

# ============================================================================
# SECTION GRAPHIQUES
# ============================================================================
st.markdown("## 📊 Analyse des anomalies")

col1, col2 = st.columns(2)

# Anomalies par type
with col1:
    st.subheader("Anomalies par type")
    anom_par_type = anomalies_filtered['type_anomalie'].value_counts().reset_index()
    anom_par_type.columns = ['Type', 'Nombre']
    fig_type = px.bar(
        anom_par_type,
        x='Nombre',
        y='Type',
        orientation='h',
        color='Nombre',
        color_continuous_scale='Reds'
    )
    fig_type.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_type, use_container_width=True)

# Anomalies par gravité
with col2:
    st.subheader("Anomalies par gravité")
    anom_par_gravite = anomalies_filtered['gravite'].value_counts().reset_index()
    anom_par_gravite.columns = ['Gravité', 'Nombre']
    
    # Ordonner: Critique > Majeure > Mineure
    gravite_order = {'Critique': 0, 'Majeure': 1, 'Mineure': 2}
    anom_par_gravite['order'] = anom_par_gravite['Gravité'].map(gravite_order)
    anom_par_gravite = anom_par_gravite.sort_values('order').drop('order', axis=1)
    
    colors = {'Critique': '#d62728', 'Majeure': '#ff7f0e', 'Mineure': '#2ca02c'}
    fig_gravite = px.pie(
        anom_par_gravite,
        names='Gravité',
        values='Nombre',
        color='Gravité',
        color_discrete_map=colors
    )
    fig_gravite.update_layout(height=400)
    st.plotly_chart(fig_gravite, use_container_width=True)

# Anomalies par source
st.subheader("Anomalies par source")
anom_par_source = anomalies_filtered['source'].value_counts().reset_index()
anom_par_source.columns = ['Source', 'Nombre']
fig_source = px.bar(
    anom_par_source,
    x='Source',
    y='Nombre',
    color='Nombre',
    color_continuous_scale='Blues'
)
fig_source.update_layout(height=350)
st.plotly_chart(fig_source, use_container_width=True)

# Score qualité par source
st.subheader("Score qualité par source")
fig_score = px.bar(
    synthese_df,
    x='source',
    y='score_qualite',
    color='score_qualite',
    color_continuous_scale='RdYlGn',
    title="Score qualité par source (%)"
)
fig_score.update_yaxes(range=[0, 100])
fig_score.update_layout(height=400)
st.plotly_chart(fig_score, use_container_width=True)

# ============================================================================
# SECTION TABLEAU ANOMALIES
# ============================================================================
st.markdown("## 📋 Tableau détaillé des anomalies")

# Colonnes à afficher
colonnes_affichage = [
    'id_anomalie', 'source', 'type_anomalie', 'gravite',
    'description', 'correction_recommandee', 'date_detection'
]

# Vérifier la présence des colonnes
colonnes_affichage = [col for col in colonnes_affichage if col in anomalies_filtered.columns]

# Afficher le tableau
st.dataframe(
    anomalies_filtered[colonnes_affichage].reset_index(drop=True),
    height=400,
    use_container_width=True
)

# ============================================================================
# SECTION STATISTIQUES DÉTAILLÉES
# ============================================================================
st.markdown("## 📊 Statistiques détaillées")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Résumé des anomalies filtrées")
    resume = {
        'Total anomalies filtrées': len(anomalies_filtered),
        'Critiques': len(anomalies_filtered[anomalies_filtered['gravite'] == 'Critique']),
        'Majeures': len(anomalies_filtered[anomalies_filtered['gravite'] == 'Majeure']),
        'Mineures': len(anomalies_filtered[anomalies_filtered['gravite'] == 'Mineure']),
    }
    
    for label, value in resume.items():
        st.metric(label, value)

with col2:
    st.subheader("Score qualité par source")
    for _, row in synthese_df.iterrows():
        st.text(
            f"{row['source']}: {row['score_qualite']:.2f}% "
            f"({int(row['total_anomalies'])} anomalies)"
        )

# ============================================================================
# PIED DE PAGE
# ============================================================================
st.markdown("---")
st.markdown(
    "**Data Governance Starter Kit** | "
    "Projet démonstration | "
    "Données fictives"
)
