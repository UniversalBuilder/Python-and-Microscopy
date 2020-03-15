# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:55:38 2020

@author: ykrempp
"""

#deal with rows and columns, save a CSV

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

#drop columns

df1 = df.drop('Manual2', axis=1)
print(df.head())
print(df1.head())

df2 = df.drop(['Manual2','Auto_th_2'], axis =1)
print(df2.head())

#adding columns

df['Date'] = '2020-30-01'

print(df.dtypes)
print(df.head())

#adding a real date not a string (object)

df['RealDate'] = pd.to_datetime('2020-01-30')
print(df.dtypes)
print(df.head())

#export the result to csv

df.to_csv('manual_vs_auto_updated_by_python.csv')

#delete specific rows

df2 = df.drop(df.index[1])
print(df2.head())

#build a new df with only rows where unnamed is different from set 1

df3 = df[df['Unnamed: 0'] !='Set1']

print(df3.head())