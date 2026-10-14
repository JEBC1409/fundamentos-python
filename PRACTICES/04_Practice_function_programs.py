# Program: request an integer without the program crashing.
# This program combines chapters 3 and 4: a while True loop keeps
# int() raises a ValueError  when the text is not a whole number,
# and except catches it. The return inside the loop ends both the
# loop and the function
def ask_integer(message):
    while True:
        text = input(message)
        try:
            return int(text)
        except ValueError:
            print("Escribe un número entero, por ejemplo 5")


age = ask_integer("Tu edad: ")
print(f"Tienes {age} años")
print(" ")

# Program: functions calling functions
# Think of functions as black boxes: parameters go in, a return
# value comes out, and their local variables never leak. Here one
# function calls another, and every path throught teh code ends
# in a return


def shipping_cost(weight_kg):
    if weight_kg <= 1:
        return 5000
    elif weight_kg <= 5:
        return 12000
    else:
        return 20000


def order_total(price, weight_kg):
    return price + shipping_cost(weight_kg)


print(order_total(40000, 0.5))
print(order_total(40000, 3))
print(order_total(40000, 10))


def add_tax(price):
    total = price * 2
    return total


print(add_tax(100))
