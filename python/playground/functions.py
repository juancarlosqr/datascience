#!/usr/bin/env python

def print_type(obj):
	"""Esta funcion imprime el tipo de datoy el valor de obj"""
	print type(obj)
	print obj
	return True

def sum_mul(param1, param2):
	s = param1 + param2
	m = param1 * param2
	return s,m

def operaciones(param1, param2):
	return param1+param2,param1-param2,param1*param2,param1/param2

print "Inicia el programa"

c = "Hola mundo"
e = 23
r = 0.314
b = True
# listas (array)
l = [22, True, "una lista", [1,2]]
l2 = [9,8,7,6,5,4,3,2,1,0]
# tuplas
t = (1,2,False,"python")
# diccionario
d = {"primero":"Ubuntu","segundo":"Debian","tercero":"Fedora"}

val = print_type(c)
print val

print_type(e)

#print_type(r)

#print_type(b)

#print_type(l)
print l[2]
print l[3][1]
print l[-1][-1]
print l2
print l2[1:5]
print l2[1:5:3]
print type(t)
print t

#t[1] = 0
#print type(t)
#print t

print_type(d)
print d["segundo"]

n1 = 2
n2 = 6
s,m = sum_mul(n1,n2)
print s
print m

print "Ahora utilizando operaciones"
todas = operaciones(6,2)
for valor in todas:
	print valor

# b = True
if b:
	print "Presione ENTER para salir..."
	raw_input("> ")

print 0

