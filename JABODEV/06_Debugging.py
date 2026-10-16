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
# logging is a record og message that show whem the program reached a
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
