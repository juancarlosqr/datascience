#!/usr/bin/env python3
from sys import version

def operators():
    print('\noperators')
    print(version)
    print('left shift (2 << 2):', 2 << 2)
    print('right shift (11 >> 1):', 11 >> 1)
    print('bit-wise AND: (5 & 3):', 5 & 3)
    print('bit-wise OR (5 | 3):', 5 | 3)
    print('bit-wise XOR (5 ^ 3):', 5 ^ 3)
    print('bit-wise invert (~5):', ~5)
    print(1, 3 < 5 < 7)
    print(2, 3 < 9 < 6)
    print(3, 10 >= 5)
    print(4, 5 >= 10)
    print(5, 5 != 10)
    print(6, 10 != 10)
    x = 4 == 4
    print(7, x)
    print(8, not x)
    y = 6 > 3
    print(9, x and y)
    print(10, x or y)

def control():
    print('\ncontrol')
    print('\nif, elif, else')
    number = 12
    guess = int(input('your guess: '))
    if number == guess:
        print('you win')
    elif number > guess:
        print('higher than that')
    else:
        print('lower than that')
    print('bye!')

    print('\nwhile')
    grade = 9
    guess = 0
    while grade != guess:
        guess = int(input('grade: '))
        if grade == guess:
            print('you guessed it')
        elif guess == 0:
            break
        elif guess == 100:
            continue
        elif grade > guess:
            print('higher')
        else:
            print('lower')
    else:
        print('while loop is over')

    print('\nfor')
    for i in range(1, 4):
        print(i)
    else:
        print('for loop is over')

    greet = 'greet'
    for c in greet:
        print(c)
    grades = [10, 7, 9]
    for gr in grades:
        print(gr)

    print('\nthe end')

if __name__ == '__main__':
    operators()
    control()

'''
output:

operators
3.6.1 |Anaconda custom (x86_64)| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
left shift (2 << 2): 8
right shift (11 >> 1): 5
bit-wise AND: (5 & 3): 1
bit-wise OR (5 | 3): 7
bit-wise XOR (5 ^ 3): 6
bit-wise invert (~5): -6
1 True
2 False
3 True
4 False
5 True
6 False
7 True
8 False
9 True
10 True

control

if, elif, else
your guess: 5
higher than that
bye!

while
grade: 9
you guessed it
while loop is over

for
1
2
3
for loop is over
g
r
e
e
t
10
7
9

the end
'''