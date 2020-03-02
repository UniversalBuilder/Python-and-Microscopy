# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#get data

df = pd.read_excel('concentrations.xlsx', sep =',')

#set figure syze and style

fig, ax = plt.subplots(1,1, figsize=(10,6))
plt.style.use('seaborn-paper')

 
#plot

sns.lineplot(x=df['c1'], y=df['rho'], color='red')
sns.regplot(x=df['c1'], y=df['rho'], marker='+', scatter_kws={"color":"red"}, fit_reg=True)

# Add titles

plt.title('Evolution de la concentration massique en fonction de la masse volumique de la solution mère')
plt.xlabel("C1 en g.$L^-1$")
plt.ylabel("\u03C1 en g.$L^-1$")
plt.savefig('robin_krempp-concentration-massique.png')
