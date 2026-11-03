import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

dados = pd.read_csv('IXRDProsame.csv')

TipoDeProponente = dados['Tipo'].value_counts()

plt.figure(figsize=(8, 5))

#comentário no bloco inteiro: ctrl + ;
# plt.pie(
#    TipoDeProponente.values,
#    labels=TipoDeProponente.index,
#    autopct="%1.1f%%",
#    startangle=90
# )

plt.title("Distribuição dos tipos de proponentes")
plt.axis("equal")
plt.show()