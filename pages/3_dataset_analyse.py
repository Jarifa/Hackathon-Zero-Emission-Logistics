#######packages

import pandas as pd
import numpy as np
import plotly
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# comment
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


# Price tegenover bouwjaar
data = pd.read_csv('clean_df.csv')

##Corr
fig, ax = plt.subplots()
sns.heatmap(data[['host_identity_verified', 'neighbourhood group', 'neighbourhood', 'instant_bookable',
                  "cancellation_policy", "room type", "Construction year", "price", "minimum nights",
                  "number of reviews", "review rate number", "calculated host listings count",
                  "availability 365"]].corr(), ax=ax, vmin=0, vmax=1, cmap='YlBu')
st.write(fig)

fig, ax = plt.subplots()
sns.heatmap(data[['host_identity_verified', 'neighbourhood group', 'neighbourhood', 'instant_bookable',
                  "cancellation_policy", "room type", "Construction year", "price", "minimum nights",
                  "number of reviews", "review rate number", "calculated host listings count",
                  "availability 365"]].corr(), ax=ax, vmin=-1, vmax=0, cmap='RdYl')
st.write(fig)

# Boxplot van prijzen per borough
Boxplot = px.box(data_frame=data, x='neighbourhood group', y='price')
st.markdown('**Barplot**')
st.plotly_chart(Boxplot)

# Histogram van gemiddelde prijs per neighbourhood group (beter leesbaar)
avg_df = data[['neighbourhood group', 'price']].groupby('neighbourhood group').mean().reset_index()
st.write(avg_df)
fig1 = px.histogram(avg_df, x='neighbourhood group', y="price", color=avg_df.index,
                    title='Prijs per neighbourhood group',
                    histfunc='avg',
                    range_y=[600, 650])

st.markdown('Een visualisatie over de gemiddelde prijs van de stadsdelen van New York. Interessant hieraan is dat'
            'de gemiddelde prijs van de stadsdelen vrijwel gelijk zijn')
st.plotly_chart(fig1)

# scatterplot van percentage service fee tegenover prijs, hierin is te zien dat er 5 verschillende 'categorien' zijn om uit te kiezen
Figscatter = px.scatter(data, x="serv_fee_perc", y="price", color='neighbourhood',
                        title='Percentage service fee tegenover prijs')
st.markdown(
    "Een scatterplot over de service fee per Neighbourhood, het valt direct op dat duidelijk patroon is de visualisatie Dit heeft"
    " Dit heeft ermee te maken dat er verschillende service fees zijn.")
st.plotly_chart(Figscatter)

Figscatter2 = px.scatter(data, x="price", y="service fee", color='neighbourhood', title='Service fee tegenover prijs')
st.plotly_chart(Figscatter2)

####Correlation service fee
regressie = px.scatter(data, x="Construction year",
                       y="price",
                       color='neighbourhood group',
                       title='Regression Bouwjaar/prijs',
                       trendline='ols')
st.markdown("**REGRESSION**")
st.markdown("Model bouwjaar tegenover de prijs, een bijbehorende correlatie.")

st.plotly_chart(regressie)

####Correlation distance tot "centrum" (The Battery als centre point)
"""regressie = px.scatter(data, x="dist",
                       y="price",
                       color='neighbourhood group',
                       title='Regression distance to centrum/prijs',
                       trendline='ols')"""
# st.markdown("**REGRESSION**")

# st.plotly_chart(regressie)
regressie = px.scatter(data[data['availability 365'] <= 365], x="minimum nights",
                       y="price",
                       title='Regression',
                       trendline='ols',
                       opacity=0.05,
                       trendline_color_override='red'
                       )
st.plotly_chart(regressie)

a = px.get_trendline_results(regressie).px_fit_results.iloc[0].rsquared
st.write('R squared: ', a)

results = px.get_trendline_results(regressie)
line_coeff = results.iloc[0]["px_fit_results"].params
st.write('lijn: ', line_coeff[1], 'x + ', line_coeff[0])
