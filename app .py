import streamlit as st
import pandas as pd
import joblib

# Load dataset to get dropdown options
df = pd.read_csv("amazon_delivery.csv")
traffic_options = df['Traffic'].dropna().unique().tolist()
weather_options = df['Weather'].dropna().unique().tolist()
vehicle_options = df['Vehicle'].dropna().unique().tolist()

# Load trained model
model_pipeline = joblib.load("delivery_time_predictor.pkl")

# App title
st.title("🚚 Delivery Time Prediction App")
st.markdown("Predict delivery time based on traffic, weather, package weight, and more.")

# Sidebar inputs
st.sidebar.header("📦 Input Features")

traffic = st.sidebar.selectbox("Traffic", traffic_options)
weather = st.sidebar.selectbox("Weather", weather_options)
vehicle = st.sidebar.selectbox("Vehicle", vehicle_options)
time_to_pickup = st.sidebar.number_input("Time to Pickup (minutes)", 1, 120, 20)
distance_km = st.sidebar.number_input("Distance (km)", 0.5, 100.0, 5.0)
package_weight_kg = st.sidebar.number_input("Package Weight (kg)", 0.1, 30.0, 1.0)
hour_of_day = st.sidebar.slider("Hour of Day", 0, 23, 12)
day_of_week = st.sidebar.slider("Day of Week (1=Mon, 7=Sun)", 1, 7, 5)
is_weekend = st.sidebar.checkbox("Is Weekend", value=False)

# Input dataframe
input_df = pd.DataFrame({
    'Traffic': [traffic],
    'Weather': [weather],
    'Vehicle': [vehicle],
    'Time_To_Pickup': [time_to_pickup],
    'Distance_km': [distance_km],
    'Package_Weight_kg': [package_weight_kg],
    'Hour_of_Day': [hour_of_day],
    'Day_of_Week': [day_of_week],
    'Is_Weekend': [is_weekend]
})

st.subheader("📋 Input Data")
st.write(input_df)

# Prediction
if st.button("Predict Delivery Time"):
    prediction = model_pipeline.predict(input_df)
    st.subheader("🕒 Predicted Delivery Time")
    st.success(f"{prediction[0]:.2f} minutes")
