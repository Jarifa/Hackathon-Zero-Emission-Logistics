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

# Dashboard
pages = st.sidebar.selectbox('Pagina', ('Home', 'Terrein Kaart', 'Verbruik', 'Ritteninformatie datasets'))

if pages == 'Home':
    st.header("**Klimaatneutraal rijden**")
    st.markdown(
        "Met dit dashboard wordt geprobeerd een zo een compleet mogelijk beeld te weergeven van de ontwikkeling van de energievraag van logistieke bedrijven en de knelpunten in het netwerk. Omdat er al een tekort is aan capaciteit op het elektriciteitsnetwerk, is de verwachting dat de aanleg van nieuwe aansluitingen door de netbeheerder tot wel 8 jaar kan duren. Daarom is het belangrijk om nu alvast in kaart te brengen wat de verwachtte energievraag is (hoeveel, waar en wanneer) in de toekomstige situatie zodat we ons op tijd kunnen voorbereiden en logistieke vervoerders niet hoeven te wachten met het aanschaffen van elektrische voertuigen omdat er onvoldoende netwerkcapaciteit beschikbaar is. Dat zou de energietransitie onnodig remmen.")

    # st.markdown("Welkom op het dashboard van groep 22. Gebruik de knoppen in de sidebar om tussen de verschillende paginas te navigeren. ")


elif pages == 'Terrein Kaart':
    st.subheader('Kaarten Bedrijventerreinen')
    st.markdown(
        "In de kaart zijn de energiebehoeftes van Schiphol tradepark en WFO per gebouw weergegeven. Hiermee gaan we een geschatte energievraag analyseren van op basis van voertuigregistraties. Op basis van publieke data en deelse CBS data. Wordt een inschatting gemaakt hoe de energiebehoefte/voorraad op bedrijventerreinen.")
    folium_static(mwfo)  # Kaart1
    folium_static(mstp)  # Kaart2
elif pages == 'Verbruik':
    st.subheader('Energie verbruik per dag')
    st.markdown(
        'In onderstaande velden voer een voertuig ID in om het energieverbruik over een dag van een vrachtwagen te visualiseren.')
    number = st.number_input('Voeg een voertuig ID in', min_value=1, max_value=200, value=1, step=1)

    # Knoppen maken zodat een dag van het jaar gekozen kan worden
    datum_2022 = st.date_input("Kies hier een datum voor het energieprofiel van 2022", datetime.date(2021, 4, 1),
                               min_value=datetime.date(2021, 4, 1), max_value=datetime.date(2021, 4, 30))

elif pages == 'Ritteninformatie datasets':
    st.subheader("Informatie over ritten")

# st.markdown("Voorbeelden van ID's in Allevoertuigen: " + voertuig_ids_string)
# st.markdown("Voorbeelden van ID's in December: " + voertuig_ids_december)
