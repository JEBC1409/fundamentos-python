"""String: Secuencia de caracteres"""

nombre = "Julian"
print(nombre[0])
print(nombre[-2])
print(len(nombre))

texto = " Hola mundo "

print(texto.strip())  # quita los espacios al inici y al final
print(texto.lower())  # Minuscula
print(texto.replace("Hola", "Chao"))  # Chao mundo
print(texto.upper())  # Mayuscula
print(texto.find("Mundo"))  # Posisicion donde empieza ( 0 -1 si no existe)
print(texto.count("o"))  # cuantas veces aparece

# split: convierte string en lista
frase = "uno,dos,tres"
print(frase.split(","))  # ["uno-dos-tres"]

# join: convierte lista en string
lista = ["uno", "dos", "tres"]
print("-".join(lista))  # "uno-dos-tres"


"""F-strings"""
nombre = "Julian"
nota = 4.567

print(f"Hola mundo {nombre}")
print(f"Nota: {nota:2f}")
print(f"'Titulo':^20")
print(f"Resultado:{5 + 3}")

# Slicing
texto = "Python"

# P y t h o n
# 0 1 2 3 4 5

print(texto[0:3])
print(texto[2:])
print(texto[:4])
print(texto[::-1])

"""Listas"""

# Una lista es como un string pero puede guardar cualquier cosa y puede ser modificada

notas = [4.5, 3.8, 4.2, 5.0]

print(notas[0])  # 4.5 - primer elemento
print(notas[-1])  # 5.0 ultimo elemento
print(notas[1:3])  # [3.8,4.2] - slicing funciona igual
print(len(notas))  # 4

# Metodos Esenciales de vistas
notas = [4.5, 3.8, 4.2, 5.0]

print(notas.append(5.0))  # Agregar al final
print(notas.insert(1, 30))  # inserta en posicion 1
print(notas.pop())  # elimina y retorna el ultimo
print(notas.pop(0))  # elimina y retoma el de posiicion 0
print(notas.sort())  # ordena de menor a mayor
print(notas.reverse())  # invierte el orden
# print(notas.index(4.5))  # posicion donde esta 4.5
print(notas.count(4.5))  # cuantas veces aparece

"""List Comprehensions"""
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)

# forma corta
cuadrados = [i**2 for i in range(5)]  # [0, 1, 4, 9, 16]
print(cuadrados)

# con condicion
pares = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]
print(pares)
