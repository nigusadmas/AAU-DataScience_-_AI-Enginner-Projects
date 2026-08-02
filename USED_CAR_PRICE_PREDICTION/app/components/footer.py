"""
=========================================================
Footer Component
=========================================================
"""

import streamlit as st
from datetime import datetime


# =========================================================
# Footer
# =========================================================

def show_footer():

    year = datetime.now().year

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <style>

        .footer {{
            margin-top:40px;
            padding:25px;
            border-radius:18px;
            background:#ffffff;
            box-shadow:0 4px 15px rgba(0,0,0,0.08);
            text-align:center;
        }}

        .footer h4 {{
            color:#2563EB;
            margin-bottom:8px;
        }}

        .footer p {{
            color:#666666;
            margin:4px;
            font-size:15px;
        }}

        </style>

        <div class="footer">

            <h4>🚗 Used Car Price Prediction System</h4>

            <p>
            Intelligent AI and Data Engineering
            </p>

            <p>
            Addis Ababa University
            </p>

            <p>
            Developed using
            <b>Python</b>,
            <b>Scikit-Learn</b>,
            <b>Streamlit</b>,
            <b>Plotly</b>
            </p>

            <p>
            © {year} Group 6 | All Rights Reserved
            </p>

        </div>

        """,
        unsafe_allow_html=True,
    )