# ETA-Predictor 🕒🚚

A machine learning web application that predicts **Estimated Time of Arrival (ETA)** for package deliveries using real-world logistics data. This project uses a trained regression model and a Streamlit-based web app to make interactive predictions.

---

## 🚀 Project Overview

- **Goal:** Predict delivery time (in minutes) based on features like traffic, weather, distance, and package weight.
- **Interface:** Interactive web UI built with Streamlit.
- **Model:** Trained using scikit-learn pipelines and joblib serialization.
- **Dataset:** Custom delivery dataset (`amazon_delivery.csv`) containing relevant delivery features.

---

## 📂 Project Structure

```
final_amazon_delivery/
│
├── amazon_delivery.csv # Raw dataset
├── delivery_time_predictor.pkl # Trained ML model (joblib)
├── app.py # Streamlit web application
├── Delivery_Time_Prediction.ipynb # EDA and model training notebook
└── README.md # Project documentation
```
---

## 🧠 Features Used

- Traffic condition
- Weather condition
- Type of delivery vehicle
- Distance to be covered (in km)
- Package weight (in kg)
- Time to pickup (in minutes)
- Hour of day
- Day of week
- Weekend indicator

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** pandas, numpy, scikit-learn, streamlit, joblib
- **Model:** Regression (Pipeline-based using scikit-learn)
- **Web Framework:** Streamlit
- **Deployment:** Localhost or deployable via platforms like Streamlit Cloud or Render

---

## 📊 Example Usage

Launch the app and fill out:

- Traffic: `High`
- Weather: `Rainy`
- Vehicle: `Bike`
- Time to Pickup: `15` minutes
- Distance: `5.0` km
- Package Weight: `2.0` kg
- Hour of Day: `14`
- Day of Week: `3` (Wednesday)
- Is Weekend: `False`

Click **Predict Delivery Time** → You'll get an ETA like **28.34 minutes**.

---
