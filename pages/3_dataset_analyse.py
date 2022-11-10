#######packages

import pandas as pd
import numpy as np
import plotly as px
import streamlit as st
import plotly.express as px
#comment
##########Code voor regression
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
##Price tegenover bouwjaar
data = pd.read_csv('clean_df.csv')
st.write(list(data))
avg_df = data[['neighbourhood', 'price']].groupby('neighbourhood').mean()
st.write(avg_df)
# data['avg_price'] = data['price'].groupby('price').mean()
fig1 = px.line(data, x="Construction year", y="avg_price", color="neighbourhood group",
               title='Prijs per neighbourhood group in relatie tot bouwjaar')
# AttributeError: 'Figure' object has no attribute 'savefig'
# st.header("**Enkele dataset analyses**")
# st.markdown("Bijgaand dit hoofdstuk worden verschillende parameters met elkaar vergeleken")
st.plotly_chart(fig1)

####Correlation service fee


##data = df.to_csv('clean_df.csv')
