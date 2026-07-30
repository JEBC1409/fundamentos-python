# Contador de palabras
frase = input("ingresa una frase")
frasSplit = frase.split()
print(f"la frase tiene {len(frasSplit)} palabras ")


# Generador de email
nom = input("Ingresa tu nombre:  ")
apellido = input("ingresa tu apellido")
print(f"{nom.lower()}.{apellido.lower()}@empresa.com")

# invertir una lista

lista = [1, 2, 3, 4, 5]
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Explicación
"""" 
lista = {1,2,4,5}

posicion: 0 1 2 3 4 
valor:    1 2 3 4 5

para leer necesitamos leer de atras hacia adelante
es decir posicion: 4,3,2,1,0

range() acepta 3 argumentos range(inicio,fin,paso)

range(4,-1-,-1):
inicio: 4 (ultima posicion)
fin: -1(para antes de -1, o sea llega hasta 0)
paso: -1 resta (-1 en cada vuelta)
genera: 4,3,2,1,0


"""

# Frecuencia de palabras
# Pide un texto al usuario
# Cuenta cuantas veces aparece cada palabra
# Usa un diccionario: {"hola": 2, "mundo": 1}
# Pista: split() + for + diccionario

texto = input("ingresa un texto: ")
palabras = texto.split()

frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)
