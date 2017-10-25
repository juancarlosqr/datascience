#!/usr/bin/env python3

import math
import sys

class Course:
    def __init__(self, title='python', price=10):
        self.title = title
        self.__price = price  # private property
        self.__isPublic = False  # private property
        self.__passwd = 'foo'

    def get_title(self):
        return f'{self.title} course'

    def get_price(self):
        return f'${self.__price}'

    def is_public(self):
        return self.__isPublic

    def __publish(self):  # private method
        self.__isPublic = True

    def publish(self, passwd):
        if (passwd == self.__passwd):
            self.__publish()


def run_oop1():
    ''''''
    print('\noop1')
    c1 = Course()
    print(1, c1.get_title())
    print(1, c1, type(c1), id(c1), sys.getsizeof(c1))
    c2 = Course('data analysis')
    print(2, c2.get_title())
    c2.title = 'dummy'
    print(2, c2.get_title())
    c3 = Course('machine learning')
    print(3, c3.get_title())
    print(3, c3.get_price())
    c3.title = 'ml'
    c3.__price = 9
    print(3, c3.get_title())
    print(3, c3.get_price())
    print(3, c3.is_public())
    # c3.__publish() # AttributeError: 'Course' object has no attribute '__publish'
    c3.publish('baz')
    print(3, c3.is_public())
    c3.publish('foo')
    print(3, c3.is_public())


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)

    def __len__(self):
        return f'{str(self.get_radius())} radius inch'

    def __str__(self):
        return f'A {str(self.get_radius())}-radius awesome circle'


def run_oop2():
    ''''''
    print('\noop2 (operator overloading)')
    c1 = Circle(4)
    c2 = Circle(5)
    print(1, c1.get_radius())
    print(2, c2.get_radius())
    c3 = c1 + c2
    print(3, 'add', c3.get_radius())
    print(4, c3)
    print(5, c3.__len__())
    # print(6, len(c3)) # TypeError: 'str' object cannot be interpreted as an integer


class Robot:
    '''Represents a Robot, with a name'''

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        '''Initializes data'''
        self.name = name # object variable
        print(f'(Initializing {self.name})')
        # when robot is created, increase population
        Robot.population += 1

    def die(self):
        '''dying'''
        print(f'{self.name} is being destroyed')
        # decrease population
        if Robot.population > 0:
            Robot.population -= 1
        else:
            print('Zero robots working')
            return

        if Robot.population == 0:
            print(f'{self.name} was last one')
        else:
            print(f'There are still {str(Robot.population)} robots working')

    def greet(self):
        '''greeting the robot

        They can say hi'''
        print(f'Greetings, my masters call me {self.name}')

    @classmethod
    def how_many(cls):
        '''print current population'''
        print(f'We have {str(cls.population)} robots')


def run_oop3():
    ''''''
    print('\noop3 (class and instance variables and methods)')
    print(Robot.__doc__)
    droid1 = Robot('R2-D2')
    droid1.greet()
    Robot.how_many()

    droid2 = Robot('C-3PO')
    droid2.greet()
    Robot.how_many()

    print('\nrobots do some hard work here')

    print('\nrobots finished their jobs. time to destroy them')
    droid1.die()
    Robot.how_many()
    droid2.die()
    Robot.how_many()


if __name__ == '__main__':
    run_oop1()
    run_oop2()
    run_oop3()

'''
output:

oop1
1 python course
1 <__main__.Course object at 0x10c300d68> <class '__main__.Course'> 4499443048 56
2 data analysis course
2 dummy course
3 machine learning course
3 $10
3 ml course
3 $10
3 False
3 False
3 True

oop2 (operator overloading)
1 4
2 5
3 add 9
4 A 9-radius awesome circle
5 9 radius inch

oop3 (class and instance variables and methods)
Represents a Robot, with a name
(Initializing R2-D2)
Greetings, my masters call me R2-D2
We have 1 robots
(Initializing C-3PO)
Greetings, my masters call me C-3PO
We have 2 robots

robots do some hard work here

robots finished their jobs. time to destroy them
R2-D2 is being destroyed
There are still 1 robots working
We have 1 robots
C-3PO is being destroyed
C-3PO was last one
We have 0 robots
'''