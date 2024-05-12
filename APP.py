import folium
import pandas as pd
import streamlit as st
import streamlit_folium as sf
from folium.plugins import Draw
df = pd.read_csv("shark.csv",sep=";")
st.title("Shark")
st.markdown("The data is shown below: ")
st.sidebar.title("Options")
st.sidebar.markdown("Select Shakr:")
Chart = st.sidebar.selectbox(  'Which Shark would you like to see?',
    df["Shark"].unique())
mask = df["Shark"] == Chart
df_WS1 = df[mask]
location = df_WS1.iloc[:,2:4]
map = folium.Map(location=location.iloc[0],zoom_start=12)
folium.PolyLine(location).add_to(map)


output = sf.st_folium(map,returned_objects=[])
st.markdown(output)
