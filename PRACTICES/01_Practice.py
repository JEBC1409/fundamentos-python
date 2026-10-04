#####Number pair and odd#####

number = int(input("Enter a number Here: "))
residual = number % 2

if residual == 0:
    print(f"{number} This is a pair number")
else:
    print(f"{number} this is a odd number")

####Number max ####
numberOne = int(input("Enter a number here: "))
numberTwo = int(input("Enter a number here: "))
numberThree = int(input("Enter a number here: "))

if numberOne >= numberTwo and numberOne > numberThree:
    print(f"Number Max is  {numberOne}")
elif numberTwo >= numberThree:
    print(f"Number Max is {numberTwo}")
else:
    print(f"Number Max is {numberThree}")


####Grade classifier#####
grade = float(input("Enter a Grade Here between 0 - 5: "))

if grade < 3.0 and grade >= 0:
    print("Failed")
elif grade >= 3.0 and grade < 4:
    print("Approved")
elif grade >= 4.0 and grade < 4.5:
    print("Remarkable")
elif grade >= 4.5 and grade <= 5:
    print("outstanding")
else:
    print("incorrect Grade")


###Id program
age = int(input("Enter age Here: "))
hasId = input("Do you have Id ? y/n  Enter s if you have and n if you dont have: ")

if age >= 18 and hasId == "y":
    print("You can come in")
elif age < 18 and hasId != "y":
    print("You are under 18 and you dont have an ID")
elif age < 18:
    print("You are under 18")
else:
    print("you dont hace an ID")


# Gear leap

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
