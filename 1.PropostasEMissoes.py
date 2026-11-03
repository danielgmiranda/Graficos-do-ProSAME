import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

dados = pd.read_csv('IXRDProsame.csv')

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