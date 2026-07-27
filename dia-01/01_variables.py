# Variables
# Buenas practicas  a la hora de nombrar variables
My_variable = "My String variable"
print(My_variable)


my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)


print(My_variable, my_bool_variable, str(my_int_variable))

print("Hello world", end=" ")

# Operaciones
print(3 + 2)
print(2 * 5)

x = 5
y = "jhon"

print(x)
print(y)
print(x, y)

"""   CASTING """
x = str(3)  # x will be '3'
y = int(3)  # y will be a 3
z = float(3)  # z will be a 3.0

"""Single Or Double Quotes  IS THE SAME"""
# Example
name = "jhon"
name2 = "jhon"
print(name, name2)

""" Variable names are case-sensitive"""
a = 4
A = 3
# A will not overwrite a

"""Multi Words Variable Names"""

# Good practices

# Camel Case = Caso camello
myVariableName = "jhon"

# Pascal Case = caso pascal
MyVariableName = "jhon"

# Snake case = caso serpiente
my_variable_name = "jhon"

"""Many Values to Multiple Variables"""
x, y, z = "orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "orange"
print(x)
print(y)
print(z)

"""Unpack Colletion"""
# if you have a collection in a list, tuple etc.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
