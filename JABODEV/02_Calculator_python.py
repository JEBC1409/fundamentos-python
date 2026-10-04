# 3.1.1 Números

# Basics + - *
print(2 + 2)

print(50 - (5 * 6))

print((50 - 5 * 6) / 4)

# floor division
print(8 / 5)  # floor division discards the fractional part
print(17 // 3)  # floor division discards the fractional part
print(17 % 3)  # the % operator returns the remainder of the division
print(5 * 3 + 2)  # floored quorient * divisor + remainder

##Calculador de potencias
print(5**2)  # 5 squared
print(2**7)  # 2 to the power of 7


# used = assignament a value a variable
width = 20
heigth = 5 * 9
print(width * heigth)


# variable no defitnily give a error
# n  try to accesan undefined variable

# it  offers full support  for floating - point  numbers

print(4 * 3.75 - 1)

# in the interactive mode last expression print is aasigned to varibale
# When using  python, it is  easier to continue  calculating
tax = float(input("Introduce  the value of the Tax in Value float example: 0.10  "))
price = float(input("Introduce the value of price the product"))

value_taxes = tax * price

total = price + value_taxes

print(
    f"The value of producti is{price}   The value of the taxes is: {value_taxes}    and te sum it is :  {round(total, 2)}"
)
