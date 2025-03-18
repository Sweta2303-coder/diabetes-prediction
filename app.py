import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Model Load Karo
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title of the app
st.title("🩺 Diabetes Prediction App")
st.write("Patient details daalo aur jaaniye diabetes ka risk!")

# Input fields for user
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=80)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=10, max_value=100, value=30)

# Prediction Function
def predict_diabetes():
    # Input ko array mein convert karo
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    # Result Show karo
    if prediction[0] == 1:
        st.error("❌ High Risk: Patient ko diabetes ho sakta hai.")
    else:
        st.success("✅ Low Risk: Patient ko diabetes nahi hai.")

# Predict Button
if st.button("Predict"):
    predict_diabetes()

# Footer
st.markdown("---")
