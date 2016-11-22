from __future__ import division
import sys
import numpy as np

print(sys.version)
# 2.7.11 | 64-bit | (default, Jun 11 2016, 10:32:30) 
# [GCC 4.1.2 20080704 (Red Hat 4.1.2-55)]

print(5/2)
# 2.5
# for python 2.7 prints 2
# for python 3.* prints 2.5
# importing division from future fix this

arr1 = np.array([[1,2,3,4],[6,7,8,9]])
print(arr1)
'''
[[1 2 3 4]
 [6 7 8 9]]
'''

print(arr1 * arr1)
'''
[[ 1  4  9 16]
 [36 49 64 81]]
'''

print(arr1 - arr1)
'''
[[0 0 0 0]
 [0 0 0 0]]
'''

# scalars
print(1 / arr1)
'''
[[ 1.          0.5         0.33333333  0.25      ]
 [ 0.16666667  0.14285714  0.125       0.11111111]]
'''

print(arr1 * 2)
'''
[[ 2  4  6  8]
 [12 14 16 18]]
'''

# exponential
print(arr1 ** 3)
'''
[[  1   8  27  64]
 [216 343 512 729]]
'''