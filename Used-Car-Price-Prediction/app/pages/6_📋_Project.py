import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Project Details",
    page_icon="📋",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📋 Used Car Price Prediction Project")

st.markdown("""
Welcome to the **Used Car Price Prediction System**.

This project was developed as part of the **Intelligent AI and Data Engineering** course.
It demonstrates the complete Machine Learning workflow from data preprocessing to model deployment.
""")

st.divider()

# ---------------------------------------------------
# Business Problem
# ---------------------------------------------------

st.header("🎯 Business Problem")

st.write("""
Pricing used cars accurately is a challenge because many factors influence the selling price, including:

- Vehicle age
- Mileage
- Fuel type
- Transmission
- Brand
- Engine size
- Ownership history

Incorrect pricing can lead to financial losses for buyers and sellers.

Machine Learning helps estimate fair market prices using historical vehicle data.
""")

st.divider()

# ---------------------------------------------------
# Project Objectives
# ---------------------------------------------------

st.header("🎯 Project Objectives")

st.markdown("""
### General Objective

Develop an intelligent Machine Learning model capable of predicting the selling price of used cars.

### Specific Objectives

- Understand the dataset
- Perform data preprocessing
- Conduct Exploratory Data Analysis (EDA)
- Train multiple regression models
- Compare model performance
- Tune the best-performing model
- Build a Streamlit web application
""")

st.divider()

# ---------------------------------------------------
# Machine Learning Workflow
# ---------------------------------------------------

st.header("⚙ Machine Learning Workflow")

st.markdown("""
1. 📂 Dataset Collection

⬇

2. 🧹 Data Cleaning

⬇

3. 📊 Exploratory Data Analysis

⬇

4. ⚙ Feature Engineering

⬇

5. 🤖 Model Training

⬇

6. 🎯 Hyperparameter Tuning

⬇

7. 📈 Model Evaluation

⬇

8. 🚗 Prediction Application
""")

st.divider()

# ---------------------------------------------------
# Regression Models
# ---------------------------------------------------

st.header("🤖 Regression Models Used")

models = [
    "Linear Regression",
    "Ridge Regression",
    "Lasso Regression",
    "Decision Tree Regressor",
    "Random Forest Regressor",
    "Gradient Boosting Regressor",
    "Support Vector Regressor",
    "Extra Trees Regressor",
    "AdaBoost Regressor"
]

for model in models:
    st.markdown(f"✅ {model}")

st.divider()

# ---------------------------------------------------
# Evaluation Metrics
# ---------------------------------------------------

st.header("📈 Evaluation Metrics")

col1, col2 = st.columns(2)

with col1:
    st.info("""
**MAE**

Mean Absolute Error

Measures the average prediction error.
""")

    st.info("""
**RMSE**

Root Mean Squared Error

Penalizes large prediction errors.
""")

with col2:
    st.info("""
**MSE**

Mean Squared Error

Average squared prediction error.
""")

    st.info("""
**R² Score**

Measures how well the model explains the variance in the data.
""")

st.divider()

# ---------------------------------------------------
# Technologies
# ---------------------------------------------------

st.header("🛠 Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("Language", "Python")
tech2.metric("Framework", "Streamlit")
tech3.metric("ML Library", "Scikit-Learn")
tech4.metric("Visualization", "Matplotlib & Plotly")

st.divider()

# ---------------------------------------------------
# Project Structure
# ---------------------------------------------------

st.header("📁 Project Structure")

st.code("""
USED_CAR_PRICE_PREDICTION/

├── app/
│   ├── pages/
│   ├── assets/
│   ├── components/
│   └── app.py
│
├── data/
├── models/
├── notebooks/
├── outputs/
├── report/
├── presentation/
├── requirements.txt
└── README.md
""")

st.divider()

# ---------------------------------------------------
# Expected Outcome
# ---------------------------------------------------

st.header("🏆 Expected Outcome")

st.success("""
✔ Accurate used car price prediction

✔ Comparison of multiple regression algorithms

✔ Interactive Streamlit web application

✔ Professional AI project suitable for academic submission
""")

st.divider()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown(
"""
<div style='text-align:center;color:gray;'>

Developed for the course

<b>Intelligent AI and Data Engineering</b>

Addis Ababa University • Group 6 • 2026

</div>
""",
unsafe_allow_html=True
)