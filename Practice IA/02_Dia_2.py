# Clasificar Edad:

edad = int(input("ingresar edad en años"))

if edad <= 0:
    print("edad no valida")
elif edad > 0 and edad <= 12:
    print(f"{edad}   Años Clasificacion: Niño")
elif edad > 12 and edad < 18:
    print(f"{edad}  Años Clasificación: Adolescente")
elif edad >= 18 and edad < 60:
    print(f"{edad}  Años Clasificación: Adulto")
else:
    print(f"{edad}  Años  Clasificación: Adulto Mayor")

# Calificacíon por notas:
nota = float(input("Ingresa la nota de 1 a 5"))

if nota < 0 or nota > 5:
    print("nota invalida")
elif nota < 3.0:
    print("Reprobado")
elif nota >= 3.0 and nota <= 3.9:
    print("Aprobado")
elif nota >= 4.0 and nota <= 4.5:
    print("Sobresaliente")
else:
    print("Excelente")

# El mayor de 3 numeros

num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Tercer numero: "))

# cuestiono empate con claude
if num1 >= num2 and num1 >= num3:
    print(f"El mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El mayor es {num2}")
elif num3 >= num1 and num3 >= num2:
    print(f"El mayor es {num3}")


# numero par o impar


numero = int(input("ingresa un numero"))

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")


# año bisiesto

anio = int(input("ingresa un año"))

# forma 1
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"el año {anio} es bisiesto")
else:
    print(f"el año {anio} no es bisiesto")
