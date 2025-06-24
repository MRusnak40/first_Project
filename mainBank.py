#show balance
import time


def showBalance():
    pass
#vklad
def deposit():
    pass

# vybrat
def withdraw():
    pass
def convert():
    pass

balance = 0
is_running=True

while is_running:
    print("-------Banking program-------")
    print("STARTING",end=" ")

    for x in range(6):
        time.sleep(1)
        print(".",end="")



    print(" ")
    print(" ")
    print("1-FUNCION-")
    print("-------------")
    print("2-Show balance-")
    print("3-Deposit-")
    print("4-Withdraw-")
    print("5-Convert-")
    print("6-Exit-")
    print(" ")

    while is_running:
        match input("Enter what you want: "):

            case "1":
                showBalance()
            case "2":
                deposit()
            case "3":
                withdraw()
            case "4":
                withdraw()
            case "5":
                convert()
            case "6":
                print(" ")
                print("Thank you for using this program")
                print("Closing program",end="")
                for x in range(6):
                    time.sleep(1)
                    print(".",end="")

                is_running=False

            case _:
                print(" ")
                print("Invalid input")
                print("choose 1-6")
                print(" ")
                continue