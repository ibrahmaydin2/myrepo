#Strings in python are surrounded by either single quotation marks, or double quotation marks.

#'hello' is the same as "hello".

#You can display a string literal with the print() function:

print("Hello")
print('Hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print ("This is Python")
print("This is 'Python'")
print('This is "Python"')

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

x = ("This is Python")
print(x)

#You can assign a multiline string to a variable by using three quotes:
x = """
This is python 
This is Python
Python
"""
print(x)

#Or three single quotes:

x = '''This is python 
This is Python
Python'''
print(x)

"""
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

#Get the character at position 1 (remember that the first character has the position 0):

x = ("Hello")
print(x[1])   #Result = e
print(x[:2])  #Result = He
print(x[1:5]) #Result = ello

#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "Banana":
    print(x)

#To get the length of a string, use the len() function.

x = "Banana" + "Blueberries"
print(len(x)) #Result = 17

#Check if "free" is present in the following text:

x = "Banana" + "Blueberries"
print("Banana" in x) #Resutl = True (Because There is Banana in x)

x = "Banana" + "Blueberries"
print("Watermelon" in x) #Result = False (Because there is no include in x)

#Use it in an if statement:

x = "Banana" + "Blueberries"
if "Banana" in x:
    print("Yes , 'Banana' is in x" )

#Using else:

x = "Watermelon" + "Blueberries"
if "Banana" in x:
    print("Yes , 'Banana' is present" )
else:
    print("No , 'Banana' is'nt present")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in

x = "Watermelon" + "Blueberries"
print("Banana" not in x) #Resutl = True 

#print only if "expensive" is NOT present:

x = "Watermelon" + "Blueberries"
if "Banana" not in x :
    print("No, 'Banana' is not present ") 

#Using else:

x = "Watermelon" + "Blueberries"
if "Banana" not in x:
    print("No, 'Banana' is not present")
else:
    print("No , 'Banana' is present")


