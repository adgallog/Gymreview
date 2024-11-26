from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List


with open("../models/gym_model.joblib", "rb") as f:
    model = joblib.load(f)

app = FastAPI()


class ModelingData(BaseModel):
    age : int
    weight : int
    height : float
    Max_BPM : int
    Avg_BPM : int
    Resting_BPM : int
    Session_Duration : float
    Calories_Burned : int
    Workout_Type : str
    Fat_Percentage : float
    Water_Intake  : float
    Workout_Frequency : int
    Experience_Level : str
    bmi : float
    def as_dataframe(self):
        return pd.DataFrame({
        'Age': [self.age],
        'Weight (kg)': [self.weight],
        'Height (m)': [self.height],
        'Max_BPM': [self.Max_BPM],
        'Avg_BPM': [self.Avg_BPM],
        'Resting_BPM': [self.Resting_BPM],
        'Session_Duration (hours)': [self.Session_Duration],
        'Calories_Burned': [self.Calories_Burned],
        'Workout_Type': [0 if self.Workout_Type == "Cardio" 
                         else 1 if self.Workout_Type == "HIIT" 
                         else 2 if self.Workout_Type == "Fuerza" 
                         else 3],
        'Fat_Percentage': [self.Fat_Percentage],
        'Water_Intake (liters)': [self.Water_Intake],
        'Workout_Frequency (days/week)': [self.Workout_Frequency],
        'Experience_Level': [1 if self.Experience_Level == "Novato" 
                             else 2 if self.Experience_Level == "Intermedio" 
                             else 3],
        'BMI': [self.bmi]
        })
        

@app.post("/predict_gender/")
async def predict_gender(data: ModelingData):
    df = data.as_dataframe()
    prediction = model.predict(df)[0]
    resultado = "Masculino" if prediction == 1 else "Femenino"

    return {"prediction": resultado}