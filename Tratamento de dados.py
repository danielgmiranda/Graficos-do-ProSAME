import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

dados = pd.read_csv('IXRDProsame.csv')

# Ler as datas de entrada em cada carteira
data_admissao = pd.to_datetime(dados['Admissao'], dayfirst=True)
data_qualificacao = pd.to_datetime(dados['Qualificacao'], dayfirst=True)
data_habilitacao = pd.to_datetime(dados['Habilitacao'], dayfirst=True)
data_execucao = pd.to_datetime(dados['Execucao'], dayfirst=True)

diferenca_admissao_qualificacao = (data_qualificacao - data_admissao).dt.days

# Montando o gráfico 1
carteiras = dados['Carteira'].value_counts()

plt.figure(figsize=(8, 5))

plt.pie(
    carteiras.values,
    labels=carteiras.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribuição das propostas por carteiras")
plt.axis("equal")
plt.show()


