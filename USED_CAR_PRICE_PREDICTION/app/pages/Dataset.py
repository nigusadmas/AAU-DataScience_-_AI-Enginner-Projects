import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Dataset",
    page_icon="📊",
    layout="wide")
# --------------------------------------------------
# CSS
# --------------------------------------------------
css = Path("app/assets/css/style.css")
if css.exists():
    with open(css) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
DATA_PATH = Path("data/processed/used_cars_clean.csv")
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)
df = load_data()
# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("""
# 📊 Dataset Dashboard
Explore and understand the Used Car dataset.
""")
st.divider()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
rows = df.shape[0]
cols = df.shape[1]
missing = df.isnull().sum().sum()
duplicates = df.duplicated().sum()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Rows", f"{rows:,}")
c2.metric("Columns", cols)
c3.metric("Missing Values", missing)
c4.metric("Duplicates", duplicates)
st.divider()

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------
st.subheader("Dataset Preview")
rows_to_show = st.slider("Number of rows",5,100,10)
st.dataframe(df.head(rows_to_show),use_container_width=True)

# --------------------------------------------------
# Search
# --------------------------------------------------
st.subheader("Search Dataset")
search = st.text_input("Search")
if search:
    filtered = df[
        df.astype(str)
          .apply(lambda x: x.str.contains(search, case=False))
          .any(axis=1)]
    st.dataframe(filtered,use_container_width=True)
st.divider()

# --------------------------------------------------
# Data Types
# --------------------------------------------------
st.subheader("Column Information")
dtype = pd.DataFrame({
    "Column":df.columns,
    "Data Type":df.dtypes.astype(str),
    "Missing":df.isnull().sum()})
st.dataframe(dtype,use_container_width=True,hide_index=True)
st.divider()

# --------------------------------------------------
# Summary Statistics
# --------------------------------------------------
st.subheader("Summary Statistics")
st.dataframe(df.describe(include="all").transpose(),use_container_width=True)
st.divider()

# --------------------------------------------------
# Missing Values
# --------------------------------------------------
st.subheader("Missing Values")
missing_df = pd.DataFrame({
    "Column":df.columns,
    "Missing":df.isnull().sum()})
fig = px.bar(
    missing_df,
    x="Column",
    y="Missing",
    color="Missing",
    title="Missing Values")
st.plotly_chart(fig,use_container_width=True)
st.divider()

# --------------------------------------------------
# Data Types Pie Chart
# --------------------------------------------------
st.subheader("Data Types Distribution")
type_count = df.dtypes.astype(str).value_counts()
pie = px.pie(
    names=type_count.index,
    values=type_count.values,
    hole=.5)
st.plotly_chart(pie,use_container_width=True)
st.divider()

# --------------------------------------------------
# Correlation
# --------------------------------------------------
numeric = df.select_dtypes(include="number")
if len(numeric.columns) > 1:
    st.subheader("Correlation Heatmap")
    corr = numeric.corr()
    heat = px.imshow(corr,text_auto=True,color_continuous_scale="Blues")
    st.plotly_chart(heat,use_container_width=True)
st.divider()

# --------------------------------------------------
# Numeric Feature Explorer
# --------------------------------------------------
st.subheader("Numeric Feature Distribution")
num_col = st.selectbox(
    "Select Numeric Column",
    numeric.columns)
hist = px.histogram(
    df,
    x=num_col,
    nbins=40,
    marginal="box",
    title=num_col)
st.plotly_chart(hist,use_container_width=True)
st.divider()

# --------------------------------------------------
# Category Explorer
#--------------------------------------------------

cat = df.select_dtypes(include="object")
if len(cat.columns) > 0:
    st.subheader("Categorical Feature Distribution")
    col = st.selectbox("Select Category",cat.columns)
    value = df[col].value_counts().head(15)
    bar = px.bar(
        x=value.index,
        y=value.values,
        color=value.values,
        labels={"x":col,"y":"Count"})
    st.plotly_chart(bar,use_container_width=True)
st.divider()

# --------------------------------------------------
# Download Dataset
# --------------------------------------------------
csv = df.to_csv(index=False)
st.download_button(
    "📥 Download Dataset",
    csv,
    file_name="used_cars_clean.csv",
    mime="text/csv",
    use_container_width=True)
st.success("Dataset loaded successfully.")