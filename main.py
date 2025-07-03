import random
import time
from importlib.util import source_hash
from itertools import filterfalse

from operator import index
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

######################################################


#checking name 
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


###############################

credit_number="1850-855-54452-4554"

print(credit_number[0:4])
print(credit_number[4:])

####################
# price formating

price1 = 3.21849
price2 = -5447.25
price3 = 12.36

print(f"price is {price1:.2f}")
print(f"price is {price2:2f} ")
print(f"price is {price3:.2f}")

####################################################
#FOOD  and list of prices

import random

foods = [input("Enter your favorite food: ") for i in range(3)]
prices = [random.randint(50, 100) for i in range(3)]
total_price = 0

list_of_products = []


for food, price in zip(foods, prices):
    print(f"You like {food} and it costs {price}")
    products_dict = {"food": food, "price": price}
    total_price += price
    list_of_products.append(products_dict)

print(list_of_products)
print(total_price)


###############################################################

list_of_shoppers= []

for x in range(2):
    name=input("Enter your name: ")
    card=input("Enter your credit card number: ")


    shopper={"name":name , "card":card}
    list_of_shoppers.append(shopper)



for shopper in list_of_shoppers:

    print(str(list_of_shoppers.index(shopper)+1)+f". name: {shopper['name']}"+" "+f" credit card: {shopper['card']}")

    time.sleep(1.5)
    #########################################################
#quiz


qestions=("What is your name?",
          "What is your age?",
          "What is your favorite food?")


options=(("Matyas","Karel","Pepa"),
         ("18","19","20"),
         ("Pizza","Burger","Spaghetti"))


answers=("Matyas",
         "18",
         "Pizza")

guess=[]
score=0
question_number=0

for qestion in qestions:

    print(qestion)

    print(f"Choose one of the following:{options[question_number]}")
    answer=input("Enter your answer: ")

    guess.append(answer)
    question_number+=1

question_number=0
for guessis in guess:

    if guessis==answers[question_number]:
        score+=1

    question_number+=1



if score==3:
    print("You win!")
elif score==2:
    print("You got one more chance!")
else:
    print("You lost!")
    print(f"The correct answers were: {answers}")
    print(f"Your answers were: {guess}")
    print(f"Your score was: {score}")
    


################################################################
#Founding mines
found_mines = 0
points = 0
while found_mines < 4:
    mines = 0

    mine_hidden = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

    while mines < 4:
        print(f"Add mines on map and let your friend find it: {mines}")
        print("mine 1 /no mine 0")
        print(mine_hidden)
        for row in range(len(mine_hidden)):
            for col in range(len(mine_hidden[row])):

                print(f"position {row}  seznam {col}")


                mine_hidden[row][col] = int(input("Enter your answer: "))

                print(" ")
                print(mine_hidden)

        for row in mine_hidden:
            for col in row:
                if col == 1:
                    mines += 1

    print(" ")
    print(" ")
    print(" ")
    print("lets play")
    time.sleep(2)
    print(" ")
    print(" ")

    while mines > 0:
        print(f"You have {mines} mines left in the map.")
        x = int(input("position X "))
        y = int(input("position Y "))

        if mine_hidden[x][y] == 1:
            print("Died")
            print(" ")
            break

        elif mine_hidden[x][y] == 2:
            points += 1
            mines -= 1
            found_mines += 1
        print("DIDNT STEP ON ONE")
####################################################
# shops and shopper

list_of_shoppers = {}

while len(list_of_shoppers) < 1:
    name = input("Enter your name: ")

    while len(name) > 12:
        print("Too long")
        name = input("Enter your name: ")

    card = input("Enter your credit card number: ")

    while card.isdigit() is False:
        print("Enter a valid credit card number")
        card = input("Enter your credit card number: ")

    status = None
    while status is None:
        print("offline/online")
        status = input("Enter your status: ")

        if status == "offline" or status == "online":
            status = status
        else:
            print("Enter a valid status")
            status = None

    payments = {}
    shopper = {"name": name, "card": card, "status": status, "payments": payments}

    list_of_shoppers.update({name: shopper})
    print(f"shopper was added: {shopper}")

print("----------------------------------")
print(" ")
print(" ")
print("List of shoppers:")

for item in list_of_shoppers.items():
    print(item, end="\n")
    print(" ")

running = True
shopping_list = {"Apple": 25,
                 "Android": 70,
                 "Nokia": 2,
                 "Huaway": 30}
list = {}
total_price = 0

while running:
    print("------Shop-----")
    for key, value in shopping_list.items():
        print(f"{key:5}: ${value:.2f}", end="\n")
    print("----------")

    electrotechnics = input("Enter your electrotechnics: ").capitalize()
    if electrotechnics == "Q":
        running = False
        break
    elif electrotechnics in shopping_list.keys():

        print(f"Added on shopping list {electrotechnics:3}  ${shopping_list[electrotechnics]:.2f}")
        list.update({electrotechnics: shopping_list[electrotechnics]})
    else:
        print("NONE existing in list")
        continue

print("-----shopping list-----", end="\n")
for key, value in shopping_list.items():
    print(f"{key:5}: ${value:.2f}", end="\n")

print("LOADING", end="")
for x in range(5):
    print(".", end="")
    time.sleep(1)
##################################################################################


def set_name(name, second_name):
    if any(char.isdigit() for char in name) is False and any(char.isdigit() for char in second_name) is False:
        person = {"name": name, "second name": second_name}
        return person
    else:
        print(f"Name contains digits: {name}", end=" ")
        print(f"or second name contains digits: {second_name}")
        return None


list_of_people = []

while len(list_of_people) < 1:

    list_of_people.append(set_name(name=input("Enter your name: ").capitalize(),
                                   second_name=input("Enter your second name: ").capitalize()))

    for person in list_of_people:
        if person == None:
            list_of_people.remove(person)
            print("Try again")
    print(f"List of people {list_of_people}")

print(f"Thank you for login {list_of_people[len(list_of_people) - 1]["name"]}  {list_of_people[len(list_of_people) - 1]["second name"]} ")

def countiung(ints):
    print(f"zadal jsi cislo {ints} dostupne funkce", end="\n")
    print("Scitat",end="\n")
    print("Odcitani",end="\n")
    print("Nasobeni",end="\n")
    print("Deleni",end="\n")


def alhpa(strs):
    print(f"Zadal jsi text {strs}", end="\n")
    print("Muzes s tim delat", end="\n")
    print("Spojit do jednoho", end="\n")
    print("Vypsat", end="\n")


#chyba ze nepocitam ze arg je nejaka mnozina cisel
def income(*args):
    for incomes in args:

        if type(incomes) is  str or type(incomes) is int:
            if incomes.isdigit():
                print("CISLO")
                countiung(incomes)

            elif incomes.isalpha():
                print("TEXT")
                alhpa(incomes)


income(input("Enter your income: "),input("Enter your income: "))
#######################################
#encription

import string
import random

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

# ENCRYPT
plain_text = input("Enter your plain text:")
cipher_text = ""

for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]

print(f"cipher text:{cipher_text}")
print(f"plain text:{plain_text}")
print(" ")

cipher_text = input("Enter your cipher text:")
plain_text = ""

for char in cipher_text:
    index = key.index(char)
    plain_text += chars[index]

print(f"cipher text:{cipher_text}")
print(f"plain text:{plain_text}")
#######################################################
#hangman

from words import wordslist
import random

words = ("nigga", "rizz", "skibidi", "ohio")+wordslist

# dictionary of key:()
hangman_art = {0: ("   ----",
                   "    ",
                   "    ",
                   "    ",
                   "   ----",
                   "    "),
               1: ("   ----",
                   "    O  ",
                   "    ",
                   "    ",
                   "   ----",
                   "    "),
               2: ("   ----",
                   "    O  ",
                   "    |  ",
                   "    ",
                   "   ----",
                   "    "),
               3: ("   ----",
                   "    O  ",
                   "   /|\\",
                   "    ",
                   "   ----",
                   "    "),
               4: ("   ----",
                   "    O  ",
                   "   /|\\",
                   "   /  ",
                   "   ----",
                   "    ",),
               5: ("   ----",
                   "    O  ",
                   "   /|\\",
                   "   / \\",
                   "   ----",
                   "    ",),
               6: ("   ----",
                   "    O  ",
                   "   /|\\",
                   "   /'\\",
                   "   ----",
                   "GAY OVER"), }


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print("HINT->", end=' ')
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    while True:
        answer = random.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters_list = set(" ")
        isRunning = True
        display_man(wrong_guesses)
        while isRunning:

            display_hint(hint)
            print(f"Guessed letters: {guessed_letters_list}")
            if wrong_guesses == len(hangman_art) - 1:
                break
            print(" ")
            guessed_letters = input("Guess letter:").lower()
            print(" ")

            if len(guessed_letters) == 1 and guessed_letters not in answer:
                guessed_letters_list.add(guessed_letters)


            if guessed_letters in answer and len(guessed_letters) == 1:

                for i in range(len(answer)):
                    if answer[i] == guessed_letters:
                        hint[i] = guessed_letters

            elif guessed_letters == answer:
                index = 0
                for x in guessed_letters:
                    hint[index] = x
                    index += 1

            else:
                print(" ")

                print("Wrong guesses!")
                print(" ")
                wrong_guesses += 1

            display_man(wrong_guesses)

            founded = False
            for x in hint:

                if x == "_":
                    founded = True

            if not founded:
                display_hint(hint)
                print(" ")
                print("*****************")

                print("You won ")
                print("*****************")
                break
        print(" ")
        print("CONTINUE?")
        match input("Q to quit anything else continue:").lower():
            case "q":
                break
            case _:
                print("  ")

                print("LETS GO!")
                print("  ")
                continue


if __name__ == "__main__":
    print("-----HANGMAN-----")
    print(" ")
    print("WELCOME TO HANGMAN")
    print(" ")
    main()
"""

