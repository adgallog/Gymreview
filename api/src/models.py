import joblib

model = joblib.load("../../models/gym_model.joblib")

class Article(BaseModel):
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