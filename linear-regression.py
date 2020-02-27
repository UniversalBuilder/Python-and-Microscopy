# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:47:43 2020

@author: ykrempp
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#---------- LOAD A DATASET

df = pd.read_csv('cells.csv', sep=';')
print(df)

# plt.xlabel('time')
# plt.xlabel('cells')
# plt.scatter(df.time, df.cells, color='red', marker='+')

#------   CONVENTIONS
# x IS independant (time)
# y IS dependant - we are predicting y


# format the dataset to separate th variable

x_df = df.drop('cells', axis ='columns')
print(x_df)

#---------------
#warning : you can also create your series using this but beware of double brackets [[]]

#x2_df = df[['time']]
#print(x2_df.dtypes) # you need dtypes as objects

#x2_df = df['time']
#print(x2_df.dtypes)
#---------------

y_df = df.cells
print(y_df)

# MODEL CREATION AND FITTING == TRAINING

reg = linear_model.LinearRegression() #creates an instance of the model

reg.fit(x_df, y_df) #training the model (fitting the line)

#PREDICTION FOR ONE VALUE

target = 5.7
print(f"Predicted nbrs cells for time = {target}: ", reg.predict([[target]]))


#SCORING THE MODEL

print("Score of the model : ", reg.score(x_df, y_df)) # score of 1 is perfect match

#get curve parameters

c = reg.intercept_ # => ordonnée à l'origine
m = reg.coef_ # => pente

print("From a manual calculation: ", (m*target + c))

#PREDICTION FOR A LIST OF VALUES

#now we can apply the model to different dataset : here is a list of time points in a csv file
cells_predict_df = pd.read_csv('cells_predicted.csv', sep=';')
print(cells_predict_df)

#apply the model
predicted_cells = reg.predict(cells_predict_df)
print(predicted_cells)

#add a column to our dataframe with the predicted values
cells_predict_df['cells'] = predicted_cells
print(cells_predict_df)

#save the final output to a csv file
cells_predict_df.to_csv('predicted_cells.csv')