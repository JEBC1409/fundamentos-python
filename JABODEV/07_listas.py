#####Lists
# A list is value that contains multiple values in a ordered sequence.
# it begins with [,end with ], abd its items are separated by commas.
# A list can mix types, and [] is the empty list, much like "" is
# the empty string

products = ["arroz", "frijol", "panela", "café"]
numbers = [1, 2, 3]
mixed = ["hola", 3.14, True, None, 42]
empty = []

print(products)  # -> print ["arroz,"frijol","panela","café"]
print(type(products))  # --> <class 'list'>


# Una lista puede escribirse en varias lineas
message = ["Sí", "No", "Tal vez"]
print("")
##Indices y negativos
# the integer inside square brackest after a list is called an index.
# the first item is at index 0, so the last index is the lenght
# minus one. Negative indexes, count  from the end: -1 is the last
# item, Using an index that is toobig raises and IndexError. List can
# contain lists, and you reach inner values with two indexes

products = ["arroz", "frijol", "panela", "café"]

print(products[0])
print(products[3])
print(products[-1])
print(products[-4])
# print(products(4))        indexError: list index out range
print("")

table = [["ana", 4.5], ["Luis", 3.8]]
print(table[0])
print(table[0][0])
print(table[1][1])

# funcionan como matrices
print("")

# Slice: varios elemento a la vez
# An index gets one value; a slice gets several,as new list. A slice
# has two integers separated by a colon.It starts at the first index
# and goes up to,  but does not includem the second one. You can
# leave either side empty: no first index means "from the start",
# no second index means "to the end"

products = ["arroz", "frijol", "panela", "café", "sal"]

print(products[1:3])
print(products[:2])
print(products[2:])
print(products[:])
print(products[0:-1])
print("")

# len, cambiar valores, + y *, del
# len returnd the number of items.You can change an items by assigning
# to its index. The + operator joins two list into  a new list, and *
# repeats a list. The del statement removes the item at an index,
# and everything after it moves ip one position. Augmented assignment
# operators liek += are shortcus for "update this variables using its own
# value"

notes = [3.5, 4.0, 2.8]  # Creación de lista --> notas
print(len(notes))  # len para contar cuantas notas

notes[2] = 3.0  # reemplazo del valor de la nota en la posisicion [2]
notes[-1] = 5.0  # reemplazo del valor de la nota en la ultima posición

print([1, 2] + [3, 4])  # concatenacion de dos listas
print(["x"] * 3)  # multiplicacion de un elemento dentro de la lista

del notes[0]  # Elimina la nota de la  posición [0]
print(notes)

total = 10
total += 5  # igual que  total = total + 5 ya llevaria 15
print(total)
names = ["Ana"]
names += ["Luis"]  # concatena un elemento de la lista con otro que se ingreso
names *= 2  # se duplican los datos  hasta la iteracion
print(names)


# Para qué sirven: ciclos con listas
# without lists you would create one variable per value, and your program
# could never store--> guardar more values than variables. A single list
# can hold any  number of items.Technically, a for loop repeats its block
# once for each item in a list: range(4) behaves like [0,1,2,3]. To get
# both -> para obtener the index and the item, use range(len(list)) or more
# simply, enumerate()

cart = []

while True:
    product = input("Producto (vacio para terminar): ")
    if product == "":
        break
    cart = cart + [product]  # concatenacion de listas

print("Tu carrito: ")
for product in cart:
    print(" " + product)

supplies = ["lapices", "cuadernos", "reglas"]

for index in range(len(supplies)):
    print(f"posición {index}: {supplies[index]}")

for index in range(len(supplies)):
    print(f"posicion {index}: {supplies[index]}")

for index, item in enumerate(supplies):
    print(f"posicion {index}: {item}")

print("")
# in, asignación múltiple y random
# the in and not in operators check whetever a values is in alist an
# give a Boolean.The multiple assignment (tuple unpacking) assings
# several variables from a list one line, but the number of variables
# must match the length of the list. The random modules has choice(),
# which picks a random item, and shuffle(), which reorders a list in
# place

pets = ["Luna", "Max", "Coco"]
print("Max" in pets)  # True
print("Rex" not in pets)  # True

name = input("Nombre de mascotas: ")
if name not in pets:
    print("No tengo una mascota llamada: " + name)
else:
    print(name + "es mi mascota")

print(" ")

product = ["Arroz", 3500, 12]
name, price, stock = product  # asignacion multiple
print(price)  # 3500
print()
# name, price  = product

import random

print(random.choice(pets))
random.shuffle(pets)
print(pets)


##Métodod: index, append, insert, remove
# a method the same thing as a fuction, except it is called on
# a value: fruits.index("lulo"). Each data types has  its own methods
# index() finds a value, append() adds to the end,  insert() adds
# to the end, insert() adds at any index, and remove() deletes the
# first matching value. Adding and removing methods change the list
# and return None.

fruits = ["mango", "lulo", "mora", "lulo"]

print(fruits.index("lulo"))  # 1 (la primera aparición)
# fruits.index("pera")           #valueError: 'pera' is not in list

fruits.append("guayaba")  # al final
fruits.insert(1, "papaya")  # en el indice 1; el resto se corre
print(fruits)  # ['mango', 'papaya', 'lulo', ,'guayaba']

fruits.remove("lulo")
print(fruits)


fruits = fruits.append("pera")  # ¡TRAMPA!
print(fruits)  # None -> perdiste la lista

word = "hola"
# word.append("x")                #AttributeError: 'str' objects has no atributted  'append'
print(" ")


##Sort y reverse, con sus trampas
# the sort method orders a list of a numbers or a list strings.
# three things to remember: it sorts in place an returns None; it cannot
# sort  a list that mixes numbers and string; and it sorts strings in
# "ASCIIbetical" order, so every uppercase letter comes before every lowercase one.
# pass reverse = True  for descending order, or key = str.lower to ignore
# case.reverse() flips the order of the items

prices = [2500, 800, 1200, 300]
prices.sort()
print(prices)  # [300, 800, 1200, 2500]
prices.sort(reverse=True)
print(prices)  # [2500,1200,800,300]

names = ["Zoe", "ana", "Bruno", "carlos", "Zoe"]
names.sort()
print(names)  # ['Bruno', 'Zoe', 'ana', 'carlos']  (mayúsculas primero)
names.sort(key=str.lower)
print(names)  # ['ana', 'Bruno', 'carlos', 'Zoe']

mixed = [3, "a", 1]
# mixed.sort                  #TypeError: no se pueden comparar int y str

queue = ["Ana", "Luis", "Sofía"]
queue.reverse()
print(queue)  # ['Sofía', 'Luis', 'Ana']

result = queue.sort()
print(result)  # None
