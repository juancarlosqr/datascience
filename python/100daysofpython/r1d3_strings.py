print(print)

subject = 'programming'
grade = 10

print('my grade on {0} was {1} '.format(subject, grade))
print('everybody was graded {} on that exercise'.format(grade))

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0 / 3))

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))

# keyword-based 'Swaroop wrote A Byte of Python'
name = 'Swaroop'
print('{name} wrote {book}'.format(name=name, book='A Byte of Python'))

print('a', end='')
print('b', end='')
print('c')

# new line
print('first line\nsecond line\ttab')

# no new line
lines = 'first line \
second line'
print(lines)

# raw string
print(r'new lines are indicated by \n')

# two logical lines in the same physical line
i =5; print(i)

# f-strings format (python 3.6)
print(f'{1.0/3:.3f}')

name = 'bob'
age = 30
print(f'his name is {name} and he is {age} years old')
print(f'''his name is {name.upper()}
and he is {2 * age} years old''')


'''
output:

<built-in function print>
my grade on programming was 10 
everybody was graded 10 on that exercise
0.333
___hello___
Swaroop wrote A Byte of Python
abc
first line
second line	tab
first line second line
new lines are indicated by \n
5
0.333
his name is bob and he is 30 years old
his name is BOB
and he is 60 years old
'''