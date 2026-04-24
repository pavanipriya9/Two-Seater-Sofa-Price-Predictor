%%writefile app.py
import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("sofa_price_model.pkl")
features = joblib.load("features.pkl")

st.title("🛋 Sofa Price Prediction")

st.write("Enter sofa details:")

# Inputs
rating = st.number_input("Rating", 0.0, 5.0, 4.0)
reviews = st.number_input("Reviews", 0, 1000, 100)
seating_height = st.number_input("Seating Height", 0.0, 50.0, 18.0)
warranty = st.number_input("Warranty (Months)", 0, 60, 12)
weight = st.number_input("Weight (KG)", 0.0, 100.0, 30.0)
discount = st.number_input("Discount (%)", 0.0, 100.0, 20.0)

material = st.text_input("Material (Wood/Fabric/Leather)")
color = st.text_input("Color (Brown/Grey/Black)")
size = st.text_input("Size (2-Seater/3-Seater)")

# Predict
if st.button("Predict Price"):

    data = {
        "Rating": rating,
        "Reviews": reviews,
        "Seating Height": seating_height,
        "Warranty (Months)": warranty,
        "Weight (KG)": weight,
        "Discount (%)": discount,
        "Material": material,
        "Color": color,
        "Size": size
    }

    df = pd.DataFrame([data])

    df = pd.get_dummies(df)
    df = df.reindex(columns=features, fill_value=0)

    prediction = model.predict(df)[0]

    st.success(f"💰 Predicted Price: ₹{round(prediction, 2)}")
