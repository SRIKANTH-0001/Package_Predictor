#import necessary packages
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("placement-dataset.csv")
X = data[["cgpa"]]
y = data["package"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.set_page_config(page_title="📊 Package Predictor", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎓 CGPA to LPA Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>Enter your CGPA and get an estimated package!</h3>", unsafe_allow_html=True)

# Input box for CGPA
cgpa = st.number_input("📌 Enter your CGPA:", min_value=0.0, max_value=10.0, step=0.01, format="%.2f")

# Predict Button
if st.button("🚀 Predict LPA"):
    predicted_lpa = model.predict([[cgpa]])[0]
    st.success(f"💰 Estimated LPA: **{predicted_lpa:.2f} LPA** 🎯")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Built by SRIKANTH❤️ using Streamlit</p>", unsafe_allow_html=True)
