version = 14

print(version)

language = "python"

print(language)

# multiple declaration
name, age, day = "john", 25, "tuesday"

print(name, age,  day)

# ValueError: too many values to unpack
# v1, v2 = "basics"

# multiple assignment
v1 = v2 = "basics"

print(v1, v2)

# data types: int, string, list, tuple, dictionary

# operators

grade1 = 8
grade2 = 2
sum = grade1 + grade2
minus = grade1 - grade2
mult = grade1 * grade2
div = grade1 / grade2
mod = grade1 % grade2

print(grade1, grade2, sum, minus, mult, div, mod)

# strings

one = "monty"
space = " "
two = "python"
name = one + space + two
print(name)
print(name[6])
print(name[0:5])
print(name[5])
print(name[6:11])
print(name[6:12])
print(name[6:20])
print(name[:])
print(name[:8])
print(name[3:])
print(name[:-1])
print(name[-2:-5])
print(name[-6:])
print(name[-6:-2])

# placeholders

print("%s license" % ("license"))
mit, gnu = "mit", "gnu"
print("%s license" % (mit))
print("%s license" % gnu)
print("%s and %s licenses" % (mit, gnu))
challenge, day = 100, 2
print("this is the %d days of %s challenge and i'm on day %d" % (challenge, two, day))

"""
output:

14
python
john 25 tuesday
basics basics
8 2 10 6 16 4.0 0
monty python
p
monty
 
pytho
python
python
monty python
monty py
ty python
monty pytho

python
pyth
license license
mit license
gnu license
mit and gnu licenses
this is the 100 days of python challenge and i'm on day 2
"""
