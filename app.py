import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("notebooks/datos/gym.csv")


# Título de la aplicación
st.title('Análisis personas Ejercitandose')
# Mostrar los datos
st.write('Datos de analisados:')
st.dataframe(df)

# Mostrar estadísticas descriptivas
st.write('Estadísticas descriptivas:')
st.write(df.describe())

# Gráfico de dispersión
st.write('Gráfico de dispersión entre total_bill y tip:')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='Age', y='Fat_Percentage', ax=ax)
st.pyplot(fig)


### Gráfico de Barras
st.write('Gráfico de barras del total de cuentas por día:')
fig, ax = plt.subplots()
sns.barplot(data=df, x='Gender', y='Age', ax=ax)
st.pyplot(fig)

# Filtrar datos por día
Gender = st.selectbox('Selecciona un día:', df['Gender'].unique())
filtered_df = df[df['Gender'] == Gender]
st.write(f'Datos filtrados por {Gender}:')
st.dataframe(filtered_df)

