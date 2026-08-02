import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
from pathlib import Path
from datetime import datetime
# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ----------------------------
# Load CSS
# ----------------------------
css_file = Path("app/assets/css/style.css")
if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True)
# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "models" / "trained_models" / "random_forest.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessing" / "preprocessor.pkl"
DATA_PATH = BASE_DIR / "data" / "processed" / "used_cars_clean.csv"
# ----------------------------
# Load Dataset
# ----------------------------
@st.cache_data
def load_dataset():
    return pd.read_csv(DATA_PATH)
df = load_dataset()
# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    return model, preprocessor
model, preprocessor = load_model()
# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.image("app/assets/images/logo.png",width=120)
    st.title("🚗 Used Car Price")
    st.success("Prediction System")
    st.markdown("---")
    st.info("""
Predict the selling price of a used vehicle using our trained Machine Learning model.
""")
    st.markdown("---")
    st.metric("Dataset",f"{len(df):,} Cars")
    st.metric("Best Model","Random Forest")
    st.metric("Version","1.0")
# ----------------------------
# Title
# ----------------------------
st.markdown(
"""
<h1 style='color:#2563EB;'>
🚗 Used Car Price Prediction
</h1>
""",unsafe_allow_html=True)
st.caption("Fill in the vehicle details and click Predict.")
st.divider()

###############################################
# vehicle information
###############################################
left,right=st.columns([2,1])
with left:
    st.subheader("🚘 Vehicle Information")
    brand=st.selectbox(
        "Brand",sorted(df["brand"].dropna().unique()))
    model_name=st.selectbox("Model",sorted(
            df[df["brand"]==brand]["model"].unique()))
    year=st.number_input("Model Year",1990,2026,2020)
    mileage=st.number_input("Mileage",0,500000,50000)
    fuel=st.selectbox("Fuel Type",
        sorted(df["fuel_type"].dropna().unique()))
    transmission=st.selectbox(
        "Transmission",
        sorted(df["transmission"].dropna().unique()))
with right:
    st.subheader("🎨 Vehicle Details")
    engine=st.selectbox("Engine",
        sorted(df["engine"].dropna().unique()))
    ext=st.selectbox(
        "Exterior Color",
        sorted(df["ext_col"].dropna().unique()))
    interior=st.selectbox(
        "Interior Color",
        sorted(df["int_col"].dropna().unique()))
    accident=st.selectbox(
        "Accident",
        sorted(df["accident"].dropna().unique()))
    clean_title=st.selectbox(
        "Clean Title",
        sorted(df["clean_title"].dropna().unique()))


# ==========================================
# Prediction Button
# ==========================================
st.divider()
prediction = None 
predict = st.button(
    "🚀 Predict Selling Price",
    use_container_width=True,
    type="primary")
if predict:
    try:
        with st.spinner("Predicting selling price..."):
            time.sleep(1)
            # ------------------------------
            # Create Input DataFrame
            # ------------------------------
            input_data = pd.DataFrame({
                "brand":[brand],
                "model":[model_name],
                "model_year":[year],
                "milage":[mileage],
                "fuel_type":[fuel],
                "engine":[engine],
                "transmission":[transmission],
                "ext_col":[ext],
                "int_col":[interior],
                "accident":[accident],
                "clean_title":[clean_title]})

            current_year = datetime.now().year

            # Vehicle age
            input_data["vehicle_age"] = current_year - input_data["model_year"]
            
            # Car age
            input_data["car_age"] = input_data["vehicle_age"]
            
            # Mileage per year
            input_data["milage_per_year"] = (
                input_data["milage"] /
                input_data["vehicle_age"].clip(lower=1)
            )
            
            # Luxury brand
            luxury_brands = [
                "BMW",
                "Mercedes-Benz",
                "Audi",
                "Lexus",
                "Porsche",
                "Jaguar",
                "Land Rover",
                "Tesla",
                "Volvo"
            ]
            
            input_data["luxury_brand"] = (
                input_data["brand"]
                .isin(luxury_brands)
                .astype(int)
            )
            # ------------------------------
            # Preprocess
            # ------------------------------
            transformed = preprocessor.transform(input_data)
            # ------------------------------
            # Predict
            # ------------------------------
            prediction = model.predict(transformed)[0]
            prediction = round(prediction,2)
        st.success("Prediction completed successfully!")
        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#2563EB,#3B82F6);
        padding:30px;
        border-radius:20px;
        color:white;
        text-align:center;
        ">
        <h2>💰 Estimated Selling Price</h2>
        <h1>${prediction:,.2f}</h1>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error("Prediction Failed")
        st.exception(e)


# ==========================================
# Prediction Information
# ==========================================

if prediction is not None:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Best Model", "Random Forest")

    with col2:
        st.metric("Prediction Time", "<1 sec")

    with col3:
        st.metric("Status", "Completed")

    st.divider()

    # ==========================================
    # Vehicle Summary
    # ==========================================

    st.subheader("🚘 Vehicle Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Brand",
            "Model",
            "Year",
            "Mileage",
            "Fuel",
            "Transmission",
            "Engine",
            "Exterior",
            "Interior",
            "Accident",
            "Clean Title"
        ],
        "Value": [
            brand,
            model_name,
            year,
            mileage,
            fuel,
            transmission,
            engine,
            ext,
            interior,
            accident,
            clean_title
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    # ==========================================
    # Download Prediction
    # ==========================================

    result = pd.DataFrame({
        "Brand": [brand],
        "Model": [model_name],
        "Year": [year],
        "Mileage": [mileage],
        "Predicted Price": [prediction]
    })

    csv = result.to_csv(index=False)

    st.download_button(
        "📥 Download Prediction",
        csv,
        "prediction.csv",
        "text/csv",
        use_container_width=True
    )

    # ==========================================
    # Prediction History (Optional)
    # ==========================================

    import plotly.express as px

    history = pd.DataFrame()

    if not history.empty:
        fig = px.bar(
            history,
            x="Brand",
            y="Prediction",
            color="Brand",
            title="Prediction History"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.success("✅ Thank you for using the Used Car Price Prediction System.")