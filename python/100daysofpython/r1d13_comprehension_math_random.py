#!/usr/bin/env python3

import os, glob, math, random
import r1d5_functions_basics

def run_comprehension():
    ''''''
    print('\ncomprehension')
    cwd = os.getcwd()
    print(1, 'cwd', cwd)
    metadata = {file:os.stat(file) for file in glob.glob('*.py')}
    print(2, 'files')
    for file, meta in metadata.items():
        print(r1d5_functions_basics.approximate_size(meta.st_size), '-', file)
    print('\nswapping the keys and values of a dict')
    my_dict = {1:'a', 2:'b', 3:'c'}
    new_dict = {value:key for key, value in my_dict.items()}
    print(1, my_dict)
    print(2, new_dict)

def run_math():
    ''''''
    print('\nmath functions')
    x = 5
    y = 2
    z = -4
    t = 3.6
    v = 3.2
    print(1, round(t))
    print(2, round(v))
    print(3, math.ceil(t))
    print(4, math.ceil(v))
    print(5, math.floor(t))
    print(6, math.floor(v))
    print(7, pow(x, y))
    print(8, abs(z))
    print(9, max(x, y, z, t))
    print(10, min(x, y, z, t))
    print(11, math.sqrt(x * x))
    print(12, math.sin(y))
    print(13, math.cos(y))
    print(14, math.tan(y))

def run_random():
    ''''''
    print('\nrandom')
    for r in range(0, 10):
        print(random.random())
    print('\nrandint')
    for r in range(0, 10):
        print(random.randint(10, 20))

if __name__ == '__main__':
    run_comprehension()
    run_math()
    run_random()

'''
output:

comprehension
1 cwd /Users/juancarlosqr/code/datascience/python/100daysofpython
2 files
5.1 KiB - r1d10_data_structures_3.py
6.1 KiB - r1d11_iterators_generators_comprehension_.py
3.7 KiB - r1d12_conversion_os_glob.py
2.4 KiB - r1d13_comprehension_math_random.py
0.1 KiB - r1d1_setup.py
1.4 KiB - r1d2_basics.py
1.3 KiB - r1d3_strings.py
5.5 KiB - r1d4_strings_methods_operators.py
1.4 KiB - r1d5_functions_basics.py
2.1 KiB - r1d6_operators_control_flow.py
1.6 KiB - r1d7_functions_modules.py
0.1 KiB - r1d7_module_say.py
5.1 KiB - r1d8_data_structures.py
4.5 KiB - r1d9_data_structures_2.py

swapping the keys and values of a dict
1 {1: 'a', 2: 'b', 3: 'c'}
2 {'a': 1, 'b': 2, 'c': 3}

math functions
1 4
2 3
3 4
4 4
5 3
6 3
7 25
8 4
9 5
10 -4
11 5.0
12 0.9092974268256817
13 -0.4161468365471424
14 -2.185039863261519

random
0.4629472123678583
0.7574228005394907
0.4096508968987119
0.21385530323662483
0.12040517190102551
0.9059686307042255
0.09111110001825473
0.5568974078724064
0.0802385134085265
0.89639978509252

randint
18
15
15
18
11
17
14
16
15
10
'''