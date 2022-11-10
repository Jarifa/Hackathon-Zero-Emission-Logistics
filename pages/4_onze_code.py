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

st.title('Onze code:')

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
