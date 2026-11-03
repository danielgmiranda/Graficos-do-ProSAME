import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

dados = pd.read_csv('IXRDProsame.csv')

categorias = dados['Categoria'].value_counts()

plt.figure(figsize=(8, 5))

plt.pie(
    categorias.values,
    labels=categorias.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribuição dos registros por categoria")
plt.axis("equal")
plt.show()