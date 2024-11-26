import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.graph_maker import display_select_grap

def display_grap_analysis(data):
    st.header("Análisis de informacion")

    # Crear barra lateral para seleccionar el tipo de gráfico y filtrar datos
    chart_type = st.sidebar.selectbox(
        "Selecciona el tipo de gráfico:",
        ["Dispersión", "Barras", "Histograma", "Linea"],
    )

    # Filtrar datos por múltiples columnas
    st.sidebar.subheader("Filtros")
    gender = st.sidebar.multiselect(
        "Selecciona el Genero:", data["Gender"].unique(), default=data["Gender"].unique()
    )
    worktype = st.sidebar.multiselect(
        "Selecciona el tipo de entrenamiento:", data["Workout_Type"].unique(), default=data["Workout_Type"].unique()
    )
    frequency = st.sidebar.multiselect(
        "Frecuencia de entrenamiento(Semanal):", data["Workout_Frequency (days/week)"].unique(), default=data["Workout_Frequency (days/week)"].unique(),
    )
    expe = st.sidebar.multiselect(
        "Selecciona el nivel de Experiencia:", data["Experience_Level"].unique(), default=data["Experience_Level"].unique()
    )

    # Aplicar filtros
    filtered_df = data[
        (data["Gender"].isin(gender))
        & (data["Workout_Type"].isin(worktype))
        & (data["Workout_Frequency (days/week)"].isin(frequency))
        & (data["Experience_Level"].isin(expe))
    ]

    display_select_grap(chart_type, filtered_df )
