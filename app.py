import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizza.csv")


modelo = LinearRegression()

x = df[['diametro']]

y = df[['preco']]

modelo.fit(x, y)

st.title('Prevendo o valor de uma pizza')

st.divider()

diametro =st.number_input('Digite o tamanho do diâmetro da pizza')

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'o valor da pizza com diâmetro de {diametro: .0f} cm é de R$ {preco_previsto: .2f}')

