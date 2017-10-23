#!/usb/bin/env python3

import re
from sys import getsizeof

nouns = ['bass', 'fax', 'waltz', 'coach', 'rash', 'cheetah', 'currency', 'vacancy', 'agency', 'day', 'book']

# plural v5
def build_match_and_apply_functions(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

def rules(rules_filename):
    ''''''
    print('inside rules')
    with open(rules_filename, encoding='utf-8') as patterns:
        for line in patterns:
            print('looping patterns')
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def pluralize(noun, filename='r1d18_rules.txt'):
    ''''''
    print('inside pluralize', noun)
    for match, apply in rules(filename):
        if match(noun):
            return apply(noun)
    raise ValueError(f'no matching rule for {noun}')

def run_regex5():
    ''''''
    print('\nregex v5 (with generators)')
    total = 0
    for n in nouns:
        print(n, pluralize(n))
        total += 1
    print('total v5', total)

def counter(x):
    ''''''
    print('inside counter')
    while True:
        yield x
        print('incrementing x')
        x += 1

def run_counter():
    ''''''
    print('\ncounter')
    c1 = counter(2)
    print(c1)
    print(next(c1))
    print(next(c1))
    print(next(c1))
    print(next(c1))

def fib(max):
    ''''''
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

def run_fib():
    ''''''
    print('\nfibonacci')
    nums = [3, 10, 1000]
    for n in nums:
        print(f'fibonacci of {n} is', end=' ')
        for i in fib(n):
            print(i, end=' ')
        print()
    fib100 = list(fib(100))
    print('fib100', fib100)
    fib20 = [n for n in fib(20)]
    print('fib20', fib20, getsizeof(fib20))
    fib20_g = (n for n in fib(20))
    print('fib20_g', fib20_g, getsizeof(fib20_g))
    for f in fib20_g:
        print(f, end=' ')
    print()

def my_range(y):
    ''''''
    x = 1
    while x <= y:
        yield x
        x += 1

def run_test():
    ''''''
    print('\nmy_range')
    r = my_range(5)
    print(r)
    print(next(r))
    print(next(r))
    print(next(r))
    print(next(r))
    print(next(r))
    # print(next(r)) # throws StopIteration exception
    print('\nin for')
    for i in my_range(10):
        print(i)

if __name__ == '__main__':
    run_regex5()
    run_counter()
    run_fib()
    run_test()

'''
output:

regex v5 (with generators)
inside pluralize bass
inside rules
looping patterns
bass basses
inside pluralize fax
inside rules
looping patterns
fax faxes
inside pluralize waltz
inside rules
looping patterns
waltz waltzes
inside pluralize coach
inside rules
looping patterns
looping patterns
coach coaches
inside pluralize rash
inside rules
looping patterns
looping patterns
rash rashes
inside pluralize cheetah
inside rules
looping patterns
looping patterns
looping patterns
looping patterns
cheetah cheetahs
inside pluralize currency
inside rules
looping patterns
looping patterns
looping patterns
currency currencies
inside pluralize vacancy
inside rules
looping patterns
looping patterns
looping patterns
vacancy vacancies
inside pluralize agency
inside rules
looping patterns
looping patterns
looping patterns
agency agencies
inside pluralize day
inside rules
looping patterns
looping patterns
looping patterns
looping patterns
day days
inside pluralize book
inside rules
looping patterns
looping patterns
looping patterns
looping patterns
book books
total v5 11

counter
<generator object counter at 0x10cf8aeb8>
inside counter
2
incrementing x
3
incrementing x
4
incrementing x
5

fibonacci
fibonacci of 3 is 0 1 1 2 
fibonacci of 10 is 0 1 1 2 3 5 8 
fibonacci of 1000 is 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
fib100 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fib20 [0, 1, 1, 2, 3, 5, 8, 13] 128
fib20_g <generator object run_fib.<locals>.<genexpr> at 0x10cf8af68> 88
0 1 1 2 3 5 8 13

my_range
<generator object my_range at 0x101880f68>
1
2
3
4
5

in for
1
2
3
4
5
6
7
8
9
10
'''