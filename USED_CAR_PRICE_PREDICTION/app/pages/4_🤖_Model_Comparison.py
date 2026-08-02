import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Model Comparison",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# Load CSS
# ==========================================================

css = Path("app/assets/css/style.css")

if css.exists():
    with open(css) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# Load Model Comparison Results
# ==========================================================

RESULT_PATH = Path("outputs/tables/model_comparison.csv")

@st.cache_data
def load_results():
    return pd.read_csv(RESULT_PATH)

results = load_results()

# Sort by R²
results = results.sort_values(
    "R2 Score",
    ascending=False
).reset_index(drop=True)

# ==========================================================
# Header
# ==========================================================

st.title("🤖 Regression Model Comparison")

st.caption(
    "Performance comparison of all trained regression models."
)

st.divider()

# ==========================================================
# Best Model
# ==========================================================

best = results.iloc[0]

st.success(
    f"🏆 Best Model: **{best['Model']}**"
)

# ==========================================================
# KPI Cards
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Best R²",
    f"{best['R2 Score']:.4f}"
)

c2.metric(
    "RMSE",
    f"{best['RMSE']:.2f}"
)

c3.metric(
    "MAE",
    f"{best['MAE']:.2f}"
)

c4.metric(
    "CV Mean",
    f"{best['CV Mean']:.4f}"
)

st.divider()

# ==========================================================
# Complete Table
# ==========================================================

st.subheader("📋 Model Performance Table")

st.dataframe(
    results,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# R² Score
# ==========================================================

st.subheader("📈 R² Score Comparison")

fig = px.bar(
    results,
    x="Model",
    y="R2 Score",
    color="R2 Score",
    text="R2 Score"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# RMSE
# ==========================================================

st.subheader("📉 RMSE Comparison")

fig = px.bar(
    results,
    x="Model",
    y="RMSE",
    color="RMSE",
    text="RMSE"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# MAE
# ==========================================================

st.subheader("📊 MAE Comparison")

fig = px.bar(
    results,
    x="Model",
    y="MAE",
    color="MAE",
    text="MAE"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# Training Time
# ==========================================================

if "Training Time" in results.columns:

    st.subheader("⏱ Training Time")

    fig = px.bar(
        results,
        x="Model",
        y="Training Time",
        color="Training Time",
        text="Training Time"
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# Cross Validation
# ==========================================================

if "CV Mean" in results.columns:

    st.subheader("🔄 Cross Validation")

    fig = px.bar(
        results,
        x="Model",
        y="CV Mean",
        color="CV Mean",
        text="CV Mean"
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# Radar Chart
# ==========================================================

st.subheader("🕸 Model Performance Radar")

radar = results.copy()

fig = px.line_polar(
    radar,
    r="R2 Score",
    theta="Model",
    line_close=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# Ranking
# ==========================================================

st.subheader("🥇 Final Ranking")

ranking = results[
    [
        "Model",
        "R2 Score",
        "RMSE",
        "MAE"
    ]
].copy()

ranking.insert(
    0,
    "Rank",
    range(1, len(ranking)+1)
)

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# Winner Card
# ==========================================================

st.divider()

st.markdown(
f"""
<div style="
background:linear-gradient(135deg,#2563EB,#1D4ED8);
padding:30px;
border-radius:20px;
color:white;
text-align:center;
">

<h2>🏆 Best Performing Model</h2>

<h1>{best['Model']}</h1>

<h3>R² Score : {best['R2 Score']:.4f}</h3>

<h3>RMSE : {best['RMSE']:.2f}</h3>

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# Download Results
# ==========================================================

csv = results.to_csv(index=False)

st.download_button(
    "📥 Download Model Comparison",
    csv,
    "model_comparison.csv",
    "text/csv",
    use_container_width=True
)

st.success("Model comparison dashboard loaded successfully.")