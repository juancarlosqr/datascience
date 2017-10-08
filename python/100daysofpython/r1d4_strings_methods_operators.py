import math

# name = input('name: ')
# grade = int(input('grade: '))
#
# print(f'Hi {name}, your grade was {grade}')

print(math.pi)

i = 10
j = 2.5
k = 5+7j

print(i * j)
print(k)
print(type(i), type(j), type(k))

print(3 / 2)
print(3 // 2)
print(2 ** 3)
print(7 % 3)

print(3 * 4 + 1)
print(3 * (4 + 1))

count = 10
count += 2
print(count)

empty = str()
foo = str('foo')
print(f'empty is {empty} and foo is {foo}')

# strings are immutable
# id() returns memory address
foo1 = 'foo'
foo2 = 'foo'
print(f'foo1 {foo1} id is {id(foo1)} and foo2 {foo2} id is {id(foo2)}')
foo1 += ' bar' # doesn't mutate original string, instead creates a new one
print(f'foo1 {foo1} id is {id(foo1)} and foo2 {foo2} id is {id(foo2)}')

spam = 'spam '
print(spam * 10)

# ord() – function returns the ASCII code of the character.
# chr() – function returns character represented by a ASCII number.
ch = 'b'
cod = 97
print(f'the ascii code of {ch} is {ord(ch)}')
print(f'the character represented by ascii code {cod} is {chr(cod)}')

name = 'monty python'
print(len(name))
print(min(name)) # the min value is the space char (ascii code 32)
print(min('name')) # is a
print(max(name))
print('ty' in name)
print('ty' not in name)

# python compares string lexicographically i.e using ASCII value of the characters.
print(1, 'tim' == 'tie') # False
print(2, 'free' != 'freedom') # True
print(3, 'arrow' > 'aron') # True
print(4, 'right' >= 'left') # True
print(5, 'teeth' < 'tee') # False
print(5, 'yellow' <= 'fellow') # False
print(6, 'abc' > '') # True
print(7, ord('a'))
# error: TypeError: ord() expected a character, but string of length 0 found
# print(8, ord(''))
print(9, ord(' '))

for i in name:
    print(i, end='')

print('string methods')

print('searching')
print(1, 'welcome to python'.isalnum())
print(2, 'welcome'.isalpha())
print(3, '2017'.isdigit())
print(4, '.5'.isdecimal())
print(5, name.isidentifier())
print(6, 'print'.isidentifier())
print(7, 'welcome'.islower())
print(8, 'FOO'.isupper())
print(9, ' \t'.isspace())
print(10, 'bar'.isprintable())
print(11, 'd'.istitle())
print(12, 'Title'.istitle())

print('testing')
print(13, name.endswith('on'))
print(14, name.startswith('mo'))
print(15, name.count('o'))
print(16, name.find('o'))
print(17, name.rfind('o'))

print('converting')
print(18, name.capitalize())
print(19, name.lower())
print(20, name.upper())
print(21, name.title())
print(22, name.swapcase())
print(23, name.replace('python', 'pycharm'))

print('char by ascii code')
for code in range(32,133):
    print(code, chr(code))

help(min)
help(str.isdecimal)
help(str.isprintable)
help(repr)
help(eval)
help(str.istitle)

'''
output:

3.141592653589793
25.0
(5+7j)
<class 'int'> <class 'float'> <class 'complex'>
1.5
1
8
1
13
15
12
empty is  and foo is foo
foo1 foo id is 4344919352 and foo2 foo id is 4344919352
foo1 foo bar id is 4345011032 and foo2 foo id is 4344919352
spam spam spam spam spam spam spam spam spam spam 
the ascii code of b is 98
the character represented by ascii code 97 is a
12
 
a
y
True
False
1 False
2 True
3 True
4 True
5 False
5 False
6 True
7 97
9 32
monty pythonstring methods
searching
1 False
2 True
3 True
4 False
5 False
6 True
7 True
8 True
9 True
10 True
11 False
12 True
testing
13 True
14 True
15 2
16 1
17 10
converting
18 Monty python
19 monty python
20 MONTY PYTHON
21 Monty Python
22 MONTY PYTHON
23 monty pycharm
char by ascii codes
32  
33 !
34 "
35 #
36 $
37 %
38 &
39 '
40 (
41 )
42 *
43 +
44 ,
45 -
46 .
47 /
48 0
49 1
50 2
51 3
52 4
53 5
54 6
55 7
56 8
57 9
58 :
59 ;
60 <
61 =
62 >
63 ?
64 @
65 A
66 B
67 C
68 D
69 E
70 F
71 G
72 H
73 I
74 J
75 K
76 L
77 M
78 N
79 O
80 P
81 Q
82 R
83 S
84 T
85 U
86 V
87 W
88 X
89 Y
90 Z
91 [
92 \
93 ]
94 ^
95 _
96 `
97 a
98 b
99 c
100 d
101 e
102 f
103 g
104 h
105 i
106 j
107 k
108 l
109 m
110 n
111 o
112 p
113 q
114 r
115 s
116 t
117 u
118 v
119 w
120 x
121 y
122 z
123 {
124 |
125 }
126 ~
127 
128 
129 
130 
131 
132 
Help on built-in function min in module builtins:

min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.

Help on method_descriptor:

isdecimal(...)
    S.isdecimal() -> bool
    
    Return True if there are only decimal characters in S,
    False otherwise.

Help on method_descriptor:

isprintable(...)
    S.isprintable() -> bool
    
    Return True if all characters in S are considered
    printable in repr() or S is empty, False otherwise.

Help on built-in function repr in module builtins:

repr(obj, /)
    Return the canonical string representation of the object.
    
    For many object types, including most builtins, eval(repr(obj)) == obj.

Help on built-in function eval in module builtins:

eval(source, globals=None, locals=None, /)
    Evaluate the given source in the context of globals and locals.
    
    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.

Help on method_descriptor:

istitle(...)
    S.istitle() -> bool
    
    Return True if S is a titlecased string and there is at least one
    character in S, i.e. upper- and titlecase characters may only
    follow uncased characters and lowercase characters only cased ones.
    Return False otherwise.
'''