import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Housing Price Predictor", page_icon="🏡")
st.title("🏠 Housing Price Predictor")
st.markdown("Use the sliders to input features and predict house prices.")

col1, col2 = st.columns(2)

# inputs
with col1:
    MedInc = st.slider("Median Income (10k USD)", 0.0, 20.0, 3.0)
    HouseAge = st.slider("House Age", 1, 50, 20)
    AveRooms = st.slider("Average Rooms", 1.0, 10.0, 5.0)
    AveBedrms = st.slider("Average Bedrooms", 0.5, 5.0, 1.0)

with col2:
    Population = st.slider("Population", 1, 5000, 1000)
    AveOccup = st.slider("Average Occupants", 1.0, 10.0, 3.0)
    Latitude = st.slider("Latitude", 32.0, 42.0, 34.0)
    Longitude = st.slider("Longitude", -125.0, -114.0, -120.0)

# Create input DataFrame
input_data = pd.DataFrame({
    'MedInc': [MedInc],
    'HouseAge': [HouseAge],
    'AveRooms': [AveRooms],
    'AveBedrms': [AveBedrms],
    'Population': [Population],
    'AveOccup': [AveOccup],
    'Latitude': [Latitude],
    'Longitude': [Longitude]
})

# Predict
if st.button("🔍 Predict Housing Price"):
    prediction = model.predict(input_data)
    st.markdown(
        f"""
        <div style="background-color:#e6f4ea;padding:20px;border-radius:10px">
            <h3 style='color:#2e7d32;'>💵 Predicted Median House Value:</h3>
            <h1 style='color:#1b5e20;'>${prediction[0]*100000:.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("Made with ❤️ by archie and arya")
