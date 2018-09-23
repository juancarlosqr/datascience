'''
Created on Mar 22, 2012

@author: juanc
'''
print 'Hello World'

def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y + a

def newMethod():
    return True

print add(1,2)
print addFixedValue(1)
raw_input('Presione ENTER para salir')