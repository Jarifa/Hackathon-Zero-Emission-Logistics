# importing required libraries and packages
import numpy as np
import pandas as pd
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# importing datasets from API
api.dataset_download_files('arianazmoudeh/airbnbopendata', unzip=True)
df_original = pd.read_csv('Airbnb_Open_Data.csv')

st.write('Original "Dirty" dataframe:')
st.write(df_original)
df = df_original

# drop NaN locations
st.write('Na values voor drop:', df[['lat', 'long']].isna().sum())
df.dropna(subset=['lat', 'long'], inplace=True)
st.write('Na values na drop:', df[['lat', 'long']].isna().sum())

# price and service fee cleanup
df['price'] = df['price'].astype(str).str[1:]
df['service fee'] = df['service fee'].astype(str).str[1:]
df['price'] = df['price'].apply(lambda row: row.replace(',', ''))
df['service fee'] = df['service fee'].apply(lambda row: row.replace(',', ''))

df['price'] = df['price'].apply(lambda price: np.nan if price == 'an' else price)
df = df.astype({"price": "int", "service fee": "int"})

st.write(df)

"""a
st.write("price en service fee als int64")
df = df_original.apply(lambda row: row['price'][1:], axis = 1)
st.write(df)
"""


# Achtergrond############################################################################################
def add_bg_from_url():
    st.markdown(
        f""" <style> .stApp {{ background-image: url(
        "https://th.bing.com/th/id/R.c6d89244cbb1c6d916e87acd4984c09e?rik=5PX6aQALkMW6vg&riu=http%3a%2f%2fimg06
        .deviantart.net%2fca80%2fi%2f2014%2f196%2fb%2f1%2fminimal_new_york_by_kevichan-d61zr27.jpg&ehk=k9sZxjAJ
        %2blmBlAiGwtw0kJmHNRzbU4GLxez%2f42eOMo4%3d&risl=&pid=ImgRaw&r=0"); background-attachment: fixed; 
        background-size: cover }} </style> """,
        unsafe_allow_html=True
    )


add_bg_from_url()
###############################################################################################################
df.to_csv('clean_df.csv')
