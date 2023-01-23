import streamlit as st
import pandas as pd
import folium
from folium import Map
from streamlit_folium import st_folium
from streamlit_folium import folium_static


# Read the CSV file into a dataframe
file = r'D:\Checkers.csv'

def display_map(file):
    data = pd.read_csv(file)
    m = Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=8)
    for i, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['NAME'],
            icon=folium.Icon(color='red')
        ).add_to(m)
    #st.write(m)
    folium_static(m)

st.header('Checkers KwaZulu-Natal Store Finder')

st.sidebar.title("Data Uploader")

def main():
    file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        display_map(file)

if __name__ == '__main__':
    main()


