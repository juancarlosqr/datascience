#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:43:48 2018

@author: jc
"""

import pandas as pd

# import dataset
dataset = pd.read_csv('data.csv')
x = dataset.iloc[:, :-1].values
dependant_column_index = 3
y = dataset.iloc[:, dependant_column_index].values

# handle missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(x[:, 1:dependant_column_index])
x[:, 1:dependant_column_index] = imputer.transform(x[:, 1:dependant_column_index])

# encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le_x = LabelEncoder()
x[:, 0] = le_x.fit_transform(x[:, 0])
ohe = OneHotEncoder(categorical_features=[0])
x = ohe.fit_transform(x).toarray()
le_y = LabelEncoder()
y = le_y.fit_transform(y)

# splitting dataset into training and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
