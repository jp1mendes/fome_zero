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


st.header( 'Visão dos Países 🌎')
st.markdown( """---""")
with st.container():
        st.markdown('#### Quantidade de restaurantes registrados no país')
        aux = df.loc[:, ['country_code', 'restaurant_name']].groupby('country_code').nunique().sort_values('restaurant_name', ascending=False).reset_index()
        fig = px.bar(aux, x='country_code', y='restaurant_name', color='country_code',labels={'country_code': 'País', 'restaurant_name': 'Quantidade de Restaurante' })
        st.plotly_chart(fig, use_container_width=True)

with st.container():
        st.markdown('#### Quantidade de cidades registradas por país')
        aux = df.loc[:, ['country_code', 'city']].groupby('country_code').nunique().sort_values('city', ascending=False).reset_index()
        fig = px.bar(aux, x='country_code', y='city', color='country_code', labels={'country_code': 'País', 'city': 'Quantidade de Cidade' })
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.markdown('#### Média de avaliações feitas por país')
        aux = df.loc[:, ['country_code', 'votes']].groupby('country_code').nunique().sort_values('votes', ascending=False).reset_index()
        aux = aux.iloc[0:5, :]
        fig = px.bar(aux, x='country_code', y='votes', color='country_code', labels={'country_code': 'País', 'votes': 'Número de Avaliações' })
        st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        st.markdown('#### Média de preço de um prato para duas pessoas por país')
        aux = df.loc[:, ['country_code', 'average_cost_for_two']].groupby('country_code').mean().sort_values('average_cost_for_two', ascending=False).reset_index()
        aux = aux.iloc[0:5, :]
        fig = px.bar(aux, x='country_code', y='average_cost_for_two', color='country_code', labels={'country_code': 'País', 'average_cost_for_two': 'preço do prato para duas pessoas' })
        st.plotly_chart(fig, use_container_width=True)