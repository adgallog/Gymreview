import streamlit as st

def display_general_info(data):
    st.header("Información General")
    st.write("Este tablero proporciona un análisis exploratorio y permite hacer predicciones de supervivencia en el Titanic.")
    # Subir archivo
    st.sidebar.title("MENU")

    # Mostrar los datos
    st.header("📊 Dataset:")
    show_data = st.checkbox("Mostrar Dataframe")
    if show_data:
        st.dataframe(data)

    st.write("----")

    # Mostrar estadísticas descriptivas
    st.header("📈 Estadísticas descriptivas:")
    st.write(data.describe())
