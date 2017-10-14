#!/usr/bin/env python3

def run_print_five():
    ''''''
    def dummy(val):
        print(val)
    def print_five(func, val):
        for i in range(0,5):
            func(val)
    print_five(dummy, 'monty python')

def run_sets():
    ''''''
    print('\nsets')
    hi = {'hello'}
    print(1, 'hi', hi, type(hi))
    list1 = ['python', 'php', 'js', 'go', 'C#', 'java']
    langs = set(list1)
    print(2, 'langs', langs, type(langs))
    print(3, 'empty', {}, type({}))
    print(4, 'set()', set(), type(set()))
    # adding values
    langs.add('elixir')
    langs.add('python')
    print(5, 'langs', langs, len(langs))
    a_set = {1, 2, 3}
    print(6, 'a_set', a_set)
    a_set.update({2, 4 ,6})
    print(7, 'a_set', a_set)
    a_set.update({3, 6, 9}, {1, 2, 3, 4, 5, 10, 15})
    print(8, 'a_set', a_set)
    a_set.update([10, 20, 30])
    print(9, 'a_set', a_set)
    # removing values with discard
    a_set.discard(20)
    print(10, 'a_set', a_set)
    a_set.discard(20)
    print(11, 'a_set', a_set)
    # removing values with remove
    a_set.remove(2)
    print(12, 'a_set', a_set)
    # a_set.remove(2) # KeyError exception
    # print(13, 'a_set', a_set)
    value = a_set.pop()
    print(13, 'a_set', a_set)
    print(14, 'value', value)
    b_set = a_set.copy()
    a_set.clear()
    print(15, 'a_set', a_set)
    print(16, 'b_set', b_set)
    # set operations
    print(17, 'in a', 50 in a_set)
    print(18, 'in b', 50 in b_set)
    print(19, 'in b', 10 in b_set)
    a_set = {1, 10, 100, 1000}
    print(20, 'union', a_set.union(b_set))
    print(21, 'a_set', a_set)
    print(22, 'b_set', b_set)
    print(23, 'intersection', a_set.intersection(b_set))
    print(23, 'difference a', a_set.difference(b_set))
    print(24, 'difference b', b_set.difference(a_set))
    print(25, 'difference a', a_set.difference(a_set))
    print(26, 'symmetric_difference', a_set.symmetric_difference(b_set))
    # union, intersection, and symmetric_difference are symmetric
    print(27, 'symmetric_difference ==', a_set.symmetric_difference(b_set) == b_set.symmetric_difference(a_set))
    # checking
    c_set = {1, 2, 3}
    d_set = {1, 2, 3, 4}
    print(28, 'c subset d', c_set.issubset(d_set))
    print(29, 'd subset c', d_set.issubset(c_set))
    print(30, 'c superset d', c_set.issuperset(d_set))
    print(31, 'd superset c', d_set.issuperset(c_set))
    # operators
    # add = c_set + d_set
    # print(32, 'c_set + d_set', add) #TypeError: unsupported operand
    print(33, 'd_set - c_set', d_set - c_set)
    print(34, 'c_set & d_set', c_set & d_set)
    my_friends = {'Jack', 'Anne'}
    your_friends = {'Bob', 'Jack', 'Michael'}
    # our_friends = my_friends + your_friends # TypeError: unsupported operand
    # print(35, 'our_friends', our_friends)  # {'Jack', 'Bob', 'Anne', 'Michael'}

def run_dicts():
    ''''''
    print('\ndictionaries')
    config = {'language': 'python', 'db': 'mongo'}
    print(1, 'config', config)
    print(2, 'type', type(config))
    print(3, 'config[db]', config['db'])
    config['ide'] = 'pycharm'
    print(4, 'config', config)
    for key, value in config.items():
        print(key, value)

def run_none():
    ''''''
    print('\nnone')
    print(1, 'type', type(None))
    print(2, '= false?', None == False)
    print(3, '= 0?', None == 0)
    print(4, '= ""?', None == '')
    print(5, '= None?', None == None)
    print(6, 'None', None)
    print(7, 'not None', not None)

def run_lists():
    ''''''
    my_list = ['monday', 'thursday', 'saturday']
    # for index, day in my_list: # ValueError: too many values to unpack
    for day in my_list:
        print(my_list.index(day), day)

if __name__ == '__main__':
    run_print_five()
    run_sets()
    run_dicts()
    run_none()
    run_lists()

'''
output:

monty python
monty python
monty python
monty python
monty python

sets
1 hi {'hello'} <class 'set'>
2 langs {'js', 'php', 'python', 'go', 'C#', 'java'} <class 'set'>
3 empty {} <class 'dict'>
4 set() set() <class 'set'>
5 langs {'js', 'php', 'python', 'go', 'elixir', 'C#', 'java'} 7
6 a_set {1, 2, 3}
7 a_set {1, 2, 3, 4, 6}
8 a_set {1, 2, 3, 4, 5, 6, 9, 10, 15}
9 a_set {1, 2, 3, 4, 5, 6, 9, 10, 15, 20, 30}
10 a_set {1, 2, 3, 4, 5, 6, 9, 10, 15, 30}
11 a_set {1, 2, 3, 4, 5, 6, 9, 10, 15, 30}
12 a_set {1, 3, 4, 5, 6, 9, 10, 15, 30}
13 a_set {3, 4, 5, 6, 9, 10, 15, 30}
14 value 1
15 a_set set()
16 b_set {3, 4, 5, 6, 9, 10, 15, 30}
17 in a False
18 in b False
19 in b True
20 union {1, 3, 4, 5, 6, 9, 10, 15, 30, 100, 1000}
21 a_set {1000, 1, 10, 100}
22 b_set {3, 4, 5, 6, 9, 10, 15, 30}
23 intersection {10}
23 difference a {1000, 1, 100}
24 difference b {3, 4, 5, 6, 9, 15, 30}
25 difference a set()
26 symmetric_difference {1, 3, 4, 5, 6, 9, 15, 30, 100, 1000}
27 symmetric_difference == True
28 c subset d True
29 d subset c False
30 c superset d False
31 d superset c True
33 d_set - c_set {4}
34 c_set & d_set {1, 2, 3}

dictionaries
1 config {'language': 'python', 'db': 'mongo'}
2 type <class 'dict'>
3 config[db] mongo
4 config {'language': 'python', 'db': 'mongo', 'ide': 'pycharm'}
language python
db mongo
ide pycharm

none
1 type <class 'NoneType'>
2 = false? False
3 = 0? False
4 = ""? False
5 = None? True
6 None None
7 not None True
0 monday
1 thursday
2 saturday
'''
