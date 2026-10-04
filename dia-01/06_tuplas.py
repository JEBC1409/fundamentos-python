## Tuples ###

my_tuple = tuple()
my_other_tuple = ("hola", 12, 12)

my_tuple = (35, 1.77, "Brais", "Moure")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-4]) indexError
# print(my_tuple[-6]) indexError


print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# La tupla no te deja cambiar son valores inmutables
# my_tuple[1] = 1.80
# print(my_tuple)

# Teneniendo en cuenta que es una nueva tupla
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


print(my_sum_tuple[3:6])


my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "MoureDev"
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))
print(type(my_tuple))


del my_tuple
# print(my_tuple)   no esta definida

# del my_tuple[2]  no definida
