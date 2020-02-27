# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:58:23 2020

@author: ykrempp
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#---------- LOAD A DATASET

df = pd.read_csv('cells.csv', sep=';')

x_df = df.drop('cells', axis ='columns')
y_df = df.cells


#split the data into training set and test set
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.4, random_state=10)

print(x_train)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

prediction_test = model.predict(x_test)
print(y_test, prediction_test)
print('mean square error = ', np.mean(prediction_test-y_test)**2)

#residual plot
plt.scatter(prediction_test, prediction_test-y_test)
plt.hlines(y=0, xmin=200, xmax=310)