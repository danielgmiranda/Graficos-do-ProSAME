import pandas as pd
import matplotlib.pyplot as plt
import squarify

dados = pd.read_csv('IXRDProsame.csv')

df = pd.DataFrame({'nb_people':[8,3,4,2], 'group':["group A", "group B", "group C", "group D"] })

# plot it
squarify.plot(sizes=df['nb_people'], label=df['group'], alpha=.8 )
plt.axis('off')
plt.show()