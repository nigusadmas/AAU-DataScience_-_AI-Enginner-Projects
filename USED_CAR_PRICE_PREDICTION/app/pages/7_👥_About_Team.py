import streamlit as st
from pathlib import Path

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="About Team",
    page_icon="👥",
    layout="wide"
)

# ==========================================================
# LOAD CSS
# ==========================================================

css = Path("app/assets/css/style.css")

if css.exists():
    with open(css) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# HEADER
# ==========================================================
st.title("👥 About Our Team")
st.caption("Intelligent AI and Data Engineering Project")
st.divider()

# ==========================================================
# UNIVERSITY INFORMATION
# ==========================================================
c1, c2, c3 = st.columns(3)
c1.metric("University", "AAU")
c2.metric("Course", "Data Science & AI Engineering")
st.divider()

# ==========================================================
# PROJECT INFORMATION
# ==========================================================
st.header("🚗 Project")
st.info("""
**Title**
Used Car Price Prediction Using Machine Learning
**Type**
Regression Machine Learning Project
**Target Variable**
Selling Price
**Development Framework**
Streamlit + Scikit-Learn
""")

# ==========================================================
# TEAM MEMBERS
# ==========================================================
st.header("👨‍💻 Meet Our Team")
st.markdown("""
<div style="
background:linear-gradient(135deg,#2563EB,#1E3A8A);
padding:25px;
border-radius:20px;
color:white;
text-align:center;
margin-bottom:25px;
box-shadow:0px 10px 30px rgba(0,0,0,.25);
">
<h2>🚀 Intelligent AI & Data Engineering Team</h2>
<p>Building an End-to-End Machine Learning Solution for Used Car Price Prediction</p>
</div>
""", unsafe_allow_html=True)
member1, member2 = st.columns(2)

# ==========================================================
# MEMBER 1
# ==========================================================
with member1:
    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0F172A,#1E293B);
    color:white;
    border-radius:20px;
    padding:25px;
    min-height:500px;
    box-shadow:0 8px 25px rgba(0,0,0,.35);
    border-top:5px solid #3B82F6;
    ">
    <div style="text-align:center;">
        <div style="font-size:70px;">👨‍💻</div>
        <h2 style="color:#60A5FA;">Nigus Admas</h2>
        <h4 style="color:#CBD5E1;">
        Machine Learning & Backend Developer
        </h4>
    </div>
    <hr style="border:1px solid #334155;">
    <h4 style="color:#38BDF8;">Responsibilities</h4>
    ✅ Data Cleaning<br>
    ✅ Data Preprocessing<br>
    ✅ Feature Engineering<br>
    ✅ Model Development<br>
    ✅ Hyperparameter Tuning<br>
    ✅ Model Evaluation<br>
    ✅ Prediction Pipeline<br>
    ✅ Backend Development<br>
    ✅ Streamlit Integration<br>
    ✅ GitHub Management
    <h4 style="color:#FACC15;">Skills</h4>

    🐍 Python • 🤖 Scikit-Learn • 📊 Pandas • 📈 NumPy • 🚀 Streamlit

    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# MEMBER 2
# ==========================================================
with member2:
    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#14532D,#166534);
    color:white;
    border-radius:20px;
    padding:25px;
    min-height:500px;
    box-shadow:0 8px 25px rgba(0,0,0,.35);
    border-top:5px solid #22C55E;
    ">
    <div style="text-align:center;">
        <div style="font-size:70px;">👩‍💻</div>
        <h2 style="color:#86EFAC;">Minale Wubet</h2>
        <h4 style="color:#DCFCE7;">
        Data Analyst & Frontend Developer
        </h4>
    </div>
    <hr style="border:1px solid #4ADE80;">
    <h4 style="color:#BBF7D0;">Responsibilities</h4>
    ✅ Exploratory Data Analysis<br>
    ✅ Data Visualization<br>
    ✅ Dashboard Design<br>
    ✅ User Interface Design<br>
    ✅ User Experience (UX)<br>
    ✅ CSS Styling<br>
    ✅ Documentation<br>
    ✅ Testing<br>
    ✅ Presentation Preparation
    <h4 style="color:#FACC15;">Skills</h4>
    
    🎨 Streamlit • 📊 Plotly • 📉 Matplotlib • 📚 Documentation • 💻 UI/UX
    </div>
    """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# TEAM STATISTICS
# ==========================================================

st.subheader("📊 Team Statistics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("👥 Members", "2")
c2.metric("🤖 ML Models", "9")
c3.metric("💻 Technologies", "10+")
c4.metric("🚀 Status", "Completed")

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================
st.header("🛠 Technology Stack")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.success("""
🐍 Python

Pandas

NumPy
""")

with col2:
    st.success("""
🤖 Machine Learning

Scikit-Learn

SHAP
""")

with col3:
    st.success("""
📊 Visualization

Plotly

Matplotlib

Seaborn
""")

with col4:
    st.success("""
🌐 Deployment

Streamlit

GitHub

Docker (Future)
""")

st.divider()

# ==========================================================
# PROJECT FEATURES
# ==========================================================

st.header("✨ Project Features")

st.markdown("""
<div style="
background:linear-gradient(135deg,#2563EB,#1E40AF);
padding:20px;
border-radius:15px;
color:white;
text-align:center;
margin-bottom:25px;
">
<h2>🚗 End-to-End Machine Learning Solution</h2>
<p>Complete workflow from data preparation to intelligent price prediction.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# ----------------------------------------------------------

with col1:

    st.success("""
### 📊 Data Analytics

✅ Dataset Understanding

✅ Data Cleaning

✅ Missing Value Handling

✅ Exploratory Data Analysis

✅ Data Visualization

✅ Feature Engineering

✅ Correlation Analysis
""")

# ----------------------------------------------------------

with col2:

    st.info("""
### 🤖 Machine Learning

✅ 9 Regression Models

✅ Cross Validation

✅ Hyperparameter Tuning

✅ Model Comparison

✅ Best Model Selection

✅ Feature Importance

✅ SHAP Explainability
""")

# ----------------------------------------------------------

with col3:

    st.warning("""
### 🌐 Web Application

✅ Interactive Dashboard

✅ Real-Time Prediction

✅ Responsive UI

✅ Prediction History

✅ Download Results

✅ GitHub Integration

✅ Deployment Ready
""")

st.markdown("---")

st.subheader("🏆 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Regression Models", "9")
c2.metric("Evaluation Metrics", "4")
c3.metric("ML Workflow", "Complete")
c4.metric("Deployment", "Streamlit")
st.divider()

# ==========================================================
# MACHINE LEARNING WORKFLOW
# ==========================================================

st.header("⚙️ Machine Learning Workflow")

st.markdown("""
<div style="
background: linear-gradient(135deg,#2563EB,#1E3A8A);
padding:25px;
border-radius:15px;
color:white;
text-align:center;
margin-bottom:20px;
">
<h2>End-to-End Machine Learning Lifecycle</h2>
<p>From Business Understanding to Web Deployment</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### 🎯 Phase 1

✅ Business Problem

⬇️

✅ Dataset Understanding

⬇️

✅ Data Cleaning

⬇️

✅ Data Preprocessing
""")

with col2:

    st.success("""
### 📊 Phase 2

✅ Exploratory Data Analysis

⬇️

✅ Feature Engineering

⬇️

✅ Feature Selection

⬇️

✅ Train/Test Split
""")

with col3:

    st.warning("""
### 🤖 Phase 3

✅ Regression Models

⬇️

✅ Cross Validation

⬇️

✅ Hyperparameter Tuning

⬇️

✅ Model Evaluation
""")

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:

    st.success("""
### 📈 Phase 4

✅ Model Comparison

⬇️

✅ Best Model Selection

⬇️

✅ Feature Importance
""")

with col5:

    st.info("""
### 🧠 Phase 5

✅ SHAP Explainability

⬇️

✅ Residual Analysis

⬇️

✅ Learning Curves
""")

with col6:

    st.error("""
### 🚀 Phase 6

✅ Model Saving

⬇️

✅ Streamlit Web App

⬇️

✅ GitHub Repository

⬇️

✅ Deployment
""")

st.markdown("---")

st.progress(100)
st.divider()
# ==========================================================
# GITHUB
# ==========================================================
st.header("🌐 Repository")
github = st.text_input(
    "GitHub Repository",
    "https://github.com/nigusadmas/AAU-DataScience_-_AI-Enginner-Projects/tree/main/USED_CAR_PRICE_PREDICTION"
)
st.link_button(
    "Open GitHub Repository",
    github
)
st.divider()
# ==========================================================
# ACKNOWLEDGEMENT
# ==========================================================
st.header("🙏 Acknowledgement")
st.write("""
We sincerely thank our friends for guiding me to develop this real-world Machine Learning project.
This project helped us understand the complete Machine Learning lifecycle,
from data preprocessing to deployment.
""")
st.divider()
# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""
<div style="text-align:center;color:gray;padding:20px;">
🚗 Used Car Price Prediction System
Developed by | nigudadmas |

© 2026 G.C

</div>
""", unsafe_allow_html=True)