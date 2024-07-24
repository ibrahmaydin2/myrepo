"""
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""

#Integers:

x = int(1)
y = int(1.3)
z = int(-15.4)
q = int("22")

print(x)
print(y)
print(z)
print(q)

#Strings:

x = str("s124d")
y = str(15)
z = str(555)

print(x)
print(y)
print(z)