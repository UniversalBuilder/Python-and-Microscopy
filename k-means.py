# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:59:47 2020

@author: ykrempp
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('seaborn-talk')
fig, ax = plt.subplots(figsize=(20,20))

df = pd.read_excel('kmeans.xlsx')

sns.regplot(x=df['X'], y=df['Y'])

from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)

model = km.fit(df)

predictions = km.predict(df)

fig2, ax2 = plt.subplots(figsize=(20,20))

plt.scatter(df['X'], df['Y'], c=predictions, s=100, cmap='viridis')
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], s= 300, c='red', alpha=0.5)