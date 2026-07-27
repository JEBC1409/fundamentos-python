num1 = float(input("ingresa el primer numero"))
num2 = float(input("ingresa el segundo numero"))

print(f"Suma: {num1+num2}")
print(f"Resta: {num1-num2}")
print(f"Multiplicacion {num1*num2}")
print(f"Potenciacion: {num1**num2}")
if num2 != 0:
    print(f"division entera: {num1//num2}")
    print(f"division: {num1/num2}")
    print(f"modulo: {num1%num2}")
else:
    print("!No es posible dividir entre 0¡")
