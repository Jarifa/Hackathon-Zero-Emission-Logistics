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
st.write(df_original.dtypes)

st.write("price en service fee als int64")
df = df_original.apply(lambda row: row['price'][1,:])
st.write(df)

# Achtergrond streamlit achtergrond = ''' <style> body { background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); background-size: cover; } </style> '''

