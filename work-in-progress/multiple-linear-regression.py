# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:23:02 2020

@author: ykrempp
"""


import pandas as pd

df = pd.read_excel('images_analyzed.xlsx')

# import seaborn as sns
# sns.lmplot(x='Time', y='Images_Analyzed', data=df, hue='Age')
# sns.lmplot(x='Coffee', y='Images_Analyzed', data=df, hue='Age')

from sklearn import linear_model
reg = linear_model.LinearRegression()

reg.fit(df[['Time', 'Coffee', 'Age']], df['Images_Analyzed']) # first 3 variables are independant, the last is the one that depends on all others

print(reg.coef_) # coefs = weights, the closest to 1 the more dependency there is. Age is not important here

print(reg.predict([[13, 2, 23]])) # predict the number of images analyzed using some variables: time = 13, coffee = 2, age = 23.