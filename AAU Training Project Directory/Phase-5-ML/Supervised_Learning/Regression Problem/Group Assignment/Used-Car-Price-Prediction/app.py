# ==========================================================
# SMART CAR PRICE PREDICTION SYSTEM
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="Car Price Prediction AI",
    page_icon="🚗",
    layout="wide"
)
# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown(
"""
<style>
/* Main Background */
.stApp{
background:
linear-gradient(
135deg,
#020617,
#0f172a,
#172554
);
}
/* Title */
h1{
color:white;
font-size:45px;
font-weight:800;
text-align:center;
}
h2,h3{
color:#e2e8f0;
text-align:center;
}

/* Normal text */
p{
color:#cbd5e1;
}
/* Input Labels */
label{
color:#e2e8f0 !important;
font-size:17px !important;
font-weight:600 !important;
}
/* Input boxes */
.stNumberInput input,
.stTextInput input,
.stSelectbox div[data-baseweb="select"]{
background:#111827 !important;
color:white !important;
border:1px solid #334155 !important;
border-radius:12px !important;
height:50px;
}
/* Dropdown text */
.stSelectbox span{
color:white !important;
}
/* Input hover */
.stNumberInput input:hover,
.stSelectbox div[data-baseweb="select"]:hover{
border:2px solid #2563eb !important;
}
/* General Card */
.card{
padding:30px;
border-radius:20px;
background:#0f172a;
border:2px solid #2563eb;
box-shadow:
0 0 30px rgba(37,99,235,0.5);
text-align:center;
}
.card h2{
color:#60a5fa;
}
.card h1{
color:white;
font-size:50px;
}
/* Interior Card */
.interior-card{
padding:20px;
border-radius:18px;
background:
linear-gradient(
135deg,
#111827,
#1e1b4b
);
border:2px solid #ec4899;
}
/* Clean Title Card */
.clean-card{
padding:20px;
border-radius:18px;
background:
linear-gradient(
135deg,
#052e16,
#064e3b
);
border:2px solid #22c55e;
}
/* Button */
.stButton button{
width:100%;
height:60px;
border-radius:15px;
background:
linear-gradient(
90deg,
#2563eb,
#4f46e5
);
color:white;
font-size:20px;
font-weight:700;
border:none;
}
.stButton button:hover{
background:
linear-gradient(
90deg,
#1d4ed8,
#4338ca
);}
/* Divider */
hr{
border-color:#334155;
}
</style>
""",
unsafe_allow_html=True
)
# ==========================================================
# LOAD MODEL FILES
# ==========================================================
@st.cache_resource
def load_components():
    model = joblib.load("models/car_price_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    encoders = joblib.load("models/label_encoders.pkl")
    with open(
        "models/features.json"
    ) as f:
        features=json.load(f)
    return model,scaler,encoders,features
model,scaler,encoders,features = load_components()
# ==========================================================
# HEADER
# ==========================================================
st.title("🚗 AI Car Price Prediction System")
st.write(
"""
Machine Learning powered vehicle price estimation system.
This application uses an optimized Random Forest Regression model.
""")
st.divider()
# ==========================================================
# USER INPUT SECTION
# ==========================================================
st.subheader("🚘 Enter Vehicle Information")
col1,col2,col3 = st.columns(3)
# ================= COLUMN 1 =================
with col1:
    model_year = st.number_input(
        "📅 Model Year",
        min_value=1990,
        max_value=2026,
        value=2020 )
    engine = st.number_input(
        "⚙️ Engine Size (Liters)",
        min_value=1.0,
        max_value=8.0,
        value=2.5,
        step=0.1)
    milage = st.number_input(
        "🚘 Mileage",
        min_value=0,
        value=50000)
# ================= COLUMN 2 =================
with col2:
    accident = st.selectbox(
        "🛡️ Accident History",
        [0,1])
    transmission = st.selectbox(
        "⚙️ Transmission",
        encoders["transmission"].classes_)
    fuel_type = st.selectbox(
        "⛽ Fuel Type",
        encoders["fuel_type"].classes_)
# ================= COLUMN 3 =================
with col3:
    brand = st.selectbox(
        "🏷️ Brand",
        encoders["brand"].classes_)
    model_name = st.selectbox(
        "🚗 Car Model",
        encoders["model"].classes_)
    ext_col = st.selectbox(
        "🎨 Exterior Color",
        encoders["ext_col"].classes_)
# ==========================================================
# SPECIAL CARDS
# ==========================================================
st.divider()
col4,col5 = st.columns(2)
with col4:
    st.markdown(
    """
    <div class="interior-card">
    """,unsafe_allow_html=True)
    int_col = st.selectbox(
        "🎨 Interior Color",
        encoders["int_col"].classes_)
    st.write("Select the primary interior color of the vehicle.")
    st.markdown("</div>",unsafe_allow_html=True)
with col5:
    st.markdown(
    """
    <div class="clean-card">
    """, unsafe_allow_html=True )
    clean_title = st.selectbox("📄 Clean Title",["Yes","No"])
    st.write("A clean title means no major ownership issues.")
    st.markdown("</div>",unsafe_allow_html=True)
# ==========================================================
# PREDICTION
# ==========================================================
st.divider()
if st.button("🚀 Predict Car Price"):
    input_data = {
        "brand":brand,
        "model":model_name,
        "model_year":model_year,
        "milage":milage,
        "fuel_type":fuel_type,
        "engine":engine,
        "transmission":transmission,
        "ext_col":ext_col,
        "int_col":int_col,
        "accident":accident}
    input_df=pd.DataFrame(
        [input_data]
    )
    # Encode categorical values
    for col,encoder in encoders.items():
        if col in input_df.columns:
            input_df[col]=encoder.transform(
                input_df[col].astype(str))
    # Arrange features exactly like training
    input_df=input_df[
        features["features"]]
    # Scaling
    input_scaled=scaler.transform(
        input_df)
    # Prediction
    prediction=model.predict(
        input_scaled)[0]
    st.success("Prediction Completed Successfully!" )
    st.markdown(
    f"""
    <div class="card">
    <h2>Estimated Car Price</h2>
    <h1>${prediction:,.0f}</h1>
    </div>
    """,unsafe_allow_html=True)
    if prediction < 10000:
        st.info("💰 Budget Vehicle Category")
    elif prediction < 30000:
        st.info("🚘 Mid-range Vehicle Category")
    else:
        st.info("🏎️ Premium Vehicle Category")
# ==========================================================
# FOOTER
# ==========================================================
from datetime import datetime

st.divider()
st.caption(
    f"© {datetime.now().year} Nigus Admas. All Rights Reserved. | 🚗 Car Price Prediction  | Powered by Machine Learning"
)