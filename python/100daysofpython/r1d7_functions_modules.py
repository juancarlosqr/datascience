#!/usr/bin/env python3
import sys, os
import r1d7_module_say

day = 6

def sum(x, y):
    return x + y

def minus(x, y):
    return x - y

def operate(operation, x, y=1):
    global day # avoid using global
    day = 7
    print(day)
    return operation(x, y)

def total(a=5, *numbers, **phonebook):
    print('a', a)
    # iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

def dummy():
    '''My dummy function

    Some dummy description.'''
    pass

def use_imports():
    print('\nimports')
    # command line args
    for i in sys.argv:
        print(i)
    # working directory
    print(os.getcwd())
    # dir() list all defined names by the module
    for d in dir(sys):
        print(d)

if __name__ == '__main__':
    x = 4
    y = 3
    add = operate(sum, x, y)
    subs = operate(minus, x, y)
    print(1, 'add', add)
    print(2, 'subs', subs)
    # functions are first-class objects
    print(3, 'add', operate(sum, 10))
    # Named or Keyword arguments
    print(4, 'subs', operate(minus, y=10, x=12))
    # global
    print(5, 'day', day)
    # VarArgs parameters
    print(6, total(10, 1, 2, 3, Jack=123, John=231, Ann=156))
    # return None
    print(7, dummy())
    # help(dummy)
    # use_imports()
    r1d7_module_say.say('today is wednesday')
    print(8, r1d7_module_say.__version__)
else:
    print('is imported')

'''
output:

7
7
1 add 7
2 subs 1
7
3 add 11
7
4 subs 2
5 day 7
a 10
single_item 1
single_item 2
single_item 3
Jack 123
John 231
Ann 156
6 None
7 None
I say today is wednesday
8 0.1
'''