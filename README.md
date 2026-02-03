# Customer Segmentation Project
Customer Spending Prediction System

A complete end-to-end Machine Learning project that predicts Customer Spending Score using data preprocessing, exploratory data analysis, Random Forest modeling, and a Streamlit web application.

Project Overview

This project helps businesses understand and predict how much a customer is likely to spend based on:

Age
Annual Income
Purchase Frequency
Gender


The trained ML model is deployed using Streamlit for real-time predictions.

Enter Customer Details

Use the sidebar sliders to input:
Age
Income
Purchase Frequency
Gender

Click Predict Spending Score

Model Output

The app classifies customers as:
🌟 High Spender
👍 Average Spender
📉 Low Spender

With predicted numerical score.

Data Processing Highlights

✔ Missing value analysis
✔ Mean vs Median imputation comparison
✔ Z-score & IQR based outlier handling
✔ Clean train-test transformations

(All implemented in useful_func.py)

How to Run the Project : 
Install dependencies :
pip install pandas numpy scikit-learn streamlit joblib

Run Streamlit App : 
streamlit run app.py
