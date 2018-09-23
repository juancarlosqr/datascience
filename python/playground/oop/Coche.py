#!/usr/bin/python

# Begin Definicion de Clases

class Coche:
	mygasolina = 0

	def __init__(self,tipo = "Coche"):
		print "Se ha creado un nuevo " + tipo
		print " - Valor inicial de Gasolina: " + str( self.mygasolina ) + " litro(s)"

	def setGasolina(self, gasolina):
		self.mygasolina += gasolina
		self.printGasolina("cargar")

	def getGasolina(self,tipo = 'int'):
		if tipo == 'str':
			return str( self.mygasolina )
		else:
			return self.mygasolina

	def printGasolina(self,action):
		print "Gasolina luego de " + action + ": " + self.getGasolina("str") + " litros(s)"
		
    def avanzar( self,valor = 5 ):
		if ( self.getGasolina() - valor < 0 ):
			print "No puede avanzar, se quedo sin gasolina"
			return 0
        self.mygasolina -= valor
        self.printGasolina("avanzar")

class Formula1(Coche):
	def avanzar(self, valor = 10 ):
            if ( self.getGasolina() - valor < 0 ):
                    print "No puede avanzar, se quedo sin gasolina"
                    return 0
		self.mygasolina -= valor
		self.printGasolina("avanzar")

# End Definicion de Clases

salto = "******************************************************"
print salto
print " "
miCoche = Coche()
miCoche.setGasolina(15)
miCoche.avanzar()
miCoche.avanzar()
miCoche.avanzar()
miCoche.avanzar()
print " "
miF1 = Formula1("Formula 1")
miF1.setGasolina(15)
miF1.avanzar()
miF1.avanzar()
print " "
print salto
raw_input("Presione ENTER para salir...")
