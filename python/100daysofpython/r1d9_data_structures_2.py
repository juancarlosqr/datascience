#!/usr/bin/env python3

import fractions
import math
import calendar

def numbers():
    print('\nnumbers')
    print(1, 'int(1.2)', int(1.2))
    print(2, 'int(1.5)', int(1.5))
    print(3, 'int(1.8)', int(1.8))
    print(4, 'int(1.0)', int(1.0))
    print(5, 'int(2.0)', int(2.0))
    print('\nfractions & trigonometry')
    x = fractions.Fraction(1, 3)
    print(1, 'x', x)
    print(2, 'x * 2', x * 2)
    print(3, 'Fraction(3, 6)', fractions.Fraction(3, 6))
    print(4, 'pi', math.pi)
    print(5, 'sin(pi / 2)', math.sin(math.pi / 2))
    print(6, 'tan(pi / 4)', math.tan(math.pi / 4))

def lists():
    print('\nlist')
    shopping = ['mango', 'apple', 'banana', 'carrot', 'beans']
    n = 2
    shopping2 = shopping[:n] + shopping[n:]
    print(1, shopping, id(shopping))
    print(2, shopping2, id(shopping2))
    shopping = shopping + [True]
    shopping.append(1)
    shopping.extend(['orange', 'mushrooms', 'apple'])
    shopping.insert(1, 'potato')
    print(3, 'shopping', shopping)
    print(4, 'count(apple)', shopping.count('apple'))
    print(5, 'banana in', 'banana' in shopping)
    print(6, 'index(orange)', shopping.index('orange'))
    del shopping[0]
    print(7, 'del [0]', shopping)
    shopping.remove('apple')
    print(8, 'remove(apple)', shopping)
    last = shopping.pop()
    print(9, 'pop()', shopping)
    print(10, 'last', last)
    print(11, 'tuple()', tuple(shopping))
    new_tuple = (1, 10, 100, 1000)
    print(12, 'list()', list(new_tuple))
    v = ('one', 2, 'three')
    print(13, 'v', v)
    x, y, z = v
    print(14, 'x, y, z:', x, y, z)
    (MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)
    print(15, 'days:', MON, TUE, WED, THU, FRI, SAT, SUN)
    print(16, 'TUE', TUE)

def calendars():
    print('\ncalendar')
    my_cal = calendar.Calendar()
    print(1, 'my_cal', my_cal, type(my_cal))
    print(2, 'my_cal.getfirstweekday()', my_cal.getfirstweekday())
    month = my_cal.monthdayscalendar(2017, 10)
    print(3, 'my_cal.monthdayscalendar(2017, 10)', month)
    print(4, 'weeks')
    for week in month:
        print(week)
    month2 = my_cal.monthdays2calendar(2017, 10)
    print(5, 'my_cal.monthdays2calendar(2017, 10)', month2)
    print(6, 'weeks')
    for week in month2:
        print(week)

if __name__ == '__main__':
    numbers()
    lists()
    calendars()

'''
output:

numbers
1 int(1.2) 1
2 int(1.5) 1
3 int(1.8) 1
4 int(1.0) 1
5 int(2.0) 2

fractions & trigonometry
1 x 1/3
2 x * 2 2/3
3 Fraction(3, 6) 1/2
4 pi 3.141592653589793
5 sin(pi / 2) 1.0
6 tan(pi / 4) 0.9999999999999999

list
1 ['mango', 'apple', 'banana', 'carrot', 'beans'] 4475183624
2 ['mango', 'apple', 'banana', 'carrot', 'beans'] 4475183560
3 shopping ['mango', 'potato', 'apple', 'banana', 'carrot', 'beans', True, 1, 'orange', 'mushrooms', 'apple']
4 count(apple) 2
5 banana in True
6 index(orange) 8
7 del [0] ['potato', 'apple', 'banana', 'carrot', 'beans', True, 1, 'orange', 'mushrooms', 'apple']
8 remove(apple) ['potato', 'banana', 'carrot', 'beans', True, 1, 'orange', 'mushrooms', 'apple']
9 pop() ['potato', 'banana', 'carrot', 'beans', True, 1, 'orange', 'mushrooms']
10 last apple
11 tuple() ('potato', 'banana', 'carrot', 'beans', True, 1, 'orange', 'mushrooms')
12 list() [1, 10, 100, 1000]
13 v ('one', 2, 'three')
14 x, y, z: one 2 three
15 days: 0 1 2 3 4 5 6
16 TUE 1

calendar
1 my_cal <calendar.Calendar object at 0x10aba5a58> <class 'calendar.Calendar'>
2 my_cal.getfirstweekday() 0
3 my_cal.monthdayscalendar(2017, 10) [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]
4 weeks
[0, 0, 0, 0, 0, 0, 1]
[2, 3, 4, 5, 6, 7, 8]
[9, 10, 11, 12, 13, 14, 15]
[16, 17, 18, 19, 20, 21, 22]
[23, 24, 25, 26, 27, 28, 29]
[30, 31, 0, 0, 0, 0, 0]
5 my_cal.monthdays2calendar(2017, 10) [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 6)], [(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], [(9, 0), (10, 1), (11, 2), (12, 3), (13, 4), (14, 5), (15, 6)], [(16, 0), (17, 1), (18, 2), (19, 3), (20, 4), (21, 5), (22, 6)], [(23, 0), (24, 1), (25, 2), (26, 3), (27, 4), (28, 5), (29, 6)], [(30, 0), (31, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]]
6 weeks
[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 6)]
[(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)]
[(9, 0), (10, 1), (11, 2), (12, 3), (13, 4), (14, 5), (15, 6)]
[(16, 0), (17, 1), (18, 2), (19, 3), (20, 4), (21, 5), (22, 6)]
[(23, 0), (24, 1), (25, 2), (26, 3), (27, 4), (28, 5), (29, 6)]
[(30, 0), (31, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
'''