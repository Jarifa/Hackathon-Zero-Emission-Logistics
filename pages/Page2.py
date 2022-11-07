import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

st.write('**Plattegrond New York**')
st.markdown('Hierbij de plattegrond van New York met de parameters van de elke AirBNB apartement')

################################################################################################################
mb = folium.Map(location=[40.730610, -73.935242], tiles="Openstreetmap")
st_map = st_folium(mb)

data = pd.read_csv('clean_df.csv')

#range:
"""for i in range(0, len(data)):
    folium.marker([data.iloc[i]['lat'], data.iloc[i]['lon']],
                  popup=data.iloc[i]['name']).add_to(mb)"""

#iterrows:
"""for index, row in data.iterrows():
    folium.Marker([row['long'], row['lat']], popup=row['NAME']).add_to(mb)"""

#itertuples
for row_tuple in data.itertuples():
    folium.Marker([row_tuple.long, row_tuple.lat], popup=row_tuple.NAME).add_to(mb)

# apply:
"""data.apply(lambda row: folium.marker([row['long'], row['lat']],
                                     popup=row['NAME']).add_to(mb))"""




