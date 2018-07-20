#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:49:10 2018

@author: jc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data preprocessing

# import dataset
dataset = pd.read_csv('salary_data.csv')
x = dataset.iloc[:, :-1].values
dependant_column_index = 1
y = dataset.iloc[:, dependant_column_index].values

# splitting dataset into training and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

# for simple linear regression, the library takes care of the feature scaling
# feature scaling
'''
from sklearn.preprocessing import StandardScaler
x_sc = StandardScaler()
x_train = x_sc.fit_transform(x_train)
x_test = x_sc.transform(x_test)
'''

# fitting simple linear regression to the training sets (x_train, y_train)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
# here the model is created, the model already learned from the data
# in terms of machine learning, that is "machine" equals to the 
# simple linear regression model and the "learning" process is when
# this model learned using the data provided to the fit method
regressor.fit(x_train, y_train)

# predicting values with test set (x_test)
y_pred = regressor.predict(x_test)

# visualizing the results

# plotting observation values
plt.scatter(x_train, y_train, color='red')
# plotting the regression line
# we use x_train in the predict method because we want
# to plotthe predictions for the training set
plt.plot(x_train, regressor.predict(x_train), color='green')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# plotting test values (prediction)
plt.scatter(x_test, y_test, color='red')
# we can keep the same values here because will result
# in the same model, the same line
plt.plot(x_train, regressor.predict(x_train), color='green')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
