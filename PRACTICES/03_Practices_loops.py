###Sum Numbers pairs###
acum = 0

for i in range(2, 101, 2):
    print(i)
    acum += i

print(f"Numeros pares acumulados hasta 100: {acum}")
print("")

# While

total = 0
number = 1

while number < 101:
    if number % 2 == 0:
        total += number
    number += 1
print(f"Suma de los numeros pares del 1 al 100: {total}")


total = 0
number = 2
while number <= 100:
    total += number
    number += 2


# Agrade point average
total = 0
count = 0

while True:
    note = float(input("Ingresela nota (-1 para Terminar)"))

    if note == -1:
        break

    if note < 0 or note > 5:
        continue

    total += note
    count = count + 1

if count > 0:
    print(round(total / count, 2))
else:
    print("No hay notas")


##Reto

for number in range(1, 31, 1):
    # Un numerp divisible entre 5 y 3, es divisble por 15
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
