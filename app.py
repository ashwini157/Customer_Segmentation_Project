import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page Configruation
st.set_page_config(page_title="Customer Spending Predictor", layout="centered")

#Load Model
@st.cache_resource
def load_model():
    return joblib.load('rf_direct_model.joblib')

try:
    model = load_model()
except:
    st.error("Pehle Step 1 wala script run karke 'rf_direct_model.joblib' banayein.")

# Make UI
st.title("🛍️ Customer Spending Predictor")
st.write("Random Forest Model ka use karke Spending Score predict karein.")

# Inputs Of Slidebars
st.sidebar.header("Customer Details")
age = st.sidebar.slider("Age", 18, 100, 30)
income = st.sidebar.number_input("Annual Income (k$)", 10, 200, 50)
freq = st.sidebar.number_input("Purchase Frequency", 1, 20, 5)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

# Prediction Logic
if st.button("Predict Spending Score"):
    gender_val = 1 if gender == "Male" else 0
    input_df = pd.DataFrame([[age, income, freq, gender_val]], 
                            columns=["Age", "Annual_Income_k$", "Purchase_Frequency", "Gender"])
    
    # Prediction
    prediction = model.predict(input_df)[0]
    
    # Results Show
    st.subheader("Results")
    st.metric("Predicted Spending Score", f"{prediction:.2f}")
    
    # To feedback
    if prediction > 70:
        st.success("High Spender Customer! 🌟")
    elif prediction > 40:
        st.info("Average Spender Customer. 👍")
    else:
        st.warning("Low Spender Customer. 📉")

# Data Preview (To Click Show Data And Data Show)
#if st.checkbox("Show Training Data Sample"):
#    df_show = pd.read_csv("customer_segmentation_uncleaned_data.csv")
#    st.write(df_show.head())