import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("models/xgboost_final_model.joblib")

# Title
st.title("🧭 Tourism Package Prediction")

# Input form
st.sidebar.header("User Features")
age = st.sidebar.slider("Age", 18, 70, 30)
income = st.sidebar.number_input("Annual Income (₹)", 100000, 1000000, 500000)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
# Add more features as needed...

# Prepare input
input_df = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Gender": [gender]
    # Add more features here...
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Package Interest: {prediction}")
