"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""

#Variables of numeric types are created when you assign a value to them:

x = 1
y = 3
z = 15424
print(type(x))
print(type(y))
print(type(z)) #all data tpes are int

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length

x = 15
y = -1245
z = 12242454664

print(type(x))
print(type(y))
print(type(z))

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals

x = 1.11
y = -1.5
z = 12.12424244

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 31e54
y = -35E114554
z = 25e3

print(type(x))
print(type(y))
print(type(z))

#Complex numbers are written with a "j" as the imaginary part:

x = 1 + 4j
y = 1-5j
z = -15j
q = 56j

print(type(x))
print(type(y))
print(type(z))
print(type(q))


#You can convert from one type to another with the int(), float(), and complex() methods

x = 1 #int
y = -124.41 #float
z = 128j #complex

#convert from int to float:
a = float(x)

#convert from float to complex:

b = complex(y)

#convert from int to complex:

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:
"""

#Import the random module, and display a random number between 1 and 100:

import random

print(random.randrange(1, 101))

#Function example

def myFunc():
    import random
    print(random.randrange(15, 1545))
myFunc()

