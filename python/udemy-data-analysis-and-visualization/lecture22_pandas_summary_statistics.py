'''
sum
min
idxmin
max
idxmax
cumsum
describe
'''
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1 = DataFrame(arr, index=['A','B'], columns=['One','Two','Three'])
print(dframe1)
'''
   One  Two  Three
A  1.0  2.0    NaN
B  NaN  3.0    4.0
'''

# sum
print(dframe1.sum())
'''
One      1.0
Two      5.0
Three    4.0
dtype: float64
'''

print(dframe1.sum(axis=1))
'''
A    3.0
B    7.0
dtype: float64
'''

# min
print(dframe1.min())
'''
One      1.0
Two      2.0
Three    4.0
dtype: float64
'''

# index of min value
print(dframe1.idxmin())
'''
One      A
Two      A
Three    B
dtype: object
'''

# acumulation
print(dframe1.cumsum())
'''
   One  Two  Three
A  1.0  2.0    NaN
B  NaN  5.0    4.0
'''

# describe
print(dframe1)
'''
   One  Two  Three
A  1.0  2.0    NaN
B  NaN  3.0    4.0
'''
print(dframe1.describe())
'''
       One       Two  Three
count  1.0  2.000000    1.0
mean   1.0  2.500000    4.0
std    NaN  0.707107    NaN
min    1.0  2.000000    4.0
25%    1.0  2.250000    4.0
50%    1.0  2.500000    4.0
75%    1.0  2.750000    4.0
max    1.0  3.000000    4.0
'''

# check for unique values
ser1 = Series(['w','y','a','w','y','z','b','q','w','g','h'])

print(ser1)
'''
0     w
1     y
2     a
3     w
4     y
5     z
6     b
7     q
8     w
9     g
10    h
dtype: object
'''

print(ser1.unique())
'''
dtype: object
['w' 'y' 'a' 'z' 'b' 'q' 'g' 'h']
'''

# count values
print(ser1.value_counts())
'''
w    3
y    2
q    1
g    1
z    1
h    1
b    1
a    1
dtype: int64
'''
