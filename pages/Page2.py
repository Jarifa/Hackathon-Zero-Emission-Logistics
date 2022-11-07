import pandas as pd
import streamlit as st
import folium
from folium import plugins
from streamlit_folium import st_folium
from streamlit_folium import folium_static


###################################################################################################################
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://th.bing.com/th/id/R.c6d89244cbb1c6d916e87acd4984c09e?rik=5PX6aQALkMW6vg&riu=http%3a%2f%2fimg06.deviantart.net%2fca80%2fi%2f2014%2f196%2fb%2f1%2fminimal_new_york_by_kevichan-d61zr27.jpg&ehk=k9sZxjAJ%2blmBlAiGwtw0kJmHNRzbU4GLxez%2f42eOMo4%3d&risl=&pid=ImgRaw&r=0");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
#######################################################################################################################
st.write('**Plattegrond New York**')
st.markdown('Hierbij de plattegrond van New York met de parameters van de elke AirBNB apartement')

################################################################################################################
mb = folium.Map(location=[40.730610, -73.935242])

data = pd.read_csv('clean_df.csv')
unique_neighbourhoods = data['neighbourhood'].unique()
st.write(type(unique_neighbourhoods))

selection = st.selectbox(
    'Select neighbourhood',
    unique_neighbourhoods
    )

st.write('You selected:', selection)

st.write('unique neighbourhoods: ', unique_neighbourhoods)

neighbourhood = data[data['neighbourhood'] == selection]
st.write('neighbourhood = ', neighbourhood)
st.write('lengte neighbourhood = ', len(data))

# range:
# for i in range(0, len(data)):
#    folium.marker([data.iloc[i]['lat'], data.iloc[i]['lon']],
#                  popup=data.iloc[i]['name']).add_to(mb)

# iterrows:
marker_cluster = folium.plugins.MarkerCluster(name='Clusters', overlay=False, control=True).add_to(mb)
for index, row in data.iterrows():
    folium.Marker(location=[row['lat'], row['long']], popup=row['NAME']).add_to(marker_cluster)



# itertuples:
# folium.Marker([data.long.values[1], data.lat.values[1]], popup=data.NAME.values[1]).add_to(mb)

# apply:
# data.apply(lambda row: folium.marker([row['long'], row['lat']], popup=row['NAME']).add_to(mb))

st_map = folium_static(mb)




