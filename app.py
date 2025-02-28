import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model,scaler = joblib.load("medical_insurance_predictor.pkl")

# Define mappings
gender_mapping = {'Male': 1, 'Female': 0}
smoker_mapping = {'Yes': 1, 'No': 0}
region_mapping = {'Southwest': 0, 'Southeast': 1, 'Northwest': 2, 'Northeast': 3}

# Features
feature_names = ['age', 'sex', 'bmi', 'children', 'smoker','region']

# Streamlit UI
st.title("Medical Insurance Predictor")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)
sex = st.selectbox("Sex", list(gender_mapping.keys()))
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
children = st.number_input("Number of Children", min_value=0,value=0)
smoker = st.selectbox("Smoker", list(smoker_mapping.keys()))
region = st.selectbox("Region", list(region_mapping.keys()))

# Predict button
if st.button("Predict Cost"):
    try:
        # Encode categorical inputs
        sex_encoded = gender_mapping[sex]
        smoker_encoded = smoker_mapping[smoker]
        region_encoded = region_mapping[region]

        # Prepare input features
        input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])

        # Convert input to DataFrame 
        input_df = pd.DataFrame(input_data, columns=feature_names)

        # Feature Scaling
        input_data_scaled = scaler.transform(input_df)  

        # Make prediction
        predicted_cost = model.predict(input_data_scaled)

        st.success(f"Expected Insurance Cost: ${predicted_cost[0]:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
