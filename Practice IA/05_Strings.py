# 01) Pedir al usuario un nombre y su ciudad. imprirmi mensaje --> nombre, ciudad

nombre = input("Ingresa tu nombre: ")
ciudad = input("Ingresa la ciudad donde vives: ")

print(f"Hola {nombre}, vives en {ciudad} y tu nombre tiene {len(nombre)} letras ")


# 2) slicing dad la variable

palabra = "programación"
print(palabra[-4])
print(palabra[8:])
print(palabra[::-1])


# 3) Métodos de String
frase = " hOla mUnDo dEsDe pyTHon "
print(frase.strip(" "))
print(frase.lower())
print(frase.upper())
print(frase.lower().count("o"))

cleaned = frase.strip().lower()
print(cleaned.startswith("hola"))


# 5 DESEMPAQUETADO
codigo = "ABC123"
a, b, c, d, e, f = codigo

letras = ""
numeros = ""

for caracter in codigo:
    if caracter.isalpha():
        letras += caracter
    elif caracter.isnumeric():
        numeros += caracter

print(f"Letras: {letras}")
print(f"Números: {numeros}")


# Cifrado
palabra = "hola"
cifrada = ""

for letra in palabra:
    nueva = chr(ord(letra) + 1)
    cifrada += nueva

print(f"Original: {palabra}")
print(f"Cifrada: {cifrada}")
