import streamlit as st
import numpy as np
import pandas as pd

# Function to predict the insurance cost (placeholder for actual model)
def predict_insurance_cost(features):
    # Placeholder logic, replace with your actual prediction model
    cost = 5000 + np.sum(np.random.randn(len(features)))
    return cost

# Streamlit app
st.title("Health Insurance Cost Predictor")

# Input for Numeric Features
age = st.number_input("Age", min_value=0, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
annual_income = st.number_input("Annual Income (in Lakhs)", min_value=0.0, max_value=100.0, value=5.0)

# Input for Categorical Features using dropdowns
gender = st.selectbox("Gender", ['Male', 'Female'])
region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional', 'Smoking=0', 'Does Not Smoke', 'Not Smoking'])
employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])
income_level = st.selectbox("Income Level", ['<10L', '10L - 25L', '> 40L', '25L - 40L'])
medical_history = st.selectbox("Medical History", ['Diabetes', 'High blood pressure', 'No Disease',
                                                  'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
                                                  'High blood pressure & Heart disease', 'Diabetes & Thyroid',
                                                  'Diabetes & Heart disease'])
insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

# When the Predict button is clicked
if st.button("Predict"):
    # Gather input features into a dictionary or array (can match your model's expected input)
    features = {
        'age': age,
        'bmi': bmi,
        'annual_income': annual_income,
        'gender': gender,
        'region': region,
        'marital_status': marital_status,
        'bmi_category': bmi_category,
        'smoking_status': smoking_status,
        'employment_status': employment_status,
        'income_level': income_level,
        'medical_history': medical_history,
        'insurance_plan': insurance_plan
    }

    # Placeholder for prediction logic
    predicted_cost = predict_insurance_cost(features)

    # Display the predicted cost
    st.success(f"Predicted Health Insurance Cost: ₹ {predicted_cost:.2f}")
