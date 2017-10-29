#!/usr/bin/env python3

import sys
import time

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def run_pal():
    ''''''
    print('\nis palindrome')
    text = input('write a word: ')
    if is_palindrome(text):
        print('is palindrome')
    else:
        print('is not palindrome')

def run_excep():
    ''''''
    try:
        prin('wrong')
        print(1/0)
        print('everything is ok')
    except NameError:
        print('name error')
    except:
        print('very wrong')
    else:
        print('bye')

class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        self.__message = f'ShortInputException: Input was {self.length} long. Expected at least {self.atleast}'
    def message(self):
        return self.__message

def run_raise():
    ''''''
    print('\nraise')
    text = 'foo'
    try:
        if len(text) < 5:
            raise ShortInputException(len(text), 5)
    except ShortInputException as ex:
        print(ex.message())
    print('available attributes of ShortInputException')
    print(dir(ShortInputException))

def run_finally():
    ''''''
    print('\nfinally')
    f = None
    try:
        f = open('r1d23_names.txt')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line, end=' ')
            sys.stdout.flush()
            print('press ctrl + c')
            time.sleep(2)
    except IOError:
        print('could not find file')
    except KeyboardInterrupt:
        print('you cancelled the reading from the file')
    finally:
        if f:
            f.close()
        print('file closed')

if __name__ == '__main__':
    # run_pal()
    run_excep()
    run_raise()
    run_finally()

'''
output:

name error

raise
ShortInputException: Input was 3 long. Expected at least 5
available attributes of ShortInputException
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', '__weakref__', 'args', 'message', 'with_traceback']

finally
Dora
 press ctrl + c
Ethan
 press ctrl + c
Wesley
 press ctrl + c
John
 press ctrl + c
Anne
 press ctrl + c
Mike
 press ctrl + c
Chris
 press ctrl + c
Sarah
 press ctrl + c
Alex
 press ctrl + c
Lizzie press ctrl + c
file closed
'''