import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# https://en.wikipedia.org/wiki/NFL_win-loss_records

'''
reading data from clipboard fails on Linux because
pandas doesn't check if there's already a QApplication running
https://github.com/pandas-dev/pandas/issues/14372
'''
nfl_frame = pd.read_clipboard()

print(nfl_frame)

# columns names
print(nfl_frame.columns)

# get a single column
print(nfl_frame.Rank)

print(nfl_frame.Team)

print(nfl_frame['First Season'])

# get several columns
print(DataFrame(nfl_frame, columns=['Team', 'First Season', 'Total Games']))

# missing column
print(DataFrame(nfl_frame, columns=['Team', 'First Season', 'Stadium']))

# retrieve first few rows. default to first 5
print(nfl_frame.head())

# retrieve 3 first few rows
print(nfl_frame.head(3))

# retrieve last rows
print(nfl_frame.tail())

# get a specific row
print(nfl_frame.ix[3])
# miami dolphins info

# set values
nfl_frame['Stadium'] = "Levi's Stadium"
print(nfl_frame)

nfl_frame['Stadium'] = np.arange(5)
print(nfl_frame)

# add a series to a dataframe
stadiums = Series(["Levi's Stadium", 'AT&T Stadium'], index=[4,0])
nfl_frame['Stadium'] = stadiums
print(nfl_frame)

# delete columns
del nfl_frame['Stadium']
print(nfl_frame)

# create a dataframe from a dict
data = {'City': ['SF', 'LA', 'NYC'], 'Population': [837000, 3880000, 8400000]}
print(data)
# {'City': ['SF', 'LA', 'NYC'], 'Population': [837000, 3880000, 8400000]}

city_frame = DataFrame(data)
print(city_frame)
'''
  City  Population
0   SF      837000
1   LA     3880000
2  NYC     8400000
'''

print(city_frame.City)
'''
0     SF
1     LA
2    NYC
Name: City, dtype: object
'''

city_frame['State'] = Series(['California'], index=[0,1])
print(city_frame)
'''
  City  Population       State
0   SF      837000  California
1   LA     3880000  California
2  NYC     8400000         NaN
'''

city_frame['State'] = np.arange(3)
print(city_frame)
'''
  City  Population  State
0   SF      837000      0
1   LA     3880000      1
2  NYC     8400000      2
'''

del city_frame['State']
print(city_frame)
'''
  City  Population
0   SF      837000
1   LA     3880000
2  NYC     8400000
'''
