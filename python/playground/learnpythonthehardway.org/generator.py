#!/usr/bin/env python
# -*- coding: utf-8 -*-

def simple_generator_function():
    yield 1
    yield 2
    yield 3

def withfor():
    for value in simple_generator_function():
        print(value)

def withnext():
    our_generator = simple_generator_function()
    print next(our_generator)
    print next(our_generator)
    print next(our_generator)

def main():
    print "with for"
    withfor()
    print "with next"
    withnext()

if __name__ == "__main__":
    main()
