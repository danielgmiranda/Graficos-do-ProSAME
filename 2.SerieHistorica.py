import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

dados = pd.read_csv('IXRDProsame.csv')

data_admissao = pd.to_datetime(dados['Admissao'], dayfirst=True)
data_qualificacao = pd.to_datetime(dados['Qualificacao'], dayfirst=True)
data_habilitacao = pd.to_datetime(dados['Habilitacao'], dayfirst=True)
data_execucao = pd.to_datetime(dados['Execucao'], dayfirst=True)

irdo = pd.to_datetime('01/01/2023', dayfirst= True)
iRDO_count = 0

for date in data_admissao:
    if pd.notna(date) and date < irdo:
        iRDO_count = iRDO_count + 1

print(iRDO_count)

iniciais = dados['Admissao'].value_counts()
