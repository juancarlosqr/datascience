import pandas as pd
from pandas import Series

obj = Series([3,6,9,12])

print(obj)
'''
0     3
1     6
2     9
3    12
dtype: int64
'''

print(obj.values)
# [ 3  6  9 12]

print(obj.index)
# RangeIndex(start=0, stop=4, step=1)

# world war 2 casualties
ww2_cas = Series([8700000, 4300000, 3000000, 2100000, 400000], index=['USSR', 'Germany', 'China', 'Japan', 'USA'])
print(ww2_cas)
'''
USSR       8700000
Germany    4300000
China      3000000
Japan      2100000
USA         400000
dtype: int64
'''

print(ww2_cas['Japan'])
# 2100000

# check which countries had cas greater than 4M
print(ww2_cas[ww2_cas > 4000000])
'''
USSR       8700000
Germany    4300000
dtype: int64
'''

# behave as dictionary
print('USSR' in ww2_cas)
# True

# convert to dictionary

ww2_dict = ww2_cas.to_dict()
print(ww2_dict)
# {'China': 3000000, 'USSR': 8700000, 'Germany': 4300000, 'USA': 400000, 'Japan': 2100000}

# convert back to series
ww2_series = Series(ww2_dict)
print(ww2_series)
'''
China      3000000
Germany    4300000
Japan      2100000
USA         400000
USSR       8700000
dtype: int64
'''

countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Venezuela']
obj2 = Series(ww2_dict, index=countries)
print(obj2)
'''
China        3000000.0
Germany      4300000.0
Japan        2100000.0
USA           400000.0
USSR         8700000.0
Venezuela          NaN
dtype: float64
'''

# using pandas to check null values
print(pd.isnull(obj2))
'''
China        False
Germany      False
Japan        False
USA          False
USSR         False
Venezuela     True
dtype: bool
'''

# using pandas to check not null values
print(pd.notnull(obj2))
'''
China         True
Germany       True
Japan         True
USA           True
USSR          True
Venezuela    False
dtype: bool
'''

# adding series. sort by index automatically
print(ww2_series + obj2)
'''
China         6000000.0
Germany       8600000.0
Japan         4200000.0
USA            800000.0
USSR         17400000.0
Venezuela           NaN
dtype: float64
'''

# name a series
obj2.name = 'World War 2 Casualties'
print(obj2)
'''
China        3000000.0
Germany      4300000.0
Japan        2100000.0
USA           400000.0
USSR         8700000.0
Venezuela          NaN
Name: World War 2 Casualties, dtype: float64
'''

obj2.index.name = 'Countries'
print(obj2)
'''
Countries
China        3000000.0
Germany      4300000.0
Japan        2100000.0
USA           400000.0
USSR         8700000.0
Venezuela          NaN
Name: World War 2 Casualties, dtype: float64
'''
