###program: Guess the number###

import random

secret = random.randint(1, 10)
print("Pensé en un número entre 1 y 10. Tiene 4 intentos")

for attemp in range(1, 5):
    guees = int(input("Tu intento: "))
    if guees < secret:
        print("Muy bajo")
    elif guees > secret:
        print("Muy alto")
    else:
        break  # Acerto sale del for

if guees == secret:
    print(f"¡Ganaste en {attemp} intentos")
else:
    print(f"Perdiste. Era {secret}")


####Program: nested loops with a menu


import sys

total = 0


while True:
    print(f"Total  acumulado: {total}")

    while True:
        option = input("(s)umar 10, (r)estar 10 o (q)uit: ")
        if option == "q":
            sys.exit()
        if option == "s" or option == "r":
            break
        print("Escribe s,r,o q")
    if option == "s":
        total = total + 10
    else:
        total = total - 10
        break
print("")
