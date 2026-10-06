####LOOPS####

# WHILE --> MIEMTRAS
# Repeat while something is True

# An if checks its condition once and moves on. A while checks it
# condition, runs the block, then jumps back up ande checks again
# it repeats until the condition become False. Each pass through
# the block is called an iteration

counter = 0
if counter < 3:
    print("if: hola")  # Sale una vez
    counter = counter + 1

counter = 0
while counter < 3:
    print("while: hola")  # Sale tre veces
    counter = counter + 1


# The look  keeps asking until the user types the right answerr.


#####While True  ##### --> MIENTRAS SEA VERDAD
answer = ""
while answer != "python":
    answer = input("¿What  languaje do we use for learning?: ")
print("¡Correcto!")


# Break and inifinte loop
# A break statement exits the loop inmediately. While True:Creaye an
# infinite loop on purpose: the condition is always true, so the only
# way put is a break.

while True:
    answer = input("what languaje  do we use for learning ?")
    if answer == "python":
        break
    print("Try again ")
print("¡Correcto!")


# A continue statement skips the rest of the block and jumps
# back back to the start of the loop. The difference with break:
# break leaves the loops for good, continue only abandons the current
# iteration.Both can be used only inside loops

total = 0
while True:
    number = int(input("Number (0 to finishes)"))
    if number == 0:
        break
    if number < 0:
        total = total + number
print(f"total: {total}")

print(" ")

##Truthy and Falsey
# in a condition,0, 0.0 and the empty string '' count as False. Every
# other value count as True. The bool() functions shows you how Python
# sees any value

print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(42))
print(bool("hola"))
print(bool("0"))


##For and Range()

# Use a for loop when you want to repeat a block a know number of times.
# for in in range(5): --> runs the block fives times, with i equal to
# 0,1,2,3 and 4. The range goes up to, but does not include, the number
# you pass

for i in range(5):
    print(f"Vuelta numero {i}")

# Iteration
# lap number 0
# lap number 1
# lap number 2
# lap number 3
# lap number 4


# A very common use case: adding something during each iteration.
# the acumulator variable is created before the loop.Remember
# The 'NameError' from chapter two: if your create it inside the loop
# and the loop doesn´t run; the variable never exist

total = 0
for price in range(1, 6):  # 1,2,3,4,5
    total = total + price
print(total)  # 15

print(" ")
###range() with start, stop  and step
# range() acepts up yo three arguments: start, stop and step.
# the step is how much the counter changes after each iteration,
# and it can be negative to count down

for i in range(2, 6):  # 2,3,4,5
    print(i, end=",")
print(" ")

for i in range(0, 10, 3):  # 0,3,6,9
    print(i, end=",")
print("")

for i in range(10, 0, -2):  ##10,8,6,4 ,2
    print(i, end=",")
print(" ")

print(" ")
# A 'for' loop is a 'while' loop  in disguise
# Anything a for loop with range() does, a while loop can do too:
# yo just manage the counter youserlf. Use for when you know how
# many times to repeat, and while when te repetition
# depends on a condition

# with a 'for' loop
for i in range(3):
    print(i)

##with a 'while' loop
i = 0
while i < 3:
    print(i)
    i = i + 1
print("")
####Import library
##Python ships with a standard library: set of modules, each one
# a group of related functions. You must import a module before
# using its functions, and you call them with the module name in
# front, like random.randint()
import random

for i in range(3):
    print(random.randint(1, 6))

import random, sys

print(" ")
###End program with sys.exit()
# A program normally ends when int reaches its las line.
# Calling sys.exit() ends it earlierm wherever you are.
# it lives in the sys module, so you import first

import sys

while True:
    command = input("Escribe 'salir' para terminar: ")
    if command == "salir":
        sys.exit()  # Termina todo el programa
    print(f"Escribiste: {command}")
