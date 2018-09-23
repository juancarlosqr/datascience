#!/usr/bin/python

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

print type(c)
print c*2

print type(e)
print e

print type(r)
print r

print type(b)
print b

print type(l)
print l
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

print type(d)
print d
print d["segundo"]

# b = True
if b:
	print "Presione ENTER para salir..."
	raw_input("> ")

print 0
