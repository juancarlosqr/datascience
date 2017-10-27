#!/usr/bin/env python3

import r1d19_generators

class SchoolMember:
    ''''''

    def __init__(self, name, time=None):
        ''''''
        self.name = name
        self.time = time
        print(f'(New School Member: {self.name})')

    def tell(self):
        ''''''
        print(f'My name is {self.name}.', end=' ')

    def go(self):
        ''''''
        print(f'I go home at {self.time}')

class Teacher(SchoolMember):
    ''''''

    def __init__(self, name, time, salary):
        ''''''
        SchoolMember.__init__(self, name, time) # using super class name, need to pass self
        self.salary = salary
        print(f'(New Teacher: {self.name})')

    def tell(self):
        ''''''
        SchoolMember.tell(self)
        print(f'My salary is {self.salary}')

class Student(SchoolMember):
    ''''''

    def __init__(self, name, mark):
        ''''''
        super().__init__(name) # using super() method, don't need to pass self
        self.marks = mark
        print(f'(New Student: {self.name})')

    def tell(self):
        ''''''
        SchoolMember.tell(self)
        print(f'My mark is {self.marks}')

    def go(self):
        ''''''
        print('I always go home at 1pm')

def run_oop1():
    ''''''
    print('\noop1')
    janet = Teacher('Janet', '4pm', 60000)
    # a field (salary) could be of different type between instances
    john = Teacher('John', '6pm', 'A')
    jim = Student('Jim', 'A')
    members = [janet, john, jim]
    print()
    for member in members:
        member.tell()
        member.go()
        if isinstance(member, SchoolMember):
            print('A School Member!')
        if isinstance(member, Teacher):
            print('A Teacher!')
        if isinstance(member, Student):
            print('A Student!')

class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        ''''''
        self.max = max

    def __iter__(self):
        ''''''
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        ''''''
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

def run_oop2():
    ''''''
    print('\noop2')
    x = Fib(100)
    print(1, x)
    print(2, x.__class__, type(x))
    print(3, x.__doc__)
    print(4, type(Fib))
    iter(x)
    print(5, next(x))
    iter(x) # resets counters
    print(5, next(x))
    print(5, next(x))
    # using Fib iterator
    for n in Fib(100):
        print(n, end=' ')
    print()

class LazyRules:
    ''''''
    file_name = 'r1d18_rules.txt'

    def __init__(self):
        ''''''
        self.pattern_file = open(LazyRules.file_name, encoding='utf-8') # self.file_name is valid too
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]
        if self.pattern_file.closed:
            raise StopIteration
        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = r1d19_generators.build_match_and_apply_functions(
            pattern, search, replace)
        self.cache.append(funcs)
        return funcs

def run_oop3():
    ''''''
    print('\noop3')
    rules = LazyRules()
    # manual iteration with iter and next
    print(rules, type(rules))
    iter(rules)
    print(next(rules))
    print(next(rules))
    print(next(rules))
    print(next(rules))
    # print(next(rules)) # raise StopIteration
    #
    # automatic iteration with for
    print('\nnouns', r1d19_generators.nouns)
    for noun in r1d19_generators.nouns:
        for match, apply in LazyRules():
            if match(noun):
                plural = apply(noun)
                break
        print(noun, plural)

if __name__ == '__main__':
    run_oop1()
    run_oop2()
    run_oop3()

'''
output:

oop1
(New School Member: Janet)
(New Teacher: Janet)
(New School Member: John)
(New Teacher: John)
(New School Member: Jim)
(New Student: Jim)

My name is Janet. My salary is 60000
I go home at 4pm
A School Member!
A Teacher!
My name is John. My salary is A
I go home at 6pm
A School Member!
A Teacher!
My name is Jim. My mark is A
I always go home at 1pm
A School Member!
A Student!

oop2
1 <__main__.Fib object at 0x10ddc04e0>
2 <class '__main__.Fib'> <class '__main__.Fib'>
3 iterator that yields numbers in the Fibonacci sequence
4 <class 'type'>
5 0
5 0
5 1
0 1 1 2 3 5 8 13 21 34 55 89 

oop3
<__main__.LazyRules object at 0x10ddc04e0> <class '__main__.LazyRules'>
(<function build_match_and_apply_functions.<locals>.match_rule at 0x10ddbe9d8>, <function build_match_and_apply_functions.<locals>.apply_rule at 0x10ddbea60>)
(<function build_match_and_apply_functions.<locals>.match_rule at 0x10ddbeae8>, <function build_match_and_apply_functions.<locals>.apply_rule at 0x10ddbeb70>)
(<function build_match_and_apply_functions.<locals>.match_rule at 0x10ddbebf8>, <function build_match_and_apply_functions.<locals>.apply_rule at 0x10ddbec80>)
(<function build_match_and_apply_functions.<locals>.match_rule at 0x10ddbe950>, <function build_match_and_apply_functions.<locals>.apply_rule at 0x10ddbed08>)

nouns ['bass', 'fax', 'waltz', 'coach', 'rash', 'cheetah', 'currency', 'vacancy', 'agency', 'day', 'book']
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
'''