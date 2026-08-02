import streamlit as st
from PIL import Image
from pathlib import Path

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# Load CSS
# =====================================================

css = Path("app/assets/css/style.css")
if css.exists():
    with open(css) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True)
# =====================================================
# Hero Image
# =====================================================
hero_path = Path("app/assets/images/hero.png")
if hero_path.exists():
    hero = Image.open(hero_path)
    st.image(hero, use_container_width=True)
else:
    st.warning("⚠ Hero image not found.")

# =====================================================
# Hero Title
# =====================================================
st.markdown("""
<div style="text-align:center">
<h1 style="font-size:55px;color:#2563EB;">
🚗 Used Car Price Prediction System
</h1>
<h3 style="color:gray;">
Intelligent AI and Data Engineering
</h3>
<p style="font-size:20px;">
Predict the selling price of used cars using advanced Machine Learning Regression algorithms.
</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# Call To Action
# =====================================================
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.button("🚗 Start Prediction", use_container_width=True)
with col2:
    st.button("📊 Explore Dataset", use_container_width=True)
with col3:
    st.button("📈 Compare Models", use_container_width=True)
st.write("")

# =====================================================
# Statistics
# =====================================================
st.markdown("## 📊 Project Statistics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("🚗 Cars", "4,009")
c2.metric("🤖 Models", "9")
c3.metric("🎯 Best Model", "Random Forest")
c4.metric("📈 R² Score", "0.95")
st.divider()

# =====================================================
# Features
# =====================================================
st.markdown("## ✨ Key Features")
f1, f2, f3, f4 = st.columns(4)
with f1:
    st.info("""
### 📊
### Data Analysis
Interactive visualizations and statistics.
""")
with f2:
    st.info("""
### 🤖
### Machine Learning
Compare multiple regression algorithms.
""")
with f3:
    st.info("""
### 📈
### Model Evaluation
MAE
RMSE
R² Score
Cross Validation
""")
with f4:
    st.info("""
### 🚗
### Smart Prediction
Instant used car price prediction.
""")
st.divider()

# =====================================================
# Workflow
# =====================================================
st.markdown("## ⚙ Machine Learning Workflow")
w1,w2,w3,w4,w5,w6,w7 = st.columns(7)
with w1:
    st.success("📂\n\nDataset")
with w2:
    st.success("🧹\n\nCleaning")
with w3:
    st.success("📊\n\nEDA")
with w4:
    st.success("⚙\n\nFeatures")
with w5:
    st.success("🤖\n\nTraining")
with w6:
    st.success("🏆\n\nBest Model")
with w7:
    st.success("🚗\n\nPrediction")
st.divider()

# =====================================================
# Models
# =====================================================
st.markdown("## 🤖 Regression Models")
m1,m2,m3 = st.columns(3)
with m1:
    st.markdown("""
✅ Linear Regression
✅ Ridge Regression
✅ Lasso Regression
""")
with m2:

    st.markdown("""
✅ Decision Tree
⭐ Random Forest
✅ Gradient Boosting
""")
with m3:
    st.markdown("""
✅ Support Vector Regression
✅ Extra Trees
✅ AdaBoost
""")
st.divider()

# =====================================================
# Technology Stack
# =====================================================
st.markdown("## 🛠 Technology Stack")
t1,t2,t3,t4 = st.columns(4)
with t1:
    st.metric("Language","Python")
with t2:
    st.metric("ML","Scikit-Learn")
with t3:
    st.metric("Framework","Streamlit")
with t4:
    st.metric("Visualization","Plotly")
st.divider()

# =====================================================
# Why Choose This App
# =====================================================
st.markdown("## 🌟 Why Use This Application?")
a,b,c,d = st.columns(4)
with a:
    st.success("🎯 High Prediction Accuracy")
with b:
    st.success("⚡ Fast Prediction")
with c:
    st.success("📈 Explainable AI (SHAP)")
with d:
    st.success("💻 Modern User Interface")
st.divider()

# =====================================================
# Footer
# =====================================================
st.markdown("""
<hr>
<div style='text-align:center;'>
### 🚗 Used Car Price Prediction System
Intelligent AI and Data Engineering
Addis Ababa University
Developed with ❤️ using Streamlit & Scikit-Learn
</div>
""", unsafe_allow_html=True)