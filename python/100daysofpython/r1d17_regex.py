#!/usb/bin/env python3

import re

def test_regex(pattern, values, title, verbose=False):
    ''''''
    print(f'\n{title}')
    print('pattern', pattern)
    test = {v: re.search(pattern, v, re.VERBOSE if verbose else 0) for v in values}
    for k, t in test.items():
        print(k, t)

def run_regex():
    ''''''
    # thousands
    pattern = r'^M{0,3}$'
    values = ['M', 'MM', 'MMM', 'MMMM', '']
    test_regex(pattern, values, 'thousands')
    # tens
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})$'
    values = ['MCMXL', 'MCML', 'MCMLX', 'MCMLXXX', 'MCMLXXXX', '']
    test_regex(pattern, values, 'tens')
    # ones
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    values = ['MDLV', 'MMDCLXVI', 'MMMDCCCLXXXVIII', '']
    test_regex(pattern, values, 'ones')
    # verbose regex
    pattern = '''
    ^                   # start of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''
    values = ['M', 'MCMLXXXIX', 'MMMDCCCLXXXVIII', '']
    test_regex(pattern, values, 'verbose', True)
    # verbose regex
    values = ['M']
    test_regex(pattern, values, 'non verbose')

def run_phones():
    ''''''
    print('\nphones pattern')
    phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
    print(1, phonePattern.search('800-555-1212').groups())
    print(2, phonePattern.search('800-555-1212-1234'))
    # print(3, phonePattern.search('800-555-1212-1234').groups()) # AttributeError: 'NoneType' object has no attribute 'groups'
    phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
    print(4, phonePattern.search('800-555-1212-1234').groups())
    print(5, phonePattern.search('800 555 1212 1234'))
    print(6, phonePattern.search('800-555-1212'))
    phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
    print(7, phonePattern.search('800-555-1212-1234').groups())
    print(8, phonePattern.search('800 555 1212 1234').groups())
    print(9, phonePattern.search('80055512121234'))
    print(9, phonePattern.search('800-555-1212'))
    phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
    print(10, phonePattern.search('80055512121234').groups())
    print(11, phonePattern.search('800-555-1212-1234').groups())
    print(12, phonePattern.search('800 555 1212 1234').groups())
    print(12, phonePattern.search('800.555.1212 x1234').groups())
    print(13, phonePattern.search('800-555-1212').groups())
    print(14, phonePattern.search('(800)5551212 x1234'))
    phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
    print(15, phonePattern.search('(800)5551212 x1234').groups())
    print(16, phonePattern.search('800-555-1212').groups())
    print(17, phonePattern.search('work 1-(800) 555.1212 #1234'))
    phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
    print(18, phonePattern.search('work 1-(800) 555.1212 #1234').groups())
    print(19, phonePattern.search('(800)5551212 x1234').groups())
    print(20, phonePattern.search('800-555-1212').groups())
    print(21, phonePattern.search('80055512121234').groups())
    phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
    print(22, phonePattern.search('800-555-1212').groups())
    print(23, phonePattern.search('work 1-(800) 555.1212 #1234').groups())

def run_test():
    ''''''
    print('\ntest')
    phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
    filename = 'r1d17_phones.txt'
    with open(filename, 'r') as file:
        phones = [phone.replace('\n', '') for phone in file]
    for p in phones:
        result = re.search(phonePattern, p)
        if not result:
            print(p)
            # else:
            #     print(result.groups())

if __name__ == '__main__':
    run_regex()
    run_phones()
    # run_test() # to run this include r1d17_phones.txt file

'''
output:

thousands
pattern ^M{0,3}$
M <_sre.SRE_Match object; span=(0, 1), match='M'>
MM <_sre.SRE_Match object; span=(0, 2), match='MM'>
MMM <_sre.SRE_Match object; span=(0, 3), match='MMM'>
MMMM None
 <_sre.SRE_Match object; span=(0, 0), match=''>

tens
pattern ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})$
MCMXL <_sre.SRE_Match object; span=(0, 5), match='MCMXL'>
MCML <_sre.SRE_Match object; span=(0, 4), match='MCML'>
MCMLX <_sre.SRE_Match object; span=(0, 5), match='MCMLX'>
MCMLXXX <_sre.SRE_Match object; span=(0, 7), match='MCMLXXX'>
MCMLXXXX None
 <_sre.SRE_Match object; span=(0, 0), match=''>

ones
pattern ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
MDLV <_sre.SRE_Match object; span=(0, 4), match='MDLV'>
MMDCLXVI <_sre.SRE_Match object; span=(0, 8), match='MMDCLXVI'>
MMMDCCCLXXXVIII <_sre.SRE_Match object; span=(0, 15), match='MMMDCCCLXXXVIII'>
 <_sre.SRE_Match object; span=(0, 0), match=''>

verbose
pattern 
    ^                   # start of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string

M <_sre.SRE_Match object; span=(0, 1), match='M'>
MCMLXXXIX <_sre.SRE_Match object; span=(0, 9), match='MCMLXXXIX'>
MMMDCCCLXXXVIII <_sre.SRE_Match object; span=(0, 15), match='MMMDCCCLXXXVIII'>
 <_sre.SRE_Match object; span=(0, 0), match=''>

non verbose
pattern 
    ^                   # start of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string

M None

phones pattern
1 ('800', '555', '1212')
2 None
4 ('800', '555', '1212', '1234')
5 None
6 None
7 ('800', '555', '1212', '1234')
8 ('800', '555', '1212', '1234')
9 None
9 None
10 ('800', '555', '1212', '1234')
11 ('800', '555', '1212', '1234')
12 ('800', '555', '1212', '1234')
12 ('800', '555', '1212', '1234')
13 ('800', '555', '1212', '')
14 None
15 ('800', '555', '1212', '1234')
16 ('800', '555', '1212', '')
17 None
18 ('800', '555', '1212', '1234')
19 ('800', '555', '1212', '1234')
20 ('800', '555', '1212', '')
21 ('800', '555', '1212', '1234')
22 ('800', '555', '1212', '')
23 ('800', '555', '1212', '1234')
'''