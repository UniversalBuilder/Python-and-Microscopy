# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:19:52 2020

@author: ykrempp
"""

#Data Sorting

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

#get info on the DF
print(df.head())
print(df.describe())

#sort DF based on 'Manual' column
df_sorted = df.sort_values('Manual', ascending=True)

#print subset of columns to check the sorting
print(df_sorted[['Manual', 'Auto_th_2']].head())


#print a susbet of rows
print(df[20:30])

#use loc (inclusive !) to select some rows and columns
print(df.loc[20:30, ['Manual', 'Auto_th_2']])

#select rows using the row value : create a df from the date of df['Unnamed: 0'] where the value is 'Set2'
df_set2 = df[df['Unnamed: 0'] == 'Set2']
print(df_set2)

#get the max values
print(max(df_set2['Manual']))

#check values greater than --> you get booleans
print(df['Manual'] > 100)

#get values greater than --> you get the values
print(df[df['Manual'] > 100])

#get values greater than AND smaller than --> you get the values
print( df[ (df['Manual'] > 100) & (df['Auto_th_2'] <80)] )

#iterate through rows
for index, row in df.iterrows():
    average_auto = (row['Auto_th_2']+row['Auto_th_3']+row['Auto_th_4'])/3
    print(round(average_auto), ' | ', row['Manual'])
    
