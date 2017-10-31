#/usr/bin/env python3

import sys
import os
import platform
import logging
import time
import functools

def run_stdlib():
    ''''''
    print('\nstdlib')
    print(1, sys.version_info)
    print(2, sys.version_info.major == 3)
    print('\nlogging')
    file_name= 'r1d25_stdlib.log'
    if platform.platform().startswith('Windows'):
        logging_file = os.path.join( \
            os.getenv('HOMEDRIVE'), \
            os.getenv('HOMEPATH'), \
            file_name
        )
    else:
        logging_file = file_name
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]: %(message)s',
        filename=logging_file,
        filemode='w',
    )
    logging.debug('start program')
    logging.info('doing some hard work')
    logging.warning('hey! be careful')
    logging.error('chaos all over the place')
    print(1, 'check', logging_file)

def powersum(power, *args):
    ''''''
    return sum([pow(arg, power) for arg in args])

def run_more():
    ''''''
    print('\nmore')
    flag = 3
    if flag > 0: print('everything is ok')
    print('\nlambda')
    points = [{'x': 2, 'y': 3},
              {'x': 4, 'y': 1},
              {'x': 3, 'y': 2}]
    points.sort(key=lambda i: i['y'])
    print(1, points)
    print('\n*args')
    print(1, powersum(2, 3, 4))
    print(2, powersum(2, 10))
    print('\nassert')
    assert len(points) > 0

def retry(f):
    print('init retry')
    @functools.wraps(f)
    def wrapper_function(*args, **kwargs):
        print('init wrapper_function')
        MAX_ATTEMPTS = 2
        log = logging.getLogger('retry')
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception(f'Attempt {attempt}/{MAX_ATTEMPTS} failed: {(args, kwargs)}')
                time.sleep(5 * attempt)
        log.critical(f'All {MAX_ATTEMPTS } attempts failed: {(args, kwargs)}')
    return wrapper_function

@retry
def save_to_db(x):
    ''''''
    # This will be automatically retried if exception is thrown
    print('writing to db a zero division result')
    print(x / 0)

def increment(f):
    def wrap(*args, **kwargs):
        '''Wrong Increment function'''
        return f(*args, **kwargs) + 1
    return wrap

def right_increment(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        '''Right Increment function'''
        return f(*args, **kwargs) + 1
    return wrap

def right_sum(x, y):
    '''Right sum'''
    return x + y

@increment
def wrong_sum(x, y):
    '''Wrong sum'''
    return x + y

@right_increment
def better_wrong_sum(x, y):
    '''Better wrong sum'''
    return x + y

def run_decorators():
    ''''''
    print('\ndecorators')
    save_to_db(10)
    print(1, 'check r1d25_stdlib.log')
    print(2, 'right sum', right_sum(6, 4))
    print(3, 'wrong sum', wrong_sum(6, 4))
    print(4, right_sum.__name__)
    print(5, right_sum.__doc__)
    print(6, wrong_sum.__name__)
    print(6, wrong_sum.__doc__)
    print(7, 'better wrong sum', better_wrong_sum(6, 4))
    print(8, better_wrong_sum.__name__)
    print(9, better_wrong_sum.__doc__)

if __name__ == '__main__':
    run_stdlib()
    run_more()
    run_decorators()

'''
output:

init retry

stdlib
1 sys.version_info(major=3, minor=6, micro=1, releaselevel='final', serial=0)
2 True

logging
1 check r1d25_stdlib.log

more
everything is ok

lambda
1 [{'x': 4, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 3}]

*args
1 25
2 100

assert

decorators
init wrapper_function
writing to db a zero division result
writing to db a zero division result
1 check r1d25_stdlib.log
2 right sum 10
3 wrong sum 11
4 right_sum
5 Right sum
6 wrap
6 Wrong Increment function
7 better wrong sum 11
8 better_wrong_sum
9 Better wrong sum
'''