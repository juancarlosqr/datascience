#!/usr/bin/python

class Car(object):
	"""docstring for Car"""

	def __init__(self, color):
		self.color = color
		self.wheels = 4
	
	def printInfo(self):
		print "This is a " + self.color + " Car of " + str( self.wheels ) + " wheels"

class Truck(Car):
	"""docstring for Truck"""
	def __init__(self, color, wheels):
		self.color = color
		self.wheels = wheels

def main():
	myCar = Car("green")
	myCar.printInfo()

	myTruck = Truck("blue",6)
	myTruck.printInfo()
	raw_input("Presione ENTER para salir...")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()