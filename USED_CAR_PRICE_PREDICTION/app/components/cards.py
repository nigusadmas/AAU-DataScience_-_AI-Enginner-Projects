import streamlit as st
def metric_card(title,value):
    st.markdown(
        f"""
        <div class="metric-card">
        <h3>{title}</h3>
        <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True)