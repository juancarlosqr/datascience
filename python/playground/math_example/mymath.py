#!/usr/bin/env python
'''
Created on Mar 22, 2012
@author: juanc
'''

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b

def divide(a,b):
	if b == 0:
		return "Zero division not allowed"
	else:
	    return a/b

def operation(a,b,o):

	a = int(a)
	b = int(b)

	if o == "+":
		return plus(a, b)

	elif o == "-":
		return minus(a, b)

	elif o == "*":
		return multi(a, b)

	elif o == "/":
		return divide(a, b)

	else:
		print "Operation not allowed"

def help():
	print ""
	print "Module %s imported successfully" % __name__
	print "Operations allowed:"
	print "plus(a,b)"
	print "minus(a,b)"
	print "multi(a,b)"
	print "divide(a,b)"
	print ""

def main():
	help()
	print add(1,2)
	print addFixedValue(1)
	raw_input('Presione ENTER para salir')

if __name__ == "__main__":
	main()
else:
	help()