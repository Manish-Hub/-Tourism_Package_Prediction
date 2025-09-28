import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("models/xgboost_final_model.joblib")

st.title("Tourism Package Predictor")

# Sidebar inputs
age = st.slider("Age", 18, 70, 30)
income = st.number_input("Income", min_value=10000, max_value=1000000, value=500000)
gender = st.selectbox("Gender", ["Male", "Female"])

# Prepare input
input_df = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Gender": [gender]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Package Interest: {prediction[0]}")
