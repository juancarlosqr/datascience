#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:25:26 2018

@author: jc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data preprocessing

# import dataset
dataset = pd.read_csv('data.csv')
x = dataset.iloc[:, :-1].values
dependant_column_index = 3
y = dataset.iloc[:, dependant_column_index].values

# splitting dataset into training and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# feature scaling
'''
from sklearn.preprocessing import StandardScaler
x_sc = StandardScaler()
x_train = x_sc.fit_transform(x_train)
x_test = x_sc.transform(x_test)
'''
