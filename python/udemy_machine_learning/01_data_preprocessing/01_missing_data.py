u#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:13:21 2018

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
