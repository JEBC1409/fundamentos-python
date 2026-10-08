##Functions

# A function is a mini program inside your program. The def statement
# defines it, which only creates it. The code in its body runs later,
# each time you call it by writing its name followed by parentheses


def print_welcome():
    print("Bienvenido a la tienda")
    print("Hoy hay descuentos")


print_welcome()
print_welcome()
print("")


# Parameters and arguments

# A function can receive values.The Values you pass in the call are
# arguments.They are stored in variables called parameters, which
# exist only while the functions runs. When the function returns,
# those variables are fotgotte


def greet_customer(name):  # name es el parametro
    print(f"Hola, {name}")
    print(f"gracias por comprar, {name}")


greet_customer("Ana")  # "ana" es el argumento
greet_customer("Luis")
# print(name)                    'name' is not defined
print("")


###return
# The value that a function call evaluates to is its return value.
# You set ir with a return statement. Because a call evaluates to
# a value, you can use it inside any expression.A return also ends
# functio inmediately


def add_shipping(price):
    return price + 5000


total = add_shipping(20000)
print(total)  # 25000
print(add_shipping(10000) + add_shipping(1000))  # 110000 + 6000 -> 21000


def is_adult(age):
    if age >= 18:
        return True
    return False


print(is_adult(20))  # True
print(is_adult(10))  # False
print(" ")


# None
# None represents the absence of value.It is the only value of the
# NoneType  type, and it is always written with a capital N.
# Python adds an invisible return None to the end of every function
# that has no return. Even print() returns None.

result = print("hola")  # imprime: hola
print(result)  # None
print(result == None)  # True


def double_it(x):  # calcula, pero nunca devuelve
    y = x * 2


print(double_it(5))  # None -> ¡el 10 se perdió! no hay return
print(" ")

##Named Arguments: sep and end
# Most argument are identified by their position: random.randint(1,10)
# is not teh same as random.randint(10,1).Others are identified by a
# by a name, like the optional sep and end of print(). These are
# called named (or keyword) arguments.

print("gatos", "perros", "ratones")  # gatos, perros, ratones
print("gatos", "perros", "ratones", sep=" ")  # gatos,perros,ratones

print("Cargando", end="...")  # no salta de linea
print("listo")  # cargando...Listo

for i in range(5):
    print(i, end=" ")
print()


# Call Stack
# The call stack is how python remembers where to return after each
# function call. Every call adds a frame on top of the strack.
# when a function returns, its frame is removed and the execution
# goes back to the line that called it, The frame at the top is
# the function  that is running right now


def apply_discount(price, percent):
    print(" apply_discount empieza")
    result = price - price * percent / 100

    print(" apply_discount termina")
    return result


def checkout(price):
    print("checkout empieza")
    final = apply_discount(price, 10)
    print(f"checkout total: {final}")
    print("checkout termina")


checkout(200)
print("fin")
print(" ")

# local and global reach
# variables created inside a function live in its local scope:a new
# one is created at every call and destroyed when the function returns-
# Variables created outside all functions live in the global scope,
# wich exists for the whole program.Code in the global scope cannot
# see local variables, and one function cannot see anothe  function´s local


def calculate():
    discount = 10  # Variable local
    print(discount)


calculate()
# print(discount)


tax_rate = 19  # variable global


def show_rate():
    print(tax_rate)  # solo la LEE: usa la global


show_rate()  # 19


def first():
    note = "desde first"  # cada funcion tiene su propio 'note'
    second()
    print(note)  # desde firt


def second():
    note = "desde second"
    print(note)


first()
