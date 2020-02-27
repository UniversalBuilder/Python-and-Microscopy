# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:34:37 2020

@author: ykrempp
"""


import pandas as pd
import numpy as np
import matplotlib


df = pd.read_csv('manual_vs_auto.csv')
#check if there are NaNs
print(df.isnull())

#drop column without data
df2 = df.drop('Manual2', axis = 1)
print(df2)

# drop rows with NaN
df3 = df2.dropna()
print(df3)

#check how the DF looks like
print(df['Manual'].describe())

#fill Nans with the mean value or any other value
df4 = df['Manual'].fillna(1000000, inplace=False)
print(df4.head(25))

#♣fill with a calculated mean (here watch row 12)
df5 = df['Manual'] = df.apply(lambda row: (round((row['Auto_th_2']+row['Auto_th_3']+row['Auto_th_4'])/3)) if np.isnan(row['Manual']) else row['Manual'], axis=1)
print(df5.head(25))

#plotting


#df['Manual'].plot()
df['Manual'].plot(kind ='hist', bins = 30, title='Manual Count', figsize=(12,10))