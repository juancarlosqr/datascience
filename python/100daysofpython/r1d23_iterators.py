#!/usb/bin/env python3

import re
import itertools

def solve(puzzle):
    '''
    From http://www.diveintopython3.net/advanced-iterators.html
    '''
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

def run_puzzle():
    ''''''
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)

def run_retest():
    ''''''
    print('\nre test')
    print(1, re.findall('[0-9]+', '16 2-by-4s in rows of 8'))
    print(2, re.findall(' s.*? s', "The sixth sick sheikh's sixth sheep's sick."))
    assert 1 + 1 == 2
    # assert 1 + 1 == 3 # AssertionError
    # assert 2 + 2 == 5, 'Only for very large values of 2' # AssertionError: Only for very large values of 2
    print('\nitertools.permutations')
    perm = list(itertools.permutations([1,3,5], 3))
    print(perm)
    print('\nitertools.product')
    product = list(itertools.product('XYZ', '123'))
    print(product)
    print('\nitertools.combinations')
    comb = list(itertools.combinations('XYZ', 2))
    print(comb)
    print('\nnames')
    names = list(open('r1d23_names.txt', encoding='utf-8'))
    print(names)
    names = [name.strip() for name in names]
    print(names)
    sorted_names = sorted(names)
    print(sorted_names)
    sorted_names = sorted(names, key=len)
    print(sorted_names)
    print('\nnames using itertools.groupby')
    groups = itertools.groupby(sorted_names, len)
    print(groups)
    print(list(groups))
    groups = itertools.groupby(sorted_names, len)
    for name_len, name_iter in groups:
        print(f'Names with {name_len} letters:')
        for name in name_iter:
            print(name)
    print('\nitertools.chain')
    print(list(itertools.chain(range(0, 3), range(10, 13))))
    print('\nzip vs itertools.zip_longest')
    print(list(zip(range(0, 3), range(10, 13))))
    print(list(zip(range(0, 3), range(10, 14))))
    print(list(itertools.zip_longest(range(0, 3), range(10, 14))))
    print('\ntranslate')
    translation_table = {ord('A'): ord('O')}
    print(translation_table)
    print('MARK', 'MARK'.translate(translation_table))
    print(str(ord('J')) + str(ord('C')))
    print('\neval')
    print(eval('1 + 1 == 2'))
    print(eval('1 + 1 == 3'))
    print(eval('9567 + 1085 == 10652'))
    print(eval('"A" + "B"'))
    print(eval('"MARK".translate({65: 79})'))
    print(eval('"MMMMM".count("M")'))
    print(eval('["$"] * 3'))
    x = 5
    print(eval('x * 2'))
    print(eval('pow(x, 2)'))

if __name__ == '__main__':
    # run_puzzle()
    run_retest()

'''
output:

./r1d23_iterators.py "HAWAII + IDAHO + IOWA + OHIO == STATES" "I + LOVE + YOU == DORA" "SEND + MORE == MONEY"
HAWAII + IDAHO + IOWA + OHIO == STATES
510199 + 98153 + 9301 + 3593 == 621246
I + LOVE + YOU == DORA
3 + 1458 + 946 == 2407
SEND + MORE == MONEY
9567 + 1085 == 10652

./r1d23_iterators.py "HAWAII + IDAHO + IOWA + OHIO == STATES" "I + LOVE + YOU == DORA" "SEND + MORE == MONEY"
HAWAII + IDAHO + IOWA + OHIO == STATES
510199 + 98153 + 9301 + 3593 == 621246
I + LOVE + YOU == DORA
1 + 2874 + 985 == 3860 # different
SEND + MORE == MONEY
9567 + 1085 == 10652

re test
1 ['16', '2', '4', '8']
2 [' sixth s', " sheikh's s", " sheep's s"]

itertools.permutations
[(1, 3, 5), (1, 5, 3), (3, 1, 5), (3, 5, 1), (5, 1, 3), (5, 3, 1)]

itertools.product
[('X', '1'), ('X', '2'), ('X', '3'), ('Y', '1'), ('Y', '2'), ('Y', '3'), ('Z', '1'), ('Z', '2'), ('Z', '3')]

itertools.combinations
[('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]

names
['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n', 'Mike\n', 'Chris\n', 'Sarah\n', 'Alex\n', 'Lizzie']
['Dora', 'Ethan', 'Wesley', 'John', 'Anne', 'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']
['Alex', 'Anne', 'Chris', 'Dora', 'Ethan', 'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']
['Dora', 'John', 'Anne', 'Mike', 'Alex', 'Ethan', 'Chris', 'Sarah', 'Wesley', 'Lizzie']

names using itertools.groupby
<itertools.groupby object at 0x10382e8b8>
[(4, <itertools._grouper object at 0x103823860>), (5, <itertools._grouper object at 0x103823898>), (6, <itertools._grouper object at 0x1038238d0>)]
Names with 4 letters:
Dora
John
Anne
Mike
Alex
Names with 5 letters:
Ethan
Chris
Sarah
Names with 6 letters:
Wesley
Lizzie

itertools.chain
[0, 1, 2, 10, 11, 12]

zip vs itertools.zip_longest
[(0, 10), (1, 11), (2, 12)]
[(0, 10), (1, 11), (2, 12)]
[(0, 10), (1, 11), (2, 12), (None, 13)]

translate
{65: 79}
MARK MORK
7467

eval
True
False
True
AB
MORK
5
['$', '$', '$']
10
25
'''