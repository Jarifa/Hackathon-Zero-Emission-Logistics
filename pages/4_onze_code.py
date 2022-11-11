import pandas as pd
import streamlit as st


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
df_original = pd.read_csv('original.csv')
data = pd.read_csv('clean_df.csv')

st.title('Onze code en data:')

st.header('Environment variables')
st.image('environment_variables.png')
st.code("""
KAGGLE_USERNAME = <username>
KAGGLE_KEY = <key>
""")

st.header('API')
st.write('De Kaggle API en environment variables')
st.code(
"""from kaggle.api.kaggle_api_extended import KaggleApi

# initiate and authenticate API
api = KaggleApi()
api.authenticate()

# importing datasets from API
api.dataset_download_files('arianazmoudeh/airbnbopendata', unzip=True)

#DataFrame inlezen
df_original = pd.read_csv('Airbnb_Open_Data.csv')""", language='python'
)


st.header('De originele dataframe:')
st.write('Original "Dirty" dataframe:', df_original.head(20))

st.header('Opschonen dataframe')
# Code voor opschonen van dataframe
st.code("""
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
""", language='python')

st.header('Van Dataframe naar GeoDataFrame:')
# code voor geopandas dataframe met dist
st.code("""
# maken van geopandas dataframe, maakt automatisch geometry kolom aan met punten
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.long, df.lat))

# Punt aanmaken die Battery aangeeft (locatie in centrum new york)
Battery = Point(-74.01540840380054, 40.7032047224727)

# afstand berekenen tot punt voor elke row in dataframe en in nieuwe kolom 'dist' plaatsen
gdf['dist'] = gdf.distance(Battery)""", language='python')

st.header('De opgeschoonde en verbeterde dataframe:')
st.write('Clean dataframe met dist vanaf Battery (centrum new york): ')
st.write(data[['NAME', 'neighbourhood group', 'price', 'lat', 'long', 'geometry', 'dist']].head(20))

st.header('De kaart van New York')
st.code("""
# map aanmaken in folium
mb = folium.Map(location=[40.730610, -73.935242])

# lijst met unieke neighbourhoods maken
unique_neighbourhoods = data['neighbourhood'].unique()

#selection box met unieke neighbourhoods
selection = st.selectbox(
    'Selecteer buurt',
    unique_neighbourhoods
)

# deze geselecteerde neighbourhood opslaan als nieuwe dataframe
neighbourhood = data[data['neighbourhood'] == selection]

# met deze nieuwe neighbourhood dataframe markers aanmaken voor op de folium map
st.write('Kaart met aanbiedingen in de buurt')
marker_cluster = folium.plugins.MarkerCluster(name='Clusters', overlay=False, control=True).add_to(mb)
for index, row in neighbourhood.iterrows():
    folium.Marker(location=[row['lat'], row['long']], popup=('Description: ' + str(row['NAME'])),
                  tooltip=('price: ' + str(row['price']))).add_to(marker_cluster)

# folium in streamlit laden
st_map = folium_static(mb, width=1100, height=800)
""", language='python')

st.header('Code voor de correlation matrix')
st.code("""
# Heatmap van 0 tot 1
fig, ax = plt.subplots()
sns.heatmap(data[['host_identity_verified', 'neighbourhood group', 'neighbourhood', 'instant_bookable',
                  "cancellation_policy", "room type", "Construction year", "price", "minimum nights",
                  "number of reviews", "review rate number", "calculated host listings count",
                  "availability 365"]].corr(), ax=ax, vmin=0, vmax=1, cmap='Blues')
st.write(fig)

# Heatmap van -1 tot 0
fig, ax = plt.subplots()
sns.heatmap(data[['host_identity_verified', 'neighbourhood group', 'neighbourhood', 'instant_bookable',
                  "cancellation_policy", "room type", "Construction year", "price", "minimum nights",
                  "number of reviews", "review rate number", "calculated host listings count",
                  "availability 365"]].corr(), ax=ax, vmin=-1, vmax=0, cmap='Reds')
st.write(fig)""", language='python')
