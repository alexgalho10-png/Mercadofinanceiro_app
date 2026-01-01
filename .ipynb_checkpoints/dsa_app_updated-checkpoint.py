
# Módulo Especial de Consultoria na Área de Dados com Agentes de IA
# Projeto Prático Para Consultoria na Área de Dados com Agentes de IA
# Deploy de App Para Day Trade Analytics em Tempo Real com Agentes de IA, Groq, DeepSeek e AWS Para Monetização

# Imports
import re
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from datetime import date

# Carrega o arquivo de variáveis de ambiente
load_dotenv()

########## Analytics ##########

# Usa o cache de dados do Streamlit para armazenar os resultados da função e evitar reprocessamento
# Define a função que extrai dados históricos de uma ação com base no ticker e período especificado
@st.cache_data
def dsa_extrai_dados(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date)
    return hist

# Interface Streamlit
st.title("Day Trade Analytics com IA")

# Opções de ações
opcoes = {
    "Microsoft": "MSFT",
    "Tesla": "TSLA",
    "Amazon": "AMZN",
    "Alphabet": "GOOG"
}
escolha = st.selectbox("Escolha uma ação", list(opcoes.keys()))
ticker = opcoes[escolha]

# Seleção de datas
data_inicial = st.date_input("Data Inicial", date(2024, 1, 1))
data_final = st.date_input("Data Final", date.today())

# Validação de datas
if data_inicial >= data_final:
    st.error("A data inicial deve ser anterior à data final.")
else:
    # Extração e exibição de dados
    dados = dsa_extrai_dados(ticker, start_date=data_inicial, end_date=data_final)
    st.write(f"Dados históricos de {escolha} entre {data_inicial} e {data_final}")
    st.dataframe(dados)
