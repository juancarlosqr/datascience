#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

def main13():
    script, first, second, third = argv
    print "The script is called: ", script
    print "First variable is: ", first
    print "Second variable is: ", second
    print "Third variable is: ", third

def main14():
    script, username = argv
    prompt = '# '
    print "%10s %5d" % ("Day", 18)
    print "%10s %5d" % ("Month", 9)
    print "%10s %5d" % ("Year", 1987)

    print "Hi %s, I'm the %s script" % (username, script)
    print "I'd would like to ask you a few questions "

    print "Do you like me %s?" % username
    likes = raw_input(prompt)

    print "Where do you live %s?" % username
    lives = raw_input(prompt)

    print "What kind of computer do you have %s?" % username
    computer = raw_input(prompt)

    print """
    Alright, so you said %r about liking me. 
    You live in %r, Not sure where that is.
    And you have a %r computer. Nice
    """ % (likes, lives, computer)

def main15():
    script, filename = argv
    txt = open(filename)

    print "Here is your file %r" % filename
    print txt.read()

    print "Type the file again:"
    file_again = raw_input("$ ")

    txt_again = open(file_again)
    print txt_again.read()

def main16():
    script, filename = argv
    print "Erasing file %s" % filename
    print "Press Ctrl-C to cancel or RETURN if it's ok"
    raw_input("? ")

    print "Opening the file..."
    target = open(filename, 'w')

    print "Truncating the file..."
    target.truncate()

    print "I'm going to ask you two lines..."
    line1 = raw_input("line1: ")
    line2 = raw_input("line2: ")

    print "Writing lines to file..."
    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")

    print "Closing file..."
    target.close()

    print "Printing file..."
    target = open(filename)
    print target.read()
    target.close()

def main():
    script, from_file, to_file = argv
    print "Copyinf from %s to %s" % (from_file, to_file)

    in_file = open(from_file) ; in_data = in_file.read()

    print "The input file is %d bytes long" % len(in_data)

    print "Output file exists? %r" % exists(to_file)
    print "Press Ctrl-C to cancel or RETURN if it's ok"
    raw_input("? ")

    out_file = open(to_file, 'w')
    out_file.write(in_data)

    print "Alright, all done."

    out_file.close()
    in_file.close()

if __name__ == "__main__":
    main()