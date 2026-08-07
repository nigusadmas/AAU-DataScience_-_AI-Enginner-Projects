import streamlit as st
def show_sidebar():
    st.sidebar.image(
        "app/assets/images/logo.png",width=120)
    st.sidebar.title("🚗 Navigation")
    st.sidebar.success("Used Car Price Prediction")
    st.sidebar.info(
        """
        Intelligent Data and AI Engineering
        """)