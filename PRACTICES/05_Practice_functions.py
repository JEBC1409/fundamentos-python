##Par
def is_even(number):
    return number % 2 == 0


print(is_even(4))
print(is_even(7))
print(is_even(0))

total = 0
for i in range(1, 101):
    if is_even(i):
        total += i


print(f"El total de numeros pares es {total}: ")
print("")

##Price


def add_tax(price, rate):
    return round(price + price * rate / 100, 2)


print(add_tax(100000, 19))  # 119000.0
print(add_tax(50000, 0))  # 50000.0
print(add_tax(99.99, 19))  # 118.99
print(" ")


# Max
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3


print(max_of_three(1, 2, 3))
print(max_of_three(1, 9, 3))
print(" ")

# Function Grade


def classify_grade(grade):
    if grade < 0 or grade > 5:
        return "Invalid"
    elif grade < 3:
        return "Failed"
    elif grade < 4:
        return "Approved"
    elif grade < 4.5:
        return "Remarkable"
    else:
        return "Outstanding"


print(classify_grade(0))  # Failed
print(classify_grade(3.95))  # Approved
print(classify_grade(4.5))  # Outstanding
print(classify_grade(7))  # Invalid
print(classify_grade(-1))  # Invalid


# ask number
def ask_number(message):
    while True:
        text = input(message)
        try:
            return float(text)
        except ValueError:
            print("Eso no es un número, intenta de nuevo")


price = ask_number("Precio: ")
print(f"El precio es {price}")
