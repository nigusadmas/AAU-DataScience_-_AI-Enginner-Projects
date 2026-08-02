from pathlib import Path
import streamlit as st


def show_sidebar():
    # Get the app directory
    BASE_DIR = Path(__file__).resolve().parents[1]

    # Image path
    logo_path = BASE_DIR / "assets" / "images" / "logo.png"

    # Display logo if it exists
    if logo_path.exists():
        st.sidebar.image(str(logo_path), width=120)
    else:
        st.sidebar.warning("Logo image not found.")

    st.sidebar.title("🚗 Navigation")

    st.sidebar.success("Used Car Price Prediction")

    st.sidebar.info(
        """
        Intelligent AI and Data Engineering
        """
    )