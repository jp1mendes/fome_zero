#importando libraries
import pandas as pd
import numpy as np
import streamlit as st
import folium
from PIL import Image
import plotly.express as px 

#==================================LIMPEZA DA BASE DE DADOS===================================================

dforiginal = pd.read_csv('zomato.csv')
df = dforiginal.copy()

#trocando os espaços dos nomes das colunas por underline e colocando tudo com letras minusculas
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()

#comando para apresentar todas as colunas da tabela
pd.set_option('display.max_columns', None)

#alterando o numeros da coluna country_code para os nomes dos paises correspondentes
df['country_code'] = df['country_code'].replace({
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America"})

#alterando o numeros da coluna rating_color para os nomes das cores correspondentes
df['rating_color'] = df['rating_color'].replace({
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred"})

#alterando o numeros da coluna price_range para os nomes das categorias correspondentes
df['price_range'] = df['price_range'].replace({
    1: "cheap",
    2: "normal",
    3: "expensive",
    4: "gourmet"})

#alterando a coluna cuisines para string pq tinha valores floats nos dados e em seguida foi separado os tipos de comida
#no caracter virgula e pegando apenas o primeiro tipo de comida
df['cuisines'] = df['cuisines'].astype(str)
df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

#===================================================================================================

#================================= barra lateral streamlit =========================================

image = Image.open('logo.png')
st.sidebar.image( image, width=120)

st.sidebar.markdown( '# Fome Zero!' )
st.sidebar.markdown( '### O melhor lugar para encontrar seu restaurante favorito!')
st.sidebar.markdown( """---""")

paises = st.sidebar.multiselect(
    'Selecione os países',
    ["India",
     "Australia",
     "Brazil",
     "Canada",
     "Indonesia",
     "New Zeland",
     "Philippines",
     "Qatar",
     "Singapure",
     "South Africa",
     "Sri Lanka",
     "Turkey",
     "United Arab Emirates",
     "England",
     "United States of America"],
    default= ["India",
     "Australia",
     "Brazil",
     "Canada",
     "Indonesia",
     "New Zeland",
     "Philippines",
     "Qatar",
     "Singapure",
     "South Africa",
     "Sri Lanka",
     "Turkey",
     "United Arab Emirates",
     "England",
     "United States of America"]
)

#filtro de países
linhas_selecionadas = df['country_code'].isin(paises)
df = df.loc[linhas_selecionadas, : ]

st.sidebar.markdown( """---""")
st.sidebar.markdown( '## Powered by João Paulo Mendes')

#===================================================================================================
#==================================== layout streamlit =============================================


st.header( 'Visão das Cidades 🏙️')
st.markdown( """---""")
with st.container():
        st.markdown('#### Cidades com mais restaurantes cadastrados')
        aux = df.loc[:, ['city', 'restaurant_name']].groupby('city').count().sort_values('restaurant_name', ascending=False).reset_index()
        aux = aux.iloc[0:9, :]
        fig = px.bar(aux, x='city', y='restaurant_name', color='city', labels={'city': 'Cidade', 'restaurant_name': 'nº de restaurantes' })
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.markdown('#### Quantidade de restaurantes com nota acima de 4.0 por cidade')
        aux = df.loc[df['aggregate_rating'] > 4.0, ['city', 'aggregate_rating']]
        aux = aux.loc[:, ['city', 'aggregate_rating']].groupby('city').count().sort_values('aggregate_rating', ascending=False).reset_index()
        aux = aux.iloc[0:9, :]
        fig = px.bar(aux, x='city', y='aggregate_rating', color='city',  labels={'city': 'Cidade', 'aggregate_rating': 'nº de restaurantes' })
        st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        st.markdown('#### Quantidade de restaurantes com nota abaixo de 2.5 por cidade')
        aux = df.loc[df['aggregate_rating'] < 2.5, ['city', 'aggregate_rating']]
        aux = aux.loc[:, ['city', 'aggregate_rating']].groupby('city').count().sort_values('aggregate_rating', ascending=False).reset_index()
        aux = aux.iloc[0:9, :]
        fig = px.bar(aux, x='city', y='aggregate_rating', color='city', labels={'city': 'Cidade', 'aggregate_rating': 'nº de restaurantes' })
        st.plotly_chart(fig, use_container_width=True)

with st.container():
        st.markdown('#### Cidades com mais restaurantes com tipos culinários distintos')
        aux = df.loc[:, ['city', 'cuisines']].groupby('city').nunique().sort_values('cuisines', ascending=False).reset_index()
        aux = aux.iloc[0:9, :]
        fig = px.bar(aux, x='city', y='cuisines', color='city',  labels={'city': 'Cidade', 'cuisines': 'nº de restaurantes' })
        st.plotly_chart(fig, use_container_width=True)

