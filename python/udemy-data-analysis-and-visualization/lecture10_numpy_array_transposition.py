import numpy as np

arr = np.arange(50).reshape((10,5))
print(arr)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]
 [25 26 27 28 29]
 [30 31 32 33 34]
 [35 36 37 38 39]
 [40 41 42 43 44]
 [45 46 47 48 49]]
'''

# transposition
print(arr.T)

# dot product
print(np.dot(arr.T, arr))
'''
[[7125 7350 7575 7800 8025]
 [7350 7585 7820 8055 8290]
 [7575 7820 8065 8310 8555]
 [7800 8055 8310 8565 8820]
 [8025 8290 8555 8820 9085]]
'''

# 3d array
arr3d = np.arange(50).reshape((5,5,2))
print(arr3d)
'''
[[[ 0  1]
  [ 2  3]
  [ 4  5]
  [ 6  7]
  [ 8  9]]

 [[10 11]
  [12 13]
  [14 15]
  [16 17]
  [18 19]]

 [[20 21]
  [22 23]
  [24 25]
  [26 27]
  [28 29]]

 [[30 31]
  [32 33]
  [34 35]
  [36 37]
  [38 39]]

 [[40 41]
  [42 43]
  [44 45]
  [46 47]
  [48 49]]]
'''

# 3d array transposition
print(arr3d.transpose((1,0,2)))
'''
[[[ 0  1]
  [10 11]
  [20 21]
  [30 31]
  [40 41]]

 [[ 2  3]
  [12 13]
  [22 23]
  [32 33]
  [42 43]]

 [[ 4  5]
  [14 15]
  [24 25]
  [34 35]
  [44 45]]

 [[ 6  7]
  [16 17]
  [26 27]
  [36 37]
  [46 47]]

 [[ 8  9]
  [18 19]
  [28 29]
  [38 39]
  [48 49]]]
'''

# swapaxes
arr_s = np.array([[1,2,3]])
print(arr_s)
'''
[[1 2 3]]
'''

print(arr_s.swapaxes(0,1))
'''
[[1]
 [2]
 [3]]
'''