#####IF-ELSE FLOW CONTROL#####

# Unlike int, float or str, el tipo bool solo tiene dos posibles valores
# True y False they´re writteen with a capital letter and neve go int
# quotes

is_raining = True
is_sunny = False

print(is_raining)
print(is_sunny)

# Comparation  Operators
# ==,!=,<,> <=,>=. They take two values and always evaluated down to a Boolean.
# A number is never equal to a string with the same digits - only to another number.

age = 20
print(age == 20)
print(age != 19)
print(age < 19)
print(age >= 18)
print(age == "42")
print(42 == 42.0)
print()
print()

# No confundir comparacion con asignacion,
# Is so diffrent when i write the word assignament == 2
# to when i decide to have comparative between two things
#  age == 29 ?

######Values Operators#####
# and, or and not combine or invert Boolean values.

age = 20
has_id = True

print(age >= 19 and has_id)  # True only if both sides are True
print(age >= 18 or has_id)  # True if least one side is True.
print(not has_id)  # flips the value


#####Condition and Block######
# A condition is an expression that evalues to True or False.
# A block is the indented code that runs depending on it - indentation
# is´nt cosmetic in python, it´s how the interpreter know where a block
# starts and ends
age = 15

if age >= 18:
    print("Eres mayor de edad")  # Inside Block if

print("Fin del programa")  # Out Block iF (its not indented)
# finished the program


####if/elif/else####
# if condition: runs its block only whem  True. An Optiional
# else: runs when its False.elif chains more conditions, checked
# only if the previous ones failed

Age = 15

if age < 13:
    print("Eres niño")
elif age < 18:
    print("Eres adolescente")
else:
    print("eres adulto")

print()
print()
# Out: youre teenager

# The order is so important
age = 70

if age > 100:
    print("eres longevo")
elif age > 60:
    print("Eres mayor ")
elif age > 18:
    print("Eres adulto")

print()
print()

####Bug Logic####
# A program that sets a Boolean, then flips it with not - proof that nesting
# proof that nesting several if statements can cancel itself out.
# The outpot never changes no matter the starting value.
is_monday = True

if is_monday == True:
    has_meeting = True
else:
    has_meeting: False

if is_monday == True:
    has_meeting = not has_meeting  # bug intentional

if has_meeting == True:
    print("Hay reunion hoy")
else:
    print("No hay reunion hoy")

# Output: No hay reunion hoy
# Try to chenge is_monday = False: the result not change


######The NameError ######
# A classic trap: an if/elif chain with no final else. if no conditions matches
# a variable you needed later is never created - Python only tells you once it tries
# to use it

membership = input("Tupo de membresia(gold/silver)")

if membership == "gold":
    discount = 0.20
elif membership == "silver":
    discount = 0.10

# if you write something , "disount" never has created

price = 100
final_price = price - (price * discount)
print(final_price)


###Correction####
membership = input("Tipo de membresía (gold/silver): ")

if membership == "gold":
    discount = 0.20
elif membership == "silver":
    discount = 0.10
else:
    print("Membresía no reconocida, no se aplica descuento")
    discount = 0.0

price = 100
final_price = price - (price * discount)
print(final_price)
