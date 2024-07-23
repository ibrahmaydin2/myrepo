#Create a variable outside of a function, and use it inside the function
x = " is a language"

def myFunc():
    print("Python" + x)

myFunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)

myFunc()

print("Python is " + x)

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

#If you use the global keyword, the variable belongs to the global scope:

def myFunc():
    global x
    x = "Fantasticc"

myFunc()

print("Python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myFunc():
    global x
    x = "FANTASTIC"

myFunc()

print("Python is " + x)