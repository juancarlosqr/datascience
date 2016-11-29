import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(range(3), index=['C','A','B'])
print(ser1)
'''
C    0
A    1
B    2
dtype: int64
'''

print(ser1.sort_index())
'''
A    1
B    2
C    0
dtype: int64
'''

print(ser1.sort_values())
'''
C    0
A    1
B    2
dtype: int64
'''

# ranking
from numpy.random import randn

ser2 = Series(randn(10))
print(ser2)
'''
0    1.290655
1    1.383484
2   -0.991176
3    0.144296
4    0.481288
5   -2.682719
6    0.593906
7    0.815368
8   -1.789567
9   -0.547529
dtype: float64
'''

print(ser2.sort_values())
'''
5   -2.682719
8   -1.789567
2   -0.991176
9   -0.547529
3    0.144296
4    0.481288
6    0.593906
7    0.815368
0    1.290655
1    1.383484
dtype: float64
'''

print(ser2.rank())
'''
0     9.0
1    10.0
2     3.0
3     5.0
4     6.0
5     1.0
6     7.0
7     8.0
8     2.0
9     4.0
dtype: float64
'''
