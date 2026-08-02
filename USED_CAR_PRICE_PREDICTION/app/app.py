"""
=========================================================
🚗 Used Car Price Prediction System
Home Page
=========================================================
"""

from pathlib import Path
import streamlit as st

from components.sidebar import show_sidebar
from components.footer import show_footer
from components.cards import metric_card

# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# Load CSS
# =========================================================

css_file = Path("app/assets/css/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

# =========================================================
# Sidebar
# =========================================================

show_sidebar()

# =========================================================
# Hero Section
# =========================================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#2563EB,#1E40AF);
padding:45px;
border-radius:20px;
text-align:center;
color:white;
">

<h1>🚗 Intelligent Used Car Price Prediction</h1>

<h4>
Machine Learning Regression Web Application
</h4>

<p>
Predict the selling price of used vehicles using
state-of-the-art Machine Learning models.
</p>
</div>
""", unsafe_allow_html=True)
st.write("")

# =========================================================
# Statistics
# =========================================================
st.subheader("📊 Project Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    metric_card(
        "Dataset",
        "4,009 Cars")
with col2:
    metric_card(
        "Models",
        "9")
with col3:
    metric_card(
        "Target",
        "Selling Price")
with col4:
    metric_card(
        "Best Model",
        "Random Forest")
st.divider()
# =========================================================
# About Project
# =========================================================

left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown("""
    <div class="about-card">
        <h2>🚗 About the Project</h2>

        📂 Dataset Understanding
        🧹 Data Cleaning
        📊 Exploratory Data Analysis
        ⚙️ Feature Engineering
        🤖 Model Training
        🎯 Hyperparameter Tuning
        📈 Model Evaluation
        💰 Price Prediction
        ☁️ Deployment
    </div>
    """, unsafe_allow_html=True)
with right:
    st.image(
        "app/assets/images/hero.png",
        use_container_width=True
    )

st.divider()

# =========================================================
# Machine Learning Workflow
# =========================================================

st.header("⚙ Machine Learning Workflow")

workflow = [
    "📂 Dataset",
    "🧹 Data Cleaning",
    "📊 Exploratory Data Analysis",
    "⚙ Feature Engineering",
    "🤖 Regression Models",
    "🎯 Hyperparameter Tuning",
    "📈 Model Evaluation",
    "🚗 Prediction",
    "🌍 Deployment",
]

cols = st.columns(len(workflow))

for col, step in zip(cols, workflow):
    with col:
        st.info(step)

st.divider()

# =========================================================
# Project Features
# =========================================================

st.header("✨ Features")
col1, col2 = st.columns(2)
with col1:
    st.success("""
✅ Data Cleaning

✅ Feature Engineering

✅ 9 Regression Models

✅ Cross Validation

✅ GridSearchCV

✅ RandomizedSearchCV
""")

with col2:

    st.success("""
✅ SHAP Explainability

✅ Feature Importance

✅ Learning Curves

✅ Residual Analysis

✅ Prediction Dashboard

✅ Interactive Visualizations
""")

st.divider()

# =========================================================
# Navigation Guide
# =========================================================

st.header("🧭 Explore the Application")

st.info("""
Use the sidebar to navigate through the application.

📊 Dataset

📈 Exploratory Data Analysis

🤖 Model Comparison

🚗 Prediction

📋 Project Information

👥 About Team
""")

st.divider()

# =========================================================
# Technologies
# =========================================================
st.header("🛠 Technology Stack")
tech1, tech2, tech3, tech4 = st.columns(4)
tech1.metric("Language", "Python")
tech2.metric("Machine Learning", "Scikit-Learn")
tech3.metric("Framework", "Streamlit")
tech4.metric("Visualization", "Plotly")

# =========================================================
# Footer
# =========================================================


footer = """
<div class="footer">

<hr>

<h4>🚗 Used Car Price Prediction System</h4>

<p>Intelligent AI and Data Engineering</p>

<p>Addis Ababa University</p>

<p>
Developed using
<b>Python</b>,
<b>Scikit-Learn</b>,
<b>Streamlit</b>,
<b>Plotly</b>
</p>

<p>nigusadmas |© 2026 addis ababa unversity | All Rights Reserved</p>

</div>
"""

st.markdown(footer, unsafe_allow_html=True)

st.markdown("""
<style>

/* Footer */
.footer{
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    background-color: #f8f9fa;
    border-top: 2px solid #0d6efd;
    border-radius: 10px;
    color: #555;
    line-height: 1.8;
}

.footer h4{
    color: #0d6efd;
    margin-bottom: 10px;
    font-size: 24px;
}

.footer p{
    margin: 6px 0;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)