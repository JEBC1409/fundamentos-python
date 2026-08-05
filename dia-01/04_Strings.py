### Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea "
print(my_new_line_string)


my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String  \\n escapado"
print(my_scape_string)

# Formateo
name, surname, age = "Brais", "Moure", 19
print("Mi nombres es  {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombres es  %s %s y mi edad es %d" % (name, surname, age))
print(f"Mi nombres es {name} {surname} y mi edad es {age}")


# Desempaquetado de caracteres
languaje = "Python"
a, b, c, d, e, f = languaje
print(a)
print(e)

# Division
languaje_slice = languaje[1:3]
print(languaje_slice)
