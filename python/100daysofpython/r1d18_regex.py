#!/usb/bin/env python3

import re

nouns = ['bass', 'fax', 'waltz', 'coach', 'rash', 'cheetah', 'currency', 'vacancy', 'agency', 'day', 'book']

# plural v1
def plural(noun):
    ''''''
    if re.search('[sxz]$', noun) or re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'

def run_regex1():
    ''''''
    print('\nregex v1')
    total = 0
    for n in nouns:
        print(n, plural(n))
        total += 1
    print('total v1', total)

# plural v2
def pluralize(noun, rules):
    ''''''
    for match, apply in rules:
        if match(noun):
            return apply(noun)

def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):
    return re.search('[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

def run_regex2():
    ''''''
    print('\nregex v2 (with functions)')
    rules = (
        (match_sxz, apply_sxz),
        (match_h, apply_h),
        (match_y, apply_y),
        (match_default, apply_default)
    )
    total = 0
    for n in nouns:
        print(n, pluralize(n, rules))
        total += 1
    print('total v2', total)

# plural v3
def build_match_and_apply_functions(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

def run_regex3():
    ''''''
    print('\nregex v3 (with closures)')
    patterns = \
        (
            ('[sxz]$',           '$',  'es'),
            ('[^aeioudgkprt]h$', '$',  'es'),
            ('(qu|[^aeiou])y$',  'y$', 'ies'),
            ('$',                '$',  's'),
        )
    rules = [build_match_and_apply_functions(pattern, search, replace) \
             for (pattern, search, replace) in patterns]
    total = 0
    for n in nouns:
        print(n, pluralize(n, rules))
        total += 1
    print('total v3', total)

# plural v4
def run_regex4():
    ''''''
    print('\nregex v4 (with rules file)')
    rules = []
    with open('r1d18_rules.txt', encoding='utf-8') as patterns:
        for line in patterns:
            pattern, search, replace = line.split(None, 3)
            rules.append(build_match_and_apply_functions(pattern, search, replace))
    total = 0
    for n in nouns:
        print(n, pluralize(n, rules))
        total += 1
    print('total v4', total)

def run_regex_practice():
    ''''''
    print('\nregex practice')
    print(1, 'search', re.search('[abc]', 'mark'))
    print(2, 'sub', re.sub('[abc]', 'o', 'mark'))
    print(3, 'sub', re.sub('[abc]', 'o', 'rock'))
    print(4, 'sub', re.sub('[abc]', 'o', 'caps'))
    print(5, 'sub', re.sub('[abc]', 'oh', 'caps'))
    print(6, 'search', re.search('[^aeiou]y$', 'vacancy'))
    print(7, 'search', re.search('[^aeiou]y$', 'boy'))
    print(8, 'search', re.search('[^aeiou]y$', 'day'))
    print(9, 'search', re.search('[^aeiou]y$', 'pita'))
    print(10, 'sub', re.sub('([^aeiou])y$', r'\1ies', 'currency')) # \1 means replace the 1st group remembered

if __name__ == '__main__':
    run_regex1()
    run_regex2()
    run_regex3()
    run_regex4()
    run_regex_practice()

'''
output:

regex v1
bass basses
fax faxes
waltz waltzes
coach coaches
rash rashes
cheetah cheetahs
currency currencies
vacancy vacancies
agency agencies
day days
book books
total v1 11

regex v2 (with functions)
bass basses
fax faxes
waltz waltzes
coach coaches
rash rashes
cheetah cheetahs
currency currencies
vacancy vacancies
agency agencies
day days
book books
total v2 11

regex v3 (with closures)
bass basses
fax faxes
waltz waltzes
coach coaches
rash rashes
cheetah cheetahs
currency currencies
vacancy vacancies
agency agencies
day days
book books
total v3 11

regex v4 (with rules file)
bass basses
fax faxes
waltz waltzes
coach coaches
rash rashes
cheetah cheetahs
currency currencies
vacancy vacancies
agency agencies
day days
book books
total v4 11

regex practice
1 search <_sre.SRE_Match object; span=(1, 2), match='a'>
2 sub mork
3 sub rook
4 sub oops
5 sub ohohps
6 search <_sre.SRE_Match object; span=(5, 7), match='cy'>
7 search None
8 search None
9 search None
10 sub currencies
'''