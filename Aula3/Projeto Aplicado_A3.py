import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados da URL com a codificação correta
url = "https://raw.githubusercontent.com/valdineyatilio/Projeto-Aplicado-I/main/Aula3/Global%20YouTube%20Statistics%20.csv"
dados = pd.read_csv(url)

# Verificar as primeiras linhas do DataFrame
print(dados.head())

# Vamos verificar os nomes das colunas
print(dados.columns)

# Gráfico 1: Histograma das visualizações
plt.figure(figsize=(10, 6))
plt.hist(dados['video views'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma de Visualizações')
plt.xlabel('Visualizações')
plt.ylabel('Contagem')
plt.grid(True)
plt.show()

# Gráfico 2: Gráfico de dispersão de visualização vs. país
plt.figure(figsize=(10, 6))
plt.scatter(dados['video views'], dados['country_rank'], alpha=0.5, color='green')
plt.title('Visualização vs País')
plt.xlabel('Visualização')
plt.ylabel('País')
plt.grid(True)
plt.show()

# Gráfico 3: Gráfico de barras do número de vídeos por categoria
plt.figure(figsize=(10, 6))
dados['category'].value_counts().plot(kind='bar', color='orange')
plt.title('Número de Vídeos por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Rank')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()