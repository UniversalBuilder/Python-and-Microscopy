# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:22:18 2020

@author: ykrempp
"""

#data grouping - group by

import pandas as pd
df = pd.read_csv('manual_vs_auto.csv')

df = df.rename(columns = {'Unnamed: 0': 'Image_Set'})
print(df.head())

df = df.drop('Manual2', axis = 1)
print(df.head())

#group by

group_df = df.groupby(by=['Image_Set'])
data_count_df = group_df.count()
data_avg_df = group_df.mean()
 

print(data_count_df)
print(data_avg_df)


#check correlation overall
print(df.corr())

#check correlation between 2 columns
print(df['Manual'].corr(df['Auto_th_2']))

