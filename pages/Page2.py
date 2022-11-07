import pandas as pd
import streamlit as st
import folium

st.write('**Plattegrond New York**')
st.markdown('Hierbij de plattegrond van New York met de parameters van de elke AirBNB apartement')

################################################################################################################
mb = folium.Map(location=[40.730610, -73.935242], tiles="Openstreetmap")

data = pd.read_csv('clean_df.csv')
for i in range(0, len(data)):
    folium.marker(location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
                  popup=data.iloc[i]['name'], ).add_to(mb)
print(mb)
