import pandas as pd
import streamlit as st
import folium

st.write('**Plattegrond New York**')
st.markdown('Hierbij de plattegrond van New York met de parameters van de elke AirBNB apartement')

################################################################################################################
mb = folium.Map(location=[40.730610, -73.935242], tiles="Openstreetmap")

data = pd.read_csv('clean_df.csv')

#range:
"""for i in range(0, len(data)):
    folium.marker([data.iloc[i]['lat'], data.iloc[i]['lon']],
                  popup=data.iloc[i]['name']).add_to(mb)"""

#iterrows:
for index, row in data.iterrows():
    folium.Marker([row['lng'], row['lat']], popup=row['NAME']).add_to(mb)

# apply:
"""data.apply(lambda row: folium.marker([row['lat'], row['lon']],
                                     popup=row['name']).add_to(mb))"""

st.write(mb)




