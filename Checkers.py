import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

@st.cache
def load_data():
    data = pd.read_csv(r'D:\Checkers.csv')
    return data

m = folium.Map()

data = load_data()

st.write(m)
st_data = st_folium(data, width=725)

st.sidebar.title("Data Analysis")

analysis_type = st.sidebar.selectbox("Select Analysis Type", ["Show Data", "Show Columns", "Show Shape", "Show Summary", "Show Missing Values"])

if analysis_type == "Show Data":
    st.write(data)

if analysis_type == "Show Columns":
    st.write("Columns:", data.columns)

if analysis_type == "Show Shape":
    st.write("Shape:", data.shape)

if analysis_type == "Show Summary":
    st.write(data.describe())

if analysis_type == "Show Missing Values":
    st.write(data.isna().sum())

load_data()

