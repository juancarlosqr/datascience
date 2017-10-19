#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, r1d5_functions_basics

def run_strings():
    ''''''
    print('\nstrings')
    s = '深入öñ Python'
    print(1, s, len(s))
    print(2, s[0])
    print(3, s + ' 3')
    print('\nformat')
    suffixes = r1d5_functions_basics.SUFFIXES[1000]
    print(1, suffixes)
    print(2, '1000{0[0]} = 1{0[1]}'.format(suffixes))
    print(3, '1MB = 1000{0.modules[r1d5_functions_basics].SUFFIXES[1000][0]}'.format(sys))
    # using f-string format
    print(4, f'1MB = 1000{sys.modules["r1d5_functions_basics"].SUFFIXES[1000][0]}')
    # methods
    s = '''Finished files are the
result of years of scientific
study combined with the
experience of years.'''
    print(5, s)
    print(6, s.splitlines())
    print(7, s.lower())
    print(8, s.upper())
    print(9, s.lower().count('f'))
    query = 'user=pilgrim&database=master&password=PapayaWhip'
    list_1 = query.split('&')
    print(10, query)
    print(11, list_1)
    list_2 = [v.split('=', 1) for v in list_1 if '=' in v]
    print(12, list_2)
    dict_1 = {i[0]:i[1] for i in list_2}
    print(13, dict_1)
    # a more easier way
    dict_2 = dict(list_2)
    print(14, dict_2)

def run_bytes():
    ''''''
    print('\nbytes')
    by = b'abcd\x65'
    print(1, by)
    print(2, type(by))
    print(3, len(by))
    by += b'\xff'
    print(4, by)
    print(5, len(by))
    print(6, by[0])
    print(7, by[4])
    print(8, by[-1])
    print(9, b'\x77')
    barr = bytearray(by)
    print(10, barr, type(barr))
    print(11, len(barr))
    barr[-1] = 102
    print(12, barr)
    by2 = b'c'
    s1 = 'abcd'
    # print(13, s1 + by2) # TypeError: must be str, not bytes
    dec = by2.decode('ascii')
    print(13, dec)
    print(14, s1 + dec)
    print(15, (s1 + dec).count(dec))
    s2 = 'c'
    print(16, s2.encode('ascii'), s2.encode('ascii') == by2)
    string_1 = '深入 Python'
    print(17, string_1)
    print(18, string_1.encode('utf-8'))
    print(19, string_1.encode('gb18030'))
    print(20, string_1.encode('big5'))
    roundtrip = (string_1.encode('big5')).decode('big5')
    print(21, roundtrip, string_1 == roundtrip)

if __name__ == '__main__':
    run_strings()
    run_bytes()

'''
output:

strings
1 深入öñ Python 11
2 深
3 深入öñ Python 3

format
1 ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
2 1000KB = 1MB
3 1MB = 1000KB
4 1MB = 1000KB
5 Finished files are the
result of years of scientific
study combined with the
experience of years.
6 ['Finished files are the', 'result of years of scientific', 'study combined with the', 'experience of years.']
7 finished files are the
result of years of scientific
study combined with the
experience of years.
8 FINISHED FILES ARE THE
RESULT OF YEARS OF SCIENTIFIC
STUDY COMBINED WITH THE
EXPERIENCE OF YEARS.
9 6
10 user=pilgrim&database=master&password=PapayaWhip
11 ['user=pilgrim', 'database=master', 'password=PapayaWhip']
12 [['user', 'pilgrim'], ['database', 'master'], ['password', 'PapayaWhip']]
13 {'user': 'pilgrim', 'database': 'master', 'password': 'PapayaWhip'}
14 {'user': 'pilgrim', 'database': 'master', 'password': 'PapayaWhip'}

bytes
1 b'abcde'
2 <class 'bytes'>
3 5
4 b'abcde\xff'
5 6
6 97
7 101
8 255
9 b'w'
10 bytearray(b'abcde\xff') <class 'bytearray'>
11 6
12 bytearray(b'abcdef')
13 c
14 abcdc
15 2
16 b'c' True
17 深入 Python
18 b'\xe6\xb7\xb1\xe5\x85\xa5 Python'
19 b'\xc9\xee\xc8\xeb Python'
20 b'\xb2`\xa4J Python'
21 深入 Python True
'''