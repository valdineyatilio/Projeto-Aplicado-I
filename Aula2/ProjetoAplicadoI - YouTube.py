import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV com a codificação 'latin1'
url = "https://raw.githubusercontent.com/valdineyatilio/Projeto-Aplicado-I/main/Aula2/Dados%20YouTube.csv.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Visualizar as primeiras linhas do DataFrame
print(dados_youtube.head())

# Verificar informações sobre as colunas e tipos de dados
print(dados_youtube.info())

# Resumo estatístico das variáveis numéricas
print(dados_youtube.describe())

