# Example1: Variable outside of a function
x = "Awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# Example2: Variable inside a fucntion

x = "Awesome"


def myfunc():
    x = "fantastic"
    print("Python is a " + x)


myfunc()

print("Python is " + x)

# Normally, when you create a variable inside a function,that variables is local, and can only be used inside that function

# To create a global variable inside a function, you can use the "global" keyword


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


# To change the value of a global variable inside a function, refer to the variable buy using the "global" keyword
x = "Awesomwe"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
