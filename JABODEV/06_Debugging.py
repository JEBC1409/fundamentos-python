##### Debugging
# Python raises an exception whenever it tries to run invalid
# code, and you cam raise your own too.A raise statement means:
# "stop running this code and jump to the except clause". If nothing
# catches it, the progra, crashes and shows the message. Usually the
# function contains


def set_age(age):
    if age < 0:
        raise Exception("la edad no puede ser negativa: ")
    return age


try:
    print(set_age(20))
    print(set_age(-5))
    print(set_age(30))
except Exception as err:
    print("Ocurrio un problema: " + str(err))


##Assert: comprobación de cordura
# An assertion is a sanity check, assert condition says "I claim this is True"
# ; if not; tehre is a bug, so stop inmediayely". if the condition is false, python
# raises an AssertionError. Unlike normal exceptions, you should not catch
# assertions with try/except: the program should crash, so you notice the bug close
# to its cause ("failiing fast")
discount = 0.25
assert discount >= 0 and discount <= 1, "el descuento debe estar entre 0 y 1"
# la condicion es True: no pasa nada

discount = 0.8
assert discount >= 0 and discount <= 1, "El descuento debe estar entre 0 y 1"
# AssertionError: El descuento debe estar entre 0 y 1


###logging: es el rastro de migajas de pan
# logging is a record of message that show whem the program reached a
# a certain point and what the variables held. is the organized version
# of putting print() calls in your code, To use it, import  the logging module
# and configure it once at the top with  basicConfig().Log messages are for
# the programmer; messages the user should see still belong in print()


import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def sum_to(n):
    logging.debug(f"Empieza sum_to({n})")
    total = 0
    for i in range(1, n):  # bug: no incluye n
        total += i
        logging.debug(f"i vale {i}, total vale {total}")
    logging.debug(f"Termina sum_to({n})")
    return total


print(sum_to(4))  # imprime 6, pero debería ser 10


##Los cincos niveles de log
# loggin levels let yot categorize messages by importance. There are five
# from least to most important: DEBUG, INFO,WARNING,ERROR and CRITICAL
# when  you set a level, you see that level and everything above it, and
# the lower ones are hidden

# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical


# El depurador y sus botones
# A debugger runs your program one line at a time and waits
# for you after  each one. It is slower than a normal run,
# but you can see the real values of the variables instead
# of guessing them from the code.
# A breakpoint marks a line where the debugger must pausea; until
# it  gets there, the program runs at normal speed

# Reto: caza los bugs
# The earlier you catch a bug, the easier ir is to fix. This small
# game has more than one bug.Run it several times, write down what goes
# wrong, and use tools fomr this chapter to find teh cause of each one
"""""
import random

guess = ""
while guess not in ("par", "impar"):
    guess = input("¿El dado saldrá par o impar? ")

roll = random.randint(1, 6)
if roll % 2 == 0:
    result = "par"
else:
    result = "impar"

if roll == guess:
    print("¡Ganaste!")
else:
    print("Perdiste")
print("Salió " + roll)

""" """"""

##Corrección


import random

guess = ""
while guess not in ("par", "impar"):
    guess = input("¿El dado saldrá par o impar? ").lower()


roll = random.randint(1, 6)
print(roll)
if roll % 2 == 0:
    result = "par"
else:
    result = "impar"

if result == guess:
    print("¡Ganaste!")
else:
    print("Perdiste")

print(f"salio {roll}")
