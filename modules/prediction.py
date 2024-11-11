import streamlit as st
import pandas as pd

def predict_gender(model):
    st.header("Predicción de Género")
    
    # Input del usuario
    st.subheader("Introduce los datos de la persona para predecir si es hombre o mujer")
    age = st.slider("Edad", 18, 59, 30)
    weight = st.slider("Peso en 'Kg'", 0, 150, 70)
    height = st.slider("ALtura en 'm'", 1.5, 2.5, 1.7)
    Max_BPM = st.slider("BPM maximo", 160, 199, 180)
    Avg_BPM = st.slider("BPM promedio", 120, 169, 143)
    Resting_BPM = st.slider("BMP en descanso", 50, 74, 62)
    Session_Duration = st.slider("Duracion del entrenamiento", 0.5, 2.0, 1.2)
    Calories_Burned = st.slider("Calorias quemadas", 300, 1800, 900)
    Workout_Type = st.selectbox("Tipo de Ejercicio", ["Cardio", "HIIT", "Fuerza", "Yoga"])
    Fat_Percentage = st.slider("Porcentaje de grasa", 10.0, 35.0, 25.0)
    Water_Intake  = st.slider("Injesta de agua", 1.5, 3.7, 2.6)
    Workout_Frequency = st.selectbox("frecuencia de entrenamiento semanal", ["2", "3", "4", "5"])
    Experience_Level = st.selectbox("Nivel de Experiencia", ["Novato", "Intermedio", "Experto"])
    bmi = st.slider("Indice de masa corporal", 12.0, 50.0, 24.9)
   

    # Preparar los datos de entrada para el modelo
    input_data = pd.DataFrame({
        'Age': [age],
        'Weight (kg)': [weight],
        'Height (m)': [height],
        'Max_BPM': [Max_BPM],
        'Avg_BPM': [Avg_BPM],
        'Resting_BPM': [Resting_BPM],
        'Session_Duration (hours)': [Session_Duration],
        'Calories_Burned': [Calories_Burned],
        'Workout_Type': [0 if Workout_Type == "Cardio" else 1 if Workout_Type == "HIIT" else 2 if Workout_Type == "Fuerza" else 3],
        'Fat_Percentage': [Fat_Percentage],
        'Water_Intake (liters)': [Water_Intake],
        'Workout_Frequency (days/week)': [Workout_Frequency],
        'Experience_Level': [1 if Experience_Level == "Novato" else 2 if Experience_Level == "Intermedio" else 3],
        'BMI': [bmi]
    })

    # Predicción
    if st.button("Hacer Predicción"):
        prediction = model.predict(input_data)[0]
        resultado = "Masculino" if prediction == 1 else "Femenino"
        st.write(f"Los datos ingresados pertenecen a una persona del Genero: **{resultado}**")
