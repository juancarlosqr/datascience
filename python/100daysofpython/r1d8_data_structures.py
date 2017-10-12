#!/usr/bin/env python3

def run_list():
    ''''''
    print('\nlists')
    # shopping list
    shop = ['apple', 'mango', 'carrot', 'banana']

    print(1, 'i have', len(shop), 'items')
    print(2, 'the items are', end=' ')
    for item in shop:
        print(item, end=' ')
    print()
    print(3, 'adding rice')
    shop.append('rice')
    print(4, 'shop list', shop)
    shop.sort()
    print(5, 'sort', shop)
    print(6, 'first item is', shop[0])
    olditem = shop[0]
    del shop[0]
    print(7, 'i bought', olditem)
    print(8, 'shop list now', shop)
    print(9, shop[::2]) # third argument on slicing is the step

def run_tuple():
    ''''''
    zoo = ('python', 'elephant', 'penguin')
    print('\ntuples')
    print(1, 'numbers of animals', len(zoo))
    print(2, 'zoo', zoo)
    # parentheses not required but are a good idea
    new_zoo = 'monkey', 'camel', zoo
    print(3, 'cages in the new zoo', len(new_zoo))
    print(4, 'new zoo', new_zoo)
    print(5, 'animals from old zoo', new_zoo[2])
    print(6, 'last animal from old zoo is', new_zoo[2][2])
    print(7, 'number of animals in new zoo', len(new_zoo)-1+len(new_zoo[2]))
    not_a_tuple = (2)
    print(8, type(not_a_tuple))
    a_tuple = (2,)
    print(9, type(a_tuple), len(a_tuple))

def run_dict():
    ''''''
    print('\ndictionaries')
    # ab is short for address book
    ab = {
        'swaroop': 'swaroop@swaroop.com',
        'larry': 'larry@swaroop.com',
        'matsumoto': 'matsumoto@swaroop.com',
        'spammer': 'spammer@swaroop.com',
    }
    print(1, 'address book', ab)
    print(2, 'swaroop email is', ab['swaroop'])
    del ab['spammer']
    print(3, 'address book', ab)
    print(4, f'there are {len(ab)} contacts in the address book')
    for name, email in ab.items():
        print(f'{name}\'s email is {email}')
    ab['guido'] = 'guido@python.org'
    if 'guido' in ab:
        print(5, 'we have guido!')

def run_set():
    ''''''
    print('\nsets')
    bri = set(['brazil', 'russia', 'india'])
    print(1, 'bri', bri)
    print(2, 'us in bri:', 'us' in bri)
    print(3, 'india in bri:', 'india' in bri)
    bric = bri.copy()
    bric.add('china')
    print(4, 'bric', bric)
    print(5, 'bric is superset of bri?', bric.issuperset(bri))
    print(6, 'bri is subset of bric', bri.issubset(bric))
    bri.remove('russia')
    print(7, bri & bric) # or bri.intersect

def run_reference():
    ''''''
    print('\nreferences')
    print(1, 'assignment')
    shop1 = ['apple', 'mango', 'carrot']
    # shop2 is just another name pointing to the same object
    shop2 = shop1
    print(2, 'shop1', id(shop1), shop1)
    print(3, 'shop2', id(shop2), shop2)
    del shop1[0]
    print(4, 'first item removed')
    print(5, 'shop1', id(shop1), shop1)
    print(6, 'shop2', id(shop2), shop2)
    # make a copy by doing a full slice
    shop3 = shop1[:]
    print(7, 'shop1', id(shop1), shop1)
    print(8, 'shop3', id(shop3), shop3)
    del shop1[0]
    print(9, 'first item removed')
    print(10, 'shop1', id(shop1), shop1)
    print(11, 'shop3', id(shop3), shop3)

def run_string():
    ''''''
    print('\nstrings')
    name = 'swaroop'
    print(1, 'find', name.find('oop')) # index 4
    delimiter = '_*_'
    bric = ['brazil', 'russia', 'india', 'china']
    print(2, delimiter.join(bric))

if __name__ == '__main__':
    run_list()
    run_tuple()
    run_dict()
    run_set()
    run_reference()
    run_string()

'''
output:

lists
1 i have 4 items
2 the items are apple mango carrot banana 
3 adding rice
4 shop list ['apple', 'mango', 'carrot', 'banana', 'rice']
5 sort ['apple', 'banana', 'carrot', 'mango', 'rice']
6 first item is apple
7 i bought apple
8 shop list now ['banana', 'carrot', 'mango', 'rice']
9 ['banana', 'mango']

tuples
1 numbers of animals 3
2 zoo ('python', 'elephant', 'penguin')
3 cages in the new zoo 3
4 new zoo ('monkey', 'camel', ('python', 'elephant', 'penguin'))
5 animals from old zoo ('python', 'elephant', 'penguin')
6 last animal from old zoo is penguin
7 number of animals in new zoo 5
8 <class 'int'>
9 <class 'tuple'> 1

dictionaries
1 address book {'swaroop': 'swaroop@swaroop.com', 'larry': 'larry@swaroop.com', 'matsumoto': 'matsumoto@swaroop.com', 'spammer': 'spammer@swaroop.com'}
2 swaroop email is swaroop@swaroop.com
3 address book {'swaroop': 'swaroop@swaroop.com', 'larry': 'larry@swaroop.com', 'matsumoto': 'matsumoto@swaroop.com'}
4 there are 3 contacts in the address book
swaroop's email is swaroop@swaroop.com
larry's email is larry@swaroop.com
matsumoto's email is matsumoto@swaroop.com
5 we have guido!

sets
1 bri {'india', 'russia', 'brazil'}
2 us in bri: False
3 india in bri: True
4 bric {'china', 'india', 'russia', 'brazil'}
5 bric is superset of bri? True
6 bri is subset of bric True
7 {'india', 'brazil'}

references
1 assignment
2 shop1 4392613192 ['apple', 'mango', 'carrot']
3 shop2 4392613192 ['apple', 'mango', 'carrot']
4 first item removed
5 shop1 4392613192 ['mango', 'carrot']
6 shop2 4392613192 ['mango', 'carrot']
7 shop1 4392613192 ['mango', 'carrot']
8 shop3 4392837192 ['mango', 'carrot']
9 first item removed
10 shop1 4392613192 ['carrot']
11 shop3 4392837192 ['mango', 'carrot']

strings
1 find 4
2 brazil_*_russia_*_india_*_china
'''