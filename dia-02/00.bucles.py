# for: sabemos la cantidad de veces
for i in range(5):
    print(i)


# range la variable toma calor y el bloque indentado se ejecuta
range(5)  # empieza en 0 , para antes de 5
range(1, 6)  # empieza en 1, para antes del 6
range(0, 10, 2)  # De 0 a 9, saltando de 2 en 2


# Tambien podemos recorrer una lista o String
for letra in "Hola":
    print(letra)


frutas = ["Manzana", "pera", "uva"]
for frutas in frutas:
    print(frutas)


# While cuando no sabes cuantas veces, pero sabes cuando parar
contador = 0
while contador < 5:
    print(contador)
    contador += 1


# brake:Control de flujo
for i in range(10):
    if i == 5:
        break
    print(i)


# Continue: salta la siguiente vuelta
for i in range(5):
    if i == 2:
        continue
    print(i)


"""Ejemplo"""
# sumar numeros hasta que el usuario escriba 0
total = 0
while True:
    num = int(input("ingrese un numero"))
    if num == 0:
        break
    total += num  # total = total + num
print(f"Total: {total}")
