# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:52:02 2020

@author: ykrempp
"""


from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
from matplotlib import pyplot

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print(df.head())

fig, ax = pyplot.subplots(figsize=(15,10))
sns.scatterplot(df['sepal length (cm)'], df['target'])

# prepare the data

Y = df['target'].values
Y = Y.astype('int')

X = df.drop(labels = ['target'], axis = 1)

names = X.columns.values

# split the dataset in training and test

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=20)

# define the model

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

# test the model

prediction_test = model.predict(X_test)

# check the accuracy

from sklearn import metrics

print('accuracy is : ', metrics.accuracy_score(y_test, prediction_test))

#check the weights of each features :

print(model.coef_)


fig2, ax2 = pyplot.subplots(figsize=(10,10))
sns.heatmap(model.coef_, cmap='jet', annot=True)
