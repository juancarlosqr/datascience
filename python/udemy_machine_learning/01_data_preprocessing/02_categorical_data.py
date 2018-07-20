d#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:53:20 2018

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
# that means changing values like
# France to 0, Germany to 1 and Spain to 2
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le_x = LabelEncoder()
x[:, 0] = le_x.fit_transform(x[:, 0])

# dummy variable encoding
# we need to dummy encode the country column because
# otherwise if we leave it like [0, 1, 2] the machine learning model
# could assume that the country with class 2 is more important than
# the country with class 1 and is not correct.
# So we create as many columns as classes we have, in this case
# 3 columns where each column's value will be 1 if belongs 
# to the observation for that particular country
ohe = OneHotEncoder(categorical_features=[0])
x = ohe.fit_transform(x).toarray()

# for y when don't use to use OneHotEncoder because the machine learning model
# will know the 'y' variable is a categorical data, since 'y' is
# the dependant variable
le_y = LabelEncoder()
y = le_y.fit_transform(y)