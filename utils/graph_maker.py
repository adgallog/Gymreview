import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def display_select_grap(chart_type, filtered_df ):
    # Crear dos columnas
    col1, col2 = st.columns(2)

    if chart_type == "Dispersión":
        with col1:            
            fig, ax = plt.subplots(figsize=(10, 10))
            fig.patch.set_facecolor('none')
            ax.set_facecolor('none')
            sns.scatterplot(
                data=filtered_df, x="Fat_Percentage", y="Calories_Burned", ax=ax, color="red"
            )
            ax.set_xlabel("Porcentaje de Grasa (%)", fontsize=20, color='white')  # Etiqueta del eje X
            ax.set_ylabel("Calorias quemadas", fontsize=20, color='white')  # Etiqueta del eje Y
            ax.set_title("Calorias quemadas vs Porcentaje de Grasa", fontsize=22, color='white')  # Título del gráfico
            ax.tick_params(axis='both', which='major', labelsize=12, labelcolor='white')
            ax.grid(True, which='both', axis='both', color='white', linestyle='--', linewidth=0.5)
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(10, 10))
            fig.patch.set_facecolor('none')
            ax.set_facecolor('none')
            sns.scatterplot(
                data=filtered_df, x="Fat_Percentage", y="Session_Duration (hours)", ax=ax, color="red"
            )
            ax.set_xlabel("Porcentaje de Grasa (%)", fontsize=20, color='white')  # Etiqueta del eje X
            ax.set_ylabel("Duración de la Sesión (horas)", fontsize=20, color='white')  # Etiqueta del eje Y
            ax.set_title("Duración del Entrenamiento vs Porcentaje de Grasa", fontsize=22, color='white')  # Título del gráfico
            ax.tick_params(axis='both', which='major', labelsize=12, labelcolor='white')
            ax.grid(True, which='both', axis='both', color='white', linestyle='--', linewidth=0.5)
            st.pyplot(fig)

    elif chart_type == "Barras":
        
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')
        sns.barplot(
            data=filtered_df,
            x="Workout_Type",
            y="Calories_Burned",
            ax=ax,
            ci=None,
            color="yellow",
        )
        ax.set_xlabel("Tipo de entrenamiento", fontsize=14, color='white')  # Etiqueta del eje X
        ax.set_ylabel("Calorias quemadas", fontsize=14, color='white')  # Etiqueta del eje Y
        ax.set_title("Promedio de Calorias quemadas por ejercicio:", fontsize=20, color='white')  # Título del gráfico
        ax.tick_params(axis='both', which='major', labelsize=12, labelcolor='white')
        ax.grid(True, which='both', axis='both', color='white', linestyle='--', linewidth=0.5)
        st.pyplot(fig)
    elif chart_type == "Histograma":
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')
        sns.histplot(
            data=filtered_df, x="BMI", bins=10, ax=ax, color="skyblue"
        )
        ax.set_xlabel("Indice de Masa Corporal", fontsize=14, color='white')  # Etiqueta del eje X
        ax.set_ylabel("Cantidad de Personas", fontsize=14, color='white')  # Etiqueta del eje Y
        ax.set_title("Conteo Indice de Masa Corporal", fontsize=20, color='white')  # Título del gráfico
        ax.tick_params(axis='both', which='major', labelsize=12, labelcolor='white')
        ax.grid(True, which='both', axis='both', color='white', linestyle='--', linewidth=0.5)
        st.pyplot(fig)
    elif chart_type == "Linea":
        fig, ax = plt.subplots(figsize=(10, 5))
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')
        sns.lineplot(
            data=filtered_df, x="Age", y="Calories_Burned", ax=ax, color="lightgreen", hue="Gender"
        )
        ax.set_xlabel("Tipo de entrenamiento", fontsize=14, color='white')  # Etiqueta del eje X
        ax.set_ylabel("Calorias quemadas", fontsize=14, color='white')  # Etiqueta del eje Y
        ax.set_title("Promedio Calorias quemadas por Edad", fontsize=20, color='white')  # Título del gráfico
        ax.tick_params(axis='both', which='major', labelsize=12, labelcolor='white')
        ax.grid(True, which='both', axis='both', color='white', linestyle='--', linewidth=0.5)
        st.pyplot(fig)