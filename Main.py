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
api.dataset_download_files('surajjha101/fortune-top-1000-companies-by-revenue-2022', unzip=True)
df_2022 = pd.read_csv('Fortune 1000 Companies by Revenue.csv')
api.dataset_download_files('shivamb/fortune-global-2000-companies-till-2021', unzip=True)
df_2021 = pd.read_csv('fortune_2000_in_2021.csv')

print('test')
st.write(df_2021)

# Achtergrond streamlit
achtergrond = ''' <style> body { background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); background-size: cover; } </style> '''


