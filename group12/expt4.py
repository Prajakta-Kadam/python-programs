# 4. Write a Python program to create a Pythagorean theorem calculator.
from math import sqrt

print('Assume the sides are a, b, c and c is the hypotenuse')
formula = input('Which side (a, b, c) do you wish to calculate? ')

if formula == 'c':
	a = int(input('Input side a: '))
	b = int(input('Input side b: '))

	c = sqrt(a ** 2 + b ** 2)

	print('The length of side c is: ')
	print(c)

elif formula == 'a':
    b = int(input('Input side b: '))
    c = int(input('Input side c: '))

    a = sqrt(c ** 2 - b ** 2)

    print('The length of side a is')
    print(a)

elif formula == 'b':
    a = int(input('Input side a: '))
    c = int(input('Input side c: '))

    b = sqrt(c ** 2 - a ** 2)

    print('The length of side b is')
    print(b)

else:
	print('Please select a side between a, b, c')
