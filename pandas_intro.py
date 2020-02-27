# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pandas as pd
# df = pd.read_csv('./Measurements_DetectedCells.csv')

# df['AreaShape_Area'].plot(kind='hist', title='Area', bins=50)

# data = [[10,200,60],
#         [12,155,45],
#         [9,50,-45.],
#         [16,240,90]]


# df2 = pd.DataFrame(data, index=[1,2,3,4], columns=['Area', 'Intensity', 'Orientation'])
# print(df2)

df3 = pd.read_csv('./manual_vs_auto.csv')

#print info about df3

print(df3.info())
print(df3.shape)
print(df3)

print(df3.head())
print(df3.tail(7))

#change index - must use unique values, like primary keys in DBs

df_new = df3.set_index('Image')
print(df_new.head())

#show columns
print(df_new.columns)

#print each unique instance in firt column

print(df3['Unnamed: 0'].unique())

#rename a column

df_ren = df3.rename(columns = {'Unnamed: 0':'Image_set'})
print(df_ren)

#isolate a column and print it

df_col = (df_ren['Manual'])
print(df_col)

#gives an overview of the dataset
print(df_ren.describe())