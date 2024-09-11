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


st.header( 'Visão dos Restaurantes 🍽️')
st.markdown( """---""")
with st.container():
        st.markdown('#### Restaurantes com maior quantidade de avaliações')
        aux = df.loc[0:11, ['restaurant_name', 'votes']].groupby('restaurant_name').nunique().sort_values('votes', ascending=False).reset_index()
        aux = aux.iloc[0:11, 0]
        st.dataframe(aux)

with st.container():
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.markdown('#### Restaurantes com maior média de avaliações')
        aux = df.loc[:, ['restaurant_id', 'restaurant_name', 'aggregate_rating']].groupby('restaurant_name').max().sort_values('aggregate_rating', ascending=False).reset_index()
        aux = aux.loc[aux['aggregate_rating'] == 4.9, :].sort_values('restaurant_id').reset_index(drop=True)
        aux = aux.loc[:, ['restaurant_name', 'aggregate_rating']]
        st.dataframe(aux, width=1000, height=400)
            
    with col2:
        st.markdown('#### Restaurantes com menor média de avaliações')
        aux = df.loc[:, ['restaurant_id', 'restaurant_name', 'aggregate_rating', 'country_code']].groupby('restaurant_name').min().sort_values('aggregate_rating').reset_index()
        aux = aux.loc[aux['aggregate_rating'] == 0, :].sort_values('restaurant_id').reset_index(drop=True)
        aux = aux.loc[:, ['restaurant_name', 'aggregate_rating']]
        st.dataframe(aux, width=700, height=400)
