# importing required libraries and packages
import streamlit as st
import requests
import pandas as pd
import numpy as np
import json
import os

from kaggle.api.kaggle_api_extended import KaggleApi

# tijdelijk; alleen voor lokaal gebruik:
# os.environ['KAGGLE_USERNAME'] = "davevanderschouw"
# os.environ['KAGGLE_KEY'] = "dea650c8a5aa2e60e1af506563daf342"
api = KaggleApi()
api.authenticate()

# importing datasets from API
api.dataset_download_files('surajjha101/fortune-top-1000-companies-by-revenue-2022', unzip=True)
df_2022 = pd.read_csv('Fortune 1000 Companies by Revenue.csv')
api.dataset_download_files('shivamb/fortune-global-2000-companies-till-2021', unzip=True)
df_2021 = pd.read_csv('fortune_2000_in_2021.csv')

print('test')
st.write(df_2021)
