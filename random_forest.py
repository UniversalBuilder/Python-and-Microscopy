# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:02:55 2020

@author: ykrempp
"""


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('images_analyzed_productivity1.csv')

#check balance
sizes = df['Productivity'].value_counts(sort=1)
print(sizes)

#ML : predict dependant variable (productivity), from independant variables

# Clean up Data
# > drop irrelevant data
df.drop(['Images_Analyzed'], axis=1, inplace=True) # same as df = df.drop(['Images_Analyzed'], axis=1)
df.drop(['User'], axis=1, inplace=True)

# > handle missing values
df = df.dropna()


# > convert non numeric data to numeric
df.Productivity[df.Productivity == 'Good'] = 1 # select values from 'Productivity' column in df where value = 'Good' and set it to 1
df.Productivity[df.Productivity == 'Bad'] = 2

# > check 
print(df.head())

#Define variables --> must be in integer type

Y = df['Productivity'].values.astype('int') # Y is dependant variable
X = df.drop(labels=['Productivity'], axis=1) # X is independant variables

# split the dataset in train and test

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=20) #keeps the randomness the same (= same set of random values)

#get the model and train it, then predict

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=10, random_state=30)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

#check accuracy
from sklearn import metrics
print('Accuracy = ', metrics.accuracy_score(Y_test, Y_pred))

#check feature relevance

feature_list = list(X.columns)
feature_relevance = pd.Series(model.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_relevance)