import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

points = np.arange(-5,5,0.01)
dx,dy = np.meshgrid(points, points)

print(dx)
'''
[[-5.   -4.99 -4.98 ...,  4.97  4.98  4.99]
 [-5.   -4.99 -4.98 ...,  4.97  4.98  4.99]
 [-5.   -4.99 -4.98 ...,  4.97  4.98  4.99]
 ..., 
 [-5.   -4.99 -4.98 ...,  4.97  4.98  4.99]
 [-5.   -4.99 -4.98 ...,  4.97  4.98  4.99]
 [-5.   -4.99 -4.98 ...,  4.97  4.98  4.99]]
'''

print(dy)
'''
[[-5.   -5.   -5.   ..., -5.   -5.   -5.  ]
 [-4.99 -4.99 -4.99 ..., -4.99 -4.99 -4.99]
 [-4.98 -4.98 -4.98 ..., -4.98 -4.98 -4.98]
 ..., 
 [ 4.97  4.97  4.97 ...,  4.97  4.97  4.97]
 [ 4.98  4.98  4.98 ...,  4.98  4.98  4.98]
 [ 4.99  4.99  4.99 ...,  4.99  4.99  4.99]]
'''

# plot
z = (np.sin(dx) + np.sin(dy))
print(z)
'''
[[  1.91784855e+00   1.92063718e+00   1.92332964e+00 ...,  -8.07710558e-03
   -5.48108704e-03  -2.78862876e-03]
 [  1.92063718e+00   1.92342581e+00   1.92611827e+00 ...,  -5.28847682e-03
   -2.69245827e-03  -5.85087534e-14]
 [  1.92332964e+00   1.92611827e+00   1.92881072e+00 ...,  -2.59601854e-03
   -5.63993297e-14   2.69245827e-03]
 ..., 
 [ -8.07710558e-03  -5.28847682e-03  -2.59601854e-03 ...,  -1.93400276e+00
   -1.93140674e+00  -1.92871428e+00]
 [ -5.48108704e-03  -2.69245827e-03  -5.63993297e-14 ...,  -1.93140674e+00
   -1.92881072e+00  -1.92611827e+00]
 [ -2.78862876e-03  -5.85087534e-14   2.69245827e-03 ...,  -1.92871428e+00
   -1.92611827e+00  -1.92342581e+00]]
'''
plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x) + sin(y)')

# numpy where
A = np.array([1,2,3,4])
B = np.array([101,201,301,401])
condition = np.array([True, True, False, False])
zipped = zip(A, B, condition)
print(zipped)
# [(1, 101, True), (2, 201, True), (3, 301, False), (4, 401, False)]
answer = [(A_val if cond else B_val) for A_val, B_val, cond in zipped]
print(answer)
# [1, 2, 301, 401]

answer2 = np.where(condition, A, B)
print(answer2)
# [  1   2 301 401]

# randn
from numpy.random import randn
arr = randn(5,5)
print(arr)
'''
[[ 0.17320146 -0.46911024 -1.0651496   0.70576956 -1.61522824]
 [ 2.0189644  -1.48538496 -1.08436758 -0.2901194  -0.42813813]
 [ 0.07606838 -0.82985605 -0.22330565 -0.72953412  0.43321977]
 [ 0.59338546 -0.41383446 -0.49838157  0.45367848 -0.08548791]
 [ 1.75803241 -0.91517365  0.05230675 -0.53317636  0.20016208]]
'''

print(np.where(arr < 0, 0, arr))
'''
[[ 0.17320146  0.          0.          0.70576956  0.        ]
 [ 2.0189644   0.          0.          0.          0.        ]
 [ 0.07606838  0.          0.          0.          0.43321977]
 [ 0.59338546  0.          0.          0.45367848  0.        ]
 [ 1.75803241  0.          0.05230675  0.          0.20016208]]
'''

# basic statistics operation
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(arr.sum())
# 45
print(arr.sum(0))
# [12 15 18]
print(arr.sum(1))
# [ 6 15 24]
print(arr.mean())
# 5.0
print(arr.std()) # standard deviation
# 2.58198889747
print(arr.var()) # variance
# 6.66666666667
bool_arr = np.array([True, False, True])
print(bool_arr.any()) # True if at least one element is True
# True
print(bool_arr.all()) # True if all elements are True
# False


# sort
arr = randn(5)
print(arr)
# [-0.25335915  1.76739519  0.86180743  1.56030563 -1.94745903]
arr.sort()
print(arr)
# [-1.94745903 -0.25335915  0.86180743  1.56030563  1.76739519]

# unique
countries = np.array(['France', 'Germany', 'USA', 'Russia', 'USA', 'Venezuela', 'Russia'])
print(np.unique(countries))
# ['France' 'Germany' 'Russia' 'USA' 'Venezuela']

# in1d
print(np.in1d(['France', 'USA', 'Sweden'], countries))
# [ True  True False]
