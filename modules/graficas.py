import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def display_grap_analysis(data):
    st.header("Análisis de Features")

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

    # Crear dos columnas
    col1, col2 = st.columns(2)

    # Mostrar el gráfico seleccionado en la primera columna

    if chart_type == "Dispersión":
        with col1:
            st.header("Calorias quemadas vs Porcentage de Grasa:")
            fig, ax = plt.subplots()
            sns.scatterplot(
                data=filtered_df, x="Fat_Percentage", y="Calories_Burned", ax=ax, color="blue"
            )
            st.pyplot(fig)
        with col2:
            st.header("Duracion del Entrenamiento vs Porcentage de Grasa:")
            fig, ax = plt.subplots()
            sns.scatterplot(
                data=filtered_df, x="Fat_Percentage", y="Session_Duration (hours)", ax=ax, color="blue"
            )
            st.pyplot(fig)
    elif chart_type == "Barras":
        st.header("Promedio de Calorias quemadas por ejercicio:")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(
            data=filtered_df,
            x="Workout_Type",
            y="Calories_Burned",
            ax=ax,
            ci=None,
            color="lightblue",
        )
        st.pyplot(fig)
    elif chart_type == "Histograma":
        st.header("Indice de Masa Corporal:")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(
            data=filtered_df, x="BMI", bins=10, ax=ax, color="skyblue"
        )
        st.pyplot(fig)
    elif chart_type == "Linea":
        st.header("Calorias Quemadas por Genero:")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(
            data=filtered_df, x="Age", y="Calories_Burned", ax=ax, color="lightgreen", hue="Gender"
        )
        st.pyplot(fig)
