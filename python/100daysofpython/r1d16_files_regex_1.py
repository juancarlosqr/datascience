#!/usr/bin/env python3

import pickle, re

def run_files():
    ''''''
    print('\nfiles')
    filename = 'r1d14.txt'
    f = open(filename, 'r')
    print(1, 'read', filename)
    print(2, f.readlines())
    f.close()
    # append
    print(3, 'append', filename)
    f = open(filename, 'a')
    f.write('me again\n')
    f.close
    # loop
    print(4, 'loop', filename)
    f = open(filename, 'r')
    for line in f:
        print(line, end='')
    f.close()
    print(5, 'loop', filename)
    with open(filename, 'r') as file:
        print(file.readlines())

def run_binary():
    ''''''
    print('\nbinary files')
    filename = 'r1d16_pick.dat'
    print(1, 'write binary', filename)
    f = open(filename, 'wb')
    pickle.dump(11, f)
    pickle.dump('A new awesome line', f)
    pickle.dump([1, 2, 3, 4], f)
    f.close()
    print(2, 'read binary', filename)
    f = open(filename, 'rb')
    print(3, pickle.load(f))
    print(4, pickle.load(f))
    print(5, pickle.load(f))
    # print(6, pickle.load(f)) # EOFError: Ran out of input
    f.close()

def run_regex():
    ''''''
    print('\nregex')
    ad = '100 NORTH MAIN ROAD'
    print(1, ad)
    print(2, ad.replace('ROAD', 'RD.'))
    ad = '100 NORTH BROAD ROAD'
    print(3, ad.replace('ROAD', 'RD.'))
    print(4, ad[:-4] + ad[-4:].replace('ROAD', 'RD.'))
    print(5, re.sub('ROAD$', 'RD.', ad))
    phone = '+1 897 665 32 43'
    print(7, 'phone', phone)
    print(6, re.sub('\+1 ^', '01', phone)) # not working
    ad = '100 NORTH BROAD'
    print(8, re.sub('ROAD$', 'RD.', ad)) # unexpected
    print(9, re.sub('\\bROAD$', 'RD.', ad))
    print(10, re.sub(r'\bROAD$', 'RD.', ad))
    ad = '100 NORTH BROAD ROAD APT. 3'
    print(11, re.sub(r'\bROAD$', 'RD.', ad))
    print(12, re.sub(r'\bROAD\b', 'RD.', ad))
    print(13, re.sub(r'^\+1', '01', phone)) # working now

def run_roman():
    '''
    Roman numbers:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    '''
    print('\nroman thousands')
    pattern = r'^M?M?M?$'
    print(1, 'search', re.search(pattern, 'M'))
    print(2, 'search', re.search(pattern, 'MM'))
    print(3, 'search', re.search(pattern, 'MMM'))
    print(4, 'search', re.search(pattern, 'MMMM'))
    print(5, 'search', re.search(pattern, ''))
    print('roman hundreds')
    pattern = r'^M?M?M?(CM|CD|D?C?C?C?)$'
    print(6, 'search', re.search(pattern, 'MCM'))
    print(7, 'search', re.search(pattern, 'MD'))
    print(8, 'search', re.search(pattern, 'MMMCCC'))
    print(9, 'search', re.search(pattern, 'MCMC'))
    print(10, 'search', re.search(pattern, ''))

if __name__ == '__main__':
    run_files()
    run_binary()
    run_regex()
    run_roman()

'''
output:

files
1 read r1d14.txt
2 ['hello python\n', 'bye python\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n']
3 append r1d14.txt
4 loop r1d14.txt
hello python
bye python
me again
me again
5 loop r1d14.txt
['hello python\n', 'bye python\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n', 'me again\n']

binary files
1 write binary r1d16_pick.dat
2 read binary r1d16_pick.dat
3 11
4 A new awesome line
5 [1, 2, 3, 4]

regex
1 100 NORTH MAIN ROAD
2 100 NORTH MAIN RD.
3 100 NORTH BRD. RD.
4 100 NORTH BROAD RD.
5 100 NORTH BROAD RD.
7 phone +1 897 665 32 43
6 +1 897 665 32 43
8 100 NORTH BRD.
9 100 NORTH BROAD
10 100 NORTH BROAD
11 100 NORTH BROAD ROAD APT. 3
12 100 NORTH BROAD RD. APT. 3
13 01 897 665 32 43

roman thousands
1 search <_sre.SRE_Match object; span=(0, 1), match='M'>
2 search <_sre.SRE_Match object; span=(0, 2), match='MM'>
3 search <_sre.SRE_Match object; span=(0, 3), match='MMM'>
4 search None
5 search <_sre.SRE_Match object; span=(0, 0), match=''>
roman hundreds
6 search <_sre.SRE_Match object; span=(0, 3), match='MCM'>
7 search <_sre.SRE_Match object; span=(0, 2), match='MD'>
8 search <_sre.SRE_Match object; span=(0, 6), match='MMMCCC'>
9 search None
10 search <_sre.SRE_Match object; span=(0, 0), match=''>
'''