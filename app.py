# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 13:10:58 2022

@author: admin
"""
#Importation des modules
import pandas as pd
import streamlit as st
from gsheetsdb import connect

#Importation de notre base de données
df = pd.read_csv("D:/stage/streamlit/world-happiness-report-2021.csv")

#Ajout titre
st.sidebar.title("World Happiness Index 2021:")

#Ajout image
st.image("https://images.pexels.com/photos/573259/pexels-photo-573259.jpeg?cs=srgb&dl=pexels-matheus-bertelli-573259.jpg&fm=jpg", caption='World Happiness Dataset')

#Ajout de la base de données
st.write(df)

#Filtrage des pays
#Country Select Filter
country_list = ["All","Western Europe", "South Asia", "Southeast Asia", "East Asia", "North America and ANZ","Middle East and North Africa", "Latin America and Caribbean","Central and Eastern Europe","Commonwealth of Independent States","Sub-Saharan Africa"]
select = st.sidebar.selectbox('Filter the region here:', country_list, key='1')
if select =="All":
    filtered_df = df
else:
    filtered_df = df[df['Regional indicator']==select]
#Ladder Score Slider
score = st.sidebar.slider('Select min Ladder Score', min_value=5, max_value=10, value = 10) # Getting the input.
df = df[df['Ladder score'] <= score] # Filtering the dataframe

#Line Chart
st.line_chart(data=None, width=0, height=0, use_container_width=True)
#Area Chart
st.area_chart(data=None, width=0, height=0, use_container_width=True)

import plotly.express as px
import seaborn as sns
import matplotlib.pyplot  as plt
#Scatter Chart
fig = px.scatter(df,
x="Logged GDP per capita",
y="Healthy life expectancy",
size="Ladder score",
color="Regional indicator",
hover_name="Country name",
size_max=10)
st.write(fig)
#Bar Chart, you can write in this way too
st.write(px.bar(df, y='Ladder score', x='Country name'))
#Seaborn Heatmap
#correlate data
corr = df.corr()
#using matplotlib to define the size
plt.figure(figsize=(8, 8))

#creating the heatmap with seaborn
fig1 = plt.figure()
ax = sns.heatmap(corr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(20, 220, n=200),
square=True
)
ax.set_xticklabels(
ax.get_xticklabels(),
rotation=45,
horizontalalignment='right'
);
st.pyplot(fig1)

#deploiement via googlesheet
gsheet_url = "https://docs.google.com/spreadsheets/d/1kikXtK7UIjQkzkUWxEB922PS9GuWtukeI9fwRykXekA/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = df
st.write(df_gsheet)
