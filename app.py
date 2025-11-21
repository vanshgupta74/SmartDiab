import streamlit as st
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺")

st.title("🩺 SmartDiab")
st.write("Enter your medical details to check diabetes risk")

# Input fields
preg = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose Level", 0, 300, 120)
bp = st.number_input("Blood Pressure", 0, 200, 80)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin Level", 0, 900, 85)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 0, 120, 30)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High chance of Diabetes")
    else:
        st.success("✅ No Diabetes Risk")
