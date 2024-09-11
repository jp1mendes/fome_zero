#importando libraries
import pandas as pd
import numpy as np
import streamlit as st
import folium
from PIL import Image
import plotly.express as px 
from streamlit_folium import folium_static

#===========================================================================================

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

#===========================================================================================

st.set_page_config(
    page_title='Home',
    page_icon= '🎲')

image = Image.open('logo.png')
st.sidebar.image( image, width=120)

st.sidebar.markdown( '# Fome Zero!' )
st.sidebar.markdown( '### O melhor lugar para encontrar seu restaurante favorito!')
st.sidebar.markdown( """---""")

st.sidebar.markdown( '## Powered by João Paulo Mendes')

st.markdown( '# Fome Zero!' )
st.markdown( '### O melhor lugar para encontrar seu restaurante favorito!')
st.markdown( """---""")

st.markdown( '##### Veja os países que estão cadastrados em nossa plataforma!')

df = df.loc[ :, ['country_code', 'latitude', 'longitude']].groupby('country_code').median().reset_index()
map = folium.Map()
for index, location_info in df.iterrows():
    folium.Marker([location_info['latitude'], location_info['longitude']]).add_to(map)
folium_static(map, width=1024, height= 600 )

#st.markdown(
#    """ 
#    ### Como utilizar esse Dashboard?
#    - Visão dos Países:
#        - Visão gerencial: Métricas gerais de comportamento.
#        - Visão tática: Indicadores semanais de crescimento.
#        - Visão geográfica: Insights de goelocalização.
#    - Visão das Cidades: 
#        - Acompanhamento dos indicadores semanais de cresciemnto.
#    - Visão dos Restaurantes: Indicadores semanais de crescimento dos restaurantes.
#    ### Ask For Help: João Paulo Mendes 
#    """
#)