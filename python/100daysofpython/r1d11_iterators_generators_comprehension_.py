#!/usr/bin/env python3

from sys import getsizeof

def run_comprehension():
    ''''''
    print('\nlist comprehension')
    day_group = [4, 7, 14, 16, 28]
    weeks= []
    for days in day_group:
        weeks.append(days/7.0)
    print(1, 'weeks', weeks)
    # using list comprehension
    weeks = [days/7.0 for days in day_group]
    print(2, 'weeks', weeks)
    weeks = [days/7.0 for days in day_group if days % 7 == 0]
    print(3, 'weeks', weeks)
    python = 'monty python'
    print(4, 'python', python, len(python))
    letters = [letter.upper() for letter in python if letter != ' ']
    print(5, 'count', letters, len(letters))
    nums = [1, 2, 3]
    letters = ['a', 'b', 'c']
    nums_letters = [[n, l.upper()] for n in nums for l in letters]
    print(6, 'nums', nums)
    print(7, 'letters', letters)
    print(8, 'nums_letters', nums_letters)

    print('\nset comprehension')
    friends = ['jose', 'ralph', 'jack', 'jane']
    starting_letters = {name[0] for name in friends}
    print(1, 'starting_letters', starting_letters, len(starting_letters))

    print('\ndict comprehensions')
    dict_comp = {n:n ** 2 for n in range(9)}
    print(1, 'dict_comp', dict_comp, type(dict_comp))
    dict_letter = {x:chr(65+x) for x in range(1, 11)}
    print(2, 'dict_letter', dict_letter, type(dict_letter))

    print('\niterable and iterator')
    print(1, 'str', hasattr(str, '__iter__'))
    print(2, 'int', hasattr(int, '__iter__'))
    print(3, 'list', hasattr(list, '__iter__'))
    simple_list = [1, 10, 100]
    iterator = iter(simple_list)
    print(4, 'simple_list', simple_list)
    print(5, 'iterator', iterator, type(iterator))
    print(6, 'next(iterator)', next(iterator))
    print(7, 'next(iterator)', next(iterator))
    print(8, 'next(iterator)', next(iterator))
    # print(9, 'next(iterator)', next(iterator)) # StopIteration exception

    print('\ngenerators')
    def gen_func():
        for x in range(5):
            yield x
    print(1, 'generator function', gen_func())
    for x in gen_func():
        print(x)
    gen_comp = (x ** 2 for x in range(10) if x % 2 == 0)
    print(2, 'generator comprehension', gen_comp)
    for x in gen_comp:
        print(x)

    print('\ncomprehensions')
    end = 100
    by = 5
    lst_comp = [x * by for x in range(end)]
    set_comp = {x * by for x in range(end)}
    dct_comp = {x: x * by for x in range(end)}
    gen_comp = (x * by for x in range(end))
    print(1, lst_comp) # list comprehension
    print(2, set_comp) # set comprehension
    print(3, dct_comp) # dict comprehension
    print(4, gen_comp) # generator comprehension
    print(5, 'sizes')
    print(6, 'lst_comp', getsizeof(lst_comp)) # list comprehension
    print(7, 'set_comp', getsizeof(set_comp)) # set comprehension
    print(8, 'dct_comp', getsizeof(dct_comp)) # dict comprehension
    print(9, 'gen_comp', getsizeof(gen_comp)) # generator comprehension
    print(10, next(gen_comp))
    print(11, next(gen_comp))
    print(12, next(gen_comp))

if __name__ == '__main__':
    run_comprehension()

'''
output:

list comprehension
1 weeks [0.5714285714285714, 1.0, 2.0, 2.2857142857142856, 4.0]
2 weeks [0.5714285714285714, 1.0, 2.0, 2.2857142857142856, 4.0]
3 weeks [1.0, 2.0, 4.0]
4 python monty python 12
5 count ['M', 'O', 'N', 'T', 'Y', 'P', 'Y', 'T', 'H', 'O', 'N'] 11
6 nums [1, 2, 3]
7 letters ['a', 'b', 'c']
8 nums_letters [[1, 'A'], [1, 'B'], [1, 'C'], [2, 'A'], [2, 'B'], [2, 'C'], [3, 'A'], [3, 'B'], [3, 'C']]

set comprehension
1 starting_letters {'j', 'r'} 2

dict comprehensions
1 dict_comp {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} <class 'dict'>
2 dict_letter {1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K'} <class 'dict'>

iterable and iterator
1 str True
2 int False
3 list True
4 simple_list [1, 10, 100]
5 iterator <list_iterator object at 0x1093f1550> <class 'list_iterator'>
6 next(iterator) 1
7 next(iterator) 10
8 next(iterator) 100

generators
1 generator function <generator object run_comprehension.<locals>.gen_func at 0x1093ebf68>
0
1
2
3
4
2 generator comprehension <generator object run_comprehension.<locals>.<genexpr> at 0x1093ebf68>
0
4
16
36
64

comprehensions
1 [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495]
2 {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495}
3 {0: 0, 1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50, 11: 55, 12: 60, 13: 65, 14: 70, 15: 75, 16: 80, 17: 85, 18: 90, 19: 95, 20: 100, 21: 105, 22: 110, 23: 115, 24: 120, 25: 125, 26: 130, 27: 135, 28: 140, 29: 145, 30: 150, 31: 155, 32: 160, 33: 165, 34: 170, 35: 175, 36: 180, 37: 185, 38: 190, 39: 195, 40: 200, 41: 205, 42: 210, 43: 215, 44: 220, 45: 225, 46: 230, 47: 235, 48: 240, 49: 245, 50: 250, 51: 255, 52: 260, 53: 265, 54: 270, 55: 275, 56: 280, 57: 285, 58: 290, 59: 295, 60: 300, 61: 305, 62: 310, 63: 315, 64: 320, 65: 325, 66: 330, 67: 335, 68: 340, 69: 345, 70: 350, 71: 355, 72: 360, 73: 365, 74: 370, 75: 375, 76: 380, 77: 385, 78: 390, 79: 395, 80: 400, 81: 405, 82: 410, 83: 415, 84: 420, 85: 425, 86: 430, 87: 435, 88: 440, 89: 445, 90: 450, 91: 455, 92: 460, 93: 465, 94: 470, 95: 475, 96: 480, 97: 485, 98: 490, 99: 495}
4 <generator object run_comprehension.<locals>.<genexpr> at 0x1093ebfc0>
5 sizes
6 lst_comp 912
7 set_comp 8416
8 dct_comp 4704
9 gen_comp 88
10 0
11 5
12 10
'''