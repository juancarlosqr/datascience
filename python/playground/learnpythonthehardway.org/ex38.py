#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Thing(object):
    """Simple class"""
    def test(__self__,hi):
        print hi

def main():
    print 'main'
    a = Thing()
    a.test('you')
    print a.__doc__

    ten_things = 'Apples Oranges Crows Telephone Light Sugar'
    print 'Wait there is not 10 things in that list, let me fix that.'

    stuff = ten_things.split(' ')
    more_stuff = ['Day','Night','Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

    while len(stuff) != 10:
        next_one = more_stuff.pop() 
        print 'Adding: ', next_one 
        stuff.append(next_one)
        print 'There is %d items now.' % len(stuff)

    print "There we go", stuff
    print "Let's do dome things with stuff"

    print stuff[1]
    print stuff[-1] # fancy!
    print stuff.pop()
    print ' '.join(stuff) # cool
    print '#'.join(stuff[3:5]) # very cool

if __name__ == '__main__':
    main() 