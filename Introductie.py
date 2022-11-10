# importing required libraries and packages
import numpy as np
import pandas as pd
import geopandas
from shapely.geometry import Point
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

st.set_page_config(layout="wide")
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
#######
api = KaggleApi()
api.authenticate()

###Introtekst
st.header("DASHBOARD Dave van der Schouw, Benjamin Niemann")
st.markdown("Welkom bij het dashboard over AirBnB data van NewYork.")
st.image('Kaggle.png')

# importing datasets from API
api.dataset_download_files('arianazmoudeh/airbnbopendata', unzip=True)
df_original = pd.read_csv('Airbnb_Open_Data.csv')

df = df_original

# st.write('names of columns in df: ', list(df))

# drop NaN locations en prices
df.dropna(subset=['lat', 'long', 'price', 'service fee'], inplace=True)

# price and service fee cleanup
df['price'] = df['price'].astype(str).str[1:]
df['service fee'] = df['service fee'].astype(str).str[1:]
df['price'] = df['price'].apply(lambda row: row.replace(',', ''))
df['service fee'] = df['service fee'].apply(lambda row: row.replace(',', ''))

df = df.astype({"price": "int", "service fee": "int"})

# nieuwe kolom met service fee percentage = service fee / price + service fee
df['serv_fee_perc'] = df['service fee'].values / (df['price'].values + df['service fee'].values)

# brookln groep veranderen naar Brooklyn
df['neighbourhood group'] = df['neighbourhood group'].replace('brookln', 'Brooklyn')


# st.write('"Clean" dataframe: ', df)

# geopandas dataframe maken
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.long, df.lat))
# st.write('geodataframe test: ', gdf)

Battery = Point(-74.01540840380054, 40.7032047224727)
# st.write('Battery point test: ', Battery)

gdf['dist'] = gdf.distance(Battery)


###############################################################################################################
gdf.to_csv('clean_df.csv')
df_original.to_csv('original.csv')
