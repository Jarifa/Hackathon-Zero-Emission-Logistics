# importing required libraries and packages
from datetime import datetime

import streamlit as st
import requests
import pandas as pd
import numpy as np
import json
import os

import geopandas as gpd
import seaborn
import plotly.express as px
import plotly.figure_factory as ff
from shapely.geometry import Point
import missingno as msno
import statsmodels.api as sm
from fuzzywuzzy import fuzz

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# importing datasets from API
api.dataset_download_files('arianazmoudeh/airbnbopendata', unzip=True)
df_original = pd.read_csv('Airbnb_Open_Data.csv')


print('test')
st.write(df_original)

#  Achtergrond streamlit
achtergrond = ''' <style> body { background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); background-size: cover; } </style> '''


