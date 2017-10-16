#!/usr/bin/env python3

import os, glob, time
import r1d5_functions_basics

def run_main():
    ''''''
    list_a = [1, 2, 3, 4]
    list_b = [10, 20, 30, 40]
    print('\nlists')
    print(1, list_a * 5)
    print(2, list_a + list_b)
    print('\ndicts')
    friends = {'mike': 28, 'john': 31, 'julia': 26}
    print(1, friends)
    one = friends.popitem()
    print(2, friends)
    print(3, one)
    keys = friends.keys()
    values = friends.values()
    print(4, keys, type(keys))
    for k in keys:
        print(k, end=' ')
    print()
    print(5, values, type(values))
    for v in values:
        print(v, end=' ')
    print()
    print(6, friends.get('john'))

def run_conversion():
    ''''''
    print('\nconversion')
    print(1, int(12.0))
    print(2, int(12.5))
    print(3, float(10))
    print(4, float(15.2))
    print(5, int('10'))
    print(6, float('12'))
    # print(7, int('hi')) # ValueError: invalid literal for int() with base 10: 'hi'
    print(8, str(20))
    print(9, str(5.5))
    print(10, round(23.87630, 2))
    print(11, round(23.27630))
    print(12, round(23.87630))

def get_prime_sum_until_num(num):
    ''''''
    print('\nget_prime_sum_until_num', num)
    result = []
    for n in range(1, num + 1):
        prime = [i for i in range(1, n + 1) if n % i == 0]
        if len(prime) <= 2:
            result.append(n)
    print(result)
    print(sum(result))

def run_os():
    ''''''
    print('\nros')
    cwd = os.getcwd()
    print(1, cwd)
    os.chdir('/Users/juancarlosqr/code/datascience')
    print(2, os.getcwd())
    path = os.path.join('/Users/juancarlosqr/code/empty', 'main.py')
    print(3, path)
    print(4, os.path.expanduser('~'))
    print(5, os.path.join(os.path.expanduser('~'), 'code', 'empty', 'run.py'))
    print(6, path.split('/')) # not what I was looking for but nice
    dirname, filename = os.path.split(path)
    print(7, dirname, filename)
    shortname, extension = os.path.splitext(filename)
    print(8, shortname, extension)
    os.chdir(cwd)
    print(9, os.path.realpath('r1d5_functions_basics.py'))

def run_glob():
    ''''''
    print('\nglob')
    print(1, glob.glob('*data*.py'))
    metadata = os.stat('r1d5_functions_basics.py')
    print(2, metadata)
    print(3, metadata.st_mtime)
    print(4, time.localtime(metadata.st_mtime))
    print(5, r1d5_functions_basics.approximate_size(metadata.st_size))

if __name__ == '__main__':
    run_main()
    run_conversion()
    get_prime_sum_until_num(10)
    run_os()
    run_glob()

'''
output:

lists
1 [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
2 [1, 2, 3, 4, 10, 20, 30, 40]

dicts
1 {'mike': 28, 'john': 31, 'julia': 26}
2 {'mike': 28, 'john': 31}
3 ('julia', 26)
4 dict_keys(['mike', 'john']) <class 'dict_keys'>
mike john 
5 dict_values([28, 31]) <class 'dict_values'>
28 31 
6 31

conversion
1 12
2 12
3 10.0
4 15.2
5 10
6 12.0
8 20
9 5.5
10 23.88
11 23
12 24

get_prime_sum_until_num 10
[1, 2, 3, 5, 7]
18

ros
1 /Users/juancarlosqr/code/datascience/python/100daysofpython
2 /Users/juancarlosqr/code/datascience
3 /Users/juancarlosqr/code/empty/main.py
4 /Users/juancarlosqr
5 /Users/juancarlosqr/code/empty/run.py
6 ['', 'Users', 'juancarlosqr', 'code', 'empty', 'main.py']
7 /Users/juancarlosqr/code/empty main.py
8 main .py
9 /Users/juancarlosqr/code/datascience/python/100daysofpython/r1d5_functions_basics.py

glob
1 ['r1d10_data_structures_3.py', 'r1d8_data_structures.py', 'r1d9_data_structures_2.py']
2 os.stat_result(st_mode=33188, st_ino=8079012, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=1415, st_atime=1508164998, st_mtime=1507553937, st_ctime=1507553937)
3 1507553937.0
4 time.struct_time(tm_year=2017, tm_mon=10, tm_mday=9, tm_hour=9, tm_min=58, tm_sec=57, tm_wday=0, tm_yday=282, tm_isdst=0)
5 1.4 KiB
'''
