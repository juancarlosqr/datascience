#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 08:44:29 2018

@author: jc
"""

import numpy as np

# array 1
arr1 = np.array([1,2,3,4,5])

arr1
# array([1, 2, 3, 4, 5])

type(arr1)
# numpy.ndarray

arr1.dtype
# dtype('int64')

# use the ndim attribute for getting the axes
# use the size attribute to know the array length
# use the shape attribute to get its shape
arr1.ndim
# 1

arr1.size
# 5

arr1.shape
# (5,)

# array 2

arr2 = np.array([[1, 3], [2, 4], [3, 5]])

arr2

arr2.ndim
# 2

arr2.size
# 6

arr2.shape
# (3, 2)
