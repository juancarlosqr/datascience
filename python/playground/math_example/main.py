#!/usr/bin/env python

#import mymath
from mymath import operation

def main():

	#print "7 + 6:", mymath.plus(7,6)
	#print "7 - 6:", mymath.minus(7,6)
	#print "7 * 6:", mymath.multi(7,6)
	#print "7 / 6:", mymath.divide(7,6)
	#print "7 / 0:", mymath.divide(7,0)
	#print ""
	a = raw_input('Valor a:')
	b = raw_input('Valor b:')
	o = raw_input('Operacion:')
	#print mymath.operation(a,b,o)
	print operation(a,b,o)
	raw_input('Presione ENTER para salir')

if __name__ == "__main__":
	main()