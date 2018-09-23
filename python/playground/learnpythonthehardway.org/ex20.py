#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_line(line_count, f):
	print line_count, f.readline()

def print_line2(f):
	print f.readline(),

def main():
	current_file = open(filename)
	
	print "Printing the whole file \n"
	print_all(current_file)

	print "Lets rewind the file, like a tape"
	rewind(current_file)

	print "Lets print 2 lines"
	print_line(1,current_file)
	print_line(2,current_file)
	
	print "Lets rewind the file, like a tape"
	rewind(current_file)
	print_line2(current_file)
	print_line2(current_file)

	current_file.close()

if __name__ == "__main__":
	main()