"""
=========================================================
Utility Functions
Used Car Price Prediction System
=========================================================
"""

from pathlib import Path
from datetime import datetime
import joblib
import pandas as pd
import streamlit as st
from config import (
    DATA_PATH,
    MODEL_PATH,
    PREPROCESSOR_PATH
)

# =========================================================
# Load Dataset
# =========================================================
@st.cache_data(show_spinner=False)
def load_dataset():
    """
    Load processed dataset.
    """
    return pd.read_csv(DATA_PATH)


# =========================================================
# Load Machine Learning Model
# =========================================================
@st.cache_resource(show_spinner=False)
def load_model():
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    return model, preprocessor


# =========================================================
# Currency Formatter
# =========================================================
def currency(value):
    if pd.isna(value):
        return "-"
    return f"${value:,.2f}"


# =========================================================
# Percentage Formatter
# =========================================================
def percentage(value):
    return f"{value * 100:.2f}%"


# =========================================================
# Number Formatter
# =========================================================
def number(value):
    return f"{value:,}"


# =========================================================
# Current Time
# =========================================================
def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# =========================================================
# Save Prediction History
# =========================================================
def save_prediction(vehicle, prediction):
    if "prediction_history" not in st.session_state:
        st.session_state.prediction_history = []
    st.session_state.prediction_history.append({
        "Time": current_time(),
        **vehicle,
        "Predicted Price": prediction})


# =========================================================
# Load Prediction History
# =========================================================
def get_prediction_history():
    if "prediction_history" not in st.session_state:
        st.session_state.prediction_history = []
    return pd.DataFrame(st.session_state.prediction_history)


# =========================================================
# Reset Prediction History
# =========================================================
def clear_prediction_history():
    st.session_state.prediction_history = []


# =========================================================
# Download DataFrame
# =========================================================
def dataframe_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


# =========================================================
# Show Success Message
# =========================================================
def success(message):
    st.success(f"✅ {message}")


# =========================================================
# Show Error Message
# =========================================================
def error(message):
    st.error(f"❌ {message}")


# =========================================================
# Show Warning
# =========================================================
def warning(message):
    st.warning(f"⚠️ {message}")


# =========================================================
# Divider
# =========================================================
def divider():
    st.markdown("---")