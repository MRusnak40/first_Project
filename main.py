from itertools import filterfalse
from xmlrpc.client import boolean

"""
First code"
# used if input and print


first_name = str(input("Enter your first name: "))
# food=str(input("What is your favorite food?"))


print(f"Hello {first_name}")
# print(f"You like {food}")


age = int(input("age "))
is_Old_enough = boolean

if age < 18:
    is_Old_enough = False
    print("Old enough is", 18)

elif age >= 18:
    is_Old_enough = True


if is_Old_enough:
        print("you can buy alcohol")

else:
    print("Too young")




########################################
# calculate sqare area of a rectangle






lenght = float(input("Enter the lenght of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = lenght * width


print(f"The area of the rectangle is {area}")






##############################################
# calculator 




isFinished = False

while not isFinished:

    number1 = float(input("Enter the first number:"))
    number2 = float(input("Enter the second number:"))
    operator = input("Enter + or - or * or /:")

    if operator == "+":
        result = number1 + number2
        print(result)
    elif operator == "-":
        result = number1 - number2
        print(result)
    elif operator == "*":
        result = number1 * number2
        print(result)
    elif operator == "/":
        result = number1 / number2
        print(round(result, 2))
    else:
        print("Invalid operator")

    continue_calc = input("Do you want to continue? (yes/no): ")
    if continue_calc.lower() != "yes":
        isFinished = True
    else:
        isFinished = False


print("Thank you for using the calculator")



#############################################
#Converter from kg to lb and vice versa



unit = input("Enter to witch unit to convert (kg, lb): ")

if unit == "kg":
    set_to_Convert = "Lbs"
elif unit == "lb":
    set_to_Convert = "Kgs"



weight = float(input(f"Enter weight in {set_to_Convert}: "))

if unit == "kg":
    unit = "Kgs."
    print(f"Your weight in kilograms is {round(weight / 2.20462, 1)} {unit}")

elif unit == "lb":
    unit = "Lbs."
    print(f"Your weight in pounds is {round(weight * 2.20462, 1)} {unit} ")

else:
    print("Invalid unit")
    
    
    ########################################################
# check if a number is positive or negative


number = int(input("Enter a number: "))

isBig=True if number>=0 else False

if isBig:
    print("The number is positive")
else:
    print("The number is negative")

"""

name=input("Enter your name: ")

#shows lenght of text
#lenght_of_name=len(name)


#finds first letter in text
#find_position_of_first_letter=name.find("a")
#finds last letter in text
#find_position_of_last_letter=name.rfind("a")

# first letter is uppercase
#name=name.capitalize()

# all is uppercase
#name=name.upper()



# returns True if all characters in the string are digits (0-9), False otherwise
# result=name.isdigit()

# isalpha() returns True if all characters in the string are letters (a-z, A-Z), False otherwise
#name=name.isalpha()

# title() converts the first character of every word to uppercase and the rest to lowercase
#name=name.title()

# counts that char
#result=name.count(" ")
#print(result)