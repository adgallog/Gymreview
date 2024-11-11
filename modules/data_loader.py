import pandas as pd
import joblib
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("data/gym.csv")

@st.cache_data
def load_model():
    return joblib.load("models/gym_model.joblib")